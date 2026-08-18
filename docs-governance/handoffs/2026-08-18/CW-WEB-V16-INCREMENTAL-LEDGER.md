# Converging Waters — v16 incremental website ledger

Status: ACTIVE
Workstream: incremental web deduplication from authoritative v13
Review transport: zero-network ChatGPT HTML Preview slices

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

## Current proposal

### v16.3 — PENDING REVIEW
Baseline: approved v16.2 local state.
Authorized delta only: remove the second visual rendering of the territorial sequence `Listen → Measure → Train → Pilot → Mandate → File or legislate` from `#thesis` because the exact sequence already remains in `#where-now` as the canonical territorial pathway.

Deterministic preservation audit: PASS.
- baseline sections: 41
- candidate sections: 41
- external hrefs: 46 unchanged
- Stanley/WGA section byte-identical
- all assets unchanged
- only `#thesis` differs relative to v16.2
- v16.3 HTML SHA-256: `6d3acae3ddfeeb7a72f089a205e8a3483130560ea0ad030fb598a8b9bf8ae09a`

Review gate: compact zero-network ChatGPT Preview slice showing `#where-now` with the retained canonical sequence and `#thesis` without its duplicate rendering.

## Hard locks

- Stanley/WGA deep-dive section and all apparatus/reference images/links.
- Existing assets during non-asset deltas.
- External href values during non-link deltas.
- Legal precedent/source blocks until dedicated review.
- No GitHub candidate staging merely to obtain review visibility.

## Cadence

`approved candidate -> one delta -> deterministic preservation check -> zero-network ChatGPT delta-slice Preview -> user approval -> next subversion`
