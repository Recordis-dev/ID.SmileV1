export function Product({ onAdd, onNavigate }) {
  const finishes = ["Graphite", "Silver", "Bone"];
  const models = ["Halo", "Halo Pro"];
  const [finish, setFinish] = React.useState("Graphite");
  const [model, setModel] = React.useState("Halo");
  const [tab, setTab] = React.useState("Overview");
  const price = model === "Halo" ? "$349" : "$549";
  const specs = [["Driver", "40 mm"], ["Weight", "142 g"], ["Playback", "38 h"], ["Charging", "USB-C"], ["Bluetooth", "5.4"], ["Part no.", "A2XKQ-04"]];

  return (
    <div>
      <Section tone="light" pad="var(--space-7)">
        <Tabs items={["Overview", "Specs", "Compare"]} active={tab}
          onSelect={(t) => (t === "Compare" ? onNavigate("Compare") : setTab(t))} style={{ display: "flex", width: "100%" }} />
      </Section>

      {tab === "Overview" ? (
        <Section tone="light" pad="0 var(--space-10)">
          <div style={{ display: "grid", gridTemplateColumns: "1.35fr 1fr", gap: "var(--space-8)", alignItems: "start" }}>
            <div style={{ display: "flex", flexDirection: "column", gap: "var(--space-3)" }}>
              <Stage tone="light" height={460} label="product photography · placeholder" />
              <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: "var(--space-3)" }}>
                {[0, 1, 2, 3].map((i) => <Stage key={i} tone={i % 2 ? "dark" : "light"} height={92} radius="var(--radius-md)" />)}
              </div>
            </div>
            <div style={{ display: "flex", flexDirection: "column", gap: "var(--space-5)", paddingTop: "var(--space-2)" }}>
              <Badge tone="accent">New</Badge>
              <h1 style={{ font: "var(--text-h1)", letterSpacing: "var(--tracking-display)" }}>{model}</h1>
              <p style={{ font: "var(--text-lead)", color: "var(--text-secondary)" }}>
                Over-ear, adaptive, and quiet enough to forget you are wearing it.
              </p>
              <div style={{ display: "flex", flexDirection: "column", gap: "var(--space-3)" }}>
                <span style={{ font: "var(--weight-medium) var(--size-caption)/1 var(--font-sans)", color: "var(--text-secondary)" }}>Model</span>
                <div style={{ display: "flex", gap: "var(--space-2)" }}>
                  {models.map((s) => <Tag key={s} selected={model === s} onClick={() => setModel(s)}>{s}</Tag>)}
                </div>
              </div>
              <div style={{ display: "flex", flexDirection: "column", gap: "var(--space-3)" }}>
                <span style={{ font: "var(--weight-medium) var(--size-caption)/1 var(--font-sans)", color: "var(--text-secondary)" }}>Finish</span>
                <div style={{ display: "flex", gap: "var(--space-2)" }}>
                  {finishes.map((s) => <Tag key={s} selected={finish === s} onClick={() => setFinish(s)}>{s}</Tag>)}
                </div>
              </div>
              <div style={{ paddingTop: "var(--space-4)", borderTop: "var(--hairline)", display: "flex", flexDirection: "column", gap: "var(--space-4)" }}>
                <div style={{ display: "flex", alignItems: "baseline", gap: "var(--space-3)" }}>
                  <span style={{ font: "var(--weight-semibold) var(--size-title)/1 var(--font-sans)", letterSpacing: "var(--tracking-tight)" }}>{price}</span>
                  <span style={{ font: "var(--text-legal)", color: "var(--text-tertiary)" }}>or $29.08/mo. for 12 mo.</span>
                </div>
                <Button size="lg" fullWidth onClick={() => onAdd(model + " · " + finish)}>Add to bag</Button>
                <span style={{ font: "var(--text-legal)", color: "var(--text-tertiary)", display: "flex", alignItems: "center", gap: 8 }}>
                  <Icon name="truck" size={14} color="var(--text-tertiary)" /> Free delivery, arrives Thursday
                </span>
              </div>
            </div>
          </div>
        </Section>
      ) : (
        <Section tone="light" pad="0 var(--space-10)" width="var(--container)">
          <h2 style={{ font: "var(--text-h3)", letterSpacing: "var(--tracking-tight)", marginBottom: "var(--space-5)" }}>Specifications</h2>
          <div>
            {specs.map(([k, v]) => (
              <div key={k} style={{ display: "flex", justifyContent: "space-between", padding: "var(--space-4) 2px", borderBottom: "var(--hairline)" }}>
                <span style={{ font: "var(--text-copy)", color: "var(--text-secondary)" }}>{k}</span>
                <span style={{ font: "var(--text-spec)" }}>{v}</span>
              </div>
            ))}
          </div>
        </Section>
      )}
    </div>
  );
}
