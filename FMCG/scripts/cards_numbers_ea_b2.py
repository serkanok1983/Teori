#!/usr/bin/env python3
"""EA kartları, 2. parti: örneklerdeki tüm rakamlar. Temsili veriler. Çalıştır: python3 scripts/cards_numbers_ea_b2.py"""
from decimal import Decimal as D, ROUND_HALF_UP
import sqlite3, difflib
q=lambda x,p="0.01": D(x).quantize(D(p),ROUND_HALF_UP)
def tl(x,p="0.01"):
    n=len(p.split('.')[1]) if '.' in p else 0
    return f"{q(x,p):,.{n}f}".replace(",","X").replace(".",",").replace("X",".")
pct=lambda x,p="0.1": "%"+tl(D(x)*100,p)

print("== kb-ea-5-5 noktadan noktaya arayüz sayısı")
for n in (4,6,8): print(n,"sistem, herkes herkesle:",n*(n-1)//2)
cost=D(40000); print("6 sistem 15 arayüz yıllık bakım",tl(15*cost,"1"),"; ERP çekirdek + 3 uydu = 3 arayüz",tl(3*cost,"1"))

print("== kb-ea-6-2 erişilebilirlik → izin verilen kesinti (30 gün)")
for a in ("0.995","0.999","0.9995"):
    mins=(1-D(a))*30*24*60; print(pct(a,"0.01"),"→",tl(mins,"0.1"),"dk =",tl(mins/60,"0.1"),"saat")

print("== kb-ea-6-3 risk puanı = olasılık × etki")
risks=[("Fidye yazılımı ile sunucuların şifrelenmesi",3,5),("Ayrılan çalışanın hesabının açık kalması",4,3),("Saha tabletinin kaybolması",4,2),("Yedeklerin geri yüklenememesi",2,5)]
for r,o,e in sorted(risks,key=lambda x:-x[1]*x[2]): print(r,o,e,o*e)

print("== kb-ea-6-4 görevler ayrılığı çakışması (SQLite)")
db=sqlite3.connect(":memory:"); c=db.cursor()
c.execute("create table yetki(kullanici, islem)")
c.executemany("insert into yetki values(?,?)",[("ayse","cari_kart_ac"),("ayse","odeme_onayla"),("mehmet","odeme_onayla"),("zeynep","cari_kart_ac"),("zeynep","fatura_kes"),("ali","cari_kart_ac"),("ali","odeme_onayla"),("ali","fatura_kes"),("can","fatura_kes")])
sql="""select a.kullanici from yetki a join yetki b on a.kullanici=b.kullanici
where a.islem='cari_kart_ac' and b.islem='odeme_onayla' order by 1;"""
print(sql); print(c.execute(sql).fetchall())

print("== kb-ea-8-1 / 8-3 mükerrer müşteri")
n,dup=D(12000),D("0.08"); print("mükerrer kayıt",tl(n*dup,"1"))
pairs=[("Yıldız Market","Yildiz Mrkt."),("Yıldız Market","Yıldız Büfe"),("Öz Kardeşler Gıda","Oz Kardesler Gida Ltd"),("Deniz Bakkal","Deniz Bakkaliye")]
tr=str.maketrans("ıİöÖüÜşŞğĞçÇ","iIoOuUsSgGcC")
for a,b in pairs:
    r=difflib.SequenceMatcher(None,a.lower().translate(tr),b.lower().translate(tr)).ratio(); print(a,"|",b,"benzerlik",tl(r,"0.01"))

print("== kb-ea-8-2 veri kalitesi")
N=5000; probs={"telefon boş":600,"konum 500 m'den fazla sapmış":250,"vergi no geçersiz (10 hane değil)":90,"kanal tipi boş":410}
for k,v in probs.items(): print(k,v,pct(D(v)/N))

print("== kb-ea-8-4 GTIN-13 kontrol hanesi")
def chk(s12):
    t=sum(int(d)*(3 if i%2 else 1) for i,d in enumerate(s12)); return (10-t%10)%10
for s in ("590123412345","400638133393"): print(s,"→",s+str(chk(s)))

print("== kb-ea-9-1 rapor yükü")
lines=D(8000)*D(22)*D(12); print("yıllık fatura satırı",tl(lines,"1"))

print("== kb-ea-9-2 sell-in / sell-out yıldız şema (SQLite)")
c.execute("create table urun(urun_id, urun_adi)"); c.executemany("insert into urun values(?,?)",[(1,"Ayran 200 ml"),(2,"Yoğurt 1 kg"),(3,"Peynir 500 g")])
c.execute("create table sell_in(tarih, urun_id, koli)"); c.executemany("insert into sell_in values(?,?,?)",[("2026-09-02",1,400),("2026-09-16",1,300),("2026-09-02",2,250),("2026-09-09",3,120)])
c.execute("create table sell_out(tarih, urun_id, koli)"); c.executemany("insert into sell_out values(?,?,?)",[("2026-09-05",1,320),("2026-09-20",1,310),("2026-09-07",2,140),("2026-09-21",2,60),("2026-09-12",3,115)])
sql2="""select u.urun_adi, i.koli sell_in, o.koli sell_out, i.koli-o.koli stok_degisimi,
 round(100.0*o.koli/i.koli,1) devir_yuzde
from urun u join (select urun_id,sum(koli) koli from sell_in group by urun_id) i using(urun_id)
join (select urun_id,sum(koli) koli from sell_out group by urun_id) o using(urun_id) order by u.urun_id;"""
print(sql2)
for r in c.execute(sql2): print(r)

print("== kb-ea-9-6 dağıtım KPI")
tot=D(2000); carry=D(1300); totsales=D(50_000_000); carrysales=D(41_000_000)
print("sayısal dağıtım",pct(carry/tot),"ağırlıklı dağıtım",pct(carrysales/totsales))
