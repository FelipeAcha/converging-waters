# REV27 / REV28 web checkpoint — 2026-08-25

## State
- REV27: visual correction checkpoint from REV26.
- REV28: integrated hub + existing deep-dive cross-navigation checkpoint from REV27.
- Production: NOT_AUTHORIZED / unchanged.
- Rolling Progress Preview: update from stale REV24 transport is still pending; do not treat the public progress route as current until readback confirms REV28.

## REV27
User-authorized corrections only:
1. Section 07: increase hierarchy of `Working naming convention` and `How to read the monitoring architecture`; add spacing before `Three evidence scales`.
2. Section 16: replace the clipped inline precedent illustrations with freely licensed Wikimedia photographs; national cases reuse the same sources already used in the Rights deep dive; global Whanganui and Atrato use freely licensed Wikimedia sources; credits/source links remain visible.

Exact HTML Drive ID: `1Au_DxXqDS_hzmsMekKTzfmN3DJc-2-94`
SHA-256: `6e2edfeacd776847826f21b4adfb7fcf219ea41fb9c81db9bb0c6f3bd3098f92`
Checkpoint Drive ID: `1PDW7WdXuJ5yW5FVWdQuzAZyoG6C9RB6e`
Validation: protected text/hrefs preserved, all sections outside `#system` and `#precedents` unchanged, 1440/390 no horizontal overflow, no console errors. Remote Wikimedia media remains REVIEW_ONLY and must be localized before production.

## REV28
No deep-dive content was rebuilt. Existing Rights, Observatory and River Economy sources were preserved and connected as one review bundle.

Hub exact HTML Drive ID: `14KkUEPDRZBxHxsAHyuo1NdGSzPT-CcGq`
Hub SHA-256: `09e02013b7176cc5165d8de7578c69ae168e941e3ba2fa93e74bc8f9021a0712`

Rights deep dive REV2 / cross-nav:
- Drive ID `1GtJ17ubxMMAFWdblhoiUYCzm6yPnuV-J`
- SHA-256 `1bdb0badef0c6f9127f94d68975996ad24436e7516212558c478e50885b42112`

Willkamayu River Observatory REV3 / cross-nav:
- Drive ID `1sD71FH_IlJjqfCU9ewQ-y7JWOJZp8tWp`
- SHA-256 `a7e339aeaf152e05b4ced5e2deb18c1d110a8317cd5c4653f3353caddf81aff5`

River Economy REV2 / cross-nav:
- Drive ID `1PP99QMOcnrkYSAnooAdaRDSfX4fgrvnx`
- SHA-256 `7354c225b9ad5f8ae44d696ac70a829b9a65259d3da750f58bd255fc7ec11e51`

Review bundle:
- Drive ID `1Q3J13cvzW5sGt_QO1WV-bylWem9Aw8uG`
- SHA-256 `a9b2c83392b78321839aef6e023cab419122fa6498afdb0e3357d7c1b136ece2`

Checkpoint sidecar Drive ID: `1uw92bO5ajiOAFGI4lNziWSO-inb7vNn8`.

Preservation/QA:
- Hub sections outside Section 17 remain REV27-exact.
- Existing substantive sections inside all three deep dives remain exact; only review cross-navigation + title metadata were added.
- Existing hrefs remain in original order; added review navigation paths resolve inside the bundle.
- Browser set-content QA at 1440 and 390 found no horizontal overflow and no console errors.
- Public localhost navigation remains blocked by the environment; this is a browser-environment limitation, not a content rewrite.

## Next gate
1. Advance the stable Rolling Progress Preview to exact REV28 and read back route + state; until then the route is stale.
2. Run final cross-cutting visual/release QA on the integrated hub + deep dives without reopening protected content.
3. Separate explicit publication gate.
4. After website closure/release decision, execute `GATE-CW-SYSTEM-RELIABILITY-AUDIT-001` (Issue #15).
