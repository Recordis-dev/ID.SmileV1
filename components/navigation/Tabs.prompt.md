Switches content within a page; never used for primary navigation (that is `Nav`).

```jsx
<Tabs items={["Overview", "Specs", "Compare"]} active={tab} onSelect={setTab} />
<Tabs variant="segmented" items={["Buy", "Lease"]} active={mode} onSelect={setMode} />
```

Underline variant: 2px ink rule under the active label, inactive labels in tertiary ink. Segmented sits in a mist track with a white thumb.
