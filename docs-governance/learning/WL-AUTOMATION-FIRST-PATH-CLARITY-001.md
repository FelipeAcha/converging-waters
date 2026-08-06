# WL-AUTOMATION-FIRST-PATH-CLARITY-001

Status: `IMPLEMENTED`
Date: 2026-08-06
Coverage: `ROUTED_CHAT`
Primary class: `OUTPUT_PRIORITY_FAILURE`
Secondary classes: `MANUAL_STEP_NOT_TRACKED`, `SURFACE_AMBIGUITY`, `RESPONSE_BEFORE_EXECUTION`

## Failure

The assistant instructed Felipe to open a GitHub file as the immediate action even though the available GitHub connector could read and update the repository directly. The response also referred to governance without clearly explaining that the folder was `docs-governance/` at the repository root, not `docs/governance/` inside the GitHub Pages directory.

## Impact

- One unnecessary human action was delegated.
- The exact repository path was ambiguous.
- Felipe reasonably concluded that the governance material did not exist.
- The stated automation-first and post-execution response contract was not followed.

## Correction

- The repository was inspected directly.
- `GOVERNANCE.md` was added at the repository root.
- `docs-governance/README.md` was added as the directory index.
- The distinction between `docs/` and `docs-governance/` was documented.
- The requested technical-memory and Drive-governance work was executed before the next handoff.

## Prevention rule

Before assigning any repository-navigation action to Felipe:

1. use the available connector to read or write the exact file;
2. state the repository-relative path, not only a descriptive folder name;
3. distinguish publication roots from governance roots;
4. ask for human navigation only when the connector cannot perform the required action;
5. place the completed automation in `DELTA`, not in `ACCIÓN INMEDIATA`;
6. when a connector is unavailable, identify the blocker and provide only the smallest unavoidable human action.

## Regression

Given:

- a repository is connected;
- a requested file can be read or updated by connector;
- a similarly named publication directory exists;

Expected:

- the assistant executes the connector action first;
- the user is not asked to open the file merely to inspect it;
- the final response names the exact root-relative path;
- the response explicitly distinguishes `docs/` from `docs-governance/`;
- no completion claim is made for Drive writes when the Drive connector is unavailable.

## Evidence

- Root index commit: `b6c10eb6237145799ddda4d2aaf7b3a7e815328c`
- Governance index commit: `b867e20b066f40b45e309ec2112cac40eb534582`
- Technical-memory addendum commit: `6acf24c3dd08eae6222a6e7fcf79ac86ba7c0e1a`

Behavioral verification remains open until a future comparable request is handled without unnecessary user navigation.
