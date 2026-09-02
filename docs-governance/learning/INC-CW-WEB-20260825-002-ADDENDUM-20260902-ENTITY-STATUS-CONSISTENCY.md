# INC-CW-WEB-20260825-002 — Addendum 2026-09-02: entity-status consistency recurrence

**Parent incident:** `INC-CW-WEB-20260825-002`  
**Prior addendum:** `INC-CW-WEB-20260825-002-ADDENDUM-20260902-PRESERVATION-CONTRACT.md`  
**Classification:** PARALLEL_CHANGE_NOT_RECONCILED / ASSUMED_COMPLETION  
**Coverage:** ROUTED_CHAT + TOOL_OR_VALIDATOR  
**Status:** CORRECTED IN CURRENT CANDIDATE · DETERMINISTIC REGRESSION ACTIVE · FULL VISUAL REVIEW DEFERRED

## Failure

Amazonas Sagrada had already been established as a **potential ally** in the project-specific Definition of Done and had been corrected in several hub sections, but the protected **Complete Alliance, Access and Timing Matrix** still represented it as `CURRENT` inside `Current collaboration layer`, with the stale description `Core autonomous initiative through Chelsea and Patrick.`

This created a cross-component contradiction: the same entity had different relationship status depending on where the reader looked.

## First control failure

The correction process validated the strings that were explicitly patched but did not run an entity-wide reconciliation across every remaining occurrence before declaring the status cleanup sufficiently advanced. Protection of the Alliance Architecture was interpreted too narrowly as a reason to avoid touching the stale status cell, even though factual status correction was explicitly authorized.

## Root cause

`LOCAL PATCH COMPLETION` was mistaken for `ENTITY-WIDE STATUS CONSISTENCY`.

The required precedence is:

`canonical relationship status -> every public representation of that entity -> protected layout preservation`.

A protected component keeps its geometry, styling, unaffected cells, links and responsive behavior; protection does not preserve a factual status known to be stale.

## Correction

Current candidate SHA-256:

`6badd80c1143d04f3f3dbe877273844f8efaa1f6167f412264c41f8bfcb73ac8`

Corrections include:

- Amazonas Sagrada matrix badge: `CURRENT` -> `POTENTIAL ALLY`;
- stale `Core autonomous initiative through Chelsea and Patrick.` wording replaced with an explicit active-direct-relationship / no-institutional-commitment description;
- matrix group heading broadened from `Current collaboration layer` to `Current relationships + territorial focus` so the group can accurately contain WGA's current convergence, Willkamayu's current territorial focus and active access to a potential ally;
- WGA row clarified as current scientific-technical convergence through WGA;
- stale pre-visit / September / informal-meeting framing updated without changing matrix geometry, row order, chips, links, disclosure nesting or responsive structure;
- Amazonas Sagrada's dedicated learning section demoted from protagonist-style naming to a cross-territorial potential-ally example while preserving useful substantive learning.

The first infographic remains a declared deferred visual exception and will be replaced later with a near-identical version without Amazonas Sagrada or Maria Gracia.

## Regression requirements

Before a future ally/status gate can close:

1. enumerate every public occurrence of each governed entity whose status changed;
2. classify each occurrence as current relationship, potential ally, personal contribution, territorial focus, historical/contextual mention or deferred visual artifact;
3. fail if Amazonas Sagrada is rendered as `CURRENT`, core project track or institutional collaborator without newer explicit authority;
4. fail if Maria Gracia is rendered as current/core rather than potential ally without newer explicit authority;
5. fail if WGA is downgraded from the current scientific-technical convergence relationship without newer evidence;
6. preserve Alliance Architecture layout, row order, chips, hrefs, disclosure structure and responsive treatment while allowing the exact factual status/copy cells authorized to change;
7. keep deferred visual artifacts explicitly registered rather than silently treating them as current-status PASS.

## Deterministic prevention active now

The isolated review loader now verifies the exact candidate SHA before rendering and contains explicit post-patch assertions that:

- the stale Amazonas Sagrada `Core autonomous initiative...` representation is absent;
- the stale `Current collaboration layer` grouping is absent;
- a `POTENTIAL ALLY` marker is present for the corrected matrix representation;
- WGA's current scientific-technical convergence marker is present.

The cumulative review state also records:

- `AMAZONAS_SAGRADA_STATUS=POTENTIAL_ALLY`;
- `AMAZONAS_SAGRADA_MATRIX_STATUS=POTENTIAL_ALLY`;
- `MARIA_GRACIA_STATUS=POTENTIAL_ALLY`;
- `WGA_STATUS=CURRENT_SCIENTIFIC_TECHNICAL_CONVERGENCE`;
- `ENTITY_STATUS_REGRESSION=PASS`.

## Evidence

- review-route content update commit: `a18b946c00d5ea7ee5462a578261ce7a6b6a9237`;
- cumulative-state update commit: `92e44820473eb0888704cefae501b160462f15f2`;
- Drive raw checkpoint ID: `1FyhWCO2BnDF7_aUqpsNe_ygbYtgwVLNt`;
- `Validate cumulative progress`: PASS;
- `ACB alliance web watchdog`: PASS;
- GitHub Pages deploy/validation workflow: PASS;
- public production root: unchanged.

## Remaining boundary

This recurrence is corrected in the current source/review candidate and has deterministic prevention on the current review route. It is **not** evidence that the full visual candidate is ready: the known image-loading defect and first-infographic replacement remain intentionally deferred until the substantive reconciliation pass is complete.

## 2026-09-02 follow-up — shared-wrapper destructive-removal near miss

During the subsequent full-hub substantive reconciliation pass, an initial local transformation attempted to remove an obsolete orientation wrapper that contained both `emerged-since-call` and the protected `stanley-update` WGA/Stanley technical section. The section inventory regression detected that `stanley-update` had disappeared before any candidate checkpoint, review-route persistence or production mutation. The failed local artifact was discarded; the corrected candidate removes only the obsolete `emerged-since-call` section and retains the existing wrapper and complete `stanley-update` content.

**Classification:** BEHAVIOR_REGRESSION_FROM_SKILL_UPDATE / SCOPE_DRIFT — prevented before persistence.  
**First control failure:** wrapper-level deletion was chosen from the obsolete child section without enumerating every sibling/protected section inside that wrapper.  
**Root cause:** `OBSOLETE CHILD -> REMOVE CONTAINER` was treated as safe without proving `ALL CONTAINER CONTENT -> AUTHORIZED FOR REMOVAL`.

Additional hard regression for wrapper/disclosure cleanup:

1. before removing any accordion/disclosure/container wrapper, enumerate every contained section ID and protected marker;
2. a wrapper may be removed only when every substantive contained block is in the current delta's explicit removal set;
3. when one obsolete section shares a wrapper with a retained/protected section, remove only the obsolete child node and preserve the wrapper plus retained content;
4. immediately compare the pre/post section inventory before any persistence;
5. fail closed if a protected WGA/Stanley, evidence, legal, Alliance Architecture, precedent or deep-dive section disappears or changes outside the current authorized delta.

Behavior evidence from the corrected reconciliation candidate:

- authoritative candidate SHA-256: `0fe164c7f71e12f6fcbdb5e4dbc44b593af51027d28880ffdfac8caeca5f630c`;
- `stanley-update` is present and raw-identical to the prior candidate, SHA-256 `867001577b7b4663530b8b33e59c3965798197d704c24f5e1e39f29c40b7d751`;
- only the five explicitly obsolete sections are removed;
- retained section order passes;
- exact raw candidate is checkpointed in Drive ID `1u-sTBpy6MeLSqdjCUSkGbLKahLBKnBvR`.
