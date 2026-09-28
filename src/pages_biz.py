from layout import page, ad, HERE
import os
from pages_home_tools import faq

HP = '<input class="hp" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">'
CONSENT = '<label class="check"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about my request and accept the <a href="{root}legal/privacy.html">Privacy Policy</a>.</label>'
COUNTRIES = ["Canada", "United States", "China", "Hong Kong", "Taiwan", "Singapore", "Malaysia", "Indonesia", "Thailand", "Australia", "United Kingdom", "India", "Other"]
CO = "".join(f"<option>{c}</option>" for c in COUNTRIES)


def build():
    # ---------------- CONSULT / LEAD GEN ----------------
    services = [
        ("🧭", "Personal Lucky Blueprint Pro", "A practitioner-reviewed BaZi reading: luck pillars, strengths, career and relationship timing."),
        ("💍", "Wedding & Event Date Selection", "Dates and hours checked against both partners' charts and the full almanac."),
        ("🏪", "Business Launch Timing", "Opening dates and hours, plus a launch countdown page for your customers."),
        ("🔢", "Business Number Audit", "Phone numbers, addresses, prices, SKUs and domains reviewed for Chinese-market appeal."),
        ("💎", "Premium Number & Domain Sourcing", "We find and negotiate lucky phone numbers, plates (where legal) and numeric domains."),
        ("🏠", "Feng Shui Home & Office", "Layout, direction and element guidance, remote or on-site through partner consultants."),
    ]
    sv = "".join(f'<div class="card hover"><div class="ic">{i}</div><h3>{t}</h3><p>{d}</p></div>' for i, t, d in services)
    choices = "".join(f'<label class="choice"><input type="radio" name="service" value="{t}" required><span>{i} {t}</span></label>' for i, t, d in services) + '<label class="choice"><input type="radio" name="service" value="Other / not sure" required><span>💬 Other / not sure</span></label>'
    cfaq, csch = faq([
        ("Is the Blueprint really free?", "Yes. It's generated instantly in your browser from your birth date. We email you a copy and occasional lucky-day tips, and you can unsubscribe any time."),
        ("How fast will I hear back about a consultation?", "We aim to reply within one business day with options, timing and a quote."),
        ("Who provides consultations?", "Requests are matched with experienced practitioners in our partner network, based on the service and language you need."),
        ("Do you guarantee outcomes?", "No. Chinese metaphysics is a cultural tradition, not a science, and our services are for guidance and cultural insight. We do guarantee clear, respectful, well-researched advice."),
    ])
    body = f'''
<section id="blueprint"><div class="wrap grid g2" style="align-items:start">
<div><span class="eyebrow">Step 1 · Free · 30 seconds</span><h2>Your personal Lucky Blueprint</h2>
<p class="lead">Your zodiac and element, your Four Pillars chart, your lucky numbers, your best allies and your 6 strongest days in the next 60. All in one printable report.</p>
<ul class="muted" style="padding-left:1.1em"><li>Accurate lunar and solar-term calendar data, 1921–2060</li><li>Instant on screen, with a copy sent to your inbox</li><li>No payment, no spam, unsubscribe any time</li></ul>
<div class="card" style="margin-top:18px"><b>What people use it for</b><p>Choosing a wedding or launch date, picking a phone number or price, understanding compatibility, or just knowing your chart.</p></div></div>
<div class="panel" data-tool="blueprint"><form class="form" data-subject="Lucky Blueprint lead" data-silent>
<label>First name <input name="name" autocomplete="given-name" required></label>
<label>Email <input type="email" name="email" autocomplete="email" required></label>
<div class="row"><label>Date of birth <input type="date" name="birthdate" min="1921-01-01" max="2060-12-31" required></label>
<label>Birth hour <span class="opt">(optional)</span><select name="birthhour"><option value="">Unknown</option>{"".join(f'<option value="{h}">{h:02d}:00–{h:02d}:59</option>' for h in range(24))}</select></label></div>
<label>Country <select name="country">{CO}</select></label>
<label>What are you planning? <span class="opt">(optional)</span><select name="interest"><option>Just curious</option><option>Wedding / engagement</option><option>Business launch</option><option>Moving house</option><option>Choosing a number or name</option><option>Career / investment timing</option></select></label>
<input type="hidden" name="summary" value="">{HP}
{CONSENT}
<button class="btn gold lg block" type="submit">Generate my free blueprint</button>
<p class="small muted center" style="margin:0">🔒 Your details are never sold.</p></form><div class="result"></div></div>
</div></section>

<section class="alt" id="services"><div class="wrap"><div class="section-head"><div><span class="eyebrow">Step 2 · Expert help</span><h2>Consultations for moments that matter</h2></div><p>Chosen by families planning weddings, founders launching brands and companies entering Chinese-speaking markets.</p></div>
<div class="grid g3">{sv}</div></div></section>

<section id="consult"><div class="wrap grid g2" style="align-items:start">
<div><span class="eyebrow">Request a consultation</span><h2>Tell us what you need. Get a plan and a quote within one business day.</h2>
<div class="grid" style="gap:12px;margin-top:18px">
<div class="card"><b>1 · Share the basics</b><p>Three short steps. It takes about 90 seconds.</p></div>
<div class="card"><b>2 · Get matched</b><p>We pair you with the right practitioner for your service and language (English, 中文 and more).</p></div>
<div class="card"><b>3 · Decide with confidence</b><p>A written recommendation you can act on, whether that's dates, numbers, names or layouts.</p></div></div></div>
<div class="panel"><form class="form" data-form data-steps data-subject="Consultation request" data-done="Thank you! Your request is in. Expect a reply within one business day with options and a quote.">
<div class="step-label small muted">Step 1 of 3</div><div class="progress"><span></span></div>
<div class="step" data-auto><h3>What can we help with?</h3><div class="choices">{choices}</div></div>
<div class="step" hidden><h3>A few details</h3>
<div class="row"><label>Your birth date <span class="opt">(optional)</span><input type="date" name="birthdate"></label><label>Partner's birth date <span class="opt">(optional)</span><input type="date" name="partner_birthdate"></label></div>
<div class="row"><label>Target date window <span class="opt">(optional)</span><input name="window" placeholder="e.g. May–June 2027"></label><label>Budget <select name="budget"><option>Under $100</option><option>$100–$300</option><option>$300–$1,000</option><option>$1,000–$5,000</option><option>$5,000+</option><option>Not sure</option></select></label></div>
<label>Tell us more <textarea name="details" placeholder="Your situation, the decision you face, languages you prefer…"></textarea></label>
<div class="step-nav"><button type="button" class="btn ghost" data-prev>← Back</button><button type="button" class="btn" data-next>Next →</button></div></div>
<div class="step" hidden><h3>Where should we reply?</h3>
<div class="row"><label>Full name <input name="name" autocomplete="name" required></label><label>Email <input type="email" name="email" autocomplete="email" required></label></div>
<div class="row"><label>Phone / WhatsApp / WeChat <span class="opt">(optional)</span><input name="phone" autocomplete="tel"></label><label>Country <select name="country">{CO}</select></label></div>
<label>Preferred contact <select name="contact_pref"><option>Email</option><option>Phone</option><option>WhatsApp</option><option>WeChat</option></select></label>
{HP}{CONSENT}
<div class="step-nav"><button type="button" class="btn ghost" data-prev>← Back</button><button class="btn gold" type="submit">Request my consultation</button></div></div>
</form></div></div></section>

<section class="alt"><div class="wrap grid g2"><div class="card"><h3>🤝 Are you a practitioner?</h3><p>Feng shui consultants, BaZi readers and date-selection specialists can join our partner network and receive qualified client requests.</p><p style="margin-top:12px"><a class="btn sm" href="careers.html#apply">Apply as a partner</a></p></div>
<div class="card"><h3>🏢 Companies & agencies</h3><p>Entering Chinese-speaking markets? Ask about number audits, naming checks and cultural launch calendars for your team.</p><p style="margin-top:12px"><a class="btn sm" href="contact.html?topic=Corporate">Talk to us</a></p></div></div></section>

<section><div class="narrow"><h2 class="center">FAQ</h2>{cfaq}<p class="small muted">Services are cultural guidance for personal and business decisions. They are not financial, legal, medical or psychological advice.</p></div></section>'''
    page("consult.html", "Free Lucky Blueprint & Expert Consultations", "Get a free personal Lucky Blueprint (zodiac, BaZi, lucky numbers, best dates) or request expert date selection, number audits and feng shui consultations.",
         body, scripts=("caldata.js", "calc.js", "festivals.js", "tools.js"), schema=csch,
         hero=("Free Lucky Blueprint &amp; Expert Consultations", "Start free with your personal report. Go further with a practitioner for weddings, launches, numbers and spaces."), crumbs=[("Blueprint & Consults", "consult.html")], priority="1.0")

    # ---------------- SUPPORT / DONATE ----------------
    body = '''
<section><div class="wrap grid g2" style="align-items:start">
<div><span class="eyebrow">🧧 Send a red envelope</span><h2>Keep 16060 free, independent and growing</h2>
<p class="lead">Every tool here is free. Your support pays for hosting and data, new features, promotion and marketing, hiring writers and creators, and the prizes in our contests.</p>
<div class="card" style="margin:18px 0"><div style="display:flex;justify-content:space-between;align-items:end"><div><small class="muted">Monthly operations goal</small><div class="stat" id="raised">$0</div></div><small class="muted" id="goal">of $6,060</small></div><div class="meter" style="margin-top:10px"><span id="meter" style="width:0%"></span></div><p class="small muted" style="margin:8px 0 0"><span id="supporters-n">0</span> supporters this month</p></div>
<h3>Where your support goes</h3><div class="bars">
<div class="bar"><span>Operations</span><i><span style="width:35%;background:var(--gold)"></span></i><b>35%</b></div>
<div class="bar"><span>Promotion</span><i><span style="width:25%;background:var(--red)"></span></i><b>25%</b></div>
<div class="bar"><span>Talent</span><i><span style="width:25%;background:var(--jade)"></span></i><b>25%</b></div>
<div class="bar"><span>Prizes</span><i><span style="width:15%;background:var(--water)"></span></i><b>15%</b></div></div>
<p class="small muted" style="margin-top:8px">Operations: hosting, data and tools · Promotion: marketing and outreach · Talent: writers, video creators, developers · Prizes: contest prizes and community events.</p></div>

<div class="panel"><h3>One-time red envelope</h3><div class="tiers" id="tiers">
<button class="tier" data-amt="6"><b>$6</b><small>Smooth 顺</small></button>
<button class="tier on" data-amt="18"><b>$18</b><small>Prosper 发</small></button>
<button class="tier" data-amt="60"><b>$60</b><small>Full cycle 甲子</small></button>
<button class="tier" data-amt="88"><b>$88</b><small>Double luck</small></button>
<button class="tier" data-amt="168"><b>$168</b><small>一路发</small></button>
<button class="tier" data-amt="0"><b>Custom</b><small>Any amount</small></button></div>
<label style="margin-top:12px">Amount (USD) <input type="number" id="amt" min="1" value="18"></label>
<label style="margin-top:10px">Purpose <select id="purpose"><option>General support</option><option>Operations & hosting</option><option>Promotions & marketing</option><option>Hiring talent</option><option>Contest prizes</option></select></label>
<div class="grid" style="gap:10px;margin-top:14px"><button class="btn gold lg block" id="paypal-once">Give with PayPal</button><div id="alt-pay"></div></div>
<p class="small muted center" style="margin:10px 0 0">Secure checkout on PayPal. Cards are accepted without a PayPal account.</p></div>
</div></section>

<section class="alt"><div class="wrap"><div class="section-head"><div><span class="eyebrow">Membership</span><h2>Join the 16060 Circle</h2></div><p>Monthly support, priced on our numbers. Cancel any time from your PayPal account.</p></div>
<div class="grid g3">
<div class="card plan"><span class="chip">Friend</span><div class="price">$6<small>/mo</small></div><ul><li>Supporter wall listing</li><li>Monthly lucky-days digest</li><li>Our sincere thanks 谢谢</li></ul><button class="btn ghost block" data-sub="6" data-name="16060 Circle — Friend">Join monthly</button></div>
<div class="card plan pop"><span class="chip gold">Most popular</span><div class="price">$16<small>/mo</small></div><ul><li>Everything in Friend</li><li>Ad-light experience (on request)</li><li>Early access to new tools</li><li>Bonus contest entries</li></ul><button class="btn gold block" data-sub="16" data-name="16060 Circle — Patron">Join monthly</button></div>
<div class="card plan"><span class="chip red">Champion</span><div class="price">$60<small>/mo</small></div><ul><li>Everything in Patron</li><li>Quarterly mini-reading</li><li>Name or logo on a tool page</li><li>Vote on the next tool we build</li></ul><button class="btn ghost block" data-sub="60" data-name="16060 Circle — Champion">Join monthly</button></div>
</div></div></section>

<section><div class="wrap grid g2" style="align-items:start">
<div><h2>Supporter wall</h2><div id="wall" class="grid" style="gap:10px"></div></div>
<div class="panel"><h3>Pledge, sponsor or pay another way</h3><p class="muted">Prefer a bank transfer, Interac, Alipay or WeChat Pay, or want to sponsor a contest prize or a tool? Tell us and we'll send payment details.</p>
<form class="form" data-form data-subject="Donation pledge / sponsorship" data-done="Thank you for your generosity! We'll email you payment details and a receipt.">
<div class="row"><label>Name <input name="name" required></label><label>Email <input type="email" name="email" required></label></div>
<div class="row"><label>Amount <input name="amount" placeholder="e.g. $160"></label><label>Type <select name="type"><option>One-time donation</option><option>Monthly support</option><option>Sponsor a contest prize</option><option>Sponsor a tool page</option><option>Corporate sponsorship</option></select></label></div>
<label>Message for the supporter wall <span class="opt">(optional)</span><input name="wall_message" maxlength="120"></label>
<label class="check"><input type="checkbox" name="show_on_wall" value="yes"> Show my first name on the supporter wall</label>
''' + HP + CONSENT + '''<button class="btn" type="submit">Send pledge</button></form></div></div></section>
<section class="alt"><div class="narrow"><h2 class="center">Donation FAQ</h2>
<details><summary>Is my donation tax-deductible?</summary><p>No. 16060 is not a registered charity, so support is a voluntary contribution to an independent website and is not tax-deductible.</p></details>
<details><summary>Can I get a refund?</summary><p>Contact us within 14 days and we'll refund a one-time donation, no questions asked. Memberships can be cancelled any time.</p></details>
<details><summary>Can my company sponsor instead?</summary><p>Yes. Sponsorships include visibility, so see <a href="advertise.html">Advertise &amp; Sponsor</a>.</p></details></div></section>
<script>
document.addEventListener("DOMContentLoaded",function(){
  var S=window.SITE, cur=S.currency||"USD", amt=document.getElementById("amt");
  document.getElementById("raised").textContent="$"+(S.fundRaised||0).toLocaleString();
  document.getElementById("goal").textContent="of $"+(S.fundGoal||6060).toLocaleString();
  document.getElementById("meter").style.width=Math.min(100,(S.fundRaised||0)/(S.fundGoal||6060)*100)+"%";
  document.getElementById("supporters-n").textContent=(S.supporters||[]).length;
  var wall=document.getElementById("wall");
  wall.innerHTML=(S.supporters||[]).length?S.supporters.map(function(s){return '<div class="card"><b>'+s.name+'</b> <span class="chip gold">$'+s.amount+'</span><p>'+(s.msg||"")+'</p></div>'}).join(""):'<div class="card"><p>🧧 Be the first name on our wall. Every red envelope counts.</p></div>';
  document.querySelectorAll(".tier").forEach(function(t){t.addEventListener("click",function(){document.querySelectorAll(".tier").forEach(function(x){x.classList.remove("on")});t.classList.add("on");if(+t.dataset.amt){amt.value=t.dataset.amt}else{amt.value="";amt.focus()}})});
  function pp(params){var u="https://www.paypal.com/cgi-bin/webscr?"+Object.keys(params).map(function(k){return k+"="+encodeURIComponent(params[k])}).join("&");window.open(u,"_blank","noopener")}
  document.getElementById("paypal-once").addEventListener("click",function(){var a=parseFloat(amt.value);if(!a||a<1){toast("Enter an amount",false);return}
    if(S.stripeLinks&&S.stripeLinks[String(a)]){window.open(S.stripeLinks[String(a)],"_blank","noopener");return}
    pp({cmd:"_donations",business:window.__route(),item_name:"16060.com — "+document.getElementById("purpose").value,amount:a.toFixed(2),currency_code:cur,no_shipping:1})});
  document.querySelectorAll("[data-sub]").forEach(function(b){b.addEventListener("click",function(){pp({cmd:"_xclick-subscriptions",business:window.__route(),item_name:b.dataset.name,a3:b.dataset.sub,p3:1,t3:"M",src:1,currency_code:cur,no_shipping:1})})});
  if(S.buyMeACoffee){document.getElementById("alt-pay").innerHTML='<a class="btn ghost block" href="'+S.buyMeACoffee+'" target="_blank" rel="noopener">☕ Buy Me a Coffee</a>'}
});
</script>'''
    page("support.html", "Support 16060 — Donate a Red Envelope", "Support free Chinese culture and timing tools with a one-time red envelope or monthly membership. Funds operations, promotion, talent and contest prizes.",
         body, hero=("Support 16060 <span class='zh' style='color:var(--red)'>红包</span>", "Donations fund operations, promotion, new talent and contest prizes."), crumbs=[("Support", "support.html")], priority="0.8")

    # ---------------- CONTESTS ----------------
    body = '''
<section><div class="wrap grid g2" style="align-items:start">
<div><span class="chip gold">Open now · free to enter</span><h2 style="margin-top:12px">The 16060 Lucky Number Story Contest</h2>
<p class="lead">Tell us about a number that changed your luck: a phone number, a wedding date, a lucky address, a license plate or a family tradition. The most compelling true stories win.</p>
<div class="countdown" id="contest-cd"></div><p class="small muted" style="margin-top:6px">Entries close 31 January 2027, 11:59 pm ET. Winners are announced by Lunar New Year, 6 February 2027.</p>
<h3 style="margin-top:22px">Prizes</h3>
<div class="grid g3"><div class="card center"><div style="font-size:2rem">🥇</div><b>$160.60</b><p class="small">Grand prize plus a Pro Blueprint reading</p></div><div class="card center"><div style="font-size:2rem">🥈</div><b>$60.60</b><p class="small">Second prize</p></div><div class="card center"><div style="font-size:2rem">🥉</div><b>$16.06</b><p class="small">Third prize</p></div></div>
<p class="small muted">Plus up to 10 honourable mentions featured on 16060. Paid by PayPal or e-transfer. <a href="legal/contest-rules.html">Official rules</a>.</p>
<h3>How to enter</h3><ol class="muted"><li>Write 100–600 words about your lucky (or unlucky!) number.</li><li>Optionally add a photo link or a video link.</li><li>Submit the form. One entry per person.</li><li><b>Bonus:</b> share your referral link. Each friend who enters earns you a bonus mention in our judging notes.</li></ol>
<h3>Judging</h3><p class="muted">Originality 40% · storytelling 30% · cultural insight 30%, judged by the 16060 editorial team.</p></div>
<div class="panel"><h3>Submit your entry</h3><form class="form" data-form data-subject="Contest entry" data-done="Your entry is in. Good luck! 祝你好运! Share the contest with friends to spread the luck.">
<div class="row"><label>Full name <input name="name" required></label><label>Email <input type="email" name="email" required></label></div>
<div class="row"><label>Country / province <input name="location" required></label><label>Your lucky number <input name="lucky_number" required></label></div>
<label>Story title <input name="title" required maxlength="100"></label>
<label>Your story (100–600 words) <textarea name="story" required minlength="400" style="min-height:200px"></textarea></label>
<label>Photo or video link <span class="opt">(optional)</span><input type="url" name="media_link" placeholder="https://"></label>
<label>Social handle <span class="opt">(optional, for a shout-out)</span><input name="social"></label>
<label>Referred by <span class="opt">(optional)</span><input name="referred_by" id="ref"></label>
<label class="check"><input type="checkbox" name="age_ok" value="yes" required> I am 18+ (or the age of majority where I live) and I accept the <a href="legal/contest-rules.html">Official Rules</a>.</label>
<label class="check"><input type="checkbox" name="original" value="yes" required> This is my own true story and I grant 16060 permission to publish it with credit.</label>
''' + HP + '''<button class="btn gold lg block" type="submit">Submit my entry</button>
<button type="button" class="btn ghost block" data-share="Enter the 16060 Lucky Number Story Contest" id="refshare">↗ Share my referral link</button></form></div>
</div></section>
<section class="alt"><div class="wrap grid g2">
<div class="card"><h3>🏅 Sponsor a prize</h3><p>Put your brand in front of every entrant and reader. Prize sponsors get logo placement, a shout-out in the winners' post and a newsletter feature.</p><p style="margin-top:12px"><a class="btn sm" href="advertise.html#form">Become a sponsor</a></p></div>
<div class="card"><h3>📅 Coming up</h3><p>• 520 Love Number Challenge (May) · • 8.8 Prosperity Photo Contest (August) · • Mid-Autumn Lantern Art (September). <a href="#" data-mail="Notify me about 16060 contests">Get notified</a></p></div></div></section>
<script>
document.addEventListener("DOMContentLoaded",function(){
  var cd=document.getElementById("contest-cd");cd.className="countdown";cd.setAttribute("data-countdown",(window.SITE||{}).contestDeadline||"2027-01-31T23:59:59-05:00");
  var r=new URL(location.href).searchParams.get("ref");if(r)document.getElementById("ref").value=r;
  var f=document.querySelector("form[data-subject='Contest entry']");
  f.addEventListener("input",function(){var e=f.querySelector("[name=name]").value.trim().split(" ")[0];if(e)document.getElementById("refshare").dataset.url=location.origin+location.pathname+"?ref="+encodeURIComponent(e)});
});
</script>'''
    page("contests.html", "Contests & Prizes — Lucky Number Story Contest", "Enter the free 16060 Lucky Number Story Contest. Share your lucky number story and win cash prizes. Entries close 31 January 2027.",
         body, hero=("Contests &amp; Prizes <span class='zh' style='color:var(--red)'>比赛</span>", "Free to enter, real prizes, and a celebration of the numbers that shape our lives."), crumbs=[("Contests", "contests.html")], priority="0.8")

    # ---------------- CAREERS ----------------
    roles = [
        ("Content Writer: Chinese Culture (EN / 中文)", "Freelance · Remote", "Research-driven guides on numbers, festivals, zodiac and timing. Bilingual is a plus."),
        ("Video Creator / Editor", "Freelance · Remote", "Short-form and YouTube explainers. Scripting, editing, motion graphics."),
        ("SEO & Growth Marketer", "Part-time · Remote", "Keyword strategy, programmatic pages, outreach and seasonal campaigns (Lunar New Year, 520, 8.8)."),
        ("Front-end Developer (JavaScript)", "Contract · Remote", "Build new calculators and widgets. Vanilla JS, accessibility, performance."),
        ("Practitioner Partner: BaZi / Feng Shui / Date Selection", "Partner network · Remote or local", "Receive qualified client requests. Set your own rates and languages."),
        ("Community & Social Media Manager", "Part-time · Remote", "Run contests, engage our audience across Instagram, TikTok, YouTube, 小红书 and WeChat."),
        ("Translator (Simplified / Traditional Chinese)", "Freelance · Remote", "Localise tools and guides for Chinese-speaking audiences."),
    ]
    rc = "".join(f'<div class="card hover"><h3>{t}</h3><p><span class="chip">{m}</span></p><p style="margin-top:8px">{d}</p><p style="margin-top:12px"><a href="#apply" onclick="document.querySelector(\'[name=role]\').value=\'{t}\'">Apply →</a></p></div>' for t, m, d in roles)
    opts = "".join(f"<option>{t}</option>" for t, m, d in roles) + "<option>Open application</option>"
    body = f'''<section><div class="wrap"><div class="section-head"><div><span class="eyebrow">Open roles</span><h2>Help build the world's best home for luck, timing and Chinese culture</h2></div><p>Remote-first. Paid work. Flexible hours. Funded by our advertisers, sponsors and supporters.</p></div>
<div class="grid g3">{rc}</div></div></section>
<section class="alt" id="apply"><div class="wrap grid g2" style="align-items:start"><div><h2>Apply</h2><p class="muted">Tell us who you are and share a link to your work. We review every application and reply to shortlisted candidates within two weeks.</p>
<div class="card"><h3>Why 16060?</h3><ul class="muted" style="padding-left:1.1em"><li>Your work reaches a global audience</li><li>Byline and portfolio credit</li><li>Performance bonuses on content that ranks and converts</li></ul></div></div>
<div class="panel"><form class="form" data-form data-subject="Job / partner application" data-done="Application received — thank you! We'll be in touch if there's a fit.">
<label>Role <select name="role">{opts}</select></label>
<div class="row"><label>Full name <input name="name" required></label><label>Email <input type="email" name="email" required></label></div>
<div class="row"><label>Location / timezone <input name="location" required></label><label>Languages <input name="languages" placeholder="English, 普通话, 粵語…"></label></div>
<div class="row"><label>Portfolio / LinkedIn / CV link <input type="url" name="portfolio" placeholder="https://" required></label><label>Rate expectation <span class="opt">(optional)</span><input name="rate"></label></div>
<label>Why you? <textarea name="pitch" required></textarea></label>
{HP}{CONSENT}<button class="btn lg" type="submit">Submit application</button></form></div></div></section>'''
    page("careers.html", "Careers & Talent — Work with 16060", "Remote roles for writers, video creators, SEO marketers, developers, translators and BaZi / feng shui practitioner partners.",
         body, hero=("Careers &amp; Talent", "Writers, creators, developers and practitioners: grow with us."), crumbs=[("Careers", "careers.html")], priority="0.6")

    # ---------------- ADVERTISE ----------------
    pk = [("Tool Sponsorship", "“Presented by” placement on a calculator, e.g. the Lucky Number Analyzer or Date Finder.", "Monthly"),
          ("Homepage Feature", "Premium banner and native card on the homepage.", "Weekly / monthly"),
          ("Festival Takeover", "Own the Lunar New Year, 520, Mid-Autumn or 8.8 season across relevant pages.", "Seasonal"),
          ("Newsletter Sponsorship", "Top slot in the lucky-days digest.", "Per issue"),
          ("Contest Sponsorship", "Fund a prize. Logo, shout-outs and entrant reach.", "Per contest"),
          ("Sponsored Guide / Video", "Clearly labelled partner content with rel=sponsored links.", "Per piece")]
    pc = "".join(f'<div class="card hover"><h3>{t}</h3><p>{d}</p><p style="margin-top:10px"><span class="chip gold">{u}</span></p></div>' for t, d, u in pk)
    body = f'''<section><div class="wrap"><div class="grid g4">
<div class="card"><div class="stat">10</div><p>Interactive tools, incl. the Blueprint</p></div><div class="card"><div class="stat">45+</div><p>Indexable pages at launch</p></div><div class="card"><div class="stat">5</div><p>Seasonal peaks each year</p></div><div class="card"><div class="stat">1</div><p>Clear, 5-digit brand domain</p></div></div>
<h2 style="margin-top:40px">Who you'll reach</h2><p class="lead">People searching for Chinese zodiac signs, lucky numbers, auspicious dates and festival timing: the Chinese diaspora, couples planning weddings, business owners and culture enthusiasts, mostly in North America and Southeast Asia.</p>
<h2 style="margin-top:30px">Placements</h2><div class="grid g3">{pc}</div>
<div class="callout" style="margin-top:22px">Ideal partners: wedding services, jewellery (gold, jade), red-envelope and gift shops, travel to Asia, language learning, telecom and number sellers, real estate, fintech and remittance, tea, and cultural events. Media kit and live traffic figures on request.</div></div></section>
<section class="alt" id="form"><div class="wrap grid g2" style="align-items:start"><div><h2>Interested in the whole thing?</h2><p class="lead">The website and the domain <b>16060.com</b> are also open to acquisition, joint venture and strategic partnership.</p><p><a class="btn gold lg" href="https://web.works/contact" target="_blank" rel="noopener">Inquire at web.works/contact</a></p></div>
<div class="panel"><h3>Advertising &amp; sponsorship inquiry</h3><form class="form" data-form data-subject="Advertising / sponsorship inquiry" data-done="Thanks! We'll send the media kit and availability within one business day.">
<div class="row"><label>Name <input name="name" required></label><label>Work email <input type="email" name="email" required></label></div>
<div class="row"><label>Company <input name="company" required></label><label>Website <input type="url" name="website" placeholder="https://"></label></div>
<div class="row"><label>Interest <select name="interest">{"".join(f"<option>{t}</option>" for t, d, u in pk)}<option>Domain / website acquisition</option><option>Partnership / JV</option></select></label><label>Monthly budget <select name="budget"><option>Under $500</option><option>$500–$2,000</option><option>$2,000–$10,000</option><option>$10,000+</option></select></label></div>
<label>Campaign goals <textarea name="goals"></textarea></label>{HP}{CONSENT}<button class="btn lg" type="submit">Request media kit</button></form></div></div></section>'''
    page("advertise.html", "Advertise, Sponsor or Partner with 16060", "Advertising, sponsorship and partnership opportunities on 16060: tool sponsorships, festival takeovers, newsletter and contest sponsorships.",
         body, hero=("Advertise · Sponsor · Partner", "Put your brand beside the moments people plan most carefully."), crumbs=[("Advertise", "advertise.html")], priority="0.7")

    # ---------------- CONTACT ----------------
    body = f'''<section><div class="wrap grid g2" style="align-items:start">
<div><h2>We'd love to hear from you</h2><p class="lead">Questions about a tool, a correction, press, partnerships or anything else.</p>
<div class="grid" style="gap:12px"><div class="card"><h3>📨 Email</h3><p><a href="#" data-mail="Hello from 16060.com">Send us an email</a>. We reply within 1–2 business days.</p></div>
<div class="card"><h3>💼 Domain, sponsorship &amp; partnership</h3><p><a href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a></p></div>
<div class="card"><h3>🧭 Consultations</h3><p><a href="consult.html#consult">Request a consultation</a></p></div></div></div>
<div class="panel"><form class="form" data-form data-subject="Contact form">
<div class="row"><label>Name <input name="name" required></label><label>Email <input type="email" name="email" required></label></div>
<label>Topic <select name="topic" id="topic"><option>General question</option><option>Tool feedback / bug</option><option>Content correction</option><option>Press / media</option><option>Advertising / sponsorship</option><option>Corporate</option><option>Partnership</option><option>Domain / website acquisition</option><option>Copyright / takedown request</option></select></label>
<label>Message <textarea name="message" required></textarea></label>{HP}{CONSENT}
<button class="btn lg" type="submit">Send message</button></form></div></div></section>
<script>document.addEventListener("DOMContentLoaded",function(){{var t=new URL(location.href).searchParams.get("topic");if(t){{var s=document.getElementById("topic");[].forEach.call(s.options,function(o){{if(o.text.indexOf(t)===0)s.value=o.text}})}}}});</script>'''
    page("contact.html", "Contact 16060", "Contact 16060 for questions, feedback, press, advertising, partnerships or domain inquiries.", body,
         hero=("Contact", "Every message is read by a human."), crumbs=[("Contact", "contact.html")], priority="0.6")

    # ---------------- ABOUT ----------------
    body = '''<section><div class="narrow prose">
<h2>Why “1 · 60 · 60”?</h2><p>An hour is sixty minutes of sixty seconds. A complete cycle of the Chinese calendar is sixty years. 16060 stands for <b>good timing</b>: the right number, the right day, the right moment.</p>
<h2>What we do</h2><ul><li><b>Free tools</b> built on astronomical calendar data (1921–2060): lucky numbers, zodiac, compatibility, BaZi, lunar conversion, auspicious dates, world clocks and countdowns.</li><li><b>Clear guides</b> that separate tradition from hype, with sources where facts are claimed.</li><li><b>Expert help</b> for decisions that matter, through vetted practitioners.</li><li><b>Community</b>: contests, stories and a growing library of videos.</li></ul>
<h2>Our principles</h2><ol><li><b>Accuracy first.</b> Calendar data is computed, not guessed.</li><li><b>Respect.</b> These are living cultural traditions, not gimmicks.</li><li><b>Honesty.</b> We label interpretation as interpretation. Nothing here is financial, legal or medical advice.</li><li><b>Free at the core.</b> Ads, sponsors and supporters keep the tools free.</li></ol>
<div class="callout">Interested in this website, the domain name, sponsorship, advertising or partnership? <a href="https://web.works/contact" target="_blank" rel="noopener">Contact us at web.works/contact</a>.</div>
</div></section>'''
    page("about.html", "About 16060", "About 16060: free tools and guides for Chinese lucky numbers, zodiac and auspicious timing. One hour, sixty minutes, sixty seconds.", body,
         hero=("About 16060", "One hour · sixty minutes · sixty seconds. One cycle · sixty years."), crumbs=[("About", "about.html")], priority="0.5")

    # ---------------- VIDEOS ----------------
    body = f'''<section><div class="wrap"><div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:18px" id="vf"><button class="btn sm" data-f="">All</button><button class="btn ghost sm" data-f="Zodiac">Zodiac</button><button class="btn ghost sm" data-f="Numbers">Numbers</button><button class="btn ghost sm" data-f="Culture">Culture</button><button class="btn ghost sm" data-f="Stories">Stories</button></div>
<div class="videos" id="vids"></div>{ad()}
<div class="grid g2" style="margin-top:30px"><div class="card"><h3>▶ Subscribe to our channel</h3><p>New explainers on numbers, festivals and timing.</p><p style="margin-top:10px" id="yt-sub"><span class="muted">Channel launching soon.</span></p></div>
<div class="panel"><h3>Feature your video</h3><p class="muted">Creators: submit a video about Chinese culture, numbers or festivals to be featured.</p>
<form class="form" data-form data-subject="Video submission"><div class="row"><label>Name <input name="name" required></label><label>Email <input type="email" name="email" required></label></div><label>YouTube URL <input type="url" name="video" required placeholder="https://youtube.com/watch?v="></label>{HP}<button class="btn" type="submit">Submit video</button></form></div></div></div></section>
<script>document.addEventListener("DOMContentLoaded",function(){{var V=(window.SITE||{{}}).videos||[];function r(f){{renderVideos("#vids",f?V.filter(function(v){{return v.tag===f}}):V)}}r("");document.getElementById("vf").addEventListener("click",function(e){{var b=e.target.closest("[data-f]");if(!b)return;[].forEach.call(this.children,function(x){{x.className="btn ghost sm"}});b.className="btn sm";r(b.dataset.f)}});var c=(window.SITE||{{}}).youtubeChannel;if(c)document.getElementById("yt-sub").innerHTML='<a class="btn sm" href="'+c+'?sub_confirmation=1" target="_blank" rel="noopener">Subscribe on YouTube</a>'}});</script>'''
    page("videos.html", "Videos: Chinese Zodiac, Lucky Numbers & Culture", "Watch the best videos on the Chinese zodiac, lucky numbers, the Great Race legend and Chinese culture.", body,
         hero=("Video Library <span class='zh' style='color:var(--red)'>视频</span>", "Hand-picked explainers on the zodiac, numbers and traditions."), crumbs=[("Videos", "videos.html")], priority="0.7")

    # ---------------- FESTIVALS ----------------
    import json
    F = json.load(open(os.path.join(HERE, "fest.json")))
    names = []
    for f in F:
        if f["name"] not in [n[0] for n in names]: names.append((f["name"], f["zh"], f["desc"], f["lunar"]))
    rows = ""
    for n, zh, d, l in names:
        ds = [x["date"] for x in F if x["name"] == n and "2026" <= x["date"][:4] <= "2030"]
        rows += f'<tr><td><b>{n}</b><br><span class="zh muted">{zh}</span></td><td>{l}</td>' + "".join(f"<td>{next((x for x in ds if x.startswith(str(y))), '—')}</td>" for y in range(2026, 2031)) + "</tr>"
    cards = "".join(f'<div class="card"><h3>{n} <span class="zh" style="color:var(--red)">{zh}</span></h3><p>{d}</p></div>' for n, zh, d, l in names)
    body = f'''<section><div class="wrap"><h2>Festival calendar 2026–2030</h2><div class="table-wrap"><table><tr><th>Festival</th><th>Lunar date</th><th>2026</th><th>2027</th><th>2028</th><th>2029</th><th>2030</th></tr>{rows}</table></div>
<p class="small muted" style="margin-top:8px">Dates computed from the Chinese lunisolar calendar (China Standard Time). Live countdowns are on the <a href="tools/countdown.html">countdown page</a>.</p>{ad()}
<h2 style="margin-top:34px">The festivals</h2><div class="grid g3">{cards}</div>
<div class="videos" data-videos="3" data-tag="Stories" style="margin-top:26px"></div></div></section>'''
    page("festivals.html", "Chinese Festival Calendar 2026–2030", "Dates for Chinese New Year, Lantern, Qingming, Dragon Boat, Qixi, Mid-Autumn, Double Ninth and more, from 2026 to 2030.", body,
         hero=("Chinese Festival Calendar <span class='zh' style='color:var(--red)'>节日</span>", "Every major festival from 2026 to 2030, computed from the lunisolar calendar."), crumbs=[("Festivals", "festivals.html")], priority="0.8")

    # ---------------- 404 ----------------
    page("404.html", "Page not found", "This page could not be found.", '<section><div class="narrow center"><div class="zh" style="font-size:6rem;color:var(--red)">迷</div><h1>Lost in time</h1><p class="lead" style="margin-inline:auto">This page doesn\'t exist, but your lucky number might. Try one of our tools.</p><p><a class="btn" href="index.html">Home</a> <a class="btn ghost" href="tools/index.html">All tools</a></p></div></section>')
