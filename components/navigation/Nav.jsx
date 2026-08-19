export function Nav({ brand = "Aperture", items = [], active, onSelect, tone = "light", actions, style, ...rest }) {
  return (
    <nav style={{
      position: "sticky", top: 0, zIndex: 100, height: 48,
      background: tone === "dark" ? "var(--scrim-chrome-inverse)" : "var(--scrim-chrome)",
      backdropFilter: "var(--blur-chrome)", WebkitBackdropFilter: "var(--blur-chrome)",
      borderBottom: tone === "dark" ? "1px solid var(--border-inverse)" : "1px solid var(--border-hairline)",
      color: tone === "dark" ? "var(--text-inverse)" : "var(--text-primary)", ...style
    }} {...rest}>
      <div style={{ maxWidth: "var(--container-wide)", margin: "0 auto", padding: "0 var(--gutter)",
        height: "100%", display: "flex", alignItems: "center", gap: "var(--space-7)" }}>
        <span style={{ font: "var(--weight-semibold) var(--size-body-sm)/1 var(--font-sans)", letterSpacing: "var(--tracking-tight)" }}>{brand}</span>
        <div style={{ display: "flex", alignItems: "center", gap: "var(--space-6)", flex: 1 }}>
          {items.map((it) => {
            const on = it === active;
            return (
              <a key={it} href="#" onClick={(e) => { e.preventDefault(); onSelect && onSelect(it); }}
                style={{ font: "var(--weight-regular) var(--size-caption)/1 var(--font-sans)",
                  color: "inherit", opacity: on ? 1 : 0.72, textDecoration: "none",
                  transition: "opacity var(--dur-fast) var(--ease-out)" }}
                onMouseEnter={(e) => (e.currentTarget.style.opacity = 1)}
                onMouseLeave={(e) => (e.currentTarget.style.opacity = on ? 1 : 0.72)}
              >{it}</a>
            );
          })}
        </div>
        <div style={{ display: "flex", alignItems: "center", gap: "var(--space-5)", opacity: 0.82 }}>{actions}</div>
      </div>
    </nav>
  );
}
