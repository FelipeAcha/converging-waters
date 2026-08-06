# WL-REVIEW-EVIDENCE-001 — Reviewability before material approval

Status: CONFIRMED
Coverage: Converging Waters presentations, documents, websites, visual assets, and material content decisions
Owner: Project production and governance workflow
Activated: 2026-08-06

## Trigger

A material approval was requested for `CW-PRES-01` before Felipe had been given a complete, accessible review package containing the current artifact, the proposed exact delta, and the evidence needed to compare them.

The decision summary described the proposed architecture, but it did not provide a single review route with the source presentation, visual overview, exact proposed wording, preservation map, and direct artifact access. Felipe therefore could not reasonably approve or correct the work.

## Primary classification

- `OUTPUT_PRIORITY_FAILURE`
- `INSUFFICIENT_EVIDENCE`
- `MANUAL_STEP_NOT_TRACKED`
- `PREMATURE_CLOSURE`

## Root cause

- The approval request treated a planning summary as though it were a complete decision packet.
- Review evidence existed in separate locations, but it was not assembled and linked before the gate was presented.
- The operator action was defined as “approve” rather than “open and review this complete package, then approve or correct.”
- Gate readiness was evaluated from production-state knowledge rather than from the reviewer’s actual access and ability to verify the proposal.

## Permanent prevention rule

No material approval may be requested until the reviewer has one complete, accessible review packet.

The packet must include, as applicable:

1. the exact current source artifact or a direct stable link;
2. an immediately readable preview, montage, rendered PDF, screenshot set, or equivalent visual overview;
3. the exact proposed delta, not only a description of intent;
4. a complete `KEEP / CONSOLIDATE / REPLACE / ADD / LINK / ARCHIVE / REMOVE` map;
5. draft wording or visual specifications for every changed or new component;
6. a function-preservation matrix showing where displaced information will live;
7. source, confidence, consent, and representation labels for material claims;
8. version, archive, rollback, and no-touch boundaries;
9. the exact approval boundary and what approval does not authorize;
10. direct links to every document or asset the reviewer is expected to inspect.

The workflow must not assume that an artifact is reviewable merely because it exists in Drive, GitHub, the local runtime, or prior chat history. Access must be exposed in the same response that requests review.

## Approval-action rule

The first operator action for a material approval must be an observable review action:

> Open the named review package at the supplied link, inspect the listed artifacts in the stated order, and then approve or provide corrections.

“Approve” by itself is not an acceptable immediate action when the evidence package has not already been delivered and linked.

## Mandatory acceptance tests

Before requesting approval:

1. Confirm that each referenced artifact has a visible link or attached file.
2. Confirm that the current baseline and proposed result can be compared without searching previous messages.
3. Confirm that all changed and new components are shown with exact wording or sufficient visual specification.
4. Confirm that no removed or consolidated function disappears from the preservation matrix.
5. Confirm that archived material remains recoverable and is not represented as deleted.
6. Confirm that the reviewer can identify the exact source version and proposed next version.
7. Confirm that the approval statement names what it authorizes and what remains blocked.
8. Open or render locally generated review files before delivery and verify that they are readable.
9. Record failed link, missing-access, or incomplete-package checks as blockers rather than asking for approval.

## Presentation-specific minimum package

For a presentation gate, include:

- source PPTX link when available;
- current PDF;
- montage or slide thumbnails;
- exact slide-by-slide change map;
- proposed text and visual content for changed/new slides;
- final sequence and numbering;
- QA and rollback plan.

## Website-specific minimum package

For a website content gate, include:

- exact current deployment or preview URL;
- current HTML/source reference;
- desktop and mobile captures or an equivalent visual audit;
- section, claim, CTA, and graphic inventory;
- exact redundancy classification and proposed canonical home for each repeated concept;
- minimal code-diff plan;
- archive location for superseded graphics or content blocks;
- before/after validation criteria.

## Regression rule

A gate is not `READY_FOR_APPROVAL` when any required review artifact is missing, inaccessible, only referenced from prior chat history, or insufficient to understand the exact delta.

The gate must remain `PREPARED_FOR_REVIEW` until the complete package is delivered and its access is verified.

## Corrective implementation for CW-PRES-01

The correction is the `CW-PRES-01 Review Packet` dated 2026-08-06, containing:

- current v06 presentation PDF;
- 25-slide visual montage;
- full extracted text;
- exact 29-slide proposed sequence;
- exact draft content for every changed or new slide;
- function-preservation matrix;
- archive and version-control plan;
- explicit approval options and boundary.

## Rollback

This rule adds a review prerequisite and does not authorize content changes. If the rule proves unnecessarily heavy for a low-risk reversible decision, the packet may be proportionally simplified, but source access, exact delta, approval boundary, and reviewer-visible evidence remain mandatory.
