# WL-WEB-PREVIEW-002 — Zero-network ChatGPT Preview transport

Status: IMPLEMENTED — BEHAVIOR TESTED LOCALLY / EXACT CHAT SURFACE PENDING USER CONFIRMATION
Owner: Project production and governance workflow
Recorded: 2026-08-18
Coverage tier: TOOL_OR_VALIDATOR

## Scope and precedence

This record supersedes only the preview-transport claim in `WL-WEB-PREVIEW-001.md` that a reliable ChatGPT review necessarily requires HTTP(S) deployment. It does **not** supersede that record's authoritative-baseline, source-identity, deployment, release, rollback, or GitHub-governance rules.

For supported ChatGPT HTML code-block Preview, the preferred review transport is now **zero-network in-chat rendering** when practical. GitHub remains the authority for website source/deployment and the fallback review surface when a zero-network in-chat Preview is impractical or fails.

## Triggering incident

A dependency-free HTML Preview canary rendered correctly in Felipe's Converging Waters Project chat. The next attempted Preview wrapped the already-published GitHub candidate in an `<iframe>` pointing to `felipeacha.github.io`. ChatGPT then displayed `¿Permitir el acceso a la red?`. Selecting `Permitir` caused the same permission prompt to recur persistently; selecting `Denegar` stopped the loop but prevented the website from rendering.

This reproduced a failure class already implied by earlier review incidents: a networked wrapper is not an acceptable substitute for a self-contained review artifact on a surface that has demonstrated a persistent permission loop.

## Primary classifications

- `SURFACE_AMBIGUITY`
- `TOOL_CONTRACT_MISMATCH`
- `ASSUMED_COMPLETION`
- `REPEATED_HUMAN_ACTION`

## Corrected rule

1. After a dependency-free HTML Preview canary succeeds, set `CHAT_PREVIEW_NETWORK_POLICY=ZERO_NETWORK` for that review surface unless the user explicitly chooses otherwise.
2. Do not use an iframe, remote image, remote CSS/JS, `fetch`, XHR, remote decompression, redirect wrapper, or other automatic external request in the in-chat Preview.
3. Prefer an **exact delta-slice Preview** for incremental review: include the requested changed region plus enough adjacent context to judge placement/order; reuse exact source markup/CSS and the exact local asset when practical.
4. Inline local assets using data URIs for the represented slice. External anchor links may remain only when they are not automatically requested by render.
5. Do not invent a platform size limit. Record measured payload size and reduce the review surface by scope, not by deleting unique information.
6. A delta-slice approval approves only the represented delta. It never proves full-page QA or approval.
7. If a zero-network Preview remains impractical or fails on the exact ChatGPT surface, stop retrying Preview transports and switch directly to the verified public GitHub candidate route. Do not ask Felipe to repeat network-permission prompts.
8. The fallback changes the review method, never the website identity or baseline.

## Current measured evidence

For Converging Waters `v16.1.1` on 2026-08-18:

- full self-contained candidate transport: approximately 1.135 MB;
- exact infographic delta slice: 296,240 bytes;
- delta-slice SHA-256: `8a08be822e0ca13cb2fbb2d25048cf4ad917dff394090ed6eadc80c83b5490c3`;
- iframe count: 0;
- automatic HTTP(S) resource references: 0;
- embedded data-image count: 1;
- principal infographic count: 1.

Local real-browser regression was executed at desktop `1440x1100` and mobile `390x844`. In both runs the HTML generated **zero network requests**, the principal infographic existed exactly once, was visible and decoded, appeared after the hero and before `#current-session`, and produced no horizontal overflow. A separate visual inspection found the original WebP data-URI screenshot rendering correctly on desktop; mobile screenshot capture exposed a WebP rasterization anomaly in the headless screenshot path, which remains a transport-test caveat and is not treated as proof of user-surface failure.

## Regression requirement

A future ChatGPT website review must fail closed rather than request user approval when any of the following is true:

- a Preview automatically requests an external host after the review surface has been classified `ZERO_NETWORK`;
- an iframe or remote render dependency is introduced as a workaround;
- the user has already reported a persistent permission loop and is asked to try `Permitir` again;
- a downloadable `.html` file is labeled an in-chat visualizer;
- a slice is presented as proof that unrelated sections were visually reviewed;
- the candidate identity changes because the preferred transport failed.

## Current gate

`v16.1.1` remains the infographic-only candidate. No later content delta may start until Felipe can review that delta either through the zero-network slice in ChatGPT or, if that fails, through the verified public GitHub candidate route. `v13` remains the authoritative untouched baseline until a later explicit promotion decision.
