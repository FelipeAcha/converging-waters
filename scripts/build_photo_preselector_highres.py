#!/usr/bin/env python3
from __future__ import annotations
import argparse, base64, gzip, hashlib, io, json, re, shutil
from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image, ImageOps

QUALITY = 92


def _fetch_source(spec: dict, cache_dir: Path, session) -> tuple[bytes, str]:
    kind = spec.get('kind')
    if kind in ('embedded-cache', 'embedded-file'):
        name = spec.get('file')
        if not name:
            raise RuntimeError(f'{kind} source missing file')
        path = (cache_dir / name).resolve()
        path.relative_to(cache_dir.resolve())
        if not path.is_file():
            raise RuntimeError(f'missing cached source: {path}')
        if kind == 'embedded-cache':
            return base64.b64decode(path.read_text(encoding='ascii').strip()), f'cache:{name}'
        return path.read_bytes(), f'cache:{name}'
    if kind == 'remote':
        url = spec.get('url')
        if not url:
            raise RuntimeError('remote source missing url')
        if session is None:
            raise RuntimeError(f'remote source requires HTTP session: {url}')
        r = session.get(url, timeout=90, allow_redirects=True, headers={
            'User-Agent': 'Mozilla/5.0 (compatible; ConvergingWatersReview/1.0)'
        })
        r.raise_for_status()
        return r.content, url
    raise RuntimeError(f'unsupported source kind: {kind}')


def _read_payload(root: Path) -> tuple[str, list[Path], bytes]:
    parts = sorted((root / 'payload2').glob('*.txt'))
    if not parts:
        raise RuntimeError('payload2 chunks missing')
    b64 = ''.join(p.read_text(encoding='utf-8').strip() for p in parts)
    gz = base64.b64decode(b64)
    return gzip.decompress(gz).decode('utf-8'), parts, gz


def _semantic_snapshot(soup: BeautifulSoup) -> list[tuple[str, str]]:
    out=[]
    for c in soup.select('.candidate'):
        code=c.select_one('code')
        img=c.select_one('img')
        if not code or not img:
            raise RuntimeError('candidate missing code or image')
        img['src']='__IMAGE_SRC__'
        out.append((code.get_text(strip=True), str(c)))
    return out


def build(root: Path, source_manifest: Path, source_cache_dir: Path,
          max_edge: int = 1600, min_edge: int = 700,
          chunk_count: int | None = None, session=None) -> dict:
    root = Path(root).resolve()
    source_manifest = Path(source_manifest).resolve()
    source_cache_dir = Path(source_cache_dir).resolve()
    current_html, parts, old_gz = _read_payload(root)
    if chunk_count is None:
        chunk_count=len(parts)

    current = BeautifulSoup(current_html, 'html.parser')
    before = _semantic_snapshot(BeautifulSoup(current_html, 'html.parser'))
    source_map = json.loads(source_manifest.read_text(encoding='utf-8'))

    candidates=current.select('.candidate')
    codes=[c.select_one('code').get_text(strip=True) for c in candidates]
    if set(codes) != set(source_map):
        missing=sorted(set(codes)-set(source_map)); extra=sorted(set(source_map)-set(codes))
        raise RuntimeError(f'candidate/source mismatch missing={missing} extra={extra}')

    assets_dir=root/'assets'
    if assets_dir.exists(): shutil.rmtree(assets_dir)
    assets_dir.mkdir(parents=True)
    report_assets=[]

    for c in candidates:
        code=c.select_one('code').get_text(strip=True)
        img=c.select_one('img')
        raw, source_label = _fetch_source(source_map[code], source_cache_dir, session)
        with Image.open(io.BytesIO(raw)) as opened:
            im=ImageOps.exif_transpose(opened).convert('RGB')
            ow,oh=im.size
            if max(ow,oh) < min_edge:
                raise RuntimeError(f'{code} source too small: {ow}x{oh}')
            scale=min(1.0, max_edge/max(ow,oh))
            if scale < 1.0:
                im=im.resize((round(ow*scale),round(oh*scale)), Image.Resampling.LANCZOS)
            w,h=im.size
            out=assets_dir/f'{code}.webp'
            im.save(out,'WEBP',quality=QUALITY,method=6)
        img['src']=f'assets/{code}.webp'
        report_assets.append({
            'code':code,'source':source_label,'source_width':ow,'source_height':oh,
            'width':w,'height':h,'long_edge':max(w,h),'bytes':out.stat().st_size
        })

    after = _semantic_snapshot(BeautifulSoup(str(current), 'html.parser'))
    if before != after:
        raise RuntimeError('non-image candidate DOM changed during high-resolution rebuild')

    needs=len(current.select('.need')); controls=len(current.select('input[type=checkbox]')); images=len(current.select('.candidate img'))
    counts={'needs':needs,'candidates':len(candidates),'controls':controls,'images':images,'assets':len(report_assets)}
    if counts != {'needs':18,'candidates':77,'controls':77,'images':77,'assets':77} and len(candidates) != 1:
        raise RuntimeError(f'unexpected selector counts: {counts}')

    payload=str(current).encode('utf-8')
    gz=gzip.compress(payload, compresslevel=9, mtime=0)
    sha=hashlib.sha256(gz).hexdigest(); b64=base64.b64encode(gz).decode('ascii')
    size=(len(b64)+chunk_count-1)//chunk_count
    chunks=[b64[i:i+size] for i in range(0,len(b64),size)]
    while len(chunks)<chunk_count: chunks.append('')
    if len(chunks)>chunk_count: raise RuntimeError('chunk split overflow')

    payload_dir=root/'payload2'; payload_dir.mkdir(exist_ok=True)
    for p in payload_dir.glob('*.txt'): p.unlink()
    for i,chunk in enumerate(chunks):
        (payload_dir/f'{i:03d}.txt').write_text(chunk,encoding='ascii')

    shell_path=root/'index.html'; shell=shell_path.read_text(encoding='utf-8')
    shell2,n=re.subn(r"EXPECTED='[0-9a-f]{64}'", f"EXPECTED='{sha}'", shell, count=1)
    if n != 1: raise RuntimeError('could not update EXPECTED payload hash in shell')
    shell_path.write_text(shell2,encoding='utf-8')

    report={
        'source_manifest':str(source_manifest),'old_payload_sha256':hashlib.sha256(old_gz).hexdigest(),
        'payload_sha256':sha,'quality':QUALITY,'max_edge':max_edge,'min_source_edge':min_edge,
        'counts':counts,'assets':report_assets
    }
    (assets_dir/'manifest.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    return report


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('review_root', type=Path)
    ap.add_argument('source_manifest', type=Path)
    ap.add_argument('source_cache_dir', type=Path)
    ap.add_argument('--max-edge', type=int, default=1600)
    ap.add_argument('--min-edge', type=int, default=700)
    args=ap.parse_args()
    import requests
    report=build(args.review_root,args.source_manifest,args.source_cache_dir,args.max_edge,args.min_edge,session=requests.Session())
    print(json.dumps({'payload_sha256':report['payload_sha256'],'counts':report['counts'],
                      'min_long_edge':min(x['long_edge'] for x in report['assets']),
                      'max_long_edge':max(x['long_edge'] for x in report['assets']),
                      'asset_bytes':sum(x['bytes'] for x in report['assets'])}, indent=2))

if __name__=='__main__': main()
