# ADR-CW-001 — Drive Artifact Governance Capability

Date: 2026-08-06
Status: `ACCEPTED — SKILL PREPARED, INSTALLATION OPEN`
Owner: Felipe Acha / AI_OS governance

## Decision

Create a new generic Skill named `drive-artifact-governance` and apply a Converging Waters-specific policy and register profile outside the Skill.

## Problem

Converging Waters needs a repeatable control that ensures:

- every living Drive artifact has one stable file identity;
- routine revisions update the same file rather than create duplicates;
- native Docs, Sheets, and Slides use their version history;
- uploaded images, PDFs, Office files, HTML, and packages use Drive revisions;
- generated and edited AI images are persisted and logged;
- review, approved, published, and legal milestones receive retention treatment;
- a project Asset Register and Version Ledger records every material change;
- completion is not claimed before Drive and ledger readback.

## Options reviewed

### 1. Reuse `norte-solar-document-governance` directly

Rejected.

It contains valuable document-authority, master/derivative, naming, folder, lifecycle, and readback patterns, but it is explicitly bound to Norte Solar codes, families, correlatives, and folder taxonomy. Direct reuse would create project leakage and false authority.

### 2. Extend `workstream-governance`

Rejected as the owner of this capability.

That Skill governs Project/workstream/conversation routing, topology, continuity, and inventories. It does not own file bytes, Drive revisions, retention, or artifact version logs.

### 3. Put the rules only in `incremental-control`

Rejected as the primary owner.

Incremental Control correctly owns authorization, gates, evidence, rollback, readback, and canonical impact. Adding Drive-specific artifact semantics would make it overly broad and duplicate a domain capability.

### 4. Create `drive-artifact-governance`

Accepted.

A separate generic Skill creates a reusable boundary for all projects while allowing project-specific profiles, names, folders, and codes to remain in their owning systems.

## Boundary

`drive-artifact-governance` owns:

- stable Drive file identity;
- native versus blob update path;
- same-file revision rule;
- AI-generated image persistence;
- milestone retention state;
- Asset Register and Version Ledger;
- revision readback and rollback IDs;
- duplicate/variant/snapshot classification.

It does not own:

- organization-specific filename codes or folder taxonomies;
- Project or conversation routing;
- material authorization or gate approval;
- Skill package release lifecycle;
- institutional learning classification;
- website deployment.

## Transition

1. Apply the project policy in `DRIVE_ARTIFACT_VERSIONING_POLICY.md`.
2. Use the bootstrap inventory to create the Drive-native register.
3. Install the packaged generic Skill.
4. Run post-install positive, negative, and boundary tests.
5. Reconcile the authoritative Drive folder by file ID and revision.
6. Patch organization-specific document-governance Skills later to delegate same-file version behavior to the generic Skill, without importing project-specific taxonomy.

## Evidence

- Skill package: `skill.zip`
- Package SHA-256: `6714a55c560a566802d7d9589eeb22717db6b3bd020079a5218c9d7b9663fa04`
- Package size: `13,981 bytes`
- Package files: `10`
- Skill Creator validation: `PASS`
- Valid version-record test: `PASS`
- Unjustified duplicate-master test: `REJECTED AS EXPECTED`
- Release-assurance packet: `PASS`
- Package-tree validation: `PASS`

## Lifecycle state

- Specified: yes
- Implemented in source: yes
- Validated: yes
- Packaged: yes
- Delivered: pending this response
- Installed: no evidence
- Invoked: no evidence
- Behavior-tested after installation: no
- Verified: no

## Rollback

Do not install the new Skill, or remove only `drive-artifact-governance` if post-install behavior fails. Existing Skills remain unchanged. Preserve the package hash, project policy, and inventory evidence for diagnosis.
