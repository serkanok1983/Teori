#!/usr/bin/env python3
"""FMCG kartları, parti 3: örnek rakamlar (temsili)."""
import math
def tl(x,d=2): s=f"{x:,.{d}f}"; return s.replace(',','X').replace('.',',').replace('X','.')
def pct(x,d=2): return '%'+tl(x*100,d)
print("== 5-4 promosyon ==")
p,c,q=30.0,18.0,1000; disc=0.20; pp=p*(1-disc); qp=1800; dip=200
base=(p-c)*q; promo=(pp-c)*qp; dipc=(p-c)*dip
print("baz katkı",tl(base,0),"promo hafta katkı",tl(promo,0),"sonrası kayıp",tl(dipc,0),"net fark",tl(promo-dipc-base,0))
print("başabaş hacim",tl(base/(pp-c),0),"artış",pct(base/(pp-c)/q-1,0))
print("== 5-5 ticari harcama ==")
spend=150_000; inc=12_000; cu=15
print("ek katkı",tl(inc*cu,0),"ROI",pct((inc*cu-spend)/spend,0),"başabaş ek adet",tl(spend/cu,0))
inc2=8_000; print("ek 8000 ROI",pct((inc2*cu-spend)/spend,0))
print("== 5-6 enflasyon ==")
m=0.03; c0=100.0; mk=1.25
def avg_margin(period, months=12):
    tot=0; price=c0*mk
    for t in range(months):
        if t%period==0: price=c0*(1+m)**t*mk
        cost=c0*(1+m)**t; tot+=(price-cost)/price
    return tot/months
for per in (12,6,3,1): print("güncelleme her",per,"ay ort brüt marj",pct(avg_margin(per)))
print("aylık %3 yıllık",pct((1+m)**12-1))
nom=0.45; inf=0.50; print("reel büyüme",pct((1+nom)/(1+inf)-1))
print("== 5-7 RGM köprü ==")
items=[("Fiyat",8.0),("Karma",2.0),("Promosyon verimliliği",1.5),("Ticari koşullar",-0.5),("Hacim",-3.0)]
x=100.0
for n,v in items: x+=v; print(n,tl(v,1),"->",tl(x,1))
print("== 6-1 kanal ==")
ch=[("Ulusal zincir",0.35,0.22),("Yerel zincir",0.20,0.27),("Geleneksel kanal",0.30,0.31),("İndirim marketi",0.10,0.18),("E-ticaret",0.05,0.24)]
w=sum(s*g for _,s,g in ch); print("ağırlıklı brüt marj",pct(w,1))
for n,s,g in ch: print(n,pct(s,0),pct(g,0),"katkı puan",tl(s*g*100,2))
print("== 6-2 nokta evreni ==")
seg=[("A",500,4),("B",1500,2),("C",3000,1)]
v=sum(n*f for _,n,f in seg); cap=8*22
print("ziyaret/ay",tl(v,0),"temsilci kapasitesi",cap,"gereken",tl(v/cap,2),"->",math.ceil(v/cap))
v2=500*4+1500*2+3000*0.5; print("C 2 ayda 1 ->",tl(v2,0),math.ceil(v2/cap))
print("== 6-3 hizmet maliyeti ==")
drop=120.0
for n,o in (("Küçük bakkal",1500),("Büyük market",6000)): print(n,"sipariş",tl(o,0),"teslim maliyet oranı",pct(drop/o))
gm=0.20
for o in (1500,6000): print(o,"kalan",pct(gm-drop/o))
print("min sipariş %4 için",tl(drop/0.04,0))
print("== 6-4 doğrudan/dolaylı ==")
F=3_000_000; var=0.04; dm=0.10
print("başabaş satış",tl(F/(dm-var),0))
for S in (30e6,50e6,80e6): print(tl(S,0),"doğrudan",tl(F+var*S,0),"dağıtıcı",tl(dm*S,0))
print("== 6-5 toptan ==")
p0=100.0; ws=0.06; rt=0.18
w=p0*(1+ws); r=w*(1+rt); print("toptancı",tl(w),"bakkal raf (KDV hariç)",tl(r))
r2=p0*(1+0.20); print("doğrudan bakkal",tl(r2))
print("== 6-6 horeca ==")
mach=60_000; kg=20; cpk=150
print("aylık katkı",tl(kg*cpk,0),"geri ödeme ay",tl(mach/(kg*cpk),1))
print("12 kg geri ödeme",tl(mach/(12*cpk),1))
print("== 6-7 e-market ==")
for aov in (400,250):
    g=aov*0.25; cost=25+45+5+aov*0.015; print("sepet",aov,"brüt",tl(g),"maliyet",tl(cost),"katkı",tl(g-cost))
be=(25+45+5)/(0.25-0.015); print("başabaş sepet",tl(be))
print("== 6-8 vaka ==")
S=60e6; dist=S*0.09+1_200_000
direct=10*540_000+6*360_000+1_200_000+S*0.005
print("dağıtıcı",tl(dist,0),pct(dist/S),"doğrudan",tl(direct,0),pct(direct/S))
S2=66e6; direct2=10*540_000+6*360_000+1_200_000+S2*0.005; cm=0.30
print("doğrudan +%10 satış maliyet",tl(direct2,0),"ek katkı",tl((S2-S)*cm,0))
print("net doğrudan avantajı",tl((S2-S)*cm-(direct2-dist),0))
inv=4_000_000; print("ek işletme sermayesi (alacak+stok)",tl(inv,0))
