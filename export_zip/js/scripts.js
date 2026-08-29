class Component extends DCLogic {
  componentDidMount() {
    const els = Array.from(document.querySelectorAll("[data-reveal]"));
    const show = el => {
      el.style.opacity = "1";
      el.style.transform = "none";
      el.removeAttribute("data-reveal");
    };
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (!reduce && els.length) {
      let node = els[0].parentElement, scrollRoot = null, guard = 0;
      while (node && node !== document.documentElement && guard++ < 40) {
        if (node.scrollHeight > node.clientHeight + 40 && getComputedStyle(node).overflowY !== "visible") { scrollRoot = node; break; }
        const next = node.parentElement;
        if (next === node) break;
        node = next;
      }
      const io = new IntersectionObserver(es => es.forEach(e => {
        if (e.isIntersecting) { show(e.target); io.unobserve(e.target); }
      }), { root: scrollRoot, threshold: 0.08 });
      els.forEach((el, i) => {
        el.style.transition = "opacity .65s ease " + Math.min(i % 4, 3) * 70 + "ms, transform .65s cubic-bezier(.2,.7,.3,1) " + Math.min(i % 4, 3) * 70 + "ms";
        el.style.opacity = "0";
        el.style.transform = "translateY(18px)";
        io.observe(el);
      });
      this._io = io;
      // safety net: never leave copy hidden if the observer doesn't fire
      this._t = setTimeout(() => {
        document.querySelectorAll("[data-reveal]").forEach(el => {
          const r = el.getBoundingClientRect();
          if (r.top < (window.innerHeight || 800) + 200) show(el);
        });
      }, 700);
      this._t2 = setTimeout(() => document.querySelectorAll("[data-reveal]").forEach(show), 4000);
    }
    // Instrumentación de intención de contacto (GA4/GTM). transport_type:'beacon'
    // evita perder el evento cuando el móvil salta a la app de WhatsApp.
    this._track = e => {
      const a = e.target.closest && e.target.closest("a[href]");
      if (!a) return;
      const href = a.getAttribute("href") || "";
      let name = null;
      if (href.indexOf("wa.me") > -1) name = "whatsapp_click";
      else if (href.indexOf("tel:") === 0) name = "phone_click";
      else if (href.indexOf("mailto:") === 0) name = "email_click";
      if (!name) return;
      const payload = {
        event: name,
        link_url: href,
        link_section: (a.closest("section") || {}).id || "global",
        link_text: (a.textContent || "").trim().slice(0, 60)
      };
      if (window.dataLayer) window.dataLayer.push(payload);
      if (window.gtag) window.gtag("event", name, Object.assign({ transport_type: "beacon" }, payload));
    };
    document.addEventListener("click", this._track, true);
    const items = Array.from(document.querySelectorAll("details"));
    items.forEach(d => {
      d.addEventListener("toggle", () => {
        const s = d.querySelector("summary > span:last-child");
        if (s) s.textContent = d.open ? "−" : "+";
        if (!d.open || this._closing) return;
        this._closing = true;
        items.forEach(o => { if (o !== d && o.open) o.open = false; });
        this._closing = false;
      });
    });
  }
  componentWillUnmount() {
    if (this._io) this._io.disconnect();
    if (this._track) document.removeEventListener("click", this._track, true);
    clearTimeout(this._t); clearTimeout(this._t2);
  }
  state = { step: 0, answers: [] };

  get questions() {
    return [
      { key: "quien", q: "¿Para quién es el tratamiento?", opts: ["Para mí (adulto)", "Para un adolescente", "Para un niño menor de 12"] },
      { key: "motivo", q: "¿Qué te gustaría corregir?", opts: ["Dientes apiñados o chuecos", "Mordida que no cierra bien", "Aún no lo sé, quiero saber si lo necesito"] },
      { key: "prioridad", q: "¿Qué pesa más en tu decisión?", opts: ["Que casi no se note", "Terminar lo antes posible", "El presupuesto mensual"] }
    ];
  }

  result() {
    const [quien, motivo, prioridad] = this.state.answers;
    if (quien === 2) return {
      title: "Valoración de ortopedia infantil",
      body: "A esta edad lo importante es revisar el crecimiento antes de mover dientes. Una valoración temprana suele evitar extracciones y tratamientos largos más adelante.",
      time: "Revisión desde los 7 años", range: "Valoración $350–$700 MXN",
      tag: "ortodoncia infantil"
    };
    if (prioridad === 0 && motivo !== 1) return {
      title: "Alineadores o brackets estéticos",
      body: "Tu prioridad es la discreción. Los alineadores son casi invisibles si los usas 22 horas al día; si prefieres no depender de eso, los brackets de cerámica dan el mismo resultado sin ser notorios.",
      time: "Duración típica 18–24 meses", range: "Desde $20,000 MXN",
      tag: "opción estética"
    };
    if (prioridad === 2) return {
      title: "Brackets metálicos con plan mensual",
      body: "Es la opción más eficiente por peso: resuelve prácticamente cualquier caso al costo más accesible y no depende de tu constancia diaria. Se puede pagar en mensualidades fijas.",
      time: "Duración típica 18–30 meses", range: "Ref. $15,000–$35,000 MXN",
      tag: "presupuesto mensual"
    };
    if (motivo === 1) return {
      title: "Caso de mordida: requiere diagnóstico",
      body: "Los problemas de mordida se resuelven con mecánica precisa y a veces ortopedia. Necesitamos radiografía y estudio antes de recomendar aparato — cualquier promesa previa sería adivinar.",
      time: "Duración típica 24–30 meses", range: "Se define en valoración",
      tag: "mordida"
    };
    return {
      title: "Brackets: el camino más directo",
      body: "Para apiñamiento y alineación general, los brackets dan control total del movimiento y el resultado más predecible en menos citas de las que imaginas.",
      time: "Duración típica 18–24 meses", range: "Ref. $15,000–$35,000 MXN",
      tag: "alineación"
    };
  }

  pick(i) {
    this.setState(s => ({ step: s.step + 1, answers: s.answers.slice(0, s.step).concat(i) }));
  }

  renderVals() {
    const num = (this.props.whatsappNumber || "5217773773106").replace(/\D/g, "");
    const base = this.props.waMessage || "Hola, me gustaría agendar una valoración de ortodoncia en ID Smile.";
    const qs = this.questions, step = this.state.step, isResult = step >= qs.length;
    const r = isResult ? this.result() : null;
    const detail = isResult
      ? "Hola, hice el orientador en su sitio. Resultado: " + r.title + " (" + r.tag + "). " +
        qs.map((q, i) => q.q + " " + q.opts[this.state.answers[i]]).join(" · ") + ". Quisiera agendar una valoración."
      : base;
    return {
      waUrl: "https://wa.me/" + num + "?text=" + encodeURIComponent(base),
      ninosWaUrl: "https://wa.me/" + num + "?text=" + encodeURIComponent("Hola, quisiera agendar una valoración de ortodoncia infantil para mi hijo/a en ID Smile."),
      quizWaUrl: "https://wa.me/" + num + "?text=" + encodeURIComponent(detail),
      isQuestion: !isResult,
      isResult,
      canGoBack: step > 0 && !isResult,
      stepLabel: isResult ? "Listo" : "Paso " + (step + 1) + " de " + qs.length,
      progressPct: Math.round((Math.min(step, qs.length) / qs.length) * 100) + "%",
      question: isResult ? "" : qs[step].q,
      options: isResult ? [] : qs[step].opts.map((label, i) => ({ label, pick: () => this.pick(i) })),
      back: () => this.setState(s => ({ step: Math.max(0, s.step - 1) })),
      restart: () => this.setState({ step: 0, answers: [] }),
      resultTitle: r ? r.title : "",
      resultBody: r ? r.body : "",
      resultTime: r ? r.time : "",
      resultRange: r ? r.range : "",
      showPrices: this.props.showPrices !== false,
      year: new Date().getFullYear()
    };
  }
}


  // Robust Pure JS Marquee Controller - v3 (Responsive, Mobile, SEO, Scroll-Physics)
  document.addEventListener("DOMContentLoaded", function() {
    const container = document.getElementById("ids-marquee-container");
    const content = document.getElementById("ids-marquee-content");
    if (!container || !content) return;

    content.style.animation = 'none';
    content.style.willChange = 'transform';

    const BASE_SPEED = 0.33;
    let targetSpeed = BASE_SPEED;
    let currentSpeed = BASE_SPEED;
    let currentX = 0;
    let isHovering = false;
    let scrollTimeout;

    function lerp(start, end, amt) {
      return (1 - amt) * start + amt * end;
    }

    function animate() {
      currentSpeed = lerp(currentSpeed, targetSpeed, 0.08);
      if (currentSpeed < 0.01) currentSpeed = 0;

      currentX -= currentSpeed;

      const scrollMax = content.scrollWidth / 2;
      if (currentX <= -scrollMax && scrollMax > 0) {
        currentX += scrollMax;
      }

      content.style.transform = `translate3d(${currentX}px, 0, 0)`;
      requestAnimationFrame(animate);
    }

    setTimeout(() => { requestAnimationFrame(animate); }, 100);

    function handleInteraction(clientX) {
      const rect = container.getBoundingClientRect();
      const centerX = rect.left + rect.width / 2;
      const distFromCenter = Math.abs(clientX - centerX) / (rect.width / 2);

      if (distFromCenter < 0.15) {
        targetSpeed = 0;
      } else {
        targetSpeed = BASE_SPEED + Math.pow(distFromCenter, 1.8) * 5.0;
      }
    }

    container.addEventListener("mouseenter", () => { isHovering = true; });
    container.addEventListener("mouseleave", () => {
      isHovering = false;
      targetSpeed = BASE_SPEED;
    });
    container.addEventListener("mousemove", (e) => {
      if (!isHovering) return;
      handleInteraction(e.clientX);
    });

    container.addEventListener("touchstart", (e) => {
      isHovering = true;
      handleInteraction(e.touches[0].clientX);
    }, {passive: true});

    container.addEventListener("touchmove", (e) => {
      if (!isHovering) return;
      handleInteraction(e.touches[0].clientX);
    }, {passive: true});

    container.addEventListener("touchend", () => {
      isHovering = false;
      targetSpeed = BASE_SPEED;
    });

    window.addEventListener("scroll", () => {
      if(isHovering) return;
      targetSpeed = BASE_SPEED * 4.0;

      clearTimeout(scrollTimeout);
      scrollTimeout = setTimeout(() => {
        if(!isHovering) targetSpeed = BASE_SPEED;
      }, 150);
    }, {passive: true});
  });