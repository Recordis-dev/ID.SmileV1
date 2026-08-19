export function Card({ tone = "light", interactive = false, padding = "var(--space-7)", radius = "var(--radius-xl)", children, style, ...rest }) {
  const [hover, setHover] = React.useState(false);
  const tones = {
    light:   { background: "var(--surface-card)", color: "var(--text-primary)", boxShadow: "var(--shadow-card)" },
    subtle:  { background: "var(--surface-subtle)", color: "var(--text-primary)", boxShadow: "none" },
    hairline:{ background: "var(--white)", color: "var(--text-primary)", boxShadow: "var(--shadow-inset-hairline)" },
    dark:    { background: "var(--surface-inverse-card)", color: "var(--text-inverse)", boxShadow: "none" }
  }[tone];
  return (
    <div
      onMouseEnter={() => setHover(true)} onMouseLeave={() => setHover(false)}
      style={{
        padding, borderRadius: radius, overflow: "hidden",
        transform: interactive && hover ? "translateY(-2px)" : "translateY(0)",
        transition: "transform var(--dur-base) var(--ease-out), box-shadow var(--dur-base) var(--ease-out)",
        ...tones,
        boxShadow: interactive && hover ? "var(--shadow-raise)" : tones.boxShadow,
        ...style
      }} {...rest}
    >{children}</div>
  );
}
