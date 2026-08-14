/** Single-choice control; the ring fills with a 6px accent inset when selected. */
export interface RadioProps {
  checked?: boolean;
  onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
  label?: string;
  description?: string;
  name?: string;
  disabled?: boolean;
  style?: React.CSSProperties;
}
export function Radio(props: RadioProps): JSX.Element;
