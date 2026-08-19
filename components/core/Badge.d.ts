/** Tiny uppercase status pill: "New", "In stock", "Backordered". */
export interface BadgeProps {
  tone?: "neutral" | "accent" | "positive" | "caution" | "critical" | "inverse";
  children?: React.ReactNode;
  style?: React.CSSProperties;
}
export function Badge(props: BadgeProps): JSX.Element;
