# Converging Waters ally web recovery — final QA and user-review gate

**Date:** 2026-09-02  
**Status:** SOURCE + BROWSER VALIDATED · USER APPROVAL PENDING  
**Mutation policy:** preserve existing mature hub / minimum necessary change  
**Production/main mutation:** NONE

## 1. Exact final review candidate

**Drive file:** `CW-WEB - Ally Recovery - Final Review Candidate - 2026-09-02.html`  
**Drive ID:** `1yqkMDDeB1DUjmktMdxk_oZMj9JsbJCrc`  
**Size:** `14,984,905 bytes`  
**SHA-256:** `0da596869b6adcb97fd45a257bfca41f2f15f8a2441da4b21135bac41ab7a73b`

The Drive raw file was downloaded after upload and compared byte-for-byte with the locally validated candidate:

```text
local_sha256=0da596869b6adcb97fd45a257bfca41f2f15f8a2441da4b21135bac41ab7a73b
drive_readback_sha256=0da596869b6adcb97fd45a257bfca41f2f15f8a2441da4b21135bac41ab7a73b
cmp_exit=0
```

## 2. Definition-of-Done deterministic audit

Fresh final audit result:

```text
overall=PASS
checks=28
errors=[]
candidate_sha256=0da596869b6adcb97fd45a257bfca41f2f15f8a2441da4b21135bac41ab7a73b
```

Verified control clusters include:

- all 33 top-level sections remain in source order;
- all 27 existing `<details>` disclosures retain the same summaries, nesting/default-open state and structure;
- 97 external hrefs remain in the same ordered sequence;
- all 19 image src/alt/title records remain preserved;
- all 8 CSS rule blocks are semantically identical after ignoring removed development comments;
- public title, meta description and footer contain no development/version/review/AI process language;
- visible internal-development marker scan = zero prohibited patterns;
- HTML development comments = zero; CSS development comments = zero;
- current representation includes Felipe as project direction, WGA as scientific-technical convergence partner, and potential-ally framing;
- Amazonas Sagrada is no longer a core/protagonist initiative;
- María Gracia is represented as a potential ally;
- major initiative infographic contains the preserved WGA and Willkamayu cards and no Amazonas core card;
- Alliance matrix remains 49 rows / 269 cells; the only row whose HTML differs from the mature source is Amazonas Sagrada;
- Amazonas row = `POTENTIAL ALLY`; no `Core autonomous initiative` language remains in that row;
- core Canchis legal facts already present in the mature hub remain present; no Canchis re-research was performed;
- one H1, unique IDs, zero missing internal fragments, zero missing alt text, zero loading/error placeholders;
- heading redundancy thresholds pass: connect=0, connecting=0, shared=3, pathway=4, architecture=2, opportunity=1, evidence=10;
- no high-similarity H2 pair, no exact duplicated long paragraph, and no top-level identity-by-negation heading pattern.

## 3. Final preservation correction from visual review

Browser review exposed one remaining obsolete ally-specific wrapper inside Alliance Architecture: a `September field window`, a welcome specifically framed around Simona, and an informal evening at Felipe's home. These were not useful as current public facts and conflicted with the ally-facing audience rule.

The correction changed only the surrounding narrative copy to a durable pattern: relationship-building in the Sacred Valley, an informal convergence gathering when useful, and focused readiness conversations. The protected alliance matrix was not changed by this correction. Its disclosure summary `Invite list to confirm` was deliberately restored unchanged after a first attempted label replacement triggered the disclosure-preservation regression.

This is a concrete example of the governing rule working as intended: a proposed generic cleanup failed the protected-disclosure test, was narrowed, and the exact existing disclosure label was preserved.

## 4. Exact browser QA

Direct `file://` and localhost navigation are blocked by this runtime's browser administrator policy. The exact candidate was therefore rendered in Playwright/Chromium with `page.set_content()` from the same UTF-8 HTML bytes. A QA-only eager-load trigger re-used each image's identical `src` payload to force the candidate's native lazy images to decode; it did not change candidate source bytes or content.

Fresh browser result:

```text
overall=PASS
candidate_sha256=0da596869b6adcb97fd45a257bfca41f2f15f8a2441da4b21135bac41ab7a73b
errors=[]
```

### Desktop · 1440 × 1000

- document/body scroll width: `1440 / 1440`;
- horizontal document overflow: none;
- outer section/main/footer overflow: none;
- images: `19`, failures `0`;
- disclosures: `27`, toggle/restore failures `0`;
- major initiative cards: `2`;
- Alliance matrix: `49 rows / 269 cells`.

### Mobile · 390 × 844

- document/body scroll width: `390 / 390`;
- horizontal document overflow: none;
- outer section/main/footer overflow: none;
- images: `19`, failures `0`;
- disclosures: `27`, toggle/restore failures `0`;
- major initiative cards: `2`;
- Alliance matrix: `49 rows / 269 cells`.

The Alliance matrix was also tested while its disclosure was explicitly open. Desktop remains within the page width. On mobile the established table is wider than the viewport inside its existing contained horizontal-scroll behavior, while the document itself remains `390px` wide with no page-level overflow. No responsive redesign was introduced.

## 5. Human visual inspection

Exact-candidate screenshots were inspected for:

- desktop and mobile first screen / hero;
- WGA + Willkamayu major initiative graphic;
- Alliance Architecture narrative;
- Alliance matrix with disclosure open;
- Legal / protection architecture and accordion cards.

No new clipping, broken images, document-level overflow, card collision or disclosure malfunction was observed. The visual grammar, palette, typography, cards, diagrams and existing progressive-disclosure behavior remain the mature hub design rather than a new redesign.

## 6. Lifecycle state

```text
BASELINE_LOCK=PASS
PHASE1_CURRENT_REALITY=PASS
PHASE2_BOUNDED_ADAPTATION=PASS
FINAL_DOD_SOURCE_AUDIT=PASS
BROWSER_RENDER_VALIDATED=PASS
DRIVE_RAW_READBACK=PASS
USER_APPROVED=false
PROMOTED=false
PUBLIC_MAIN_MUTATED=false
```

## 7. Gate

The workstream is now at **FINAL USER REVIEW**. The candidate must not be promoted or replace the current main/public authoritative route until Felipe explicitly approves the exact review candidate identified by SHA-256 above.