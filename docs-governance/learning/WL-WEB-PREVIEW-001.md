# WL-WEB-PREVIEW-001 — Executable web preview and controlled publication

Status: VERIFIED FOR CONVERGING WATERS
Owner: Felipe
Recorded: 2026-08-04
Coverage tier: TOOL_OR_VALIDATOR
Telemetry status: PARTIAL — GitHub evidence available; n8n reliability persistence unavailable during this session

## Finding

A complete HTML website linked through `sandbox:` or stored as a file in Google Drive is not an executable web preview in ChatGPT. It is treated as source or a downloadable attachment. A reliable review experience requires a real HTTP(S) deployment.

## Triggering incident

The reviewed website was initially presented as an HTML attachment and was described as visible in the conversation. The user correctly reported that the interface showed only code or a download option. Later, GitHub Pages URLs returned 404 because the repository-level Pages prerequisite had not yet been enabled. Several experimental workflows and trigger files were then created while isolating the failure.

## Primary classifications

- SURFACE_AMBIGUITY
- ASSUMED_COMPLETION
- LIFECYCLE_PREREQUISITE_MISSED
- MANUAL_STEP_NOT_TRACKED
- TOOL_CONTRACT_MISMATCH
- PREMATURE_CLOSURE
- RESPONSE_BEFORE_EXECUTION

Secondary cost findings:

- EXCESSIVE_CAUTION_COST
- UNNECESSARY_REBUILD

## First control failures

1. A downloadable file was described as an interactive preview without exact-surface behavior evidence.
2. Notebook HTML rendering was treated as visible in the user interface without user-visible readback.
3. Individual public routes were diagnosed before confirming that GitHub Pages itself had been enabled.
4. Publication was described as complete before public HTTP and browser-render validation.
5. Recovery created multiple overlapping workflows instead of preserving one validated deployment path.

## Corrected route

1. Preserve the reviewed source.
2. Optimize images and other assets before publication.
3. Use an independent repository owned by Felipe.
4. Activate GitHub Pages once with `Source: GitHub Actions`.
5. Maintain one active deployment workflow.
6. Separate production, preview and immutable releases.
7. Validate repository structure and package integrity.
8. Deploy.
9. Verify public HTTP responses.
10. Render the release in a headless browser and inspect expected content, images, links and error states.
11. Deliver the preview URL only after readback succeeds.
12. Promote to production only after explicit approval.
13. Remove temporary workflows, triggers and diagnostics after recovery.

## Regression requirements

A future workflow must fail rather than claim completion when any of these conditions is unmet:

- GitHub Pages is not enabled;
- the expected HTML or release package is missing;
- the package hash or integrity test fails;
- public routes do not return HTTP 200;
- the browser-rendered DOM lacks expected content markers;
- images have missing or invalid sources;
- the loader displays an error state;
- preview and production are not clearly distinguished;
- more than one workflow is actively responsible for deployment;
- an attachment link is labeled as an interactive preview.

## Verified evidence

- Repository: `FelipeAcha/converging-waters`
- Active deployment workflow: `.github/workflows/bootstrap-pages.yml`
- Deployment evidence: `.github/pages-deployment-status.json`
- Successful deployment run: `30950028830`
- Source commit tested: `4f86abb11b17c5d6f7b7666a890124a3edfaf7cf`
- Root: `https://felipeacha.github.io/converging-waters/`
- Preview: `https://felipeacha.github.io/converging-waters/preview/`
- Release: `https://felipeacha.github.io/converging-waters/releases/v13/`

The recorded run passed local validation, GitHub Pages configuration, artifact upload, deployment and a headless-browser smoke test that checked expected content, image sources and link presence.

## Durable prevention

The operating standard is maintained at:

`docs-governance/standards/WEB_PREVIEW_PUBLISHING_FAST_PATH.md`

The generic cross-project lesson may be mirrored into Norte Solar governance, but Converging Waters content, identities, documents and deployment resources remain outside Norte Solar.

## Revalidation triggers

Revalidate when:

- GitHub Pages or GitHub Actions changes materially;
- repository permissions, owner or visibility changes;
- a different hosting platform is used;
- the release format or loader changes;
- 30 days pass before a high-impact publication instruction;
- a user reports a different preview or deployment behavior.
