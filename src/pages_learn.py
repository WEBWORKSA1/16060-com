from layout import page, ad

ARTICLES = []


def art(slug, title, desc, tag, body, related=()):
    ARTICLES.append((slug, title, desc, tag))
    rel = "".join(f'<li><a href="{r}.html">{t}</a></li>' for r, t in related)
    schema = {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc,
              "author": {"@type": "Organization", "name": "16060 Editorial"}, "publisher": {"@type": "Organization", "name": "16060"},
              "datePublished": "2026-09-28", "dateModified": "2026-09-28", "mainEntityOfPage": f"https://16060.com/learn/{slug}.html"}
    html = f'''<section><div class="wrap article-layout"><article class="prose">
<p class="small muted">By 16060 Editorial · Updated 28 Sep 2026 · <button class="btn ghost sm" data-share="{title}">↗ Share</button></p>
{body.replace("<!--AD-->", ad())}
<div class="cta-band" style="margin-top:34px"><div><h2>Put it into practice</h2><p>Get your free Lucky Blueprint: zodiac, four pillars, lucky numbers and your best dates for the next 60 days.</p></div><div><a class="btn gold lg block" href="../consult.html#blueprint">Get it free →</a></div></div>
</article><aside class="sidebar no-print">{ad("sidebar")}<div class="card"><h3>Related</h3><ul style="padding-left:1.1em;margin:0">{rel}</ul></div>
<div class="card"><h3>Try the tools</h3><p><a href="../tools/lucky-number.html">Lucky Number Analyzer →</a><br><a href="../tools/zodiac-finder.html">Zodiac Finder →</a><br><a href="../tools/auspicious-dates.html">Date Finder →</a></p></div></aside></div></section>'''
    page(f"learn/{slug}.html", title, desc, html, schema=schema, hero=(title, desc), crumbs=[("Learn", "learn/index.html"), (title, f"learn/{slug}.html")], og_type="article", priority="0.8")


def build():
    art("what-does-16060-mean", "What Does 16060 Mean?", "One hour, sixty minutes, sixty seconds, and one sixty-year cycle. An honest look at the number 16060 in Chinese culture.", "Explainer", '''
<div class="toc"><b>In this guide</b><ol><li><a href="#time">1 · 60 · 60 as time</a></li><li><a href="#cycle">The 60-year cycle</a></li><li><a href="#digits">The digits 1, 6 and 0</a></li><li><a href="#honest">What 16060 is not</a></li></ol></div>
<h2 id="time">1 · 60 · 60: the shape of an hour</h2><p>Split 16060 as <b>1 · 60 · 60</b> and it describes an hour: one hour, sixty minutes, sixty seconds, or 3,600 seconds in all. Base-60 timekeeping goes back to ancient Mesopotamia, but the idea has a well-known Chinese counterpart: <span class="zh">一寸光阴一寸金，寸金难买寸光阴</span>, “an inch of time is an inch of gold, but an inch of gold cannot buy an inch of time.”</p>
<h2 id="cycle">Sixty: the number of a complete cycle</h2><p>Sixty is one of the most important numbers in the Chinese calendar. Ten Heavenly Stems combined with twelve Earthly Branches produce the <a href="../tools/sixty-year-cycle.html">sexagenary cycle</a> (六十甲子). It names every year, and traditionally every day. A 60th birthday, <span class="zh">花甲</span>, marks the completion of a full cycle of life and is celebrated as a longevity milestone.</p><p>So 16060 can read as “one cycle, sixty and sixty”: a whole hour and a whole cycle together.</p>
<!--AD-->
<h2 id="digits">The digits</h2><ul><li><b>1</b> (yī, or yāo 幺 when reading phone numbers): firstness and leadership. Paired with 6, <b>16</b> echoes <span class="zh">一路</span> (yī lù, “all the way”), as in the famous 168 一路发, “prosper all the way.”</li><li><b>6</b> (liù): “smooth, flowing,” from the idiom <span class="zh">六六大顺</span>. In Cantonese it evokes 祿 (prosperity). Betrothal gifts of ¥6,666 are popular.</li><li><b>0</b> (líng): wholeness, a new beginning.</li><li><b>No 4.</b> 16060 contains no 4 (sì, which sounds like 死), the digit most Chinese buyers avoid.</li></ul>
<p>Run it through our <a href="../tools/lucky-number.html?n=16060">Lucky Number Analyzer</a>. It scores as favourable, with a rhythmic 6060 repeat, but it has no prestige 8.</p>
<h2 id="honest">What 16060 is not</h2><p>Unlike 168 or 8888, 16060 has no single fixed phrase attached to it. Readings such as “all the way, cycle after cycle” are modern, interpretive wordplay. The number is also used in unrelated contexts around the world: helpline numbers, postal codes and part numbers. This site has no connection to any of them (see our <a href="../legal/disclaimer.html">disclosure</a>).</p>
<blockquote>Our take: 16060 stands for <b>good timing</b>. Every tool on this site helps you choose the right number, sign or moment.</blockquote>''',
        [("chinese-lucky-numbers-guide", "Chinese lucky numbers 0–9"), ("sixty-year-cycle-explained", "The 60-year cycle explained"), ("shichen-chinese-double-hours", "The 12 Chinese double-hours")])

    art("chinese-lucky-numbers-guide", "Chinese Lucky Numbers: The Complete Guide (0–9 and Beyond)", "Why 8 means prosperity, 4 is avoided, 9 means forever, and what 168, 518, 520 and 1314 say, with the Cantonese twists.", "Guide", '''
<p>Chinese number symbolism rests mostly on <b>homophones</b>: numbers that sound like other words. Because numbers are read aloud constantly (prices, phone numbers, floors, dates), these associations shape real decisions.</p>
<div class="table-wrap"><table><tr><th>Digit</th><th>Mandarin</th><th>Association</th><th>Verdict</th></tr>
<tr><td><b>0</b></td><td class="zh">零 líng</td><td>Wholeness, beginnings</td><td>Neutral–good</td></tr>
<tr><td><b>1</b></td><td class="zh">一 yī</td><td>First, independence; can suggest “alone”</td><td>Neutral</td></tr>
<tr><td><b>2</b></td><td class="zh">二 èr</td><td>“Good things come in pairs” 好事成双</td><td>Good</td></tr>
<tr><td><b>3</b></td><td class="zh">三 sān</td><td>Sounds like 生 (life) in Cantonese; 散 (scatter) in Mandarin</td><td>Mixed</td></tr>
<tr><td><b>4</b></td><td class="zh">四 sì</td><td>Sounds like 死 (death)</td><td>Avoided</td></tr>
<tr><td><b>5</b></td><td class="zh">五 wǔ</td><td>Five elements; sounds like 无 (without)</td><td>Neutral</td></tr>
<tr><td><b>6</b></td><td class="zh">六 liù</td><td>Smooth 六六大顺; 祿 prosperity (Cantonese)</td><td>Very good</td></tr>
<tr><td><b>7</b></td><td class="zh">七 qī</td><td>Togetherness; the 7th lunar month is the ghost month</td><td>Mixed</td></tr>
<tr><td><b>8</b></td><td class="zh">八 bā</td><td>Sounds like 发 (prosper)</td><td>Best</td></tr>
<tr><td><b>9</b></td><td class="zh">九 jiǔ</td><td>Sounds like 久 (long-lasting)</td><td>Very good</td></tr></table></div>
<!--AD-->
<h2>Famous combinations</h2><ul><li><b>168</b> 一路发: prosper all the way</li><li><b>518</b> 我要发: I will prosper</li><li><b>520</b> 我爱你: I love you. 20 May is an unofficial Valentine's Day, and weddings spike.</li><li><b>1314</b> 一生一世: for a whole lifetime. Often paired as 5201314.</li><li><b>28</b> 易发: easy prosperity (Cantonese)</li><li><b>14</b> 要死 and <b>74</b> 气死: avoided</li><li><b>250</b> 二百五: slang for a fool, so never price anything at 250</li></ul>
<h2>In daily life</h2><p>Buildings skip 4th, 14th and 24th floors. Weddings favour dates with 6, 8 and 9. Red-envelope amounts avoid 4 and favour 8 (¥88, ¥888) or 6 (¥666). The Beijing Olympics opened at 8:08 pm on 8/8/08.</p>
<p>Test any number with the <a href="../tools/lucky-number.html">Lucky Number Analyzer</a>.</p>''',
        [("lucky-number-economy", "The lucky-number economy"), ("why-4-is-unlucky", "Why 4 is unlucky"), ("what-does-16060-mean", "What 16060 means")])

    art("lucky-number-economy", "The Lucky-Number Economy: Phones, Plates, Property and Domains", "How superstition moves real money: auction records, a property-price study and the Chinese numeric domain market, with sources.", "Economy", '''
<p>Lucky numbers aren't just folklore. They carry measurable price premiums across several markets.</p>
<h2>Phone numbers</h2><p>In August 2003 Sichuan Airlines paid <b>¥2.33 million (about US$280,000)</b> for the phone number 8888-8888 (<a href="https://www.chinadaily.com.cn/en/doc/2003-08/19/content_256178.htm" rel="nofollow noopener" target="_blank">China Daily</a>). Carriers in China still sell “beautiful numbers” (靓号) at premium prices.</p>
<h2>Licence plates</h2><p>Hong Kong's Transport Department auctions “vanity” and lucky plates for charity. The plate <b>“W”</b> set a record of <b>HK$26 million</b> in 2021, and <b>“R”</b> fetched HK$25.5 million in 2024 (<a href="https://www.scmp.com/news/hong-kong/society/article/3209965/lucky-car-number-plate-letter-r-sells-hk25-million-auction-hong-kong" rel="nofollow noopener" target="_blank">SCMP</a>). The plate <b>“28”</b> (Cantonese: 易发, easy prosperity) sold for <b>HK$18.1 million</b> in 2016 (<a href="https://www.bloomberg.com/news/articles/2016-02-22/hong-kong-just-auctioned-off-a-lucky-license-plate-number-for-2-3-million" rel="nofollow noopener" target="_blank">Bloomberg</a>).</p>
<!--AD-->
<h2>Property</h2><p>Economists at UBC studied about 117,000 Greater Vancouver home sales (2000–2005). In neighbourhoods with many Chinese buyers, addresses ending in <b>4 sold at a 2.2% discount</b> and those ending in <b>8 at a 2.5% premium</b> (<a href="https://economics.ubc.ca/wp-content/uploads/sites/38/2013/05/pdf_paper_nicole-fortin-supersitition-housing-market.pdf" rel="nofollow noopener" target="_blank">Fortin et al.</a>).</p>
<h2>Stock codes</h2><p>A study of Taiwanese listings (1991–2015) found that firms with lucky listing codes earned return premiums, driven by retail investors. The effect has faded in recent years (<a href="https://www.sciencedirect.com/science/article/abs/pii/S0927538X17301452" rel="nofollow noopener" target="_blank">Pacific-Basin Finance Journal</a>).</p>
<h2>Numeric domains</h2><p>Numbers work across dialects and don't need pinyin typing, so short numeric .com domains became prized assets in China. Reported sales include 360.com (US$16M), 55.com (US$2.3M), 114.com (US$2.1M) and 88888.com (US$245k) (<a href="https://mediaoptions.com/blog/understanding-numeric-domain-value-in-chinese-culture/" rel="nofollow noopener" target="_blank">MediaOptions</a>). Industry rules of thumb: a 4 can cut a numeric domain's value by up to half, a leading 0 lowers it, and an 8 raises it (<a href="https://ggrg.com/numeric-domains-2-0-the-definitive-guide/" rel="nofollow noopener" target="_blank">GGRG</a>).</p>
<div class="callout"><b>Need a lucky number sourced or audited?</b> We help businesses choose phone numbers, addresses, prices and domains that land well with Chinese customers. <a href="../consult.html#consult">Request an audit →</a></div>''',
        [("chinese-lucky-numbers-guide", "Chinese lucky numbers 0–9"), ("why-4-is-unlucky", "Why 4 is unlucky")])

    art("sixty-year-cycle-explained", "The 60-Year Cycle (Jiazi) Explained", "Heavenly Stems, Earthly Branches and the sixty-year cycle behind the Chinese zodiac, BaZi and 60th-birthday celebrations.", "Calendar", '''
<h2>Two wheels turning together</h2><p>Imagine two gears: one with 10 teeth (the <b>Heavenly Stems</b> 天干) and one with 12 (the <b>Earthly Branches</b> 地支). Turn them together and the same pair of teeth meets again only after <b>60</b> turns, the lowest common multiple of 10 and 12. Each of the 60 combinations has a name, starting with <span class="zh">甲子</span> (Jiǎzǐ).</p>
<h2>What the stems and branches carry</h2><ul><li>Stems give the <b>element</b> (two each for Wood, Fire, Earth, Metal, Water) and <b>polarity</b> (yang, yin).</li><li>Branches give the <b>animal</b>, a direction, a season and a two-hour period of the day.</li></ul>
<!--AD-->
<h2>Years, months, days and hours</h2><p>The cycle labels years (2026 = 丙午 Fire Horse, 2027 = 丁未 Fire Goat). It also labels months, and it has counted days without a break for well over two thousand years, which makes it one of the longest continuous day counts in use. BaZi uses four such pairs, for year, month, day and hour, which is why it's called “eight characters.”</p>
<h2>Turning sixty</h2><p>Your 60th birthday completes a whole cycle (花甲, or 甲子 return). Families celebrate it as a major longevity milestone.</p>
<p>See every combination in the <a href="../tools/sixty-year-cycle.html">60-Year Cycle Table</a>.</p>''',
        [("what-does-16060-mean", "What 16060 means"), ("shichen-chinese-double-hours", "The 12 double-hours")])

    art("how-to-choose-an-auspicious-date", "How to Choose an Auspicious Date (择日) for Weddings, Openings and Moves", "A practical guide to the 12 Day Officers, clash days and number symbolism, the building blocks of Chinese date selection.", "Timing", '''
<p>Choosing a good day (择日, zé rì) is one of the most common ways Chinese families and businesses apply tradition, whether for weddings, grand openings, moving house or signing deals.</p>
<h2>Step 1: know the day officers</h2><p>The almanac assigns each day one of twelve officers. A classic rhyme sorts them: <span class="zh">除危定执黄，成开皆可用；建满平收黑，闭破不相当</span>. In other words, <b>Remove, Danger, Stable, Initiate, Success and Open</b> are usable (yellow) days. <b>Establish, Full, Balance, Receive, Close and Destruction</b> are black days. Destruction and Close are avoided for big events.</p>
<h2>Step 2: avoid your clash day</h2><p>Every day has an earthly branch. The animal directly opposite it clashes. A Rat-year person avoids Horse days for major events, and so on.</p>
<!--AD-->
<h2>Step 3: match the event</h2><ul><li><b>Weddings</b>: Success 成, Stable 定, Open 开. Both partners' clash days are avoided.</li><li><b>Business openings</b>: Open 开 and Success 成. Many open at 8:08 or 9:09.</li><li><b>Moving</b>: Success, Open, Remove 除 (clearing the old).</li><li><b>Contracts</b>: Stable 定, Success, Initiate 执.</li></ul>
<h2>Step 4: numbers and hours</h2><p>Dates containing 6, 8 or 9 are popular (think 8 August, or 18 and 28 of any month), and those with 4 are skipped. Professionals also pick an auspicious <b>hour</b> using the 12 double-hours.</p>
<p>Run steps 1–3 automatically with the <a href="../tools/auspicious-dates.html">Auspicious Date Finder</a>.</p>''',
        [("chinese-lucky-numbers-guide", "Lucky numbers guide"), ("shichen-chinese-double-hours", "The 12 double-hours")])

    art("year-of-the-fire-goat-2027", "2027: Year of the Fire Goat (丁未) — Dates, Meaning and What to Expect", "Lunar New Year 2027 falls on 6 February. What the Fire Goat year means, who it favours, and how to prepare.", "Forecast", '''
<h2>Key dates</h2><ul><li><b>Lunar New Year:</b> Saturday 6 February 2027</li><li><b>Year runs:</b> 6 Feb 2027 – 25 Jan 2028</li><li><b>BaZi year starts:</b> Start of Spring (立春), about 4 February 2027</li><li><b>Stem-branch:</b> 丁未, Yin Fire over the Goat</li></ul>
<h2>What Fire Goat energy means</h2><p>The Goat is associated with gentleness, creativity and community. Yin Fire (丁) is candle-light rather than a bonfire: warm and illuminating rather than explosive. Traditional commentators read such years as favouring the arts, care, craft and cooperation over aggression.</p>
<!--AD-->
<h2>Signs in focus</h2><ul><li><b>Goat</b>: 本命年, the birth-sign year. Wear red and move steadily.</li><li><b>Horse</b>: Six Harmony partner, well supported.</li><li><b>Rabbit and Pig</b>: triad allies, a cooperative year.</li><li><b>Ox</b>: clashes with the Goat, a year of change. Plan big decisions carefully.</li><li><b>Rat</b>: harm relationship. Communicate clearly.</li></ul>
<p>Read your sign's page in the <a href="../zodiac/index.html">zodiac section</a>, then count down to the New Year with our <a href="../tools/countdown.html">festival countdown</a>.</p>
<p class="small muted">Forecasts are traditional and cultural interpretations, provided for entertainment.</p>''',
        [("sixty-year-cycle-explained", "The 60-year cycle"), ("how-to-choose-an-auspicious-date", "Choosing auspicious dates")])

    art("why-4-is-unlucky", "Why 4 Is Unlucky in Chinese Culture, and How Businesses Handle It", "Tetraphobia explained: the 4 = 死 homophone, missing floors, pricing rules and what global brands do when selling to Chinese customers.", "Business", '''
<p>In Mandarin, Cantonese, Japanese and Korean, the word for four sounds like the word for death (<span class="zh">四 sì / 死 sǐ</span>). Fear of the number, tetraphobia, has practical effects across East Asia and the diaspora.</p>
<h2>Where it shows up</h2><ul><li><b>Buildings</b>: 4th, 14th, 24th floors (and sometimes 13th) are skipped or relabelled.</li><li><b>Hospitals</b> avoid room numbers with 4.</li><li><b>Phone numbers and plates</b> containing 4 sell for less. 14 (要死) and 74 (气死) are the worst.</li><li><b>Property</b>: in a Vancouver study, addresses ending in 4 sold at about a 2.2% discount in Chinese-majority areas.</li><li><b>Gifts</b>: never give four of anything, especially clocks, since 送钟 sounds like attending a funeral.</li></ul>
<!--AD-->
<h2>A playbook for businesses</h2><ol><li>Audit prices: move ¥/$4, 14, 44 endings to 8 or 9 (e.g. 88, 168, 199).</li><li>Avoid 4 in hotlines, SKUs customers see, table numbers and room numbers.</li><li>Launch on auspicious dates and times such as 8:08 or 9:09, and avoid the 7th lunar month for openings.</li><li>Use lucky numbers in promotions: 6.18, 8.8 and 11.11 are shopping moments.</li></ol>
<div class="callout"><b>Selling to Chinese customers?</b> Our Business Number Audit reviews your prices, phone numbers, address and launch dates. <a href="../consult.html#consult">Request an audit →</a></div>''',
        [("chinese-lucky-numbers-guide", "Lucky numbers 0–9"), ("lucky-number-economy", "The lucky-number economy")])

    art("shichen-chinese-double-hours", "Shichen: The 12 Chinese Double-Hours and Their Animals", "Traditional Chinese timekeeping divided the day into twelve two-hour shichen. Here are their names, animals and uses today.", "Time", '''
<p>Before clocks, China divided the day into twelve <b>shichen</b> (时辰) of two hours each, named after the Earthly Branches and their animals. They are still used in BaZi, in traditional medicine's “organ clock” and in choosing auspicious hours.</p>
<div class="table-wrap"><table><tr><th>Shichen</th><th>Time</th><th>Animal</th></tr>
<tr><td class="zh">子时 Zǐ</td><td>23:00–00:59</td><td>Rat</td></tr><tr><td class="zh">丑时 Chǒu</td><td>01:00–02:59</td><td>Ox</td></tr><tr><td class="zh">寅时 Yín</td><td>03:00–04:59</td><td>Tiger</td></tr><tr><td class="zh">卯时 Mǎo</td><td>05:00–06:59</td><td>Rabbit</td></tr><tr><td class="zh">辰时 Chén</td><td>07:00–08:59</td><td>Dragon</td></tr><tr><td class="zh">巳时 Sì</td><td>09:00–10:59</td><td>Snake</td></tr><tr><td class="zh">午时 Wǔ</td><td>11:00–12:59</td><td>Horse</td></tr><tr><td class="zh">未时 Wèi</td><td>13:00–14:59</td><td>Goat</td></tr><tr><td class="zh">申时 Shēn</td><td>15:00–16:59</td><td>Monkey</td></tr><tr><td class="zh">酉时 Yǒu</td><td>17:00–18:59</td><td>Rooster</td></tr><tr><td class="zh">戌时 Xū</td><td>19:00–20:59</td><td>Dog</td></tr><tr><td class="zh">亥时 Hài</td><td>21:00–22:59</td><td>Pig</td></tr></table></div>
<!--AD-->
<h2>Smaller units</h2><p>Each shichen was split into an upper and lower half. The day was also divided into 100 <b>ke</b> (刻) of about 14.4 minutes, later standardised to 96, which makes a quarter-hour. That's why 一刻钟 still means fifteen minutes.</p>
<p>See the current shichen live on our <a href="../tools/clocks-timers.html">1·60·60 clock</a>.</p>''',
        [("what-does-16060-mean", "What 16060 means"), ("sixty-year-cycle-explained", "The 60-year cycle")])

    cards = "".join(f'<a class="card hover" href="{s}.html"><span class="chip gold">{tg}</span><h3 style="margin-top:10px">{t}</h3><p>{d}</p></a>' for s, t, d, tg in ARTICLES)
    page("learn/index.html", "Learn: Chinese Numbers, Zodiac and Timing Guides", "Guides to Chinese lucky numbers, the 60-year cycle, auspicious dates, the Fire Goat year and the lucky-number economy.",
         f'<section><div class="wrap"><div class="grid g3">{cards}</div>{ad()}</div></section>',
         hero=("Learn", "Well-researched guides to Chinese number symbolism, the calendar and timing."), crumbs=[("Learn", "learn/index.html")], priority="0.8")
