export function Badge({ tone = "neutral", children, style, ...rest }) {
  const tones = {
    neutral:  { background: "var(--mist)", color: "var(--text-secondary)" },
    accent:   { background: "var(--accent-soft)", color: "var(--accent-press)" },
    positive: { background: "var(--positive-soft)", color: "var(--positive)" },
    caution:  { background: "var(--caution-soft)", color: "var(--caution)" },
    critical: { background: "var(--critical-soft)", color: "var(--critical)" },
    inverse:  { background: "rgba(255,255,255,0.12)", color: "var(--white)" }
  }[tone];
  return (
    <span style={{
      display: "inline-flex", alignItems: "center", alignSelf: "flex-start", flex: "0 0 auto", height: 22, padding: "0 10px",
      borderRadius: "var(--radius-pill)", font: "var(--weight-medium) var(--size-micro)/1 var(--font-sans)",
      letterSpacing: "var(--tracking-wide)", textTransform: "uppercase", whiteSpace: "nowrap", ...tones, ...style
    }} {...rest}>{children}</span>
  );
}
