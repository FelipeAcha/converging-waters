# Converging Waters

Independent personal repository for the Converging Waters collaboration and the Willkamayu, Amazonas Sagrada and WGA exploratory work.

## Separation rule

This repository is owned under the personal GitHub account `FelipeAcha`. It is not a Norte Solar repository and must not use Norte Solar secrets, organizations, workflows, Drive folders, canonical records or infrastructure, except for generic cross-project standards explicitly approved and documented without Converging Waters project content.

## Repository areas

- Website publication files: [`docs/`](docs/)
- Governance and technical continuity: [`GOVERNANCE.md`](GOVERNANCE.md) and [`docs-governance/`](docs-governance/)

`docs/` is the GitHub Pages publication root. `docs-governance/` is a separate root-level governance directory.

## Website environments

- Review preview: `/preview/`
- Immutable reviewed release: `/releases/v13/`
- Production root: `/` — promoted only after explicit approval

## Publication model

GitHub Pages publishes from `main` → `/docs`. New iterations are added as immutable release folders, the preview pointer is updated, and production is promoted only after visual and automated validation.

The sole active publication workflow is:

`/.github/workflows/bootstrap-pages.yml`

Temporary import, probe and recovery workflows must be removed after an incident is resolved so there is only one deployment owner.

## Canonical operating references

- Governance index: [`GOVERNANCE.md`](GOVERNANCE.md)
- Project technical memory: [`docs-governance/PROJECT_TECHNICAL_MEMORY.md`](docs-governance/PROJECT_TECHNICAL_MEMORY.md)
- Technical-memory addendum — 2026-08-06: [`docs-governance/PROJECT_TECHNICAL_MEMORY_ADDENDUM_2026-08-06.md`](docs-governance/PROJECT_TECHNICAL_MEMORY_ADDENDUM_2026-08-06.md)
- Project gate control: [`docs-governance/PROJECT_GATE_CONTROL.md`](docs-governance/PROJECT_GATE_CONTROL.md)
- Current handoff: [`docs-governance/handoffs/2026-08-05/HANDOFF.md`](docs-governance/handoffs/2026-08-05/HANDOFF.md)
- Drive artifact versioning policy: [`docs-governance/standards/DRIVE_ARTIFACT_VERSIONING_POLICY.md`](docs-governance/standards/DRIVE_ARTIFACT_VERSIONING_POLICY.md)
- Fast path: [`docs-governance/standards/WEB_PREVIEW_PUBLISHING_FAST_PATH.md`](docs-governance/standards/WEB_PREVIEW_PUBLISHING_FAST_PATH.md)
- Verified learning record: [`docs-governance/learning/WL-WEB-PREVIEW-001.md`](docs-governance/learning/WL-WEB-PREVIEW-001.md)
- Deployment evidence: [`.github/pages-deployment-status.json`](.github/pages-deployment-status.json)

## Review URLs

- Preview: `https://felipeacha.github.io/converging-waters/preview/`
- Reviewed v13 release: `https://felipeacha.github.io/converging-waters/releases/v13/`
- Project gateway: `https://felipeacha.github.io/converging-waters/`
