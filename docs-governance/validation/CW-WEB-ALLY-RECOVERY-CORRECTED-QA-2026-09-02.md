# Converging Waters ally web recovery — corrected published-baseline QA

**Date:** 2026-09-02  
**Status:** SOURCE + PROTECTED VISUAL VALIDATED · REAL-WEB REVIEW SURFACE STAGED · USER APPROVAL PENDING  
**Public promotion:** NONE

## Baseline

Effective published hub HTML SHA-256:
`3b296999839430c2a1029e41ff404e3de368c1a66b85d1f1503e1c539a2f0f0e`

Resolved from successful GitHub Pages artifact at head:
`a1ac1277765c48706bec7a2446185cd8b05befe3`

Repository compare through `351639cae5d0495af72511da87f5ec0eb7e4638f` shows no later deployed web input changed.

## Corrected candidate

Drive ID: `1EQM1iDLI0GeXTyTzWa55VnRHMC1txODh`  
SHA-256 after Drive raw readback: `ec5a629ee2f63c7ce353ea7ca97bd46eed386499be04e59121e767298c2c72ac`  
Byte readback: PASS.

## Real-web review surfaces

A ChatGPT Web Preview is a real rendered website preview, not a wireframe. It remains a valid human review surface when the exact candidate is rendered there and the Preview is visible to Felipe.

An isolated live review transport has also been staged at:
`https://felipeacha.github.io/converging-waters/candidates/progress/`

The route is `REVIEW_TRANSPORT_ONLY`; it does not replace the authoritative public root. Its loader reconstructs the exact review transport from six staged chunks and refuses to render unless the reconstructed SHA-256 equals:
`6427c247a5bdbce5b193d9ee812b9349057ce62923be5a1ab138d0fef25059ba`.

GitHub readback confirms all six staged chunk blobs match the locally computed canonical Git blob identities. GitHub Pages deployment run `33661867687` completed successfully at head `37fe87dd403a09960fa6bd08f063a190f41235ca`.

The earlier wireframe PDF remains historical QA/supporting evidence only. It is not the primary human review surface and must not substitute for the functioning website candidate.

## Frozen Alliance disclosure bundle

| Component | Published SHA-256 | Candidate | Result |
|---|---|---|---|
| Alliance wrapper | `3fac530898ff763cf2e685d2908558b4622aa8385a2ba80857b00a762510de33` | same | PASS |
| `#alliance-architecture` | `03adaa4acb6456d6606fa7ab9796eaa5d6af8a59a58e119f298c0ff8e406e65a` | same | PASS |
| `#people-guardians-stewardship` | `6b461310204fac3dae51ee1733865bbe6d4099c402e929ada914bd9e6a326388` | same | PASS |

Matrix remains 49 rows / 269 cells.

## Targeted visual equality

Published vs candidate isolated component rendered in Chromium:
- desktop top state: 0 differing pixels;
- desktop matrix-open state: 0 differing pixels;
- mobile top state: 0 differing pixels;
- mobile matrix-open state: 0 differing pixels.

## Source/structure audit

PASS:
- effective published baseline identity;
- 32 top-level sections, exact published order;
- no resurrected `#context` section;
- 23 top-level accordions;
- 27 nested `<details>` disclosures;
- frozen Alliance/stewardship/precedent/authority-boundary raw equality;
- copy-only changed sections preserve published DOM/attribute structure;
- external href sequence exact;
- image src/alt/title sequence exact;
- executable CSS exact after development-comment removal;
- script bytes exact;
- no HTML development comments;
- no prohibited web-development markers in visible public copy.

## Browser smoke

Desktop 1440x1000 and mobile 390x844:
- document/body width equals viewport;
- 1 H1;
- 32 sections;
- 23 top-level accordions;
- 27 nested details;
- 13/13 images decoded;
- 0 duplicate IDs;
- top-level accordion and nested-details toggle/restore checks PASS.

## Lifecycle

`PUBLISHED_BASELINE_LOCK=PASS`  
`CORRECTED_SOURCE_AUDIT=PASS`  
`ALLIANCE_RAW_FREEZE=PASS`  
`ALLIANCE_PIXEL_FREEZE=PASS`  
`BROWSER_SMOKE=PASS`  
`REAL_WEB_REVIEW_SURFACE_STAGED=PASS`  
`CHATGPT_WEB_PREVIEW=VALID_REVIEW_MODE_WHEN_USER_VISIBLE`  
`ISOLATED_REVIEW_ROUTE_DEPLOYMENT=PASS`  
`USER_APPROVED=false`  
`PROMOTED=false`  
`PUBLIC_MAIN_MUTATED=false`

Next gate: Felipe reviews the exact functioning website candidate through ChatGPT Web Preview or the validated isolated live review route. No promotion occurs before explicit approval.
