# Converging Waters — Drive Artifact Versioning Policy

Status: `ACTIVE — IMPLEMENTATION PARTIAL`
Owner: Felipe Acha
Applies to: documents, spreadsheets, presentations, PDFs, Office files, HTML, datasets, images, AI-generated visuals, exports, and packages produced or maintained for Converging Waters.

## 1. Authority model

- **Google Drive** is the intended authoritative system for editable project artifacts, operational files, current exports, and their version histories.
- **GitHub** is authoritative for website source and deployment, technical governance, structured policies, durable handoffs, validators, hashes, and reproducible evidence.
- A GitHub bootstrap register is staging evidence until reconciled into the Drive register.
- Chat attachments and local generated files are not durable authority.

## 2. Stable-file rule

One living artifact must have one stable Drive identity.

When an artifact already exists:

- preserve its Drive `fileId` and URL;
- edit a native Google Doc, Sheet, or Slide in place;
- replace the bytes of PDFs, images, Office files, HTML, ZIPs, or other uploaded files on the same Drive file ID;
- record the version in the project ledger;
- do not create routine `v02`, `v03`, `FINAL`, `FINAL-2`, or similarly duplicated files merely to preserve history.

Create a separate file only for:

1. explicit side-by-side comparison;
2. a materially different audience or use;
3. an immutable approved or published snapshot;
4. an external submission that must remain frozen;
5. legal, audit, contractual, or evidentiary retention;
6. incompatible format, ownership, or permission boundary;
7. an approved destructive-migration rollback.

Every exception must be logged with owner, reason, approval, and review trigger.

## 3. Master, derivative, snapshot, variant, and reference

Use these classes:

- `MASTER_NATIVE` — authoritative Google Doc, Sheet, or Slide.
- `MASTER_BLOB` — authoritative uploaded file updated in place.
- `DERIVATIVE_CURRENT` — latest export refreshed in place, linked to its master.
- `RELEASE_SNAPSHOT` — intentionally frozen milestone copy.
- `VARIANT` — parallel alternative required for review or separate use.
- `REFERENCE` — received or external source preserved without becoming the editable authority.

A PDF export is not the master when an editable source exists. A generated image visible in chat is not the Drive master until its Drive file ID and revision are verified.

## 4. Version-history rules

### Native Google files

- edit the existing file through Docs, Sheets, or Slides;
- obtain pre-write and post-write revision or modified-time evidence;
- use a named version for review, approval, publication, submission, or other material milestones when the available surface supports it;
- record the version label and readback in the ledger even when the provider groups revisions.

### Uploaded files and images

- use the existing Drive file ID and upload/replace the new bytes as a revision;
- list revisions after the update;
- record the new and previous revision IDs;
- mark approved, published, submitted, or legal-record revisions `Keep forever` when supported;
- never claim permanent retention when the `Keep forever` action was not executed and verified.

Google states that unretained blob revisions may be removed after 30 days or after 100 newer unretained revisions; up to 200 blob revisions may be marked `Keep forever`. Therefore, provider-default history is not an archival policy.

## 5. AI-generated visual rule

Every image generated or edited at Felipe's request must enter this workflow before completion is claimed:

1. identify the conceptual asset and existing Drive master, if any;
2. for the first version, create one stable Drive file and register its file ID;
3. for later edits, replace the bytes on that same file ID;
4. create a separate file only for an explicit comparison variant or frozen release;
5. record the prompt or edit instruction, source conversation, exposed model label, dimensions, checksum when available, change summary, Drive revision, previous revision, and rollback target;
6. complete Drive and ledger readback.

Do not invent seeds, hidden model versions, or generation parameters that were not exposed.

## 6. Project register

Maintain one Google Sheet named:

`Converging Waters — Asset Register & Version Ledger`

Required tabs:

- `Assets` — one current row per stable asset identity.
- `Versions` — one append-only row per material version.
- `Relationships` — master, derivative, snapshot, variant, and source relationships.
- `Exceptions` — approved deviations from the stable-file rule.
- `Controlled Values` — allowed classes, statuses, retention tiers, and change types.

The initial workbook and CSV bootstrap files were prepared on 2026-08-06. Their current state is `PREPARED`, not yet a Drive-native register.

## 7. Retention tiers

- `WORKING` — provider-default history for routine edits.
- `REVIEW` — named/checkpointed review version.
- `APPROVED` — named version or retained blob revision plus approval evidence.
- `PUBLISHED` — approved retention plus publication or submission evidence.
- `LEGAL_RECORD` — retained revision, checksum, custodian, access state, and evidentiary metadata.

## 8. Naming practice

A living master should normally retain a stable descriptive name without routine version numbers:

`Converging Waters — [Artifact Title].[ext]`

The ledger carries `v01`, `v02`, and later labels. Separate snapshot or variant files may include:

- `— Variant A`
- `— Review Snapshot — YYYY-MM-DD`
- `— Approved Release — vNN`
- `— External Submission — YYYY-MM-DD`

Existing version-numbered files are not renamed until Drive IDs, ownership, links, dependencies, and comparison needs have been audited.

## 9. Required readback

An update is incomplete until all applicable states pass:

`PREPARED → UPLOADED_OR_UPDATED → REVISION_OBSERVED → REGISTERED → RETAINED → READ_BACK → VERIFIED`

Required evidence:

- Drive file ID and URL;
- parent folder;
- MIME type;
- current revision or modified time;
- previous revision / rollback target;
- change summary;
- retention status;
- asset-register row;
- version-ledger row;
- post-write readback.

## 10. Current implementation state

- GitHub governance indexes: implemented.
- CW-G1 validation packet: implemented and awaiting human validation.
- Drive versioning policy: implemented in GitHub.
- Asset Register and Version Ledger workbook: prepared locally with an initial 45-asset staging inventory.
- Google Drive register creation, folder audit, file-ID reconciliation, and revision migration: `BLOCKED` because the Google Drive connector is unavailable in the current execution environment.
- Any proposed reusable Skill or automation is an AI_OS / Start Digital transfer candidate, not an implementation state or deliverable of Converging Waters.

No file is represented as uploaded, versioned, retained, or registered in Drive until connector or UI evidence confirms it.

## 11. Official Google references

- Drive file activity and non-Google file versions: https://support.google.com/drive/answer/2409045
- Docs, Sheets, and Slides version history and named versions: https://support.google.com/docs/answer/190843
- Drive API upload/update guidance: https://developers.google.com/workspace/drive/api/guides/manage-uploads
- Drive API revision management and retention: https://developers.google.com/workspace/drive/api/guides/manage-revisions

## 12. Review triggers

Review this policy when:

- a Drive connector exposes new revision or named-version actions;
- the project moves to a Shared Drive;
- ownership or access rules change;
- legal or funder retention requirements arise;
- more than one master is detected for the same logical asset;
- a generated artifact is delivered without Drive persistence or ledger registration;
- AI_OS returns a verified reusable control that Felipe explicitly approves for use in Converging Waters.
