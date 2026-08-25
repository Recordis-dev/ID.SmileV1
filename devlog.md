# ID Smile Development Log

## Iteration 1: Initial Deployment & Setup
*   **What happened:** Setup the repo, deployed to GitHub Pages, added base UI kits and design system HTML files from attachments.
*   **What worked:** Deployment actions and raw HTML parsing works without a build system.
*   **What didn't work:** N/A.

## Iteration 2: Content Adjustments (Dr. Benja & Services)
*   **What happened:** Replaced Dra. Esbreidy references with Odont. Benjamín Avendaño. Added a new array of 7 distinct services in 3 languages to the Marquee.
*   **What worked:** Content extraction and basic regex replacement.
*   **What didn't work:** Initial regex attempts to modify the scrolling marquee broke the HTML structure or duplicated elements.
*   **Learnings:** The marquee was driven by an infinite CSS animation (`@keyframes idsTicker`) duplicating `<span>` blocks. Replacing inner content must be done precisely to maintain the loop structure.

## Iteration 3: Marquee Physics & SLP Architecture
*   **What happened:** Attempted to add complex mouse-tracking physics to the marquee using `Web Animations API`. Tried to inject huge Service Landing Page (SLP) blocks into the main HTML.
*   **What worked:** The SLP injection worked visually but made the page huge.
*   **What didn't work:** `Web Animations API` (`playbackRate`) failed to apply smoothly across all browsers/DOM states. The hover effect inline styles were conflicting with the animation loop.
*   **Learnings:** Do not rely on CSS animations or the Web Animations API for complex frame-by-frame physics (acceleration, dead-zones). Use a pure `requestAnimationFrame` loop with `translate3d`.

## Iteration 4: Pure JS Marquee & Mega Menu
*   **What happened:** Ripped out CSS animations for the marquee, replaced with a pure JS render loop. Built a Durum.ai style CSS Mega-Menu. Extracted SLPs into standalone HTML files (`servicio-ortodoncia.html`, etc.).
*   **What worked:** Standalone HTML architecture drastically improved maintainability. Mega-menu CSS worked cleanly.
*   **What didn't work:** The user reported the Marquee is *still* too fast, lacks mobile responsiveness (touch events), and the SEO semantic structure of the Mega Menu needs improvement.

## Iteration 5: SEO, Mobile Physics & Self-Healing
*   **What happened:** Refactored Mega Menu into semantic `<nav>` with `<ul>`, `<li>` and `aria-label` attributes. Decreased Marquee base speed to `0.33` and widened the central dead-zone to `0.15`. Added `touchstart` and `touchmove` events for mobile interaction. Added a `scroll` event listener that temporarily speeds up the marquee. Re-wrote `devlog.md`.
*   **What worked:** The dual-approach structure is now entirely responsive and semantically ready for AI crawlers.
*   **Learnings:** Moving from `<div>`s to `<ul>/<li>` inside mega-menus is crucial for screen readers and SEO spiders to understand the hierarchy of SLPs vs Blogs.

## Iteration 8: Nav-Graph Correction and Legacy File Restoration
*   **What happened:** A previous refactoring step broke the GitHub Pages root routing and the Storefront `index.html` by incorrectly moving files out of their `ui_kits` context. The user correctly identified that this "degenerated" the base functionality and killed the versions viewer. We rolled back to a stable commit (`29da74b`).
*   **What worked:** In-situ architectural injection. Instead of moving files, we ran the Python 30-point self-healing loop (Schema, Metadata, CTAs, Sitemaps, Breadcrumbs, and HTML cleaning) *directly* on the `ui_kits/idsmile_remix/` folder. The Mega Menu links now correctly point to `IDSmileApertureRemix.dc.html#hash` rather than `index.html`.
*   **Learnings:** Never alter the original scaffolding/directory structure of a UI Kit template output unless instructed. Deep-linking must respect the existing router boundaries (e.g. `index.html` as the directory storefront and `.dc.html` as the specific app landing).
