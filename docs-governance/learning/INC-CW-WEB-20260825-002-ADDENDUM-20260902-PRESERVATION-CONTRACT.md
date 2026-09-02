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