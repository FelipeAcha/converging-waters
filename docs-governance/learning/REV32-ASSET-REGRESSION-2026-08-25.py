#!/usr/bin/env python3
"""Regression for F21: protected field/data images must survive standalone review transport.

Usage:
  python REV32-ASSET-REGRESSION-2026-08-25.py <baseline-rev31.html> <candidate-rev32.html>
"""
from pathlib import Path
from bs4 import BeautifulSoup
import base64
import sys

if len(sys.argv) != 3:
    raise SystemExit("usage: test <baseline-rev31.html> <candidate-rev32.html>")
base = BeautifulSoup(Path(sys.argv[1]).read_text(encoding="utf-8"), "html.parser")
cand = BeautifulSoup(Path(sys.argv[2]).read_text(encoding="utf-8"), "html.parser")
b = base.select_one("#stanley-update")
c = cand.select_one("#stanley-update")
assert b is not None and c is not None, "missing #stanley-update"
bi = b.find_all("img")
ci = c.find_all("img")
assert len(bi) == len(ci) == 13, (len(bi), len(ci))
assert [x.get("alt") for x in bi] == [x.get("alt") for x in ci], "alt text changed"
assert [a.get("href") for a in b.find_all("a", href=True)] == [a.get("href") for a in c.find_all("a", href=True)], "href sequence changed"
assert len(c.find_all("a", href=True)) == 17
for img in ci:
    src = img.get("src", "")
    assert src.startswith("data:image/webp;base64,"), f"non-self-contained protected image: {src[:80]}"
    raw = base64.b64decode(src.split(",", 1)[1])
    assert raw[:4] == b"RIFF" and raw[8:12] == b"WEBP", "invalid WebP payload"
print("PASS: 13/13 protected images self-contained; 17/17 links and all alt text preserved.")
