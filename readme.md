# Aperture Design System

A premium, monochrome, product-first design system: enormous white space, near-black ink, one blue
accent, hairline rules, huge tight-tracked display type, and full-bleed cinematic staging for product
imagery. Built for storefronts and product marketing where the object is the hero and the interface
gets out of the way.

## Where this came from

The brief was the public DESIGN.md template distributed as:

```
npx getdesign@latest add apple
```

Source page: https://getdesign.md/apple/design-md — an independent, third-party written *analysis of
publicly observable patterns*, summarised there as "premium white space, SF Pro, cinematic imagery"
and recommended for "premium product pages, cinematic marketing sites, and monochrome luxury designs".
The catalogue page carries the raw markdown behind a download control that could not be fetched
programmatically, so the token values, component inventory and copy here are **authored from that
written style brief**, not extracted from a file.

### What this system deliberately is not

It is a *style* system, not a brand recreation. It carries no third-party logo, no licensed
typeface, no product photography, and no reconstruction of any real company's screens, and it is not
affiliated with or endorsed by anyone. The aesthetic axes named in the brief — value-driven
monochrome, extreme negative space, hairline structure, restrained motion, mono-set specs — are
implemented under a neutral house name, **Aperture**, with its own numeric scale and its own accent
blue (`#0A66FF`). If you need to match a specific brand, replace `tokens/colors.css` and
`tokens/fonts.css`; nothing else assumes those values.

### Substitutions to fix (see CAVEATS at the bottom)

| Needed | Shipped | Why |
| --- | --- | --- |
| Optically-sized neutral grotesque | **Inter** (Google Fonts) | The brief names a system font that is not redistributable |
| Spec / numeral face | **IBM Plex Mono** | No mono was specified |
| Icon set | **Lucide**, 1.5px stroke, from CDN | No icon assets accompanied the brief |
| Photography | CSS "stage" panels (`Stage` in the web kit) | No imagery accompanied the brief; never generated |
| Logo | Wordmark set in type | No mark was supplied, and none was invented |

---

## Content fundamentals

**Voice.** Declarative and unhurried. Sentences are short and end in a full stop, even as headlines —
"Halo." "The line." "Machined from a single billet." The product is the subject; the company is
almost never named inside body copy.

**Person.** Second person for anything the reader does ("Your bag", "Add to bag", "You can add it
back at any time"). First-person plural only in support contexts ("How can we help?"). Never "I".

**Casing.** Sentence case everywhere: headlines, buttons, labels, table headers. Uppercase appears in
exactly two places — the 11px eyebrow above a headline (`NEW`, `ENGINEERING`) and status badges
(`IN STOCK`). Title Case is never used.

**Length.** Headlines are three to six words. Leads are one or two sentences, capped around 60
characters per line by `--container-narrow`. Button labels are one or two words with no punctuation
("Buy", "Add to bag", "Check out", "Learn more").

**Numbers carry the argument.** Claims are stated as measured facts in mono type — `142 g`, `38 h`,
`40 mm`, `From $349` — usually as a row of three under a headline instead of a paragraph of adjectives.
Prices are always written with the currency symbol and, where financing applies, a second tertiary
line ("or $29.08/mo. for 12 mo.").

**Never.** No exclamation marks, no emoji, no "amazing / revolutionary / game-changing", no ALL-CAPS
shouting, no hype adverbs, no jokes in error copy. Errors state the fact and the fix: "Check this
number." "Payment declined."

---

## Visual foundations

**Colour.** Value, not hue, does the work. Five near-whites (`#FFFFFF` → `#DCDFE3`) and six inks
(`#9AA1A9` → `#121417`) cover every surface and every piece of type; ink-900 is intentionally not pure
black. Exactly one accent — `#0A66FF` — reserved for links, the single primary CTA per view, and focus
rings; it is never used as a fill for decoration. Status colours (green / amber / red) appear only
when they carry information. Two backgrounds per page maximum: white and mist, or void and graphite.

**Dark stages.** Cinematic sections invert to `--void #08090B` with white display type and
`#A8AEB6` secondary copy. Dark and light sections alternate down a page; a page never uses more than
one dark treatment consecutively.

**Type.** One grotesque for everything, one mono for specifications. Display runs 96 / 72 / 56px at
semibold with `-0.032em` tracking and 1.04 leading — the tracking tightens as size grows and body
copy sits at `-0.011em`. Body is 17px / 1.52 in secondary ink; 15px small; 13px legal in tertiary.
Weight range is 300–700 but display never drops below 500, and 700 is nearly unused.

**Space.** The scale is 4 8 12 16 **22** 32 44 60 80 110 148 200 — the gutter unit is 22px, not 24.
Marketing sections breathe at 110–200px vertically while interface padding stays at 16–22px; that
contrast is the single strongest signal of the style. Containers: 692 (prose), 1024, 1280, 1440.

**Borders and elevation.** A 1px `#DCDFE3` hairline does the work borders and dividers usually do —
lists, spec tables and card outlines are all hairlines. Shadows are almost absent: `--shadow-card` is
barely perceptible, `--shadow-raise` appears only under a hovered navigating card, `--shadow-modal`
only under a dialog. Separation normally comes from a mist fill against white, not from a shadow.

**Radii.** 8 / 12 / 18 / 28 / 42px plus a 980px pill. Buttons and chips are *always* full pills,
never rounded rectangles. Cards are generous (28px) and feature panels rounder still (42px).

**Transparency and blur.** Only the global bar: a 72% scrim with `saturate(180%) blur(20px)`, floating
over whatever scrolls beneath, plus a light blur behind the dialog scrim. Nothing else is translucent —
no frosted cards, no glassy panels.

**Motion.** Long and decelerating: 200ms for hover colour, 320ms for state, 560ms for layout, 900ms
for cinematic reveals, all on `cubic-bezier(0.28, 0.11, 0.32, 1)`. No bounce, no spring, no overshoot,
no attention-seeking loops. Hover states shift a fill exactly one step (`--mist` → `--fog`) or lift a
card 2px; press states scale to 0.97 rather than changing colour. Links underline on hover with a 3px
offset. Focus is a 2px accent ring, 3px offset — never removed.

**Imagery.** One object, centred, lit from above, on either a near-black or a near-white ground, with
no props and no context. Colour is neutral to cool, contrast is high, grain is absent. Photography is
full-bleed inside its rounded panel and is never cropped into circles or decorated with overlays; text
sits above or below it, not on top of it — except in the hero, where display type sits on the dark
ground and the object sits below.

**Layout rules.** The 48px bar is the only fixed element. Content is centre-aligned in the hero and
left-aligned everywhere else. Grids are 3-up on desktop for products and 4-up for thumbnails.
Comparison and spec data always render as hairline rows with mono values, right- or centre-aligned.

---

## Iconography

Lucide, loaded from CDN (`https://unpkg.com/lucide@latest/dist/umd/lucide.min.js`) and wrapped by
`components/core/Icon.jsx`. **This is a substitution** — no icon assets came with the brief. Rules:

- Stroke is 1.5px so glyphs match the weight of a 1px hairline; 2px only inside a filled checkbox.
- Sizes: 14px inline with legal copy, 16px in nav and buttons, 18px with body copy, 24px maximum.
- Monochrome and inherit `currentColor`. Icons are never coloured, never filled, never in a coloured circle.
- Icons never appear next to headlines and never carry meaning alone — an icon-only control gets a `Tooltip`.
- **No emoji, ever.** No unicode arrows in UI chrome either; the chevron is a Lucide glyph. (One
  exception: `—` as an em-dash "not applicable" value in comparison tables.)
- Common set in use: `chevron-right`, `chevron-down`, `search`, `shopping-bag`, `check`, `x`, `truck`,
  `triangle-alert`.

There is no logo file. Wherever a mark would go, set **Aperture** in semibold with tight tracking
(see `guidelines/brand-wordmark.html`).

---

## Index

| Path | What |
| --- | --- |
| `styles.css` | The one file consumers link; `@import`s everything below |
| `tokens/fonts.css` | Webfont declaration (Inter + IBM Plex Mono) |
| `tokens/colors.css` | Paper, ink, accent, status, semantic aliases, dark scope |
| `tokens/typography.css` | Families, sizes, weights, leading, tracking, role shorthands |
| `tokens/spacing.css` | 4→200 scale, section rhythm, containers, control heights |
| `tokens/effects.css` | Radii, hairline, shadows, blur, motion, z-index |
| `tokens/base.css` | Body reset, link colours, selection, focus ring |
| `guidelines/*.html` | 22 specimen cards (Colors, Type, Spacing, Surfaces, Brand) |
| `components/core/` | `Icon`, `Button`, `Badge`, `Tag`, `Card` |
| `components/forms/` | `Input`, `Select`, `Checkbox`, `Radio`, `Switch` |
| `components/navigation/` | `Nav`, `Tabs` |
| `components/feedback/` | `Dialog`, `Toast`, `Tooltip` |
| `ui_kits/aperture_web/` | Click-through storefront: Store, Product, Compare, Bag, Support |
| `jsx-loader.js` | Preview-only shim so the card and kit HTML can render the `.jsx` sources |
| `SKILL.md` | Agent Skills front-matter for use in Claude Code |

Each component directory holds `<Name>.jsx`, `<Name>.d.ts`, `<Name>.prompt.md`, and one card HTML
showing its states.

### Intentional additions

- **`Icon`** — a wrapper for the substituted Lucide set, so no screen ever hand-rolls an SVG.
- **`Stage` / `Section` / `Eyebrow` / `Footer`** (inside the web kit, not the component library) —
  marketing furniture the brief implies but does not enumerate. They live in `ui_kits/aperture_web/Chrome.jsx`
  precisely so they are not mistaken for shared primitives.

---

## CAVEATS

1. **The raw DESIGN.md was not machine-readable.** Everything here is derived from the published style
   description on getdesign.md, so the numbers are a coherent invention consistent with that brief —
   not values copied from a source file. If you have the downloaded `DESIGN.md`, drop it in and the
   tokens can be reconciled against it exactly.
2. **Fonts are substituted.** Inter and IBM Plex Mono stand in. Send the real font files (or name the
   licensed family) and `tokens/fonts.css` becomes proper `@font-face` rules.
3. **Icons are substituted.** Lucide from CDN. If you have an icon set, it should be copied in.
4. **There is no photography and no logo.** `Stage` panels and a type-set wordmark hold their places.
5. **Deliberately unbranded.** No third-party mark, typeface, palette or screen is reproduced here.

## **What I need from you**

Pick up whichever of these applies and I will fold it in:

- **the downloaded `DESIGN.md` file** — so tokens match the source line for line;
- **your fonts** (files or licensed family names) and **your icon set**;
- **real product photography** — 3–5 images to replace the `Stage` placeholders;
- **the brand this is actually for** (name, wordmark, accent colour), so `Aperture` stops being a stand-in;
- **a second surface** if you need one — mobile app, docs site, or slide template — and I will build that kit next.

---

Remember to set this file's type to **Design System** in the Share menu so others in your org can use it.
