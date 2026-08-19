export function Toast({ message, tone = "neutral", icon, onDismiss, style, ...rest }) {
  const tones = {
    neutral:  { background: "var(--ink-900)", color: "var(--white)" },
    positive: { background: "var(--positive)", color: "var(--white)" },
    critical: { background: "var(--critical)", color: "var(--white)" }
  }[tone];
  return (
    <div style={{
      display: "inline-flex", alignItems: "center", gap: "var(--space-3)",
      padding: "12px 18px", borderRadius: "var(--radius-pill)", boxShadow: "var(--shadow-raise)",
      font: "var(--weight-medium) var(--size-body-sm)/1.2 var(--font-sans)", ...tones, ...style
    }} {...rest}>
      {icon ? <Icon name={icon} size={16} /> : null}
      <span>{message}</span>
      {onDismiss ? (
        <span onClick={onDismiss} style={{ cursor: "pointer", opacity: 0.7, display: "inline-flex" }}>
          <Icon name="x" size={14} />
        </span>
      ) : null}
    </div>
  );
}
