/** Centred modal over a blurred scrim. For decisions only — never for content that could be a page. */
export interface DialogProps {
  open?: boolean;
  title?: string;
  description?: string;
  onClose?: () => void;
  /** Buttons, right-aligned: secondary first, primary last. */
  actions?: React.ReactNode;
  children?: React.ReactNode;
  width?: number;
  style?: React.CSSProperties;
}
export function Dialog(props: DialogProps): JSX.Element | null;
