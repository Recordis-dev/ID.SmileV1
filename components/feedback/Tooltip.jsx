export function Tooltip({ label, placement = "top", children, style, ...rest }) {
  const [show, setShow] = React.useState(false);
  const pos = {
    top:    { bottom: "calc(100% + 8px)", left: "50%", transform: "translateX(-50%)" },
    bottom: { top: "calc(100% + 8px)", left: "50%", transform: "translateX(-50%)" },
    left:   { right: "calc(100% + 8px)", top: "50%", transform: "translateY(-50%)" },
    right:  { left: "calc(100% + 8px)", top: "50%", transform: "translateY(-50%)" }
  }[placement];
  return (
    <span
      onMouseEnter={() => setShow(true)} onMouseLeave={() => setShow(false)}
      style={{ position: "relative", display: "inline-flex", ...style }} {...rest}
    >
      {children}
      <span style={{
        position: "absolute", ...pos, zIndex: 400, pointerEvents: "none",
        padding: "6px 10px", borderRadius: "var(--radius-sm)", background: "var(--ink-900)",
        color: "var(--white)", font: "var(--text-legal)", whiteSpace: "nowrap",
        opacity: show ? 1 : 0,
        transition: "opacity var(--dur-fast) var(--ease-out)"
      }}>{label}</span>
    </span>
  );
}
