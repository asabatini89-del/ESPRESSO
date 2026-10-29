// Exports every design to PNG: node social/src/render.js  (needs Playwright and a local web server on :8765 at the repo root)
const { chromium } = require(process.env.PW || "playwright");
const path = require("path");
const OUT = path.join(__dirname, "..");
const IDS = ["p01","p02","p03","p04","p05","p06","p07","p08","p09","p10","s01","s02","s03","s04","s05","s06","s07","s08","s09","s10"];
(async () => {
  const b = await chromium.launch();
  for (const lang of ["en","ar"]) for (const id of IDS) {
    const story = id.startsWith("s");
    const p = await b.newPage({viewport:{width:1080,height:story?1920:1350}});
    const errs = []; p.on("pageerror", e => errs.push(e.message)); p.on("requestfailed", r => errs.push("FAIL " + r.url()));
    await p.goto(`http://127.0.0.1:8765/social/src/designs.html?id=${id}&lang=${lang}`);
    await p.waitForSelector("body[data-ready]"); await p.waitForTimeout(150);
    const file = `${story ? "stories" : "posts"}/${lang}/${id}-${lang}.png`;
    await p.locator("#frame").screenshot({path: path.join(OUT, file)});
    console.log(file, errs.length ? errs : "");
    await p.close();
  }
  await b.close();
})();
