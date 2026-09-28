import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layout import OUT, HERE
os.makedirs(os.path.join(OUT,'assets/js'), exist_ok=True)
import sxtwl, datetime, json
from lunardate import LunarDate
F=[("Lunar New Year","春节",1,1,"The biggest festival of the year — family reunions, red envelopes, lion dances and fireworks."),
   ("Lantern Festival","元宵节",1,15,"The first full moon closes the New Year season with lanterns, riddles and sweet tangyuan."),
   ("Dragon Boat Festival","端午节",5,5,"Dragon boat races and zongzi rice dumplings honour the poet Qu Yuan."),
   ("Qixi (Chinese Valentine's Day)","七夕",7,7,"The legend of the Cowherd and the Weaver Girl, reunited once a year on a bridge of magpies."),
   ("Ghost Festival","中元节",7,15,"Offerings are made to ancestors and wandering spirits in the middle of the 7th lunar month."),
   ("Mid-Autumn Festival","中秋节",8,15,"Mooncakes, lanterns and moon-gazing under the fullest moon of the year."),
   ("Double Ninth Festival","重阳节",9,9,"A day for climbing heights, chrysanthemums and honouring elders."),
   ("Laba Festival","腊八节",12,8,"Laba congee marks the countdown to the New Year.")]
out=[]
for y in range(2025,2033):
    for n,zh,m,d,desc in F:
        try:
            s=LunarDate(y,m,d).to_solar_date()
            out.append({"name":n,"zh":zh,"date":s.isoformat(),"desc":desc,"lunar":f"{m}/{d}"})
        except Exception as e: print(e)
# solar-term festivals
def term(y,idx):
    d=datetime.date(y,1,1)
    while d.year==y:
        x=sxtwl.fromSolar(d.year,d.month,d.day)
        if x.hasJieQi() and x.getJieQi()==idx: return d
        d+=datetime.timedelta(1)
for y in range(2025,2033):
    out.append({"name":"Qingming (Tomb-Sweeping Day)","zh":"清明节","date":term(y,7).isoformat(),"desc":"Families sweep ancestors' tombs and enjoy spring outings.","lunar":"solar term"})
    out.append({"name":"Winter Solstice Festival","zh":"冬至","date":term(y,0).isoformat(),"desc":"'Winter solstice is as big as the New Year' — dumplings in the north, tangyuan in the south.","lunar":"solar term"})
out.sort(key=lambda x:x["date"])
open(os.path.join(OUT,'assets/js/festivals.js'),'w').write('window.FESTIVALS='+json.dumps(out,ensure_ascii=False,separators=(',',':'))+';')
json.dump(out,open(os.path.join(HERE,'fest.json'),'w'),ensure_ascii=False)
print([o for o in out if o['date']>='2026-09-28'][:4])
