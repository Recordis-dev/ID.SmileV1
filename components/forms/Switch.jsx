export function Switch({ checked = false, onChange, label, disabled, style, ...rest }) {
  return (
    <label style={{ display: "inline-flex", alignItems: "center", gap: "var(--space-3)",
      cursor: disabled ? "default" : "pointer", opacity: disabled ? 0.4 : 1, ...style }}>
      <input type="checkbox" role="switch" checked={checked} disabled={disabled}
        onChange={onChange} style={{ position: "absolute", opacity: 0, width: 0, height: 0 }} {...rest} />
      <span style={{
        width: 50, height: 30, borderRadius: "var(--radius-pill)", padding: 3, flex: "0 0 auto",
        background: checked ? "var(--positive)" : "var(--fog)",
        transition: "background var(--dur-base) var(--ease-out)"
      }}>
        <span style={{
          display: "block", width: 24, height: 24, borderRadius: "50%", background: "var(--white)",
          boxShadow: "0 1px 3px rgba(8,9,11,0.22)",
          transform: checked ? "translateX(20px)" : "translateX(0)",
          transition: "transform var(--dur-base) var(--ease-out)"
        }}></span>
      </span>
      {label ? <span style={{ font: "var(--text-copy)" }}>{label}</span> : null}
    </label>
  );
}
