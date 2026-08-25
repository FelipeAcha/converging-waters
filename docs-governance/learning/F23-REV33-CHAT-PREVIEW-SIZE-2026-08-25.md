# F23 — REV33 Chat Preview unavailable after self-contained image localization

**Date:** 2026-08-25
**Workstream:** Converging Waters web
**State:** CONFIRMED · CORRECTIVE TRANSPORT CREATED · RELEASE ARTIFACT UNCHANGED
**Production:** NOT AUTHORIZED / NOT MODIFIED

## Failure
After REV33 localized the five precedent photographs into the self-contained review HTML, the exact standalone review artifact grew to 14,985,914 bytes. The user reported that ChatGPT displayed `Vista previa no disponible` instead of the page.

## Classification
- `TOOL_CONTRACT_MISMATCH`
- `SURFACE_AMBIGUITY`
- `INSUFFICIENT_EVIDENCE`

## First control failure
Release QA proved the exact artifact and browser rendering, but the final handoff did not re-prove the **actual ChatGPT Preview surface** after the artifact size increased materially. Browser-valid and file-valid were incorrectly treated as sufficient evidence for Chat Preview availability.

## Corrective action
Created a separate review-only transport:

`CW-WEB-v16.9 - REV33 - VISUAL-PREVIEW-LIGHT - 2026-08-25.html`

- size: 1,986,485 bytes
- SHA-256: `21dc076f6eb889a73401c0c0fd49c2ed20f65bb2e2197f104d5ed6bf8999f370`
- body text: identical to the REV33 release-tree Hub
- href sequence: identical, 115/115
- alt sequence: identical, 19/19
- id sequence: identical, 37/37
- image count: identical, 19/19
- remote image refs: 0
- relative image refs: 0
- Wikimedia upload image refs: 0

Only the five precedent-photo bytes are visually recompressed/downscaled in this review transport to stay inside a practical Chat Preview payload; the exact REV33 release candidate and its original localized image bytes remain unchanged and authoritative.

## Prevention for audit/reengineering
1. Treat `CHAT_PREVIEW_USER_VISIBLE` as a distinct lifecycle state after any material asset-size change.
2. Re-run the exact in-chat Preview canary/transport check after image localization or large data-URI embedding.
3. Add a Preview payload budget check before handing off an HTML attachment to ChatGPT Preview.
4. When the release artifact is too heavy for Chat Preview, create a clearly labeled `REVIEW_TRANSPORT_ONLY` derivative whose text, href, alt, IDs, layout rules and image count are regression-compared against the release candidate.
5. Never mutate or recompress the authoritative release artifact merely to satisfy a review-surface limitation.

## Rollback
Delete/disregard the lightweight review transport. REV33 release candidate, REV32 baseline and production state are unaffected.
