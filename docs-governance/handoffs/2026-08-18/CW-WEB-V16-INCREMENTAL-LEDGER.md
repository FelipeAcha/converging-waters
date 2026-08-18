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

Primary approval gate: compact zero-network ChatGPT Preview slice showing `#where-now` with the retained canonical sequence and `#thesis` without its duplicate rendering.

## Rolling cumulative progress preview

Felipe explicitly requested a second review surface that shows the cumulative visual impact after every micro-step, not only the narrow delta slice.

Stable review-only route:
`https://felipeacha.github.io/converging-waters/candidates/progress/`

Current frontier: `#thesis`.

Current progress transport shows:
- all approved changes from v16.1.1 and v16.2;
- the current proposed v16.3 delta;
- the full Stanley/WGA deep-dive block above the frontier;
- the principal infographic in its approved upper position;
- downstream sections retained in the underlying candidate DOM but intentionally hidden from the visual review until their turn.

Transport verification:
- Stanley/WGA: 13 images / 17 links;
- all 46 external hrefs remain in the candidate DOM;
- all 16 v16.1.1 public assets match the current v16.3 candidate byte-for-byte;
- `WGA's expanded field possibility` short duplicate is absent;
- territorial sequence occurs once;
- visible `#emerged-since-call`, `#stanley-update`, and `#thesis` content/hrefs/images are structurally equivalent to the local v16.3 candidate after applying the approved/proposed deltas;
- GitHub Pages deployment for commit `6ed9c6f6559623383cedee3df29ed93706adb92c` completed successfully in run `32158994079` (`local_validate`, configure, upload, deploy, and smoke all success);
- deployed Pages artifact contains `./candidates/progress/index.html`.

The progress route is `REVIEW_TRANSPORT_ONLY`; it is not the authoritative preview alias, not a release, and not approval of v16.3 or any hidden downstream section.

## Hard locks

- Stanley/WGA deep-dive section and all apparatus/reference images/links.
- Existing assets during non-asset deltas.
- External href values during non-link deltas.
- Legal precedent/source blocks until dedicated review.
- The stable progress route may be updated for cumulative review because Felipe explicitly authorized that review surface; it must never repoint the authoritative `preview/` or `releases/v13/` routes.

## Cadence

`approved candidate -> one delta -> deterministic preservation check -> zero-network ChatGPT delta-slice Preview -> cumulative progress route -> user approval -> next subversion`
