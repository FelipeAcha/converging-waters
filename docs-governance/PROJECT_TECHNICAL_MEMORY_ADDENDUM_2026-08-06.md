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
| CW-D026 | All work concerning Skills — including comparison, design, improvement, creation, packaging, installation, release, testing, or verification of `Conversation Branch Organizer` and any other reusable Skill — belongs to Optimización Stack Digital / AI_OS. Converging Waters may identify requirements, failure modes, or improvement candidates and prepare a transfer note, but must not treat Skill development or lifecycle as a Converging Waters deliverable. | CONFIRMED |

## Skill-routing correction

The substantive project requirements remain valid, but Skill implementation is out of scope here.

- The `Conversation Branch Organizer` discussion and any proposed evolution toward conversation architecture must be transferred to Optimización Stack Digital / AI_OS.
- Any future proposal for a reusable Drive-governance Skill must likewise be reviewed, designed, packaged, installed, and tested in Optimización Stack Digital / AI_OS.
- Converging Waters may state what behavior it needs from a future Skill, but the canonical project memory records only the project requirement and the transfer destination.
- No Skill is represented here as prepared, packaged, delivered, installed, invoked, behavior-tested, or verified.
- The Converging Waters Drive policy, asset register, version ledger, and CW-G1 validation packet remain project records independent of whether AI_OS later supplies reusable automation.

## Current implementation evidence

- Root governance index created at `GOVERNANCE.md`.
- Governance-directory index created at `docs-governance/README.md`.
- Representation-validation packet created at `docs-governance/validation/CW-G1-REPRESENTATION-VALIDATION.md`.
- Drive policy created at `docs-governance/standards/DRIVE_ARTIFACT_VERSIONING_POLICY.md`.
- Bootstrap asset and version CSVs created under `docs-governance/registries/`.
- A local XLSX register was prepared with an initial 45-asset staging inventory and 45 initial version records.

## Current blockers and open work

- The Google Drive connector is unavailable in the current execution environment.
- The authoritative Drive folder has not yet been recursively audited.
- Existing files have not yet been reconciled to Drive file IDs, revision IDs, ownership, parent folders, or retention states.
- UUID-named generated PNGs require visual/context mapping before they receive stable conceptual asset IDs.
- The XLSX register is prepared but not yet imported as the Drive-native Google Sheet.

Skill work is not a Converging Waters blocker. Any Skill-related next step must be transferred to Optimización Stack Digital / AI_OS.

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
