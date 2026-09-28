/* 16060 calculation engine — zodiac, sexagenary cycle, lunar calendar,
   four pillars, 12 day officers, lucky-number analysis. Requires caldata.js */
(function () {
  const DAY = 86400000;
  const EPOCH = Date.UTC(1900, 0, 1);
  const STEMS = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"];
  const STEMS_PY = ["Jiǎ", "Yǐ", "Bǐng", "Dīng", "Wù", "Jǐ", "Gēng", "Xīn", "Rén", "Guǐ"];
  const BRANCHES = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"];
  const BRANCHES_PY = ["Zǐ", "Chǒu", "Yín", "Mǎo", "Chén", "Sì", "Wǔ", "Wèi", "Shēn", "Yǒu", "Xū", "Hài"];
  const ANIMALS = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"];
  const ANIMAL_ZH = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"];
  const ANIMAL_EMOJI = ["🐀", "🐂", "🐅", "🐇", "🐉", "🐍", "🐎", "🐐", "🐒", "🐓", "🐕", "🐖"];
  const ELEMENTS = ["Wood", "Fire", "Earth", "Metal", "Water"];
  const ELEMENT_ZH = ["木", "火", "土", "金", "水"];
  const BRANCH_ELEMENT = [4, 2, 0, 0, 2, 1, 1, 2, 3, 3, 2, 4];
  const TERMS = ["Winter Solstice", "Minor Cold", "Major Cold", "Start of Spring", "Rain Water", "Awakening of Insects", "Spring Equinox", "Pure Brightness", "Grain Rain", "Start of Summer", "Grain Buds", "Grain in Ear", "Summer Solstice", "Minor Heat", "Major Heat", "Start of Autumn", "End of Heat", "White Dew", "Autumn Equinox", "Cold Dew", "Frost's Descent", "Start of Winter", "Minor Snow", "Major Snow"];
  const TERMS_ZH = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑", "白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪"];
  const OFFICERS = [
    ["建", "Establish", 0], ["除", "Remove", 1], ["满", "Full", 0], ["平", "Balance", 0],
    ["定", "Stable", 1], ["执", "Initiate", 1], ["破", "Destruction", -1], ["危", "Danger", 1],
    ["成", "Success", 1], ["收", "Receive", 0], ["开", "Open", 1], ["闭", "Close", -1]
  ];
  const LUNAR_MONTHS = ["", "Zhēng (1st)", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "La (12th)"];
  const SHICHEN = [
    ["子", "Zǐ", "23:00–00:59", "Rat"], ["丑", "Chǒu", "01:00–02:59", "Ox"], ["寅", "Yín", "03:00–04:59", "Tiger"],
    ["卯", "Mǎo", "05:00–06:59", "Rabbit"], ["辰", "Chén", "07:00–08:59", "Dragon"], ["巳", "Sì", "09:00–10:59", "Snake"],
    ["午", "Wǔ", "11:00–12:59", "Horse"], ["未", "Wèi", "13:00–14:59", "Goat"], ["申", "Shēn", "15:00–16:59", "Monkey"],
    ["酉", "Yǒu", "17:00–18:59", "Rooster"], ["戌", "Xū", "19:00–20:59", "Dog"], ["亥", "Hài", "21:00–22:59", "Pig"]
  ];

  const mod = (a, n) => ((a % n) + n) % n;
  const dayNum = (y, m, d) => Math.round((Date.UTC(y, m - 1, d) - EPOCH) / DAY);
  const fromDayNum = n => { const t = new Date(EPOCH + n * DAY); return { y: t.getUTCFullYear(), m: t.getUTCMonth() + 1, d: t.getUTCDate() }; };
  const iso = o => `${o.y}-${String(o.m).padStart(2, "0")}-${String(o.d).padStart(2, "0")}`;
  const parseISO = s => { const [y, m, d] = s.split("-").map(Number); return { y, m, d }; };

  const C = window.CAL || { terms: [], months: [], cny: {}, t0: 0 };

  function inRange(y) { return y >= 1921 && y <= 2060; }

  // Chinese (lunar) year for a Gregorian date, by Lunar New Year
  function lunarYearOf(y, m, d) {
    const cny = C.cny[y];
    if (!cny) return y;
    return iso({ y, m, d }) < cny ? y - 1 : y;
  }
  function pillarOfYear(ly) { return { s: mod(ly - 4, 10), b: mod(ly - 4, 12) }; }
  function sexagenaryIndex(s, b) { for (let i = 0; i < 60; i++) if (i % 10 === s && i % 12 === b) return i; return 0; }
  function gz(s, b) { return STEMS[s] + BRANCHES[b]; }
  function stemElement(s) { return Math.floor(s / 2); }
  function yinYang(s) { return s % 2 === 0 ? "Yang" : "Yin"; }

  function zodiac(y, m, d) {
    const ly = lunarYearOf(y, m, d);
    const p = pillarOfYear(ly);
    const el = stemElement(p.s);
    return {
      lunarYear: ly, stem: p.s, branch: p.b, animal: ANIMALS[p.b], animalZh: ANIMAL_ZH[p.b], emoji: ANIMAL_EMOJI[p.b],
      element: ELEMENTS[el], elementZh: ELEMENT_ZH[el], yinyang: yinYang(p.s), gz: gz(p.s, p.b),
      cycleNo: sexagenaryIndex(p.s, p.b) + 1, cnyStart: C.cny[ly], cnyEnd: C.cny[ly + 1]
    };
  }

  // Lunar date conversion
  function toLunar(y, m, d) {
    const n = dayNum(y, m, d);
    const arr = C.months;
    let lo = 0, hi = arr.length - 1, idx = -1;
    while (lo <= hi) { const mid = (lo + hi) >> 1; if (Math.floor(arr[mid] / 100) <= n) { idx = mid; lo = mid + 1; } else hi = mid - 1; }
    if (idx < 0 || idx >= arr.length - 1) return null;
    const v = arr[idx], start = Math.floor(v / 100), leap = v % 2, month = ((v % 100) - leap) / 2;
    const len = Math.floor(arr[idx + 1] / 100) - start;
    return { month, leap: !!leap, day: n - start + 1, monthLen: len, year: lunarYearOf(y, m, d) };
  }
  function fromLunar(ly, lm, ld, leap) {
    const arr = C.months;
    const cny = C.cny[ly]; if (!cny) return null;
    const c = parseISO(cny), startN = dayNum(c.y, c.m, c.d);
    for (let i = 0; i < arr.length - 1; i++) {
      const v = arr[i], s = Math.floor(v / 100); if (s < startN) continue;
      const lp = v % 2, mo = ((v % 100) - lp) / 2;
      if (mo === lm && !!lp === !!leap) {
        const len = Math.floor(arr[i + 1] / 100) - s;
        if (ld > len) return null;
        return fromDayNum(s + ld - 1);
      }
      if (i > 0 && s > startN + 400) break;
    }
    return null;
  }

  // Solar terms
  function termsOfYear(y) {
    const a = dayNum(y, 1, 1), b = dayNum(y + 1, 1, 1), out = [];
    C.terms.forEach((n, i) => { if (n >= a && n < b) out.push({ date: iso(fromDayNum(n)), idx: mod(C.t0 + i, 24) }); });
    return out.map(t => ({ ...t, name: TERMS[t.idx], zh: TERMS_ZH[t.idx] }));
  }
  // month branch by solar "jie" terms (odd indices)
  function solarMonth(n) {
    const arr = C.terms; let idx = -1;
    for (let i = arr.length - 1; i >= 0; i--) { const ti = mod(C.t0 + i, 24); if (arr[i] <= n && ti % 2 === 1) { idx = ti; break; } }
    if (idx < 0) return null;
    return mod((idx - 3) / 2 + 2, 12);
  }
  function lichunYear(y, m, d) {
    const n = dayNum(y, m, d), ts = termsOfYear(y).find(t => t.idx === 3);
    if (!ts) return y;
    const l = parseISO(ts.date);
    return n < dayNum(l.y, l.m, l.d) ? y - 1 : y;
  }
  function dayPillar(y, m, d) {
    const idx = mod(dayNum(y, m, d) - dayNum(2000, 1, 7), 60); // 2000-01-07 = 甲子
    return { s: idx % 10, b: idx % 12, idx };
  }
  function fourPillars(y, m, d, hour) {
    const yy = lichunYear(y, m, d), yp = pillarOfYear(yy);
    const mb = solarMonth(dayNum(y, m, d));
    const ms = mod((yp.s % 5) * 2 + 2 + mod(mb - 2, 12), 10);
    const dp = dayPillar(y, m, d);
    let hp = null;
    if (hour !== null && hour !== undefined && hour !== "") {
      const hb = Math.floor((Number(hour) + 1) / 2) % 12;
      const ds = Number(hour) >= 23 ? dp.s + 1 : dp.s; // late Rat hour uses next day's stem
      hp = { s: mod((ds % 5) * 2 + hb, 10), b: hb };
    }
    const pillars = { year: yp, month: { s: ms, b: mb }, day: { s: dp.s, b: dp.b }, hour: hp };
    const count = [0, 0, 0, 0, 0];
    Object.values(pillars).forEach(p => { if (!p) return; count[stemElement(p.s)]++; count[BRANCH_ELEMENT[p.b]]++; });
    return { pillars, count, dayMaster: { stem: dp.s, element: ELEMENTS[stemElement(dp.s)], yy: yinYang(dp.s) } };
  }
  function officer(y, m, d) {
    const n = dayNum(y, m, d), mb = solarMonth(n), dp = dayPillar(y, m, d);
    if (mb === null) return null;
    return OFFICERS[mod(dp.b - mb, 12)];
  }

  // Zodiac compatibility
  const TRINE = [[0, 4, 8], [1, 5, 9], [2, 6, 10], [3, 7, 11]];
  const HARMONY = [[0, 1], [2, 11], [3, 10], [4, 9], [5, 8], [6, 7]];
  const HARM = [[0, 7], [1, 6], [2, 5], [3, 4], [8, 11], [9, 10]];
  const pairIn = (list, a, b) => list.some(p => (p[0] === a && p[1] === b) || (p[0] === b && p[1] === a));
  function compatibility(a, b) {
    if (a === b) return { score: 72, label: "Same sign", note: "Shared instincts and values — easy understanding, but you may mirror each other's blind spots." };
    if (pairIn(HARMONY, a, b)) return { score: 95, label: "Six Harmony 六合", note: "The classic 'secret friend' pairing — complementary energies that stabilise each other." };
    if (TRINE.some(t => t.includes(a) && t.includes(b))) return { score: 90, label: "Triad 三合", note: "Members of the same trine share outlook and pace — a natural alliance in love and business." };
    if (mod(a - b, 12) === 6) return { score: 35, label: "Clash 六冲", note: "Direct opposites on the zodiac wheel. Attraction can be strong but friction is frequent — needs deliberate compromise." };
    if (pairIn(HARM, a, b)) return { score: 48, label: "Harm 六害", note: "A subtle mismatch — misunderstandings build quietly. Communicate early and often." };
    return { score: 66, label: "Neutral", note: "No classical bond or conflict — the relationship is shaped by effort, element balance and timing." };
  }

  // Lucky number analyzer
  const DIGITS = {
    "0": { zh: "零 líng", m: "Wholeness, beginnings; sounds like 良 (good) in some readings", w: 1 },
    "1": { zh: "一 yī / 幺 yāo", m: "Firstness, independence, leading", w: 1 },
    "2": { zh: "二 èr", m: "Pairs and harmony — 'good things come in pairs' (好事成双)", w: 2 },
    "3": { zh: "三 sān", m: "Sounds like 生 (life/birth) in Cantonese", w: 1 },
    "4": { zh: "四 sì", m: "Sounds like 死 (death) — widely avoided", w: -9 },
    "5": { zh: "五 wǔ", m: "The Five Elements; can sound like 无 (without) — neutral", w: 0 },
    "6": { zh: "六 liù", m: "Smooth, flowing (六六大顺); prosperity 祿 in Cantonese", w: 5 },
    "7": { zh: "七 qī", m: "Togetherness (起); also the ghost month — mixed", w: 0 },
    "8": { zh: "八 bā", m: "Sounds like 发 (fā, prosper) — the luckiest digit", w: 8 },
    "9": { zh: "九 jiǔ", m: "Sounds like 久 (long-lasting) — longevity, eternity", w: 4 }
  };
  const COMBOS = [
    ["1314", 9, "一生一世 — 'one life, one lifetime' (love forever)"],
    ["168", 10, "一路发 — 'prosper all the way'"],
    ["518", 8, "我要发 — 'I will prosper'"],
    ["520", 6, "我爱你 — 'I love you'"],
    ["888", 14, "Triple prosperity"], ["666", 10, "Triple smoothness — 六六大顺"],
    ["999", 9, "Everlasting"], ["88", 6, "Double prosperity (囍 feel)"], ["66", 4, "Double smooth"],
    ["99", 3, "Long-lasting"], ["16", 3, "一路 — 'all the way'"], ["28", 5, "易发 — 'easy prosperity' (Cantonese)"],
    ["14", -10, "要死 — sounds like 'want to die'"], ["74", -7, "气死 — 'furious'"], ["44", -8, "Double 4"],
    ["250", -6, "二百五 — slang for 'idiot'"], ["58", 4, "唔发 / 我发 — prosperity reading"]
  ];
  function analyzeNumber(raw) {
    const s = String(raw).replace(/[^0-9]/g, "");
    if (!s) return null;
    let score = 50; const notes = []; const digits = {};
    for (const ch of s) digits[ch] = (digits[ch] || 0) + 1;
    Object.keys(digits).sort().forEach(k => { const w = DIGITS[k].w * Math.min(digits[k], 4) * (8 / Math.max(s.length, 8)); score += w; });
    let comboHits = [];
    COMBOS.forEach(([p, w, desc]) => {
      if (p === "14" && s.includes("1314")) return;
      let i = s.indexOf(p), c = 0; while (i !== -1) { c++; i = s.indexOf(p, i + p.length); }
      if (c) { score += w * Math.min(c, 2); comboHits.push({ p, w, desc, c }); }
    });
    const last = s[s.length - 1];
    if (last === "8" || last === "9" || last === "6") { score += 4; notes.push(`Ends in ${last} — endings carry extra weight in Chinese number reading.`); }
    if (last === "4") { score -= 6; notes.push("Ends in 4 — the most avoided ending."); }
    if (/(\d)\1\1/.test(s)) { score += 4; notes.push("Contains a triple repeat — memorable and prized."); }
    if (/(\d\d)\1/.test(s)) { score += 3; notes.push("Contains a repeating pair pattern (e.g. 6060) — rhythmic and easy to recall."); }
    if (/0123|1234|2345|3456|5678|6789/.test(s)) { score += 3; notes.push("Contains an ascending run — reads as 'rising step by step' (步步高)."); }
    if (!s.includes("4")) { score += 3; notes.push("No 4 anywhere — a key requirement for many buyers."); }
    score = Math.max(1, Math.min(99, Math.round(score)));
    const grade = score >= 85 ? ["Supremely auspicious", "大吉"] : score >= 70 ? ["Very auspicious", "吉"] : score >= 55 ? ["Favourable", "小吉"] : score >= 40 ? ["Neutral", "平"] : ["Unfavourable", "凶"];
    return { s, score, grade, digits, comboHits, notes, sum: [...s].reduce((a, b) => a + +b, 0) };
  }

  window.Calc = {
    STEMS, STEMS_PY, BRANCHES, BRANCHES_PY, ANIMALS, ANIMAL_ZH, ANIMAL_EMOJI, ELEMENTS, ELEMENT_ZH, BRANCH_ELEMENT,
    TERMS, TERMS_ZH, OFFICERS, LUNAR_MONTHS, SHICHEN, DIGITS, COMBOS,
    mod, dayNum, fromDayNum, iso, parseISO, inRange, lunarYearOf, pillarOfYear, sexagenaryIndex, gz, stemElement, yinYang,
    zodiac, toLunar, fromLunar, termsOfYear, solarMonth, lichunYear, dayPillar, fourPillars, officer, compatibility, analyzeNumber
  };
})();
