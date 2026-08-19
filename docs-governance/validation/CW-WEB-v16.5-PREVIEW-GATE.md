# CW-WEB v16.5 — Preview gate

Status: PENDING USER REVIEW — REVISION 3
Date: 2026-08-19
Parent workstream: issue #5

## Approved baseline

v16.4 local state was explicitly approved by Felipe in the Converging Waters Project chat.

## One authorized delta

Rewrite only `#system` to clarify hydrological order, candidate monitoring geography and scope boundaries. Revision 3 remains inside the same one-section delta; v16.5 has not been approved yet.

## Revision 3 changes after Felipe review + school-research handoff

- Promote `Yanahuara` from an alternate note to an explicit corridor node separate from Urubamba.
- Candidate orientation chain becomes `Pisac → Calca → Huarán → Urubamba → Yanahuara → Pachar → Ollantaytambo`.
- Keep the one-shared-node Huambutío architecture and the M1/M2/M3 source-attribution logic.
- Add three distinct diagnostic tributary nodes without turning the corridor into a permanent-sensor list:
  - Yanahuara: `YAN-0 / YAN-T / YAN-1`;
  - Pachar / Hatun Mayu: `PACH-0 / PACH-HAT / PACH-1`;
  - Ollantaytambo / Patacancha: `OLL-0 / PAT-0 / PAT-1 / OLL-1`.
- Make `OLL-1` explicitly the candidate post-town/outlet point after Ollantaytambo and the Patacancha confluence.
- State that ANA's `PGIRH-067 Pachar` is evidenced as an **EHA hydrological station**; do not imply water-quality variables until separately verified.
- Add one concise citizen-science implication: not every code requires a permanent sensor; some nodes can use recurrent reference measurements and periodic school/community sampling.
- Preserve the future school mapping schema `district → populated center / microcuenca → schools → students → nearest monitoring node` without turning `#system` into the school inventory.
- Preserve Cusco/Huatanay as an explicit Phase 1 vs Phase 2 team decision.
- Keep downstream continuity as implication, not project footprint.
- Keep the PTAR links but simplify the narrative to the stable infrastructure/performance question rather than volatile budget values.

## Deterministic preservation result

PASS

- approved v16.4 HTML SHA-256: `5c28d9256b2ad86bdac4511d1bfc431ec5b3cb4d8e1341430dd84b14256c3719`
- revised v16.5 REV 3 HTML SHA-256: `465a88055c06870ba47f2bf29344a19564504c149633777ae154108d3de1b168`
- revised `#system` SHA-256: `c23ce6c7ee1a6f2f3e4ac272cc5b74c00c7b43d6b1fd57d748a8911c27610d8e`
- total section count: 42; unchanged from the approved structure
- only changed section relative to approved v16.4: `#system`
- external hrefs: 46; values and order unchanged
- Stanley/WGA protected section byte-identical
- Stanley/WGA: 13 images / 17 links
- all 16 assets unchanged byte-for-byte
- one shared Huambutío confluence heading
- all diagnostic node codes present
- old `estimated US$46M project` phrase absent
- redundant rev-1 scope-card headings absent

## Browser / route validation state

A fresh local Chromium attempt in the current execution environment did not complete: Chromium's network service crashed/hung during localhost rendering and produced no DOM. This is an environment/browser-validation limitation, not evidence of page failure.

The stable cumulative progress source was committed at `b36d2ae2f5b781faba21972c71a7dce0b98b446e`.

GitHub Pages deployment diagnostics for that commit:
- run `32304592741`;
- local validation: success;
- configure: success;
- upload: success;
- deploy: success;
- smoke: success.

The deployed Pages artifact `9384234670` was downloaded and inspected. Its `candidates/progress/index.html` SHA-256 is `c09efa94cf13679562a74e85fd5882ecd1493121e14845d43e75231192198924`, exactly matching the locally prepared REV 3 progress transport, and contains the Yanahuara, Hatun Mayu/Pachar, Patacancha/Ollantaytambo and `PGIRH-067` markers.

Keep lifecycle states separate:
- `SOURCE_VALIDATED = true`
- `DEPLOYED_ARTIFACT_VALIDATED = true`
- `DIRECT_PUBLIC_HTTP_FETCH_VALIDATED = false` in the current execution environment because DNS access to the Pages host is unavailable here
- `LOCAL_BROWSER_RENDER_VALIDATED = false` because of the Chromium environment failure
- `CHAT_VISUALIZER_VALIDATED = pending user-visible in-chat Preview for REV 3`
- `USER_APPROVED = false`

## Review transport

1. Primary approval surface: zero-network ChatGPT Preview containing the exact revised `#system` content with transport-only CSS.
2. Cumulative context surface: stable review-only route `https://felipeacha.github.io/converging-waters/candidates/progress/`, source labeled `v16.5 PROPOSED · REV 3`, frontier `#system`.

The cumulative route remains `REVIEW_TRANSPORT_ONLY`; it does not repoint `/preview/`, modify `/releases/v13/`, or promote v16.5.

## Evidence and canonical-memory boundary

Hydrology/source depth remains in:
`docs-governance/registries/WILLKAMAYU_HYDROLOGY_AND_EVIDENCE_REGISTER.md`

Candidate monitoring-node architecture + school/citizen-science integration is now owned by:
`docs-governance/registries/WILLKAMAYU_MONITORING_AND_CITIZEN_SCIENCE_NODE_REGISTER.md`

Cross-conversation integration is recorded in:
`docs-governance/handoffs/2026-08-19/CW_SCHOOL_RESEARCH_TO_MONITORING_HANDOFF.md`

Website rule: keep `#system` legible and evidence-backed; school counts and detailed school inventories remain outside this section and outside this gate.

## Next transition

If Felipe approves v16.5 REV 3, it becomes the last approved local state. The next website delta must start from v16.5 and touch one new target only.
