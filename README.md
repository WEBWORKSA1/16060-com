# 16060.com — Luck · Time · Culture

Free Chinese lucky-number, zodiac, BaZi, lunar-calendar, auspicious-date and time tools, with lead generation, donations, contests, careers and advertising sections. Static site hosted free on GitHub Pages.

- **Live:** https://webworksa1.github.io/16060-com/
- **Inquiries (domain / sponsorship / advertising / partnership):** https://web.works/contact

## How it deploys (GitHub Pages, free plan)
- `main` holds the **source**: a Python generator in `src/` plus hand-written CSS/JS in `src/static/assets/`.
- `python src/build.py` renders all 47 pages into `_site/` (plain static site — works on any host).
- `python src/jekyllize.py` packages `_site/` for the **`gh-pages`** branch: each page keeps only its unique content + front matter, the shared head/header/footer live once in `_layouts/default.html`, and GitHub Pages' built-in Jekyll assembles the final pages. Assets are served from `src/static/assets/`.
- GitHub Pages serves `gh-pages` / root (Settings → Pages → Deploy from a branch).
- Optional automation: `docs/optional-pages-workflow.yml` rebuilds on every push — move it to `.github/workflows/` from the GitHub web UI to enable it.

## Structure
| Path | What |
|---|---|
| `src/layout.py` | Shared layout: top inquiry bar, header, footer, SEO/schema |
| `src/pages_home_tools.py` | Homepage + 9 tool pages |
| `src/pages_zodiac.py` | 12 zodiac animal pages + hub |
| `src/pages_learn.py` | 8 guides |
| `src/pages_biz.py` | **Lead generation** (`consult.html`), support/donate, contests, careers, advertise, contact, about, videos, festivals, 404 |
| `src/pages_legal.py` | Trademark & copyright disclosure, privacy, terms, cookies, contest rules |
| `src/static/assets/js/config.js` | **All switches**: AdSense, GA4, PayPal/Stripe, videos, fund goal, contest deadline |
| `src/jekyllize.py` | Packages the build for the `gh-pages` branch (Jekyll layout) |
| `docs/` | Research, concept, phase-wise build prompts, optional CI workflow |

## Go-live checklist
1. First form submission → FormSubmit sends a one-time activation email to the inbox. Click it.
2. AdSense: paste `ca-pub-…` into `config.js`; add `ads.txt` to the root of the `gh-pages` branch.
3. Custom domain: Settings → Pages → Custom domain → `16060.com` (creates `CNAME` on `gh-pages`), then DNS A records → 185.199.108.153 / .109.153 / .110.153 / .111.153 and `www` CNAME → `webworksa1.github.io`.

## Local build
```bash
pip install sxtwl lunardate
python src/gen_data.py && python src/gen_fest.py && python src/build.py   # output in _site/
python src/jekyllize.py                                                    # gh-pages package in _jk/
```

© 2026 16060.com. “16060” is used descriptively as a domain name; see `legal/disclaimer.html`.
