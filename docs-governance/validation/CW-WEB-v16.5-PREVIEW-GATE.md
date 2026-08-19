# CW-WEB v16.5 — Preview gate

Status: PENDING USER REVIEW — REVISION 2
Date: 2026-08-19
Parent workstream: issue #5

## Approved baseline

v16.4 local state was explicitly approved by Felipe in the Converging Waters Project chat.

## One authorized delta

Rewrite only `#system` to clarify hydrological order, candidate monitoring geography and scope boundaries. Revision 2 remains inside the same one-section delta; v16.5 has not been approved yet.

## Revision 2 changes after Felipe review

- Replace Yucay as a principal corridor anchor with `Huarán`.
- Use `Pachar` as the primary downstream orientation anchor between Urubamba and Ollantaytambo; keep Yanahuara as an additional/alternate candidate sampling area pending station design.
- Do not claim Huarán is the exact midpoint; current geodata supports it as an intermediate point but not an exact midpoint claim.
- Replace the visually confusing two-column duplication of Huambutío with one shared confluence node: main stem + Huatanay tributary branch -> one Huambutío mixing point -> downstream corridor.
- Clarify that M1–M4+ are candidate measurement logic, not a finalized station network.
- Keep Cusco/Huatanay participation as an explicit Phase 1 vs Phase 2 team decision while allowing measurement geography to extend beyond benefit geography.
- Remove the redundant cards `Primary working scope`, `Measurement can extend upstream`, and `No scope inflation`; their unique meaning is already carried by the corridor, measurement-logic and downstream-continuity blocks.
- Replace the ambiguous `Capacity pressure / US$46M` card with one compact `Huatanay infrastructure context` note. It identifies the actual project as the PTAR Cusco / San Jerónimo expansion, dates the 2023 capacity figures, and explicitly avoids freezing the obsolete US$46M estimate as a current project value.
- Preserve the two existing external PTAR/SUNASS href values and the existing `#validation` internal link.

## Deterministic preservation result

PASS

- approved v16.4 HTML SHA-256: `5c28d9256b2ad86bdac4511d1bfc431ec5b3cb4d8e1341430dd84b14256c3719`
- revised v16.5 HTML SHA-256: `d7a644d97a6cb995e6ee444ab3138ea4321f9409318e697d2d94edca67e1a460`
- revised `#system` SHA-256: `3a9fd19749825020c0381c1dd058b476cb66c87f3af55f82de719e5d119151a9`
- only changed section relative to approved v16.4: `#system`
- section count unchanged
- external hrefs: 46, values and order unchanged
- Stanley/WGA raw section SHA-256 unchanged: `d22889e1b98d8f49d3ea09f74092e97273d06964852e19b20c0aebd26d5525e1`
- Stanley/WGA: 13 images / 17 links
- all 16 assets unchanged byte-for-byte
- one shared Huambutío confluence heading
- old `estimated US$46M project` phrase absent
- redundant rev-1 scope-card headings absent

## Review transport

1. Primary approval surface: compact zero-network ChatGPT Preview containing the revised `#system` section.
2. Cumulative context surface: stable review-only route `https://felipeacha.github.io/converging-waters/candidates/progress/`, labeled `v16.5 PROPOSED · REV 2`, with frontier `#system`.

The cumulative route remains `REVIEW_TRANSPORT_ONLY`; it does not repoint `/preview/`, modify `/releases/v13/`, or promote v16.5.

## Evidence boundary

The detailed locality, naming, hydrology and PTAR investment-history evidence lives in `docs-governance/registries/WILLKAMAYU_HYDROLOGY_AND_EVIDENCE_REGISTER.md`.

Website rule for this section: preserve the minimum narrative needed to understand the system, candidate measurement logic and open phase choices. Avoid repeating scope disclaimers as multiple cards and avoid presenting volatile monetary estimates without a date/source context.

## Next transition

If Felipe approves revised v16.5, it becomes the last approved local state. The next website delta must start from v16.5 and touch one new target only.
