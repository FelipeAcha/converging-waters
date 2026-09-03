import fs from 'node:fs';
import path from 'node:path';
import puppeteer from 'puppeteer-core';
import { parseState, validateSnapshot } from './active_review_candidate_contract.mjs';

const target = process.env.ACB_ACTIVE_TARGET_URL;
const chrome = process.env.CHROME_BIN;
const statePath = process.env.ACB_STATE_PATH || 'docs/candidates/progress/.cumulative-progress-state.txt';
const outDir = process.env.ACB_OUTPUT_DIR || 'acb-active-evidence';
if (!target) throw new Error('ACB_ACTIVE_TARGET_URL is required');
if (!chrome) throw new Error('CHROME_BIN is required');
const state = parseState(fs.readFileSync(statePath, 'utf8'));
if (!state.SOURCE_HUB_SHA256 || !state.REVIEW_ROUTE) throw new Error('Active review state is incomplete');
fs.mkdirSync(outDir, { recursive: true });

const browser = await puppeteer.launch({ executablePath: chrome, headless: true, args: ['--no-sandbox','--disable-gpu','--disable-dev-shm-usage'] });

async function findHubFrame(page) {
  const deadline = Date.now() + 90000;
  while (Date.now() < deadline) {
    for (const frame of page.frames()) {
      try {
        const v = await frame.evaluate(() => ({
          hash: document.documentElement?.dataset?.cwAuthoritativeCandidateSha256 || '',
          hasRoadmap: !!document.getElementById('current-roadmap-final'),
          hasAlliance: !!document.getElementById('alliance-architecture')
        }));
        if (v.hash === state.SOURCE_HUB_SHA256 && v.hasRoadmap && v.hasAlliance) return frame;
      } catch {}
    }
    await new Promise(r => setTimeout(r, 500));
  }
  throw new Error(`Timed out waiting for inner hub hash ${state.SOURCE_HUB_SHA256}`);
}

async function snapshotForViewport(name, width, height) {
  const page = await browser.newPage();
  await page.setViewport({ width, height, deviceScaleFactor: 1 });
  await page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }]);
  const consoleErrors = [];
  const pageErrors = [];
  const failedResponses = [];
  const failedRequests = [];
  page.on('console', msg => { if (msg.type() === 'error') consoleErrors.push(msg.text()); });
  page.on('pageerror', err => pageErrors.push(String(err)));
  page.on('response', res => {
    if (res.status() >= 400) failedResponses.push({url:res.url(), status:res.status(), resourceType:res.request().resourceType()});
  });
  page.on('requestfailed', req => failedRequests.push({url:req.url(), resourceType:req.resourceType(), error:req.failure()?.errorText || ''}));
  const response = await page.goto(target, { waitUntil: 'networkidle2', timeout: 120000 });
  if (!response || response.status() !== 200) throw new Error(`${name}: HTTP ${response?.status()}`);
  const hub = await findHubFrame(page);

  // QA-only: eager-load the exact existing image src values even when accordions are closed.
  await hub.evaluate(async () => {
    const imgs = [...document.images];
    imgs.forEach(img => { img.loading = 'eager'; });
    await Promise.all(imgs.map(img => {
      if (img.complete && img.naturalWidth > 0) return Promise.resolve();
      return new Promise(resolve => {
        const done = () => resolve();
        img.addEventListener('load', done, {once:true});
        img.addEventListener('error', done, {once:true});
        setTimeout(done, 12000);
      });
    }));
  });

  const independentPoints = await hub.evaluate(async () => {
    const wait = ms => new Promise(r => setTimeout(r, ms));
    const find = n => [...document.querySelectorAll('.cw-section-accordion')].find(box => {
      const label = box.querySelector(':scope > .cw-accordion-trigger .cw-accordion-label');
      return label && label.textContent.trim().startsWith(n + ' ·');
    });
    const check = async (child, parent) => {
      const c = find(child), p = find(parent);
      if (!c || !p) return false;
      const cb = c.querySelector(':scope > .cw-accordion-trigger');
      const pb = p.querySelector(':scope > .cw-accordion-trigger');
      if (!cb || !pb) return false;
      if (cb.getAttribute('aria-expanded') === 'true') cb.click();
      if (pb.getAttribute('aria-expanded') === 'true') pb.click();
      await wait(30);
      cb.click();
      await wait(50);
      const ok = cb.getAttribute('aria-expanded') === 'true' && pb.getAttribute('aria-expanded') !== 'true';
      cb.click();
      await wait(30);
      return ok;
    };
    return { '08': await check('08','07'), '12': await check('12','11') };
  });

  const point15Render = await hub.evaluate(async () => {
    const wait = ms => new Promise(r => setTimeout(r, ms));
    const box = [...document.querySelectorAll('.cw-section-accordion')].find(x => x.dataset.cwSection === '15');
    const button = box?.querySelector(':scope > .cw-accordion-trigger');
    if (!box || !button) return {rendered:false, reason:'missing-point-15'};
    if (button.getAttribute('aria-expanded') !== 'true') button.click();
    await wait(80);
    const cards = [...document.querySelectorAll('#finance-hypotheses .finance-route-card')];
    const viewportWidth = document.documentElement.clientWidth;
    const rects = cards.map(card => { const r=card.getBoundingClientRect(); return {left:r.left,right:r.right,width:r.width,height:r.height}; });
    const rendered = cards.length === 4 && rects.every(r => r.width > 0 && r.height > 0 && r.left >= -1 && r.right <= viewportWidth + 1);
    return {rendered, cardCount:cards.length, viewportWidth, rects};
  });
  const financeHandle = await hub.$('#finance-hypotheses');
  if (financeHandle) await financeHandle.screenshot({path:path.join(outDir, `active-${name}-point15.png`)});

  const metrics = await hub.evaluate(() => {
    const ids = [...document.querySelectorAll('[id]')].map(x => x.id).filter(Boolean);
    const counts = ids.reduce((m,id)=>(m[id]=(m[id]||0)+1,m),{});
    const duplicateIds = Object.entries(counts).filter(([,v])=>v>1).map(([k])=>k);
    const imgs = [...document.images].map(img => ({src:img.currentSrc||img.src||'', complete:img.complete, naturalWidth:img.naturalWidth, naturalHeight:img.naturalHeight}));
    const links = [...document.querySelectorAll('a')].map(a => ({href:a.getAttribute('href')||'', text:(a.innerText||'').trim()}));
    const invalidLinks = links.filter(x => !x.href.trim() || /^javascript:/i.test(x.href.trim()));
    const brokenFragments = links.filter(x => x.href.startsWith('#') && x.href.length > 1 && !document.getElementById(decodeURIComponent(x.href.slice(1))));
    const p19 = [...document.querySelectorAll('#deep-dives a[href*="deep-dives/"]')];
    const p20 = [...document.querySelectorAll('#current-roadmap-final a')];
    const p20Moves = [...document.querySelectorAll('#current-roadmap-final .roadmap-next')];
    const financeRouteCards = [...document.querySelectorAll('#finance-hypotheses .finance-route-card')];
    const financeMechanismMenu = document.querySelector('#finance-hypotheses .finance-mechanism-menu');
    const pointLabelLeft = n => {
      const box = [...document.querySelectorAll('.cw-section-accordion')].find(x => x.dataset.cwSection === n);
      const label = box?.querySelector(':scope > .cw-accordion-trigger .cw-accordion-label');
      return label ? label.getBoundingClientRect().left : Number.NaN;
    };
    const point18LabelLeftPx = pointLabelLeft('18');
    const point19LabelLeftPx = pointLabelLeft('19');
    const text = (document.body.innerText||'').replace(/\s+/g,' ');
    const failurePattern = /(unable to load|could not load|integrity mismatch|loading review|loading substantive review|error state)/i;
    return {
      candidateHash: document.documentElement.dataset.cwAuthoritativeCandidateSha256 || '',
      accordions: document.querySelectorAll('.cw-section-accordion').length,
      details: document.querySelectorAll('details').length,
      images: imgs.length,
      brokenImages: imgs.filter(x => !x.complete || x.naturalWidth <= 0 || x.naturalHeight <= 0),
      allianceRows: document.querySelectorAll('#alliance-architecture table tr').length,
      allianceCells: document.querySelectorAll('#alliance-architecture table th, #alliance-architecture table td').length,
      deepDiveLinksPoint19: p19.length,
      deepDiveLinksPoint19AllNewTab: p19.every(a => a.target === '_blank' && (a.rel||'').includes('noopener') && (a.rel||'').includes('noreferrer')),
      roadmapLinksPoint20: p20.length,
      roadmapNextMovesPoint20: p20Moves.length,
      financeRouteCardsPoint15: financeRouteCards.length,
      financeMechanismMenuPoint15Present: !!financeMechanismMenu,
      financeRouteCardsPoint15Rendered: false,
      point18LabelLeftPx,
      point19LabelLeftPx,
      point18_19LabelLeftDeltaPx: Math.abs(point18LabelLeftPx - point19LabelLeftPx),
      legacyANumberingVisible: /07A\s*·\s*From evidence to implementation|10A\s*·\s*River Economy/.test(text),
      pageOverflowPx: Math.max(0, document.documentElement.scrollWidth - document.documentElement.clientWidth),
      failurePlaceholderVisible: failurePattern.test(text.slice(0,3000)),
      duplicateIds,
      invalidLinks,
      brokenFragments
    };
  });
  const nonCritical = x => {
    try { return new URL(x.url).pathname.endsWith('/favicon.ico'); } catch { return false; }
  };
  metrics.financeRouteCardsPoint15Rendered = point15Render.rendered === true;
  metrics.financeRouteCardsPoint15RenderDetail = point15Render;
  metrics.failedResponses = failedResponses;
  metrics.failedRequests = failedRequests;
  metrics.criticalFailedResponses = failedResponses.filter(x => !nonCritical(x));
  metrics.criticalFailedRequests = failedRequests.filter(x => !nonCritical(x));
  metrics.independentPoints = independentPoints;
  metrics.consoleErrors = consoleErrors;
  metrics.pageErrors = pageErrors;
  metrics.httpStatus = response.status();
  const errors = validateSnapshot(metrics, state);
  const nonCriticalPageErrors = pageErrors.filter(e => e.includes('REV04 identity mismatch') && metrics.candidateHash === state.SOURCE_HUB_SHA256);
  const criticalPageErrors = pageErrors.filter(e => !nonCriticalPageErrors.includes(e));
  metrics.nonCriticalPageErrors = nonCriticalPageErrors;
  metrics.criticalPageErrors = criticalPageErrors;
  if (criticalPageErrors.length) errors.push(`${name}: page errors ${JSON.stringify(criticalPageErrors)}`);
  const screenshot = path.join(outDir, `active-${name}.png`);
  await page.screenshot({path:screenshot, fullPage:true});
  fs.writeFileSync(path.join(outDir, `active-${name}.json`), JSON.stringify({metrics, errors}, null, 2) + '\n');
  await page.close();
  return {name, metrics, errors, screenshot};
}

const results = [];
try {
  results.push(await snapshotForViewport('desktop', 1440, 1000));
  results.push(await snapshotForViewport('mobile', 390, 844));
} finally {
  await browser.close();
}
const allErrors = results.flatMap(r => r.errors.map(e => `${r.name}: ${e}`));
const report = {target, revision:state.REVISION_NAME, expectedHash:state.SOURCE_HUB_SHA256, results, errors:allErrors, status:allErrors.length ? 'FAIL' : 'PASS'};
fs.writeFileSync(path.join(outDir, 'active-review-report.json'), JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify({target, revision:state.REVISION_NAME, status:report.status, errors:allErrors}, null, 2));
if (allErrors.length) process.exitCode = 1;
