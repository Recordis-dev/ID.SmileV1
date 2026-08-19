export function Input({ label, hint, error, type = "text", value, onChange, placeholder, disabled, icon, style, ...rest }) {
  const [focus, setFocus] = React.useState(false);
  return (
    <label style={{ display: "flex", flexDirection: "column", gap: "var(--space-2)", ...style }}>
      {label ? <span style={{ font: "var(--weight-medium) var(--size-caption)/1.2 var(--font-sans)", color: "var(--text-secondary)" }}>{label}</span> : null}
      <span style={{
        display: "flex", alignItems: "center", gap: "var(--space-2)",
        height: "var(--control-h)", padding: "0 16px", background: disabled ? "var(--mist)" : "var(--white)",
        borderRadius: "var(--radius-md)",
        boxShadow: error ? "inset 0 0 0 1px var(--critical)" : focus ? "inset 0 0 0 2px var(--accent)" : "var(--shadow-inset-hairline)",
        transition: "box-shadow var(--dur-fast) var(--ease-out)"
      }}>
        {icon ? <Icon name={icon} size={16} color="var(--text-tertiary)" /> : null}
        <input
          type={type} value={value} onChange={onChange} placeholder={placeholder} disabled={disabled}
          onFocus={() => setFocus(true)} onBlur={() => setFocus(false)}
          style={{ flex: 1, minWidth: 0, border: "none", outline: "none", background: "transparent",
            font: "var(--text-copy)", letterSpacing: "var(--tracking-normal)", color: "var(--text-primary)" }}
          {...rest}
        />
      </span>
      {error ? <span style={{ font: "var(--text-legal)", color: "var(--critical)" }}>{error}</span>
        : hint ? <span style={{ font: "var(--text-legal)", color: "var(--text-tertiary)" }}>{hint}</span> : null}
    </label>
  );
}
