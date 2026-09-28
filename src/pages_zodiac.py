from layout import page, ad, HERE
import os
import json
from pages_home_tools import ANIMALS, AZH, EMO, zgrid, faq

CNY = json.load(open(os.path.join(HERE, "cny.json")))
STEMS = "甲乙丙丁戊己庚辛壬癸"; BR = "子丑寅卯辰巳午未申酉戌亥"
ELS = ["Wood", "Fire", "Earth", "Metal", "Water"]

D = {
 "Rat": ("Quick-witted, resourceful and charming, the Rat won first place in the Great Race by riding on the Ox's back.", ["Sharp and adaptable", "Thrifty and good with money", "Sociable, great networker"], ["Can be calculating", "Restless", "Guarded with feelings"], "2, 3", "Blue, gold, green", "Entrepreneur, analyst, writer, trader", "Earth animal of the north; 子 hour 23:00–01:00"),
 "Ox": ("Diligent, dependable and patient, the Ox builds success step by step and rarely gives up.", ["Hard-working", "Reliable and honest", "Calm under pressure"], ["Stubborn", "Slow to change", "Reserved"], "1, 4", "White, yellow, green", "Engineer, farmer, manager, craftsperson", "丑 hour 01:00–03:00"),
 "Tiger": ("Brave, competitive and magnetic, the Tiger is a natural leader who loves a challenge.", ["Courageous", "Confident", "Generous and protective"], ["Impulsive", "Short-tempered", "Restless with routine"], "1, 3, 4", "Blue, grey, orange", "Leader, athlete, founder, advocate", "寅 hour 03:00–05:00"),
 "Rabbit": ("Gentle, elegant and quietly strategic, the Rabbit values peace, beauty and careful decisions.", ["Diplomatic", "Kind and artistic", "Prudent"], ["Conflict-averse", "Can be indecisive", "Sensitive"], "3, 4, 6", "Red, pink, purple, blue", "Designer, diplomat, counsellor, curator", "卯 hour 05:00–07:00"),
 "Dragon": ("The only mythical animal in the zodiac, the Dragon symbolises power, ambition and good fortune — the most popular birth year in China.", ["Charismatic", "Ambitious", "Energetic and lucky"], ["Arrogant at times", "Impatient", "Demanding"], "1, 6, 7", "Gold, silver, grey", "Executive, entrepreneur, performer, politician", "辰 hour 07:00–09:00"),
 "Snake": ("Wise, intuitive and composed, the Snake thinks deeply and acts decisively when the time is right.", ["Intelligent", "Intuitive", "Elegant and calm"], ["Secretive", "Possessive", "Suspicious"], "2, 8, 9", "Black, red, yellow", "Scientist, strategist, investor, philosopher", "巳 hour 09:00–11:00"),
 "Horse": ("Free-spirited, energetic and warm, the Horse loves movement, travel and an audience.", ["Energetic", "Independent", "Cheerful and popular"], ["Impatient", "Restless", "Dislikes constraint"], "2, 3, 7", "Yellow, green", "Salesperson, journalist, pilot, tour guide", "午 hour 11:00–13:00"),
 "Goat": ("Gentle, creative and compassionate, the Goat (also Sheep or Ram) thrives in harmony and beauty. 2027 is a Fire Goat year.", ["Creative", "Empathetic", "Persevering"], ["Worrying", "Indecisive", "Can be passive"], "2, 7", "Brown, red, purple", "Artist, stylist, nurse, teacher", "未 hour 13:00–15:00"),
 "Monkey": ("Clever, curious and playful, the Monkey solves problems with wit and invention.", ["Inventive", "Quick learner", "Fun and sociable"], ["Mischievous", "Easily bored", "Can be vain"], "4, 9", "White, blue, gold", "Engineer, marketer, scientist, entertainer", "申 hour 15:00–17:00"),
 "Rooster": ("Observant, hard-working and confident, the Rooster is punctual, honest and proud of a job well done.", ["Diligent", "Honest and direct", "Organised"], ["Critical", "Boastful", "Perfectionist"], "5, 7, 8", "Gold, brown, yellow", "Accountant, surgeon, officer, journalist", "酉 hour 17:00–19:00"),
 "Dog": ("Loyal, honest and just, the Dog is a trusted friend who stands up for what's right.", ["Loyal", "Fair-minded", "Responsible"], ["Anxious", "Stubborn", "Critical"], "3, 4, 9", "Red, green, purple", "Lawyer, nurse, teacher, security", "戌 hour 19:00–21:00"),
 "Pig": ("Generous, sincere and good-humoured, the Pig enjoys life's pleasures and is loved for its kindness.", ["Generous", "Sincere", "Easy-going and diligent"], ["Naive", "Indulgent", "Trusts too easily"], "2, 5, 8", "Yellow, grey, brown, gold", "Hospitality, chef, entertainer, caregiver", "亥 hour 21:00–23:00"),
}
HARMONY = {0: 1, 1: 0, 2: 11, 11: 2, 3: 10, 10: 3, 4: 9, 9: 4, 5: 8, 8: 5, 6: 7, 7: 6}
TRINE = [[0, 4, 8], [1, 5, 9], [2, 6, 10], [3, 7, 11]]
HARM = {0: 7, 7: 0, 1: 6, 6: 1, 2: 5, 5: 2, 3: 4, 4: 3, 8: 11, 11: 8, 9: 10, 10: 9}


def outlook(b):
    g = 7  # 2027 Goat 未
    if b == g: return "本命年 — your birth-sign year. Tradition says wear red for protection, favour steady plans over big gambles, and look after your health and relationships."
    if HARMONY.get(b) == g: return "Six Harmony with the Goat — one of the best-supported signs of 2027. Partnerships, support from others and new starts are favoured."
    if any(b in t and g in t for t in TRINE): return "Triad ally of the Goat — a cooperative year. Teams, creative work and family plans tend to flow."
    if (b - g) % 12 == 6: return "Clashes with the Goat year — expect change and movement. Plan major moves carefully and use auspicious dates for big decisions."
    if HARM.get(b) == g: return "Harm relationship with the Goat — small misunderstandings can grow. Communicate clearly and double-check agreements."
    return "Neutral to the Goat — results follow effort. A good year to build skills and relationships steadily."


def build():
    for i, a in enumerate(ANIMALS):
        intro, st, wk, nums, cols, careers, hour = D[a]
        rows = ""
        for y in range(1924 + i, 2044, 12):
            s = (y - 4) % 10
            rows += f'<tr class="{"hl" if y == 2027 or y == 2026 else ""}"><td><b>{y}</b></td><td class="zh">{STEMS[s]}{BR[(y-4)%12]}</td><td class="el-{ELS[s//2]}">{"Yang" if s%2==0 else "Yin"} {ELS[s//2]}</td><td>{CNY.get(str(y),"")}</td><td>{CNY.get(str(y+1),"")} (eve)</td></tr>'
        best = [ANIMALS[HARMONY[i]]] + [ANIMALS[x] for t in TRINE if i in t for x in t if x != i]
        clash = ANIMALS[(i + 6) % 12]
        harm = ANIMALS[HARM[i]]
        links = " · ".join(f'<a href="{b.lower()}.html">{EMO[ANIMALS.index(b)]} {b}</a>' for b in best)
        faqs = [(f"What years are the Year of the {a}?", "Recent years: " + ", ".join(str(y) for y in range(1948 + i, 2044, 12)) + ". Check exact dates in the table, since each year starts at Lunar New Year."),
                (f"Who is the {a} most compatible with?", f"{best[0]} (Six Harmony) and {best[1]} and {best[2]} (Triad)."),
                (f"What are lucky numbers for the {a}?", f"Commonly cited lucky numbers are {nums}; lucky colours are {cols.lower()}.")]
        fh, fsch = faq(faqs)
        body = f'''<section><div class="wrap article-layout"><article class="prose">
<div class="big-score" style="margin-bottom:10px"><div style="font-size:5rem;line-height:1">{EMO[i]}</div><div><span class="chip gold">Earthly Branch {BR[i]} · #{i+1} of 12</span><p class="lead" style="margin-top:8px">{intro}</p></div></div>
<div class="grid g2" style="margin:20px 0"><div class="card"><h3>Strengths</h3><ul>{"".join(f"<li>{x}</li>" for x in st)}</ul></div><div class="card"><h3>Watch-outs</h3><ul>{"".join(f"<li>{x}</li>" for x in wk)}</ul></div></div>
<div class="table-wrap"><table>
<tr><th>Lucky numbers*</th><td><b>{nums}</b></td></tr><tr><th>Lucky colours*</th><td>{cols}</td></tr>
<tr><th>Best matches</th><td>{links}</td></tr><tr><th>Clash</th><td><a href="{clash.lower()}.html">{EMO[(i+6)%12]} {clash}</a></td></tr><tr><th>Harm</th><td>{harm}</td></tr>
<tr><th>Suited careers</th><td>{careers}</td></tr><tr><th>Hour</th><td>{hour}</td></tr></table></div>
<p class="small muted">*As commonly cited in popular Chinese astrology; sources vary.</p>
{ad()}
<h2>{a} in 2027, the Fire Goat year</h2><div class="callout">{outlook(i)}</div>
<p>2027 (丁未, Fire Goat) runs from 6 February 2027 to 25 January 2028. Use the <a href="../tools/auspicious-dates.html">Auspicious Date Finder</a> with your birth year to find your strongest days.</p>
<h2>Years of the {a}</h2><div class="table-wrap"><table><tr><th>Year</th><th>干支</th><th>Element</th><th>Starts</th><th>Ends</th></tr>{rows}</table></div>
<p class="small muted">Born in January or February? Use the <a href="../tools/zodiac-finder.html">Zodiac Finder</a> to confirm your animal.</p>
<h2>FAQ</h2>{fh}
<div class="cta-band" style="margin-top:28px"><div><h2>Your full {a} blueprint</h2><p>Four pillars, lucky numbers and best days for the next 60.</p></div><div><a class="btn gold lg block" href="../consult.html#blueprint">Get it free →</a></div></div>
</article>
<aside class="sidebar no-print">{ad("sidebar")}<div class="card"><h3>All signs</h3><p>{" ".join(f'<a href="{x.lower()}.html">{EMO[k]}</a>' for k, x in enumerate(ANIMALS))}</p></div><div class="card"><h3>Check compatibility</h3><p><a href="../tools/compatibility.html?a={i}&b={HARMONY[i]}">{a} + {best[0]} →</a></p></div></aside></div></section>'''
        page(f"zodiac/{a.lower()}.html", f"Year of the {a} {AZH[i]} — Traits, Lucky Numbers & 2027 Outlook",
             f"Chinese zodiac {a}: personality, lucky numbers and colours, compatibility, years and dates, and the 2027 Fire Goat outlook.",
             body, schema=fsch, hero=(f"Year of the {a} <span class='zh' style='color:var(--red)'>{AZH[i]}</span>", f"Personality, compatibility, lucky numbers and every {a} year from 1924 to 2043."),
             crumbs=[("Zodiac", "zodiac/index.html"), (a, f"zodiac/{a.lower()}.html")], og_type="article", priority="0.8")

    page("zodiac/index.html", "The 12 Chinese Zodiac Animals", "The 12 Chinese zodiac animals: years, personalities, compatibility and lucky numbers for Rat, Ox, Tiger, Rabbit, Dragon, Snake, Horse, Goat, Monkey, Rooster, Dog and Pig.",
         f'''<section><div class="wrap">{zgrid()}{ad()}
<div class="prose narrow" style="margin-top:30px"><h2>The Great Race</h2><p>Legend says the Jade Emperor held a race to choose the animals of the calendar. The clever Rat rode on the Ox's back and leapt ahead at the finish, which is why the cycle begins with the Rat. The Pig, who stopped for a meal and a nap, came last.</p>
<h2>More than animals</h2><p>Each year pairs an animal (earthly branch) with an element and polarity (heavenly stem), which gives <a href="../tools/sixty-year-cycle.html">60 unique years</a>. 2026 is the <b>Fire Horse</b> and 2027 the <b>Fire Goat</b>.</p></div>
<div class="videos" data-videos="3" data-tag="Zodiac" style="margin-top:26px"></div></div></section>''',
         hero=("The 12 Zodiac Animals <span class='zh' style='color:var(--red)'>十二生肖</span>", "Pick your sign for personality, compatibility, lucky numbers and the 2027 outlook."),
         crumbs=[("Zodiac", "zodiac/index.html")], priority="0.9")
