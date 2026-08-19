export function Dialog({ open = false, title, description, onClose, actions, children, width = 480, style, ...rest }) {
  if (!open) return null;
  return (
    <div onClick={onClose} style={{
      position: "fixed", inset: 0, zIndex: 400, background: "var(--surface-scrim)",
      backdropFilter: "blur(4px)", display: "flex", alignItems: "center", justifyContent: "center",
      padding: "var(--space-6)", animation: "none"
    }}>
      <div onClick={(e) => e.stopPropagation()} style={{
        width, maxWidth: "100%", background: "var(--surface-card)", borderRadius: "var(--radius-lg)",
        boxShadow: "var(--shadow-modal)", padding: "var(--space-7)",
        display: "flex", flexDirection: "column", gap: "var(--space-5)", ...style
      }} {...rest}>
        <div style={{ display: "flex", flexDirection: "column", gap: "var(--space-2)" }}>
          {title ? <h3 style={{ font: "var(--weight-semibold) var(--size-title)/var(--leading-snug) var(--font-sans)", letterSpacing: "var(--tracking-tight)" }}>{title}</h3> : null}
          {description ? <p style={{ font: "var(--text-copy)", color: "var(--text-secondary)" }}>{description}</p> : null}
        </div>
        {children}
        <div style={{ display: "flex", justifyContent: "flex-end", gap: "var(--space-3)" }}>{actions}</div>
      </div>
    </div>
  );
}
