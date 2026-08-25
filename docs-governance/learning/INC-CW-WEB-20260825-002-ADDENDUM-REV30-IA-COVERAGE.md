# Incident addendum — REV30 final-IA coverage reconciliation

Parent incident: `INC-CW-WEB-20260825-002`  
Date: 2026-08-25  
Production: NOT_AUTHORIZED / unchanged

## F19 — partial hub review artifact was described as if it were the complete final one-page hub

**Failure:** REV30 descends from the `REV21 - Hub Close 04A-17` recovery line and contains the mid/late hub review surface (people insertion + Sections 05–17), but prior closure language described the hub as ~98–99% substantively complete without reconciling the exact artifact against the confirmed `CW-WEB-Final-IA-v0.2-2026-08-24.md` authority. The final IA requires a complete one-page narrative hub with 12 functional sections, including top-level orientation (`What Converging Waters is`, `Why these living waters`, `How we work`) and a final `Current Roadmap + Open Decisions` synthesis.

**Classification:** `ASSUMED_COMPLETION` + `INSUFFICIENT_EVIDENCE` + `PREMATURE_CLOSURE`.

**Impact:** understated remaining integration work and risked finalizing a partial review artifact as the whole hub.

**Corrective action:** treat REV30 as the authoritative stabilized mid/late hub component, not as the complete final hub. Reintegrate the exact approved early-hub source without reconstructing it, map existing stabilized content to the confirmed final IA, and add a concise final roadmap/next-steps synthesis while preserving existing open-decision/readiness/validation content.

**Preventive action:** before any future percentage-complete or release-ready claim, run an IA coverage reconciliation: every required final-IA functional section must map to an exact current DOM region or be explicitly OPEN. A review frontier label such as `04A-17` must never be silently treated as a complete page.

## F20 — stale review-version metadata inside otherwise current HTML artifacts

**Failure:** the REV30 hub `<title>` still identifies `REV29 · final QA anchor repair`; the River Economy REV2 cross-navigation file still carries a `Deep Dive REV1` document title. These are metadata/version-label drift, not content loss.

**Classification:** `PARALLEL_CHANGE_NOT_RECONCILED` + `INSUFFICIENT_EVIDENCE`.

**Impact:** confusing provenance during review and avoidable ambiguity when comparing files or browser tabs.

**Corrective action:** repair document-title/review metadata only in the next final-assembly candidate; do not change substantive content as part of that fix.

**Preventive action:** final candidate QA must assert that filename review label, checkpoint `review_label`, HTML `<title>`, bundle manifest, and displayed review banner identify the same candidate lineage.

## Verified current interpretation

- `CW-WEB-Final-IA-v0.2-2026-08-24.md` remains the confirmed-in-principle final information architecture authority.
- REV30 is a stabilized component source for the current mid/late hub, not the complete final one-page hub.
- Existing Sections 08–10 already contain much of the substantive next-step material (`What remains open`, `60–90 Day Readiness Package`, `What needs to be validated now`), but the final IA still calls for an end-of-hub synthesis: `Current Roadmap + Open Decisions — what is known, what remains open and what happens next`.
- Rights of Nature, Willkamayu River Observatory and River Economy exist as separate reviewable HTML pages; they are not equally mature. Rights is the most developed legal-learning surface; Observatory explicitly remains a design-and-content candidate pending evidence ingestion; River Economy remains an exploratory evidence-led framework pending validation/model depth.
