/** Single-line text field with optional label, leading icon, hint and error. */
export interface InputProps {
  label?: string;
  hint?: string;
  /** Replaces the hint and switches the border to critical. */
  error?: string;
  type?: string;
  value?: string;
  onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
  placeholder?: string;
  disabled?: boolean;
  /** Lucide icon name shown inside, before the text. */
  icon?: string;
  style?: React.CSSProperties;
}
export function Input(props: InputProps): JSX.Element;
