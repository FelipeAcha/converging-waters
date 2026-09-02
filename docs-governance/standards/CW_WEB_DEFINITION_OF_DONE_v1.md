# Converging Waters Web — Definition of Done v1

**Status:** APPROVED DESIGN CONTRACT WITH CURRENT CORRECTIONS  
**Date:** 2026-09-02  
**Scope:** Converging Waters ally-facing one-page hub and its deep-dive navigation  
**Implementation posture:** preserve-first, minimum necessary mutation, incremental execution

## 0. Governing rule

The existing mature hub is the implementation baseline. Do not regenerate, rewrite, reconstruct, or redesign the HTML from scratch.

Execution order:

`KEEP -> UPDATE ONLY WHAT CHANGED -> REFRAME ONLY WHAT THE NEW AUDIENCE REQUIRES -> REMOVE ONLY PURE INTERNAL/DEVELOPMENT WRAPPERS AFTER HARVESTING ALL USEFUL INFORMATION`

Default action for every existing element is `KEEP`.

Every change must identify:
- the exact existing block being changed;
- the reason it must change;
- the checklist requirement it satisfies;
- the exact protected scope that must remain unchanged;
- the targeted regression used to prove preservation.

Any unlisted mutation is a failure.

## 1. Baseline and source preservation

- Source implementation baseline: `CW-WEB-v16.9 - REV33 - Localized Precedent Images + Immutable Release QA - 2026-08-25 - REVIEW.html`.
- Drive file ID: `1jAN0Ic9J-fW_EKfQKJO_2vm9bS-JUSSt`.
- The baseline must be copied byte-for-byte into a separate candidate before patching. Copying is allowed; regeneration is prohibited.
- The source baseline itself remains immutable.
- REV02 may contribute QA infrastructure and responsive fixes only where they can be applied without destructive redesign. Its editorial direction is not the content baseline.
- The historical snapshot remains immutable rollback evidence.

## 2. Hard preservation rules

1. `DEFAULT_CONTENT_ACTION = KEEP`.
2. Existing DOM, text, order, colors, components, accordion structures, diagrams, tables/matrices, images, links and semantic chips remain unchanged unless a specific requirement below authorizes a mutation.
3. Preservation is stronger than general UX optimization. Readability preferences do not authorize refactoring a working block.
4. No section is removed merely because similar content exists elsewhere.
5. No content is moved to another surface merely because a deep dive exists.
6. No previously approved component is redesigned for stylistic novelty.
7. Every removal must first harvest and rehome all useful ally-facing information.
8. Existing external hrefs remain byte-identical unless an explicit link update is required.
9. Existing visual identity is protected unless a factual, legal, accessibility or verified rendering defect requires a bounded change.
10. Canchis/legal evidence is not re-researched in the current recovery cycle. Preserve current verified material unless a later explicit trigger requires revalidation.

# DEFINITION OF DONE CHECKLIST

## A. Audience and purpose

- [ ] A01. Primary audience is potential allies and collaborators.
- [ ] A02. The site informs, contextualizes, demonstrates substance and opens collaboration; it is not a sales funnel.
- [ ] A03. A reader with no prior knowledge of Peru, Cusco, Canchis, Willkamayu or the institutions can understand the page.
- [ ] A04. Local places, institutions and acronyms receive context on first meaningful use where necessary.
- [ ] A05. The page explains territory, purpose, evidence, work already developed, active lines of work, capabilities, possible allies and paths to deeper material.
- [ ] A06. Territory and the living river system remain central to the narrative.
- [ ] A07. Collaboration is grounded in demonstrated work, evidence and opportunities rather than marketing claims.

## B. Voice and language

- [ ] B01. Human, natural, context-specific English.
- [ ] B02. Primarily affirmative framing: say directly what Converging Waters seeks to understand, protect, regenerate, measure, enable or strengthen.
- [ ] B03. Avoid repetitive artificial formulas such as `X, not Y`, `do not X`, `rather than X` when describing identity or purpose.
- [ ] B04. Negative constructions remain allowed where needed for scientific, legal, ethical or factual precision.
- [ ] B05. No hype, sales language, urgency marketing or inflated claims.
- [ ] B06. No empty slogans.
- [ ] B07. Use precise verbs appropriate to the subject; avoid dependence on a small set of generic verbs.
- [ ] B08. No literal-translation or generic corporate-English feel.
- [ ] B09. Visible copy is concise where possible without sacrificing substance.
- [ ] B10. Avoid unnecessary meta-language explaining the page itself.

## C. Redundancy control

- [ ] C01. Audit lexical repetition in nearby headings, leads, labels and CTAs.
- [ ] C02. Do not overuse `connect`, `connecting`, `shared`, `pathway`, `architecture`, `opportunity`, `evidence` or any other dominant term.
- [ ] C03. Consecutive headings must perform distinct semantic jobs.
- [ ] C04. Repeated propositions are retained only when they serve different narrative functions or add material evidence, scope, status, audience, timing or implication.
- [ ] C05. Avoid visually monotonous repetition of identical card patterns when the existing baseline already provides a richer grammar.
- [ ] C06. Avoid repetitive generic CTAs.
- [ ] C07. Legitimate purposeful repetition is preserved.
- [ ] C08. Every substantive topic keeps an authoritative home.
- [ ] C09. Every candidate receives a global headings/leads/propositions redundancy audit.
- [ ] C10. Final human-language pass checks rhythm and repetition beyond deterministic lint.

## D. Minimum-mutation preservation

- [ ] D01. Mature hub is the protected source implementation baseline.
- [ ] D02. Default action is KEEP.
- [ ] D03. MODIFY requires an explicit cause.
- [ ] D04. REMOVE is exceptional.
- [ ] D05. Useful information is harvested before any wrapper is removed.
- [ ] D06. Audience change normally means minimum reframing, not deletion.
- [ ] D07. Status change means status update, not component reconstruction.
- [ ] D08. A changed participant relationship does not erase prior useful findings.
- [ ] D09. Useful findings remain even when the person or organization that surfaced them changes role.
- [ ] D10. Approved visual components remain unless a specific defect or factual change requires mutation.
- [ ] D11. Existing links are preserved unless explicit update is necessary.
- [ ] D12. Existing palette is preserved.
- [ ] D13. Existing semantic chip system is preserved.
- [ ] D14. Existing mature cards, diagrams and layout grammar are preserved.
- [ ] D15. Each changed block is tracked in a migration/preservation manifest.
- [ ] D16. Every element outside the authorized delta must remain unchanged.
- [ ] D17. No section already developed is reinterpreted from zero.
- [ ] D18. No restructuring for novelty or aesthetics alone.

## E. Information architecture

- [ ] E01. Preserve the one-page narrative hub plus specialist deep dives architecture.
- [ ] E02. Homepage remains useful and substantial by itself.
- [ ] E03. Deep dives add specialist depth; they do not justify emptying the homepage.
- [ ] E04. Legal / Rights remains substantially represented on the homepage.
- [ ] E05. Evidence / Observatory remains substantially represented on the homepage.
- [ ] E06. River Economy remains substantially represented on the homepage.
- [ ] E07. Alliance Architecture remains substantially represented on the homepage.
- [ ] E08. Precedents & Lessons remains substantially represented and visual on the homepage.
- [ ] E09. Deep dives own exhaustive sources, datasets, methods, modeling and specialist records where appropriate.
- [ ] E10. Navigation uses reader-facing concepts, not internal development labels.
- [ ] E11. Page can be followed coherently from beginning to end.
- [ ] E12. Existing overall section architecture is preserved unless a bounded change is explicitly approved.

## F. Progressive disclosure / accordions — PRESERVE EXISTING IMPLEMENTATION

- [ ] F01. Do not redesign or restructure the current progressive-disclosure system in the recovery pass.
- [ ] F02. Existing accordions and disclosure nesting remain exactly as implemented unless a specific defect is later identified.
- [ ] F03. Nested accordions are explicitly allowed and must not be removed merely because they are nested.
- [ ] F04. A separate visible conclusion/summary is NOT mandatory when the title/heading itself adequately communicates the main point.
- [ ] F05. Add a separate visible summary only when necessary for comprehension; do not add one mechanically to every block.
- [ ] F06. Existing accordion titles, hierarchy, open/closed behavior, styling and navigation remain protected unless a later explicit change is approved.
- [ ] F07. Legal detail may remain in nested/structured accordions on the homepage as already developed.
- [ ] F08. Evidence, source notes, matrices and technical detail may retain the disclosure organization already present.
- [ ] F09. Existing keyboard/accessibility behavior must not regress.
- [ ] F10. Any future redesign of accordions is a separate later gate, not part of the current recovery.

## G. Visual identity and approved components

- [ ] G01. Preserve the existing palette.
- [ ] G02. Preserve green / teal / gold and the established mint / blue / yellow / clay / rose semantic families.
- [ ] G03. Preserve domain-chip color semantics.
- [ ] G04. Color is not the sole information carrier.
- [ ] G05. Preserve established typography and visual hierarchy unless a verified defect requires a bounded fix.
- [ ] G06. Preserve mature card designs.
- [ ] G07. Preserve established semantic iconography.
- [ ] G08. Preserve useful diagrams and flows.
- [ ] G09. Preserve existing documentary/territorial imagery where it still serves the content.
- [ ] G10. Avoid stock/marketing aesthetics.
- [ ] G11. Preserve existing emphasis conventions unless they create a verified accessibility issue.
- [ ] G12. Preserve spacing/visual rhythm unless a verified responsive defect requires correction.
- [ ] G13. Preserve the existing major infographic essentially unchanged.
- [ ] G14. If Amazonas Sagrada appears as a protagonist/core node in that infographic, remove/downgrade only that representation; preserve the rest of the infographic.

## H. Alliance Architecture — protected block

- [ ] H01. Preserve the full section.
- [ ] H02. Preserve layout.
- [ ] H03. Preserve colors.
- [ ] H04. Preserve format.
- [ ] H05. Preserve semantic chips.
- [ ] H06. Preserve matrix organization.
- [ ] H07. Preserve column structure and established width priorities.
- [ ] H08. Preserve all still-relevant actors.
- [ ] H09. Do not reinvent relationships already mapped without new evidence.
- [ ] H10. Update only factual relationship/status changes and explicitly authorized wording corrections.
- [ ] H11. WGA reflects the current scientific-technical convergence relationship.
- [ ] H12. Amazonas Sagrada is represented as a potential ally, not a core/protagonist initiative.
- [ ] H13. Maria Gracia is represented as a potential ally rather than current co-author/core project lead.
- [ ] H14. Felipe retains current project direction where identity/leadership is shown.
- [ ] H15. Interest is never inflated into commitment.
- [ ] H16. Personal relationship is never inflated into institutional authority.
- [ ] H17. Preserve the large alliance matrix.
- [ ] H18. Preserve its existing responsive/mobile treatment unless a verified defect requires correction.
- [ ] H19. All unchanged cells/rows are preserved exactly.

## I. People, organizations and capabilities

- [ ] I01. Keep person and organization distinct.
- [ ] I02. Keep capability and commitment distinct.
- [ ] I03. Keep expertise and authority distinct.
- [ ] I04. Preserve useful capability intelligence already identified.
- [ ] I05. Update only current relationship representation when it has changed.
- [ ] I06. Former/core participants may remain as potential allies or capability sources where relevant.
- [ ] I07. Do not attribute positions to communities, Indigenous organizations or institutions without confirmed authority.
- [ ] I08. Preserve existing people/capability visual components unless a status update requires a bounded copy change.

## J. WGA / Stanley / technical possibilities

- [ ] J01. Preserve portable eDNA material.
- [ ] J02. Preserve metagenomic-observation material.
- [ ] J03. Preserve environmental-sampling material.
- [ ] J04. Preserve sensor possibilities.
- [ ] J05. Preserve GPS/time/environmental metadata concepts.
- [ ] J06. Preserve field-node concepts.
- [ ] J07. Preserve traceable-provenance concepts.
- [ ] J08. Preserve Raspberry Pi / Jetson-style field-compute possibilities where already documented.
- [ ] J09. Preserve bioacoustics material.
- [ ] J10. Preserve federated environmental-data / atlas concepts.
- [ ] J11. Preserve data-stewardship concepts.
- [ ] J12. Preserve community/citizen-science possibilities.
- [ ] J13. Preserve useful WGA images/references already integrated.
- [ ] J14. Remove only meeting/changelog/internal-development wrappers around this material.
- [ ] J15. Reframe durable content as scientific/technical possibilities relevant to Observatory, citizen science and monitoring.
- [ ] J16. Potential technologies must not be presented as confirmed deployments.
- [ ] J17. Unverified options retain their validation status/caveats.

## K. Amazonas Sagrada

- [ ] K01. Represent Amazonas Sagrada as a potential ally in the current state.
- [ ] K02. Do not present it as a current core/protagonist territory equivalent to Willkamayu in project identity.
- [ ] K03. Preserve useful regenerative-enterprise insights.
- [ ] K04. Preserve useful conservation/livelihood relationships and learning.
- [ ] K05. Preserve traceability concepts.
- [ ] K06. Preserve useful water/sanitation possibilities.
- [ ] K07. Preserve cross-territorial learning possibilities.
- [ ] K08. Preserve relevant capabilities already identified.
- [ ] K09. Change commitment language to potential-collaboration language only where current status requires it.
- [ ] K10. Preserve initiative autonomy.
- [ ] K11. Do not attribute current commitments without authority.

## L. Legal / Rights / Guardianship

- [ ] L01. Preserve current Canchis content in this recovery cycle; no new Canchis research now.
- [ ] L02. Preserve existing municipal / regional / national-administrative / judicial route architecture.
- [ ] L03. Preserve LAW / EVIDENCE / PEOPLE / IMPLEMENTATION logic.
- [ ] L04. Preserve combined protection architecture.
- [ ] L05. Preserve citizen science + MRV relationship to implementable protection.
- [ ] L06. Preserve community participation.
- [ ] L07. Preserve guardians / stewards distinctions.
- [ ] L08. Preserve restoration / sanitation / accountability relationships.
- [ ] L09. Preserve existing legal accordions and nesting.
- [ ] L10. Preserve source-trail disclosure.
- [ ] L11. Preserve Marañon / Titicaca comparator context already validated.
- [ ] L12. Preserve legal precision and status distinctions.
- [ ] L13. Deep dive adds legal record depth; it does not replace substantial homepage legal content.
- [ ] L14. Update a legal fact only when an explicit later evidence trigger warrants it.

## M. Evidence / Observatory / citizen science

- [ ] M01. Preserve evidence-status distinctions already used in the hub.
- [ ] M02. Do not turn correlation into causality.
- [ ] M03. Preserve source-attribution questions.
- [ ] M04. Preserve river-system perspective.
- [ ] M05. Preserve main-stem + tributary logic.
- [ ] M06. Preserve Huatanay context where it explains a real system issue.
- [ ] M07. Preserve sanitation / PTAR context where relevant.
- [ ] M08. Preserve monitoring architecture.
- [ ] M09. Preserve QA/QC logic.
- [ ] M10. Preserve school-network / citizen-science work.
- [ ] M11. Preserve WGA fit without overstating it.
- [ ] M12. Preserve evidence/source-trail links that remain valid.

## N. River Economy / financing / tourism

- [ ] N01. Preserve River Economy thesis.
- [ ] N02. Preserve livelihoods.
- [ ] N03. Preserve agriculture/water-use context where already relevant.
- [ ] N04. Preserve tourism/recreation potential.
- [ ] N05. Preserve visitor-contribution mechanisms with correct evidence/status framing.
- [ ] N06. Preserve restoration-sponsorship concepts.
- [ ] N07. Preserve water-responsibility concepts.
- [ ] N08. Preserve avoided-cost / value-at-risk framing.
- [ ] N09. Preserve anti-greenwashing safeguards.
- [ ] N10. Do not turn the section into an investment pitch.

## O. Precedents & Lessons

- [ ] O01. Preserve visual precedent section.
- [ ] O02. Preserve Peru-first ordering.
- [ ] O03. Preserve Marañon lesson.
- [ ] O04. Preserve Titicaca lesson.
- [ ] O05. Preserve stingless-bees precedent where present.
- [ ] O06. Preserve Whanganui lesson.
- [ ] O07. Preserve Atrato lesson.
- [ ] O08. Preserve approved precedent images/illustrations.
- [ ] O09. Avoid duplicating the entire Legal section.
- [ ] O10. Legal deep dive retains the more complete precedent record.

## P. Zero internal development material in ally-facing artifact

- [ ] P01. No REV labels.
- [ ] P02. No internal version numbers.
- [ ] P03. No candidate/review labels.
- [ ] P04. No baseline/checkpoint language.
- [ ] P05. No rollback/gate language.
- [ ] P06. No progress notes.
- [ ] P07. No changelog wrappers such as `what changed since...`.
- [ ] P08. No internal-session instructions.
- [ ] P09. No ChatGPT references.
- [ ] P10. No OpenAI references.
- [ ] P11. No AI-assisted drafting/process disclosure in the ally-facing page.
- [ ] P12. No internal development comments in the distributed HTML.
- [ ] P13. Clean external-facing `<title>`.
- [ ] P14. Clean external-facing meta description.
- [ ] P15. External-facing footer only.
- [ ] P16. No QA/internal technical routes exposed as public content.

## Q. UX / responsive / accessibility preservation

- [ ] Q01. One visible H1.
- [ ] Q02. Coherent heading hierarchy.
- [ ] Q03. No desktop horizontal overflow.
- [ ] Q04. No mobile horizontal overflow.
- [ ] Q05. Matrices remain legible.
- [ ] Q06. Preserve existing mobile matrix/card transformation where it works.
- [ ] Q07. Entity names remain readable.
- [ ] Q08. Links work.
- [ ] Q09. Same-page fragments resolve.
- [ ] Q10. Content images have useful alt text.
- [ ] Q11. Images load correctly.
- [ ] Q12. Existing accordion accessibility does not regress.
- [ ] Q13. Existing nested accordions are allowed and protected.
- [ ] Q14. No loading/failure placeholders remain.
- [ ] Q15. First screen gives enough context to know the territory/initiative and why the work matters, without forcing a specific slogan template.
- [ ] Q16. Mobile preserves information priority, not only layout.
- [ ] Q17. Density is managed primarily through the existing proven disclosure architecture, not by deleting useful content.

## R. Acceptance and validation

- [ ] R01. All applicable checklist items PASS or have an explicit user-approved exception.
- [ ] R02. Preservation manifest is complete.
- [ ] R03. Every mutation is linked to a stated reason/checklist requirement.
- [ ] R04. Every removed wrapper proves that useful information was first preserved/re-homed.
- [ ] R05. Redundancy audit passes.
- [ ] R06. Affirmative/natural-language audit passes.
- [ ] R07. Internal-language scan returns zero prohibited public markers.
- [ ] R08. Current-authority/status audit passes for the entities being changed.
- [ ] R09. Link validation passes.
- [ ] R10. Technical/browser ACB passes.
- [ ] R11. Desktop visual QA passes.
- [ ] R12. Mobile visual QA passes.
- [ ] R13. Screenshots correspond to the exact candidate hash.
- [ ] R14. Candidate is compared against the immutable source baseline.
- [ ] R15. Alliance Architecture has no unauthorized regression.
- [ ] R16. Previously approved information/components have no unauthorized regression.
- [ ] R17. Final preview is delivered before any promotion.

# MIGRATION POLICY

## Protected / minimal-change map

| Existing hub block | Treatment | Authorized current mutation | Protected scope |
|---|---|---|---|
| Hero / opening thesis | MODIFY_MINIMALLY | Remove internal review/version language; update current identity; replace artificial/negative framing only where needed | Overall visual system, existing composition and useful imagery |
| Core thesis | MODIFY_MINIMALLY | Update only assumptions tied to the old core-participant structure and current audience | All still-valid reasoning and content |
| Willkamayu | KEEP | Status/context correction only if strictly needed | Existing ecological/cultural/economic/institutional structure, visuals, colors, icons |
| Major infographic | PROTECTED | If Amazonas Sagrada is shown as a core/protagonist node, downgrade/remove only that node; apply any necessary Maria Gracia status change only if represented there | All remaining geometry, colors, labels, structure and styling |
| People map | STATUS_UPDATE_ONLY | Felipe current direction; Maria Gracia potential ally; Amazonas Sagrada potential ally; other status changes only where already authorized | Existing capabilities, cards, visual grammar |
| WGA / Stanley technical material | REFRAME_WRAPPER_ONLY | Remove meeting/changelog framing; present durable technical possibilities with existing caveats | Technologies, images, references, technical detail |
| Collaboration framework | KEEP | Only remove internal meeting/draft wording where present | Loop, citizen-science logic, evidence-to-action logic, diagrams, stewardship principles |
| Evidence / Observatory | KEEP | Remove internal ownership/revision markers and update status only if necessary | Monitoring architecture, QA/QC, diagrams, river-system reasoning, Huatanay context |
| Evidence -> implementation | KEEP | Internal-wrapper/status correction only | Existing flow and implementation logic |
| People + Guardians + Stewardship | KEEP | Current status/attribution changes only if necessary | Existing stewardship, participation, education, guardianship structure and disclosure |
| Roadmap / open decisions | REFRAME_WRAPPER_ONLY | Convert obsolete meeting/date framing into durable current questions/priorities while preserving substance | Questions, dependencies, safeguards, readiness criteria, evidence gaps |
| Amazonas Sagrada application | DOWNGRADE_STATUS_ONLY | Core/current framing -> potential ally/cross-territorial learning where necessary | Useful regenerative-enterprise, traceability, livelihood, water/sanitation and capability material |
| Technical options | KEEP_WITH_STATUS | Remove person/meeting wrapper only if it no longer fits audience; maintain provenance when useful | Technical options and validation safeguards |
| Finance hypotheses | REFRAME_WRAPPER_ONLY | Remove meeting/funding-pitch framing | Existing financing distinctions, safeguards and hypotheses |
| Alliance Architecture | PROTECTED | Only current factual status changes: Amazonas Sagrada -> potential ally; Maria Gracia -> potential ally; other evidenced status changes | Layout, colors, format, chips, matrix structure, widths, unaffected rows/cells, responsive behavior |
| Legal Protection Architecture | PROTECTED | Remove internal wrapper/labels only; no current Canchis re-research | Current legal content, diagrams, accordions, nesting, route logic, sources |
| Precedents & Lessons | KEEP | Internal review-marker cleanup only | Existing cases, images, Peru-first order and differentiated lessons |
| River Economy | KEEP | Internal-wrapper/status correction only | Existing thesis, scenarios, livelihoods/tourism framing and safeguards |
| Deep-dive navigation | KEEP | Current labels only if required | Architecture and navigation logic |
| Current-session / changed-since / agenda / emerged-since-call wrappers | HARVEST_THEN_REMOVE_WRAPPER | Rehome every useful finding into its existing authoritative section; remove only the time-bound/internal wrapper | All substantive ally-relevant content |
| Footer | MODIFY_MINIMALLY | Remove internal review/version/AI/process content and replace with simple external-facing footer text | Existing styling if it remains suitable |
| HTML development comments/review markers | REMOVE_FROM_PUBLIC_ARTIFACT | Strip internal-only markers from candidate output | Preserve equivalent governance evidence outside public HTML |

# INCREMENTAL EXECUTION PLAN

## Principle

Work from coarse structure to fine section edits while keeping the entire original page present for context. Do not rebuild a new page section-by-section.

### Phase 0 — Freeze and prove the baseline

1. Obtain the exact source HTML bytes from the mature hub.
2. Compute and persist source hash.
3. Copy the source byte-for-byte to a new isolated candidate path.
4. Verify candidate hash equals source hash before any patch.
5. Build the first preservation manifest.
6. Record all protected blocks, accordion/disclosure markers, images, links, Alliance Architecture/matrix, infographic and section order.

**Acceptance:** candidate is an exact copy; zero semantic/layout change.

### Phase 1 — Coarse structural/current-reality pass

Perform only the changes required to make the overall existing hub suitable as the new ally-facing base while preserving its complete structure:

1. remove/replace internal review/version/session wrappers without deleting substantive information;
2. update top-level identity/current relationship framing only where necessary;
3. apply current status downgrade of Amazonas Sagrada -> potential ally;
4. apply current status downgrade of Maria Gracia -> potential ally;
5. preserve WGA current role accurately;
6. preserve the major infographic; only remove/downgrade Amazonas Sagrada there if it is actually present as a core/protagonist node;
7. preserve Alliance Architecture layout/matrix and modify only authorized status cells;
8. preserve all accordions, including nested accordions, exactly as implemented;
9. preserve the remainder of the page untouched.

**Acceptance:** macro page still looks and behaves like the mature hub; only current-reality/internal-wrapper differences are visible.

### Phase 2 — Section-by-section bounded adaptation

Proceed in the existing page order. Before touching each section, create an internal delta record:

`SECTION | CURRENT BLOCK | AUTHORIZED CHANGE | REASON | CHECKLIST IDS | PROTECTED SUBSCOPE | TARGETED REGRESSION`

For each section:
1. inspect exact current block;
2. identify only wording/status/internal-wrapper changes required by this specification;
3. patch those exact nodes/strings;
4. leave all other DOM and styling intact;
5. run targeted preservation diff;
6. run redundancy/natural-language check on the changed text in context;
7. render in the full-page context;
8. close the internal section gate only when preservation and acceptance checks pass;
9. continue to the next section autonomously unless an evidence conflict, material scope expansion or genuine user decision is encountered.

Priority order follows the existing hub, not a newly invented architecture.

### Phase 3 — Global editorial/technical reconciliation

After all bounded section patches:

1. global redundancy audit;
2. affirmative/natural-language audit;
3. prohibited internal-language scan;
4. entity/status consistency audit;
5. preservation manifest reconciliation;
6. external-href preservation check;
7. accordion/disclosure structure comparison;
8. Alliance Architecture/matrix regression;
9. infographic regression;
10. desktop/mobile browser QA;
11. ACB hard gates;
12. exact-hash screenshots.

### Phase 4 — Final review gate

Deliver the exact cumulative candidate for user review before promotion.

No promotion to main/public authoritative route without explicit user approval.

# AUTONOMY RULE

Within this frozen specification, routine bounded changes are pre-authorized for autonomous execution. Do not interrupt the user for micro-approvals.

Stop only when:
- a requested change conflicts with this specification;
- the exact baseline cannot be recovered;
- a factual/status contradiction cannot be resolved from current authority;
- a proposed mutation would affect a protected block beyond the authorized exception;
- a legal/scientific claim requires new external research beyond the current authorized recovery scope;
- promotion/publication approval is required.

# REVIEW REPORT FORMAT

Every substantial candidate review must report:

1. `CHECKLIST PASS / FAIL / NOT YET TESTED`;
2. exact changed blocks;
3. exact protected blocks verified unchanged;
4. redundancy findings;
5. internal-language findings;
6. remaining open items;
7. next committed gate;
8. rollback/source hash.

# CURRENT EXPLICIT FREEZES

- Progressive disclosure: **NO CHANGE** in the current recovery pass.
- Nested accordions: **ALLOWED AND PROTECTED**.
- Separate always-visible conclusion: **NOT REQUIRED** when the heading/title already communicates the point.
- Major infographic: **PRESERVE**, with only bounded current-status change if Amazonas Sagrada (and where applicable Maria Gracia) is represented inconsistently with current reality.
- Alliance Architecture: **PRESERVE**, status updates only.
- Canchis evidence: **NO RE-RESEARCH NOW**.
- Source code strategy: **PATCH EXISTING HTML; NEVER REGENERATE**.
