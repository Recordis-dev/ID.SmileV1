Renders a single thin-stroke Lucide glyph; use it anywhere an icon appears instead of inline SVG or emoji.

```jsx
<Icon name="chevron-right" size={16} />
```

Requires the Lucide UMD script on the page (`https://unpkg.com/lucide@latest/dist/umd/lucide.min.js`). Stroke stays at 1.5 so glyphs read at the same weight as 1px hairlines. Icons are monochrome and inherit `currentColor` — never colour them for decoration.
