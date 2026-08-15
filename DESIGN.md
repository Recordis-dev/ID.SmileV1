---
name: ID Smile / Aperture Design System
colors:
  surface: '#FFFFFF'
  surface-dim: '#FAFBFC'
  surface-bright: '#FFFFFF'
  surface-container-lowest: '#FFFFFF'
  surface-container-low: '#F2F4F6'
  surface-container: '#E7EAEE'
  surface-container-high: '#DCDFE3'
  surface-container-highest: '#9AA1A9'
  on-surface: '#121417'
  on-surface-variant: '#5A6169'
  inverse-surface: '#08090B'
  inverse-on-surface: '#A8AEB6'
  outline: '#DCDFE3'
  outline-variant: '#9AA1A9'
  surface-tint: '#7C838C'
  primary: '#0A66FF'
  on-primary: '#FFFFFF'
  primary-container: '#EAF1FF'
  on-primary-container: '#0752CC'
  inverse-primary: '#2A7BFF'
  secondary: '#121417'
  on-secondary: '#FFFFFF'
  secondary-container: '#F2F4F6'
  on-secondary-container: '#121417'
  tertiary: '#7C838C'
  on-tertiary: '#FFFFFF'
  tertiary-container: '#F2F4F6'
  on-tertiary-container: '#3C4248'
  error: '#D0342C'
  on-error: '#FFFFFF'
  error-container: '#FBEBEA'
  on-error-container: '#D0342C'
  primary-fixed: '#EAF1FF'
  primary-fixed-dim: '#2A7BFF'
  on-primary-fixed: '#0752CC'
  on-primary-fixed-variant: '#0A66FF'
  secondary-fixed: '#F2F4F6'
  secondary-fixed-dim: '#DCDFE3'
  on-secondary-fixed: '#121417'
  on-secondary-fixed-variant: '#5A6169'
  tertiary-fixed: '#F2F4F6'
  tertiary-fixed-dim: '#DCDFE3'
  on-tertiary-fixed: '#3C4248'
  on-tertiary-fixed-variant: '#5A6169'
  background: '#FFFFFF'
  on-background: '#121417'
  surface-variant: '#F2F4F6'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 96px
    fontWeight: '300'
    lineHeight: 1.04
    letterSpacing: -0.032em
  headline-lg:
    fontFamily: Inter
    fontSize: 56px
    fontWeight: '600'
    lineHeight: 1.12
    letterSpacing: -0.021em
  headline-md:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 1.12
    letterSpacing: -0.021em
  body-lg:
    fontFamily: Inter
    fontSize: 17px
    fontWeight: '400'
    lineHeight: 1.52
    letterSpacing: -0.011em
  body-md:
    fontFamily: Inter
    fontSize: 15px
    fontWeight: '400'
    lineHeight: 1.62
    letterSpacing: -0.011em
  label-md:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 1.62
    letterSpacing: -0.011em
  label-sm:
    fontFamily: 'IBM Plex Mono'
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 1.4
    letterSpacing: -0.011em
rounded:
  sm: 8px
  DEFAULT: 12px
  md: 18px
  lg: 28px
  xl: 42px
  full: 980px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 22px
  lg: 44px
  xl: 80px
  gutter: 22px
  margin-mobile: 22px
  margin-desktop: 200px
---

## Brand & Style

Aperture is a minimalist, declarative design system focused on the product. It relies on generous spacing and value contrast rather than lines and color to create hierarchy.

**Key Principles:**
- **Cinematic.** Dark stages invert to `--void #08090B` with white display type.
- **Unadorned.** Claims are stated as measured facts in mono type. No exclamation marks, no hype.
- **Generous Space.** The contrast between wide marketing sections (110–200px) and tight interface padding (16–22px) is the strongest signal of the style.

## Colors

Value, not hue, does the work.

- **Near-whites:** Five near-whites cover every surface.
- **Inks:** Six inks cover every piece of type. Ink-900 `#121417` is intentionally not pure black.
- **Accent:** Exactly one accent (`#0A66FF`) is reserved for links, focus rings, and the single primary CTA. It is never used as a fill for decoration.
- **Dark stages:** Invert to `#08090B` with white display type.

## Typography

One grotesque for everything, one mono for specifications.

- **Sans:** Inter.
- **Mono:** IBM Plex Mono. Used for specs, numeral data.
- **Weights:** 300 to 700. Display is never below 500.

## Layout & Spacing

- **Scale:** 4, 8, 12, 16, 22, 32, 44, 60, 80, 110, 148, 200.
- **Gutter:** 22px.
- **Grids:** 3-up on desktop for products, 4-up for thumbnails.

## Elevation & Depth

- **Hairlines:** A 1px `#DCDFE3` hairline does the work borders usually do.
- **Shadows:** Almost absent. `--shadow-card` is barely perceptible.
- **Separation:** Comes from a mist fill against white, not from a shadow.

## Shapes

- Radii: 8, 12, 18, 28, 42px, plus a 980px pill.
- Buttons and chips are always full pills.
- Cards are generous (28px).

## Motion

Long and decelerating.
- Hover states shift a fill exactly one step (`--mist` -> `--fog`) or lift a card 2px.
- Links underline on hover. Focus is a 2px accent ring.
