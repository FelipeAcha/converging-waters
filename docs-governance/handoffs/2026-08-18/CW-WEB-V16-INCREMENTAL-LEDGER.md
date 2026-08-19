# Converging Waters — v16 incremental website ledger

Status: ACTIVE
Workstream: incremental web deduplication and clarification from authoritative v13
Review transport: zero-network ChatGPT delta-slice Preview + stable cumulative progress route

## Baseline

- Authoritative untouched baseline: v13.
- Current public release/preview baseline remains v13 until a separate promotion decision.
- v14/v15 remain superseded review attempts.

## Approved increments

### v16.1.1 — APPROVED
Delta: keep the principal original infographic, place it directly below the hero/title area, and suppress only the later duplicate HTML/CSS reconstruction from active display.

### v16.2 — APPROVED 2026-08-18
Baseline: v16.1.1.
Delta: remove only the short `WGA's expanded field possibility` summary card from `#emerged-since-call`; retain the immediately following full `#stanley-update` deep dive unchanged.
Preservation evidence:
- Stanley/WGA raw section SHA-256: `d22889e1b98d8f49d3ea09f74092e97273d06964852e19b20c0aebd26d5525e1`
- Stanley/WGA: 13 images / 17 links
- all 16 assets preserved byte-for-byte
- external href list preserved: 46
- exact v16.2 HTML SHA-256: `d378b280d2b85df212d44ce517626b415ece225a07e1287d33b62f07e35b5f79`

### v16.3 — APPROVED 2026-08-18
Baseline: approved v16.2 local state.
Delta: remove only the second visual rendering of `Listen → Measure → Train → Pilot → Mandate → File or legislate` from `#thesis`; retain the exact territorial pathway in `#where-now` as its single active visual home.
Preservation evidence:
- section count unchanged
- 46 external hrefs unchanged
- Stanley/WGA section byte-identical
- all assets unchanged
- exact v16.3 HTML SHA-256: `6d3acae3ddfeeb7a72f089a205e8a3483130560ea0ad030fb598a8b9bf8ae09a`

### v16.4 — APPROVED 2026-08-18
Baseline: approved v16.3 local state.
Delta: suppress only the residual visible wrapper of `#purpose-mrv` by adding `hidden aria-hidden="true"`; no inner content deleted or rewritten.
Preservation evidence:
- section count unchanged
- 46 external hrefs unchanged
- Stanley/WGA section byte-identical
- all 16 assets unchanged
- `#purpose-mrv` inner HTML SHA-256 preserved: `8334e4aec880e4cab4d39b547f08c5105b44c313dafe251db8e74de668717f8a`
- exact v16.4 HTML SHA-256: `5c28d9256b2ad86bdac4511d1bfc431ec5b3cb4d8e1341430dd84b14256c3719`

## Current proposal

### v16.5 — PENDING REVIEW · REVISION 3
Baseline: approved v16.4 local state.
Authorized delta only: rewrite `#system` to clarify the river system, candidate monitoring geography and scope boundaries.

Revision-3 content logic:
- use `Willkamayu / Vilcanota–Urubamba` as a working main-stem label while preserving historical/institutional naming distinctions;
- show the main stem and Huatanay branch converging into one shared Huambutío node;
- use candidate orientation/participation chain `Pisac → Calca → Huarán → Urubamba → Yanahuara → Pachar → Ollantaytambo`;
- treat Yanahuara as a distinct node rather than folding it into Urubamba;
- retain M1/M2/M3 Huambutío attribution logic;
- add diagnostic node patterns:
  - Yanahuara: `YAN-0 / YAN-T / YAN-1`;
  - Pachar / Hatun Mayu: `PACH-0 / PACH-HAT / PACH-1`;
  - Ollantaytambo / Patacancha: `OLL-0 / PAT-0 / PAT-1 / OLL-1`;
- identify `OLL-1` as a candidate post-town/outlet point for the first corridor;
- note that `PGIRH-067 Pachar` is evidenced as an ANA hydrological automatic station, not automatically a water-quality station;
- state that not every node requires a permanent sensor and preserve periodic school/community sampling as a possible mode;
- preserve school-network mapping schema `district → populated center / microcuenca → schools → students → nearest monitoring node` without turning `#system` into the school inventory;
- keep Cusco/Huatanay participation as an explicit Phase 1 vs Phase 2 team decision;
- keep downstream continuity `Lower Urubamba → Atalaya → Ucayali → Amazon → Atlantic` as ecological implication, not project footprint;
- keep the PTAR external links while simplifying the public text to a stable infrastructure/performance question rather than volatile investment figures.

Deterministic preservation audit: PASS.
- approved v16.4 HTML SHA-256: `5c28d9256b2ad86bdac4511d1bfc431ec5b3cb4d8e1341430dd84b14256c3719`
- revised v16.5 REV 3 HTML SHA-256: `465a88055c06870ba47f2bf29344a19564504c149633777ae154108d3de1b168`
- revised `#system` SHA-256: `c23ce6c7ee1a6f2f3e4ac272cc5b74c00c7b43d6b1fd57d748a8911c27610d8e`
- total section count: 42; unchanged
- only changed section relative to v16.4: `#system`
- external hrefs: 46 unchanged, values and order identical
- Stanley/WGA protected section byte-identical
- Stanley/WGA: 13 images / 17 links
- all 16 assets unchanged byte-for-byte
- one shared Huambutío node
- diagnostic node-code regression: PASS
- old `estimated US$46M project` phrase absent

Primary approval gate: zero-network ChatGPT Preview of revised `#system`.

## Rolling cumulative progress preview

Stable review-only route:
`https://felipeacha.github.io/converging-waters/candidates/progress/`

Current reviewed frontier: `#system`.

Current progress source is labeled `v16.5 PROPOSED · REV 3` and is derived from exact v16.1.1 plus approved v16.2/v16.3/v16.4 mutations and exact v16.5 REV 3 `#system` markup. Downstream sections remain in the underlying candidate but are hidden only in the review transport until their turn.

The stable progress route is `REVIEW_TRANSPORT_ONLY`; it is not the authoritative preview alias, not a release and not promotion of v16.5.

## Monitoring + citizen-science canonical integration

Primary node-architecture register:
`docs-governance/registries/WILLKAMAYU_MONITORING_AND_CITIZEN_SCIENCE_NODE_REGISTER.md`

Cross-conversation school-research handoff:
`docs-governance/handoffs/2026-08-19/CW_SCHOOL_RESEARCH_TO_MONITORING_HANDOFF.md`

The school census remains authoritative in its own research workstream; website and monitoring records must link to that verified inventory rather than rebuilding its counts independently.

## Hard locks

- Stanley/WGA deep-dive section and all apparatus/reference images/links.
- Existing assets during non-asset deltas.
- External href values during non-link deltas.
- Legal precedent/source blocks until dedicated review.
- v13 remains untouched.
- The stable progress route may be updated for cumulative review because Felipe explicitly authorized that surface; it must never repoint the authoritative `/preview/` or `/releases/v13/` routes.

## Cadence

`approved candidate -> one delta -> deterministic preservation check -> zero-network ChatGPT delta-slice Preview -> cumulative progress route -> user approval -> next subversion`
