export function Select({ label, value, onChange, options = [], disabled, style, ...rest }) {
  const [focus, setFocus] = React.useState(false);
  return (
    <label style={{ display: "flex", flexDirection: "column", gap: "var(--space-2)", ...style }}>
      {label ? <span style={{ font: "var(--weight-medium) var(--size-caption)/1.2 var(--font-sans)", color: "var(--text-secondary)" }}>{label}</span> : null}
      <span style={{ position: "relative", display: "flex", alignItems: "center" }}>
        <select
          value={value} onChange={onChange} disabled={disabled}
          onFocus={() => setFocus(true)} onBlur={() => setFocus(false)}
          style={{
            appearance: "none", width: "100%", height: "var(--control-h)", padding: "0 42px 0 16px",
            background: disabled ? "var(--mist)" : "var(--white)", border: "none",
            borderRadius: "var(--radius-md)",
            boxShadow: focus ? "inset 0 0 0 2px var(--accent)" : "var(--shadow-inset-hairline)",
            font: "var(--text-copy)", color: "var(--text-primary)", outline: "none", cursor: "pointer",
            transition: "box-shadow var(--dur-fast) var(--ease-out)"
          }}
          {...rest}
        >
          {options.map((o) => <option key={o.value ?? o} value={o.value ?? o}>{o.label ?? o}</option>)}
        </select>
        <span style={{ position: "absolute", right: 14, pointerEvents: "none" }}>
          <Icon name="chevron-down" size={16} color="var(--text-tertiary)" />
        </span>
      </span>
    </label>
  );
}
