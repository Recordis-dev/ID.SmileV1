/* Loads sibling .jsx files that use `export function Name()` into the global scope,
   so plain HTML pages (cards, UI kit screens) can render them without a bundler.
   The compiled design-system bundle is what production consumers use; this is for previews. */
window.ApertureLoad = async function (paths) {
  for (const p of paths) {
    const src = await (await fetch(p)).text();
    const stripped = src.replace(/^\s*export\s+/gm, "").replace(/^\s*import[^;]*;?$/gm, "");
    const out = Babel.transform(stripped, { presets: [["react", { runtime: "classic" }]] }).code;
    (0, eval)(out);
  }
};
