# CW Photo Review Resolution Regression — 2026-08-29

## User-visible defect
The published GitHub Pages photo preselector rendered the correct candidates but used an excessively reduced visual payload. Image quality was too low for photographic curation.

## Root cause
The public transport had optimized review images far below the preserved canonical source resolution. The highest-quality preserved source available for this review contains local images around 850–1200+ px on the long edge and remote review sources around 1000–2500 px.

## Corrected invariant
Only image resolution changes. Candidate codes, copy, section order, selection limits, statuses, source links, review URL, and production root remain unchanged.

For the GitHub Pages review surface, build 77 local review assets from the pinned canonical source. Never upscale. Preserve source pixels up to a 1600 px long edge and encode at WebP quality 92. Fail the build if any canonical source resolves below 800 px on its long edge or cannot be retrieved.

## Canonical high-resolution source
Drive file ID: `14yTW3jxECQGe8aUM5CKxE9EmXujylsG5`
SHA-256: `bce202a8f29cdbd1fd0827f36b29f464e30d1812f9f5397cae1ef50ff8521ff8`

## Review surface
`https://felipeacha.github.io/converging-waters/review/photo-preselector/`
