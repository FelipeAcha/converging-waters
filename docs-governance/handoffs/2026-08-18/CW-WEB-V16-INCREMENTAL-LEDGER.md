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
- 41 sections retained
- 46 external hrefs unchanged
- Stanley/WGA section byte-identical
- all assets unchanged
- exact v16.3 HTML SHA-256: `6d3acae3ddfeeb7a72f089a205e8a3483130560ea0ad030fb598a8b9bf8ae09a`

### v16.4 — APPROVED 2026-08-18
Baseline: approved v16.3 local state.
Delta: suppress only the residual visible wrapper of `#purpose-mrv` by adding `hidden aria-hidden="true"`; no inner content deleted or rewritten.
Preservation evidence:
- 41 sections retained
- 46 external hrefs unchanged
- Stanley/WGA section byte-identical
- all 16 assets unchanged
- `#purpose-mrv` inner HTML SHA-256 preserved: `8334e4aec880e4cab4d39b547f08c5105b44c313dafe251db8e74de668717f8a`
- exact v16.4 HTML SHA-256: `5c28d9256b2ad86bdac4511d1bfc431ec5b3cb4d8e1341430dd84b14256c3719`

## Current proposal

### v16.5 — PENDING REVIEW
Baseline: approved v16.4 local state.
Authorized delta only: rewrite `#system` to clarify the river system, candidate monitoring geography and scope boundaries.

Proposed content logic:
- use `Willkamayu / Vilcanota–Urubamba` as a working main-stem label while preserving historical/institutional naming distinctions;
- show the Huatanay joining the Vilcanota at Huambutío upstream of Pisac;
- show candidate first working/benefit corridor `Pisac → Calca → Yucay → Urubamba → Ollantaytambo` as PROPOSED, not confirmed;
- show candidate attribution stations: upstream main-stem reference, Huatanay pre-confluence, main stem just downstream of Huambutío, and representative corridor sites;
- show Cusco/Huatanay citizen science and monitoring as a possible phase-2 expansion / team decision, not a commitment;
- show downstream hydrological continuity `Lower Urubamba → Atalaya → Ucayali → Amazon → Atlantic` while explicitly stating that hydrological continuity is not project footprint.

Deterministic preservation audit: PASS.
- baseline HTML SHA-256: `5c28d9256b2ad86bdac4511d1bfc431ec5b3cb4d8e1341430dd84b14256c3719`
- candidate HTML SHA-256: `bdbdf65b94209d47e184d9de189564249d0c99cabde8fd508aef0d971e04a70e`
- baseline sections: 41
- candidate sections: 41
- only changed section: `#system`
- external hrefs: 46 unchanged
- Stanley/WGA raw SHA-256 unchanged: `d22889e1b98d8f49d3ea09f74092e97273d06964852e19b20c0aebd26d5525e1`
- Stanley/WGA: 13 images / 17 links
- all 16 assets unchanged
- candidate `#system` SHA-256: `10678f303c7454de1bdf01e506ac45d75d7c5f1f0b32e0ac6c47075dbac64381`

Primary approval gate: compact zero-network ChatGPT Preview of the proposed `#system` section.

## Rolling cumulative progress preview

Stable review-only route:
`https://felipeacha.github.io/converging-waters/candidates/progress/`

Current reviewed frontier: `#system`.

Current progress transport is derived from the exact v16.1.1 source plus the approved v16.2/v16.3/v16.4 mutations and the exact v16.5 `#system` markup. Downstream sections remain in the underlying candidate but are hidden only in the review transport until their turn.

The stable progress route is `REVIEW_TRANSPORT_ONLY`; it is not the authoritative preview alias, not a release and not promotion of v16.5.

## Hydrology and evidence track

A separate durable evidence register and research issue own the historical naming, Huatanay/Vilcanota source base, candidate monitoring-station evidence and the Japanese-cooperation study lead. Website claims should consume only evidence promoted from that track at the appropriate confidence level.

## Hard locks

- Stanley/WGA deep-dive section and all apparatus/reference images/links.
- Existing assets during non-asset deltas.
- External href values during non-link deltas.
- Legal precedent/source blocks until dedicated review.
- v13 remains untouched.
- The stable progress route may be updated for cumulative review because Felipe explicitly authorized that surface; it must never repoint the authoritative `/preview/` or `/releases/v13/` routes.

## Cadence

`approved candidate -> one delta -> deterministic preservation check -> zero-network ChatGPT delta-slice Preview -> cumulative progress route -> user approval -> next subversion`
