export function Compare({ onNavigate }) {
  const models = [
    { name: "Halo", price: "From $349", tone: "light" },
    { name: "Halo Pro", price: "From $549", tone: "dark" },
    { name: "Studio", price: "From $1,299", tone: "light" }
  ];
  const rows = [
    ["Driver", ["40 mm", "40 mm", "50 mm"]],
    ["Playback", ["38 h", "44 h", "Wired"]],
    ["Weight", ["142 g", "158 g", "310 g"]],
    ["Adaptive staging", ["—", "Yes", "Yes"]],
    ["Finishes", ["3", "3", "1"]]
  ];
  return (
    <Section tone="light">
      <div style={{ textAlign: "center", display: "flex", flexDirection: "column", gap: "var(--space-3)", marginBottom: "var(--space-8)" }}>
        <Eyebrow>Compare</Eyebrow>
        <h1 style={{ font: "var(--text-h1)", letterSpacing: "var(--tracking-display)" }}>Which one is yours?</h1>
      </div>
      <div style={{ display: "grid", gridTemplateColumns: "160px repeat(3, 1fr)", gap: "var(--space-5)" }}>
        <div></div>
        {models.map((m) => (
          <div key={m.name} style={{ display: "flex", flexDirection: "column", gap: "var(--space-3)", textAlign: "center", alignItems: "center" }}>
            <Stage tone={m.tone} height={180} radius="var(--radius-lg)" style={{ width: "100%" }} />
            <span style={{ font: "var(--weight-semibold) var(--size-title)/1.2 var(--font-sans)", letterSpacing: "var(--tracking-tight)" }}>{m.name}</span>
            <span style={{ font: "var(--text-spec)" }}>{m.price}</span>
            <Button variant="secondary" size="sm" onClick={() => onNavigate("Halo")}>Select</Button>
          </div>
        ))}
      </div>
      <div style={{ marginTop: "var(--space-7)" }}>
        {rows.map(([label, values]) => (
          <div key={label} style={{ display: "grid", gridTemplateColumns: "160px repeat(3, 1fr)", gap: "var(--space-5)",
            padding: "var(--space-4) 0", borderTop: "var(--hairline)" }}>
            <span style={{ font: "var(--text-small)", color: "var(--text-tertiary)" }}>{label}</span>
            {values.map((v, i) => <span key={i} style={{ font: "var(--text-spec)", textAlign: "center" }}>{v}</span>)}
          </div>
        ))}
      </div>
    </Section>
  );
}
