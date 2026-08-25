#!/usr/bin/env python3
from __future__ import annotations
import re, sys
from pathlib import Path

REQ = {
    'STATE','SOURCE_REVIEW','SOURCE_HUB_SHA256','CUMULATIVE_PROGRESS',
    'DEEP_DIVES','CONTENT_MUTATION_MODE','PRODUCTION','AUTHORITY_LEDGER'
}

def parse_state(path: Path):
    data={}
    for raw in path.read_text(encoding='utf-8').splitlines():
        line=raw.strip()
        if not line or line.startswith('#'):
            continue
        if '=' not in line:
            raise ValueError(f'invalid state line: {raw}')
        k,v=line.split('=',1)
        data[k.strip()]=v.strip()
    return data

def fail(msg):
    print(f'FAIL: {msg}', file=sys.stderr)
    raise SystemExit(1)

def main(argv):
    if len(argv)!=2:
        print('usage: validate_cumulative_progress.py <progress-dir>', file=sys.stderr)
        return 2
    root=Path(argv[1])
    state_path=root/'.cumulative-progress-state.txt'
    if not state_path.is_file(): fail('missing .cumulative-progress-state.txt')
    try: state=parse_state(state_path)
    except Exception as e: fail(str(e))
    missing=sorted(REQ-set(state))
    if missing: fail(f'missing state keys: {missing}')
    rev=state['SOURCE_REVIEW']
    if not re.fullmatch(r'REV\d+',rev): fail('SOURCE_REVIEW must match REV<integer>')
    sha=state['SOURCE_HUB_SHA256']
    if not re.fullmatch(r'[0-9a-f]{64}',sha): fail('SOURCE_HUB_SHA256 must be lowercase SHA-256')
    if state['STATE']!='REVIEW_TRANSPORT_ONLY': fail('STATE must be REVIEW_TRANSPORT_ONLY')
    if state['PRODUCTION']!='NOT_AUTHORIZED': fail('PRODUCTION must be NOT_AUTHORIZED on progress transport')
    if state['CONTENT_MUTATION_MODE']!='ADDITIVE_ONLY': fail('CONTENT_MUTATION_MODE must remain ADDITIVE_ONLY')
    progress=state['CUMULATIVE_PROGRESS']
    if progress=='BLOCKED_WITH_REASON':
        if not state.get('BLOCKED_REASON','').strip(): fail('BLOCKED_WITH_REASON requires BLOCKED_REASON')
        print(f'PASS: cumulative progress explicitly blocked at {rev}: {state["BLOCKED_REASON"]}')
        return 0
    expected=f'ADVANCED_TO_{rev}'
    if progress!=expected: fail(f'CUMULATIVE_PROGRESS must be {expected} or BLOCKED_WITH_REASON')
    index=(root/'index.html')
    current=(root/'current.html')
    if not index.is_file() or not current.is_file(): fail('missing index.html or current.html')
    if rev not in index.read_text(encoding='utf-8'): fail(f'index.html does not advertise {rev}')
    if sha not in current.read_text(encoding='utf-8'): fail('current.html does not carry SOURCE_HUB_SHA256')
    slugs=[s.strip() for s in state['DEEP_DIVES'].split(',') if s.strip()]
    if not slugs: fail('DEEP_DIVES must not be empty')
    for slug in slugs:
        if not re.fullmatch(r'[a-z0-9-]+',slug): fail(f'invalid deep-dive slug: {slug}')
        if not (root/'deep-dives'/slug/'index.html').is_file(): fail(f'missing deep dive: {slug}')
    print(f'PASS: cumulative progress {progress}; hub={sha}; deep_dives={len(slugs)}')
    return 0

if __name__=='__main__':
    raise SystemExit(main(sys.argv))
