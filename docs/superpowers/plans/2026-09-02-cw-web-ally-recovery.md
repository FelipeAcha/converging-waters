# Converging Waters Ally Web Recovery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce the ally-facing Converging Waters hub by patching the exact mature REV33 HTML only where the approved Definition of Done requires, preserving all other content, layout, visuals, accordions, links and evidence.

**Architecture:** The source of truth for implementation is the exact raw Drive HTML identified in Phase 0. Work occurs on isolated descendants of that byte-identical candidate, never by rebuilding the page. Each phase uses a bounded mutation manifest, deterministic preservation checks, full-page context, and a durable raw HTML checkpoint before advancing.

**Tech Stack:** Static HTML/CSS/JS; Python 3 deterministic patch/audit scripts run locally; BeautifulSoup/lxml only for inspection and bounded node edits where exact string replacement is unsafe; browser QA where available; Google Drive for immutable raw review HTML; GitHub for specifications, manifests, validation reports and regression evidence.

**Spec:** `docs-governance/standards/CW_WEB_DEFINITION_OF_DONE_v1.md`

## Global Constraints

- Source baseline Drive ID: `1jAN0Ic9J-fW_EKfQKJO_2vm9bS-JUSSt`.
- Phase 0 exact-copy candidate Drive ID: `1tXU8wJn22k9T19hiE41k8xZDtSnZMI3c`.
- Baseline SHA-256: `8a6cba580702e696594dfa7b347cb2e979fc3e966780653a1d60a6a84c894723`.
- `DEFAULT_CONTENT_ACTION = KEEP`.
- Patch existing HTML; never regenerate or reconstruct it.
- Existing progressive disclosure is frozen for this recovery pass; nested accordions are allowed and protected.
- A separate summary paragraph is not required when the heading already communicates the point.
- Alliance Architecture and its large matrix are protected; only explicitly authorized status/copy cells may change.
- The major infographic is protected; only the Amazonas Sagrada / Maria Gracia current-status representation may change if present and inconsistent.
- Amazonas Sagrada = potential ally, not a current core/protagonist initiative.
- Maria Gracia = potential ally, not current co-author/core project lead.
- Felipe retains current project direction where leadership is represented.
- WGA remains the current scientific-technical convergence partner; potential technologies must not be presented as confirmed deployments.
- No Canchis re-research in this recovery cycle.
- Every removed time-bound/internal wrapper must first preserve/rehome all ally-relevant substance.
- External hrefs, images, styles, untouched DOM and unrelated text remain byte-identical wherever possible.
- No public promotion before final user preview and explicit approval.

---

### Task 1: Phase 1 current-reality and internal-wrapper patch

**Files:**
- Read-only baseline: `/mnt/data/CW-WEB - Ally Recovery - Phase 0 Exact Baseline Candidate - 2026-09-02.html`
- Create working candidate: `/mnt/data/cw_ally_recovery/phase1/index.html`
- Create patch manifest: `/mnt/data/cw_ally_recovery/phase1/manifest.json`
- Create patch script: `/mnt/data/cw_ally_recovery/tools/phase1_patch.py`
- Create regression script: `/mnt/data/cw_ally_recovery/tools/verify_phase1.py`
- Persist report: `docs-governance/validation/CW-WEB-ALLY-RECOVERY-PHASE1-2026-09-02.md`
- Persist manifest: `docs-governance/validation/CW-WEB-ALLY-RECOVERY-PHASE1-MANIFEST-2026-09-02.json`

**Interfaces:**
- Consumes: exact Phase 0 candidate bytes and current factual authority already captured in project records.
- Produces: one full-page Phase 1 candidate with only macro current-reality/internal-wrapper mutations and a machine-readable change ledger.

- [ ] **Step 1: Copy Phase 0 candidate exactly and verify hash before patching**

Run:
```bash
mkdir -p /mnt/data/cw_ally_recovery/phase1 /mnt/data/cw_ally_recovery/tools
cp '/mnt/data/CW-WEB - Ally Recovery - Phase 0 Exact Baseline Candidate - 2026-09-02.html' /mnt/data/cw_ally_recovery/phase1/index.html
sha256sum '/mnt/data/CW-WEB - Ally Recovery - Phase 0 Exact Baseline Candidate - 2026-09-02.html' /mnt/data/cw_ally_recovery/phase1/index.html
cmp -s '/mnt/data/CW-WEB - Ally Recovery - Phase 0 Exact Baseline Candidate - 2026-09-02.html' /mnt/data/cw_ally_recovery/phase1/index.html
```
Expected: both SHA values equal the frozen baseline hash and `cmp` exits 0.

- [ ] **Step 2: Inspect only the authorized macro targets before editing**

Extract exact HTML/text for: hero, `current-session`, `changed-since`, `where-now`, `shared-direction`, `collaboration-layer`, `emerged-since-call`, `stanley-update`, `agenda`, `people`, `three-paths`, `amazonas-application`, `alliance-architecture`, footer/title/meta and internal comments. Record every proposed string/node change in the manifest before patching.

- [ ] **Step 3: Write failing preservation/current-status tests**

The regression must fail on the untouched Phase 0 candidate for required public-state changes, and must independently assert all protected invariants: 27 details elements; identical ordered summary hash unless an explicitly authorized summary label changes; identical styles hash; identical external href sequence; identical image fingerprints; unchanged Canchis/legal section; Alliance matrix row/cell structure; untouched rows/cells hashes; major infographic geometry/style preserved; no new section order changes.

- [ ] **Step 4: Apply the minimum Phase 1 patch**

Patch only: top-level identity/status wording; Amazonas Sagrada and Maria Gracia status where represented; WGA role wording where stale; internal review/version/session wrappers; public `<title>`/meta/footer/comments. For wrapper sections, harvest useful content into its already-existing authoritative topic section before removing only the obsolete wrapper. Do not re-style, reorder, collapse, expand or redesign anything.

- [ ] **Step 5: Run targeted Phase 1 regression**

Run:
```bash
python /mnt/data/cw_ally_recovery/tools/verify_phase1.py \
  --baseline '/mnt/data/CW-WEB - Ally Recovery - Phase 0 Exact Baseline Candidate - 2026-09-02.html' \
  --candidate /mnt/data/cw_ally_recovery/phase1/index.html \
  --manifest /mnt/data/cw_ally_recovery/phase1/manifest.json
```
Expected: PASS with zero unauthorized mutations.

- [ ] **Step 6: Persist raw Phase 1 candidate and read back bytes**

Create an isolated Drive copy/updated descendant, upload the exact Phase 1 bytes, download/read back the raw file, compare SHA-256, and fail closed on mismatch.

- [ ] **Step 7: Persist Phase 1 manifest and checkpoint in GitHub**

Checkpoint must list exact changed sections/strings, preserved fingerprints, candidate Drive ID, byte size, SHA-256, and `PHASE1 = PASS` only after readback.

---

### Task 2: Section-by-section bounded adaptation

**Files:**
- Modify: `/mnt/data/cw_ally_recovery/phase2/index.html` copied exactly from the verified Phase 1 bytes.
- Create: `/mnt/data/cw_ally_recovery/phase2/delta-ledger.json`
- Create: `/mnt/data/cw_ally_recovery/tools/verify_section_delta.py`
- Persist: `docs-governance/validation/CW-WEB-ALLY-RECOVERY-PHASE2-2026-09-02.md`

**Interfaces:**
- Consumes: verified Phase 1 candidate.
- Produces: fully adapted ally-facing content while retaining the mature page architecture and all useful substantive material.

- [ ] **Step 1: Copy verified Phase 1 bytes to Phase 2 and prove identity**
- [ ] **Step 2: Traverse sections in existing DOM order**

For each section record exactly: `SECTION`, `CURRENT BLOCK HASH`, `AUTHORIZED CHANGE`, `REASON`, `CHECKLIST IDS`, `PROTECTED SUBSCOPE HASHES`, `TARGETED REGRESSION`.

- [ ] **Step 3: Patch only audience/status/internal-process language**

Preserve technical, legal, economic, territorial and research findings. Reframe meeting-specific language into durable ally-facing context. Keep WGA/Stanley technical possibilities, Amazonas Sagrada learnings, Patrick-derived technical options and finance hypotheses with their existing caveats/status; remove only obsolete meeting/process wrappers.

- [ ] **Step 4: Run per-section preservation tests after each bounded patch**

A changed section may differ only in manifest-listed nodes. Every unrelated section remains raw-hash identical to the preceding verified candidate until its own bounded turn.

- [ ] **Step 5: Run local redundancy and natural-language checks after each changed text block**

Flag nearby overuse of `connect`, `connecting`, `shared`, `pathway`, `architecture`, `opportunity`, `evidence`, repeated headings/CTAs and `X, not Y` identity formulas. Do not use the redundancy check as authorization to remove valid distinct content.

- [ ] **Step 6: Persist the verified full Phase 2 candidate and checkpoint**

Read back exact raw bytes, SHA-256 and delta ledger before closing Phase 2.

---

### Task 3: Global Definition-of-Done audit

**Files:**
- Read: verified Phase 2 HTML.
- Create: `/mnt/data/cw_ally_recovery/qa/final_audit.json`
- Create: `/mnt/data/cw_ally_recovery/tools/final_dod_audit.py`
- Persist: `docs-governance/validation/CW-WEB-ALLY-RECOVERY-FINAL-QA-2026-09-02.md`

**Interfaces:**
- Consumes: verified Phase 2 candidate and the full Definition of Done.
- Produces: checklist-level PASS/FAIL/NOT_APPLICABLE evidence.

- [ ] **Step 1: Scan ally-facing HTML for prohibited internal markers**

Reject REV/version/review/candidate/checkpoint/rollback/gate/progress/ChatGPT/OpenAI/AI-assisted/internal-session/development-note markers in title, metadata, visible copy, footer and comments, with contextual exceptions only for legitimate domain language.

- [ ] **Step 2: Reconcile current entity/status representation**

Verify Felipe, WGA, Amazonas Sagrada and Maria Gracia against the approved current-state rules without re-researching Canchis.

- [ ] **Step 3: Verify protected structures**

Compare details/nesting/default open state; matrix structure and unaffected cells; infographic unaffected geometry/styling; external href sequence; images/alt/source fingerprints; styles; section order; legal/Canchis content; precedents; River Economy; Observatory; Guardianship; deep-dive navigation.

- [ ] **Step 4: Run global redundancy/voice audit**

Produce term-frequency and nearby-heading/lead diagnostics plus a human editorial pass limited to changed copy.

- [ ] **Step 5: Run static integrity audit**

Require one H1, unique IDs, valid internal fragments, no missing local resources, useful image alt text, no loading/failure placeholders and no unexpected href changes.

- [ ] **Step 6: Mark every Definition-of-Done item PASS/FAIL/NOT_APPLICABLE with evidence**

No broad aggregate PASS may substitute for item-level evidence.

---

### Task 4: Browser QA and review artifact

**Files:**
- Read: exact verified final candidate.
- Create screenshots under `/mnt/data/cw_ally_recovery/qa/screenshots/`.
- Persist raw final review HTML in Drive and final review checkpoint in GitHub.

**Interfaces:**
- Consumes: final source-validated candidate.
- Produces: exact user-review candidate; no promotion.

- [ ] **Step 1: Render exact candidate at desktop and mobile widths**

Check overflow, text clipping, matrix readability, accordion operation/nesting, images, infographic, Alliance Architecture and first-screen context.

- [ ] **Step 2: Verify screenshots correspond to the candidate SHA-256**
- [ ] **Step 3: Prepare the exact review surface without semantic changes**

Use a verified zero-network in-chat delta/full Preview when practical; otherwise use the isolated verified review route only as review transport, never as promotion.

- [ ] **Step 4: Stop at explicit user approval gate**

Do not repoint main/release/production routes.

---

## Self-review

- Spec coverage: Tasks 1-4 cover preservation/current-state migration, section-level adaptation, A-R checklist validation, browser QA and final approval gate.
- Placeholder scan: no TBD/TODO/implement-later placeholders.
- Interface consistency: each task consumes only the exact verified output of the preceding task; raw HTML hashes and Drive IDs provide handoff identity.
- Scope discipline: no redesign, no Canchis research, no public promotion, no reconstruction from summaries or generated HTML.