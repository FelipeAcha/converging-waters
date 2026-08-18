# CW-WEB v16.4 — Preview gate

Status: PENDING USER REVIEW
Date: 2026-08-18
Parent workstream: issue #5

## Approved baseline

v16.3 local state was explicitly approved by Felipe in the Converging Waters Project chat.

## One authorized delta

Suppress only the residual visible wrapper of `#purpose-mrv` by adding `hidden aria-hidden="true"` to that section.

The detailed native HTML/CSS infographic reconstruction inside `#purpose-mrv` was already suppressed in approved v16.1.1. The residual section heading/intro therefore created an empty duplicate shell later in the page after the principal original infographic had been moved to the top.

No source content inside `#purpose-mrv` is deleted or rewritten. Its inner HTML remains byte-identical; only the section opening tag changes.

## Deterministic preservation result

PASS

- baseline HTML SHA-256: `6d3acae3ddfeeb7a72f089a205e8a3483130560ea0ad030fb598a8b9bf8ae09a`
- candidate HTML SHA-256: `5c28d9256b2ad86bdac4511d1bfc431ec5b3cb4d8e1341430dd84b14256c3719`
- baseline sections: 41
- candidate sections: 41
- external hrefs: 46, unchanged
- Stanley/WGA protected section remains byte-identical
- all 16 assets unchanged
- exact whole-document diff normalizes to zero when the two authorized attributes are removed
- `#purpose-mrv` inner-content SHA-256 preserved: `8334e4aec880e4cab4d39b547f08c5105b44c313dafe251db8e74de668717f8a`

## Review transport

1. Primary approval surface: compact zero-network ChatGPT Preview showing the end of `#citizen-science`, the hidden `#purpose-mrv` position, and adjacent `#system` context.
2. Cumulative context surface: stable review-only route `https://felipeacha.github.io/converging-waters/candidates/progress/` showing approved v16.1.1 + v16.2 + v16.3 with v16.4 proposed, through the current reviewed frontier.

The public cumulative route is review transport only. It does not repoint `/preview/`, does not modify `/releases/v13/`, and does not promote v16.4.

## Browser validation limitation

A fresh local Chromium/Playwright navigation attempt was blocked by the execution environment with `ERR_BLOCKED_BY_ADMINISTRATOR` for both `file://` and localhost navigation. Per the web-workstream recovery rule, no further equivalent browser retries were attempted. Deterministic source validation passed; exact-surface ChatGPT Preview and the explicitly authorized stable cumulative route remain the review gates.

## Next transition

If Felipe approves v16.4, it becomes the last approved local state and the workstream continues with one new delta only.
