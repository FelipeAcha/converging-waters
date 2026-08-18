# CW-WEB v16.4 — Preview gate

Status: APPROVED 2026-08-18
Date: 2026-08-18
Parent workstream: issue #5

## Approved baseline

v16.3 local state was explicitly approved by Felipe in the Converging Waters Project chat.

## Approved delta

Suppress only the residual visible wrapper of `#purpose-mrv` by adding `hidden aria-hidden="true"` to that section.

The detailed native HTML/CSS infographic reconstruction inside `#purpose-mrv` was already suppressed in approved v16.1.1. The residual section heading/intro therefore created an empty duplicate shell later in the page after the principal original infographic had been moved to the top.

No source content inside `#purpose-mrv` was deleted or rewritten. Its inner HTML remains byte-identical; only the section opening tag changed.

## Deterministic preservation result

PASS

- baseline HTML SHA-256: `6d3acae3ddfeeb7a72f089a205e8a3483130560ea0ad030fb598a8b9bf8ae09a`
- candidate HTML SHA-256: `5c28d9256b2ad86bdac4511d1bfc431ec5b3cb4d8e1341430dd84b14256c3719`
- baseline sections: 41
- candidate sections: 41
- external hrefs: 46, unchanged
- Stanley/WGA protected section remains byte-identical
- all 16 assets unchanged
- `#purpose-mrv` inner-content SHA-256 preserved: `8334e4aec880e4cab4d39b547f08c5105b44c313dafe251db8e74de668717f8a`

## Review outcome

Felipe explicitly approved v16.4 in the Converging Waters Project chat on 2026-08-18 while requesting that the subsequent `#system` hydrology/monitoring section be corrected as a separate delta. That separate delta is v16.5.

## Browser validation limitation

A local Chromium/Playwright navigation attempt was blocked by the execution environment with `ERR_BLOCKED_BY_ADMINISTRATOR` for both `file://` and localhost navigation. Deterministic source validation passed; exact-surface ChatGPT Preview and the explicitly authorized cumulative route supplied the review evidence.

## Next transition

CLOSED — v16.4 is the approved baseline for v16.5.
