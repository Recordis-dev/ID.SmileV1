export function Tabs({ items = [], active, onSelect, variant = "underline", style, ...rest }) {
  const seg = variant === "segmented";
  return (
    <div style={{
      display: "inline-flex", alignItems: "center", gap: seg ? 4 : "var(--space-6)",
      padding: seg ? 4 : 0, background: seg ? "var(--mist)" : "transparent",
      borderRadius: seg ? "var(--radius-pill)" : 0,
      borderBottom: seg ? "none" : "1px solid var(--border-hairline)", ...style
    }} {...rest}>
      {items.map((it) => {
        const on = it === active;
        return (
          <button key={it} onClick={() => onSelect && onSelect(it)}
            style={{
              border: "none", cursor: "pointer", background: seg && on ? "var(--white)" : "transparent",
              borderRadius: seg ? "var(--radius-pill)" : 0,
              padding: seg ? "8px 18px" : "0 0 12px",
              boxShadow: seg && on ? "0 1px 3px rgba(18,20,23,0.10)" : "none",
              font: (on ? "var(--weight-medium) " : "var(--weight-regular) ") + "var(--size-body-sm)/1 var(--font-sans)",
              color: on ? "var(--text-primary)" : "var(--text-tertiary)",
              borderBottom: seg ? "none" : on ? "2px solid var(--ink-900)" : "2px solid transparent",
              marginBottom: seg ? 0 : -1,
              transition: "color var(--dur-fast) var(--ease-out)"
            }}
          >{it}</button>
        );
      })}
    </div>
  );
}
