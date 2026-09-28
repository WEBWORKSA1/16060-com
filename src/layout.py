import os, json, html, math

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("OUT", os.path.join(HERE, "..", "_site"))
DOMAIN = "https://16060.com/"
PAGES = []  # for sitemap

TOOLS = [
    ("tools/lucky-number.html", "Lucky Number Analyzer", "Score any phone, plate, address or price", "八"),
    ("tools/zodiac-finder.html", "Zodiac Finder", "Your animal, element & yin-yang by exact date", "肖"),
    ("tools/compatibility.html", "Zodiac Compatibility", "Harmony, triads & clashes for any two signs", "合"),
    ("tools/sixty-year-cycle.html", "60-Year Cycle Table", "Every 甲子 year with stem, branch & element", "甲"),
    ("tools/lunar-converter.html", "Lunar Date Converter", "Gregorian ⇄ Chinese lunar calendar", "月"),
    ("tools/four-pillars.html", "Four Pillars (BaZi)", "Your birth chart & five-element balance", "柱"),
    ("tools/auspicious-dates.html", "Auspicious Date Finder", "Good days for weddings, openings & moves", "吉"),
    ("tools/clocks-timers.html", "Clocks & Timers · 1·60·60", "World clocks, shichen, stopwatch & timer", "时"),
    ("tools/countdown.html", "Countdown Builder", "Lunar New Year & custom shareable countdowns", "倒"),
]
COMMUNITY = [
    ("contests.html", "Contests & Prizes", "Enter the Lucky Number Story contest"),
    ("support.html", "Support 16060", "Red-envelope donations & memberships"),
    ("careers.html", "Careers & Talent", "Write, film, build and consult with us"),
    ("advertise.html", "Advertise & Sponsor", "Placements, sponsorships & partnerships"),
    ("about.html", "About", "Why 1 · 60 · 60"),
    ("contact.html", "Contact", "Questions, partnerships, press"),
]


def esc(s):
    return html.escape(s, quote=True)


def favicon():
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#c62828"/>'
            '<circle cx="32" cy="32" r="22" fill="none" stroke="#ffe6a8" stroke-width="2" stroke-dasharray="2 3.76"/>'
            '<text x="32" y="41" font-family="Georgia,serif" font-size="24" font-weight="700" text-anchor="middle" fill="#ffe6a8">60</text></svg>')


def wheel_svg():
    br = "子丑寅卯辰巳午未申酉戌亥"
    parts = ['<svg class="wheel" viewBox="0 0 400 400" role="img" aria-label="The sixty-year cycle wheel">',
             '<defs><radialGradient id="wg" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#d7322b" stop-opacity=".35"/><stop offset="1" stop-color="#d7322b" stop-opacity="0"/></radialGradient></defs>',
             '<circle cx="200" cy="200" r="196" fill="url(#wg)"/>',
             '<circle cx="200" cy="200" r="190" fill="none" stroke="#e3b04b" stroke-opacity=".5"/>',
             '<circle cx="200" cy="200" r="150" fill="none" stroke="#e3b04b" stroke-opacity=".35"/>',
             '<circle cx="200" cy="200" r="96" fill="none" stroke="#d7322b" stroke-opacity=".6" stroke-width="2"/>']
    for i in range(60):
        a = math.radians(i * 6 - 90)
        r1, r2 = (176, 190) if i % 5 else (166, 190)
        parts.append(f'<line x1="{200+r1*math.cos(a):.1f}" y1="{200+r1*math.sin(a):.1f}" x2="{200+r2*math.cos(a):.1f}" y2="{200+r2*math.sin(a):.1f}" stroke="#e3b04b" stroke-opacity="{0.9 if i%5==0 else 0.45}" stroke-width="{2 if i%5==0 else 1}"/>')
    for i, ch in enumerate(br):
        a = math.radians(i * 30 - 90)
        parts.append(f'<text x="{200+124*math.cos(a):.1f}" y="{200+124*math.sin(a)+9:.1f}" text-anchor="middle" class="br" font-family="Noto Serif SC,serif" font-size="26">{ch}</text>')
    parts.append('<text x="200" y="196" text-anchor="middle" font-family="Noto Serif SC,serif" font-size="44" font-weight="700" fill="#e3b04b">16060</text>')
    parts.append('<text x="200" y="228" text-anchor="middle" font-family="Inter,sans-serif" font-size="13" letter-spacing="4" class="sub">1 · 60 · 60</text>')
    parts.append('</svg>')
    return "".join(parts)


def header(root):
    tools = "".join(f'<a href="{root}{p}"><b class="zh" style="color:var(--red)">{ic}</b><div>{t}<span>{d}</span></div></a>' for p, t, d, ic in TOOLS)
    comm = "".join(f'<a href="{root}{p}"><div>{t}<span>{d}</span></div></a>' for p, t, d in COMMUNITY)
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="topbar">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership — <a href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a></div>
<header class="site-header"><nav class="wrap nav" aria-label="Main">
<a class="logo" href="{root}index.html" aria-label="16060 home"><span class="logo-mark">60</span><span>16060<small>Luck · Time · Culture</small></span></a>
<ul class="menu">
<li class="dd"><button aria-expanded="false">Tools ▾</button><div class="dd-panel">{tools}<a href="{root}tools/index.html"><div><b>All tools →</b></div></a></div></li>
<li><a href="{root}zodiac/index.html">Zodiac</a></li>
<li><a href="{root}learn/index.html">Learn</a></li>
<li><a href="{root}festivals.html">Festivals</a></li>
<li><a href="{root}videos.html">Videos</a></li>
<li class="dd"><button aria-expanded="false">Community ▾</button><div class="dd-panel">{comm}</div></li>
</ul>
<div class="nav-actions"><a class="btn sm" href="{root}consult.html">Free Blueprint</a>
<button class="icon-btn" data-theme-toggle aria-label="Toggle dark or light mode"><svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 3a9 9 0 0 1 0 18z" fill="currentColor"/></svg></button>
<button class="icon-btn burger" data-menu aria-label="Menu" aria-expanded="false">☰</button></div>
</nav></header>'''


def footer(root):
    tl = "".join(f'<li><a href="{root}{p}">{t.split(" · ")[0]}</a></li>' for p, t, d, ic in TOOLS[:7])
    return f'''<footer class="site-footer"><div class="wrap">
<div class="fgrid">
<div><a class="logo" href="{root}index.html"><span class="logo-mark">60</span><span>16060<small>Luck · Time · Culture</small></span></a>
<p class="muted small" style="margin-top:14px">One hour · sixty minutes · sixty seconds. One cycle · sixty years. Free tools and guides to Chinese lucky numbers, the zodiac and auspicious timing.</p>
<form class="news" data-form data-subject="Newsletter signup" data-done="You're on the list — watch your inbox for the next lucky-days digest.">
<label class="sr" for="nl-email">Email</label><input id="nl-email" type="email" name="email" placeholder="Your email for lucky-days alerts" required>
<input type="hidden" name="list" value="newsletter"><input class="hp" name="_honey" tabindex="-1" autocomplete="off">
<button class="btn sm" type="submit">Join</button></form></div>
<div><h4>Tools</h4><ul>{tl}</ul></div>
<div><h4>Explore</h4><ul><li><a href="{root}zodiac/index.html">12 Zodiac Animals</a></li><li><a href="{root}learn/index.html">Guides</a></li><li><a href="{root}festivals.html">Festivals</a></li><li><a href="{root}videos.html">Videos</a></li><li><a href="{root}learn/what-does-16060-mean.html">What 16060 means</a></li><li><a href="{root}consult.html">Free Blueprint &amp; Consults</a></li></ul></div>
<div><h4>Community</h4><ul><li><a href="{root}contests.html">Contests</a></li><li><a href="{root}support.html">Support / Donate</a></li><li><a href="{root}careers.html">Careers</a></li><li><a href="{root}advertise.html">Advertise</a></li><li><a href="{root}about.html">About</a></li><li><a href="{root}contact.html">Contact</a></li></ul></div>
<div><h4>Legal</h4><ul><li><a href="{root}legal/disclaimer.html">Trademark &amp; Copyright</a></li><li><a href="{root}legal/privacy.html">Privacy</a></li><li><a href="{root}legal/terms.html">Terms</a></li><li><a href="{root}legal/cookies.html">Cookies</a></li><li><a href="{root}legal/contest-rules.html">Contest Rules</a></li></ul></div>
</div>
<div class="legal-line"><span>© <span data-year>2026</span> 16060.com. Content for cultural education and entertainment. “16060” is used descriptively as a domain name; no affiliation with any other organisation using this number. <a href="{root}legal/disclaimer.html">Disclosure</a>.</span>
<span><a href="https://web.works/contact" target="_blank" rel="noopener">Acquire / sponsor this site</a></span></div>
</div></footer>
<div class="modal" id="exit-modal" hidden><div class="modal-box" role="dialog" aria-modal="true" aria-labelledby="exit-t">
<button class="modal-x" data-close aria-label="Close">×</button>
<div class="zh" style="font-size:3rem;color:var(--red)">福</div>
<h2 id="exit-t">Before you go — your free Lucky Blueprint</h2>
<p class="muted">Your zodiac, element, four pillars, lucky numbers and best dates for the next 60 days — generated instantly, free.</p>
<a class="btn gold lg block" href="{root}consult.html#blueprint">Get my free blueprint</a></div></div>
<div class="sticky-cta"><p>🧧 Free personal Lucky Blueprint</p><a class="btn sm" href="{root}consult.html#blueprint">Get it</a><button data-dismiss aria-label="Dismiss">×</button></div>'''


def ad(slot="inContent"):
    return f'<div class="ad-slot" data-slot="{slot}" aria-label="Advertisement"></div>'


def page(path, title, desc, body, scripts=(), schema=None, hero=None, crumbs=None, og_type="website", priority="0.7"):
    depth = path.count("/")
    root = "../" * depth
    canonical = DOMAIN + ("" if path == "index.html" else path)
    full_title = title if "16060" in title else f"{title} | 16060"
    sch = ""
    base_schema = {"@context": "https://schema.org", "@type": "WebSite", "name": "16060", "url": DOMAIN}
    if path == "index.html":
        sch += f'<script type="application/ld+json">{json.dumps(base_schema)}</script>'
    if crumbs:
        items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN}]
        for i, (n, u) in enumerate(crumbs):
            items.append({"@type": "ListItem", "position": i + 2, "name": n, "item": DOMAIN + u})
        sch += f'<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":items})}</script>'
    if schema:
        sch += f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>'
    crumb_html = ""
    if crumbs:
        crumb_html = '<nav class="crumbs" aria-label="Breadcrumb"><a href="' + root + 'index.html">Home</a>' + "".join(
            f' / <a href="{root}{u}">{esc(n)}</a>' if i < len(crumbs) - 1 else f' / <span>{esc(n)}</span>' for i, (n, u) in enumerate(crumbs)) + "</nav>"
    hero_html = ""
    if hero:
        h1, sub = hero
        hero_html = f'<section class="page-hero"><div class="wrap">{crumb_html}<h1>{h1}</h1><p class="lead">{sub}</p></div></section>'
    js = "".join(f'<script src="{root}assets/js/{s}" defer></script>' for s in scripts)
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#b71c1c">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="16060">
<meta property="og:title" content="{esc(full_title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}"><meta property="og:image" content="{DOMAIN}assets/img/og.svg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{root}assets/img/favicon.svg">
<link rel="manifest" href="{root}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Serif+SC:wght@600;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/style.css">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
{sch}
</head>
<body data-root="{root}">
{header(root)}
<main id="main">
{hero_html}
{body.replace("{root}", root)}
</main>
{footer(root)}
<script src="{root}assets/js/config.js" defer></script>
<script src="{root}assets/js/app.js" defer></script>
{js}
</body>
</html>'''
    fp = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w").write(doc)
    if path != "404.html":
        PAGES.append((canonical, priority))
