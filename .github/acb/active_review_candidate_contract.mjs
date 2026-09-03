export function parseState(text) {
  const out = {};
  for (const raw of String(text || '').split(/\r?\n/)) {
    if (!raw || raw.startsWith('#') || !raw.includes('=')) continue;
    const i = raw.indexOf('=');
    out[raw.slice(0, i)] = raw.slice(i + 1);
  }
  return out;
}

const n = (state, key) => Number.parseInt(state[key], 10);
const f = (state, key) => Number.parseFloat(state[key]);

export function validateSnapshot(snapshot, state) {
  const errors = [];
  const req = (ok, msg) => { if (!ok) errors.push(msg); };
  req(snapshot.candidateHash === state.SOURCE_HUB_SHA256,
      `active candidate hash mismatch: got ${snapshot.candidateHash}, expected ${state.SOURCE_HUB_SHA256}`);
  req(snapshot.accordions === n(state, 'ACTIVE_QA_EXPECTED_ACCORDIONS'),
      `accordion count ${snapshot.accordions} != ${state.ACTIVE_QA_EXPECTED_ACCORDIONS}`);
  req(snapshot.details === n(state, 'ACTIVE_QA_EXPECTED_DETAILS'),
      `details count ${snapshot.details} != ${state.ACTIVE_QA_EXPECTED_DETAILS}`);
  req(snapshot.images === n(state, 'ACTIVE_QA_EXPECTED_IMAGES'),
      `image count ${snapshot.images} != ${state.ACTIVE_QA_EXPECTED_IMAGES}`);
  req(snapshot.brokenImages.length === 0, `broken images: ${JSON.stringify(snapshot.brokenImages)}`);
  req(snapshot.allianceRows === n(state, 'ACTIVE_QA_EXPECTED_ALLIANCE_ROWS'),
      `Alliance rows ${snapshot.allianceRows} != ${state.ACTIVE_QA_EXPECTED_ALLIANCE_ROWS}`);
  req(snapshot.allianceCells === n(state, 'ACTIVE_QA_EXPECTED_ALLIANCE_CELLS'),
      `Alliance cells ${snapshot.allianceCells} != ${state.ACTIVE_QA_EXPECTED_ALLIANCE_CELLS}`);
  req(snapshot.deepDiveLinksPoint19 === n(state, 'ACTIVE_QA_EXPECTED_DEEP_DIVE_LINKS_POINT_19'),
      `Point 19 deep-dive links ${snapshot.deepDiveLinksPoint19} != ${state.ACTIVE_QA_EXPECTED_DEEP_DIVE_LINKS_POINT_19}`);
  req(snapshot.deepDiveLinksPoint19AllNewTab,
      'Point 19 deep-dive links must all open in a new tab with noopener/noreferrer');
  req(snapshot.roadmapLinksPoint20 === n(state, 'ACTIVE_QA_EXPECTED_ROADMAP_LINKS_POINT_20'),
      `Point 20 links ${snapshot.roadmapLinksPoint20} != ${state.ACTIVE_QA_EXPECTED_ROADMAP_LINKS_POINT_20}`);
  req(snapshot.roadmapNextMovesPoint20 === n(state, 'ACTIVE_QA_EXPECTED_ROADMAP_NEXT_MOVES_POINT_20'),
      `Point 20 next moves ${snapshot.roadmapNextMovesPoint20} != ${state.ACTIVE_QA_EXPECTED_ROADMAP_NEXT_MOVES_POINT_20}`);
  if (state.ACTIVE_QA_EXPECTED_FINANCE_ROUTE_CARDS_POINT_15) {
    req(snapshot.financeRouteCardsPoint15 === n(state, 'ACTIVE_QA_EXPECTED_FINANCE_ROUTE_CARDS_POINT_15'),
        `Point 15 financing-route cards ${snapshot.financeRouteCardsPoint15} != ${state.ACTIVE_QA_EXPECTED_FINANCE_ROUTE_CARDS_POINT_15}`);
    req(snapshot.financeMechanismMenuPoint15Present === false,
        'Point 15 legacy finance-mechanism menu must be absent');
  }
  if (state.ACTIVE_QA_MAX_POINT_18_19_LABEL_LEFT_DELTA_PX) {
    req(Number.isFinite(snapshot.point18_19LabelLeftDeltaPx) && snapshot.point18_19LabelLeftDeltaPx <= f(state, 'ACTIVE_QA_MAX_POINT_18_19_LABEL_LEFT_DELTA_PX'),
        `Point 18/19 heading left-edge delta ${snapshot.point18_19LabelLeftDeltaPx}px > ${state.ACTIVE_QA_MAX_POINT_18_19_LABEL_LEFT_DELTA_PX}px`);
  }
  for (const point of String(state.ACTIVE_QA_INDEPENDENT_POINTS || '').split(',').filter(Boolean)) {
    req(snapshot.independentPoints?.[point] === true, `Point ${point} is not an independent accordion`);
  }
  req(!snapshot.legacyANumberingVisible, 'legacy 07A/10A numbering remains visible');
  req(snapshot.pageOverflowPx <= 2, `page overflow ${snapshot.pageOverflowPx}px`);
  req(!snapshot.failurePlaceholderVisible, 'loading/failure placeholder remains visible');
  req(snapshot.duplicateIds.length === 0, `duplicate ids: ${snapshot.duplicateIds.join(', ')}`);
  req(snapshot.invalidLinks.length === 0, `invalid links: ${JSON.stringify(snapshot.invalidLinks)}`);
  req(snapshot.brokenFragments.length === 0, `broken fragments: ${JSON.stringify(snapshot.brokenFragments)}`);
  req((snapshot.criticalFailedResponses || []).length === 0, `critical failed responses: ${JSON.stringify(snapshot.criticalFailedResponses || [])}`);
  req((snapshot.criticalFailedRequests || []).length === 0, `critical failed requests: ${JSON.stringify(snapshot.criticalFailedRequests || [])}`);
  return errors;
}
