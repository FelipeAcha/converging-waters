# AI_OS transfer — Web Workstream Control improvements from Converging Waters

Status: READY_FOR_AI_OS_INSTALLATION
Date: 2026-08-18
Updated: 2026-08-19
Source workstream: Converging Waters website v16 incremental recovery
Owning system for the Skill: AI_OS

## Purpose

Capture reusable web-workflow improvements learned and behavior-tested in the Converging Waters Project without making Converging Waters the canonical home of the transversal Skill.

## Existing behavior preserved

- authoritative baseline lock;
- one authorized delta per subversion;
- deterministic preservation manifests;
- protected-section hashes/image/link counts;
- external href preservation during non-link deltas;
- zero-network ChatGPT HTML Preview after the network-permission-loop incident;
- downloadable HTML is not the ChatGPT visualizer;
- delta-slice approval gates;
- baseline/candidate rollback separation;
- final link/asset/responsive QA only after incremental content approval.

## Reusable improvement 1 — two review surfaces

Add two distinct review artifacts to controlled web workstreams:

1. `DELTA_SLICE_PREVIEW` — exact changed region plus adjacent context; this remains the approval surface.
2. `ROLLING_PROGRESS_PREVIEW` — exact cumulative state from the top of the page through the current review frontier, containing all approved deltas plus the current proposed delta.

Rules for the rolling progress preview:

- derive from the exact current candidate, never manually reconstruct from summaries;
- include protected blocks in full when they fall above the frontier;
- keep unreviewed downstream content in candidate source and hide it only in review transport;
- use transport-only CSS/navigation suppression when possible;
- if a full in-chat cumulative preview is impractically large, retain the small zero-network delta preview and use a verified static review route only when the user explicitly requests/authorizes a link;
- prefer one stable review-only route per workstream (for example `candidates/progress/`) and update it after each step;
- a progress route is never promotion, never the authoritative release/preview alias, and never proof that hidden downstream sections were reviewed;
- reuse a previously published asset base only when hashes match the current candidate;
- validate the progress route for version/frontier, protected blocks, asset/link invariants and hidden downstream boundary.

## Reusable improvement 2 — intra-section semantic control

The v16.5 review exposed a second class of redundancy: a section can be structurally unique but still repeat the same meaning through multiple summary cards.

Add these Skill rules:

- run an `INTRA_SECTION_REDUNDANCY_SCAN` whenever a section is rewritten;
- enforce `ONE_CONCEPT_ONE_PRIMARY_HOME` both across sections and inside a section;
- if measurement geography, benefit geography, downstream implications and phase decisions are all present, give each a distinct visual role rather than restating the same scope disclaimer several times;
- do not duplicate a real-world confluence/junction/shared node across parallel lanes when the layout implies two separate places or sequential events; model a single shared convergence node;
- distinguish `ORIENTATION_ANCHOR`, `CANDIDATE_STATION`, `BENEFIT_GEOGRAPHY` and `CONFIRMED_SITE`; settlement spacing alone is never enough to justify a scientific monitoring station;
- reject unsupported geographic superlatives such as `exact midpoint` unless explicitly verified;
- apply a `VOLATILE_FACT_CHECK` to money, project budgets, capacity, schedules and other time-sensitive figures before publishing them; old estimates must be dated or moved into an evidence register rather than shown as timeless current facts.

Targeted regression pattern:

```text
SHARED_NODE_OCCURRENCES == 1
UNAUTHORIZED_EXTERNAL_HREF_CHANGES == 0
PROTECTED_BLOCK_HASH_CHANGED == false
STALE_UNDATED_NUMERIC_CLAIMS == 0
DUPLICATE_SCOPE_CARD_HEADINGS == 0
UNVERIFIED_GEOGRAPHIC_SUPERLATIVES == 0
```

## Deterministic helpers

`make_progress_preview.py`

Purpose: generate a rolling cumulative transport from an exact candidate through a named section frontier, optionally rewriting unchanged asset paths to a verified public asset base.

Future Skill implementation should also add deterministic checks for the intra-section rules above rather than relying only on prose instructions.

## Behavior evidence from Converging Waters

- ChatGPT zero-network delta Preview: behavior-tested successfully on the exact Project-chat surface.
- Stable cumulative review route: `https://felipeacha.github.io/converging-waters/candidates/progress/`.
- v16.5 Revision 2 demonstrates one shared Huambutío confluence node instead of two confusing parallel references.
- v16.5 Revision 2 removes three redundant scope-summary cards while preserving their unique meaning in primary blocks.
- old undated `US$46M` website wording was removed after source review showed that the figure was a dated 2023 PTAR Cusco / San Jerónimo estimate and later official estimates changed materially.
- candidate locality wording was downgraded from an unsupported `exact midpoint` idea to orientation-anchor language.
- Stanley/WGA remains protected at 13 images / 17 links; full candidate external href invariant remains 46.
- Pages deployment for the v16.5 Revision-2 cumulative transport: source commit `0563fa3df652b31cc526bda6b1c788e82ec62b31`, run `32302013753`; deployment diagnostics report local validation, configure, upload, deploy and smoke all `success`.

## Packaged Skill status

The package hash recorded in the 2026-08-18 transfer (`c5fe9b1a1c8bf86c933eeeb42fc1da5c4820f291c39d8030693db2897d948999`) predates the v16.5 addendum above.

Do **not** claim the installed transversal Skill already contains the v16.5 rules until AI_OS incorporates this addendum and a new package is validated/installed. This file is the authoritative transfer note from Converging Waters; the canonical transversal Skill remains owned by AI_OS.
