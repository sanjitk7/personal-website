// Adversarial check of project-card hover on b-cards and b-carousel, desktop (hover) and phone (touch).
// Usage: from the repo root run `python3 -m http.server 8765`, then `node mockups/tests/hover-check.js <screenshot-dir>`.
const { chromium } = require('playwright');
const out = process.argv[2]; let fails = 0;
const ok = (c, m) => { if (!c) { fails++; console.log('FAIL', m); } };
const opacities = el => [...el.querySelectorAll('.img img')].map(im => +getComputedStyle(im).opacity);

(async () => {
  const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY, bypass: 'localhost' } });
  for (const page of ['b-cards', 'b-carousel']) {
    for (const [tag, opts] of [['desktop', { viewport: { width: 1440, height: 900 } }],
                               ['mobile', { viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true }]]) {
      const ctx = await b.newContext({ ...opts, deviceScaleFactor: 1 }); const p = await ctx.newPage();
      const errs = [];
      p.on('pageerror', e => errs.push(e.message));
      p.on('console', m => m.type() === 'error' && errs.push(m.text()));
      p.on('requestfailed', r => errs.push('request failed ' + r.url()));
      await p.goto(`http://localhost:8765/mockups/${page}.html`, { waitUntil: 'networkidle' });
      await p.evaluate(() => document.querySelectorAll('img').forEach(i => (i.loading = 'eager')));
      await p.waitForLoadState('networkidle'); await p.waitForTimeout(500);
      const real = errs.filter(x => !/googletagmanager|ERR_TUNNEL_CONNECTION_FAILED/.test(x)); // analytics is blocked in this sandbox only
      ok(!real.length, `${page}/${tag} errors: ${real.join(' | ')}`);
      const sw = await p.evaluate(() => [document.documentElement.scrollWidth, innerWidth]);
      ok(sw[0] <= sw[1], `${page}/${tag} horizontal page overflow ${sw}`);
      const canHover = await p.evaluate(() => matchMedia('(hover:hover)').matches);
      const cards = await p.$$('#work .card');
      for (let i = 0; i < cards.length; i++) {
        const c = cards[i];
        await c.scrollIntoViewIfNeeded(); await p.waitForTimeout(350);
        const info = await c.evaluate(el => ({
          name: el.querySelector('h3').textContent,
          imgs: [...el.querySelectorAll('.img img')].map(im => ({ cls: im.className, loaded: im.complete && im.naturalWidth > 0,
            fit: getComputedStyle(im).objectFit, op: +getComputedStyle(im).opacity })),
        }));
        const id = `${page}/${tag} "${info.name}"`;
        for (const im of info.imgs) {
          ok(im.loaded, `${id} ${im.cls} image failed to load`);
          ok(im.fit === 'contain', `${id} ${im.cls} uses object-fit:${im.fit}, so it gets cropped`);
        }
        const hasHov = info.imgs.some(x => x.cls === 'hov');
        ok(info.imgs[0].cls === 'base' && info.imgs[0].op === 1, `${id} default image not visible at rest`);
        if (hasHov) ok(info.imgs[1].op === 0, `${id} hover image visible at rest`);
        if (canHover && page === 'b-carousel') await (await c.$('.img')).screenshot({ path: `${out}/h-${i}-before.png` });
        if (!hasHov) { // a card without a second image must never go blank on hover
          await c.hover(); await p.waitForTimeout(450);
          ok((await c.evaluate(opacities))[0] === 1, `${id} has no hover image and goes blank on hover`);
          await p.mouse.move(0, 0); continue;
        }

        await c.hover(); await p.waitForTimeout(450);
        const ops = await c.evaluate(opacities);
        if (canHover) {
          ok(ops[0] === 0 && ops[1] === 1, `${id} hover did not switch cleanly (default=${ops[0]}, hover=${ops[1]})`);
          // Overlay test: the hovered render must be pixel-identical to a render with the default image removed.
          const withBase = await (await c.$('.img')).screenshot();
          await c.evaluate(el => (el.querySelector('.base').style.visibility = 'hidden'));
          const withoutBase = await (await c.$('.img')).screenshot();
          await c.evaluate(el => (el.querySelector('.base').style.visibility = ''));
          ok(Buffer.compare(withBase, withoutBase) === 0, `${id} default image shows through the hover image`);
          if (page === 'b-carousel') await (await c.$('.img')).screenshot({ path: `${out}/h-${i}-after.png` });
        } else {
          ok(ops[0] === 1 && ops[1] === 0, `${id} touch device got stuck in hover state`);
        }
        await p.mouse.move(0, 0); await p.waitForTimeout(400);
        const back = await c.evaluate(opacities);
        ok(back[0] === 1 && back[1] === 0, `${id} did not return to default after hover`);
      }
      if (page === 'b-carousel') {
        // Hover lift must not be clipped by the scroll track.
        const clip = await p.evaluate(() => { const t = document.querySelector('.track'); return parseFloat(getComputedStyle(t).paddingTop); });
        ok(clip >= 4, `${page}/${tag} track has no top padding, hover lift is clipped`);
        // Arrows must reach every card and disable at the end.
        await p.evaluate(() => (document.querySelector('.track').style.scrollBehavior = 'auto'));
        await p.$eval('.track', t => { t.scrollIntoView(); t.scrollLeft = 0; }); await p.waitForTimeout(200);
        ok(await p.$eval('.arr.prev', x => x.disabled), `${page}/${tag} prev arrow not disabled at the start`);
        const seen = new Set();
        for (let k = 0; k < 12; k++) {
          (await p.evaluate(() => { const t = document.querySelector('.track').getBoundingClientRect();
            return [...document.querySelectorAll('.track .card')].map((c, i) => { const r = c.getBoundingClientRect();
              return r.left >= t.left - 2 && r.right <= t.right + 2 ? i : -1; }).filter(i => i >= 0); })).forEach(i => seen.add(i));
          if (await p.$eval('.arr.next', x => x.disabled)) break;
          await p.click('.arr.next'); await p.waitForTimeout(300);
        }
        ok(seen.size === cards.length, `${page}/${tag} arrows only reach cards ${[...seen]} of ${cards.length}`);
        ok(await p.$eval('.arr.next', x => x.disabled), `${page}/${tag} next arrow not disabled at the end`);
      }
      console.log(`${page}/${tag}: ${cards.length} cards checked, hover-capable=${canHover}`);
      await ctx.close();
    }
  }
  await b.close();
  console.log(fails ? `${fails} FAILURES` : 'ALL CHECKS PASSED');
  process.exit(fails ? 1 : 0);
})();
