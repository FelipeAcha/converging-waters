#!/usr/bin/env python3
"""Fail closed when an HTML review transport references missing local dependencies.

Usage: python CW-PREVIEW-HANDOFF-REGRESSION-2026-08-29.py <review-dir>
Checks HTML/CSS/JS document dependencies used for rendering. External http(s), data:, mailto:, anchors are allowed.
"""
from pathlib import Path
from bs4 import BeautifulSoup
import re, sys

if len(sys.argv) != 2:
    raise SystemExit('usage: regression.py <review-dir>')
root = Path(sys.argv[1])
index = root / 'index.html'
assert index.is_file(), f'missing {index}'
text = index.read_text(encoding='utf-8')
soup = BeautifulSoup(text, 'html.parser')
refs = []
for tag, attr in [('script','src'),('link','href'),('img','src'),('source','src'),('video','src'),('audio','src'),('iframe','src')]:
    for node in soup.find_all(tag):
        v = (node.get(attr) or '').strip()
        if v: refs.append(v)
refs += re.findall(r'''fetch\(\s*["']([^"']+)["']''', text)
missing=[]
for ref in refs:
    if ref.startswith(('http://','https://','data:','mailto:','tel:','#','javascript:','blob:')):
        continue
    path = ref.split('?',1)[0].split('#',1)[0]
    if not path: continue
    target=(root/path).resolve()
    try: target.relative_to(root.resolve())
    except ValueError: missing.append((ref,'ESCAPES_ROOT')); continue
    if not target.exists(): missing.append((ref,'MISSING'))
assert not missing, 'broken local review dependencies: ' + repr(missing)
print(f'PASS: review transport dependencies resolve locally ({len(refs)} refs scanned).')
