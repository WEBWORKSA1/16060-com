from layout import page, ad, TOOLS, wheel_svg, esc
import json

ANIMALS = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
AZH = "鼠牛虎兔龙蛇马羊猴鸡狗猪"
EMO = ["🐀", "🐂", "🐅", "🐇", "🐉", "🐍", "🐎", "🐐", "🐒", "🐓", "🐕", "🐖"]


def zgrid():
    return '<div class="zgrid">' + "".join(
        f'<a class="z" href="{{root}}zodiac/{a.lower()}.html"><b>{AZH[i]}</b><span>{EMO[i]} {a}</span><small>{", ".join(str(y) for y in (1984+i, 1996+i, 2008+i))}</small></a>'
        for i, a in enumerate(ANIMALS)) + "</div>"


def tool_cards(n=9):
    return "".join(f'<a class="card hover reveal" href="{{root}}{p}"><div class="ic">{ic}</div><h3>{t}</h3><p>{d}</p></a>' for p, t, d, ic in TOOLS[:n])


FAQ_HOME = [
    ("What does 16060 mean?", "Read aloud as “1 · 60 · 60”, it maps to time — one hour is sixty minutes of sixty seconds — and to the Chinese 60-year cycle (甲子). The digits carry positive associations: 6 (liù) evokes “smooth” (六六大顺), 0 wholeness, and 1-6 echoes 一路 (“all the way”). There is no 4. See our full explainer."),
    ("Are the tools free?", "Yes. Every calculator is free, with no sign-up. The optional Lucky Blueprint asks for your email so we can send your report and follow-ups; unsubscribe any time."),
    ("How accurate is the zodiac calculator?", "It uses astronomically computed Lunar New Year dates and solar terms for 1921–2060, so people born in January or February get the right animal. BaZi pillars change at the solar terms and are computed to the day."),
    ("Is this fortune-telling?", "We present Chinese number symbolism and calendar traditions for cultural education and entertainment. Nothing here is financial, legal or medical advice."),
    ("Can I advertise, sponsor or partner?", "Yes — see the Advertise page, or use the inquiry link at the top of every page."),
]


def faq(items):
    sch = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items), sch


def build():
    fh, fsch = faq(FAQ_HOME)
    home = f'''
<section class="hero"><div class="wrap hero-grid">
<div><span class="eyebrow">一 · 六十 · 六十 &nbsp;|&nbsp; Luck · Time · Culture</span>
<h1>Find your lucky numbers, your sign and your <span style="color:var(--gold)">perfect timing</span>.</h1>
<p class="lead">Free calculators for Chinese lucky numbers, the zodiac, the 60-year cycle, BaZi and auspicious dates, plus world clocks and festival countdowns. Built on real calendar data.</p>
<div class="hero-cta"><a class="btn lg" href="{{root}}tools/lucky-number.html">Score my number</a><a class="btn gold lg" href="{{root}}consult.html#blueprint">Free Lucky Blueprint</a></div>
<form class="news" action="{{root}}tools/lucky-number.html" method="get" style="max-width:520px" aria-label="Quick lucky number check">
<label class="sr" for="qn">Number to check</label><input id="qn" name="n" inputmode="numeric" placeholder="Try a phone, plate or price, e.g. 16060" required><button class="btn gold sm" type="submit">Check</button></form>
<div class="trust" style="margin-top:18px"><span>Free, no sign-up</span><span>1921–2060 calendar data</span><span>Shareable results</span></div></div>
<div class="hero-art">{wheel_svg()}</div></div></section>

<section style="padding-top:28px"><div class="wrap"><div class="section-head"><div><span class="eyebrow">Today</span><h2>Today's almanac at a glance</h2></div><a href="{{root}}tools/auspicious-dates.html">Find auspicious dates →</a></div><div data-today></div></div></section>

<div class="wrap">{ad("top")}</div>

<section class="alt"><div class="wrap"><div class="section-head"><div><span class="eyebrow">Free tools</span><h2>Nine calculators, one purpose: better timing</h2></div><p>Each result has its own link you can share, and a print-ready layout.</p></div>
<div class="grid g3">{tool_cards()}</div></div></section>

<section><div class="wrap"><div class="section-head"><div><span class="eyebrow">十二生肖</span><h2>The 12 zodiac animals</h2></div><p>Personality, lucky numbers and colours, best matches and the year ahead for every sign.</p></div>{zgrid()}
<p class="center" style="margin-top:20px"><a class="btn ghost" href="{{root}}tools/zodiac-finder.html">Not sure of your sign? Find it by exact birth date →</a></p></div></section>

<section class="alt"><div class="wrap"><div class="cta-band reveal" id="lead">
<div><span class="eyebrow" style="color:#ffe6a8">Free · instant · personal</span><h2>Get your personal Lucky Blueprint</h2>
<p>Your zodiac and element, your Four Pillars chart, your lucky numbers and your 6 strongest days in the next 60. Generated in seconds and ready to print.</p>
<div class="trust" style="color:#ffdcd0"><span>No payment</span><span>Printable PDF</span><span>Unsubscribe anytime</span></div></div>
<div><a class="btn gold lg block" href="{{root}}consult.html#blueprint">Create my blueprint →</a><p class="small" style="margin:10px 0 0;text-align:center">Planning a wedding, launch or move? <a style="color:#ffe6a8" href="{{root}}consult.html#consult">Book a pro consultation</a></p></div>
</div></div></section>

<section><div class="wrap"><div class="section-head"><div><span class="eyebrow">Countdown</span><h2>Lunar New Year 2027 — Year of the Fire Goat 丁未</h2></div><a href="{{root}}tools/countdown.html">All festival countdowns →</a></div>
<div class="countdown" data-countdown="2027-02-06T00:00:00"></div>
<p class="muted" style="margin-top:12px">Saturday 6 February 2027. The Fire Horse year (丙午) began on 17 February 2026.</p></div></section>

<section class="alt"><div class="wrap"><div class="section-head"><div><span class="eyebrow">Learn</span><h2>Guides worth reading</h2></div><a href="{{root}}learn/index.html">All guides →</a></div>
<div class="grid g3">
<a class="card hover" href="{{root}}learn/what-does-16060-mean.html"><span class="chip gold">Explainer</span><h3 style="margin-top:10px">What does 16060 mean?</h3><p>Time, the 60-year cycle and the symbolism of 1, 6 and 0.</p></a>
<a class="card hover" href="{{root}}learn/chinese-lucky-numbers-guide.html"><span class="chip gold">Guide</span><h3 style="margin-top:10px">Chinese lucky numbers 0–9</h3><p>Why 8 prospers, 4 is avoided, and what 168, 520 and 1314 mean.</p></a>
<a class="card hover" href="{{root}}learn/lucky-number-economy.html"><span class="chip gold">Economy</span><h3 style="margin-top:10px">The lucky-number economy</h3><p>US$280k phone numbers, HK$26M licence plates and 5-digit domains.</p></a>
</div></div></section>

<section><div class="wrap"><div class="section-head"><div><span class="eyebrow">Watch</span><h2>Videos</h2></div><a href="{{root}}videos.html">Video library →</a></div><div class="videos" data-videos="3"></div></div></section>

<div class="wrap">{ad("inContent")}</div>

<section class="alt"><div class="wrap grid g3">
<div class="card"><div class="ic">🏆</div><h3>Win in our contest</h3><p>Share your lucky-number story for a share of the prize pool.</p><p style="margin-top:12px"><a href="{{root}}contests.html">Enter the contest →</a></p></div>
<div class="card"><div class="ic">🧧</div><h3>Send a red envelope</h3><p>Help keep every tool free, fund new features and pay for prizes.</p><p style="margin-top:12px"><a href="{{root}}support.html">Support 16060 →</a></p></div>
<div class="card"><div class="ic">✍️</div><h3>Work with us</h3><p>We're looking for writers, video creators, developers and consultants.</p><p style="margin-top:12px"><a href="{{root}}careers.html">See open roles →</a></p></div>
</div></section>

<section><div class="narrow"><h2 class="center">Questions</h2>{fh}</div></section>
'''
    page("index.html", "16060 — Chinese Lucky Numbers, Zodiac & Auspicious Timing Tools",
         "Free Chinese lucky number analyzer, zodiac finder, 60-year cycle, BaZi four pillars, auspicious date finder, lunar converter and festival countdowns.",
         home, scripts=("caldata.js", "calc.js", "festivals.js", "tools.js"), schema=fsch, priority="1.0")

    # ---------- tools index ----------
    page("tools/index.html", "Free Chinese Calendar & Lucky Number Tools", "All 16060 calculators: lucky numbers, zodiac, compatibility, 60-year cycle, lunar converter, BaZi, auspicious dates, clocks and countdowns.",
         f'<section><div class="wrap"><div class="grid g3">{tool_cards()}</div>{ad()}</div></section>',
         hero=("All tools", "Nine free calculators built on astronomical calendar data from 1921 to 2060. Results are shareable and printable."), crumbs=[("Tools", "tools/index.html")], priority="0.9")

    side = f'<aside class="sidebar no-print">{ad("sidebar")}<div class="card"><h3>More tools</h3><ul style="padding-left:1.1em;margin:0">' + "".join(f'<li><a href="{{root}}{p}">{t}</a></li>' for p, t, d, ic in TOOLS) + '</ul></div><div class="card"><h3>🧧 Free Blueprint</h3><p>Your full personal report in seconds.</p><p style="margin-top:10px"><a class="btn sm block" href="{root}consult.html#blueprint">Get it free</a></p></div></aside>'

    def tool_page(path, title, h1, sub, desc, inner, explainer, faqs, extra_scripts=()):
        fh, fsch = faq(faqs)
        app_schema = {"@context": "https://schema.org", "@type": "WebApplication", "name": title, "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "url": "https://16060.com/" + path}
        body = f'''<section><div class="wrap tool"><div>{inner}
{ad()}
<article class="prose" style="margin-top:30px">{explainer}</article>
<h2 style="margin-top:34px">FAQ</h2>{fh}
<div style="margin-top:26px" class="videos" data-videos="2"></div></div>{side}</div></section>'''
        page(path, title, desc, body, scripts=("caldata.js", "calc.js", "festivals.js") + tuple(extra_scripts) + ("tools.js",),
             schema=[app_schema, fsch], hero=(h1, sub), crumbs=[("Tools", "tools/index.html"), (title, path)], priority="0.9")

    # Lucky number
    tool_page("tools/lucky-number.html", "Lucky Number Analyzer", "Chinese Lucky Number Analyzer <span class=\"zh\" style=\"color:var(--red)\">吉数</span>",
              "Score any phone number, licence plate, house number, price or numeric domain using traditional Chinese number symbolism.",
              "Check if a phone number, licence plate, address, price or domain is lucky in Chinese culture. Instant score with digit meanings and combos like 168, 518, 520.",
              '''<div class="panel" data-tool="lucky-number"><form class="form" autocomplete="off">
<label>Your number <input name="n" inputmode="numeric" placeholder="e.g. 16060, 138-8888-1688, 518" required></label>
<button class="btn lg" type="submit">Analyze number</button></form>
<p class="small muted" style="margin-top:10px">Try: <button class="btn ghost sm" type="button" data-try="16060">16060</button> <button class="btn ghost sm" type="button" data-try="168">168</button> <button class="btn ghost sm" type="button" data-try="88888888">88888888</button> <button class="btn ghost sm" type="button" data-try="1314520">1314520</button> <button class="btn ghost sm" type="button" data-try="4414">4414</button></p>
<div class="result"></div></div>''',
              '''<h2>How the score works</h2><p>Every digit carries a traditional association, mostly from how it sounds in Mandarin or Cantonese. <b>8</b> (bā) sounds like 发 (fā, “prosper”), <b>6</b> (liù) evokes “smooth” (六六大顺), <b>9</b> (jiǔ) sounds like 久 (“long-lasting”), and <b>4</b> (sì) sounds like 死 (“death”). The analyzer weights each digit, then adds or subtracts for well-known combinations (168 一路发, 518 我要发, 520 我爱你, 1314 一生一世, 14 要死), for endings, repeats, ascending runs, and for the absence of 4.</p>
<h2>Where lucky numbers matter</h2><ul><li><b>Phone numbers</b>: in 2003 Sichuan Airlines paid ¥2.33 million (about US$280,000) for the number 8888-8888.</li><li><b>Licence plates</b>: Hong Kong's plate “W” sold for HK$26 million in 2021, and “28” (“easy prosperity” in Cantonese) for HK$18.1 million.</li><li><b>Property</b>: a study of Vancouver sales found addresses ending in 8 sold at about a 2.5% premium in Chinese-majority areas, and those ending in 4 at a 2.2% discount.</li><li><b>Prices &amp; domains</b>: retailers price at ¥88 and ¥168, and numeric .com domains without a 4 are worth far more to Chinese buyers.</li></ul>
<p>Sources and more figures are in our <a href="../learn/lucky-number-economy.html">lucky-number economy guide</a>.</p>''',
              [("Is 16060 a lucky number?", "It scores well: no 4, two 6s (smooth), a rhythmic 6060 repeat, and 16 echoes 一路 (“all the way”). It has no 8, so it isn't in the top tier."),
               ("Does the number have to be all digits?", "Enter anything; we strip non-digits. Plates with letters are scored on their digits."),
               ("Why is 4 unlucky but 14 worse?", "4 sounds like 死 (death), and 14 reads as 要死 (“going to die”). 1314 is the exception: it reads 一生一世, “a whole lifetime”."),
               ("Is this the same in Cantonese?", "Mostly. Cantonese adds a few readings, e.g. 3 as 生 (life) and 28 as 易发 (easy prosperity).")])

    # Zodiac finder
    tool_page("tools/zodiac-finder.html", "Chinese Zodiac Finder", "Chinese Zodiac Finder <span class=\"zh\" style=\"color:var(--red)\">生肖</span>",
              "Enter your exact birth date. We use the real Lunar New Year date for your birth year, so January and February birthdays get the right animal.",
              "Find your Chinese zodiac animal, element and yin-yang by exact birth date, with Lunar New Year boundaries from 1921 to 2060.",
              '''<div class="panel" data-tool="zodiac-finder"><form class="form"><label>Date of birth <input type="date" name="d" min="1921-01-01" max="2060-12-31" required></label><button class="btn lg" type="submit">Find my sign</button></form><div class="result"></div></div>''',
              '''<h2>Why your Gregorian birth year isn't enough</h2><p>The zodiac year starts at Lunar New Year, which falls between 21 January and 20 February. Someone born on 20 January 1990 is a <b>Snake</b> (the 1989 year), not a Horse, because the Horse year only began on 27 January 1990. This tool looks up the exact New Year date for your birth year.</p>
<h2>Animal, element and yin-yang</h2><p>Each year combines one of the <b>12 Earthly Branches</b> (the animals) with one of the <b>10 Heavenly Stems</b>, which give an element (Wood, Fire, Earth, Metal, Water) and a polarity (yin or yang). Together they make the 60-year cycle, so a Metal Horse returns only every 60 years.</p>''',
              [("Which date does the zodiac year start?", "Popular zodiac uses Lunar New Year. BaZi practitioners start the year at 立春, the Start of Spring (about 4 February). Our Four Pillars tool uses that rule."),
               ("What's my element?", "It comes from the last digit of the Chinese year: 0–1 Metal, 2–3 Water, 4–5 Wood, 6–7 Fire, 8–9 Earth."),
               ("What sign is 2026?", "2026 is the Fire Horse (丙午), from 17 February 2026 to 5 February 2027. 2027 is the Fire Goat (丁未).")])

    # Compatibility
    tool_page("tools/compatibility.html", "Zodiac Compatibility Calculator", "Zodiac Compatibility <span class=\"zh\" style=\"color:var(--red)\">合婚</span>",
              "Test any two signs for love, friendship or business, using the classical Six Harmonies, Triads, Clashes and Harms.",
              "Chinese zodiac compatibility calculator for love and business, with the full 12×12 compatibility matrix.",
              '''<div class="panel" data-tool="compatibility"><div class="row"><label>First sign <select name="a"></select></label><label>Second sign <select name="b"></select></label></div><div class="result"></div>
<h3 style="margin-top:22px">Full compatibility matrix</h3><div class="matrix"></div></div>''',
              '''<h2>The four classical relationships</h2><ul><li><b>Six Harmonies 六合</b>: Rat–Ox, Tiger–Pig, Rabbit–Dog, Dragon–Rooster, Snake–Monkey, Horse–Goat. These are the “secret friends”.</li><li><b>Triads 三合</b>: Rat–Dragon–Monkey, Ox–Snake–Rooster, Tiger–Horse–Dog, Rabbit–Goat–Pig. Allies who share an outlook.</li><li><b>Clashes 六冲</b>: signs directly opposite each other on the wheel, six apart.</li><li><b>Harms 六害</b>: quieter mismatches that breed misunderstanding.</li></ul><p>Scores are a simplified guide. Practitioners compare full birth charts, where the elements often matter more than the animals.</p>''',
              [("Which signs are most compatible?", "The Six Harmony pairs and members of the same triad score highest."), ("Can clashing signs marry?", "Of course. Traditional practice suggests extra care with timing and communication, not avoidance.")])

    # 60-year cycle
    tool_page("tools/sixty-year-cycle.html", "60-Year Cycle (Jiazi) Table", "The 60-Year Cycle <span class=\"zh\" style=\"color:var(--red)\">六十甲子</span>",
              "All sixty stem–branch combinations with each year's element, animal and exact New Year date. Filter by animal or element.",
              "Complete Chinese sexagenary (Jiazi) cycle table: all 60 stem-branch years with elements, animals and Lunar New Year dates.",
              '''<div class="panel" data-tool="sixty-year-cycle"><div class="row"><label>Cycle <select name="start"><option value="1924">1924 – 1983</option><option value="1984" selected>1984 – 2043</option><option value="2044">2044 – 2103</option></select></label><label>Filter <select name="f"></select></label></div><div class="result" style="margin-top:16px"></div></div>''',
              '''<h2>How the cycle works</h2><p>Ten Heavenly Stems (甲乙丙丁戊己庚辛壬癸) and twelve Earthly Branches (子丑寅卯辰巳午未申酉戌亥) advance together. Because the lowest common multiple of 10 and 12 is 60, the pairing repeats every sixty years. The first combination, 甲子 (Jiǎzǐ), names the whole cycle. The current cycle began in 1984.</p><p>Completing one cycle, your 60th birthday (花甲 or 甲子 “return”), is a major longevity milestone in Chinese culture. The same 60-count also names days, so every date has its own pillar. See it in the <a href="lunar-converter.html">Lunar Converter</a>.</p>''',
              [("When did the current cycle begin?", "In 1984, the Wood Rat year (甲子). The next begins in 2044."), ("Why 60?", "It's the lowest common multiple of 10 stems and 12 branches.")])

    # Lunar converter
    tool_page("tools/lunar-converter.html", "Chinese Lunar Calendar Converter", "Lunar Calendar Converter <span class=\"zh\" style=\"color:var(--red)\">农历</span>",
              "Convert between Gregorian and Chinese lunar dates (1921–2060). Shows leap months, the day pillar, the day officer and solar terms.",
              "Convert Gregorian dates to Chinese lunar calendar dates and back, with leap months, day pillar and solar terms.",
              '''<div class="panel" data-tool="lunar-converter"><h3>Gregorian → Lunar</h3><form id="g2l" class="form"><div class="row"><label>Date <input type="date" name="d" min="1921-02-08" max="2060-12-31" required></label><div style="align-self:end"><button class="btn block" type="submit">Convert</button></div></div></form><div id="g2l-out" class="result"></div>
<h3 style="margin-top:26px">Lunar → Gregorian</h3><form id="l2g" class="form"><div class="row"><label>Lunar year <input type="number" name="y" min="1921" max="2059" required></label><label>Month (1–12) <input type="number" name="m" min="1" max="12" value="1" required></label></div><div class="row"><label>Day (1–30) <input type="number" name="d" min="1" max="30" value="1" required></label><label class="check" style="align-self:end"><input type="checkbox" name="leap"> Leap month (闰月)</label></div><button class="btn" type="submit">Convert</button></form><div id="l2g-out" class="result"></div></div>''',
              '''<h2>About the Chinese calendar</h2><p>The traditional calendar is <b>lunisolar</b>. Months begin on the new moon and last 29 or 30 days. A leap month is added about seven times every 19 years so the calendar keeps pace with the seasons, which are tracked separately by the 24 solar terms (节气). Birthdays, festivals and many family events still follow lunar dates.</p>''',
              [("What is a leap month?", "An extra month, repeated after a regular one, added when a lunar month contains no major solar term."), ("Which range is supported?", "1921 to 2060, from astronomical calculations.")])

    # Four pillars
    tool_page("tools/four-pillars.html", "Four Pillars (BaZi) Calculator", "Four Pillars of Destiny <span class=\"zh\" style=\"color:var(--red)\">八字</span>",
              "Your BaZi chart: year, month, day and hour pillars, with year and month set by the solar terms, plus your five-element balance and Day Master.",
              "Free BaZi (Four Pillars of Destiny) calculator: year, month, day and hour pillars, Day Master and five-element balance.",
              '''<div class="panel" data-tool="four-pillars"><form class="form"><div class="row"><label>Date of birth <input type="date" name="d" min="1921-01-01" max="2060-12-31" required></label><label>Birth hour <span class="opt">(optional)</span><select name="h"><option value="">Unknown</option>''' +
              "".join(f'<option value="{h}">{h:02d}:00 – {h:02d}:59</option>' for h in range(24)) + '''</select></label></div><button class="btn lg" type="submit">Calculate my pillars</button></form><div class="result"></div></div>''',
              '''<h2>What the four pillars are</h2><p>BaZi (八字, “eight characters”) describes the moment of birth as four stem–branch pairs: year, month, day and hour. The <b>day stem</b> is the Day Master, the “self” of the chart. Each character belongs to one of the Five Elements, and practitioners read the balance and interplay between them.</p><h2>Solar terms, not calendar months</h2><p>BaZi months follow the 12 “jié” solar terms. The year changes at 立春 (Start of Spring, about 4 February), not at Lunar New Year. That's why your BaZi year animal can differ from your popular zodiac animal.</p>''',
              [("Do I need my birth time?", "No. Without it you get three pillars (six characters). The hour pillar adds detail."), ("How do I read the chart properly?", "The free tool shows structure and balance. A full reading covers 10-year luck pillars and interactions, which you can request from a consultant.")])

    # Auspicious dates
    tool_page("tools/auspicious-dates.html", "Auspicious Date Finder", "Auspicious Date Finder <span class=\"zh\" style=\"color:var(--red)\">择日</span>",
              "Find traditionally favourable days for weddings, business openings, moving, travel and signing, and avoid days that clash with your sign.",
              "Find auspicious dates for weddings, business openings, moving house and signing contracts using the Chinese 12 Day Officers system.",
              '''<div class="panel" data-tool="auspicious-dates"><form class="form"><div class="row"><label>Event <select name="event"><option value="wedding">Wedding / engagement</option><option value="opening">Business opening / launch</option><option value="moving">Moving house</option><option value="signing">Signing a contract</option><option value="travel">Travel</option><option value="general">General</option></select></label>
<label>Your birth year <span class="opt">(to avoid clash days)</span><input type="number" name="by" min="1921" max="2060" placeholder="e.g. 1988"></label></div>
<div class="row"><label>Start date <input type="date" name="start" required></label><label>Look ahead <select name="days"><option>30</option><option selected>60</option><option>90</option></select></label></div>
<button class="btn lg" type="submit">Find my dates</button></form><div class="result"></div></div>''',
              '''<h2>The 12 Day Officers</h2><p>The Chinese almanac (通胜 Tung Shing) gives each day one of twelve “officers” (建除十二神): Establish, Remove, Full, Balance, Stable, Initiate, Destruction, Danger, Success, Receive, Open and Close. The day is set by comparing that day's earthly branch with the solar month's branch. A classic rhyme sorts them into “yellow” (usable) and “black” (avoid) days. <b>Success 成</b> and <b>Open 开</b> are favourites for weddings and openings.</p><h2>Clash days</h2><p>Every day has a branch, and the branch directly opposite it “clashes”. On a Horse day, for example, people born in Rat years traditionally avoid major events. Enter your birth year and we flag those days.</p>''',
              [("Is this the same as a professional date selection?", "It's a reliable first filter. Professional 择日 also checks hours, both people's full charts and additional stars."), ("Does my timezone matter?", "Dates are calendar days; for hour selection, use local time.")])

    # Clocks
    tool_page("tools/clocks-timers.html", "World Clocks, Shichen, Stopwatch & Timer", "1 · 60 · 60 <span class=\"zh\" style=\"color:var(--red)\">时间</span>",
              "One hour, sixty minutes, sixty seconds. World clocks for Chinese-speaking hubs, the traditional double-hour (时辰), a stopwatch and a timer.",
              "Live world clocks (Beijing, Hong Kong, Taipei, Singapore), the Chinese double-hour shichen, stopwatch and countdown timer.",
              '''<div class="panel" data-tool="clocks-timers"><small class="muted">Your local time</small><div class="bigtime">--:--:--</div>
<div class="big-score shichen" style="justify-content:center;margin-bottom:20px"></div>
<div class="clock-grid"></div>
<div class="grid g2" style="margin-top:24px"><div class="card"><h3>Stopwatch</h3><div class="bigtime sw" style="font-size:2.6rem">00:00.00</div><p class="center"><button class="btn sm" data-sw="start">Start</button> <button class="btn ghost sm" data-sw="lap">Lap</button> <button class="btn ghost sm" data-sw="reset">Reset</button></p><ol class="laps small muted"></ol></div>
<div class="card"><h3>Timer</h3><div class="bigtime tv" style="font-size:2.6rem">00:00:00</div><p class="center"><button class="btn ghost sm" data-t="60">1 min</button> <button class="btn ghost sm" data-t="600">10 min</button> <button class="btn ghost sm" data-t="1500">25 min</button> <button class="btn gold sm" data-t="3600">1 hour · 60·60</button></p>
<div class="row" style="grid-template-columns:repeat(3,1fr)"><input name="th" type="number" min="0" placeholder="h" aria-label="hours"><input name="tm" type="number" min="0" max="59" placeholder="m" aria-label="minutes"><input name="ts" type="number" min="0" max="59" placeholder="s" aria-label="seconds"></div><p class="center" style="margin-top:10px"><button class="btn sm" data-timer="go">Start</button> <button class="btn ghost sm" data-timer="stop">Stop</button></p></div></div></div>''',
              '''<h2>一寸光阴一寸金</h2><p>“An inch of time is an inch of gold, but an inch of gold cannot buy an inch of time.” Traditional China divided the day into twelve <b>shichen</b> (时辰) of two hours each, named after the earthly branches. 子时 (23:00–00:59) starts the day. Each double-hour is linked to a zodiac animal, and BaZi uses it for the hour pillar.</p><p>Base-60 time (60 seconds, 60 minutes) comes from ancient Mesopotamia. Chinese tradition has its own 60-count in the 甲子 cycle. 16060, one hour of sixty minutes of sixty seconds, sits where the two meet.</p>''',
              [("What shichen is it now?", "See the live panel above. It updates every second."), ("Why is 23:00 the start of the day?", "The Rat hour 子时 straddles midnight. Some BaZi schools switch the day pillar at 23:00.")])

    # Countdown
    tool_page("tools/countdown.html", "Lunar New Year & Festival Countdown", "Festival Countdowns <span class=\"zh\" style=\"color:var(--red)\">倒计时</span>",
              "Live countdowns to Lunar New Year and every major Chinese festival, plus a builder for your own shareable countdown.",
              "Countdown to Chinese New Year 2027 and all Chinese festivals, and create your own shareable countdown link.",
              '''<div data-tool="countdown"><div class="panel"><h3>Create your own countdown</h3><form class="form"><div class="row"><label>Title <input name="t" placeholder="Our wedding · Store opening"></label><label>Date <input type="date" name="d" required></label></div><div class="row"><label>Time <input type="time" name="tm" value="08:08"></label><div style="align-self:end"><button class="btn block" type="submit">Create countdown</button></div></div></form></div><div class="my-cd result"></div>
<h3 style="margin-top:26px">Upcoming festivals</h3><div class="grid g2 fest-list"></div></div>''',
              '''<h2>Why countdowns matter in Chinese culture</h2><p>Timing is central. Businesses open at 8:08, weddings are set on chosen days, and the whole world counts down to Lunar New Year. The Beijing Olympics opened at 8:08 pm on 08/08/08. Build a countdown for your own event and share the link. It updates live for everyone who opens it.</p>''',
              [("When is Chinese New Year 2027?", "Saturday, 6 February 2027 — the Year of the Fire Goat."), ("Can I embed a countdown?", "Share the generated link. Embeddable widgets are on our roadmap for sponsors.")])
