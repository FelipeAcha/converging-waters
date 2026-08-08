# WL-WEB-DEDUP-PRESERVATION-001 — Deduplicate without content or asset loss

Status: VERIFIED FOR V16.1 STEP 1
Owner: Project production and governance workflow
Activated: 2026-08-07
Updated: 2026-08-08
Coverage tier: TOOL_OR_VALIDATOR

## Trigger

A proposed website deduplication candidate was generated after the user explicitly required that no unique information be lost and that all Stanley / WGA material, apparatus examples, reference cards, images and links remain. The candidate was built from a reconstructed structural subset rather than from the exact authoritative v13 source. It therefore removed material that the user had explicitly protected, including the full Stanley / WGA apparatus and reference section shown in the authoritative website.

A later candidate passed source-level preservation checks but still did not satisfy the user's user-visible review expectation. This established that source/hash preservation alone is not sufficient: the exact public candidate route must also be rendered and checked, and recovery must proceed one explicitly requested delta at a time from the named baseline rather than from a prior failed candidate.

## Primary classification

- `INSUFFICIENT_EVIDENCE`
- `ASSUMED_COMPLETION`
- `OUTPUT_PRIORITY_FAILURE`
- `UNNECESSARY_REBUILD`
- `SCOPE_DRIFT`

## First control failure

The deduplication operation did not begin from the exact authoritative HTML and asset set. A semantic preservation claim was then made without a deterministic comparison proving that protected sections, images, links and retained source blocks were unchanged.

The second control failure was treating a source-level regression pass as sufficient evidence of the user's rendered result. The user-visible route must be checked directly before claiming the requested visual state is present.

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
11. After any user-visible contradiction, restart the next candidate from the exact baseline named by the user, not from the failed candidate.
12. Use one requested delta per incremental subversion. Do not combine unrelated cleanup, rewriting, link repair, reordering or optimization into the same step.
13. Before claiming a visual correction is complete, render the exact public candidate route in a real browser and test the requested element's presence, order and visibility.
14. Untouched external `href` values must remain identical in count, order and value unless link editing is the explicitly authorized step. Live reachability testing is a separate step and must not be mixed into an infographic-only delta.
15. For infographic deduplication, preserve the designated principal graphic exactly, change only its requested placement/visibility, and suppress only the duplicate visual representation. Do not touch unrelated sections.

## Current hard lock — Stanley / WGA

The complete `stanley-update` section remains protected. It includes the full apparatus/reference area: sample + sequence; context + verify; learn + steward; portable field science; Sacred Valley possibility; design principle; ecosystem atlas/metagenome patterns; small field computers; sensor + metadata nodes; citizen-science bioacoustics; autonomous field systems; portable sequencing in context; WGA public/data/academy/storytelling links; the four-step technical-next-step sequence; and the final clarification band.

## v16.1 step-1 contract

Baseline: exact v13 package.

Only authorized website delta:

- move the existing principal consolidated infographic `#purpose-visual-reference` to immediately below the hero/title block;
- suppress the later native duplicate infographic reconstruction `.visual-shell` from rendering;
- make no other intentional content change.

Required invariants:

- exact v13 ZIP and HTML hashes are verified before transformation;
- the principal infographic exists exactly once;
- the duplicate visual shell is suppressed exactly once;
- the principal infographic renders before `#current-session`;
- Stanley / WGA markers remain rendered;
- all external href values match v13 exactly in count, order and value.

Verified behavior evidence:

- v16.1 candidate commit: `920d9af200431a3f8331eb23e8fdeeac987c8707`
- GitHub Pages deployment run: `31272198961` — SUCCESS
- rendered-regression branch: `review/v16-1-render-qa`
- rendered-regression run: `31272325675` — SUCCESS
- rendered external hrefs: `46`, exact v13 match
- principal infographic above `current-session`: PASS
- Stanley / WGA rendered markers: PASS

## Current candidate routing

- v13 remains the authoritative baseline and current preview source.
- v14 and v15 remain historical/rejected or superseded review candidates and must not be used as the source for the next recovery step.
- v16.1 is the current incremental candidate for infographic placement/deduplication only.
- Further changes must create v16.2, v16.3, etc., each with one explicitly requested delta unless Felipe explicitly authorizes batching.

## Revalidation triggers

Re-run the preservation regression whenever:

- a new authoritative website baseline supersedes v13;
- an explicitly protected section is changed;
- an asset is optimized or replaced;
- a new deduplication/consolidation set is proposed;
- navigation or fragment targets are changed;
- the user reports missing information, imagery, references or functionality;
- the public candidate route differs from source-level expectations.

## Rollback

The current v13 release remains untouched. v14 and v15 remain separate historical candidates. v16.1 can be removed without changing v13 or the current preview route.
