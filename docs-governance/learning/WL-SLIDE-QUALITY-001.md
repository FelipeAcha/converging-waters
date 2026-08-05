# WL-SLIDE-QUALITY-001 — Presentation readability and image integrity

Status: CONFIRMED
Coverage: Converging Waters presentation production
Owner: Project production workflow
Activated: 2026-08-05

## Trigger

Repeated user corrections identified two presentation-quality failures:

1. reference snapshots were inserted with crop behavior, causing important content to disappear in PPTX/PDF rendering;
2. multiple distinct ideas were placed as visually continuous paragraphs without bullets, numbering, or sufficient spacing, making slides difficult to scan.

Additional related risks were identified in tables and team-facing content.

## Root causes

- Image placement optimized for filling a frame rather than preserving the full source.
- Slide text was treated as document prose instead of presentation content.
- Quality assurance did not explicitly test PDF export and full-screen legibility before delivery.
- Table-cell padding was not treated as a global design requirement.
- Internal production lessons risked appearing in team-facing materials.

## Permanent prevention rules

### Images

- Default to `contain / fit`, never crop, for screenshots, diagrams, infographics, maps, and evidence images.
- Preserve aspect ratio.
- Use a neutral frame and internal margin.
- Complex graphics occupy a full slide when needed for legibility.
- When both overview and detail are required, use separate slides rather than silently cropping the overview.

### Text

- Every distinct idea in a slide content block must use bullets or numbering.
- Avoid hyphens as substitute bullets.
- Use clear visual separation between items: at least approximately 1.5 line spacing or an equivalent paragraph gap.
- Prefer 3–6 concise bullets per slide.
- Move supporting detail to the roadmap document or appendix rather than shrinking the font.

### Tables

- Apply internal horizontal and vertical cell padding globally.
- Align short content vertically centered and longer content at the top.
- Resize columns based on content.
- Reduce wording before reducing font size.
- Split dense tables across slides when readability requires it.

### Team-facing scope

- Exclude internal workflow, image-production, debugging, and private-conversation notes from the shared deck.
- Include only information useful to the team’s understanding, decisions, commitments, or next steps.

## Mandatory acceptance tests

Before any presentation is delivered:

1. Open the PPTX.
2. Export to PDF.
3. Inspect representative slides and every newly added slide at full-screen size.
4. Verify that all images are complete and uncropped.
5. Verify bullets or numbering for every multi-point text block.
6. Verify adequate item spacing.
7. Verify table padding and legibility.
8. Verify no text overflow, clipping, missing images, broken links, or unexpectedly small text.
9. Verify Google Slides import compatibility through standards-compatible PPTX construction.
10. Confirm that internal production notes are absent from the team-facing content.

## Regression rule

A slide package cannot be marked complete solely because the source file was generated. Completion requires successful PPTX opening, PDF export, visual inspection, and preserved-behavior checks against previously approved slides.

## Rollback

If a new slide fails visual QA:

- freeze only the affected slide or new insertion;
- preserve unrelated approved slides;
- correct the specific image/text/table component;
- rerun targeted PPTX/PDF validation;
- do not rebuild the full deck unless corruption cannot be localized.
