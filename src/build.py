import os, json, shutil
from layout import OUT, PAGES, favicon, DOMAIN, HERE
shutil.copytree(os.path.join(HERE, "static"), OUT, dirs_exist_ok=True)
import pages_home_tools, pages_zodiac, pages_learn, pages_biz, pages_legal

for m in (pages_home_tools, pages_zodiac, pages_learn, pages_biz, pages_legal):
    m.build()

# 404: make relative URLs work at any depth
p = os.path.join(OUT, "404.html"); s = open(p).read()
s = s.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<script>document.write(\'<base href="\'+(location.hostname.indexOf("github.io")>-1?"/"+location.pathname.split("/")[1]+"/":"/")+\'">\')</script>', 1)
open(p, "w").write(s)

# sitemap / robots / manifest / config
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f"  <url><loc>{u}</loc><lastmod>2026-09-28</lastmod><priority>{pr}</priority></url>\n" for u, pr in PAGES) + "</urlset>\n"
open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}sitemap.xml\n")
open(os.path.join(OUT, "manifest.webmanifest"), "w").write(json.dumps({
    "name": "16060 — Luck · Time · Culture", "short_name": "16060", "start_url": "./index.html", "display": "standalone",
    "background_color": "#0d0b0a", "theme_color": "#b71c1c",
    "icons": [{"src": "assets/img/favicon.svg", "sizes": "any", "type": "image/svg+xml"}]}, indent=1))
open(os.path.join(OUT, ".nojekyll"), "w").write("")
open(os.path.join(OUT, "assets/img/favicon.svg"), "w").write(favicon())

open(os.path.join(OUT, "assets/img/og.svg"), "w").write('''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630"><defs><radialGradient id="g" cx="80%" cy="0%" r="70%"><stop offset="0" stop-color="#8e1414"/><stop offset="1" stop-color="#0d0b0a"/></radialGradient></defs><rect width="1200" height="630" fill="url(#g)"/><text x="80" y="330" font-family="Georgia,serif" font-size="170" font-weight="700" fill="#e3b04b">16060</text><text x="84" y="410" font-family="Arial,sans-serif" font-size="40" fill="#f5ede4">Lucky numbers · Zodiac · Auspicious timing</text><text x="84" y="470" font-family="Arial,sans-serif" font-size="32" fill="#b9aa9c">1 · 60 · 60 — free tools and guides</text><rect x="80" y="520" width="300" height="60" rx="14" fill="#b71c1c"/><text x="230" y="561" text-anchor="middle" font-family="Arial,sans-serif" font-size="30" font-weight="700" fill="#fff">16060.com</text></svg>''')
print(len(PAGES), "pages")
