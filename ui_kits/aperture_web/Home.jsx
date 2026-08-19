export function Home({ onNavigate }) {
  const products = [
    { name: "Halo", line: "Over-ear, 40 mm", price: "From $349", tone: "dark" },
    { name: "Halo Pro", line: "Adaptive staging", price: "From $549", tone: "light" },
    { name: "Studio", line: "Reference monitor", price: "From $1,299", tone: "dark" }
  ];
  return (
    <div>
      <Section tone="dark" pad="var(--space-8)">
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: "var(--space-5)", textAlign: "center" }}>
          <Eyebrow tone="dark">New</Eyebrow>
          <h1 style={{ font: "var(--weight-semibold) var(--size-display-xl)/var(--leading-display) var(--font-sans)",
            letterSpacing: "var(--tracking-display)" }}>Halo</h1>
          <p style={{ font: "var(--text-lead)", color: "var(--text-inverse-secondary)", maxWidth: 520 }}>
            Sound that holds its place in the room. Machined aluminium, 38 hours, nothing you have to think about.
          </p>
          <div style={{ display: "flex", gap: "var(--space-5)", marginTop: "var(--space-2)" }}>
            <Button onClick={() => onNavigate("Halo")}>Buy</Button>
            <Button variant="ghost" iconRight="chevron-right" onClick={() => onNavigate("Halo")}>Learn more</Button>
          </div>
          <Stage tone="dark" height={380} label="hero photography · placeholder" style={{ width: "100%", marginTop: "var(--space-6)" }} />
        </div>
      </Section>

      <Section tone="light">
        <div style={{ display: "flex", alignItems: "flex-end", justifyContent: "space-between", marginBottom: "var(--space-6)" }}>
          <h2 style={{ font: "var(--text-h2)", letterSpacing: "var(--tracking-tight)" }}>The line.</h2>
          <Button variant="ghost" iconRight="chevron-right" onClick={() => onNavigate("Compare")}>Compare all models</Button>
        </div>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: "var(--space-5)" }}>
          {products.map((p) => (
            <Card key={p.name} tone="subtle" interactive padding="0" onClick={() => onNavigate("Halo")} style={{ cursor: "pointer" }}>
              <Stage tone={p.tone} height={240} radius="0" />
              <div style={{ padding: "var(--space-5)", display: "flex", flexDirection: "column", gap: 6 }}>
                <span style={{ font: "var(--weight-semibold) var(--size-title)/1.2 var(--font-sans)", letterSpacing: "var(--tracking-tight)" }}>{p.name}</span>
                <span style={{ font: "var(--text-small)", color: "var(--text-secondary)" }}>{p.line}</span>
                <span style={{ font: "var(--text-spec)", marginTop: 6 }}>{p.price}</span>
              </div>
            </Card>
          ))}
        </div>
      </Section>

      <Section tone="subtle">
        <div style={{ display: "grid", gridTemplateColumns: "1.1fr 1fr", gap: "var(--space-7)", alignItems: "center" }}>
          <div style={{ display: "flex", flexDirection: "column", gap: "var(--space-4)" }}>
            <Eyebrow>Engineering</Eyebrow>
            <h2 style={{ font: "var(--text-h2)", letterSpacing: "var(--tracking-tight)" }}>Machined from a single billet.</h2>
            <p style={{ font: "var(--text-copy)", color: "var(--text-secondary)", maxWidth: 460 }}>
              One piece of aluminium, cut for eleven hours, then finished by hand. The result is a frame with no seams to rattle and no panels to flex.
            </p>
            <div style={{ display: "flex", gap: "var(--space-7)", marginTop: "var(--space-2)" }}>
              {[["142 g", "each cup"], ["38 h", "playback"], ["40 mm", "driver"]].map(([v, l]) => (
                <div key={l} style={{ display: "flex", flexDirection: "column", gap: 4 }}>
                  <span style={{ font: "var(--weight-semibold) var(--size-title)/1 var(--font-sans)", letterSpacing: "var(--tracking-tight)" }}>{v}</span>
                  <span style={{ font: "var(--text-legal)", color: "var(--text-tertiary)" }}>{l}</span>
                </div>
              ))}
            </div>
          </div>
          <Stage tone="light" height={360} label="detail photography · placeholder" />
        </div>
      </Section>
    </div>
  );
}
