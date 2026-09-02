#!/usr/bin/env python3
from pathlib import Path
import argparse, base64, gzip, hashlib, json, re

def sha(b): return hashlib.sha256(b).hexdigest()

def decode_payload(root: Path, prefix: str, parts: int) -> bytes:
    chunks=[]
    for i in range(parts):
        p=root/f'{prefix}{i:02d}.txt'
        if not p.is_file(): raise SystemExit(f'MISSING_PAYLOAD_PART {p}')
        chunks.append(p.read_text('utf-8').strip())
    return gzip.decompress(base64.b64decode(''.join(chunks)))

def raw_section(data: bytes, sid: str) -> bytes:
    pat=re.compile(rb'<section\b[^>]*\bid=["\']'+re.escape(sid.encode())+rb'["\'][^>]*>.*?</section>',re.S|re.I)
    m=pat.search(data)
    if not m: raise AssertionError(f'MISSING_SECTION {sid}')
    return m.group(0)

def alliance_wrapper(data: bytes, start: str, end: str) -> bytes:
    sb=start.encode(); eb=end.encode(); a=data.find(sb)
    if a<0: raise AssertionError('MISSING_ALLIANCE_WRAPPER_START')
    b=data.find(eb,a)
    if b<0: raise AssertionError('MISSING_ALLIANCE_WRAPPER_END')
    return data[a:b+len(eb)]

def audit(html: bytes, cfg: dict) -> dict:
    errors=[]; checks={}
    for sid,expected in cfg['frozen_raw_sections'].items():
        try: got=sha(raw_section(html,sid))
        except AssertionError as e: got='MISSING'; errors.append(str(e))
        ok=got==expected; checks[f'RAW::{sid}']={'pass':ok,'expected':expected,'got':got}
        if not ok: errors.append(f'FROZEN_RAW_MISMATCH {sid} expected={expected} got={got}')
    try: w=sha(alliance_wrapper(html,cfg['alliance_wrapper_start'],cfg['alliance_wrapper_end']))
    except AssertionError as e: w='MISSING'; errors.append(str(e))
    exp=cfg['frozen_alliance_wrapper_sha256']; ok=w==exp
    checks['ALLIANCE_WRAPPER_RAW']={'pass':ok,'expected':exp,'got':w}
    if not ok: errors.append(f'FROZEN_ALLIANCE_WRAPPER_MISMATCH expected={exp} got={w}')
    return {'overall':'PASS' if not errors else 'FAIL','html_sha256':sha(html),'checks':checks,'errors':errors}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--config',required=True,type=Path); ap.add_argument('--candidate',type=Path); ap.add_argument('--json-out',type=Path)
    ns=ap.parse_args(); cfg=json.loads(ns.config.read_text('utf-8'))
    root=Path(cfg['payload_dir']); published=decode_payload(root,cfg['payload_prefix'],cfg['payload_parts'])
    out={'published':audit(published,cfg),'published_sha256':sha(published),'baseline_sha256_at_lock':cfg['effective_published_baseline_sha256_at_lock']}
    if ns.candidate: out['candidate']=audit(ns.candidate.read_bytes(),cfg)
    fail=out['published']['overall']!='PASS' or ('candidate' in out and out['candidate']['overall']!='PASS')
    out['overall']='FAIL' if fail else 'PASS'
    txt=json.dumps(out,indent=2); print(txt)
    if ns.json_out: ns.json_out.parent.mkdir(parents=True,exist_ok=True); ns.json_out.write_text(txt+'\n','utf-8')
    return 1 if fail else 0
if __name__=='__main__': raise SystemExit(main())
