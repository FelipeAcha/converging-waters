# Converging Waters ally web recovery — Phase 0 baseline lock

**Date:** 2026-09-02  
**Gate:** `CW-WEB-ALLY-RECOVERY-PHASE0-BASELINE-LOCK`  
**Status:** PASS  
**Execution mode:** Incremental Control + Web Workstream Control  
**Mutation policy:** preserve-first / minimum necessary change  
**Public route mutation:** NONE

## 1. Pre-execution reconciliation against Felipe's latest instructions

The frozen Definition of Done and execution plan were rechecked against every material requirement in the immediately preceding user instruction before any website mutation.

| Requirement | Coverage | Result |
|---|---|---|
| Do not rebuild/regenerate HTML; use the mature hub exactly and patch only what is necessary | Definition of Done §0, §2, D01-D18; Phase 0 copy-first rule | PASS |
| A separate always-visible conclusion is unnecessary when the heading already communicates the main point | F04-F05 | PASS |
| Do not change current progressive disclosure in this recovery cycle | F01-F02, F06-F10 | PASS |
| Nested accordions are allowed; do not remove them simply for being nested | F03, Q13 | PASS |
| Preserve the existing major infographic essentially unchanged; only bounded current-status correction if Amazonas Sagrada is represented as core/protagonist | G13-G14; migration policy | PASS |
| Use Incremental Control and Web Workstream Control; work from coarse full-page context to bounded section-by-section deltas | Current execution stack; Phase 1 + Phase 2 | PASS |
| Keep effort and mutation to the minimum; continuously compare work against the frozen plan/checklist | Governing rule, D01-D18, review-report contract, preservation manifest | PASS |
| Maria Gracia -> potential ally and Amazonas Sagrada -> potential ally, without erasing useful prior findings | H12-H14, I04-I06, K01-K11 | PASS |
| Do not spend time re-researching Canchis in the current recovery cycle | hard preservation rule 10; L01/L14 | PASS |

**Coverage conclusion:** no material requirement from the latest instruction is unrepresented in the current frozen execution contract. Generic UX preferences may not override the project-specific baseline or explicit user decisions.

## 2. Exact source baseline

**Drive source file:** `CW-WEB-v16.9 - REV33 - Localized Precedent Images + Immutable Release QA - 2026-08-25 - REVIEW.html`  
**Drive source ID:** `1jAN0Ic9J-fW_EKfQKJO_2vm9bS-JUSSt`  
**Size:** `14,985,914 bytes`  
**SHA-256:** `8a6cba580702e696594dfa7b347cb2e979fc3e966780653a1d60a6a84c894723`

This is the mature hub implementation baseline for the recovery workstream.

## 3. Exact candidate copy

A Drive copy was created directly from the source file, not reconstructed from HTML text, summaries, screenshots, prior candidates or model output.

**Candidate file:** `CW-WEB - Ally Recovery - Phase 0 Exact Baseline Candidate - 2026-09-02.html`  
**Drive candidate ID:** `1tXU8wJn22k9T19hiE41k8xZDtSnZMI3c`  
**Size after raw readback:** `14,985,914 bytes`  
**SHA-256 after raw readback:** `8a6cba580702e696594dfa7b347cb2e979fc3e966780653a1d60a6a84c894723`  
**Byte comparison:** `cmp_exit=0`

Result: **baseline and candidate are byte-identical before the first patch.**

## 4. Deterministic preservation audit

Manifest:
`docs-governance/validation/CW-WEB-ALLY-RECOVERY-PHASE0-MANIFEST-2026-09-02.json`

`audit_web_candidate.py` result:

```text
status=PASS
baseline_html_sha256=8a6cba580702e696594dfa7b347cb2e979fc3e966780653a1d60a6a84c894723
candidate_html_sha256=8a6cba580702e696594dfa7b347cb2e979fc3e966780653a1d60a6a84c894723
identified_section_ids=32
external_anchor_hrefs=97
errors=[]
```

The HTML contains 33 top-level `<section>` blocks when the id-less hero is included. All 32 id-bearing sections are protected in the Phase 0 manifest; no changed, added or removed sections are authorized.

## 5. Structural preservation fingerprint

### Section order

`hero -> current-session -> changed-since -> where-now -> shared-direction -> collaboration-layer -> emerged-since-call -> stanley-update -> agenda -> thesis -> context -> people-authority-boundary -> people -> three-paths -> willkamayu -> collaboration-framework -> system -> evidence-to-implementation -> rev20-roadmap-orientation -> open-decisions -> first-outcome -> what-we-need-now -> river-economy-overview -> rev20-enabling-orientation -> amazonas-application -> technical-options -> finance-hypotheses -> alliance-architecture -> people-guardians-stewardship -> guardians-legal -> precedents -> deep-dives -> current-roadmap-final`

### Existing disclosure system

- `<details>` count: `27`
- current distribution: collaboration-framework `3`; system `3`; amazonas-application `1`; alliance-architecture `2`; guardians-legal `12`; precedents `6`
- ordered summary-text SHA-256: `54b07260902e411730ed5c02abda33bcca05e1a65b53a11ca9b27b134b71da61`
- ordered details DOM SHA-256: `b939e638874e65eec42423761953c622497632641ca5c17db94eee54e7e3089e`
- policy: preserve the implementation exactly during recovery; nested disclosures remain allowed and may not be prohibited by a generic UX rule.

### Links, images and styles

- anchors: `115`
- external hrefs: `97`
- ordered external href SHA-256: `c6d05423c4c8a88c07d8beb76b7d4c22c54d50d88797e734d69a183de9592ec8`
- images: `19`
- ordered image section/alt/source fingerprint SHA-256: `ac46c0564b9b7ce7a9dfb4c47c2eb00413b3a5d86a8f6cf68eaa219150726803`
- style blocks: `8`
- ordered style-text SHA-256: `e107a0a5a9deb33300fb6ec42651c23ba915c9efe99c41f58684d9ef2080e117`

### Alliance Architecture protected fingerprint

- details: `2`
- tables: `1`
- alliance matrix rows: `49`
- alliance matrix cells: `269`
- matrix DOM SHA-256: `1ddf3e070bc8d01e0161de1449f4d6f83c42c1c52c15db5bf6ab3286467c4151`
- full section raw SHA-256: `03adaa4acb6456d6606fa7ab9796eaa5d6af8a59a58e119f298c0ff8e406e65a`

### Major visual / initiative-context fingerprints

- `three-paths` raw section SHA-256: `1be1a7d9087c28f13bcb1027d879aa4983bb70633f29f9b969d311e8de327349`
- `willkamayu` raw section SHA-256: `ae74a6aab37b80c8a99ce6d34b3d620bfb8d0530480ccccd7c4b6a15f01c5b24`
- embedded Willkamayu visual source SHA-256: `4c7cf432bda35e954952ffba99a466a72b493cb27226ea84ff1b01ea317c0049`

These are preservation anchors. They do not authorize redesign; future bounded changes must identify the exact affected subcomponent and preserve the remainder.

## 6. Phase 0 acceptance

- exact source recovered: PASS
- raw source hash established: PASS
- separate Drive candidate created by direct copy: PASS
- raw candidate read back: PASS
- source/candidate size equality: PASS
- source/candidate SHA-256 equality: PASS
- byte comparison: PASS
- deterministic preservation audit: PASS
- section-order baseline recorded: PASS
- disclosure baseline recorded: PASS
- image/link/style fingerprints recorded: PASS
- Alliance Architecture/matrix fingerprint recorded: PASS
- major visual context fingerprint recorded: PASS
- semantic/content mutations: `0`
- public website mutations: `0`

## 7. Gate state

`PHASE0_BASELINE_LOCK = PASS`

The next committed transition is **Phase 1 — coarse structural/current-reality pass**. It has **not** started in this checkpoint.

Phase 1 remains bounded to the already-authorized macro corrections: remove/reframe internal review/session wrappers after harvesting useful content; update current top-level relationship/status reality; downgrade Amazonas Sagrada and Maria Gracia to potential allies where represented; preserve WGA's current role; preserve infographic/visual system, Alliance Architecture, matrix, disclosure implementation, colors, layout, substantive findings and every unrelated block.

No public promotion is authorized.
