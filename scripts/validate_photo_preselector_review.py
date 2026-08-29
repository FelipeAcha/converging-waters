#!/usr/bin/env python3
"""Deterministic contract validator for the Converging Waters photo preselector review surface."""
from __future__ import annotations

import base64
import gzip
import hashlib
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

EXPECTED_GZIP_SHA256 = "277700a35c7dfa03de1d575ceae93571e601b550c1206c3d3239e43a61c05c40"
EXPECTED_PARTS = 26
EXPECTED_COUNTS = (18, 77, 77, 77)


class PayloadAudit(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.needs = 0
        self.candidates = 0
        self.checkboxes = 0
        self.images: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        data = dict(attrs)
        classes = set(data.get("class", "").split())
        if tag == "section" and "need" in classes:
            self.needs += 1
        if tag == "article" and "candidate" in classes:
            self.candidates += 1
        if tag == "input" and data.get("type") == "checkbox":
            self.checkboxes += 1
        if tag == "img":
            self.images.append(data.get("src", ""))


def fail(message: str) -> None:
    raise SystemExit("FAIL: " + message)


def validate(root: Path) -> None:
    root = root.resolve()
    shell_path = root / "index.html"
    payload_dir = root / "payload2"
    if not shell_path.is_file():
        fail(f"missing shell: {shell_path}")
    if not payload_dir.is_dir():
        fail(f"missing payload directory: {payload_dir}")

    shell = shell_path.read_text(encoding="utf-8")
    refs = re.findall(r'''(?:src|href)=["']([^"']+)["']''', shell)
    refs += re.findall(r'''fetch\(\s*["']([^"']+)["']''', shell)
    for ref in refs:
        if ref.startswith(("http://", "https://", "data:", "mailto:", "tel:", "#", "javascript:", "blob:")):
            continue
        rel = ref.split("?", 1)[0].split("#", 1)[0]
        if not rel:
            continue
        target = (root / rel).resolve()
        try:
            target.relative_to(root)
        except ValueError:
            fail(f"local dependency escapes review root: {ref}")
        if not target.exists():
            fail(f"missing local dependency: {ref}")

    expected_names = [f"{i:03d}.txt" for i in range(EXPECTED_PARTS)]
    parts = sorted(payload_dir.glob("*.txt"))
    names = [p.name for p in parts]
    if names != expected_names:
        fail(f"payload chunk set mismatch: expected {expected_names}, found {names}")

    encoded = "".join(p.read_text(encoding="utf-8").strip() for p in parts)
    try:
        raw = base64.b64decode(encoded, validate=True)
    except Exception as exc:
        fail(f"payload base64 is invalid: {exc}")

    actual_sha = hashlib.sha256(raw).hexdigest()
    if actual_sha != EXPECTED_GZIP_SHA256:
        fail(f"payload SHA-256 mismatch: {actual_sha} != {EXPECTED_GZIP_SHA256}")

    try:
        payload_html = gzip.decompress(raw).decode("utf-8")
    except Exception as exc:
        fail(f"payload gzip/UTF-8 is invalid: {exc}")

    audit = PayloadAudit()
    audit.feed(payload_html)
    observed = (audit.needs, audit.candidates, audit.checkboxes, len(audit.images))
    if observed != EXPECTED_COUNTS:
        fail(f"payload counts mismatch: {observed} != {EXPECTED_COUNTS}")

    for pos, src in enumerate(audit.images, 1):
        if not src.startswith("data:image/") or ";base64," not in src:
            fail(f"image {pos} is not an embedded data image")
        _, image_payload = src.split(";base64,", 1)
        try:
            base64.b64decode(image_payload, validate=True)
        except Exception as exc:
            fail(f"image {pos} has invalid base64: {exc}")

    required_shell_markers = (
        EXPECTED_GZIP_SHA256,
        "Array.from({length:26}",
        "object-fit:contain",
        "checked.length>r",
        "checked.length>=r",
        "data-selector-ready",
        "Payload integrity mismatch",
        "DecompressionStream",
    )
    missing = [m for m in required_shell_markers if m not in shell]
    if missing:
        fail("shell enforcement markers missing: " + repr(missing))

    if re.search(r'<img[^>]+src=["\']https?://', payload_html, flags=re.I):
        fail("payload contains an automatic remote image source")

    print(
        "PASS photo preselector contract: 26/26 chunks, gzip SHA-256, 18/77/77/77, "
        "embedded images, full-frame contain, selection enforcement, local-dependency regression"
    )


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: validate_photo_preselector_review.py <review-dir>")
    validate(Path(sys.argv[1]))


if __name__ == "__main__":
    main()
