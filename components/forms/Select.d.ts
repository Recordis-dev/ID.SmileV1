/** Native select styled to match Input, with a thin chevron. */
export interface SelectOption { value: string; label: string; }
export interface SelectProps {
  label?: string;
  value?: string;
  onChange?: (e: React.ChangeEvent<HTMLSelectElement>) => void;
  /** Strings or {value,label} objects. */
  options?: (SelectOption | string)[];
  disabled?: boolean;
  style?: React.CSSProperties;
}
export function Select(props: SelectProps): JSX.Element;
