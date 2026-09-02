# CW-WEB v17.0 REV02 — Preview gate

Status: PENDING USER REVIEW
Date: 2026-09-02
Lifecycle: REVIEW
Review surface: Alliance Website / first-time ally orientation

## Purpose

Provide a concrete, scan-friendly orientation surface for a potential ally who does not already know Converging Waters, while keeping the detailed research in deeper supporting documents and preserving the frozen historical website as rollback evidence.

## Source authority

Primary framing source:
- `Converging Waters - Alliance Orientation and Workstream Navigator - 2026-08-29 - v02`
- Google Doc ID: `1IfbWHwA6QRC8JvMhIp7b8vsfMwtUcNY8lEr5MQjTeJc`
- Review text readback reports snapshot `1 September 2026 · v03` inside the document.

Website source:
- repository: `FelipeAcha/converging-waters`
- branch: `main`
- path: `docs/candidates/v17.0-rev02/index.html`
- Git blob SHA: `02d5d60b9c6de54af8cdede09df5df6d12aa52d0`
- source size: `20940` bytes
- exact source SHA-256: `da321db9ff7200edda8c47908a7ef38b5d3052679be4b00ff789b1ea32d7825a`
- candidate creation commit: `d16e737c28fb227a65e7c4c2098d19fe56dff676`
- latest ACB verification commit: `2480a67b420c6a0cbfb09bf3133856df0e157af4`

## Review transport

Stable review-only route:
`https://felipeacha.github.io/converging-waters/candidates/v17.0-rev02/`

This route is `REVIEW_TRANSPORT_ONLY`. It does not replace the main public route and does not mutate the frozen historical snapshot.

## What REV02 is building

The page now exposes the project in four progressive layers:

1. `What this is` — one connected river system; evidence + local knowledge + science; autonomous allies connected by purpose.
2. `What we're building` — an integrated platform organized into Understand, Measure, Enable action, and Sustain & connect.
3. `Workstream map` — eight scan-friendly workstream cards with semantic domain chips, current state and next move.
4. `Where you fit` — three explicit ally entry paths: evidence, capability and responsibility, followed by deeper reading surfaces.

The first screen states the geography, initiative purpose and operating idea without assuming prior project knowledge.

## REV01 → REV02 delta

REV01 failed the public mobile browser audit because the hero grid retained a min-content width wider than the 390 px viewport. Evidence showed 26 px page overflow and hero descendants extending to approximately 416 px.

REV02 changes only the responsive presentation needed to close that gate:
- adds `min-width: 0` to mobile hero-grid children;
- reduces the mobile H1 clamp to prevent the `Converging` word from forcing the grid wider than the viewport;
- preserves the information architecture, copy, desktop hierarchy and workstream model.

REV01 remains preserved at:
`docs/candidates/v17.0-rev01/index.html`

## Deterministic and browser validation

Zero-network source validation: PASS.

Local exact-candidate browser validation before publication:
- desktop viewport: `1440 × 1100`
- mobile viewport: `390 × 844`
- mobile horizontal overflow: `0 px`
- local non-HTTP structural gates: `15/15 PASS`

Public GitHub Pages ACB validation:
- workflow: `ACB alliance web watchdog`
- run: `33609430143`
- active candidate job: `100180845228`
- candidate hard gates: `16/16 PASS = 100%`
- candidate enforcement job: PASS
- rendered HTML SHA-256: `b1296f10f7a8df6e9b9ee3423fd072c0168fa6927427b5b6ab3514b9946b1059`
- ACB report SHA-256: `fec3334ab82897bc32068ca4e7e38901173cd1846ed5032709d933b9b0ed0483`
- desktop screenshot SHA-256: `de1673318ce6142e2749ba8f6495e632bd389e7881d329a78d579c30be9187a0`
- mobile screenshot SHA-256: `c27f57e92605b76de5823f4a10f7fb321187d7006ecbb275dda6ad48b67a68ac`

## Explicit visual / UX review

Exact public desktop and mobile screenshots were visually inspected after browser rendering.

Result: `12/12 PASS` for the current review-candidate checklist:

1. first-time reader understands where they are and what the initiative is;
2. value proposition is visible without scrolling through internal process material;
3. strategy and invitation to allies are prominent;
4. dense information is converted to scan-friendly cards and layers;
5. domain chips are semantic and consistently color-coded;
6. no wide table or matrix blocks mobile reading;
7. the purpose → measurement → learning flow is directionally legible and unclipped;
8. visual rhythm avoids a continuous wall of text;
9. each topic has one main home within the page;
10. secondary detail is routed toward deeper-reading surfaces instead of duplicated inline;
11. mobile preserves the same information priority as desktop;
12. the page is legible as an ally-facing orientation surface without requiring prior Converging Waters context.

Photography and richer art direction remain a later visual-content decision; they are not required to understand or review this information architecture.

## ACB enforcement model

The watchdog now distinguishes:
- `ACTIVE CANDIDATE — BLOCKING`: `v17.0 REV02`; its hard-gate failure makes enforcement fail closed.
- `LEGACY / WORKING — MONITOR ONLY`: current root and immutable v13; their known historical debt remains visible in artifacts but does not falsely block promotion of a new independent candidate.

The active-candidate enforcement summary passed in run `33609430143`.

The watchdog remains event-driven on pushes and pull requests, with a five-minute recovery heartbeat.

## Known legacy monitor debt

This checkpoint does not claim that every historical surface satisfies the new checklist.

- current published-working surface: previously measured at 93.75%, with heading-hierarchy debt;
- immutable v13 review surface: previously measured at 81.25%, with legacy image/table/heading issues.

Those surfaces remain preserved and monitored. They are not silently rewritten to make the active-candidate gate green.

## Assistant-caused rework recorded

One intermediate watchdog edit (`577b8b93eaef900a6acc4cbecab1bb2315d441e3`) contained a duplicate YAML `env` mapping in one step and produced a jobless workflow failure. It was corrected immediately in `2480a67b420c6a0cbfb09bf3133856df0e157af4`; run `33609430143` then parsed, executed all browser jobs and passed the active-candidate enforcement summary. Future workflow mutations must be checked for duplicate YAML mapping keys before write.

## Lifecycle readback

- `SOURCE_VALIDATED = true`
- `ZERO_NETWORK_SOURCE_VALIDATED = true`
- `PUBLIC_REVIEW_ROUTE_DEPLOYED = true`
- `PUBLIC_BROWSER_RENDER_VALIDATED = true`
- `HARD_GATES_16_OF_16 = true`
- `VISUAL_GATES_12_OF_12 = true`
- `ACTIVE_CANDIDATE_ENFORCEMENT = PASS`
- `USER_APPROVED = false`
- `PROMOTED_TO_MAIN = false`

## Rollback

Preserved rollback points:
- REV01: `docs/candidates/v17.0-rev01/index.html`
- frozen historical website: source commit `982157efc2f051b7766439faf9a62f84de68a397`, exact source `docs/` tree `ea1af83277d140943db023e585d32e63dced72d9`
- historical route: `https://felipeacha.github.io/converging-waters/history/2026-09-01/`

No approved or historical surface was overwritten by REV02.

## Next gate

`USER-REVIEW-v17.0-REV02`

Felipe reviews the exact desktop/mobile/public candidate. Until explicit approval, REV02 remains REVIEW and the next material content/art-direction delta must not be promoted to the main route.
