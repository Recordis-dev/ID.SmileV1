/** Thin-stroke Lucide glyph, sized and coloured from the surrounding text. */
export interface IconProps {
  /** Lucide icon name, e.g. "chevron-right", "search", "shopping-bag". */
  name: string;
  /** Box size in px. 16 in dense UI, 18 inline with body copy, 24 in nav. */
  size?: number;
  /** Stroke width. Keep 1.5 to match the hairline system; never above 2. */
  stroke?: number;
  color?: string;
  style?: React.CSSProperties;
}
export function Icon(props: IconProps): JSX.Element;
