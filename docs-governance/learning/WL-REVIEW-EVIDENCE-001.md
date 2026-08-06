# WL-REVIEW-EVIDENCE-001 — Reviewability before material approval

Status: IMPLEMENTED
Coverage: Converging Waters presentations, documents, websites, visual assets, and material content decisions
Owner: Project production and governance workflow
Activated: 2026-08-06
Updated: 2026-08-06

## Trigger

A material approval was requested for `CW-PRES-01` before Felipe had been given a complete, accessible review package containing the current artifact, the proposed exact delta, and the evidence needed to compare them.

The decision summary described the proposed architecture, but it did not provide a single review route with the source presentation, visual overview, exact proposed wording, preservation map, and direct artifact access. Felipe therefore could not reasonably approve or correct the work.

A subsequent correction generated a ZIP bundle even though Felipe reviews preliminary versions directly inside ChatGPT using its native document viewers. The ZIP added an unnecessary download, duplicated files, and created avoidable local-storage burden.

## Primary classification

- `OUTPUT_PRIORITY_FAILURE`
- `INSUFFICIENT_EVIDENCE`
- `MANUAL_STEP_NOT_TRACKED`
- `PREMATURE_CLOSURE`
- `EXCESSIVE_CAUTION_COST`

## Root cause

- The approval request treated a planning summary as though it were a complete decision packet.
- Review evidence existed in separate locations, but it was not assembled and linked before the gate was presented.
- The operator action was defined as “approve” rather than “open and review this complete package, then approve or correct.”
- Gate readiness was evaluated from production-state knowledge rather than from the reviewer’s actual access and ability to verify the proposal.
- “Complete package” was interpreted as a downloadable bundle rather than complete review access in the user’s actual working surface.
- Delivery optimization did not account for duplicate downloads, local disk usage, or the fact that preliminary review occurs inside ChatGPT.

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
10. direct access to every document or asset the reviewer is expected to inspect.

The workflow must not assume that an artifact is reviewable merely because it exists in Drive, GitHub, the local runtime, or prior chat history. Access must be exposed in the same response that requests review.

## Review delivery and storage discipline

- The default surface for reviewing preliminary versions is the current ChatGPT conversation using native viewers, inline attachments, or individual artifact links.
- Do not create or recommend ZIP files, download bundles, duplicate folders, or consolidated export packages by default.
- Create a ZIP or equivalent bundle only when Felipe explicitly requests it or when a verified external handoff requires multiple files to be transferred together.
- Even for an external handoff, prefer a single standard artifact or individual stable links when they satisfy the real delivery need better than a ZIP.
- Do not regenerate, duplicate, re-export, or repackage preliminary artifacts that Felipe is already reviewing unless a content correction, format correction, access failure, or gate requirement makes regeneration necessary.
- Minimize local disk burden and artifact proliferation. Review completeness means that all necessary evidence is accessible, not that every item has been downloaded or bundled.
- Present only the priority review sequence and the exact artifacts needed for the current decision. Supporting evidence remains accessible but should not obscure the primary review task.

## Approval-action rule

The first operator action for a material approval must be an observable review action:

> Open the named review artifact in the current ChatGPT conversation, inspect the listed priority items in the stated order, and then approve or provide corrections.

“Approve” by itself is not an acceptable immediate action when the evidence package has not already been delivered and linked.

## Mandatory acceptance tests

Before requesting approval:

1. Confirm that each referenced artifact has a visible link, attachment, or native ChatGPT viewer.
2. Confirm that the current baseline and proposed result can be compared without searching previous messages.
3. Confirm that all changed and new components are shown with exact wording or sufficient visual specification.
4. Confirm that no removed or consolidated function disappears from the preservation matrix.
5. Confirm that archived material remains recoverable and is not represented as deleted.
6. Confirm that the reviewer can identify the exact source version and proposed next version.
7. Confirm that the approval statement names what it authorizes and what remains blocked.
8. Open or render locally generated review files before delivery and verify that they are readable.
9. Record failed link, missing-access, or incomplete-package checks as blockers rather than asking for approval.
10. Confirm that no ZIP or bundle is being created unless it was explicitly requested or a documented external handoff requires it.
11. Confirm that already accessible preliminary artifacts are not being regenerated or duplicated without a concrete corrective need.
12. Confirm that the first review instruction identifies the smallest priority set the reviewer must inspect now.

## Presentation-specific minimum packet

For a presentation gate, provide inside ChatGPT:

- source PPTX link when available;
- current PDF in a native viewer;
- montage or slide thumbnails when they materially accelerate review;
- exact slide-by-slide change map;
- proposed text and visual content for changed/new slides;
- final sequence and numbering;
- QA and rollback plan.

Do not package these into a ZIP unless explicitly requested or required for external transmission.

## Website-specific minimum packet

For a website content gate, provide inside ChatGPT:

- exact current deployment or preview URL;
- current HTML/source reference;
- desktop and mobile captures or an equivalent visual audit;
- section, claim, CTA, and graphic inventory;
- exact redundancy classification and proposed canonical home for each repeated concept;
- minimal code-diff plan;
- archive location for superseded graphics or content blocks;
- before/after validation criteria.

Do not create a downloadable site bundle merely for review when the native preview and source references are sufficient.

## Regression rule

A gate is not `READY_FOR_APPROVAL` when any required review artifact is missing, inaccessible, only referenced from prior chat history, or insufficient to understand the exact delta.

A review handoff also fails when it creates an unrequested ZIP, duplicate export, unnecessary local download, or redundant regeneration of an artifact already accessible in ChatGPT.

The gate must remain `PREPARED_FOR_REVIEW` until the complete evidence is accessible through the appropriate review surface and the priority review instruction is explicit.

## Corrective implementation for CW-PRES-01

The current `CW-PRES-01` review materials remain valid and must not be regenerated. Felipe will review the latest individual artifacts directly through ChatGPT’s viewers.

The immediate review priority is:

1. the proposed 29-slide sequence and `KEEP / CONSOLIDATE / REPLACE / ADD / LINK / ARCHIVE` map;
2. the exact draft content for changed and new slides;
3. the function-preservation matrix and approval boundary.

The previously generated ZIP is not a required review route and must not be regenerated.

## Rollback

This rule changes only the review-delivery workflow. It does not modify presentation or website content. If native ChatGPT viewing is unavailable for a required format, provide the smallest alternative artifact needed for access; do not default to a broad bundle.
