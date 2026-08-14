/** Transient confirmation pill, bottom-centre, auto-dismissing after ~4s. */
export interface ToastProps {
  message: string;
  tone?: "neutral" | "positive" | "critical";
  /** Lucide icon name shown before the message. */
  icon?: string;
  onDismiss?: () => void;
  style?: React.CSSProperties;
}
export function Toast(props: ToastProps): JSX.Element;
