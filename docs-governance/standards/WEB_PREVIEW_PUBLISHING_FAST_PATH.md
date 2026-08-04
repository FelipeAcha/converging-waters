# Web Preview and Publishing Fast Path

Status: ACTIVE
Owner: Felipe
Scope: Converging Waters personal repository
Last verified: 2026-08-04

## Purpose

Provide a repeatable, low-friction path for reviewing and publishing complete static websites without confusing downloadable HTML files with executable web previews.

## Separation boundary

This repository, its website, assets, workflows, GitHub Pages deployment and project records remain under Felipe's personal scope. They must not use Norte Solar repositories, secrets, Drive folders, service accounts, canonical project records or infrastructure.

A generic publishing lesson may be shared with Norte Solar only as a project-neutral standard. No Converging Waters content, project data, identities, documents or deployment resources move into Norte Solar.

## Core lesson

An HTML file attached through `sandbox:` or stored in Google Drive is a file for download or source inspection. It is not a reliable executable preview inside ChatGPT.

For any complete website or interactive HTML deliverable, the review surface must be a real HTTP(S) URL. The default preview route for this project is GitHub Pages.

## Fast path

1. **Freeze the reviewed source.** Preserve the current known-good HTML before changing publication infrastructure.
2. **Optimize assets before transport.** Extract large Base64 images, deduplicate repeated assets, preserve SVG, convert raster images to WebP where appropriate, add dimensions, lazy loading and asynchronous decoding.
3. **Use the independent repository.** Publish only from `FelipeAcha/converging-waters`.
4. **Keep three surfaces.**
   - Production gateway: `/`
   - Current review preview: `/preview/`
   - Immutable reviewed release: `/releases/<version>/`
5. **Activate GitHub Pages once.** In repository settings, use `Pages -> Build and deployment -> Source: GitHub Actions`. This one-time administrative prerequisite must be confirmed before diagnosing individual routes.
6. **Use one active deployment workflow.** `.github/workflows/bootstrap-pages.yml` is the sole active publishing workflow.
7. **Validate before claiming success.** Require repository checks, package integrity, HTTP 200 responses, headless-browser rendering, expected text markers, image presence and link presence.
8. **Review before promotion.** Update `/preview/`, obtain explicit approval, then promote the approved release to `/`.
9. **Preserve rollback.** Keep the prior immutable release and revert the preview or production pointer if the new release fails.

## Recommended repository structure

```text
/
├── README.md
├── converging-waters-repository-ready.zip
├── docs/
│   ├── index.html
│   ├── preview/index.html
│   └── releases/<version>/index.html
├── docs-governance/
│   ├── learning/
│   └── standards/
└── .github/
    ├── pages-deployment-status.json
    └── workflows/bootstrap-pages.yml
```

## Asset rules

- Avoid a monolithic HTML file with large Base64 raster images unless offline portability is the explicit requirement.
- Prefer relative asset files for normal web publication.
- Deduplicate identical images using hashes.
- Keep source-quality dimensions adequate for the displayed size; do not preserve unnecessarily large pixels.
- Use WebP for photographic raster assets and SVG for vector graphics.
- Add descriptive `alt` text.
- Add explicit `width` and `height` when practical.
- Use `loading="lazy"` below the fold and `decoding="async"`.
- Maintain an asset manifest with path, size and SHA-256 when releases are packaged.

## Acceptance criteria

A release is not considered publicly verified until all applicable checks pass:

### Repository and package

- required HTML files exist;
- ZIP or release package passes SHA-256 verification;
- package integrity test passes;
- no duplicate HTML IDs;
- internal anchors resolve;
- referenced local assets exist;
- external URLs are syntactically valid.

### Public deployment

- `/`, `/preview/` and the immutable release return HTTP 200;
- the public release renders in a real browser;
- expected content markers appear in the rendered DOM;
- images have non-empty, valid sources;
- the expected minimum number of images and links is present;
- the loader does not display an error state;
- desktop and mobile layouts do not introduce horizontal overflow;
- meaningful browser or JavaScript errors are absent.

## Retired failure patterns

Do not repeat these routes:

- presenting a `sandbox:` HTML link as an interactive preview;
- claiming notebook HTML output is embedded in the chat without visible confirmation;
- debugging `/preview/` before confirming GitHub Pages itself is enabled;
- creating several competing import and deployment workflows;
- treating workflow creation, CI start or file upload as proof of publication;
- claiming completion before HTTP and browser readback;
- asking Felipe to repeat manual tests that automation can perform;
- leaving diagnostic trigger files and obsolete workflows active after recovery.

## Future update recipe

For the next website version:

1. preserve the current release folder;
2. optimize and package the new version locally;
3. add it under `docs/releases/<new-version>/` or update the verified release loader/package;
4. point `docs/preview/index.html` to the new candidate;
5. run the single deployment workflow;
6. inspect `.github/pages-deployment-status.json`;
7. open the preview URL and perform the final visual review;
8. after explicit approval, update production `/`;
9. retain the previous release for rollback;
10. remove temporary triggers or diagnostics created during recovery.

## Current verified implementation

- Repository: `FelipeAcha/converging-waters`
- Active workflow: `.github/workflows/bootstrap-pages.yml`
- Preview: `https://felipeacha.github.io/converging-waters/preview/`
- Immutable release: `https://felipeacha.github.io/converging-waters/releases/v13/`
- Deployment evidence: `.github/pages-deployment-status.json`

The 2026-08-04 deployment passed local validation, GitHub Pages configuration, artifact upload, public deployment and headless-browser smoke testing.
