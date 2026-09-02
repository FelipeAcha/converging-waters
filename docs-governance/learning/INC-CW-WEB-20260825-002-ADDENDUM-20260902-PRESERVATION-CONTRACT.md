# INC-CW-WEB-20260825-002 — Addendum 2026-09-02: approved-baseline preservation contract

**Parent incident:** `INC-CW-WEB-20260825-002`  
**Classification:** SCOPE_DRIFT / UNNECESSARY_REBUILD / BEHAVIOR_REGRESSION_FROM_GENERIC_STANDARD  
**Status:** CORRECTED IN PROJECT SPEC · BEHAVIOR VERIFICATION PENDING

## Failure

During planning for the ally-facing website recovery, generic UX guidance was elevated above the already-developed hub and the user's preservation intent. Two concrete rules were introduced without user authorization:

1. a mandatory separately visible conclusion/summary even when the existing heading already communicated the point;
2. a prohibition on nested accordions, despite nested disclosure already existing and working in the mature hub.

The same planning pass also drifted toward summarizing/removing mature homepage material instead of preserving the existing implementation and changing only current-status, audience-wrapper and internal-development language.

## Root cause

Generic design guidance was treated as permission to refactor a mature approved implementation. The governing order should have been:

`explicit current user decision > approved project-specific baseline/contract > generic UX preference`.

This is a recurrence of the parent incident's preserve-and-repair lesson and therefore remains attached to the existing incident rather than creating a separate reliability chain.

## Corrected contract

The project-specific authority is now:

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

A recovery candidate must fail if any of the following occurs without explicit authorization:

1. source HTML is reconstructed instead of copied from the exact mature baseline;
2. an existing accordion/disclosure marker disappears, changes nesting or changes default behavior;
3. a new mandatory summary paragraph is inserted solely to satisfy a generic template;
4. Alliance Architecture layout, palette, matrix structure or unaffected cells change;
5. the major infographic changes beyond the explicitly authorized current-status exception;
6. a useful finding disappears because its meeting/changelog wrapper was removed;
7. a deep dive is used as justification to delete substantial homepage content;
8. an untouched DOM/text/link/asset block changes outside the declared delta.

## Acceptance evidence still required

This addendum is **corrected and persisted**, not yet behavior-verified. Verification requires the next recovery candidate to:

- start from the exact mature source;
- pass source/candidate hash equivalence before the first patch;
- preserve the existing disclosure structure;
- run the project-specific Definition of Done and preservation manifest against every bounded delta;
- pass final browser and user-preview review before promotion.
