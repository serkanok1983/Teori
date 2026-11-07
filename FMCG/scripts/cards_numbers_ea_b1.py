#!/usr/bin/env python3
"""EA kartları, 1. parti: örneklerdeki tüm rakamlar. Temsili veriler. Çalıştır: python3 scripts/cards_numbers_ea_b1.py"""
from decimal import Decimal as D, ROUND_HALF_UP
import sqlite3, statistics
q=lambda x,p="0.01": D(x).quantize(D(p),ROUND_HALF_UP)
def tl(x,p="0.01"):
    n=len(p.split('.')[1]) if '.' in p else 0
    return f"{q(x,p):,.{n}f}".replace(",","X").replace(".",",").replace("X",".")
pct=lambda x,p="0.1": "%"+tl(D(x)*100,p)

print("== kb-ea-1-1 tekrar giriş maliyeti")
orders,reentries,minutes,err=D(120),D(2),D("1.5"),D("0.02")
m=orders*reentries*minutes; print("günlük ek giriş dk",tl(m,"1"),"saat",tl(m/60,"0.1"))
print("günlük hatalı kayıt",tl(orders*reentries*err,"0.1"),"ayda (22 gün)",tl(orders*reentries*err*22,"1"))
print("ayda saat (22 gün)",tl(m*22/60,"1"))

print("== kb-ea-1-5 lisans vs abonelik, 5 yıl")
lic,maint=D(900000),D("0.20"); users,fee=D(25),D(1800)
cl=cs=D(0)
for y in range(1,6):
    cl+= lic if y==1 else 0; cl+=lic*maint; cs+=users*fee*12
    print(f"yıl {y}: lisans kümülatif {tl(cl,'1')} abonelik kümülatif {tl(cs,'1')}")
print("yıllık bakım",tl(lic*maint,'1'),"yıllık abonelik",tl(users*fee*12,'1'))
exitc=D(350000); print("çıkış maliyeti / yıllık abonelik =",tl(exitc/(users*fee*12),"0.01"))

print("== kb-ea-2-2 benimseme")
actual,recorded=D(1840),D(1288); print("uygulamada kayıtlı ziyaret oranı",pct(recorded/actual))
reps={"A":(6.1,3.2),"B":(3.4,5.9),"C":(5.8,5.6)}
for k,(u,e) in reps.items(): print(k,"fayda",u,"kolaylık",e)
w=D(40); print("40 temsilcinin %30'u", tl(w*D("0.30"),"1"))
print("hedef %90 için ek kayıt",tl(actual*D("0.90")-recorded,"1"))

print("== kb-ea-3-2 tamamlayıcılık")
for name,ld0,ld1,err0,err1 in [("A",D(2),D(1),D("0.031"),D("0.009")),("B",D(2),D("1.8"),D("0.031"),D("0.027"))]:
    print(name,"teslim süresi değişimi",pct((ld1-ld0)/ld0),"hata değişimi",pct((err1-err0)/err0))
inv=D(1500000); print("yatırım her ikisinde",tl(inv,"1"))
orders=D(30000); print("A yılda önlenen hatalı sipariş",tl(orders*(D("0.031")-D("0.009")),"1"),"B",tl(orders*(D("0.031")-D("0.027")),"1"))
cost=D(450); print("A tasarruf",tl(orders*(D("0.031")-D("0.009"))*cost,"1"),"B",tl(orders*(D("0.031")-D("0.027"))*cost,"1"))

print("== kb-ea-3-6 iş gerekçesi NBD")
I=D(1800000); ben=[D(500000),D(900000),D(1100000),D(1100000),D(1100000)]; run=D(250000); r=D("0.35")
npv=-I; cum=-I; pb=None
for t,b in enumerate(ben,1):
    cf=b-run; npv+=cf/(1+r)**t; prev=cum; cum+=cf
    print(f"yıl {t}: net akış {tl(cf,'1')} bugünkü değer {tl(cf/(1+r)**t,'1')} kümülatif {tl(cum,'1')}")
    if pb is None and cum>=0: pb=t-1+(-prev/cf)
print("NBD",tl(npv,'1'),"geri dönüş yıl",tl(pb,'0.1'))
tot=sum(b-run for b in ben); print("5 yıl net fayda",tl(tot,'1'),"basit getiri",pct((tot-I)/I))
npv2=-I+sum((b*D("0.7")-run)/(1+r)**t for t,b in enumerate(ben,1)); print("fayda %30 düşük NBD",tl(npv2,'1'))

print("== kb-ea-4-1 el değiştirme")
h0,w=6,D(3); print("6 el değiştirme bekleme saat",tl(h0*w,'0.1'),"3 el değiştirme",tl(3*w,'0.1'))
print("dokunma süresi 40 dk oranı 18 saatte",pct(D(40)/(D(18)*60+40)))

print("== kb-ea-4-2 izleme medyan")
before=[3,5,2,8,4,6,9,3,5,7,4,12]; after=[1,2,1,3,2,1,4,2,2,1,3,2]
print("önce medyan",statistics.median(before),"ort",tl(D(sum(before))/len(before),'0.1'),"sonra medyan",statistics.median(after),"ort",tl(D(sum(after))/len(after),'0.1'))
print("5 günü aşan önce",sum(x>5 for x in before),"/12 sonra",sum(x>5 for x in after))

print("== kb-ea-4-3 BPMN geçit")
N=D(1000); over=N*D("0.18"); appr=over*D("0.60"); print("limit aşan",tl(over,'1'),"onaylanan",tl(appr,'1'),"reddedilen",tl(over-appr,'1'),"doğrudan",tl(N-over,'1'),"sevk edilen toplam",tl(N-over+appr,'1'))

print("== kb-ea-4-6 Little")
thr=D(80); ct=D("2.5"); print("WIP",tl(thr*ct,'1'))
touch=D(35); elapsed=ct*24*60; print("akış verimliliği",pct(touch/elapsed,'0.01'))
wip2=D(100); print("WIP 100 ise süre gün",tl(wip2/thr,'0.01'))
tw=D(8*60); print("8 saatlik iş günü bazında akış verim (2,5 iş günü)",pct(touch/(ct*tw),'0.1'))
cpc=(D(4)*D(52000)/D(22)/D(80)); print("vaka başı personel maliyeti (4 kişi, 52.000 TL/ay, 22 gün, 80 vaka/gün)",tl(cpc))

print("== kb-ea-4-7 süreç madenciliği (sqlite)")
db=sqlite3.connect(":memory:")
db.execute("create table olay(vaka text, aktivite text, zaman text)")
log=[("S1","Sipariş","2026-10-01 09:00"),("S1","Onay","2026-10-01 09:30"),("S1","Sevk","2026-10-02 08:00"),("S1","Fatura","2026-10-02 08:10"),
("S2","Sipariş","2026-10-01 10:00"),("S2","Sevk","2026-10-01 16:00"),("S2","Fatura","2026-10-01 16:05"),
("S3","Sipariş","2026-10-01 11:00"),("S3","Onay","2026-10-02 15:00"),("S3","Sevk","2026-10-03 09:00"),("S3","Fatura","2026-10-03 09:20"),
("S4","Sipariş","2026-10-01 12:00"),("S4","Onay","2026-10-01 12:20"),("S4","Sevk","2026-10-02 10:00"),("S4","Fatura","2026-10-02 10:05"),
("S5","Sipariş","2026-10-01 13:00"),("S5","Sevk","2026-10-02 09:00"),("S5","Fatura","2026-10-04 11:00"),("S5","Fatura","2026-10-04 11:30")]
db.executemany("insert into olay values(?,?,?)",log)
sql1="""select varyant, count(*) vaka_sayisi from (
  select vaka, group_concat(aktivite,' > ') varyant from (select * from olay order by vaka, zaman) group by vaka)
group by varyant order by vaka_sayisi desc;"""
sql2="""select vaka, round((julianday(max(zaman))-julianday(min(zaman)))*24,1) saat from olay group by vaka order by saat desc;"""
print(sql1); [print(r) for r in db.execute(sql1)]
print(sql2); [print(r) for r in db.execute(sql2)]

print("== kb-ea-4-9 onay matrisi")
reqs=D(600); s1,s2,s3=D("0.70"),D("0.25"),D("0.05")
print("şef",tl(reqs*s1,'1'),"müdür",tl(reqs*s2,'1'),"direktör",tl(reqs*s3,'1'))
old=reqs*1; print("eskiden direktöre giden",tl(old,'1'))
wait_old,wait_new=D(26),D("4.5"); print("ort bekleme saat",wait_old,"->",wait_new,"azalış",pct((wait_new-wait_old)/wait_old))

print("== kb-ea-5-4 portföy TIME")
apps={"Eski ön muhasebe":(2,2),"ERP":(4,4),"Excel prim tablosu":(4,1),"Depo barkod uygulaması":(2,4),"Mobil sipariş (eski)":(3,2)}
for a,(bf,tq) in apps.items():
    t="Yatırım yap (Invest)" if bf>=3 and tq>=3 else "Taşı (Migrate)" if bf>=3 else "Koru/izle (Tolerate)" if tq>=3 else "Kaldır (Eliminate)"
    print(a,bf,tq,t)
