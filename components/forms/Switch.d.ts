/** Immediate-effect toggle. 50x30 track, positive green when on. */
export interface SwitchProps {
  checked?: boolean;
  onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
  label?: string;
  disabled?: boolean;
  style?: React.CSSProperties;
}
export function Switch(props: SwitchProps): JSX.Element;
