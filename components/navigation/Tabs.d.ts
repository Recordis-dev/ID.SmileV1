/** In-page section switch: hairline underline, or a segmented pill for two to four short options. */
export interface TabsProps {
  items?: string[];
  active?: string;
  onSelect?: (item: string) => void;
  variant?: "underline" | "segmented";
  style?: React.CSSProperties;
}
export function Tabs(props: TabsProps): JSX.Element;
