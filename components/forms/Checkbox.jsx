export function Checkbox({ checked = false, onChange, label, description, disabled, style, ...rest }) {
  return (
    <label style={{ display: "flex", gap: "var(--space-3)", alignItems: description ? "flex-start" : "center",
      cursor: disabled ? "default" : "pointer", opacity: disabled ? 0.4 : 1, ...style }}>
      <input type="checkbox" checked={checked} onChange={onChange} disabled={disabled}
        style={{ position: "absolute", opacity: 0, width: 0, height: 0 }} {...rest} />
      <span style={{
        width: 20, height: 20, flex: "0 0 auto", borderRadius: 6, marginTop: description ? 2 : 0,
        display: "inline-flex", alignItems: "center", justifyContent: "center",
        background: checked ? "var(--accent)" : "var(--white)",
        boxShadow: checked ? "none" : "var(--shadow-inset-hairline)",
        transition: "background var(--dur-fast) var(--ease-out)"
      }}>{checked ? <Icon name="check" size={13} stroke={2.5} color="var(--white)" /> : null}</span>
      <span style={{ display: "flex", flexDirection: "column", gap: 2 }}>
        {label ? <span style={{ font: "var(--text-copy)" }}>{label}</span> : null}
        {description ? <span style={{ font: "var(--text-small)", color: "var(--text-tertiary)" }}>{description}</span> : null}
      </span>
    </label>
  );
}
