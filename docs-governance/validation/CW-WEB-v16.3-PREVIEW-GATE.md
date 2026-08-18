# CW-WEB v16.3 — Preview gate

Status: PENDING USER REVIEW
Date: 2026-08-18
Parent workstream: issue #5

## Approved baseline

v16.2 local state was explicitly approved by Felipe in the Converging Waters Project chat.

## One authorized delta

Remove only the second visual rendering of:

`Listen → Measure → Train → Pilot → Mandate → File or legislate`

from `#thesis`.

The exact same territorial-pathway sequence remains in `#where-now`, which becomes its single active home.

## Deterministic preservation result

PASS

- baseline HTML SHA-256: `d378b280d2b85df212d44ce517626b415ece225a07e1287d33b62f07e35b5f79`
- candidate HTML SHA-256: `6d3acae3ddfeeb7a72f089a205e8a3483130560ea0ad030fb598a8b9bf8ae09a`
- baseline sections: 41
- candidate sections: 41
- external hrefs: 46, unchanged
- Stanley/WGA raw section SHA-256 unchanged: `d22889e1b98d8f49d3ea09f74092e97273d06964852e19b20c0aebd26d5525e1`
- all assets unchanged
- only `#thesis` differs relative to approved v16.2
- exact HTML diff: deletion of one 13-line `.sequence` block only

## Review transport

Compact zero-network ChatGPT Preview slice containing exact `#where-now` and `#thesis` markup with local review CSS only.

Transport properties:
- 5,937 bytes
- 0 iframes
- 0 automatic HTTP(S) references
- 0 images
- territorial pathway headline appears exactly once
- no `.sequence` duplicate remains in `#thesis`

## Browser caveat

A local Chromium screenshot invocation hung in the current container after page construction. No content claim depends on that browser run. Source/preservation validation passed, and exact-surface ChatGPT Preview remains the active review gate. Do not retry or reinterpret the browser hang as a website-content failure.

## Next transition

If Felipe approves the zero-network Preview, v16.3 becomes the last approved local state and the workstream advances to one new delta only.
