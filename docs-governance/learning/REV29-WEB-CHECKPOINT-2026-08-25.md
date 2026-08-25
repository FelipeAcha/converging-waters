# REV29 web checkpoint — 2026-08-25

## State
- Baseline: REV28 integrated hub + existing deep dives.
- Delta: final-QA repair only — replace stale internal link `#validation` with existing section `#what-we-need-now`.
- Deep-dive component bytes from REV28 are unchanged.
- Production: NOT_AUTHORIZED / unchanged.
- Rolling Progress Preview: still not current until its GitHub transport is advanced/read back; do not represent the stale public route as REV29.

## Exact artifacts
Hub HTML Drive ID: `16aEUok0KcuS8hLxSKSe9b2K1r5Fr4jTt`
Hub SHA-256: `2079443902521e5427ab1fa4d7ba20394ef4910d714bea2c74ad981daf51c7f9`

REV29 integrated review bundle Drive ID: `1Pj_H5CU6qR0V-r9GXET99UOSX1pDOYBf`
Bundle SHA-256: `d073a603f178bfcb8173845f4da533aaa08d0f7b8a0376c348a46e5c043ceb1c`

Checkpoint sidecar Drive ID: `1QhbXONLsh1_cLd5imWl46MbaGO2JeDXe`.

Unchanged REV28 deep dives:
- Rights: `1bdb0badef0c6f9127f94d68975996ad24436e7516212558c478e50885b42112`
- Observatory: `a7e339aeaf152e05b4ced5e2deb18c1d110a8317cd5c4653f3353caddf81aff5`
- River Economy: `7354c225b9ad5f8ae44d696ac70a829b9a65259d3da750f58bd255fc7ec11e51`

## Final-QA evidence to this gate
Static QA on all four integrated pages:
- duplicate IDs: 0;
- missing internal anchors: 0 after REV29 repair;
- missing local bundle links: 0;
- images missing alt: 0;
- details missing summary: 0.

Browser set-content QA at 1440px and 390px for hub + all three deep dives:
- horizontal overflow: 0;
- console errors: 0.

Known release debt: five Wikimedia precedent images in hub and three in Rights deep dive remain remote review media. Attribution/source links are present. Before production, localize those image bytes (or formally decide to retain remote hosting) and rerun asset/hash/render QA.

## Next gate
`ROLLING_PROGRESS_ADVANCE_TO_REV29` then exact route/state readback; after that continue final release QA/publication decision without reopening protected content.
