export function Tag({ selected = false, onRemove, onClick, children, style, ...rest }) {
  const [hover, setHover] = React.useState(false);
  return (
    <span
      onClick={onClick}
      onMouseEnter={() => setHover(true)} onMouseLeave={() => setHover(false)}
      style={{
        display: "inline-flex", alignItems: "center", gap: "var(--space-2)", height: 32, padding: "0 14px",
        borderRadius: "var(--radius-pill)",
        background: selected ? "var(--ink-900)" : hover ? "var(--mist)" : "transparent",
        color: selected ? "var(--white)" : "var(--text-primary)",
        boxShadow: selected ? "none" : "var(--shadow-inset-hairline)",
        font: "var(--weight-regular) var(--size-body-sm)/1 var(--font-sans)",
        cursor: onClick ? "pointer" : "default", whiteSpace: "nowrap", flex: "0 0 auto", alignSelf: "flex-start",
        transition: "background var(--dur-fast) var(--ease-out), color var(--dur-fast) var(--ease-out)",
        ...style
      }} {...rest}
    >
      {children}
      {onRemove ? (
        <span onClick={(e) => { e.stopPropagation(); onRemove(e); }} style={{ display: "inline-flex", cursor: "pointer", opacity: 0.6 }}>
          <Icon name="x" size={13} />
        </span>
      ) : null}
    </span>
  );
}
