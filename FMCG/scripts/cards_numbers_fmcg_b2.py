#!/usr/bin/env python3
"""FMCG kartları, parti 2: örnek rakamlar (temsili)."""
import math
def tl(x,d=2): s=f"{x:,.{d}f}"; return s.replace(',','X').replace('.',',').replace('X','.')
def pct(x,d=2): return '%'+tl(x*100,d)
print("== 3-4 ==")
N=1000; present=600; catsales_total=50_000_000; catsales_present=37_500_000
print("sayısal",pct(present/N,0),"ağırlıklı",pct(catsales_present/catsales_total,0))
avg_abs=(catsales_total-catsales_present)/(N-present); share=0.08
print("dışarıdaki nokta ort kategori satış",tl(avg_abs,0),"100 yeni nokta * pay",tl(100*avg_abs*share,0))
print("== 3-5 ==")
b,pl=42.0,35.0; q=1_000_000; print("prim",pct(b/pl-1),"yıllık prim geliri",tl((b-pl)*q,0))
print("== 3-7 ==")
H=10000; steps=[("bilinirlik",0.80),("değerlendirme",0.50),("mağazada bulma",0.70),("rafta seçme",0.60),("tekrar alma",0.45)]
x=H
for n,r in steps: x*=r; print(n,pct(r,0),tl(x,0))
x2=H*0.8*0.5*0.85*0.6; print("bulma %85 olursa alıcı",tl(x2,0),"vs",tl(H*0.8*0.5*0.7*0.6,0))
print("== 3-8 ==")
for e in (0.05,0.03): print("hata",e,"n",math.ceil(1.96**2*0.25/e**2))
p=0.30; n=400; print("p=0,30 n=400 hata payı ±",pct(1.96*math.sqrt(p*(1-p)/n)))
print("== 4-2 ==")
segs={"Fiyat odaklı aile":(40,0.03,2,4),"Premium bireysel":(15,0.12,4,2),"Sağlık odaklı":(10,0.20,5,3)}
w=(0.4,0.3,0.3)
for k,(sz,g,fit,comp) in segs.items():
    print(k,"büyüklük",sz,"büyüme",pct(g,0),"5 yıl sonra",tl(sz*(1+g)**5,1))
print("== 4-3 ==")
for n,c,p in (("Maliyet lideri",20,25),("Farklılaşan",24,32)): print(n,"birim kâr",tl(p-c),"marj",pct((p-c)/p))
print("== 4-4 ==")
sk=[38,22,12,8,6,4,3,2,2,1.5,0.8,0.4,0.2,0.1,0.0]
tot=sum(sk); print("SKU",len(sk),"toplam katkı",tl(tot,1),"ilk 3 pay",pct(sum(sk[:3])/tot,1),"son 5 pay",pct(sum(sk[-5:])/tot,1))
print("== 4-5 ==")
stages=[("Fikir taraması",50_000,0.5),("Konsept testi",300_000,0.6),("Geliştirme",1_200_000,0.7),("Test pazarı",2_500_000,0.6)]
cum=1; exp=0
for n,c,p in stages: exp+=c*cum; cum*=p
print("başarı olasılığı",pct(cum),"proje başı beklenen maliyet",tl(exp,0),"başarılı ürün başı",tl(exp/cum,0))
nogate=sum(c for _,c,_ in stages); print("kapısız (hepsi sonuna gider) proje başı",tl(nogate,0),"başarı başı",tl(nogate/cum,0))
print("== 4-6 ==")
tail_sales=6_000_000; cm=0.30; transfer=0.6; cost_per_sku=180_000; n=8
lost=tail_sales*(1-transfer)*cm; saved=cost_per_sku*n; print("kaybedilen katkı",tl(lost,0),"tasarruf",tl(saved,0),"net",tl(saved-lost,0))
for tr in (0.3,): print("transfer %30 net",tl(saved-tail_sales*(1-tr)*cm,0))
print("== 4-7 ==")
H=20_000_000; aw=0.40; dist=0.60; trial=0.20; rep=0.35; trial_units=1; rep_units=4
triers=H*aw*dist*trial; repeaters=triers*rep; vol=triers*trial_units+repeaters*rep_units
print("deneyen",tl(triers,0),"tekrarlayan",tl(repeaters,0),"yıl1 adet",tl(vol,0),"deneme payı",pct(triers/vol,1))
dist2=0.45; t2=H*aw*dist2*trial; v2=t2*(1+rep*rep_units); print("dağıtım %45",tl(v2,0))
print("== 5-1 ==")
p0,p1,q0,q1,c=20.0,22.0,1000,920,14.0
e=((q1-q0)/((q1+q0)/2))/((p1-p0)/((p1+p0)/2)); print("ark esneklik",tl(e))
print("gelir",tl(p0*q0,0),tl(p1*q1,0),"katkı",tl((p0-c)*q0,0),tl((p1-c)*q1,0))
# break-even volume loss for +10% price
print("katkı eşit kalması için izin verilen hacim kaybı",pct(1-(p0-c)/(p1-c)))
print("== 5-3 ==")
for g,p in ((500,45.0),(1000,82.0),(2000,150.0)): print(g,"g",tl(p),"kg fiyatı",tl(p/g*1000))
print("1kg->900g aynı fiyat kg artışı",pct(82/0.9/82-1))
