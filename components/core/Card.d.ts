/**
 * Generously rounded container. Four tones; elevation is near-flat by default.
 * @startingPoint section="Core" subtitle="Card tones: light, subtle, hairline, dark" viewport="700x260"
 */
export interface CardProps {
  tone?: "light" | "subtle" | "hairline" | "dark";
  /** Adds a 2px lift and deeper shadow on hover. Only for cards that navigate. */
  interactive?: boolean;
  padding?: string;
  radius?: string;
  children?: React.ReactNode;
  style?: React.CSSProperties;
}
export function Card(props: CardProps): JSX.Element;
