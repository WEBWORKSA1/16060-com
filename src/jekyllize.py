"""Package the generated _site/ as a compact Jekyll site for GitHub Pages (gh-pages branch).

Every page keeps only its unique <main> content plus front matter; the shared
<head>, header and footer live once in _layouts/default.html. Static assets are
served from src/static/assets/ (already in the repository). Calendar data is
delta-encoded (~7 KB instead of ~37 KB) and decoded in the browser into the
same window.CAL structure that calc.js expects.
Usage: python src/jekyllize.py   (after build.py) -> output in _jk/
"""
import os, re, json, glob, shutil
from layout import OUT, HERE, header, footer

JK = os.path.join(HERE, "..", "_jk")
A = "src/static/assets/"          # asset base (relative to site root)
shutil.rmtree(JK, ignore_errors=True)
os.makedirs(os.path.join(JK, "_layouts"), exist_ok=True)


def q(s):  # YAML single-quoted scalar
    return "'" + s.replace("'", "''") + "'"


R = "{{ page.root }}"
layout = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
{{% if page.is404 %}}<script>document.write('<base href="'+(location.hostname.indexOf("github.io")>-1?"/"+location.pathname.split("/")[1]+"/":"/")+'">')</script>{{% endif %}}
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{{{{ page.title }}}}</title>
<meta name="description" content="{{{{ page.description }}}}">
<link rel="canonical" href="{{{{ page.canonical }}}}">
<meta name="theme-color" content="#b71c1c">
<meta property="og:type" content="{{{{ page.og_type }}}}"><meta property="og:site_name" content="16060">
<meta property="og:title" content="{{{{ page.title }}}}"><meta property="og:description" content="{{{{ page.description }}}}">
<meta property="og:url" content="{{{{ page.canonical }}}}"><meta property="og:image" content="https://16060.com/{A}img/og.svg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{R}{A}img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{R}{A}img/favicon.svg">
<link rel="manifest" href="{R}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Noto+Serif+SC:wght@600;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{R}{A}css/style.css">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
{{{{ page.schema }}}}
</head>
<body data-root="{R}">
{header(R)}
<main id="main">
{{{{ content }}}}
</main>
{footer(R)}
<script src="{R}{A}js/config.js" defer></script>
<script src="{R}{A}js/app.js" defer></script>
{{% for s in page.scripts %}}<script src="{R}{A}js/{{{{ s }}}}" defer></script>{{% endfor %}}
</body>
</html>
'''
open(os.path.join(JK, "_layouts/default.html"), "w").write(layout)

pages = sorted(glob.glob(os.path.join(OUT, "**/*.html"), recursive=True))
for fp in pages:
    rel = os.path.relpath(fp, OUT)
    s = open(fp).read()
    g = lambda pat: re.search(pat, s, re.S).group(1)
    title = g(r"<title>(.*?)</title>")
    desc = g(r'<meta name="description" content="(.*?)">')
    canon = g(r'<link rel="canonical" href="(.*?)">')
    ogt = g(r'<meta property="og:type" content="(.*?)">')
    root = g(r'<body data-root="(.*?)">')
    schema = "".join(re.findall(r'<script type="application/ld\+json">.*?</script>', s, re.S))
    main = g(r'<main id="main">\n(.*)\n</main>')
    tail = s[s.index("</main>"):]
    scripts = re.findall(r'<script src="[./]*assets/js/([\w.]+)" defer></script>', tail)
    scripts = [x for x in scripts if x not in ("config.js", "app.js")]
    fm = ["---", "layout: default", f"title: {q(title)}", f"description: {q(desc)}", f"canonical: {q(canon)}",
          f"og_type: {ogt}", f"root: {q(root)}", f"scripts: [{', '.join(scripts)}]"]
    if schema:
        fm.append(f"schema: {q(schema)}")
    if rel == "404.html":
        fm.append("is404: true")
        fm.append("permalink: /404.html")
    fm.append("---")
    out = os.path.join(JK, rel)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write("\n".join(fm) + "\n" + main + "\n")

# compact calendar data
d = json.loads(open(os.path.join(OUT, "assets/js/caldata.js")).read()[len("window.CAL="):-1])
t, m = d["terms"], d["months"]
tstr = "".join(str(t[i + 1] - t[i] - 13) for i in range(len(t) - 1))
ms = [v // 100 for v in m]
mstr = "".join(str((ms[i + 1] - ms[i] - 29) + 2 * (m[i] % 2)) for i in range(len(m) - 1))
js = ("/* Chinese calendar data 1920-2061 (delta-encoded; decoded to window.CAL) */\n(function(){"
      f"var T0={t[0]},I0={d['t0']},TD=\"{tstr}\",M0={ms[0]},MM={(m[0] % 100) // 2},ML={m[0] % 2},MD=\"{mstr}\",ME={ms[-1]},EP=Date.UTC(1900,0,1);\n"
      "var terms=[T0],n=T0;for(var i=0;i<TD.length;i++){n+=+TD[i]+13;terms.push(n)}\n"
      "var months=[M0*100+MM*2+ML],s=M0,mo=MM,cny={};for(var j=0;j<MD.length;j++){var c=+MD[j];s+=29+(c&1);var leapNext=(j+1<MD.length)?(+MD[j+1]>>1):0;"
      "if(j+1===MD.length){leapNext=" + str(m[-1] % 2) + "}mo=leapNext?mo:(mo%12)+1;months.push(s*100+mo*2+leapNext)}\n"
      "months.forEach(function(v){var lp=v%2,mm=((v%100)-lp)/2;if(mm===1&&!lp){var dt=new Date(EP+Math.floor(v/100)*864e5);var y=dt.getUTCFullYear();cny[y]=y+'-'+('0'+(dt.getUTCMonth()+1)).slice(-2)+'-'+('0'+dt.getUTCDate()).slice(-2)}});\n"
      "window.CAL={epoch:'1900-01-01',t0:I0,terms:terms,months:months,cny:cny};})();\n")
os.makedirs(os.path.join(JK, A, "js"), exist_ok=True)
os.makedirs(os.path.join(JK, A, "img"), exist_ok=True)
open(os.path.join(JK, A, "js/caldata.js"), "w").write(js)
shutil.copy(os.path.join(OUT, "assets/js/festivals.js"), os.path.join(JK, A, "js/festivals.js"))
for f in ("favicon.svg", "og.svg"):
    shutil.copy(os.path.join(OUT, "assets/img", f), os.path.join(JK, A, "img", f))
shutil.copy(os.path.join(OUT, "sitemap.xml"), JK)
shutil.copy(os.path.join(OUT, "robots.txt"), JK)
man = json.load(open(os.path.join(OUT, "manifest.webmanifest")))
man["icons"][0]["src"] = A + "img/favicon.svg"
open(os.path.join(JK, "manifest.webmanifest"), "w").write(json.dumps(man, indent=1, ensure_ascii=False))
open(os.path.join(JK, "_config.yml"), "w").write(
    "# GitHub Pages (Jekyll) config for 16060.com\ntitle: \"16060\"\nexclude:\n  - README.md\n  - docs\n  - .gitignore\n"
    + "".join(f"  - src/{f}\n" for f in sorted(os.listdir(HERE)) if f.endswith((".py", ".json"))))
print("jekyll pages:", len(pages))
