import assert from 'node:assert/strict';
import { parseState, validateSnapshot } from './active_review_candidate_contract.mjs';

const state = parseState(`REVISION_NAME=CW-ALLY-REV06A — Alignment + Financing Clarity
SOURCE_HUB_SHA256=d5a73de694756bfc3f4efbf62cb98ba4d72a9052dca178e7d45a0ac0cd0958c0
REVIEW_ROUTE=candidates/progress/cw-ally-rev06a-alignment-financing-clarity.html
ACTIVE_QA_EXPECTED_ACCORDIONS=23
ACTIVE_QA_EXPECTED_DETAILS=27
ACTIVE_QA_EXPECTED_IMAGES=13
ACTIVE_QA_EXPECTED_ALLIANCE_ROWS=49
ACTIVE_QA_EXPECTED_ALLIANCE_CELLS=269
ACTIVE_QA_EXPECTED_DEEP_DIVE_LINKS_POINT_19=3
ACTIVE_QA_EXPECTED_ROADMAP_LINKS_POINT_20=0
ACTIVE_QA_EXPECTED_ROADMAP_NEXT_MOVES_POINT_20=3
ACTIVE_QA_EXPECTED_FINANCE_ROUTE_CARDS_POINT_15=4
ACTIVE_QA_MAX_POINT_18_19_LABEL_LEFT_DELTA_PX=1
ACTIVE_QA_INDEPENDENT_POINTS=08,12
`);
assert.equal(state.REVIEW_ROUTE, 'candidates/progress/cw-ally-rev06a-alignment-financing-clarity.html');
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
  financeRouteCardsPoint15: 4,
  financeMechanismMenuPoint15Present: false,
  point18_19LabelLeftDeltaPx: 0,
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
assert.ok(validateSnapshot({...good, financeRouteCardsPoint15: 0}, state).some(x => x.includes('Point 15')));
assert.ok(validateSnapshot({...good, financeMechanismMenuPoint15Present: true}, state).some(x => x.includes('legacy finance-mechanism')));
assert.ok(validateSnapshot({...good, point18_19LabelLeftDeltaPx: 39.5}, state).some(x => x.includes('Point 18/19')));
assert.ok(validateSnapshot({...good, criticalFailedResponses: [{url:'https://example.test/missing.css', status:404}]}, state).some(x => x.includes('critical failed responses')));
console.log('PASS active review candidate contract unit tests');
