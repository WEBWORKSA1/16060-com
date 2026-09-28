import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layout import OUT, HERE
os.makedirs(os.path.join(OUT,'assets/js'), exist_ok=True)
import sxtwl, datetime, json
E=datetime.date(1900,1,1)
start=datetime.date(1920,1,1); end=datetime.date(2061,12,31)
terms=[]; months=[]
d=start
while d<=end:
    x=sxtwl.fromSolar(d.year,d.month,d.day)
    n=(d-E).days
    if x.hasJieQi(): terms.append([n,x.getJieQi()])
    if x.getLunarDay()==1: months.append([n,x.getLunarMonth(),1 if x.isLunarLeap() else 0])
    d+=datetime.timedelta(1)
# check term index of Feb 4 2026
print([t for t in terms if E+datetime.timedelta(t[0])==datetime.date(2026,2,4)])
# compress terms: first index + consecutive check
idx0=terms[0][1]
ok=all(terms[i][1]==(idx0+i)%24 for i in range(len(terms)))
print('seq ok',ok, len(terms), len(months))
data={"epoch":"1900-01-01","t0":idx0,"terms":[t[0] for t in terms],"months":[m[0]*100+m[1]*2+m[2] for m in months]}
# CNY per year
cny={}
for m in months:
    if m[1]==1 and m[2]==0:
        dt=E+datetime.timedelta(m[0]); cny[dt.year]=dt.isoformat()
data["cny"]=cny
open(os.path.join(OUT,'assets/js/caldata.js'),'w').write('window.CAL='+json.dumps(data,separators=(',',':'))+';')
json.dump(cny,open(os.path.join(HERE,'cny.json'),'w'))
print(cny[2026],cny[2027],cny[2028])
