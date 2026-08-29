#!/usr/bin/env python3
from __future__ import annotations
import argparse, base64, gzip, hashlib, json, re
from pathlib import Path

ALLIANCE_REV24_SHA256 = "21929e6c37f70fd52f5e18a18efa16e2afa5801af2f601e5ea5152a487c3328e"
PRINCIPAL_ASSET = "assets/legacy/asset-be0fa6e11454.webp"


def span_by_id(html: str, element_id: str):
    start_re = re.compile(r'<(?P<tag>[A-Za-z][\w:-]*)\b(?=[^>]*\bid\s*=\s*["\']' + re.escape(element_id) + r'["\'])[^>]*>', re.I)
    m = start_re.search(html)
    if not m:
        raise RuntimeError(f"missing id {element_id}")
    tag = m.group("tag")
    tok_re = re.compile(r'</?' + re.escape(tag) + r'\b[^>]*>', re.I)
    depth = 0
    for t in tok_re.finditer(html, m.start()):
        token = t.group(0)
        if token.startswith("</"):
            depth -= 1
            if depth == 0:
                return m.start(), t.end(), html[m.start():t.end()]
        elif not token.rstrip().endswith("/>"):
            depth += 1
    raise RuntimeError(f"unclosed {tag}#{element_id}")


def replace_id(html: str, element_id: str, new_raw: str) -> str:
    a, b, _ = span_by_id(html, element_id)
    return html[:a] + new_raw + html[b:]


def insert_before_id(html: str, element_id: str, raw: str) -> str:
    a, _, _ = span_by_id(html, element_id)
    return html[:a] + raw + html[a:]


def localize_legacy_assets(raw: str) -> str:
    return re.sub(r'(?P<a>\b(?:src|href)=["\'])assets/', r'\g<a>assets/legacy/', raw)


def decode_chunks(paths: list[Path]) -> str:
    b64 = re.sub(r"\s+", "", "".join(p.read_text(encoding="ascii") for p in paths))
    b64 += "=" * (-len(b64) % 4)
    return gzip.decompress(base64.b64decode(b64)).decode("utf-8")


def load_current_hub(repo: Path):
    paths = sorted((repo / "docs/payload").glob("hub-*.txt"))
    if len(paths) != 17:
        raise RuntimeError(f"expected 17 current hub chunks, found {len(paths)}")
    return decode_chunks(paths), paths


def load_approved_alliance(repo: Path) -> str:
    path = repo / "docs-governance/recovery/alliance-rev24.b64"
    if not path.is_file():
        raise RuntimeError(f"missing exact REV24 alliance checkpoint: {path}")
    b64 = re.sub(r"\s+", "", path.read_text(encoding="ascii"))
    raw = gzip.decompress(base64.b64decode(b64)).decode("utf-8")
    got = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    if got != ALLIANCE_REV24_SHA256:
        raise RuntimeError(f"REV24 alliance SHA mismatch: {got}")
    _, _, exact = span_by_id(raw, "alliance-architecture")
    if exact != raw:
        raise RuntimeError("REV24 alliance checkpoint contains bytes outside the section")
    return raw


def strip_authorized_baseline(html: str) -> str:
    html = replace_id(html, "stanley-update", "__STANLEY__")
    html = replace_id(html, "alliance-architecture", "__ALLIANCE__")
    return html


def strip_authorized_candidate(html: str) -> str:
    a, b, _ = span_by_id(html, "principal-infographic")
    html = html[:a] + html[b:]
    html = replace_id(html, "stanley-update", "__STANLEY__")
    html = replace_id(html, "alliance-architecture", "__ALLIANCE__")
    return html


def restore(baseline: str, approved_early: str, approved_alliance: str) -> tuple[str, dict]:
    principal = span_by_id(approved_early, "principal-infographic")[2]
    stanley = span_by_id(approved_early, "stanley-update")[2]
    alliance = span_by_id(approved_alliance, "alliance-architecture")[2]

    principal = localize_legacy_assets(principal)
    stanley = localize_legacy_assets(stanley)

    out = replace_id(baseline, "stanley-update", stanley)
    out = replace_id(out, "alliance-architecture", alliance)
    try:
        span_by_id(out, "principal-infographic")
    except RuntimeError:
        out = insert_before_id(out, "current-session", principal)
    else:
        out = replace_id(out, "principal-infographic", principal)

    if strip_authorized_baseline(baseline) != strip_authorized_candidate(out):
        raise RuntimeError("unauthorized bytes changed outside the three restoration regions")

    principal_out = span_by_id(out, "principal-infographic")[2]
    stanley_out = span_by_id(out, "stanley-update")[2]
    alliance_out = span_by_id(out, "alliance-architecture")[2]
    if principal_out != principal:
        raise RuntimeError("principal infographic is not exact approved block after asset localization")
    if stanley_out != stanley:
        raise RuntimeError("stanley section is not exact approved block after asset localization")
    if alliance_out != alliance:
        raise RuntimeError("alliance section is not exact REV24/REV17 recovery block")

    if hashlib.sha256(alliance.encode("utf-8")).hexdigest() != ALLIANCE_REV24_SHA256:
        raise RuntimeError("restored alliance block does not match exact REV24/REV17 checkpoint")
    if len(re.findall(r"<img\b", stanley, re.I)) != 13:
        raise RuntimeError("approved Stanley section no longer has 13 images")
    if len(re.findall(r"<a\b", stanley, re.I)) != 17:
        raise RuntimeError("approved Stanley section no longer has 17 links")
    if PRINCIPAL_ASSET not in principal:
        raise RuntimeError("principal infographic did not localize to canonical legacy asset")

    section_id_re = re.compile(r'<section\b[^>]*\bid\s*=\s*["\']([^"\']+)["\']', re.I)
    before_ids = section_id_re.findall(baseline)
    after_ids = section_id_re.findall(out)
    if before_ids != after_ids:
        raise RuntimeError("section ID order changed")

    report = {
        "baseline_sha256": hashlib.sha256(baseline.encode("utf-8")).hexdigest(),
        "candidate_sha256": hashlib.sha256(out.encode("utf-8")).hexdigest(),
        "principal_infographic": "RESTORED_FROM_v16.1.1",
        "stanley_update": "RESTORED_FROM_v16.1.1_APPROVED_LINEAGE",
        "alliance_architecture": "RESTORED_FROM_REV24_RECOVERY_SOURCE_REV17",
        "alliance_sha256": ALLIANCE_REV24_SHA256,
        "stanley_images": 13,
        "stanley_links": 17,
        "untouched_bytes": "EXACT_AFTER_REMOVING_3_AUTHORIZED_REGIONS",
        "section_order": "UNCHANGED",
    }
    return out, report


def write_payload(html: str, paths: list[Path]):
    packed = gzip.compress(html.encode("utf-8"), compresslevel=9, mtime=0)
    b64 = base64.b64encode(packed).decode("ascii")
    n = len(paths)
    size = (len(b64) + n - 1) // n
    chunks = [b64[i:i+size] for i in range(0, len(b64), size)]
    while len(chunks) < n:
        chunks.append("")
    if len(chunks) != n:
        raise RuntimeError(f"payload split produced {len(chunks)} chunks, expected {n}")
    for path, chunk in zip(paths, chunks):
        path.write_text(chunk, encoding="ascii")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=Path("."))
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--report", type=Path, default=Path("/tmp/hub-recovery-report.json"))
    args = ap.parse_args()
    repo = args.repo.resolve()
    baseline, hub_paths = load_current_hub(repo)
    approved_early = (repo / "docs/candidates/v16.1.1/index.html").read_text(encoding="utf-8")
    approved_alliance = load_approved_alliance(repo)
    candidate, report = restore(baseline, approved_early, approved_alliance)
    asset = repo / "docs" / PRINCIPAL_ASSET
    if not asset.is_file() or asset.stat().st_size == 0:
        raise RuntimeError(f"principal infographic asset missing: {asset}")
    if args.write:
        write_payload(candidate, hub_paths)
        reread, _ = load_current_hub(repo)
        if reread != candidate:
            raise RuntimeError("written hub payload does not round-trip exactly")
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
