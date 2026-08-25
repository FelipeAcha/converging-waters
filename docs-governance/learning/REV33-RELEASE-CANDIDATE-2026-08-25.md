# REV33 release candidate — localized precedent media + immutable release QA — 2026-08-25

Status: `RELEASE_CANDIDATE_READY / PUBLICATION_DECISION_PENDING / PRODUCTION_NOT_AUTHORIZED`

## Approval carried forward
- User explicitly accepted the REV32 corrective visual result on 2026-08-25: `listo, quedó bien`.
- REV32 remains the approved material baseline for this release-hardening delta.
- REV33 changes no substantive copy, link destination, alt text, section order, or deep-dive content.

## Authorized release-hardening delta
The only candidate mutation is localization of the five precedent photographs that still loaded from `upload.wikimedia.org`:
- Marañón
- Titicaca
- stingless bee
- Whanganui
- Atrato

Exact original Wikimedia bytes were fetched without resizing or recompression. Existing source/provenance links and captions remain intact.

## Source acquisition evidence
A temporary isolated branch `rev33-wikimedia-localization` was created from main SHA `dc549cf9447c07226ce42f505440a5b0ee4f3db4` because the local execution environment could not resolve `upload.wikimedia.org`.

- GitHub Actions fetch run: `32904289920` — SUCCESS
- Artifact: `9584197005` / `rev33-wikimedia-assets`
- Artifact digest: `sha256:56ade5fef5cd0304c9fbea9e7a0326dc7713a04eddf9013278e1b183027e0480`
- Second isolated staging run: `32905212213` — SUCCESS
- Staged asset branch head: `2d2aacf217dc96e27c1c9718127d38f9eb3f604f`

Exact localized asset SHA-256:
- `maranon.jpg` — `ab7bd096db3fd462eed7485cd70f1789000bc857796401438a68f8fb024df9f5`
- `titicaca.jpg` — `e2dc30b9dbe85a7d054b521a62f0664b4ac89c956b9be1c92674a3d3640283cc`
- `stingless-bee.jpg` — `031151b44b85930533e45d0fe0b935a1f62ec988f7ceb3003988d6ff0df2fee7`
- `whanganui.jpg` — `772e86e8c52965b9ffdd25dc13142ec51fdd959304f9cef72cf0b3f3bf8ce08f`
- `atrato.jpg` — `bf9a515d826b5c063c6f094d76b09375546b4d09591339a19c6afc50a0a1573a`

## REV33 durable artifacts
Standalone self-contained review HTML:
- Drive ID: `1jAN0Ic9J-fW_EKfQKJO_2vm9bS-JUSSt`
- Bytes: `14,985,914`
- SHA-256: `8a6cba580702e696594dfa7b347cb2e979fc3e966780653a1d60a6a84c894723`
- Raw Drive readback SHA verified exact.

Release bundle Hub + 3 deep dives + localized media:
- Drive ID: `1Hnmv86nTjpCmwVTStGJ2cXYUbVTYtR9U`
- Bytes: `11,673,108`
- SHA-256: `9888aade3f04e1afc25900ea86a343ef67c9412cc49a120dc70eb38ec47a8e94`
- Raw Drive readback SHA verified exact.

Release manifest:
- Drive ID: `1ucLdyrumO6NBqYsqvp80UGLwhrfxyIJO`
- Local SHA-256: `cc841d274217c746cb2d93f8249c4dd0ed7ec5a56dd3ac69ecbc41005380a673`

Immutable QA JSON:
- Drive ID: `1ic3upDVZR4GoroG_wsGoHaQEiHgAHsK9`
- Local SHA-256: `43d557b0db531ccd6e1fd130b09ef47edc4d699cef01c03b09a3d4db21e3eb66`

Checkpoint:
- Drive ID: `1-duxcTuHRTGIWh8_UNZG-1u6njIbyFui`

## Preservation proof REV32 → REV33
- Hub visible/body text: identical
- Hub href sequence: identical
- Hub alt sequence: identical
- Rights body text: identical
- Rights href sequence: identical
- Rights alt sequence: identical
- Observatory: byte-identical
- River Economy: byte-identical
- Remaining `upload.wikimedia.org` image refs: `0`
- External href sequence: identical
- External href occurrences: `157`
- External href unique: `97`

## Immutable release QA
Static:
- localized asset integrity: 5/5 PASS
- duplicate IDs: 0
- missing internal anchors: 0
- images missing alt: 0
- details without summary: 0
- missing local refs: 0

Browser validation with system Chromium on exact local release tree, desktop 1440px and mobile 390px:
- Hub: 33 sections, 19 images, 0 broken images, 0 horizontal overflow, 0 console/page errors, 0 automatic external requests
- Rights: 16 sections, 3 images, 0 broken images, 0 overflow/errors
- Observatory: 11 sections, 0 overflow/errors
- River Economy: 10 sections, 0 overflow/errors

Initial Playwright-managed-browser launch was unavailable; QA correctly switched to `/usr/bin/chromium`. A first harness run falsely classified lazy data-URI images before lazy loading was forced; the verifier was corrected, the candidate was not changed, and final read-only QA is PASS.

## Reliability recurrence note
During isolated branch setup, the assistant repeated the same `create_branch` action after the first successful creation, receiving harmless `422 Reference already exists` responses. This is **not a new failure class**; it is a recurrence of existing F16 tool/write-discipline behavior and must be included in the later system reliability audit.

## Rolling Progress state
`docs/candidates/progress/` remains deliberately on the last stable REV24 transport. It was not moved piecemeal. The full REV33 route cannot be advanced until the entire Hub + deep dives + binary asset dependency tree can be staged and validated atomically. This is a review-transport debt, not a content/release-candidate defect and is not a publication authorization.

## Current gate
`REV33_PUBLICATION_DECISION`

REV33 is technically release-ready. Production remains untouched. Promotion/publication requires Felipe's separate explicit authorization. Rolling Progress synchronization must be performed atomically as part of the pre-promotion/promotion transition, never by moving a pointer ahead of its dependency tree.