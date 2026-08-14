/**
 * Pill button. One primary per view; everything else is secondary, outline or ghost.
 * @startingPoint section="Core" subtitle="Pill buttons in five skins and three sizes" viewport="700x220"
 */
export interface ButtonProps {
  /** primary = accent fill (the single CTA). secondary = grey fill. outline = hairline. inverse = white on dark stages. ghost = inline text link with no box. */
  variant?: "primary" | "secondary" | "outline" | "inverse" | "ghost";
  /** sm 32px, md 44px, lg 54px. */
  size?: "sm" | "md" | "lg";
  disabled?: boolean;
  fullWidth?: boolean;
  /** Lucide icon name shown before the label. */
  icon?: string;
  /** Lucide icon name shown after the label — usually "chevron-right". */
  iconRight?: string;
  /** Renders an <a> instead of a <button>. */
  href?: string;
  onClick?: (e: React.MouseEvent) => void;
  children?: React.ReactNode;
  style?: React.CSSProperties;
}
export function Button(props: ButtonProps): JSX.Element;
