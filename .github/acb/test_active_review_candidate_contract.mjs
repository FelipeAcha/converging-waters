import assert from 'node:assert/strict';
import { parseState, validateSnapshot } from './active_review_candidate_contract.mjs';

const state = parseState(`REVISION_NAME=CW-ALLY-REV06 — Narrative Clarity + Clean Numbering
SOURCE_HUB_SHA256=c61e9f1a4157d84d3cd1c07b690c6d35aeae204a88a7f6281c79e7c07af3d6da
REVIEW_ROUTE=candidates/progress/cw-ally-rev06-narrative-clarity-clean-numbering.html
ACTIVE_QA_EXPECTED_ACCORDIONS=23
ACTIVE_QA_EXPECTED_DETAILS=27
ACTIVE_QA_EXPECTED_IMAGES=13
ACTIVE_QA_EXPECTED_ALLIANCE_ROWS=49
ACTIVE_QA_EXPECTED_ALLIANCE_CELLS=269
ACTIVE_QA_EXPECTED_DEEP_DIVE_LINKS_POINT_19=3
ACTIVE_QA_EXPECTED_ROADMAP_LINKS_POINT_20=0
ACTIVE_QA_EXPECTED_ROADMAP_NEXT_MOVES_POINT_20=3
ACTIVE_QA_INDEPENDENT_POINTS=08,12
`);
assert.equal(state.REVIEW_ROUTE, 'candidates/progress/cw-ally-rev06-narrative-clarity-clean-numbering.html');
const good = {
  candidateHash: state.SOURCE_HUB_SHA256,
  accordions: 23,
  details: 27,
  images: 13,
  brokenImages: [],
  allianceRows: 49,
  allianceCells: 269,
  deepDiveLinksPoint19: 3,
  deepDiveLinksPoint19AllNewTab: true,
  roadmapLinksPoint20: 0,
  roadmapNextMovesPoint20: 3,
  independentPoints: { '08': true, '12': true },
  legacyANumberingVisible: false,
  pageOverflowPx: 0,
  failurePlaceholderVisible: false,
  duplicateIds: [],
  invalidLinks: [],
  brokenFragments: []
};
assert.deepEqual(validateSnapshot(good, state), []);
assert.ok(validateSnapshot({...good, roadmapLinksPoint20: 2}, state).some(x => x.includes('Point 20')));
assert.ok(validateSnapshot({...good, candidateHash: 'stale'}, state).some(x => x.includes('candidate hash')));
assert.ok(validateSnapshot({...good, brokenImages: [{src:'x'}]}, state).some(x => x.includes('broken images')));
console.log('PASS active review candidate contract unit tests');
