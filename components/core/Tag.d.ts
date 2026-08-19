/** Selectable / removable hairline chip used for filters and configuration choices. */
export interface TagProps {
  selected?: boolean;
  /** Renders a small x; called when it is clicked. */
  onRemove?: (e: React.MouseEvent) => void;
  onClick?: (e: React.MouseEvent) => void;
  children?: React.ReactNode;
  style?: React.CSSProperties;
}
export function Tag(props: TagProps): JSX.Element;
