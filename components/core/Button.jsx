export function Button({
  variant = "primary", size = "md", disabled = false, fullWidth = false,
  icon, iconRight, href, onClick, children, style, ...rest
}) {
  const [hover, setHover] = React.useState(false);
  const [press, setPress] = React.useState(false);
  const height = { sm: "var(--control-h-sm)", md: "var(--control-h)", lg: "var(--control-h-lg)" }[size];
  const pad = { sm: "0 14px", md: "0 22px", lg: "0 30px" }[size];
  const font = { sm: "var(--size-caption)", md: "var(--size-body-sm)", lg: "var(--size-body)" }[size];

  const skins = {
    primary: { background: hover ? "var(--accent-hover)" : "var(--accent)", color: "var(--white)", boxShadow: "none" },
    secondary: { background: hover ? "var(--fog)" : "var(--mist)", color: "var(--text-primary)" },
    outline: { background: hover ? "var(--mist)" : "transparent", color: "var(--text-primary)", boxShadow: "var(--shadow-inset-hairline)" },
    inverse: { background: hover ? "var(--white)" : "rgba(255,255,255,0.92)", color: "var(--ink-900)" },
    ghost: { background: "transparent", color: hover ? "var(--accent-hover)" : "var(--accent)", padding: 0, height: "auto" }
  }[variant];

  const s = {
    display: "inline-flex", alignItems: "center", justifyContent: "center", gap: "var(--space-2)",
    height, padding: pad, width: fullWidth ? "100%" : "auto",
    font: "var(--weight-medium) " + font + "/1 var(--font-sans)",
    letterSpacing: "var(--tracking-normal)",
    borderRadius: "var(--radius-pill)", border: "none", cursor: disabled ? "default" : "pointer",
    textDecoration: "none", whiteSpace: "nowrap",
    opacity: disabled ? 0.36 : 1,
    transform: press && !disabled ? "scale(0.97)" : "scale(1)",
    transition: "background var(--dur-fast) var(--ease-out), color var(--dur-fast) var(--ease-out), transform var(--dur-fast) var(--ease-out)",
    ...skins, ...style
  };

  const Tag = href ? "a" : "button";
  return (
    <Tag
      href={href} onClick={disabled ? undefined : onClick} disabled={!href ? disabled : undefined}
      onMouseEnter={() => setHover(true)} onMouseLeave={() => { setHover(false); setPress(false); }}
      onMouseDown={() => setPress(true)} onMouseUp={() => setPress(false)}
      style={s} {...rest}
    >
      {icon ? <Icon name={icon} size={size === "sm" ? 14 : 16} /> : null}
      {children}
      {iconRight ? <Icon name={iconRight} size={size === "sm" ? 14 : 16} /> : null}
    </Tag>
  );
}
