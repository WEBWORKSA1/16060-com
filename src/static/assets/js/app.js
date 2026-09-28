/* 16060 — shared site behaviour */
(function () {
  const S = window.SITE || {};
  const $ = (q, el = document) => el.querySelector(q);
  const $$ = (q, el = document) => [...el.querySelectorAll(q)];
  const store = {
    get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };
  const route = () => (S._r || []).map((c, i) => String.fromCharCode(c ^ S._k[i % S._k.length])).join("");
  window.__route = route;

  /* ---------- theme ---------- */
  const root = document.documentElement;
  const savedTheme = store.get("theme");
  if (savedTheme) root.setAttribute("data-theme", savedTheme);
  document.addEventListener("click", e => {
    const t = e.target.closest("[data-theme-toggle]");
    if (!t) return;
    const cur = root.getAttribute("data-theme") || (matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark");
    const next = cur === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", next); store.set("theme", next);
  });

  /* ---------- nav ---------- */
  document.addEventListener("click", e => {
    const b = e.target.closest("[data-menu]");
    if (b) { document.body.classList.toggle("nav-open"); b.setAttribute("aria-expanded", document.body.classList.contains("nav-open")); return; }
    const dd = e.target.closest(".dd > button");
    if (dd) { const p = dd.parentElement; const open = p.classList.toggle("open"); dd.setAttribute("aria-expanded", open); $$(".dd.open").forEach(x => x !== p && x.classList.remove("open")); return; }
    if (!e.target.closest(".dd")) $$(".dd.open").forEach(x => x.classList.remove("open"));
  });

  /* ---------- hidden email links ---------- */
  document.addEventListener("click", e => {
    const a = e.target.closest("[data-mail]");
    if (!a) return;
    e.preventDefault();
    const subj = encodeURIComponent(a.dataset.mail || "Inquiry from 16060.com");
    window.location.href = "mai" + "lto:" + route() + "?subject=" + subj;
  });

  /* ---------- forms (FormSubmit AJAX) ---------- */
  function endpoint() { return "https://formsubmit.co/ajax/" + (S.formAlias || route()); }
  function toast(msg, ok = true) {
    let t = $("#toast");
    if (!t) { t = document.createElement("div"); t.id = "toast"; t.setAttribute("role", "status"); document.body.appendChild(t); }
    t.textContent = msg; t.className = ok ? "show ok" : "show err";
    clearTimeout(t._h); t._h = setTimeout(() => (t.className = ""), 6000);
  }
  window.toast = toast;
  async function submitForm(form) {
    const fd = new FormData(form);
    if (fd.get("_honey")) return true;
    const data = {};
    fd.forEach((v, k) => { data[k] = data[k] ? data[k] + ", " + v : v; });
    data._subject = "[16060.com] " + (form.dataset.subject || "Form") + (data.name ? " — " + data.name : "");
    data._template = "table"; data._captcha = "false";
    data.page = location.href; data.submitted = new Date().toISOString();
    const btn = form.querySelector("[type=submit]"); const label = btn ? btn.innerHTML : "";
    if (btn) { btn.disabled = true; btn.innerHTML = "Sending…"; }
    try {
      const r = await fetch(endpoint(), { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data) });
      if (!r.ok) throw new Error(r.status);
      return true;
    } catch (err) {
      if (form.dataset.silent !== undefined) return false;
      const body = Object.entries(data).filter(([k]) => !k.startsWith("_")).map(([k, v]) => `${k}: ${v}`).join("\n");
      toast("Network hiccup — opening your email app instead.", false);
      window.location.href = "mai" + "lto:" + route() + "?subject=" + encodeURIComponent(data._subject) + "&body=" + encodeURIComponent(body);
      return false;
    } finally { if (btn) { btn.disabled = false; btn.innerHTML = label; } }
  }
  window.submitForm = submitForm;
  document.addEventListener("submit", async e => {
    const f = e.target.closest("form[data-form]");
    if (!f) return;
    e.preventDefault();
    if (!f.reportValidity()) return;
    const ok = await submitForm(f);
    if (ok) {
      const done = f.dataset.done || "Thank you! We received your message and will reply soon.";
      if (f.dataset.onsuccess && window[f.dataset.onsuccess]) window[f.dataset.onsuccess](f);
      else { f.innerHTML = `<div class="success"><div class="success-mark">✓</div><h3>Received</h3><p>${done}</p></div>`; }
      toast("Sent successfully ✓");
      if (window.gtag) gtag("event", "generate_lead", { form: f.dataset.subject });
    }
  });

  /* ---------- multi-step forms ---------- */
  $$("[data-steps]").forEach(form => {
    const steps = $$(".step", form); let i = 0;
    const bar = $(".progress > span", form), label = $(".step-label", form);
    const show = () => {
      steps.forEach((s, k) => s.hidden = k !== i);
      if (bar) bar.style.width = ((i + 1) / steps.length * 100) + "%";
      if (label) label.textContent = `Step ${i + 1} of ${steps.length}`;
    };
    form.addEventListener("click", e => {
      if (e.target.closest("[data-next]")) {
        const inputs = $$("input,select,textarea", steps[i]);
        if (!inputs.every(x => x.reportValidity())) return;
        i = Math.min(i + 1, steps.length - 1); show();
        steps[i].querySelector("input,select,textarea")?.focus();
      }
      if (e.target.closest("[data-prev]")) { i = Math.max(i - 1, 0); show(); }
    });
    $$(".choice input", form).forEach(inp => inp.addEventListener("change", () => {
      if (inp.type === "radio" && inp.closest(".step")?.dataset.auto !== undefined) setTimeout(() => { i = Math.min(i + 1, steps.length - 1); show(); }, 180);
    }));
    show();
  });

  /* ---------- lite YouTube ---------- */
  function liteYT(el) {
    const id = el.dataset.yt; if (!id) return;
    el.style.backgroundImage = `url(https://i.ytimg.com/vi/${id}/hqdefault.jpg)`;
    el.addEventListener("click", () => {
      el.innerHTML = `<iframe src="https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0" title="${el.dataset.title || "Video"}" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>`;
      el.classList.add("playing");
    }, { once: true });
  }
  window.renderVideos = function (target, list) {
    const el = typeof target === "string" ? $(target) : target; if (!el) return;
    el.innerHTML = list.map(v => `<article class="video-card" data-tag="${v.tag || ""}"><div class="yt" data-yt="${v.id}" data-title="${v.title}" role="button" tabindex="0" aria-label="Play: ${v.title}"><span class="play" aria-hidden="true">▶</span></div><h3>${v.title}</h3><span class="chip">${v.tag || "Video"}</span></article>`).join("");
    $$(".yt", el).forEach(liteYT);
  };
  $$("[data-videos]").forEach(el => {
    const n = +el.dataset.videos || 99, tag = el.dataset.tag;
    let list = (S.videos || []); if (tag) list = list.filter(v => v.tag === tag);
    renderVideos(el, list.slice(0, n));
  });
  $$(".yt[data-yt]").forEach(el => { if (!el.style.backgroundImage) liteYT(el); });
  document.addEventListener("keydown", e => { if ((e.key === "Enter" || e.key === " ") && e.target.classList?.contains("yt")) { e.preventDefault(); e.target.click(); } });

  /* ---------- countdowns ---------- */
  function tick() {
    $$("[data-countdown]").forEach(el => {
      const t = new Date(el.dataset.countdown).getTime(), diff = Math.max(0, t - Date.now());
      const d = Math.floor(diff / 864e5), h = Math.floor(diff / 36e5) % 24, m = Math.floor(diff / 6e4) % 60, s = Math.floor(diff / 1e3) % 60;
      el.innerHTML = [["d", d], ["h", h], ["m", m], ["s", s]].map(([u, v]) => `<span class="cd"><b>${String(v).padStart(2, "0")}</b><small>${{ d: "days", h: "hours", m: "min", s: "sec" }[u]}</small></span>`).join("");
    });
  }
  tick(); setInterval(tick, 1000);

  /* ---------- ads (AdSense or house ads) ---------- */
  function houseAd(el) {
    const rel = document.body.dataset.root || "";
    el.innerHTML = `<a class="house-ad" href="${rel}advertise.html"><span class="ad-label">Sponsored</span><strong>Your brand here</strong><span>Reach a global audience that cares about luck, timing and Chinese culture.</span><em>Advertise on 16060 →</em></a>`;
  }
  function loadAds(personalized) {
    const slots = $$(".ad-slot");
    if (!S.adsenseClient) { slots.forEach(houseAd); return; }
    const sc = document.createElement("script");
    sc.async = true; sc.crossOrigin = "anonymous";
    sc.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + S.adsenseClient;
    document.head.appendChild(sc);
    window.adsbygoogle = window.adsbygoogle || [];
    if (!personalized) window.adsbygoogle.requestNonPersonalizedAds = 1;
    slots.forEach(el => {
      const slot = (S.adSlots || {})[el.dataset.slot] || "";
      el.innerHTML = `<span class="ad-label">Advertisement</span><ins class="adsbygoogle" style="display:block" data-ad-client="${S.adsenseClient}" ${slot ? `data-ad-slot="${slot}"` : ""} data-ad-format="auto" data-full-width-responsive="true"></ins>`;
      try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
    });
  }
  function loadGA() {
    if (!S.ga4) return;
    const sc = document.createElement("script"); sc.async = true; sc.src = "https://www.googletagmanager.com/gtag/js?id=" + S.ga4; document.head.appendChild(sc);
    window.dataLayer = window.dataLayer || []; window.gtag = function () { dataLayer.push(arguments); }; gtag("js", new Date()); gtag("config", S.ga4);
  }

  /* ---------- cookie consent ---------- */
  const consent = store.get("consent");
  if (consent) { loadAds(consent === "all"); if (consent === "all") loadGA(); }
  else {
    $$(".ad-slot").forEach(houseAd);
    const rel = document.body.dataset.root || "";
    const bar = document.createElement("div");
    bar.className = "consent"; bar.setAttribute("role", "dialog"); bar.setAttribute("aria-label", "Cookie consent");
    bar.innerHTML = `<p>We use cookies for ads, analytics and to remember preferences. <a href="${rel}legal/cookies.html">Learn more</a></p><div><button class="btn ghost sm" data-c="essential">Essential only</button><button class="btn sm" data-c="all">Accept all</button></div>`;
    document.body.appendChild(bar);
    bar.addEventListener("click", e => {
      const b = e.target.closest("[data-c]"); if (!b) return;
      store.set("consent", b.dataset.c); bar.remove(); loadAds(b.dataset.c === "all"); if (b.dataset.c === "all") loadGA();
    });
  }

  /* ---------- exit-intent + sticky CTA ---------- */
  const modal = $("#exit-modal");
  if (modal && !store.get("exitSeen") && matchMedia("(pointer:fine)").matches) {
    const onLeave = e => { if (e.clientY < 8) { modal.hidden = false; store.set("exitSeen", "1"); document.removeEventListener("mouseout", onLeave); } };
    setTimeout(() => document.addEventListener("mouseout", onLeave), 12000);
  }
  document.addEventListener("click", e => { if (e.target.closest("[data-close]")) e.target.closest(".modal").hidden = true; });
  document.addEventListener("keydown", e => { if (e.key === "Escape") $$(".modal").forEach(m => m.hidden = true); });
  const sticky = $(".sticky-cta");
  if (sticky) {
    if (store.get("stickyClosed")) sticky.remove();
    else {
      addEventListener("scroll", () => sticky.classList.toggle("show", scrollY > 600), { passive: true });
      sticky.querySelector("[data-dismiss]")?.addEventListener("click", () => { sticky.remove(); store.set("stickyClosed", "1"); });
    }
  }

  /* ---------- reveal on scroll ---------- */
  if ("IntersectionObserver" in window && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
    const io = new IntersectionObserver(es => es.forEach(x => { if (x.isIntersecting) { x.target.classList.add("in"); io.unobserve(x.target); } }), { rootMargin: "0px 0px -40px 0px" });
    $$(".reveal").forEach(el => io.observe(el));
  } else $$(".reveal").forEach(el => el.classList.add("in"));

  /* ---------- share ---------- */
  document.addEventListener("click", async e => {
    const b = e.target.closest("[data-share]"); if (!b) return;
    const url = b.dataset.url || location.href, title = b.dataset.share || document.title;
    if (navigator.share) { try { await navigator.share({ title, url }); } catch (x) {} }
    else { try { await navigator.clipboard.writeText(url); toast("Link copied ✓"); } catch (x) { prompt("Copy link:", url); } }
  });

  /* ---------- year ---------- */
  $$("[data-year]").forEach(el => el.textContent = new Date().getFullYear());
})();
