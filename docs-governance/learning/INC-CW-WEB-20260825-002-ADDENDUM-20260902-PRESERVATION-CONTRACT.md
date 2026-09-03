# INC-CW-WEB-20260825-002 — Addendum 2026-09-02: approved-baseline preservation contract

**Parent incident:** `INC-CW-WEB-20260825-002`  
**Classification:** SCOPE_DRIFT / UNNECESSARY_REBUILD / BEHAVIOR_REGRESSION_FROM_GENERIC_STANDARD  
**Status:** CORRECTED · PRESERVATION REGRESSIONS BEHAVIOR-VERIFIED · USER APPROVAL PENDING

## Failure

During planning for the ally-facing website recovery, generic UX guidance was elevated above the already-developed hub and the user's preservation intent. Two concrete rules were introduced without user authorization:

1. a mandatory separately visible conclusion/summary even when the existing heading already communicated the point;
2. a prohibition on nested accordions, despite nested disclosure already existing and working in the mature hub.

The same planning pass also drifted toward summarizing/removing mature homepage material instead of preserving the existing implementation and changing only current-status, audience-wrapper and internal-development language.

## Root cause

Generic design guidance was treated as permission to refactor a mature approved implementation. The governing order is:

`explicit current user decision > approved project-specific baseline/contract > generic UX preference`.

This is a recurrence of the parent incident's preserve-and-repair lesson and therefore remains attached to the existing incident rather than creating a second GitHub reliability chain.

## Corrected contract

The project-specific authority is:

`docs-governance/standards/CW_WEB_DEFINITION_OF_DONE_v1.md`

Hard corrections:

- source code strategy = patch the existing mature HTML; never regenerate;
- default action = KEEP;
- progressive disclosure = preserve current implementation in the recovery pass;
- nested accordions = allowed and protected;
- separate visible summary = not mandatory when the heading/title already communicates the point;
- major infographic = preserve essentially unchanged, with only bounded current-status corrections;
- Alliance Architecture/matrix = protected; status changes only;
- Amazonas Sagrada = potential ally;
- Maria Gracia = potential ally;
- Canchis = no new re-research during this recovery pass;
- internal/version/ChatGPT/development wrappers = remove only after harvesting all ally-relevant substance;
- redundancy and natural-language checks = required, but they do not authorize destructive restructuring.

## Regression requirements

A recovery candidate fails if any of the following occurs without explicit authorization:

1. source HTML is reconstructed instead of copied from the exact mature baseline;
2. an existing accordion/disclosure marker disappears, changes nesting or changes default behavior;
3. a new mandatory summary paragraph is inserted solely to satisfy a generic template;
4. Alliance Architecture layout, palette, matrix structure or unaffected cells change;
5. the major infographic changes beyond the explicitly authorized current-status exception;
6. a useful finding disappears because its meeting/changelog wrapper was removed;
7. a deep dive is used as justification to delete substantial homepage content;
8. an untouched DOM/text/link/asset block changes outside the declared delta.

## Behavior-verification evidence

Final review candidate:

- Drive ID: `1yqkMDDeB1DUjmktMdxk_oZMj9JsbJCrc`
- SHA-256: `0da596869b6adcb97fd45a257bfca41f2f15f8a2441da4b21135bac41ab7a73b`
- final QA: `docs-governance/validation/CW-WEB-ALLY-RECOVERY-FINAL-QA-2026-09-02.md`

Fresh deterministic audit and exact Chromium render verified:

- exact mature source was copied before the first patch;
- section order preserved;
- 27/27 existing disclosure structures, summary labels and default states preserved;
- 97 external hrefs preserved in order;
- 19 image src/alt/title records preserved;
- CSS rules preserved, with only development comments removed;
- Alliance matrix remains 49 rows / 269 cells and only the Amazonas Sagrada row differs from the mature source;
- WGA and Willkamayu remain the two cards in the major initiative graphic after the authorized Amazonas core-node removal;
- current Canchis evidence was retained without re-research;
- desktop/mobile exact-source browser QA passed with zero document-level overflow, zero broken images and zero accordion toggle failures.

The preservation regression also caught a proposed change to the existing `Invite list to confirm` disclosure label during final ally-facing cleanup. That attempted change failed the disclosure-structure audit and was reverted before checkpointing. This demonstrates that the project-specific preservation control is active rather than merely documented.

## Remaining lifecycle boundary

The prevention is **behavior-verified on the current recovery candidate**. It is not yet the final public release because:

- `USER_APPROVED=false`;
- `PROMOTED=false`;
- the current main/public authoritative route has not been changed.

Final user review and explicit approval remain the next gate before any promotion.

## Later recurrence — REV06 point-level visual and comprehension gap

A later named review candidate exposed a narrower recurrence that the broader preservation checks did not catch:

- **Point 18** and **Point 19** were visibly misaligned in the exact review surface even though structural/browser checks had passed;
- **Point 15** used a separate `Mechanism menu already in the work` note that was technically present but conceptually redundant and harder to understand than the established card grammar.

The user screenshot is authoritative evidence of the visible defect. A source-level assumption that adjacent headings share the same layout contract is not enough when the exact rendered result differs.

### Root cause extension

The regression suite checked global structure, counts, links, resources and page overflow, but it did not encode the **specific observable constraint** the user was judging: the left-edge relationship between Points 18 and 19. It also did not encode the intended comprehension behavior for Point 15: financing functions and concrete mechanisms should be integrated into one readable visual structure rather than split between cards and a redundant note.

### Corrected prevention

For point-level visual or interaction feedback:

1. convert the exact user-observable discrepancy into a browser metric or behavior assertion whenever practical;
2. a user screenshot that contradicts a PASS invalidates the relevant PASS until reconciled;
3. preserve the existing visual grammar when it can carry the additional information more clearly than a new standalone explanatory layer;
4. keep the correction bounded to the named visible points and re-run preservation checks on adjacent protected blocks.

REV06A implements this as:

- Point 18/19 left-edge delta must be `<= 1px` on the exact live desktop/mobile review route;
- Point 15 must expose exactly four financing-route cards and the legacy mechanism-menu note must be absent;
- Alliance Architecture, Precedents and Specialist Deep Dives remain protected outside the authorized delta.

### Verification

**CW-ALLY-REV06A — Alignment + Financing Clarity**:

- authoritative raw SHA-256: `d5a73de694756bfc3f4efbf62cb98ba4d72a9052dca178e7d45a0ac0cd0958c0`;
- exact raw Drive readback: PASS;
- ACB run: `33701191061`;
- desktop Point 18 / Point 19 left edges: `130px / 130px`, delta `0px`;
- mobile Point 18 / Point 19 left edges: `14px / 14px`, delta `0px`;
- Point 15 financing-route cards: `4`;
- legacy financing mechanism menu: absent;
- exact live desktop/mobile active-candidate browser contract: PASS.

Canonical reliability event: `REL-20260902-CW-WEB-REV06A-VISUAL-CLARITY-001`.
