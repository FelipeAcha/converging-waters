# INC-CW-WEB-20260825-002 — Addendum 2026-09-02: navigation behavior + revision identity

**Parent incident:** `INC-CW-WEB-20260825-002`  
**Related addenda:** preservation contract; entity-status consistency  
**Classification:** INSUFFICIENT_EVIDENCE / PREMATURE_CLOSURE / RESPONSE_BEFORE_EXECUTION  
**Coverage:** ROUTED_CHAT + TOOL_OR_VALIDATOR  
**Status:** CORRECTED IN `CW-ALLY-REV05` · SOURCE REGRESSIONS ACTIVE · LIVE ASSET/FINAL VISUAL GATE STILL DEFERRED

## User-reported navigation defect

The user reported that links in the final roadmap did not produce a useful navigation result and requested that specialist deep dives always open in a new browser tab. The prior source audit had proved only that every `#anchor` pointed to an existing ID. That was insufficient because a target can exist inside a collapsed top-level accordion and therefore produce little or no visible result for the reader.

### Root cause

`ANCHOR EXISTS` was mistaken for `LINK PRODUCES A USEFUL VISIBLE RESULT`.

The required precedence is:

`destination exists -> destination is semantically appropriate -> containing disclosure becomes visible -> reader can perceive navigation result`.

### Correction in CW-ALLY-REV05

- every actual deep-dive link opens with `target="_blank"` plus `rel="noopener noreferrer"`;
- the final roadmap no longer points to generic hidden readiness/open-question destinations;
- its links now resolve to the evidence-to-implementation bridge, River Observatory deep dive, and Rights/governance deep dive;
- internal hash navigation now opens the existing containing top-level accordion before scrolling to the target;
- progressive disclosure structure and default closed state remain unchanged.

### Regression requirements

A future navigation gate fails if:

1. a deep-dive link opens in the same tab unless explicitly authorized;
2. a `#hash` target exists but remains inaccessible/hidden because its containing accordion is not opened on navigation;
3. a final-roadmap CTA points to a generic or stale destination rather than the workstream named by the card;
4. target-blank links omit `noopener noreferrer`;
5. navigation behavior is declared PASS solely from ID existence without a rendered-behavior test when browser tooling is available.

## Review-route placeholder write — corrected failure

During REV05 staging, the review-route path was first created with a placeholder body before the exact review transport was written. The placeholder was replaced immediately and was never treated as a valid candidate, but creating a user-facing review path with placeholder content is itself a preventable external-write failure.

### Root cause

`RESERVE PATH` was treated as harmless even though the path was already a user-visible review destination.

### Hard prevention

- never create or update a named review route with placeholder content;
- create the route only once the exact transport is ready, or use a non-user-facing temporary path/ref;
- a named revision route is valid only after exact content readback plus gate state update;
- any placeholder commit is registered as a failed attempt and cannot be counted as progress.

Failed placeholder commit: `7001e1de2d4d05a37f9cdbdc4de8f4fd42e6dfd7`  
Corrective route commit: `c450f53656e6610cad26cddf896e5072fc9634a5`

## Human-readable revision identity

The user also identified that SHA-256 identifiers are unsuitable as the primary rollback language. Starting with this gate, every durable ally-facing candidate receives a human-readable revision name before closure, while hashes remain exact technical identity.

Current naming chain:

- `CW-ALLY-BASE — Published Hub Baseline`
- `CW-ALLY-REV01 — Exact Recovery`
- `CW-ALLY-REV02 — Workstream Reality`
- `CW-ALLY-REV03 — Alliance Status Consistency`
- `CW-ALLY-REV04 — Full Hub Reconciliation`
- `CW-ALLY-REV05 — Evidence → Value → Protection`

Canonical technical register for this workstream: `docs/candidates/progress/REVISION-REGISTER.md`.

## Current evidence

Authoritative REV05 SHA-256: `33f4886bd8eb57a4c8ce112dcaf772f1c916255801151fb9a62fdbd1a1d7548a`  
Drive raw checkpoint ID: `1eA8e2cpZndYmlTSXPyZ3T4-2pEEzu2SR`  
Drive byte readback: `285762` bytes  
Review route: `docs/candidates/progress/cw-ally-rev05-evidence-value-protection.html`  
Alliance Architecture raw section remains unchanged: `aa8af986d451e10e410cd3876aec4de4b6664d0ff3758e08ca38b73aa2f012ae`.

## Remaining boundary

The substantive/navigation correction is implemented and source-validated. Full live-review readiness remains blocked until the known image-asset issue and first-infographic replacement are completed and the exact live route passes browser-level asset validation.
