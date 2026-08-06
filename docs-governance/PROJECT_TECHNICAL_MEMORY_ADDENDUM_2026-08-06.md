# Converging Waters — Technical Memory Addendum — 2026-08-06

Status: `ACTIVE — CANONICAL ADDENDUM`
Owner: Felipe Acha
Parent memory: `PROJECT_TECHNICAL_MEMORY.md`

This addendum forms part of the canonical Converging Waters technical memory until its decision records are consolidated into the parent file. It does not replace prior decisions.

## New confirmed decisions

| ID | Decision | Status |
|---|---|---|
| CW-D020 | Google Drive is the intended authoritative system for editable Converging Waters project artifacts, operational files, current exports, and their version histories. GitHub remains authoritative for website source/deployment, technical governance, policies, handoffs, validators, hashes, and reproducible evidence. | CONFIRMED |
| CW-D021 | A living artifact must normally preserve one stable Drive file ID and URL. Routine revisions must update the existing native Google file or replace the bytes of the existing uploaded file. A separate file is permitted only for explicit comparison, a materially different use, an immutable release/submission, an evidentiary requirement, an incompatible boundary, or an approved rollback. | CONFIRMED |
| CW-D022 | Every image generated or edited at Felipe's request must be persisted in Drive and entered in the version ledger before completion is claimed. The first version creates the master file; later edits update the same Drive file ID unless an explicit side-by-side variant or frozen release is required. | CONFIRMED |
| CW-D023 | The project will maintain one `Converging Waters — Asset Register & Version Ledger` with `Assets`, `Versions`, `Relationships`, `Exceptions`, and `Controlled Values` tabs. The register uses Drive file IDs as identity and logs change summaries, revision IDs, retention, source, readback, and rollback. | CONFIRMED |
| CW-D024 | Review, approved, published, submitted, and legal-record milestones require explicit retention evidence: named versions for native Google files when supported, and `Keep forever` for material uploaded-file revisions when supported. Provider-default blob history is not treated as permanent archival retention. | CONFIRMED |
| CW-D025 | No Drive persistence, revision, retention, or registration may be claimed without connector or UI evidence. When Drive access is unavailable, artifacts and ledger rows remain `PREPARED` or `BLOCKED`, with exact migration and readback work preserved. | CONFIRMED |

## Skill overlap decision

The installed Skill review produced this boundary:

- `norte-solar-document-governance` contains useful patterns but is hard-coded to Norte Solar organization codes, families, correlatives, states, and folders. It must not govern Converging Waters directly.
- `workstream-governance` owns Projects, workstreams, conversations, routing, and inventory topology; it does not own file revision history.
- `incremental-control` owns authorization, gates, readback, rollback, and canonical impact; it does not define Drive artifact identity or version semantics.
- `workflow-learning` owns failure classification and prevention after an omitted or incorrect save/version action.
- `skill-release-assurance` owns Skill package lifecycle, not project documents.

Decision: create a separate generic Skill, `drive-artifact-governance`, and keep Converging Waters-specific policy and inventory in this project. The generic Skill is prepared, validated, and packaged; it is not yet installed, invoked, behavior-tested, or verified.

## Current implementation evidence

- Root governance index created at `GOVERNANCE.md`.
- Governance-directory index created at `docs-governance/README.md`.
- Representation-validation packet created at `docs-governance/validation/CW-G1-REPRESENTATION-VALIDATION.md`.
- Drive policy created at `docs-governance/standards/DRIVE_ARTIFACT_VERSIONING_POLICY.md`.
- Bootstrap asset and version CSVs created under `docs-governance/registries/`.
- A local XLSX register was prepared with an initial 45-asset staging inventory and 45 initial version records.
- The generic Skill package passed Skill Creator validation, its positive record test passed, its invalid duplicate-master test was rejected, the release packet validated, and the package tree contains one Skill.

## Current blockers and open work

- The Google Drive connector is unavailable in the current execution environment.
- The authoritative Drive folder has not yet been recursively audited.
- Existing files have not yet been reconciled to Drive file IDs, revision IDs, ownership, parent folders, or retention states.
- UUID-named generated PNGs require visual/context mapping before they receive stable conceptual asset IDs.
- The XLSX register is prepared but not yet imported as the Drive-native Google Sheet.
- The `drive-artifact-governance` Skill is not yet installed or behavior-tested.

## CW-G1 continuation

The active project gate remains `CW-G1 / CW-PRES-01`.

The representation packet is ready. Human validation remains required for:

- the three-initiative architecture;
- each of the six individual profiles;
- authority and public-use boundaries;
- time and resource availability;
- the exact shared purpose;
- the first shared result;
- external representation and credit rules.

Unanswered fields remain open and must not be inferred.
