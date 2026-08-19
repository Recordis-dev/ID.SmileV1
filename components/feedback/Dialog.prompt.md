A decision surface: confirm, choose, or stop.

```jsx
<Dialog open={o} title="Remove from bag?" description="You can add it back later."
  onClose={close} actions={<><Button variant="secondary" onClick={close}>Keep</Button><Button onClick={remove}>Remove</Button></>} />
```

18px radius, 60px shadow, blurred scrim. Actions are right-aligned with the primary last. Title is 28px semibold; body is secondary ink.
