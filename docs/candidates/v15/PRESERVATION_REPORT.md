# Converging Waters v15 - Preservation-first deduplication report

## Result

- Baseline: exact recovered v13 source
- Baseline sections: **42**
- Candidate sections: **39**
- Removed standalone sections: **agenda, open-decisions, decision**
- Retained sections byte-identical: **PASS**
- Assets preserved byte-for-byte: **PASS (16/16)**
- Broken fragment links: **0**
- Missing local image assets: **0**
- HTML minification: **NO**

## Hard preservation lock - Stanley / WGA

The entire `stanley-update` section is copied from v13 without any byte-level change.

- Raw section SHA-256: `d22889e1b98d8f49d3ea09f74092e97273d06964852e19b20c0aebd26d5525e1`
- Images inside section: **13**
- Links inside section: **17**
- Result: **PASS_BYTE_IDENTICAL**

This preserves the full apparatus/reference area: sample + sequence; context + verify; learn + steward; portable field science; Sacred Valley possibility; design principle; ecosystem atlas/metagenome patterns; small field computers; sensor + metadata nodes; citizen science bioacoustics; autonomous field systems; portable sequencing in context; WGA public/data/academy/storytelling links; technical-next-step sequence; and clarification band.

## Why only three sections were removed

This recovery deliberately uses a much stricter interpretation of deduplication than the rejected v14 candidate. No substantive deep-dive section is consolidated or rewritten.

1. `agenda` - a second meta reading/agenda layer after `current-session`; removing it does not remove the actual current-session agenda or any technical/project section.
2. `open-decisions` - a short summary of unknowns already represented in the more detailed `validation`, `first-outcome`, `current-decision`, governance/data/territorial sections.
3. `decision` - a second closing decision block after the richer `current-decision`; the richer current decision remains unchanged.

Everything else remains in the same order and with identical HTML bytes, including `changed-since`, `where-now`, `shared-direction`, `collaboration-layer`, `emerged-since-call`, `stanley-update`, `three-paths`, Willkamayu, citizen science, purpose/MRV visuals, basin/system, convergence, Chelsea, Amazonas Sagrada, Patrick technical track, finance, allies, governance, guardians, tourism, legal, precedents, safeguards, budget, upside, roadmap, validation, current decision, open fronts and sources.

## Hashes

- Baseline HTML SHA-256: `fcb857aa61635a800f2faef512e9a14c3d53445ec996a03603ffa939dbd4ca11`
- Candidate HTML SHA-256: `cda4715f2891cf3e22787c5f449389c91ddf6ffef7c5b4e61ed2c18844474908`
