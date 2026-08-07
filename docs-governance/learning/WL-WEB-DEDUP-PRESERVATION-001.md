# WL-WEB-DEDUP-PRESERVATION-001 — Deduplicate without content or asset loss

Status: VERIFIED FOR CONVERGING WATERS
Owner: Project production and governance workflow
Activated: 2026-08-07
Coverage tier: TOOL_OR_VALIDATOR

## Trigger

A proposed website deduplication candidate was generated after the user explicitly required that no unique information be lost and that all Stanley / WGA material, apparatus examples, reference cards, images and links remain. The candidate was built from a reconstructed structural subset rather than from the exact authoritative v13 source. It therefore removed material that the user had explicitly protected, including the full Stanley / WGA apparatus and reference section shown in the authoritative website.

## Primary classification

- `INSUFFICIENT_EVIDENCE`
- `ASSUMED_COMPLETION`
- `OUTPUT_PRIORITY_FAILURE`
- `UNNECESSARY_REBUILD`

## First control failure

The deduplication operation did not begin from the exact authoritative HTML and asset set. A semantic preservation claim was then made without a deterministic comparison proving that protected sections, images, links and retained source blocks were unchanged.

## Permanent prevention rule

For any future Converging Waters website deduplication, restructuring or consolidation:

1. Resolve the authoritative current website using the current handoff and technical memory before editing.
2. Recover and verify the exact authoritative HTML and asset set. A structural reconstruction, summary, screenshot-derived recreation or prior generated candidate is not an acceptable source for lossless deduplication.
3. Inventory top-level sections, assets, internal fragment links and explicitly protected blocks before removing anything.
4. Remove only complete, evidenced redundant sections or blocks. Do not rewrite or reserialize retained sections when subtraction alone can achieve the requested change.
5. Every retained top-level section must remain byte-identical unless the user explicitly authorizes edits to that section.
6. Every explicitly protected section must have a hard regression anchor consisting of its raw section hash plus its child image/link counts and, where applicable, asset hashes.
7. All retained assets must remain byte-identical unless the user explicitly approves replacement or optimization.
8. A claim such as `CONTENT_DELETED_WITHOUT_RELOCATION=0` is invalid unless it is derived from the exact authoritative source and a deterministic preservation comparison.
9. Deduplication must prefer the smallest subtraction set. When two sections overlap but each contains unique detail or serves a distinct narrative function, keep both.
10. The current approved/review baseline and every rejected or superseded candidate remain separate and recoverable; a correction creates a new candidate rather than overwriting the prior one.

## Current hard lock — Stanley / WGA

For the v13 → v15 correction, the complete `stanley-update` section is protected byte-for-byte:

- section id: `stanley-update`
- raw section SHA-256: `d22889e1b98d8f49d3ea09f74092e97273d06964852e19b20c0aebd26d5525e1`
- images inside section: `13`
- links inside section: `17`

This block includes the complete apparatus/reference area: sample + sequence; context + verify; learn + steward; portable field science; Sacred Valley possibility; design principle; ecosystem atlas/metagenome patterns; small field computers; sensor + metadata nodes; citizen-science bioacoustics; autonomous field systems; portable sequencing in context; WGA public/data/academy/storytelling links; the four-step technical-next-step sequence; and the final clarification band.

## Deterministic and behavior regression

The preservation-first v15 builder performs raw section subtraction from the exact recovered v13 HTML and fails when any of these invariants are violated:

- baseline section count differs from the verified inventory;
- any retained top-level section hash changes;
- `stanley-update` is missing or its raw hash changes;
- the Stanley / WGA image count differs from 13;
- the Stanley / WGA link count differs from 17;
- any of the 16 recovered v13 asset hashes changes;
- a local image reference is missing;
- an internal fragment link is broken;
- browser-rendered DOM smoke checks cannot find the protected WGA apparatus/reference markers.

Verified regression evidence:

- authoritative v13 HTML SHA-256: `fcb857aa61635a800f2faef512e9a14c3d53445ec996a03603ffa939dbd4ca11`
- authoritative v13 assets: `16`
- GitHub Actions run: `31228287502`
- run result: `SUCCESS`
- build regression: `PASS`
- headless-browser smoke test: `PASS`
- candidate retained-section byte identity: `PASS`
- candidate Stanley / WGA hard lock: `PASS_BYTE_IDENTICAL`

## Current corrected candidate scope

The corrected v15 candidate removes only three standalone sections from the 42-section v13 baseline:

- `agenda` — duplicate meta reading/agenda layer after the current-session agenda;
- `open-decisions` — short unknowns summary covered in greater detail by validation, first-outcome, current-decision and the substantive governance/data/territorial sections;
- `decision` — second closing decision block after the richer `current-decision` section.

All other top-level sections remain in their original order and are byte-identical to v13. This is deliberately more conservative than the rejected v14 candidate.

## Revalidation triggers

Re-run the preservation regression whenever:

- a new authoritative website baseline supersedes v13;
- an explicitly protected section is changed;
- an asset is optimized or replaced;
- a new deduplication/consolidation set is proposed;
- navigation or fragment targets are changed;
- the user reports missing information, imagery, references or functionality.

## Rollback

The current v13 release remains untouched. The rejected v14 candidate remains a separate artifact. The corrected v15 work is a separate candidate and can be discarded without changing the current v13 preview.
