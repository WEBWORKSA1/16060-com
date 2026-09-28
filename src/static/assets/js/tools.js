/* 16060 — interactive tools. Each tool mounts on [data-tool="name"]. */
(function () {
  const $ = (q, el = document) => el.querySelector(q);
  const $$ = (q, el = document) => [...el.querySelectorAll(q)];
  const K = window.Calc;
  const ROOT = document.body.dataset.root || "";
  const today = new Date();
  const todayISO = `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, "0")}-${String(today.getDate()).padStart(2, "0")}`;
  const P = s => K.parseISO(s);
  const fmt = s => new Date(s + "T12:00:00").toLocaleDateString(undefined, { weekday: "short", year: "numeric", month: "short", day: "numeric" });
  const animalLink = b => `${ROOT}zodiac/${K.ANIMALS[b].toLowerCase()}.html`;
  const elSpan = (i, txt) => `<span class="el-${K.ELEMENTS[i]}">${txt}</span>`;
  const pillarHTML = (label, p) => p ? `<div class="pillar"><small class="muted">${label}</small><span class="zh">${elSpan(K.stemElement(p.s), K.STEMS[p.s])}<br>${elSpan(K.BRANCH_ELEMENT[p.b], K.BRANCHES[p.b])}</span><small>${K.STEMS_PY[p.s]} ${K.BRANCHES_PY[p.b]}</small><br><small class="muted">${K.ELEMENTS[K.stemElement(p.s)]} · ${K.ANIMALS[p.b]}</small></div>` : `<div class="pillar"><small class="muted">${label}</small><span class="zh muted">?</span><small class="muted">add birth hour</small></div>`;
  const setParams = obj => { const u = new URL(location.href); Object.entries(obj).forEach(([k, v]) => v === "" || v == null ? u.searchParams.delete(k) : u.searchParams.set(k, v)); history.replaceState(null, "", u); };
  const param = k => new URL(location.href).searchParams.get(k);
  const shareBtn = t => `<button class="btn ghost sm no-print" data-share="${t}">↗ Share result</button> <button class="btn ghost sm no-print" onclick="print()">⎙ Print / PDF</button>`;
  const leadNudge = () => `<div class="callout no-print"><b>Want the full picture?</b> Get a free personal Lucky Blueprint — zodiac, four pillars, lucky numbers and your best dates for the next 60 days. <a href="${ROOT}consult.html#blueprint">Get it free →</a></div>`;
  const animalOptions = (sel) => K.ANIMALS.map((a, i) => `<option value="${i}" ${i === sel ? "selected" : ""}>${K.ANIMAL_EMOJI[i]} ${a} ${K.ANIMAL_ZH[i]}</option>`).join("");
  const HETU = { Water: [1, 6], Fire: [2, 7], Wood: [3, 8], Metal: [4, 9], Earth: [5, 0] };

  const tools = {
    /* ---------------- Lucky number ---------------- */
    "lucky-number"(el) {
      const form = $("form", el), out = $(".result", el);
      function run(v) {
        const r = K.analyzeNumber(v);
        if (!r) { out.innerHTML = `<p class="muted">Enter at least one digit.</p>`; return; }
        setParams({ n: r.s });
        const cls = d => ({ 8: "top", 6: "good", 9: "good", 2: "good", 4: "bad" }[d] || "");
        out.innerHTML = `<div class="panel">
          <div class="big-score"><div class="ring" style="--p:${r.score}"><b>${r.score}</b></div>
          <div><span class="chip ${r.score >= 70 ? "gold" : r.score < 40 ? "red" : ""}">${r.grade[1]} · ${r.grade[0]}</span>
          <h3 style="margin-top:10px">“${r.s}” scores ${r.score}/99</h3><p class="muted">Digit sum ${r.sum} · ${r.s.length} digits · ${r.digits["4"] ? r.digits["4"] + "× four" : "no 4s"} · ${r.digits["8"] || 0}× eight</p></div></div>
          <div class="digits">${[...r.s].map(d => `<span class="digit ${cls(d)}" title="${K.DIGITS[d].m}">${d}</span>`).join("")}</div>
          ${r.comboHits.length ? `<h4>Combinations found</h4><ul>${r.comboHits.map(c => `<li><b>${c.p}</b> ${c.w > 0 ? "✅" : "⚠️"} ${c.desc}${c.c > 1 ? ` (×${c.c})` : ""}</li>`).join("")}</ul>` : ""}
          ${r.notes.length ? `<h4>Pattern notes</h4><ul>${r.notes.map(n => `<li>${n}</li>`).join("")}</ul>` : ""}
          <h4>Digit by digit</h4><div class="table-wrap"><table><tr><th>Digit</th><th>Chinese</th><th>Meaning</th><th>Count</th></tr>
          ${Object.keys(r.digits).sort().map(d => `<tr><td><b>${d}</b></td><td class="zh">${K.DIGITS[d].zh}</td><td>${K.DIGITS[d].m}</td><td>${r.digits[d]}</td></tr>`).join("")}</table></div>
          <p style="margin-top:14px">${shareBtn("My lucky number score on 16060")}</p></div>${leadNudge()}`;
        out.scrollIntoView({ behavior: "smooth", block: "nearest" });
      }
      form.addEventListener("submit", e => { e.preventDefault(); run($("[name=n]", form).value); });
      $$("[data-try]", el).forEach(b => b.addEventListener("click", () => { $("[name=n]", form).value = b.dataset.try; run(b.dataset.try); }));
      const n = param("n"); if (n) { $("[name=n]", form).value = n; run(n); }
    },

    /* ---------------- Zodiac finder ---------------- */
    "zodiac-finder"(el) {
      const form = $("form", el), out = $(".result", el);
      function run(d) {
        const { y, m, d: dd } = P(d);
        if (!K.inRange(y)) { out.innerHTML = `<p class="muted">Please choose a date between 1921 and 2060.</p>`; return; }
        const z = K.zodiac(y, m, dd); setParams({ d });
        const near = y !== z.lunarYear || (C = window.CAL.cny[y], Math.abs(new Date(d) - new Date(C)) < 30 * 864e5);
        out.innerHTML = `<div class="panel">
          <div class="big-score"><div style="font-size:4.5rem;line-height:1">${z.emoji}</div>
          <div><span class="chip gold">${z.gz} · ${z.cycleNo}/60 in the cycle</span><h2 style="margin:8px 0 4px">${z.yinyang} ${z.element} ${z.animal} <span class="zh" style="color:var(--red)">${z.animalZh}</span></h2>
          <p class="muted" style="margin:0">Chinese year ${z.lunarYear}: ${fmt(z.cnyStart)} → ${fmt(z.cnyEnd)} (day before)</p></div></div>
          ${near ? `<div class="callout">Born near Lunar New Year? You were born ${y !== z.lunarYear ? "<b>before</b>" : "<b>after</b>"} the ${y} New Year (${fmt(window.CAL.cny[y])}), so your sign is the <b>${z.animal}</b>, not the animal of the Gregorian year${y !== z.lunarYear ? " " + y : ""}. (BaZi astrologers use the Start of Spring ~Feb 4 instead — see the <a href="${ROOT}tools/four-pillars.html">Four Pillars tool</a>.)</div>` : ""}
          <div class="grid g3" style="margin-top:16px">
            <div class="card"><h3>Element</h3><p>${elSpan(K.stemElement(z.stem), z.element + " " + z.elementZh)} — heavenly stem ${K.STEMS[z.stem]} (${K.STEMS_PY[z.stem]})</p></div>
            <div class="card"><h3>Best matches</h3><p>${[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].filter(b => K.compatibility(z.branch, b).score >= 90).map(b => `<a href="${animalLink(b)}">${K.ANIMAL_EMOJI[b]} ${K.ANIMALS[b]}</a>`).join(", ")}</p></div>
            <div class="card"><h3>Clash</h3><p><a href="${animalLink((z.branch + 6) % 12)}">${K.ANIMAL_EMOJI[(z.branch + 6) % 12]} ${K.ANIMALS[(z.branch + 6) % 12]}</a> — opposite on the wheel</p></div>
          </div>
          <p style="margin-top:16px"><a class="btn" href="${animalLink(z.branch)}">Read the full ${z.animal} profile →</a> ${shareBtn("My Chinese zodiac on 16060")}</p></div>${leadNudge()}`;
      }
      let C;
      form.addEventListener("submit", e => { e.preventDefault(); run($("[name=d]", form).value); });
      const d = param("d"); if (d) { $("[name=d]", form).value = d; run(d); }
    },

    /* ---------------- Compatibility ---------------- */
    "compatibility"(el) {
      const a = $("[name=a]", el), b = $("[name=b]", el), out = $(".result", el);
      a.innerHTML = animalOptions(+(param("a") ?? 0)); b.innerHTML = animalOptions(+(param("b") ?? 4));
      function run() {
        const x = +a.value, y = +b.value, r = K.compatibility(x, y); setParams({ a: x, b: y });
        out.innerHTML = `<div class="panel"><div class="big-score"><div class="ring" style="--p:${r.score}"><b>${r.score}</b></div>
          <div><h2 style="margin:0">${K.ANIMAL_EMOJI[x]} ${K.ANIMALS[x]} + ${K.ANIMAL_EMOJI[y]} ${K.ANIMALS[y]}</h2><span class="chip gold">${r.label}</span><p class="muted" style="margin-top:8px">${r.note}</p></div></div>
          <h4 style="margin-top:14px">How to make it work</h4><ul>
          <li>${r.score >= 85 ? "Lean into shared goals — this pairing thrives on joint projects and long horizons." : r.score >= 60 ? "Agree on roles early; neutral pairings flourish when strengths are made explicit." : "Schedule regular check-ins and avoid major decisions on days that clash either sign (see the Auspicious Date Finder)."}</li>
          <li>Check the <b>element balance</b> of both birth years in the <a href="${ROOT}tools/four-pillars.html">Four Pillars tool</a> — elements often matter more than animals.</li></ul>
          <p>${shareBtn("Our zodiac compatibility on 16060")}</p></div>`;
      }
      a.addEventListener("change", run); b.addEventListener("change", run); run();
      // matrix
      const mx = $(".matrix", el);
      if (mx) mx.innerHTML = `<div class="table-wrap"><table><tr><th></th>${K.ANIMALS.map((n, i) => `<th title="${n}">${K.ANIMAL_EMOJI[i]}</th>`).join("")}</tr>${K.ANIMALS.map((n, i) => `<tr><th>${K.ANIMAL_EMOJI[i]} ${n}</th>${K.ANIMALS.map((m, j) => { const s = K.compatibility(i, j).score; return `<td style="text-align:center;background:${s >= 90 ? "rgba(63,164,122,.25)" : s <= 40 ? "rgba(215,50,43,.22)" : s <= 50 ? "rgba(215,50,43,.1)" : "transparent"}">${s}</td>`; }).join("")}</tr>`).join("")}</table></div>`;
    },

    /* ---------------- 60-year cycle ---------------- */
    "sixty-year-cycle"(el) {
      const sel = $("[name=start]", el), filt = $("[name=f]", el), out = $(".result", el);
      function run() {
        const start = +sel.value, f = filt.value, cur = K.lunarYearOf(today.getFullYear(), today.getMonth() + 1, today.getDate());
        let rows = "";
        for (let i = 0; i < 60; i++) {
          const y = start + i, p = K.pillarOfYear(y), e = K.ELEMENTS[K.stemElement(p.s)];
          if (f && f !== K.ANIMALS[p.b] && f !== e) continue;
          rows += `<tr class="${y === cur ? "hl" : ""}"><td>${i + 1}</td><td class="zh" style="font-size:1.2rem">${K.gz(p.s, p.b)}</td><td>${K.STEMS_PY[p.s]}-${K.BRANCHES_PY[p.b]}</td><td><b>${y}</b></td><td>${window.CAL.cny[y] ? fmt(window.CAL.cny[y]) : "—"}</td><td>${elSpan(K.stemElement(p.s), e)} · ${K.yinYang(p.s)}</td><td><a href="${animalLink(p.b)}">${K.ANIMAL_EMOJI[p.b]} ${K.ANIMALS[p.b]}</a></td></tr>`;
        }
        out.innerHTML = `<div class="table-wrap"><table><tr><th>#</th><th>干支</th><th>Pinyin</th><th>Year</th><th>New Year's Day</th><th>Element</th><th>Animal</th></tr>${rows}</table></div>`;
      }
      filt.innerHTML = `<option value="">All years</option><optgroup label="Animal">${K.ANIMALS.map(a => `<option>${a}</option>`).join("")}</optgroup><optgroup label="Element">${K.ELEMENTS.map(a => `<option>${a}</option>`).join("")}</optgroup>`;
      sel.addEventListener("change", run); filt.addEventListener("change", run); run();
    },

    /* ---------------- Lunar converter ---------------- */
    "lunar-converter"(el) {
      const f1 = $("#g2l", el), f2 = $("#l2g", el), o1 = $("#g2l-out", el), o2 = $("#l2g-out", el);
      const dayName = d => { const n = ["", "初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十", "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十"]; return n[d]; };
      const monthZh = ["", "正月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "冬月", "腊月"];
      function g2l(v) {
        const { y, m, d } = P(v); const l = K.toLunar(y, m, d);
        if (!l) { o1.innerHTML = `<p class="muted">Out of range (1921–2060).</p>`; return; }
        const yp = K.pillarOfYear(l.year), dp = K.dayPillar(y, m, d), off = K.officer(y, m, d);
        const terms = K.termsOfYear(y).filter(t => t.date === v);
        o1.innerHTML = `<div class="panel"><h2 class="zh" style="margin:0">${K.gz(yp.s, yp.b)}年 ${l.leap ? "闰" : ""}${monthZh[l.month]}${dayName(l.day)}</h2>
          <p class="lead" style="margin:6px 0 12px">Lunar ${l.leap ? "leap " : ""}month ${l.month}, day ${l.day} · Year of the ${K.ANIMALS[yp.b]} (${l.year})</p>
          <div class="grid g3"><div class="card"><h3>Day pillar</h3><p class="zh" style="font-size:1.4rem">${K.gz(dp.s, dp.b)}</p><p>${K.STEMS_PY[dp.s]} ${K.BRANCHES_PY[dp.b]} · clashes ${K.ANIMALS[(dp.b + 6) % 12]}</p></div>
          <div class="card"><h3>Day officer</h3><p class="zh" style="font-size:1.4rem">${off ? off[0] : "—"}</p><p>${off ? off[1] + (off[2] > 0 ? " · traditionally favourable" : off[2] < 0 ? " · traditionally avoided" : " · neutral") : ""}</p></div>
          <div class="card"><h3>Month length</h3><p class="zh" style="font-size:1.4rem">${l.monthLen} days</p><p>${l.monthLen === 30 ? "大月 big month" : "小月 small month"}${terms.length ? " · Solar term today: " + terms[0].zh + " " + terms[0].name : ""}</p></div></div></div>`;
      }
      f1.addEventListener("submit", e => { e.preventDefault(); g2l($("[name=d]", f1).value); });
      f2.addEventListener("submit", e => {
        e.preventDefault();
        const r = K.fromLunar(+$("[name=y]", f2).value, +$("[name=m]", f2).value, +$("[name=d]", f2).value, $("[name=leap]", f2).checked);
        o2.innerHTML = r ? `<div class="panel"><h2 style="margin:0">${fmt(K.iso(r))}</h2><p class="muted">Gregorian date · <a href="?d=${K.iso(r)}">see full lunar details</a></p></div>` : `<p class="muted">That lunar date doesn't exist (month too short, or no such leap month that year).</p>`;
      });
      const d = param("d") || todayISO; $("[name=d]", f1).value = d; g2l(d);
      $("[name=y]", f2).value = today.getFullYear();
    },

    /* ---------------- Four pillars ---------------- */
    "four-pillars"(el) {
      const form = $("form", el), out = $(".result", el);
      function run(d, h) {
        const { y, m, d: dd } = P(d);
        if (!K.inRange(y)) { out.innerHTML = `<p class="muted">Please choose a date between 1921 and 2060.</p>`; return; }
        setParams({ d, h });
        const r = K.fourPillars(y, m, dd, h === "" ? null : h), tot = r.count.reduce((a, b) => a + b, 0);
        const max = Math.max(...r.count), weak = K.ELEMENTS[r.count.indexOf(Math.min(...r.count))], strong = K.ELEMENTS[r.count.indexOf(max)];
        const colors = ["var(--wood)", "var(--fire)", "var(--earth)", "var(--metal)", "var(--water)"];
        out.innerHTML = `<div class="panel"><div class="pillars">${pillarHTML("Hour 时", r.pillars.hour)}${pillarHTML("Day 日", r.pillars.day)}${pillarHTML("Month 月", r.pillars.month)}${pillarHTML("Year 年", r.pillars.year)}</div>
          <div class="grid g2" style="margin-top:18px"><div><h3>Five-element balance</h3><div class="bars">${r.count.map((c, i) => `<div class="bar"><span class="el-${K.ELEMENTS[i]}">${K.ELEMENTS[i]} ${K.ELEMENT_ZH[i]}</span><i><span style="width:${c / tot * 100}%;background:${colors[i]}"></span></i><b>${c}</b></div>`).join("")}</div></div>
          <div><h3>Day Master: ${r.dayMaster.yy} ${r.dayMaster.element}</h3><p class="muted">The day stem ${K.STEMS[r.dayMaster.stem]} represents <b>you</b> in a BaZi chart. Your chart is strongest in <b>${strong}</b>${r.count.includes(0) ? ` and has no <b>${weak}</b>` : ` and lightest in <b>${weak}</b>`}. Traditional practice looks for balance — many people favour colours, directions and numbers of the weaker element (${weak}: numbers ${HETU[weak].join(" & ")}).</p></div></div>
          <p class="small muted">Year and month pillars change at the solar terms (year at 立春 Start of Spring), not on Jan 1 or Lunar New Year. Computed to the day; births within hours of a solar-term change should be checked by a practitioner. Hour pillar uses local clock time.</p>
          <p>${shareBtn("My Four Pillars on 16060")}</p></div>
          <div class="callout no-print"><b>Get a professional BaZi reading.</b> Luck pillars, 10-year cycles, career and relationship timing — reviewed by a practitioner. <a href="${ROOT}consult.html#consult">Request a consultation →</a></div>`;
      }
      form.addEventListener("submit", e => { e.preventDefault(); run($("[name=d]", form).value, $("[name=h]", form).value); });
      const d = param("d"); if (d) { $("[name=d]", form).value = d; $("[name=h]", form).value = param("h") || ""; run(d, param("h") || ""); }
    },

    /* ---------------- Auspicious dates ---------------- */
    "auspicious-dates"(el) {
      const form = $("form", el), out = $(".result", el);
      const EVENT = { wedding: ["成", "定", "开"], opening: ["开", "成", "定"], moving: ["成", "开", "除"], travel: ["成", "开", "危"], signing: ["定", "成", "执"], general: ["成", "开", "定"] };
      $("[name=start]", form).value = todayISO;
      function run() {
        const start = P($("[name=start]", form).value), days = +$("[name=days]", form).value, ev = $("[name=event]", form).value;
        const by = $("[name=by]", form).value, myB = by ? K.pillarOfYear(+by).b : null;
        let n0 = K.dayNum(start.y, start.m, start.d), rows = [], best = [];
        for (let i = 0; i < days; i++) {
          const o = K.fromDayNum(n0 + i), off = K.officer(o.y, o.m, o.d); if (!off) continue;
          const dp = K.dayPillar(o.y, o.m, o.d), clash = (dp.b + 6) % 12, date = K.iso(o);
          let score = off[2] > 0 ? 60 : off[2] < 0 ? 15 : 40;
          if (EVENT[ev].includes(off[0])) score += 25 - EVENT[ev].indexOf(off[0]) * 5;
          if (myB !== null && clash === myB) score -= 45;
          if (myB !== null && K.compatibility(dp.b, myB).score >= 90) score += 10;
          const dn = K.analyzeNumber(`${o.m}${o.d}`); if (dn && /8|6|9/.test(`${o.d}`)) score += 3; if (`${o.d}`.includes("4")) score -= 3;
          const wk = new Date(date + "T12:00").getDay(); if ((ev === "wedding") && (wk === 0 || wk === 6)) score += 4;
          score = Math.max(0, Math.min(100, score));
          const row = { date, off, dp, clash, score };
          rows.push(row);
        }
        best = [...rows].sort((a, b) => b.score - a.score).slice(0, 5).sort((a, b) => a.date.localeCompare(b.date));
        const lab = s => s >= 80 ? `<span class="chip jade">Excellent</span>` : s >= 60 ? `<span class="chip gold">Good</span>` : s >= 35 ? `<span class="chip">Fair</span>` : `<span class="chip red">Avoid</span>`;
        out.innerHTML = `<div class="panel"><h3>Top 5 dates for ${$("[name=event] option:checked", form).textContent.toLowerCase()}</h3>
          <div class="grid g3">${best.map(r => `<div class="card"><b>${fmt(r.date)}</b><p class="zh" style="font-size:1.3rem;margin:6px 0">${K.gz(r.dp.s, r.dp.b)} · ${r.off[0]}</p><p class="small">${r.off[1]} day · clashes ${K.ANIMALS[r.clash]}</p>${lab(r.score)}</div>`).join("")}</div>
          <h3 style="margin-top:22px">Day-by-day</h3><div class="table-wrap"><table><tr><th>Date</th><th>Day pillar</th><th>Officer 建除</th><th>Clashes</th><th>Rating</th></tr>
          ${rows.map(r => `<tr><td>${fmt(r.date)}</td><td class="zh">${K.gz(r.dp.s, r.dp.b)}</td><td><span class="${r.off[2] > 0 ? "day-good" : r.off[2] < 0 ? "day-bad" : ""}">${r.off[0]} ${r.off[1]}</span></td><td>${K.ANIMAL_EMOJI[r.clash]} ${K.ANIMALS[r.clash]}${myB === r.clash ? " ⚠️ <b>you</b>" : ""}</td><td>${lab(r.score)} <small class="muted">${r.score}</small></td></tr>`).join("")}</table></div>
          <p class="small muted" style="margin-top:12px">Method: the traditional 12 Day Officers (建除十二神) from the solar-month and day branch, the rhyme “除危定执黄，成开皆可用；建满平收黑，闭破不相当”, event-specific preferences, your zodiac clash and date-digit symbolism. For weddings and business launches, practitioners also check the full almanac and your personal chart.</p>
          <p>${shareBtn("Auspicious dates from 16060")}</p></div>
          <div class="callout no-print"><b>High-stakes date?</b> A professional date selection (择日) checks both people's charts, hours and the full almanac. <a href="${ROOT}consult.html#consult">Request date selection →</a></div>`;
      }
      form.addEventListener("submit", e => { e.preventDefault(); run(); });
      run();
    },

    /* ---------------- Clocks & timers ---------------- */
    "clocks-timers"(el) {
      const zones = [["Beijing", "Asia/Shanghai"], ["Hong Kong", "Asia/Hong_Kong"], ["Taipei", "Asia/Taipei"], ["Singapore", "Asia/Singapore"], ["Kuala Lumpur", "Asia/Kuala_Lumpur"], ["Sydney", "Australia/Sydney"], ["Vancouver", "America/Vancouver"], ["San Francisco", "America/Los_Angeles"], ["Toronto", "America/Toronto"], ["New York", "America/New_York"], ["London", "Europe/London"], ["Dubai", "Asia/Dubai"], ["Mumbai", "Asia/Kolkata"], ["Tokyo", "Asia/Tokyo"]];
      const grid = $(".clock-grid", el), big = $(".bigtime", el), sc = $(".shichen", el);
      grid.innerHTML = zones.map(([n, z]) => `<div class="clock"><small class="muted">${n}</small><b data-z="${z}">--:--</b><small class="muted" data-zd="${z}"></small></div>`).join("");
      function tick() {
        const now = new Date();
        big.textContent = now.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit", second: "2-digit" });
        $$("[data-z]", grid).forEach(b => b.textContent = now.toLocaleTimeString([], { timeZone: b.dataset.z, hour: "2-digit", minute: "2-digit" }));
        $$("[data-zd]", grid).forEach(b => b.textContent = now.toLocaleDateString([], { timeZone: b.dataset.zd, weekday: "short", day: "numeric", month: "short" }));
        const h = now.getHours(), i = Math.floor((h + 1) / 2) % 12, s = K.SHICHEN[i];
        const secsInto = ((h + 1) % 2) * 3600 + now.getMinutes() * 60 + now.getSeconds();
        sc.innerHTML = `<span class="zh" style="font-size:3rem;color:var(--red)">${s[0]}时</span><div><b>${s[1]} hour · ${s[3]}</b><br><span class="muted">${s[2]} · ${Math.round(secsInto / 72)}% through this double-hour · ${7200 - secsInto} seconds left</span></div>`;
      }
      tick(); setInterval(tick, 1000);
      // stopwatch
      let swStart = 0, swAcc = 0, swT = null; const sw = $(".sw", el), laps = $(".laps", el);
      const fmtMs = ms => { const h = Math.floor(ms / 36e5), m = Math.floor(ms / 6e4) % 60, s = Math.floor(ms / 1e3) % 60, c = Math.floor(ms / 10) % 100; return `${h ? h + ":" : ""}${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}.${String(c).padStart(2, "0")}`; };
      const swRender = () => sw.textContent = fmtMs(swAcc + (swT ? Date.now() - swStart : 0));
      $("[data-sw=start]", el).onclick = e => { if (swT) { swAcc += Date.now() - swStart; clearInterval(swT); swT = null; e.target.textContent = "Start"; } else { swStart = Date.now(); swT = setInterval(swRender, 31); e.target.textContent = "Pause"; } };
      $("[data-sw=lap]", el).onclick = () => { laps.insertAdjacentHTML("afterbegin", `<li>${fmtMs(swAcc + (swT ? Date.now() - swStart : 0))}</li>`); };
      $("[data-sw=reset]", el).onclick = () => { clearInterval(swT); swT = null; swAcc = 0; swRender(); laps.innerHTML = ""; $("[data-sw=start]", el).textContent = "Start"; };
      // timer
      let tEnd = 0, tT = null, tLeft = 0; const tv = $(".tv", el);
      const tRender = ms => { const s = Math.ceil(ms / 1000); tv.textContent = `${String(Math.floor(s / 3600)).padStart(2, "0")}:${String(Math.floor(s / 60) % 60).padStart(2, "0")}:${String(s % 60).padStart(2, "0")}`; document.title = tT ? tv.textContent + " · Timer" : document.title; };
      function beep() { try { const a = new (window.AudioContext || window.webkitAudioContext)(); [0, .35, .7].forEach(t => { const o = a.createOscillator(), g = a.createGain(); o.frequency.value = 880; o.connect(g); g.connect(a.destination); g.gain.setValueAtTime(.2, a.currentTime + t); g.gain.exponentialRampToValueAtTime(.001, a.currentTime + t + .3); o.start(a.currentTime + t); o.stop(a.currentTime + t + .3); }); } catch (e) {} }
      function startTimer(ms) { clearInterval(tT); tEnd = Date.now() + ms; tT = setInterval(() => { const l = tEnd - Date.now(); if (l <= 0) { clearInterval(tT); tT = null; tRender(0); beep(); window.toast && toast("⏰ Time's up!"); } else tRender(l); }, 200); }
      $$("[data-t]", el).forEach(b => b.onclick = () => { tLeft = +b.dataset.t * 1000; tRender(tLeft); startTimer(tLeft); });
      $("[data-timer=go]", el).onclick = () => { const h = +$("[name=th]", el).value || 0, m = +$("[name=tm]", el).value || 0, s = +$("[name=ts]", el).value || 0; tLeft = (h * 3600 + m * 60 + s) * 1000; if (tLeft) startTimer(tLeft); };
      $("[data-timer=stop]", el).onclick = () => { clearInterval(tT); tT = null; tRender(0); };
    },

    /* ---------------- Countdown ---------------- */
    "countdown"(el) {
      const list = $(".fest-list", el), mine = $(".my-cd", el), form = $("form", el);
      const F = (window.FESTIVALS || []).filter(f => f.date >= todayISO).slice(0, 8);
      list.innerHTML = F.map(f => `<div class="card"><span class="chip">${f.lunar === "solar term" ? "Solar term" : "Lunar " + f.lunar}</span><h3 style="margin-top:8px">${f.name} <span class="zh" style="color:var(--red)">${f.zh}</span></h3><p>${fmt(f.date)}</p><div class="countdown" data-countdown="${f.date}T00:00:00"></div></div>`).join("");
      function show(t, d) {
        mine.innerHTML = `<div class="panel center"><h2>${t.replace(/</g, "&lt;")}</h2><p class="muted">${new Date(d).toLocaleString()}</p><div class="countdown" style="justify-content:center" data-countdown="${d}"></div><p style="margin-top:14px">${shareBtn(t)}</p></div>`;
      }
      form.addEventListener("submit", e => { e.preventDefault(); const t = $("[name=t]", form).value || "My countdown", d = $("[name=d]", form).value + "T" + ($("[name=tm]", form).value || "00:00"); setParams({ t, at: d }); show(t, d); });
      const t = param("t"), at = param("at"); if (t && at) show(t, at);
    },

    /* ---------------- Blueprint (lead magnet) ---------------- */
    "blueprint"(el) {
      const form = $("form", el), out = $(".result", el);
      form.addEventListener("submit", async e => {
        e.preventDefault(); if (!form.reportValidity()) return;
        const name = $("[name=name]", form).value.trim(), d = $("[name=birthdate]", form).value, h = $("[name=birthhour]", form).value;
        const { y, m, d: dd } = P(d);
        if (!K.inRange(y)) { toast("Please choose a birth date between 1921 and 2060", false); return; }
        const btn = $("[type=submit]", form); btn.disabled = true; btn.textContent = "Generating…";
        const z = K.zodiac(y, m, dd), fp = K.fourPillars(y, m, dd, h === "" ? null : h);
        $("[name=summary]", form).value = `${z.element} ${z.animal} · Day master ${fp.dayMaster.element}`;
        await window.submitForm(form);
        btn.disabled = false; btn.textContent = "Generate my free blueprint";
        const weakIdx = fp.count.indexOf(Math.min(...fp.count)), weak = K.ELEMENTS[weakIdx], own = z.element;
        const lucky = [...new Set([...HETU[own], ...HETU[weak], 8, 6])].slice(0, 6);
        // next 60 days picks
        const n0 = K.dayNum(today.getFullYear(), today.getMonth() + 1, today.getDate()); const picks = [];
        for (let i = 1; i < 61; i++) { const o = K.fromDayNum(n0 + i), off = K.officer(o.y, o.m, o.d), dp = K.dayPillar(o.y, o.m, o.d); if (off && off[2] > 0 && (dp.b + 6) % 12 !== z.branch && ["成", "开", "定"].includes(off[0])) picks.push({ d: K.iso(o), off, dp }); }
        const matches = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].filter(b => K.compatibility(z.branch, b).score >= 90);
        out.innerHTML = `<div class="panel" id="report"><span class="chip gold">Personal Lucky Blueprint</span>
          <h2 style="margin-top:10px">${name.replace(/</g, "")}'s blueprint · ${z.emoji} ${z.yinyang} ${z.element} ${z.animal}</h2>
          <p class="muted">Born ${fmt(d)}${h !== "" ? ` · ${K.SHICHEN[Math.floor((+h + 1) / 2) % 12][0]}时 hour` : ""} · Chinese year ${z.gz} (${z.cycleNo}/60)</p>
          <div class="pillars" style="margin:16px 0">${pillarHTML("Hour", fp.pillars.hour)}${pillarHTML("Day", fp.pillars.day)}${pillarHTML("Month", fp.pillars.month)}${pillarHTML("Year", fp.pillars.year)}</div>
          <div class="grid g2"><div class="card"><h3>Your lucky numbers</h3><div class="digits">${lucky.map(n => `<span class="digit top">${n}</span>`).join("")}</div><p>From your year element (${own}), your chart's lightest element (${weak}) and the universal prosperity digits 8 &amp; 6.</p></div>
          <div class="card"><h3>Best allies</h3><p>${matches.map(b => `${K.ANIMAL_EMOJI[b]} ${K.ANIMALS[b]}`).join(" · ")}</p><h3 style="margin-top:12px">Handle with care</h3><p>${K.ANIMAL_EMOJI[(z.branch + 6) % 12]} ${K.ANIMALS[(z.branch + 6) % 12]} (clash)</p></div></div>
          <h3 style="margin-top:18px">Your strongest days in the next 60</h3><div class="grid g3">${picks.slice(0, 6).map(p => `<div class="card"><b>${fmt(p.d)}</b><p class="zh">${K.gz(p.dp.s, p.dp.b)} · ${p.off[0]} ${p.off[1]}</p></div>`).join("")}</div>
          <p style="margin-top:16px">${shareBtn("My 16060 Lucky Blueprint")}</p></div>
          <div class="callout no-print"><b>Next step:</b> turn this into decisions — a professional reading, a wedding or launch date, or a lucky business number. <a href="#consult">Book a consultation ↓</a></div>`;
        out.scrollIntoView({ behavior: "smooth" });
      });
    }
  };

  $$("[data-tool]").forEach(el => { const f = tools[el.dataset.tool]; if (f) try { f(el); } catch (e) { console.error(e); } });

  /* home: today widget */
  const tw = $("[data-today]");
  if (tw) {
    const y = today.getFullYear(), m = today.getMonth() + 1, d = today.getDate();
    const l = K.toLunar(y, m, d), dp = K.dayPillar(y, m, d), off = K.officer(y, m, d), z = K.zodiac(y, m, d);
    const next = (window.FESTIVALS || []).find(f => f.date > todayISO);
    tw.innerHTML = `<div class="grid g4">
      <div class="card"><small class="muted">Today (lunar)</small><h3 class="zh" style="margin:6px 0">${l ? `${l.leap ? "闰" : ""}${l.month}月${l.day}日` : ""}</h3><p>Year of the ${z.animal} ${z.emoji} · ${z.gz}</p></div>
      <div class="card"><small class="muted">Day pillar</small><h3 class="zh" style="margin:6px 0">${K.gz(dp.s, dp.b)}</h3><p>Clashes ${K.ANIMAL_EMOJI[(dp.b + 6) % 12]} ${K.ANIMALS[(dp.b + 6) % 12]}</p></div>
      <div class="card"><small class="muted">Day officer 建除</small><h3 class="zh" style="margin:6px 0">${off ? off[0] + " · " + off[1] : "—"}</h3><p class="${off && off[2] > 0 ? "day-good" : off && off[2] < 0 ? "day-bad" : ""}">${off ? (off[2] > 0 ? "Traditionally favourable" : off[2] < 0 ? "Traditionally avoided for big events" : "Neutral day") : ""}</p></div>
      <div class="card"><small class="muted">Next festival</small><h3 style="margin:6px 0">${next ? next.name : ""}</h3><p>${next ? fmt(next.date) : ""}</p></div></div>`;
  }
})();
