/**
 * Slim 48px translucent global bar with blur; the product's only persistent chrome.
 * @startingPoint section="Navigation" subtitle="48px translucent global bar" viewport="700x150"
 */
export interface NavProps {
  /** Wordmark text — the system ships no logo file, so the brand name is set in type. */
  brand?: string;
  items?: string[];
  active?: string;
  onSelect?: (item: string) => void;
  tone?: "light" | "dark";
  /** Right-aligned icons, usually <Icon name="search" /> and <Icon name="shopping-bag" />. */
  actions?: React.ReactNode;
  style?: React.CSSProperties;
}
export function Nav(props: NavProps): JSX.Element;
