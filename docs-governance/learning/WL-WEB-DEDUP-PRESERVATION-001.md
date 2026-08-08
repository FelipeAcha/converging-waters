# WL-WEB-DEDUP-PRESERVATION-001 — Deduplicate without content or asset loss

Status: IMPLEMENTED — PUBLIC ROUTE VERIFIED / CHAT VISUALIZER NOT YET VERIFIED
Owner: Project production and governance workflow
Activated: 2026-08-07
Updated: 2026-08-08
Coverage tier: TOOL_OR_VALIDATOR

## Trigger

A proposed website deduplication candidate was generated after the user explicitly required that no unique information be lost and that all Stanley / WGA material, apparatus examples, reference cards, images and links remain. The candidate was built from a reconstructed structural subset rather than from the exact authoritative v13 source. It therefore removed material that the user had explicitly protected, including the full Stanley / WGA apparatus and reference section shown in the authoritative website.

A later candidate passed source-level preservation checks but still did not satisfy the user's user-visible review expectation. The v16.1 route used a client-side loader even though automated browser checks passed; Felipe reported that he could not see the web. The static v16.1.1 public route then passed browser checks, but Felipe still reported that the web was not visible in the ChatGPT conversation visualizer. This establishes that source/hash preservation, public HTTP success and headless rendering are not sufficient for the actual review workflow. The in-chat visual review surface is itself a required acceptance criterion.

## Primary classification

- `INSUFFICIENT_EVIDENCE`
- `ASSUMED_COMPLETION`
- `OUTPUT_PRIORITY_FAILURE`
- `UNNECESSARY_REBUILD`
- `SCOPE_DRIFT`
- `TOOL_CONTRACT_MISMATCH`
- `SURFACE_AMBIGUITY`

## First control failures

1. The original deduplication operation did not begin from the exact authoritative HTML and asset set.
2. A semantic preservation claim was made without a deterministic comparison proving that protected sections, images, links and retained source blocks were unchanged.
3. A source/headless regression pass was treated as sufficient proof of user-visible review delivery even though the candidate depended on a client-side loader.
4. A successful public GitHub Pages route was then treated as sufficient review delivery even though Felipe's required review surface is the ChatGPT conversation visualizer. Public-route verification and in-chat visualization are separate lifecycle states and must never be conflated.

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
16. Review candidates must be directly viewable static HTML with local project assets whenever possible. Do not insert a client-side ZIP loader, remote decompression dependency, iframe, redirect chain or other delivery layer merely to expose a review candidate.
17. `HTTP 200` and headless rendering do not override a user's exact-surface report that the candidate is not viewable. At the first such contradiction, retire that delivery route and create the smallest replacement without asking the user to retry it.
18. Every website candidate submitted for Felipe's review must also be available in the current ChatGPT Project conversation as an in-chat visualizer artifact. A GitHub Pages URL is supplemental evidence, not a substitute for the in-chat review surface.
19. Do not advance from `v16.x` to the next subversion, do not request content approval, and do not start another website delta until the current candidate has an accessible in-chat visualizer artifact on the exact conversation surface. If this cannot be produced, mark the gate `BLOCKED — CHAT_VISUALIZER_DELIVERY` and make no further website-content mutation.
20. The in-chat visualizer copy must be generated from the exact candidate, with transport-only changes when required for sandbox display. It must preserve visible content, section order, images and links. It must not be a screenshot-derived recreation, semantic reconstruction or approximate rendering.
21. Each incremental subversion carries one user-authorized delta and one approval gate: `baseline → single delta → deterministic preservation test → browser test → in-chat visualizer → user review → next delta`.
22. Any future web-specific Skill or workflow must compose with Incremental Control and Workflow Learning rather than duplicate them. Incremental Control owns one-delta gating and approval boundaries; Workflow Learning owns failure classification and prevention; the web-specific layer owns HTML/assets/links/render/visualizer invariants.

## Current hard lock — Stanley / WGA

The complete `stanley-update` section remains protected. It includes the full apparatus/reference area: sample + sequence; context + verify; learn + steward; portable field science; Sacred Valley possibility; design principle; ecosystem atlas/metagenome patterns; small field computers; sensor + metadata nodes; citizen-science bioacoustics; autonomous field systems; portable sequencing in context; WGA public/data/academy/storytelling links; the four-step technical-next-step sequence; and the final clarification band.

## v16.1.1 step-1 contract

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
- all external href values match v13 exactly in count, order and value;
- candidate is static HTML and local assets, not a client-side loader;
- exact public candidate route returns and renders the static page directly;
- an equivalent in-chat visualizer artifact is delivered before any further website-content delta.

Verified behavior evidence:

- v16.1 dynamic delivery: superseded after Felipe reported the page was not visible on his review surface.
- static v16.1.1 source commit: `37071fabf430af3f10dd44743bfce0737d722a8d`
- static candidate path: `docs/candidates/v16.1.1/`
- public Pages deployment run: `31274518173`; deployment and public-route validation passed.
- direct public visibility regression run: `31274560599` — SUCCESS.
- direct static candidate check: PASS; no v16.1 loader string served.
- Stanley / WGA rendered markers: PASS.
- ChatGPT conversation visualizer: NOT YET VERIFIED; Felipe explicitly reported that the web is not visible there.

## Current candidate routing

- v13 remains the authoritative baseline and current preview source.
- v14 and v15 remain historical/rejected or superseded review candidates and must not be used as the source for the next recovery step.
- v16.1 remains preserved as the failed dynamic-delivery attempt.
- v16.1.1 is the current incremental candidate for infographic placement/deduplication only.
- Current gate: `BLOCKED — CHAT_VISUALIZER_DELIVERY`.
- No v16.2 content work may start until v16.1.1 is available in the current ChatGPT Project conversation visualizer.
- Further content changes must create v16.2, v16.3, etc., each with one explicitly requested delta unless Felipe explicitly authorizes batching.

## Revalidation triggers

Re-run the preservation regression whenever:

- a new authoritative website baseline supersedes v13;
- an explicitly protected section is changed;
- an asset is optimized or replaced;
- a new deduplication/consolidation set is proposed;
- navigation or fragment targets are changed;
- the user reports missing information, imagery, references or functionality;
- the public candidate route differs from source-level expectations;
- a review route introduces any new loader, external rendering dependency or redirect layer;
- the in-chat visualizer differs from the exact candidate or cannot be opened on the current conversation surface.

## Rollback

The current v13 release remains untouched. v14, v15 and v16.1 remain separate historical candidates. v16.1.1 can be removed without changing v13 or the current preview route.
