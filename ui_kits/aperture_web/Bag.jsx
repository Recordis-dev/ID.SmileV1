export function Bag({ items, onRemove, onNavigate }) {
  const [ship, setShip] = React.useState("Standard");
  const [gift, setGift] = React.useState(false);
  const [confirm, setConfirm] = React.useState(null);
  const subtotal = items.length * 349;
  const total = (subtotal + 28.75 + (ship === "Express" ? 12 : 0)).toFixed(2);

  return (
    <Section tone="light" width="var(--container)">
      <h1 style={{ font: "var(--text-h1)", letterSpacing: "var(--tracking-display)", marginBottom: "var(--space-7)" }}>
        {items.length ? "Your bag." : "Your bag is empty."}
      </h1>

      {items.length === 0 ? (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "flex-start", gap: "var(--space-5)" }}>
          <p style={{ font: "var(--text-lead)", color: "var(--text-secondary)" }}>Start with the line, or compare the three models.</p>
          <Button onClick={() => onNavigate("Halo")}>Shop Halo</Button>
        </div>
      ) : (
        <div style={{ display: "grid", gridTemplateColumns: "1.4fr 1fr", gap: "var(--space-8)", alignItems: "start" }}>
          <div>
            {items.map((it, i) => (
              <div key={i} style={{ display: "flex", gap: "var(--space-5)", padding: "var(--space-5) 0", borderBottom: "var(--hairline)" }}>
                <Stage tone="light" height={110} radius="var(--radius-md)" style={{ width: 140, flex: "0 0 auto" }} />
                <div style={{ flex: 1, display: "flex", flexDirection: "column", gap: 6 }}>
                  <span style={{ font: "var(--weight-medium) var(--size-subtitle)/1.2 var(--font-sans)", letterSpacing: "var(--tracking-tight)" }}>{it}</span>
                  <span style={{ font: "var(--text-small)", color: "var(--text-tertiary)" }}>Arrives Thursday · Free delivery</span>
                  <Button variant="ghost" style={{ alignSelf: "flex-start", font: "var(--weight-regular) var(--size-caption)/1 var(--font-sans)" }}
                    onClick={() => setConfirm(i)}>Remove</Button>
                </div>
                <span style={{ font: "var(--text-spec)" }}>$349.00</span>
              </div>
            ))}
            <div style={{ display: "flex", flexDirection: "column", gap: "var(--space-4)", paddingTop: "var(--space-6)" }}>
              <span style={{ font: "var(--weight-medium) var(--size-caption)/1 var(--font-sans)", color: "var(--text-secondary)" }}>Delivery</span>
              {[["Standard", "Free, 3-5 days"], ["Express", "$12, tomorrow"]].map(([s, d]) => (
                <Radio key={s} name="ship" checked={ship === s} onChange={() => setShip(s)} label={s} description={d} />
              ))}
              <Checkbox checked={gift} onChange={() => setGift(!gift)} label="This is a gift" description="Adds a note, hides the price" />
            </div>
          </div>

          <Card tone="subtle" padding="var(--space-6)" radius="var(--radius-lg)" style={{ display: "flex", flexDirection: "column", gap: "var(--space-4)" }}>
            <span style={{ font: "var(--weight-semibold) var(--size-subtitle)/1 var(--font-sans)", letterSpacing: "var(--tracking-tight)" }}>Summary</span>
            {[["Subtotal", "$" + subtotal + ".00"], ["Delivery", ship === "Express" ? "$12.00" : "Free"], ["Tax", "$28.75"]].map(([k, v]) => (
              <div key={k} style={{ display: "flex", justifyContent: "space-between", font: "var(--text-copy)", color: "var(--text-secondary)" }}>
                <span>{k}</span><span style={{ font: "var(--text-spec)", color: "var(--text-primary)" }}>{v}</span>
              </div>
            ))}
            <div style={{ display: "flex", justifyContent: "space-between", paddingTop: "var(--space-4)", borderTop: "var(--hairline)" }}>
              <span style={{ font: "var(--weight-semibold) var(--size-subtitle)/1 var(--font-sans)" }}>Total</span>
              <span style={{ font: "var(--weight-semibold) var(--size-subtitle)/1 var(--font-sans)" }}>{"$" + total}</span>
            </div>
            <Input label="Email" placeholder="you@studio.com" />
            <Select label="Country" options={["United States", "Canada", "United Kingdom", "Germany", "Japan"]} />
            <Button size="lg" fullWidth>Check out</Button>
            <span style={{ font: "var(--text-legal)", color: "var(--text-tertiary)", textAlign: "center" }}>Free returns within 14 days.</span>
          </Card>
        </div>
      )}

      <Dialog open={confirm !== null} title="Remove from bag?" description="You can add it back at any time."
        onClose={() => setConfirm(null)}
        actions={<><Button variant="secondary" onClick={() => setConfirm(null)}>Keep</Button>
          <Button onClick={() => { onRemove(confirm); setConfirm(null); }}>Remove</Button></>} />
    </Section>
  );
}
