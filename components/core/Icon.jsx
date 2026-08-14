export function Icon({ name, size = 18, stroke = 1.5, color = "currentColor", style, ...rest }) {
  const ref = React.useRef(null);
  React.useEffect(() => {
    if (window.lucide && ref.current) window.lucide.createIcons({ nameAttr: "data-lucide", root: ref.current });
  }, [name, size, stroke]);
  return (
    <span
      ref={ref}
      style={{ display: "inline-flex", alignItems: "center", justifyContent: "center", width: size, height: size, color, flex: "0 0 auto", ...style }}
      {...rest}
    >
      <i data-lucide={name} width={size} height={size} stroke-width={stroke}></i>
    </span>
  );
}
