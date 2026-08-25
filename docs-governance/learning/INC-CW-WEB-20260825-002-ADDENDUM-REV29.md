# Incident addendum — REV29 final-QA finding

Parent incident: `INC-CW-WEB-20260825-002`  
Date: 2026-08-25  
Production: NOT_AUTHORIZED / unchanged

## F17 — stale internal anchor survived prior section restructuring

**Failure:** the hub still contained `href="#validation"` in the River System / sanitation context, but no element with `id="validation"` existed in the current integrated hub. The intended destination is the preserved `#what-we-need-now` section (`10 · What needs to be validated now`).

**Classification:** `PARALLEL_CHANGE_NOT_RECONCILED` + `INSUFFICIENT_EVIDENCE`.

**First control failure:** section/ID restructuring and later integration preserved the visible link text but did not enforce an all-internal-anchors-resolve regression before earlier closure claims.

**User impact:** latent navigation defect. It was caught by the REV28 cross-cutting final-QA validator before production, not reported by the user.

**Corrective action:** REV29 changes exactly that href from `#validation` to `#what-we-need-now`; no linked copy, section content or deep-dive bytes were changed.

**Preventive action:** every final web candidate/bundle must fail closed when any internal `#anchor` does not resolve in its owning HTML page. This test is separate from external-link validation and from DOM/text preservation.

**Regression:** REV28 test = RED (`#validation` missing). REV29 test = GREEN (0 missing internal anchors, 0 missing local bundle links, 0 duplicate IDs, 0 details without summary, 0 images without alt).

**Evidence:**
- REV29 hub Drive ID `16aEUok0KcuS8hLxSKSe9b2K1r5Fr4jTt`
- REV29 hub SHA-256 `2079443902521e5427ab1fa4d7ba20394ef4910d714bea2c74ad981daf51c7f9`
- REV29 bundle Drive ID `1Pj_H5CU6qR0V-r9GXET99UOSX1pDOYBf`
- REV29 bundle SHA-256 `d073a603f178bfcb8173845f4da533aaa08d0f7b8a0376c348a46e5c043ceb1c`

## Open release dependency — remote precedent photography

This is **not classified as another failure yet**. REV27/REV29 intentionally use freely licensed Wikimedia image URLs during review, with source/credit links. The current execution environment cannot DNS-resolve Wikimedia, so exact local image bytes could not be mirrored here. Before production, either localize the eight remote precedent-image references used across hub/Rights (five unique images) and verify hashes/attribution/rendering, or make an explicit release decision to retain remote hosting. Production remains blocked from silently inheriting this unresolved asset dependency.
