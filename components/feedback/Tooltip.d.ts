/** Small ink label on hover. Explains an icon; never holds essential copy. */
export interface TooltipProps {
  label: string;
  placement?: "top" | "bottom" | "left" | "right";
  children?: React.ReactNode;
  style?: React.CSSProperties;
}
export function Tooltip(props: TooltipProps): JSX.Element;
