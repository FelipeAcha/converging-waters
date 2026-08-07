# WL-WEB-PREVIEW-001 — Executable web preview and controlled publication

Status: VERIFIED FOR CONVERGING WATERS
Owner: Felipe
Recorded: 2026-08-04
Last material correction: 2026-08-07
Coverage tier: TOOL_OR_VALIDATOR
Telemetry status: PARTIAL — GitHub evidence available; n8n reliability persistence unavailable during this session

## Finding

A complete HTML website linked through `sandbox:` or stored as a file in Google Drive is not an executable web preview in ChatGPT. It is treated as source or a downloadable attachment. A reliable review experience requires a real HTTP(S) deployment.

A second failure mode is equally important: a technically reachable website is not necessarily the project's current website. When the current handoff, technical memory, artifact register, or version ledger already identifies the authoritative web artifact and deployment, those records have precedence over older URLs, reference sites, historical prototypes, or ad hoc rediscovery.

## Triggering incident

The reviewed website was initially presented as an HTML attachment and was described as visible in the conversation. The user correctly reported that the interface showed only code or a download option. Later, GitHub Pages URLs returned 404 because the repository-level Pages prerequisite had not yet been enabled. Several experimental workflows and trigger files were then created while isolating the failure.

On 2026-08-07, during a later review, the current Converging Waters handoff already identified the current web synthesis as `Converging_Waters_Final_Preview_v13.html` and GitHub as the authority for website source/deployment. After an embedded preview failure, the assistant incorrectly re-resolved “the current web” from an older Netlify reference and then produced a reconstructed visual that was not the authoritative current website. The user correctly rejected this. The underlying failure was authority drift, not merely a rendering failure.

## Primary classifications

- SURFACE_AMBIGUITY
- ASSUMED_COMPLETION
- LIFECYCLE_PREREQUISITE_MISSED
- MANUAL_STEP_NOT_TRACKED
- TOOL_CONTRACT_MISMATCH
- PREMATURE_CLOSURE
- RESPONSE_BEFORE_EXECUTION
- BASELINE_AUTHORITY_DRIFT
- SECONDARY_REFERENCE_OVERRIDE
- UNSUPPORTED_VISUAL_EQUIVALENCE

Secondary cost findings:

- EXCESSIVE_CAUTION_COST
- UNNECESSARY_REBUILD
- REPEATED_HUMAN_ACTION

## First control failures

1. A downloadable file was described as an interactive preview without exact-surface behavior evidence.
2. Notebook HTML rendering was treated as visible in the user interface without user-visible readback.
3. Individual public routes were diagnosed before confirming that GitHub Pages itself had been enabled.
4. Publication was described as complete before public HTTP and browser-render validation.
5. Recovery created multiple overlapping workflows instead of preserving one validated deployment path.
6. A later recovery path failed to re-read the authoritative handoff before resolving the phrase “current web”.
7. An older/reference URL was allowed to override the explicit current-artifact record.
8. A reconstructed visual was presented as useful evidence for the real website without proving visual equivalence.

## Authoritative baseline resolution rule

Before any web review, redundancy audit, preview, screenshot, edit, comparison, deployment, or publication action:

1. Read the current project handoff and the latest applicable technical-memory/gate record.
2. Resolve the current web artifact from the authoritative record, not from conversational recency, URL familiarity, search results, filenames found elsewhere, or historical references.
3. For Converging Waters, apply the authority split defined in canonical memory:
   - Google Drive: editable project artifacts, current exports, and version history;
   - GitHub: website source/deployment, technical governance, validators, hashes, releases, and reproducible evidence.
4. Treat older deployments, Netlify prototypes, historical pages, reference websites, and external examples as `REFERENCE_ONLY` unless the user explicitly promotes one of them to current authority.
5. If two sources appear to claim “current”, stop and reconcile them before doing any preview or content analysis.
6. Never silently substitute one website for another because the preferred preview route fails.
7. A failure to render the authoritative website changes the preview method, not the identity of the website being reviewed.
8. A generated or reconstructed image may be used only if it is explicitly labeled as a conceptual reconstruction. It must never be presented as a faithful screenshot or review baseline unless exact visual equivalence has been verified.

At the time of the 2026-08-07 incident, the authoritative handoff identified:

- web synthesis: `Converging_Waters_Final_Preview_v13.html`;
- repository: `FelipeAcha/converging-waters`;
- website source/deployment authority: GitHub;
- release family: v13.

These values are historical evidence of the incident. Future sessions must resolve the then-current values from the latest authoritative handoff/memory rather than hard-coding v13 forever.

## Corrected route

1. Resolve and lock the authoritative current web baseline before choosing a preview method.
2. Preserve the reviewed source.
3. Optimize images and other assets before publication when required.
4. Use the project's authorized deployment repository.
5. Maintain one active deployment workflow.
6. Separate production, preview and immutable releases.
7. Validate repository structure and package integrity.
8. Deploy or access the already-deployed authoritative release.
9. Verify public HTTP responses when the review surface depends on HTTP.
10. Render the authoritative release in a supported browser/headless environment and inspect expected content, images, links and error states.
11. Deliver the preview route only after readback succeeds.
12. If ChatGPT cannot faithfully render that authoritative release, state the limitation and switch review method without switching the underlying website.
13. Promote to production only after explicit approval.
14. Remove temporary workflows, triggers and diagnostics after recovery.

## Regression requirements

A future workflow must fail rather than claim completion when any of these conditions is unmet:

- the current handoff or technical-memory baseline was not checked before resolving “current web”;
- a reference or historical URL is about to replace the authoritative current artifact without explicit user approval;
- two sources conflict about which web artifact is current and the conflict has not been reconciled;
- a preview failure causes a different website or older deployment to be substituted silently;
- a generated/reconstructed image is labeled or implied to be a faithful screenshot without exact-equivalence evidence;
- GitHub Pages is required but not enabled;
- the expected HTML or release package is missing;
- the package hash or integrity test fails;
- required public routes do not return HTTP 200;
- the browser-rendered DOM lacks expected content markers;
- images have missing or invalid sources;
- the loader displays an error state;
- preview and production are not clearly distinguished;
- more than one workflow is actively responsible for deployment;
- an attachment link is labeled as an interactive preview without exact-surface verification.

## Verified evidence

- Repository: `FelipeAcha/converging-waters`
- Active deployment workflow: `.github/workflows/bootstrap-pages.yml`
- Deployment evidence: `.github/pages-deployment-status.json`
- Successful deployment run: `30950028830`
- Source commit tested: `4f86abb11b17c5d6f7b7666a890124a3edfaf7cf`
- Root: `https://felipeacha.github.io/converging-waters/`
- Preview: `https://felipeacha.github.io/converging-waters/preview/`
- Release recorded at the original validation event: `https://felipeacha.github.io/converging-waters/releases/v13/`
- Current-conversation handoff at the 2026-08-07 incident: `docs-governance/handoffs/2026-08-05/HANDOFF.md`
- Canonical authority split: `docs-governance/PROJECT_TECHNICAL_MEMORY_ADDENDUM_2026-08-06.md`, decisions CW-D020 through CW-D025.

The recorded deployment run passed local validation, GitHub Pages configuration, artifact upload, deployment and a headless-browser smoke test that checked expected content, image sources and link presence. The 2026-08-07 correction additionally verified that the handoff explicitly names `Converging_Waters_Final_Preview_v13.html` as the current web synthesis and that canonical memory assigns website source/deployment authority to GitHub.

## Durable prevention

The operating standard is maintained at:

`docs-governance/standards/WEB_PREVIEW_PUBLISHING_FAST_PATH.md`

The baseline-resolution rule in this learning record is mandatory for Converging Waters web work. It complements the publication fast path: the fast path controls how a verified website is previewed/published; this rule controls which website is allowed to be treated as current in the first place.

The generic cross-project lesson may be mirrored into Optimización Stack Digital / AI_OS as a reusable governance pattern, but Converging Waters content, identities, documents and deployment resources remain within Converging Waters.

## Revalidation triggers

Revalidate when:

- a new project handoff supersedes the current one;
- the authoritative current web artifact changes;
- the release family or deployment host changes;
- GitHub Pages or GitHub Actions changes materially;
- repository permissions, owner or visibility changes;
- a different hosting platform is explicitly promoted to current authority;
- the release format or loader changes;
- 30 days pass before a high-impact publication instruction;
- the user reports a different preview or deployment behavior;
- the user refers to “current”, “latest”, “the web”, or “the version we are working on” and more than one plausible candidate exists.
