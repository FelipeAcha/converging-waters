# Converging Waters Web — Definition of Done v2

**Status:** CURRENT GOVERNING STANDARD  
**Date:** 2026-09-02  
**Scope:** ally-facing one-page hub, specialist deep dives, recovery candidates and review surfaces.

## 0. Authority order

`CURRENT USER DECISION > EFFECTIVE PUBLISHED HUB > PROJECT-SPECIFIC CONTRACT > GENERIC UX GUIDANCE`

The effective published hub is the implementation baseline. A Drive review file, historical REV, prior candidate, screenshot, or previous automated PASS may be evidence, but none supersedes the bytes actually deployed on the published hub.

## 1. Baseline resolution gate — mandatory before mutation

- [ ] B01. Resolve the latest successful GitHub Pages deployment artifact.
- [ ] B02. Decode the effective hub bytes from its payload.
- [ ] B03. Record full-page SHA-256 and deployment head SHA.
- [ ] B04. Compare later repository commits to prove whether `docs/index.html`, `docs/payload/**`, `docs/assets/**` or another deployed web input changed after that deployment.
- [ ] B05. If later deployed inputs changed, resolve the later effective deployment before editing.
- [ ] B06. Historical REV files may be used only as provenance for a block when current published bytes prove the same block is identical.

Current lock evidence at adoption:
- effective published HTML SHA-256: `3b296999839430c2a1029e41ff404e3de368c1a66b85d1f1503e1c539a2f0f0e`;
- successful Pages deployment head: `a1ac1277765c48706bec7a2446185cd8b05befe3`;
- subsequent commits through `351639cae5d0495af72511da87f5ec0eb7e4638f` changed governance/status files only, not deployed web inputs.

## 2. Default mutation rule

`KEEP -> UPDATE ONLY EXPLICITLY AUTHORIZED COPY -> PRESERVE DOM/ATTRIBUTES -> VERIFY RAW AND VISUAL INVARIANTS`

- [ ] P01. Default action is KEEP.
- [ ] P02. No section is regenerated from memory or from an older REV.
- [ ] P03. No removed section, wrapper, card, image, link or disclosure may reappear merely because it existed in an older source.
- [ ] P04. Any changed section must have an explicit reason and declared delta.
- [ ] P05. Copy-only changes must preserve the published DOM and attribute structure exactly.
- [ ] P06. External href sequence, image records, executable CSS and scripts remain exact unless separately authorized.
- [ ] P07. Generic readability or design preferences never authorize restructuring a protected mature component.

## 3. Alliance Architecture — hard frozen bundle

Felipe's 2026-09-02 correction supersedes earlier permission to update relationship/status cells inside this component.

The frozen bundle comprises:
1. top-level accordion wrapper `data-cw-section="14"`;
2. `#alliance-architecture` in full, including headings, callouts, cards, disclosures and matrix;
3. the attached `#people-guardians-stewardship` block because the published Alliance trigger controls its visibility;
4. the existing responsive/mobile behavior associated with that disclosure.

Hard identities at adoption:
- Alliance section SHA-256: `03adaa4acb6456d6606fa7ab9796eaa5d6af8a59a58e119f298c0ff8e406e65a`;
- Alliance wrapper SHA-256: `3fac530898ff763cf2e685d2908558b4622aa8385a2ba80857b00a762510de33`;
- attached stewardship section SHA-256: `6b461310204fac3dae51ee1733865bbe6d4099c402e929ada914bd9e6a326388`.

- [ ] A01. Alliance raw section hash equals the published hash.
- [ ] A02. Alliance wrapper raw hash equals the published hash.
- [ ] A03. Attached stewardship raw hash equals the published hash.
- [ ] A04. Matrix remains 49 rows / 269 cells.
- [ ] A05. Desktop component pixel comparison against published = zero differing pixels for the tested state.
- [ ] A06. Mobile component pixel comparison against published = zero differing pixels for the tested state.
- [ ] A07. Matrix-open visual state is compared on desktop and mobile.
- [ ] A08. Any mismatch is blocking; row/cell counts or no-overflow results cannot override a raw/pixel mismatch.
- [ ] A09. No status/copy update occurs inside the frozen bundle unless Felipe explicitly reopens it.

## 4. Other protected components

- [ ] C01. `#precedents` raw bytes remain published-identical unless explicitly reopened.
- [ ] C02. `#people-authority-boundary` raw bytes remain published-identical unless explicitly reopened.
- [ ] C03. Existing progressive-disclosure implementation and nesting remain unchanged.
- [ ] C04. Nested accordions are allowed and protected.
- [ ] C05. The major initiative graphic/card structure stays in the published geometry unless a bounded change is explicitly authorized.
- [ ] C06. Existing visual identity, palette, typography, cards, diagrams and semantic color families remain the baseline.

## 5. Audience and language

- [ ] L01. Primary audience is potential allies and collaborators with no assumed project history.
- [ ] L02. First screen states territory, purpose and collaboration status directly.
- [ ] L03. Public copy is primarily affirmative and substantive.
- [ ] L04. Avoid identity-by-negation formulas and generic AI/corporate phrasing.
- [ ] L05. Necessary scientific/legal caveats may use negation where precision requires it.
- [ ] L06. No hype, sales funnel, urgency marketing or empty slogans.
- [ ] L07. No internal development/version/process language in public title, meta, body, footer or HTML comments.
- [ ] L08. `ChatGPT`, `OpenAI`, review-candidate, rollback/checkpoint/gate, REV/version-development and similar internal markers are prohibited on the ally-facing page.
- [ ] L09. Legitimate domain uses of words such as `candidate` or `review` are allowed when they refer to monitoring/scientific work rather than web-development process.

## 6. Current project framing outside frozen blocks

- [ ] S01. Willkamayu–Vilcanota–Urubamba is the territorial focus.
- [ ] S02. Felipe is represented according to current project direction where relevant.
- [ ] S03. WGA is represented according to the current scientific-technical convergence relationship.
- [ ] S04. Amazonas Sagrada may be framed as a potential ally outside the frozen Alliance bundle.
- [ ] S05. María Gracia may be framed as a potential ally outside frozen published blocks.
- [ ] S06. Person, organization, capability, interest, authority and commitment remain distinct.
- [ ] S07. No community or institution is assigned authority or commitment without evidence.

## 7. Substantive preservation

- [ ] D01. Homepage remains substantial; deep dives add depth rather than emptying it.
- [ ] D02. Willkamayu river-system/ecological/cultural/economic context remains.
- [ ] D03. Observatory, source attribution, main-stem/tributary logic, QA/QC and Huatanay context remain.
- [ ] D04. Evidence-to-implementation chain remains.
- [ ] D05. Citizen science, schools, stewardship and WGA technical possibilities remain with appropriate caveats.
- [ ] D06. Rights/guardianship/legal architecture remains; current Canchis material is preserved without re-research in this recovery cycle.
- [ ] D07. River Economy, livelihoods, tourism/recreation, financing hypotheses and safeguards remain.
- [ ] D08. Precedents remain visual and Peru-first.
- [ ] D09. Useful findings are not deleted merely because a participant's current relationship changed.

## 8. Technical/browser QA

- [ ] Q01. Exactly one H1.
- [ ] Q02. No duplicate IDs.
- [ ] Q03. Same top-level section order as the effective published baseline unless explicitly authorized.
- [ ] Q04. No resurrected historical section absent from current published baseline.
- [ ] Q05. Desktop document-level horizontal overflow = zero.
- [ ] Q06. Mobile document-level horizontal overflow = zero.
- [ ] Q07. All current images decode.
- [ ] Q08. Top-level accordions open/close and restore state.
- [ ] Q09. Existing nested `<details>` controls open/close and restore state.
- [ ] Q10. Existing matrix mobile containment behavior remains.
- [ ] Q11. Browser QA must include targeted visual checks of protected components; generic whole-page screenshots are not sufficient evidence.

## 9. Review surface — mandatory human gate

- [ ] R01. Felipe reviews a wireframe/Preview, not raw HTML.
- [ ] R02. A downloadable HTML file may exist as machine evidence but is never the primary user-review artifact.
- [ ] R03. Screenshot galleries are QA evidence, not the primary review surface.
- [ ] R04. Wireframe/Preview must represent the exact candidate copy and component structure being proposed.
- [ ] R05. Frozen components are visibly marked as frozen in the review surface.
- [ ] R06. No production/public promotion before explicit approval of the review surface.

## 10. Fail-closed acceptance

A candidate is `PASS` only when all applicable hard gates pass. These signals are necessary but not sufficient by themselves: row counts, cell counts, link counts, screenshot existence, no-overflow, generic ACB success, or a previous candidate PASS.

A candidate MUST FAIL if:
- the baseline is not the effective published hub;
- any frozen raw hash differs;
- a frozen visual comparison differs;
- an unlisted structural mutation appears;
- a historical section reappears;
- the review surface is raw HTML instead of wireframe/Preview;
- any rejected/stale candidate is configured as a blocking ACB surface;
- the published freeze contract is not a hard blocking gate.

## 11. ACB enforcement

The ACB watchdog must:
- run generic browser health checks on the published-working hub as monitor-only when they surface pre-existing baseline defects;
- treat the deterministic published freeze contract as the hard blocking preservation gate;
- treat rejected historical candidates as monitor-only;
- run `.github/acb/validate_published_freeze.py` against decoded `docs/payload/hub-*.txt` on every relevant web change;
- fail on any frozen Alliance/stewardship/precedent/authority-boundary hash mismatch;
- persist deterministic evidence.

## 12. Current lifecycle

`PUBLISHED_BASELINE_LOCKED -> CANDIDATE_SOURCE_VALIDATED -> PROTECTED_VISUAL_DIFF_PASS -> WIREFRAME_REVIEW -> USER_APPROVAL -> PROMOTION`

Skipping a state is a failure.
