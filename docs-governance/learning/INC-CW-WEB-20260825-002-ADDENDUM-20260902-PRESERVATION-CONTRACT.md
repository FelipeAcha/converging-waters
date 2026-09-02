# INC-CW-WEB-20260825-002 — Addendum 2026-09-02: published-baseline preservation recurrence

**Classification:** SCOPE_DRIFT / FALSE_PRESERVATION_PASS / BASELINE_MISIDENTIFICATION  
**Status:** CORRECTED IN CURRENT CANDIDATE · PREVENTION SOURCE PROPOSED ON BRANCH · USER REVIEW PENDING

## Recurrence

The recovery cycle initially treated REV33 as the source baseline and later claimed a final QA PASS even though the published Alliance Architecture had been altered. The validator proved shallow invariants such as 49 rows / 269 cells, disclosure counts and no overflow, but did not prove the frozen component was the same component the user had approved and published.

Felipe detected the visual regression and also corrected the review contract: he reviews wireframes/Previews, not raw HTML or screenshot galleries.

## Root cause

Three controls were missing or incorrectly scoped:
1. baseline authority was a historical Drive review file instead of the effective GitHub Pages deployment;
2. Alliance protection checked structure/status deltas instead of raw byte identity and visual identity;
3. the active ACB watchdog still treated rejected candidate `v17.0-rev02` as the blocking promotion surface.

## Exact published authority recovered

The successful Pages artifact for head `a1ac1277765c48706bec7a2446185cd8b05befe3` decodes to HTML SHA-256 `3b296999839430c2a1029e41ff404e3de368c1a66b85d1f1503e1c539a2f0f0e`.

A GitHub compare from that deployment head through `351639cae5d0495af72511da87f5ec0eb7e4638f` shows only governance/status files changed; no `docs/index.html`, `docs/payload/**` or deployed asset changed. Therefore those decoded bytes remain the effective published baseline for this correction.

The published Alliance section is byte-identical to the restored REV30 Alliance block:
`03adaa4acb6456d6606fa7ab9796eaa5d6af8a59a58e119f298c0ff8e406e65a`.

## Corrected frozen bundle

The freeze now covers:
- Alliance wrapper: `3fac530898ff763cf2e685d2908558b4622aa8385a2ba80857b00a762510de33`;
- `#alliance-architecture`: `03adaa4acb6456d6606fa7ab9796eaa5d6af8a59a58e119f298c0ff8e406e65a`;
- attached `#people-guardians-stewardship`: `6b461310204fac3dae51ee1733865bbe6d4099c402e929ada914bd9e6a326388`.

The attached stewardship block is frozen because the published Alliance accordion trigger controls its visibility; protecting only the inner Alliance section is insufficient.

## Red / green regression

RED reproduced on the rejected candidate:
- published Alliance SHA: `03adaa...406e65a`;
- rejected candidate Alliance SHA: `ed689d...7962a`;
- rejected candidate also resurrected historical `#context`, absent from the effective published hub.

A second RED caught that the first corrected build still changed the Alliance-controlled stewardship add-on. The builder was narrowed and rerun.

GREEN corrected candidate:
- candidate SHA-256: `ec5a629ee2f63c7ce353ea7ca97bd46eed386499be04e59121e767298c2c72ac`;
- Alliance raw identity: PASS;
- Alliance wrapper raw identity: PASS;
- attached stewardship raw identity: PASS;
- precedents and people-authority boundary raw identity: PASS;
- 32 top-level sections in published order; historical `#context` absent;
- 23 top-level accordions; 27 nested details; 13/13 images load; no document-level overflow at 1440px or 390px.

## Visual regression

The frozen Alliance disclosure bundle was isolated and rendered from both published baseline and corrected candidate using the same Chromium environment.

Pixel comparison result: zero differences for:
- desktop top state;
- desktop matrix-open state;
- mobile top state;
- mobile matrix-open state.

## Prevention

Current prevention source is `CW_WEB_DEFINITION_OF_DONE_v2.md` plus `.github/acb/validate_published_freeze.py` and the ACB watchdog update on branch `cw/web-published-baseline-regression-20260902`.

The prior behavior-verification claim is withdrawn. Future PASS requires exact published-baseline resolution, raw protected hashes, targeted visual equality and wireframe/Preview review before promotion.
