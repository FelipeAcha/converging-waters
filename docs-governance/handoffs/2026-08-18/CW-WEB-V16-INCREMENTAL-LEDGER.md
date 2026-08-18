# Converging Waters — v16 incremental website ledger

Status: ACTIVE
Workstream: incremental web deduplication from authoritative v13
Review transport: zero-network ChatGPT delta-slice Preview + stable cumulative progress route

## Baseline

- Authoritative untouched baseline: v13
- Current public review baseline remains v13 until a separate promotion decision.
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
- only `#thesis` differs relative to v16.2
- exact v16.3 HTML SHA-256: `6d3acae3ddfeeb7a72f089a205e8a3483130560ea0ad030fb598a8b9bf8ae09a`

## Current proposal

### v16.4 — PENDING REVIEW
Baseline: approved v16.3 local state.
Authorized delta only: suppress the residual visible wrapper of `#purpose-mrv` by adding `hidden aria-hidden="true"` to the section.

Reason: the detailed native HTML/CSS reconstruction inside this section was already suppressed in approved v16.1.1 after the principal original infographic was moved to the top. The remaining later heading/intro therefore acts as an empty duplicate shell.

Deterministic preservation audit: PASS.
- baseline sections: 41
- candidate sections: 41
- external hrefs: 46 unchanged
- Stanley/WGA section byte-identical
- all 16 assets unchanged
- no `#purpose-mrv` content deleted or rewritten
- `#purpose-mrv` inner HTML SHA-256 preserved: `8334e4aec880e4cab4d39b547f08c5105b44c313dafe251db8e74de668717f8a`
- exact v16.4 HTML SHA-256: `5c28d9256b2ad86bdac4511d1bfc431ec5b3cb4d8e1341430dd84b14256c3719`

Primary approval gate: compact zero-network ChatGPT Preview slice around `#citizen-science` → hidden `#purpose-mrv` → adjacent `#system` context.

## Rolling cumulative progress preview

Stable review-only route:
`https://felipeacha.github.io/converging-waters/candidates/progress/`

Current reviewed frontier: `#citizen-science`.

Current progress transport shows:
- approved v16.1.1, v16.2 and v16.3;
- current proposed v16.4;
- the principal infographic in its approved upper position;
- the complete Stanley/WGA deep-dive block above the frontier;
- unchanged intervening sections through citizen science;
- downstream sections retained but intentionally hidden in the review transport until their turn.

The stable progress route is `REVIEW_TRANSPORT_ONLY`; it is not the authoritative preview alias, not a release and not promotion of v16.4.

## Hard locks

- Stanley/WGA deep-dive section and all apparatus/reference images/links.
- Existing assets during non-asset deltas.
- External href values during non-link deltas.
- Legal precedent/source blocks until dedicated review.
- v13 remains untouched.
- The stable progress route may be updated for cumulative review because Felipe explicitly authorized that surface; it must never repoint the authoritative `/preview/` or `/releases/v13/` routes.

## Cadence

`approved candidate -> one delta -> deterministic preservation check -> zero-network ChatGPT delta-slice Preview -> cumulative progress route -> user approval -> next subversion`
