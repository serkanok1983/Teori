#!/usr/bin/env python3
"""EA kartları, 4. parti: örneklerdeki tüm rakamlar. Temsili veriler. Çalıştır: python3 scripts/cards_numbers_ea_b4.py"""
from decimal import Decimal as D, ROUND_HALF_UP
import sqlite3
q=lambda x,p="0.01": D(x).quantize(D(p),ROUND_HALF_UP)
def tl(x,p="0.01"):
    n=len(p.split('.')[1]) if '.' in p else 0
    return f"{q(x,p):,.{n}f}".replace(",","X").replace(".",",").replace("X",".")
pct=lambda x,p="0.1": "%"+tl(D(x)*100,p)

print("== kb-ea-17-4 tedarikçi puanlama")
w=[D("0.40"),D("0.25"),D("0.20"),D("0.15")]
for k,s in {"A":[4,3,4,3],"B":[3,5,3,4],"C":[5,2,3,3]}.items(): print(k,tl(sum(a*b for a,b in zip(w,s))))
print("huni 9 -> 5 -> 3 -> 2")

print("== kb-ea-18-3 sapma")
pm,am=8,13; pb,ab=D(3000000),D(4200000); print("süre sapması",pct(D(am-pm)/pm),"bütçe sapması",pct((ab-pb)/pb))

print("== kb-ea-18-4 canlı geçiş sonrası düşüş")
base=400
for wk,v in [(1,260),(2,300),(4,360),(8,410)]: print("hafta",wk,v,pct(D(v-base)/base))

print("== kb-ea-18-5 aşama süreleri")
ph={"Hazırlık":3,"Keşif (standarda uyum)":6,"Gerçekleştirme":12,"Canlıya geçiş":4}; t=sum(ph.values())
for k,v in ph.items(): print(k,v,pct(D(v)/t))
print("toplam hafta",t)

print("== kb-ea-18-6 açılış bakiyesi mutabakatı (sqlite)")
c=sqlite3.connect(":memory:")
c.executescript("""
create table eski(cari text, bakiye_kurus int); create table yeni(cari text, bakiye_kurus int);
insert into eski values ('C001',1250000),('C002',845050),('C003',230000),('C004',99000),('C005',412575);
insert into yeni values ('C001',1250000),('C002',845050),('C003',203000),('C005',412575),('C006',15000);
""")
sql="""select coalesce(e.cari,y.cari) cari, e.bakiye_kurus eski, y.bakiye_kurus yeni,
 coalesce(y.bakiye_kurus,0)-coalesce(e.bakiye_kurus,0) fark
 from eski e left join yeni y on e.cari=y.cari
 union all select y.cari,null,y.bakiye_kurus,y.bakiye_kurus from yeni y where y.cari not in (select cari from eski)"""
rows=[r for r in c.execute(sql) if r[3]!=0]
print("SQL:",sql.replace("\n"," "))
for r in rows: print(r[0],"eski",tl(D(r[1] or 0)/100),"yeni",tl(D(r[2] or 0)/100),"fark",tl(D(r[3])/100))
te=c.execute("select sum(bakiye_kurus) from eski").fetchone()[0]; ty=c.execute("select sum(bakiye_kurus) from yeni").fetchone()[0]
print("toplam eski",tl(D(te)/100),"yeni",tl(D(ty)/100),"fark",tl(D(ty-te)/100))

print("== kb-ea-18-7 eğitim")
u=85; print("anahtar kullanıcı (10 kişiye 1)",-(-u//10),"eğitim saati 6 saat",u*6)

print("== kb-ea-19-1 kazanılmış değer")
BAC=D(1200000); PV=BAC*D("0.5"); EV=BAC*D("0.4"); AC=D(560000)
CPI=EV/AC; SPI=EV/PV; print("PV",tl(PV,"1"),"EV",tl(EV,"1"),"AC",tl(AC,"1"),"CPI",tl(CPI),"SPI",tl(SPI),"EAC",tl(BAC/CPI,"1"))

print("== kb-ea-19-3 AMS sözleşmesi")
base_h,rate,extra_h,erate=80,D(2000),15,D(2400); print("paket",tl(base_h*rate,"1"),"ek",tl(extra_h*erate,"1"),"toplam",tl(base_h*rate+extra_h*erate,"1"))
print("ek saatlerin payı",pct(D(extra_h)/(base_h+extra_h)))

print("== kb-ea-20-1 tekrarlı giriş")
o=400; print("üç ayrı giriş",o*3,"tek giriş",o,"azalma",pct(D(o*2)/(o*3)))

print("== kb-ea-20-3 üçlü eşleştirme")
po,gr,inv,pr=1000,980,1000,D("42.00"); print("fark adet",inv-gr,"tutar",tl((inv-gr)*pr),"fatura",tl(inv*pr),"mal kabul",tl(gr*pr))

print("== kb-ea-20-4 kapanış")
print("kapanış 12 -> 5 iş günü, kısalma",pct(D(7)/12))

print("== kb-ea-20-5 hareketli ortalama")
q0,c0,q1,c1=500,D("20.00"),300,D("24.00"); avg=(q0*c0+q1*c1)/(q0+q1); print("ortalama",tl(avg),"stok değeri",tl(q0*c0+q1*c1))
print("200 çıkış değeri",tl(200*avg),"kalan",600,tl(600*avg))
std=D("21.00"); print("standart maliyetle fiyat farkı",tl(q1*(c1-std)))

print("== kb-ea-20-6 MRP")
fg=1000; per=2; gross=fg*per; oh=600; sr=400; net=gross-oh-sr; lot=500; order=-(-net//lot)*lot
print("brüt",gross,"net",net,"sipariş",order,"; teslim 10. hafta, temin süresi 2 hafta -> sipariş 8. hafta")

print("== kb-ea-18-5 boşluk sınıflandırma")
gaps={"süreç değişikliği":14,"yapılandırma/küçük geliştirme":8}; print("toplam boşluk",sum(gaps.values()),gaps)
print("== kb-ea-18-3 kapsam artışı: gerçekleştirme aşamasında gelen yeni rapor/ekran isteği", 31)
