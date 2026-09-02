import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import puppeteer from 'puppeteer-core';

const target = process.env.ACB_TARGET_URL;
const chrome = process.env.CHROME_BIN;
const outDir = process.env.ACB_OUTPUT_DIR || 'acb-evidence';
if (!target) throw new Error('ACB_TARGET_URL is required');
if (!chrome) throw new Error('CHROME_BIN is required');
fs.mkdirSync(outDir, { recursive: true });

const checklist = JSON.parse(fs.readFileSync('.github/acb/alliance-web-checklist.json', 'utf8'));
const browser = await puppeteer.launch({
  executablePath: chrome,
  headless: true,
  args: ['--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage']
});

const report = {
  schema_version: '1.0',
  target,
  commit_sha: process.env.GITHUB_SHA || null,
  run_id: process.env.GITHUB_RUN_ID || null,
  generated_at: new Date().toISOString(),
  checklist_sha256: crypto.createHash('sha256').update(JSON.stringify(checklist)).digest('hex'),
  viewports: {},
  hard_gates: {},
  visual_review_gates: Object.fromEntries(checklist.visual_review_gates.map(x => [x, 'PENDING_EXPLICIT_VISUAL_REVIEW']))
};

let renderedHtmlForHash = '';

for (const vp of checklist.required_viewports) {
  const page = await browser.newPage();
  await page.setViewport({ width: vp.width, height: vp.height, deviceScaleFactor: 1 });
  const consoleErrors = [];
  const pageErrors = [];
  page.on('console', msg => { if (msg.type() === 'error') consoleErrors.push(msg.text()); });
  page.on('pageerror', err => pageErrors.push(String(err)));

  const response = await page.goto(target, { waitUntil: 'networkidle2', timeout: 90000 });
  await new Promise(resolve => setTimeout(resolve, 2500));
  const screenshot = path.join(outDir, `${vp.name}.png`);
  await page.screenshot({ path: screenshot, fullPage: true });

  const metrics = await page.evaluate(() => {
    const visible = el => {
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return s.display !== 'none' && s.visibility !== 'hidden' && Number(s.opacity || 1) > 0 && r.width > 0 && r.height > 0;
    };
    const ids = [...document.querySelectorAll('[id]')].map(el => el.id).filter(Boolean);
    const counts = ids.reduce((m, id) => (m[id] = (m[id] || 0) + 1, m), {});
    const duplicateIds = Object.entries(counts).filter(([,n]) => n > 1).map(([id]) => id);
    const imgs = [...document.images].filter(visible).map(img => ({
      src: img.currentSrc || img.src || '',
      alt: img.getAttribute('alt'),
      naturalWidth: img.naturalWidth,
      naturalHeight: img.naturalHeight
    }));
    const links = [...document.querySelectorAll('a')].filter(visible).map(a => ({
      href: a.getAttribute('href') || '',
      text: (a.innerText || '').trim().slice(0,120)
    }));
    const invalidLinks = links.filter(x => !x.href.trim() || /^javascript:/i.test(x.href.trim()));
    const brokenFragments = links.filter(x => x.href.startsWith('#') && x.href.length > 1 && !document.getElementById(decodeURIComponent(x.href.slice(1))));
    const h1s = [...document.querySelectorAll('h1')].filter(visible);
    const headings = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].filter(visible).map(h => ({level:Number(h.tagName.slice(1)), text:(h.innerText||'').trim().slice(0,160)}));
    const headingJumps = [];
    for (let i=1;i<headings.length;i++) if (headings[i].level > headings[i-1].level + 1) headingJumps.push({from:headings[i-1],to:headings[i]});
    const overflowing = [...document.querySelectorAll('body *')].filter(visible).map(el => {
      const r = el.getBoundingClientRect();
      return {tag:el.tagName.toLowerCase(), id:el.id||'', cls:String(el.className||'').slice(0,120), left:r.left, right:r.right, width:r.width};
    }).filter(r => r.left < -2 || r.right > window.innerWidth + 2).slice(0,100);
    const bodyText = (document.body.innerText || '').replace(/\s+/g,' ').trim();
    const failurePattern = /(unable to load|could not load|integrity mismatch|loading published working synthesis|loading converging waters|error state)/i;
    return {
      title: document.title.trim(),
      hasViewportMeta: !!document.querySelector('meta[name="viewport"]'),
      metaDescription: document.querySelector('meta[name="description"]')?.content?.trim() || '',
      visibleH1Count: h1s.length,
      visibleH1Text: h1s.map(x => (x.innerText||'').trim()),
      hasMain: !![...document.querySelectorAll('main')].find(visible),
      hasNav: !![...document.querySelectorAll('nav')].find(visible),
      hasFooter: !![...document.querySelectorAll('footer')].find(visible),
      duplicateIds,
      visibleImages: imgs.length,
      brokenImages: imgs.filter(x => x.naturalWidth <= 0 || x.naturalHeight <= 0),
      imagesMissingAlt: imgs.filter(x => x.alt === null || !String(x.alt).trim()),
      visibleLinks: links.length,
      invalidLinks,
      brokenFragments,
      headings,
      headingJumps,
      scrollWidth: document.documentElement.scrollWidth,
      clientWidth: document.documentElement.clientWidth,
      pageOverflowPx: Math.max(0, document.documentElement.scrollWidth - document.documentElement.clientWidth),
      overflowingElements: overflowing,
      bodyTextLength: bodyText.length,
      failurePlaceholderVisible: failurePattern.test(bodyText.slice(0,2500))
    };
  });

  const html = await page.content();
  if (vp.name === 'desktop') renderedHtmlForHash = html;
  report.viewports[vp.name] = {
    ...metrics,
    http_status: response?.status() ?? null,
    console_errors: consoleErrors,
    page_errors: pageErrors,
    screenshot
  };
  fs.writeFileSync(path.join(outDir, `${vp.name}.html`), html, 'utf8');
  await page.close();
}

await browser.close();
report.rendered_html_sha256 = crypto.createHash('sha256').update(renderedHtmlForHash).digest('hex');

const desktop = report.viewports.desktop;
const mobile = report.viewports.mobile;
const set = (name, pass, evidence) => report.hard_gates[name] = { status: pass ? 'PASS' : 'FAIL', evidence };
set('page_loads_without_error_state', [desktop,mobile].every(v => v.http_status === 200 && v.page_errors.length === 0), {desktop_status:desktop.http_status,mobile_status:mobile.http_status,desktop_page_errors:desktop.page_errors,mobile_page_errors:mobile.page_errors});
set('document_has_nonempty_title', !!desktop.title && !!mobile.title, {desktop:desktop.title,mobile:mobile.title});
set('document_has_viewport_meta', desktop.hasViewportMeta && mobile.hasViewportMeta, {desktop:desktop.hasViewportMeta,mobile:mobile.hasViewportMeta});
set('exactly_one_visible_h1', desktop.visibleH1Count === 1 && mobile.visibleH1Count === 1, {desktop:desktop.visibleH1Text,mobile:mobile.visibleH1Text});
set('main_landmark_present', desktop.hasMain && mobile.hasMain, {desktop:desktop.hasMain,mobile:mobile.hasMain});
set('no_duplicate_ids', desktop.duplicateIds.length === 0 && mobile.duplicateIds.length === 0, {desktop:desktop.duplicateIds,mobile:mobile.duplicateIds});
set('no_broken_images', desktop.brokenImages.length === 0 && mobile.brokenImages.length === 0, {desktop:desktop.brokenImages,mobile:mobile.brokenImages});
set('all_content_images_have_alt_text', desktop.imagesMissingAlt.length === 0 && mobile.imagesMissingAlt.length === 0, {desktop:desktop.imagesMissingAlt,mobile:mobile.imagesMissingAlt});
set('no_invalid_empty_or_javascript_links', desktop.invalidLinks.length === 0 && mobile.invalidLinks.length === 0, {desktop:desktop.invalidLinks,mobile:mobile.invalidLinks});
set('all_same_page_fragment_links_resolve', desktop.brokenFragments.length === 0 && mobile.brokenFragments.length === 0, {desktop:desktop.brokenFragments,mobile:mobile.brokenFragments});
set('no_horizontal_page_overflow_desktop', desktop.pageOverflowPx <= 2, {overflow_px:desktop.pageOverflowPx,scroll_width:desktop.scrollWidth,client_width:desktop.clientWidth});
set('no_horizontal_page_overflow_mobile', mobile.pageOverflowPx <= 2, {overflow_px:mobile.pageOverflowPx,scroll_width:mobile.scrollWidth,client_width:mobile.clientWidth});
set('no_material_element_overflow_desktop', desktop.overflowingElements.length === 0, desktop.overflowingElements);
set('no_material_element_overflow_mobile', mobile.overflowingElements.length === 0, mobile.overflowingElements);
set('heading_hierarchy_has_no_level_jumps', desktop.headingJumps.length === 0 && mobile.headingJumps.length === 0, {desktop:desktop.headingJumps,mobile:mobile.headingJumps});
set('no_loading_or_failure_placeholder_remains_visible', !desktop.failurePlaceholderVisible && !mobile.failurePlaceholderVisible, {desktop:desktop.failurePlaceholderVisible,mobile:mobile.failurePlaceholderVisible});

const hardNames = checklist.hard_gates;
const missing = hardNames.filter(name => !(name in report.hard_gates));
if (missing.length) throw new Error(`Guard implementation missing hard gates: ${missing.join(', ')}`);
report.hard_gate_pass_count = hardNames.filter(name => report.hard_gates[name].status === 'PASS').length;
report.hard_gate_total = hardNames.length;
report.hard_gate_percent = Math.round(10000 * report.hard_gate_pass_count / report.hard_gate_total) / 100;
report.hard_gate_status = report.hard_gate_pass_count === report.hard_gate_total ? 'PASS' : 'FAIL';

fs.writeFileSync(path.join(outDir, 'acb-report.json'), JSON.stringify(report, null, 2) + '\n', 'utf8');
console.log(JSON.stringify({target:report.target, hard_gate_status:report.hard_gate_status, hard_gate_percent:report.hard_gate_percent, rendered_html_sha256:report.rendered_html_sha256}, null, 2));
if (report.hard_gate_status !== 'PASS') process.exitCode = 1;
