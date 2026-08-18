# AI_OS transfer — Web Workstream Control improvements from Converging Waters

Status: READY_FOR_AI_OS_INSTALLATION
Date: 2026-08-18
Source workstream: Converging Waters website v16 incremental recovery
Owning system for the Skill: AI_OS

## Purpose

Capture reusable web-workflow improvements learned and behavior-tested in the Converging Waters Project without making Converging Waters the canonical home of the transversal Skill.

## Existing behavior preserved

- authoritative baseline lock;
- one authorized delta per subversion;
- deterministic preservation manifests;
- protected-section hashes/image/link counts;
- external href preservation during non-link deltas;
- zero-network ChatGPT HTML Preview after the network-permission-loop incident;
- downloadable HTML is not the ChatGPT visualizer;
- delta-slice approval gates;
- baseline/candidate rollback separation;
- final link/asset/responsive QA only after incremental content approval.

## New reusable improvement

Add two distinct review artifacts to controlled web workstreams:

1. `DELTA_SLICE_PREVIEW` — exact changed region plus adjacent context; this remains the approval surface.
2. `ROLLING_PROGRESS_PREVIEW` — exact cumulative state from the top of the page through the current review frontier, containing all approved deltas plus the current proposed delta.

Rules for the rolling progress preview:

- derive from the exact current candidate, never manually reconstruct from summaries;
- include protected blocks in full when they fall above the frontier;
- keep unreviewed downstream content in candidate source and hide it only in review transport;
- use transport-only CSS/navigation suppression when possible;
- if a full in-chat cumulative preview is impractically large, retain the small zero-network delta preview and use a verified static review route only when the user explicitly requests/authorizes a link;
- prefer one stable review-only route per workstream (for example `candidates/progress/`) and update it after each step;
- a progress route is never promotion, never the authoritative release/preview alias, and never proof that hidden downstream sections were reviewed;
- reuse a previously published asset base only when hashes match the current candidate;
- validate the progress route for version/frontier, protected blocks, asset/link invariants and hidden downstream boundary.

## New deterministic helper

`make_progress_preview.py`

Purpose: generate a rolling cumulative transport from an exact candidate through a named section frontier, optionally rewriting unchanged asset paths to a verified public asset base.

## Behavior evidence from Converging Waters

- ChatGPT zero-network delta Preview: behavior-tested successfully on the exact Project-chat surface.
- Stable cumulative review route created at `https://felipeacha.github.io/converging-waters/candidates/progress/` after explicit user request.
- Current route state: approved v16.1.1 + approved v16.2 + proposed v16.3; visual frontier `#thesis`.
- Stanley/WGA protected block in cumulative state: 13 images / 17 links.
- Full candidate: 46 external hrefs preserved.
- 16 published v16.1.1 assets match the current v16.3 candidate byte-for-byte.
- Pages deployment commit `6ed9c6f6559623383cedee3df29ed93706adb92c`, run `32158994079`: local validation, configure, upload, deploy and smoke all `success`.
- Pages artifact contains `./candidates/progress/index.html`.

## Packaged Skill update

Package filename: `skill.zip`
Package SHA-256: `c5fe9b1a1c8bf86c933eeeb42fc1da5c4820f291c39d8030693db2897d948999`
Package created and validated in the current ChatGPT execution environment.

This file is a transfer/handoff only. The installed/canonical transversal Skill remains owned by AI_OS and requires installation of the updated package in the Skill library or persistence in the AI_OS technical source when that surface is available.
