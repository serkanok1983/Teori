#!/usr/bin/env python3
"""ECO kartları, 4. parti (b4): örneklerdeki tüm rakamlar. Çıktı: cards_numbers_eco_b4.out
Tüm rakamlar temsilidir; vergi oranları örnek orandır, güncel mevzuat oranı değildir."""
OUT=[]
def tr(x,d=0):
    s=f"{x:,.{d}f}"; return s.replace(",","X").replace(".",",").replace("X",".")
def pct(x,d=1): return ("−%" if x<0 else "%")+tr(abs(x)*100,d)
def money(x): return ("-" if x<0 else "")+tr(abs(x))
def put(k,v): OUT.append(f"{k} = {v}")

# 32-3 stres testi
c="st"; eq=40_000_000; usd=1_000_000; e0=34; e1=e0*1.4; ar=60_000_000; inv=30_000_000; debt=50_000_000
l_fx=usd*(e1-e0); l_ar=ar*0.10; l_inv=inv*0.10; l_int=debt*0.10
tot=l_fx+l_ar+l_inv+l_int
put(c+".eq",tr(eq)); put(c+".usd",tr(usd)); put(c+".e0",tr(e0)); put(c+".e1",tr(e1,1)); put(c+".ar",tr(ar)); put(c+".inv",tr(inv)); put(c+".debt",tr(debt))
put(c+".l_fx",tr(l_fx)); put(c+".l_ar",tr(l_ar)); put(c+".l_inv",tr(l_inv)); put(c+".l_int",tr(l_int)); put(c+".tot",tr(tot))
put(c+".eq1",tr(eq-tot)); put(c+".eqch",pct(-tot/eq,0))

# 32-4 yüksek enflasyonda finans
c="hi"; m=0.03; P=100
put(c+".m",pct(m,0)); put(c+".P",tr(P)); put(c+".pv60",tr(P/(1+m)**2,2)); put(c+".loss60",pct(1-1/(1+m)**2,2))
put(c+".pv90",tr(P/(1+m)**3,2)); put(c+".loss90",pct(1-1/(1+m)**3,2))
cost=80; rc=cost*(1+m)**2; mk=0.20; price=cost*(1+mk)
put(c+".cost",tr(cost)); put(c+".rc",tr(rc,2)); put(c+".mk",pct(mk,0)); put(c+".price",tr(price,2))
put(c+".m_hist",tr(price-cost,2)); put(c+".m_rep",tr(price-rc,2)); put(c+".mpct_hist",pct((price-cost)/price,1)); put(c+".mpct_rep",pct((price-rc)/price,1))
put(c+".price_rep",tr(rc*(1+mk),2))

# 33-2 çift taraflı kayıt
c="de"; net=100_000; kdv=0.20; cogs=70_000
put(c+".net",tr(net)); put(c+".kdv_r",pct(kdv,0)); put(c+".kdv",tr(net*kdv)); put(c+".brut",tr(net*(1+kdv))); put(c+".cogs",tr(cogs)); put(c+".gp",tr(net-cogs))

# 33-3 tahakkuk ve dönem sonu
c="ac"; rent=1_200_000; bonus=600_000; prem=300_000
put(c+".rent",tr(rent)); put(c+".rent_m",tr(rent/12)); put(c+".bonus",tr(bonus)); put(c+".bonus_m",tr(bonus/12)); put(c+".prem",tr(prem))
base=2_000_000; put(c+".base",tr(base)); put(c+".wrong_jan",money(base-rent)); put(c+".right_jan",tr(base-rent/12-bonus/12)); put(c+".wrong_dec",tr(base-bonus)); put(c+".right_dec",tr(base-rent/12-bonus/12+prem))

# 33-4 gelir tablosu
c="is"; gross=220_000_000; ded=20_000_000; ns=gross-ded; cg=164_000_000; gp=ns-cg; opex=26_000_000; ebit=gp-opex; fin=6_000_000; ebt=ebit-fin; t=0.25; tax=ebt*t; ni=ebt-tax; dep=2_000_000
for k,v in dict(gross=gross,ded=ded,ns=ns,cg=cg,gp=gp,opex=opex,ebit=ebit,fin=fin,ebt=ebt,tax=tax,ni=ni,dep=dep,ebitda=ebit+dep).items(): put(f"{c}.{k}",tr(v))
put(c+".t",pct(t,0)); put(c+".gm",pct(gp/ns,0)); put(c+".em",pct(ebit/ns,0)); put(c+".nm",pct(ni/ns,1))

# 33-5 bilanço
c="bs"; cash=5e6; ar=40e6; inv=25e6; fa=20e6; ap=30e6; sl=20e6; ll=10e6
ta=cash+ar+inv+fa; eq=ta-ap-sl-ll
for k,v in dict(cash=cash,ar=ar,inv=inv,fa=fa,ta=ta,ap=ap,sl=sl,ll=ll,eq=eq,ca=cash+ar+inv,cl=ap+sl,nd=sl+ll-cash,nwc=ar+inv-ap).items(): put(f"{c}.{k}",tr(v))
put(c+".cr",tr((cash+ar+inv)/(ap+sl),2)); put(c+".qr",tr((cash+ar)/(ap+sl),2)); put(c+".de",tr((sl+ll)/eq,2))

# 33-6 nakit akış tablosu
c="cf"; ni=3e6; dep=2e6; dar=-6e6; dinv=-4e6; dap=3e6; capex=-3e6; loan=6e6; div=-1e6
cfo=ni+dep+dar+dinv+dap; cfi=capex; cff=loan+div
for k,v in dict(ni=ni,dep=dep,dar=dar,dinv=dinv,dap=dap,cfo=cfo,capex=capex,loan=loan,div=div,cff=cff,cfi=cfi,net=cfo+cfi+cff).items(): put(f"{c}.{k}",money(v))

# 33-7 faaliyet raporu okuma
c="ar"; rg=0.40; inf=0.45; arg=0.70; dso0=60
put(c+".rg",pct(rg,0)); put(c+".inf",pct(inf,0)); put(c+".real",pct((1+rg)/(1+inf)-1,1)); put(c+".arg",pct(arg,0))
put(c+".dso0",str(dso0)); put(c+".dso1",tr(dso0*(1+arg)/(1+rg),1))
s0=100e6; put(c+".s0",tr(s0)); put(c+".s1",tr(s0*(1+rg))); put(c+".ar0",tr(s0*dso0/365)); put(c+".ar1",tr(s0*dso0/365*(1+arg)))

# 34-1 stok değerleme
c="iv"; q1,p1=1000,50; q2,p2=1000,60; sold=1000; sp=80
fifo=q1*p1; avg=(q1*p1+q2*p2)/(q1+q2)*sold
put(c+".q1",tr(q1)); put(c+".p1",tr(p1)); put(c+".q2",tr(q2)); put(c+".p2",tr(p2)); put(c+".sold",tr(sold)); put(c+".sp",tr(sp))
put(c+".rev",tr(sold*sp)); put(c+".fifo",tr(fifo)); put(c+".avg",tr(avg)); put(c+".gp_fifo",tr(sold*sp-fifo)); put(c+".gp_avg",tr(sold*sp-avg))
put(c+".end_fifo",tr(q2*p2)); put(c+".end_avg",tr((q1*p1+q2*p2)-avg)); put(c+".unit_avg",tr((q1*p1+q2*p2)/(q1+q2)))
put(c+".nrv_q",tr(200)); put(c+".nrv",tr(45)); put(c+".wd",tr(200*(60-45)))

# 34-2 şüpheli alacak - yaşlandırma
c="dd"; b=[("0_30",30e6,0.01),("31_60",10e6,0.03),("61_90",5e6,0.10),("90p",3e6,0.40),("dava",1e6,1.0)]
tot=0; s=0
for k,a,r in b:
    put(f"{c}.a_{k}",tr(a)); put(f"{c}.r_{k}",pct(r,0)); put(f"{c}.p_{k}",tr(a*r)); tot+=a*r; s+=a
put(c+".s",tr(s)); put(c+".tot",tr(tot)); put(c+".ratio",pct(tot/s,1))

# 34-3 duran varlık ve amortisman
c="fa"; cost=3_000_000; n=5
put(c+".cost",tr(cost)); put(c+".n",str(n)); put(c+".sl",tr(cost/n))
bv=cost; r=2/n; put(c+".r",pct(r,0))
for y in range(1,4):
    d=bv*r; put(f"{c}.db{y}",tr(d)); bv-=d
put(c+".infl",pct(0.30,0)); put(c+".repl",tr(cost*1.3**n)); put(c+".gap",tr(cost*1.3**n-cost))

# 34-5 TFRS 16 kiralama
c="ls"; pmt=100_000; n=36; i=0.03
pv=pmt*(1-(1+i)**-n)/i
put(c+".pmt",tr(pmt)); put(c+".n",str(n)); put(c+".i",pct(i,0)); put(c+".pv",tr(pv)); put(c+".dep",tr(pv/n)); put(c+".int1",tr(pv*i))
put(c+".tot1",tr(pv/n+pv*i)); put(c+".diff1",tr(pv/n+pv*i-pmt)); put(c+".total",tr(pmt*n)); put(c+".tot_int",tr(pmt*n-pv))
put(c+".ebitda_yil",tr(pmt*12))

open(__file__.replace(".py",".out"),"w").write("\n".join(OUT)+"\n")
print("\n".join(OUT))
