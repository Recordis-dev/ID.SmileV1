/* Shared marketing furniture for the Aperture web kit. */

export function Stage({ tone = "dark", height = 520, label, radius = "var(--radius-2xl)", children, style }) {
  const bg = tone === "dark"
    ? "radial-gradient(120% 90% at 50% 6%, #2A2F36 0%, #0D0F12 60%, #08090B 100%)"
    : "radial-gradient(120% 90% at 50% 8%, #FFFFFF 0%, #EFF1F4 68%, #E4E7EB 100%)";
  return (
    <div style={{ position: "relative", height, borderRadius: radius, overflow: "hidden", background: bg,
      display: "flex", alignItems: "center", justifyContent: "center", ...style }}>
      {children}
      {label ? (
        <span style={{ position: "absolute", bottom: 18, left: 22,
          font: "var(--text-spec)", color: tone === "dark" ? "rgba(255,255,255,0.34)" : "var(--text-tertiary)" }}>
          {label}
        </span>
      ) : null}
    </div>
  );
}

export function Eyebrow({ children, tone = "light" }) {
  return (
    <span style={{ font: "var(--weight-medium) var(--size-micro)/1 var(--font-sans)",
      letterSpacing: "var(--tracking-caps)", textTransform: "uppercase",
      color: tone === "dark" ? "var(--text-inverse-secondary)" : "var(--text-tertiary)" }}>{children}</span>
  );
}

export function Section({ tone = "light", pad = "var(--space-10)", width = "var(--container-wide)", children, style }) {
  return (
    <section style={{ background: tone === "dark" ? "var(--void)" : tone === "subtle" ? "var(--surface-subtle)" : "var(--white)",
      color: tone === "dark" ? "var(--text-inverse)" : "var(--text-primary)", paddingBlock: pad, paddingInline: "var(--gutter)", ...style }}>
      <div style={{ maxWidth: width, margin: "0 auto" }}>{children}</div>
    </section>
  );
}

export function Footer() {
  const cols = [
    ["Shop", ["Halo", "Halo Pro", "Studio", "Accessories"]],
    ["Account", ["Your orders", "Saved items", "Trade in"]],
    ["Support", ["Manuals", "Repair", "Contact"]],
    ["Aperture", ["Newsroom", "Careers", "Sustainability"]]
  ];
  return (
    <footer style={{ background: "var(--surface-subtle)", padding: "var(--space-8) var(--gutter) var(--space-6)" }}>
      <div style={{ maxWidth: "var(--container-wide)", margin: "0 auto" }}>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: "var(--space-6)" }}>
          {cols.map(([head, links]) => (
            <div key={head} style={{ display: "flex", flexDirection: "column", gap: "var(--space-3)" }}>
              <span style={{ font: "var(--weight-semibold) var(--size-caption)/1 var(--font-sans)" }}>{head}</span>
              {links.map((l) => (
                <a key={l} href="#" onClick={(e) => e.preventDefault()}
                  style={{ font: "var(--text-legal)", color: "var(--text-secondary)" }}>{l}</a>
              ))}
            </div>
          ))}
        </div>
        <div style={{ marginTop: "var(--space-7)", paddingTop: "var(--space-4)", borderTop: "var(--hairline)",
          display: "flex", justifyContent: "space-between", font: "var(--text-legal)", color: "var(--text-tertiary)" }}>
          <span>Copyright 2026 Aperture. All rights reserved.</span>
          <span style={{ display: "flex", gap: "var(--space-5)" }}>
            <a href="#" onClick={(e) => e.preventDefault()} style={{ color: "var(--text-tertiary)" }}>Privacy</a>
            <a href="#" onClick={(e) => e.preventDefault()} style={{ color: "var(--text-tertiary)" }}>Terms</a>
          </span>
        </div>
      </div>
    </footer>
  );
}
