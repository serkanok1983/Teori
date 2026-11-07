#!/usr/bin/env python3
"""FMCG kartları, parti 1: örnek rakamlar (temsili). Çalıştır: python3 cards_numbers_fmcg_b1.py > cards_numbers_fmcg_b1.out"""
import datetime as dt
def tl(x,d=2): s=f"{x:,.{d}f}"; return s.replace(',','X').replace('.',',').replace('X','.')
def pct(x,d=2): return '%'+tl(x*100,d)
print("== kb-fmcg-1-1-margin-stack ==")
gp=4.09; case=12; drop=350
for cs in (40,10):
    u=cs*case; g=u*gp; print(f"{cs} koli={u} adet brüt kâr {tl(g)} TL, teslimat sonrası {tl(g-drop)} TL")
print("oran", tl((40*case*gp-drop)/(10*case*gp-drop),1))
print("başabaş koli (teslimat maliyetini karşılayan):", tl(drop/(case*gp),2))
a,b,c=1000,20,10
P=(a+b*c)/(2*b); q=a-b*P; print("entegre P",tl(P),"q",q,"kâr",tl((P-c)*q))
w=(a+b*c)/(2*b); P2=(a+b*w)/(2*b); q2=a-b*P2; print("ayrı w",tl(w),"P",tl(P2),"q",q2,"perakendeci",tl((P2-w)*q2),"üretici",tl((w-c)*q2),"toplam",tl((P2-w)*q2+(w-c)*q2))
print("== kb-fmcg-1-2-scale-and-concentration ==")
F=12_000_000; v=18
for Q in (1_000_000,2_000_000,4_000_000): print(f"Q={tl(Q,0)} birim maliyet {tl(v+F/Q)}")
sh=[30,20,15,10,8,7,5,5]; print("toplam",sum(sh),"CR4",sum(sh[:4]),"HHI",sum(s*s for s in sh))
sh2=[30+15,20,10,8,7,5,5]; print("1 ve 3 birleşirse HHI",sum(s*s for s in sh2),"artış",sum(s*s for s in sh2)-sum(s*s for s in sh))
print("== kb-fmcg-1-3-channel-actors ==")
M,R=5,200; print("doğrudan temas",M*R,"bayi üzerinden",M+R)
print("== kb-fmcg-1-4-channel-power-conflict ==")
S=40_000_000; cm=0.30; print("zincire satış",tl(S,0),"katkı",tl(S*cm,0))
for rec in (0,0.4): print(f"listeden çıkma, geri kazanım {pct(rec,0)}: kayıp katkı {tl(S*cm*(1-rec),0)}")
print("ek %2 iskonto maliyeti",tl(S*0.02,0))
print("== kb-fmcg-1-5-turkish-fmcg-landscape ==")
d=dt.date(2026,11,2)
for n in (30,45,60): print(n,"gün ->",(d+dt.timedelta(days=n)).isoformat())
print("== kb-fmcg-2-1-fmcg-pnl ==")
gs=100_000_000; ts=0.18*gs; ns=gs-ts; cogs=0.58*ns; gp1=ns-cogs; varsell=0.09*ns; cont=gp1-varsell; fixed=14_000_000; ebit=cont-fixed
for k,x in [("brüt satış",gs),("ticari indirim/destek",ts),("net satış",ns),("SMM",cogs),("brüt kâr",gp1),("değişken satış-dağıtım",varsell),("katkı",cont),("sabit gider",fixed),("FVÖK",ebit)]: print(k,tl(x,0),pct(x/ns,1) if k!="brüt satış" else "")
print("== kb-fmcg-2-2-gross-to-net ==")
L=100.0; oninv=0.08; inv=L*(1-oninv); ciro=0.03*inv; promo_per_unit=2.50; vol=120_000; listing=180_000; lf=listing/vol
net=inv-ciro-promo_per_unit-lf
print("liste",tl(L),"fatura altı",tl(L*oninv),"fatura",tl(inv),"ciro primi",tl(ciro),"promosyon",tl(promo_per_unit),"listeleme/adet",tl(lf),"cep net",tl(net),"G2N",pct(1-net/L))
print("== kb-fmcg-2-3-contribution-breakeven ==")
p,vc,F=30.0,21.0,450_000; cmu=p-vc; be=F/cmu; print("KM",tl(cmu),"KM oranı",pct(cmu/p),"başabaş",tl(be,0),"ciro",tl(be*p,0))
Q=60_000; prof=cmu*Q-F; print("60.000 adet kâr",tl(prof,0),"FKD",tl(cmu*Q/prof,2))
Q2=Q*1.10; prof2=cmu*Q2-F; print("+%10 hacim kâr",tl(prof2,0),"değişim",pct(prof2/prof-1))
p3=p*0.95; cm3=p3-vc; print("%5 indirimde KM",tl(cm3),"aynı kâr için hacim",tl((cmu*Q)/cm3,0),"artış",pct((cmu*Q)/cm3/Q-1))
print("== kb-fmcg-2-4-roi-roce-npv ==")
I=25_000; cases=20; cmc=60; maint=150; months=12
cf=(cases*cmc-maint)*months; r=0.35; n=5
npv=-I+sum(cf/(1+r)**t for t in range(1,n+1)); print("yıllık nakit",tl(cf,0),"geri ödeme yıl",tl(I/cf,2),"NBD",tl(npv,0))
for c2 in (10,):
    cf2=(c2*cmc-maint)*12; npv2=-I+sum(cf2/(1+r)**t for t in range(1,n+1)); print("10 koli: nakit",tl(cf2,0),"geri ödeme",tl(I/cf2,2),"NBD",tl(npv2,0))
roi=(cf*n-I)/I; print("basit ROI 5 yıl",pct(roi))
ebit_d=3_600_000; cap=18_000_000; print("ROCE",pct(ebit_d/cap))
print("== kb-fmcg-2-6-price-volume-mix-variance ==")
B={'A':(10000,50.0,30.0),'B':(10000,30.0,22.0)}  # adet, fiyat, maliyet
Aa={'A':(8000,52.0,30.0),'B':(14000,30.0,22.0)}
def tot(D): return sum(q*(p-c) for q,p,c in D.values())
bq=sum(v[0] for v in B.values()); aq=sum(v[0] for v in Aa.values())
bavg=tot(B)/bq
vol=(aq-bq)*bavg
mix=sum((Aa[k][0]-aq*B[k][0]/bq)*(B[k][1]-B[k][2]) for k in B)
price=sum(Aa[k][0]*(Aa[k][1]-B[k][1]) for k in B)
cost=-sum(Aa[k][0]*(Aa[k][2]-B[k][2]) for k in B)
print("bütçe katkı",tl(tot(B),0),"gerçek",tl(tot(Aa),0),"fark",tl(tot(Aa)-tot(B),0))
print("ort birim katkı",tl(bavg),"hacim",tl(vol,0),"karma",tl(mix,0),"fiyat",tl(price,0),"maliyet",tl(cost,0),"toplam",tl(vol+mix+price+cost,0))
print("== kb-fmcg-3-1-consumer-decisions ==")
shop=1000; oos=0.08; sw=0.40; print("rafta bulamayan",shop*oos,"rakibe geçen",shop*oos*sw)
print("== kb-fmcg-3-2-repeat-buying-patterns ==")
hh=10000
for nm,pen,fr in (("A",0.40,3.0),("B",0.10,2.4)): print(nm,"alıcı",int(hh*pen),"alım",tl(hh*pen*fr,0))
base=hh*0.10*2.4; print("B +%20 penetrasyon",tl(hh*0.12*2.4,0),"B +%20 sıklık",tl(hh*0.10*2.88,0))
print("pazar payı A",pct(hh*.4*3/(hh*.4*3+hh*.1*2.4),1))
