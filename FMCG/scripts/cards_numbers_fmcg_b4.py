#!/usr/bin/env python3
"""FMCG kartları, parti 4: örnek rakamlar (temsili)."""
import math
def tl(x,d=2): s=f"{x:,.{d}f}"; return s.replace(',','X').replace('.',',').replace('X','.')
def pct(x,d=2): return '%'+tl(x*100,d)
S=60e6; gm=0.09; sup=0.012
opex={"Personel":2.4e6,"Araç ve yakıt":1.1e6,"Depo":0.6e6,"Şüpheli alacak":0.3e6,"Diğer":0.4e6}
print("== 7-1 ==")
g=S*gm; s=S*sup; o=sum(opex.values()); ebit=g+s-o
print("brüt",tl(g,0),"destek",tl(s,0),"gider",tl(o,0),"FVÖK",tl(ebit,0),pct(ebit/S))
print("== 7-2 ==")
cogs=S*(1-gm); rec=S*45/365; inv=cogs*20/365; pay=cogs*30/365; fixed=2e6
ce=rec+inv-pay+fixed
print("alacak",tl(rec,0),"stok",tl(inv,0),"borç",tl(pay,0),"duran",tl(fixed,0),"sermaye",tl(ce,0),"ROCE",pct(ebit/ce,1))
coc=0.35; print("sermaye maliyeti",tl(ce*coc,0),"ekonomik kâr",tl(ebit-ce*coc,0))
rec2=S*30/365; ce2=rec2+inv-pay+fixed; print("vade 30 gün sermaye",tl(ce2,0),"ROCE",pct(ebit/ce2,1))
print("== 7-3 ==")
dso=45; dso2=35; fr=S*(dso-dso2)/365; print("serbest kalan",tl(fr,0),"aylık %3 finansman tasarrufu yıllık",tl(fr*((1.03)**12-1),0))
print("DSO formül alacak",tl(rec,0),"/ satış *365 =",tl(rec/S*365,1))
aging=[("0–30 gün",4.2e6,0.0),("31–60 gün",2.0e6,0.02),("61–90 gün",0.8e6,0.10),("90+ gün",0.4e6,0.50)]
print("toplam",tl(sum(a[1] for a in aging),0),"karşılık",tl(sum(a[1]*a[2] for a in aging),0))
print("== 7-4 ==")
w={"Kapsama":0.30,"Finansal güç":0.25,"Lojistik":0.20,"Yönetim":0.15,"Uyum":0.10}
c={"A":(4,3,4,3,5),"B":(3,5,3,4,3),"C":(5,2,4,4,2)}
for k,v in c.items(): print(k,tl(sum(x*y for x,y in zip(w.values(),v)),2))
print("== 7-5 ==")
o1,o2=1800,2200; aov=1500*12; print("ek satış yıl",tl((o2-o1)*aov,0),"distribütör brüt",tl((o2-o1)*aov*gm,0))
print("== 8-1 ==")
rep=45_000; vis=176; tel=30_000; calls=600
print("ziyaret başı",tl(rep/vis),"telefon başı",tl(tel/calls))
for n,cost,cnt,sr,ov in (("Ön satış",rep,vis,0.70,2500),("Telefonla satış",tel,calls,0.35,1200)):
    orders=cnt*sr; print(n,"sipariş",tl(orders,0),"sipariş başı maliyet",tl(cost/orders),"maliyet/satış",pct(cost/(orders*ov)))
print("== 8-2 / 8-3 ==")
def sales(v,sr,l,lv): return v*sr*l*lv
b=sales(176,0.60,4,600); n=sales(176,0.70,5,600)
print("aylık satış",tl(b,0),"->",tl(n,0),"artış",pct(n/b-1,1))
print("yalnız strike",tl(sales(176,0.70,4,600),0),"yalnız kalem",tl(sales(176,0.60,5,600),0))
print("== 8-4 ==")
inc=800_000*0.30; cost=540_000; print("marjinal katkı",tl(inc,0),"maliyet",tl(cost,0),"fark",tl(inc-cost,0))
inc2=2_200_000*0.30; print("A bölge ek satış 2,2M katkı",tl(inc2,0),"fark",tl(inc2-cost,0))
print("== 8-5 ==")
avail=7*60
for st,tr in ((20,15),(20,10)): print("servis",st,"yol",tr,"ziyaret/gün",avail//(st+tr),"aylık",avail//(st+tr)*22)
print("== 8-6 ==")
for sp in (8,12): n=math.ceil(46/sp); print("kontrol aralığı",sp,"şef",n,"maliyet",tl(n*900_000,0))
print("şef başı temsilci 46/6",tl(46/6,1),"46/4",tl(46/4,1))
print("== 8-7 ==")
k=[("Satış hedef gerçekleşme",0.40,1.05),("Sayısal dağıtım hedefi",0.25,0.92),("Tahsilat",0.20,0.98),("Mükemmel mağaza puanı",0.15,1.10)]
sc=sum(wt*min(v,1.2) for _,wt,v in k); print("ağırlıklı skor",pct(sc,1))
