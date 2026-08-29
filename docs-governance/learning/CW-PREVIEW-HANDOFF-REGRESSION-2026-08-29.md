# CW Preview Handoff Regression — 2026-08-29

## Failure corrected
A new-conversation handoff repeatedly degraded a working review surface into a non-renderable ChatGPT attachment or an obsolete GitHub transport. The obsolete transport referenced missing local files and could therefore look valid in source control while failing for the reviewer.

## Root cause
Review readiness was being inferred from the existence of HTML rather than proven on the exact public review surface. Transport integrity, payload completeness, browser rendering, and durable readback were not all enforced by one contract.

## Permanent invariant
For the Converging Waters photo preselector, the canonical review surface is:

`https://felipeacha.github.io/converging-waters/review/photo-preselector/`

A handoff may call the selector ready only when the latest `Photo preselector review contract` check is green and `.github/photo-preselector-review-status.json` records `browser_contract: PASS` for the latest relevant Pages deployment.

## Enforced regression matrix
The contract fails when any of these is false:
- the review shell exists;
- the payload contains exactly 26 ordered chunks;
- the reconstructed gzip SHA-256 is `277700a35c7dfa03de1d575ceae93571e601b550c1206c3d3239e43a61c05c40`;
- decompression succeeds;
- payload counts are exactly 18 needs / 77 candidates / 77 controls / 77 images;
- all 77 review images are embedded data images, with no automatic remote image source;
- the shell preserves full-frame `object-fit: contain`;
- selection-limit enforcement markers remain present;
- literal local review dependencies resolve inside the review root;
- the public route and last payload chunk return HTTP 200;
- headless Chrome renders the public route with `data-selector-ready="true"`;
- the rendered public DOM still contains 18/77/77/77 and no transport-error state.

## Handoff rule
Never substitute a sandbox `.html`, attachment download, or ChatGPT inline Preview for this canonical public review URL. If the public contract is not green, report the review surface as blocked and repair the transport before asking Felipe to review.

## Revalidation triggers
Re-run the full contract after any change to the selector shell, payload chunks, review validator, public Pages transport, or review workflow. Revalidate again after every GitHub Pages deployment.
