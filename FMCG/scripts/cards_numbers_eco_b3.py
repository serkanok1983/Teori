#!/usr/bin/env python3
"""ECO kartları, 3. parti (b3): örneklerdeki tüm rakamlar. Çıktı: cards_numbers_eco_b3.out
Tüm rakamlar temsilidir; gerçek faiz, kur, vergi veya piyasa verisi değildir."""
OUT=[]
def tr(x,d=0):
    s=f"{x:,.{d}f}"; return s.replace(",","X").replace(".",",").replace("X",".")
def pct(x,d=1): return ("−%" if x<0 else "%")+tr(abs(x)*100,d)
def money(x): return ("-" if x<0 else "")+tr(abs(x))
def put(k,v): OUT.append(f"{k} = {v}")
def npv(r,cfs): return sum(cf/(1+r)**t for t,cf in enumerate(cfs))
def irr(cfs,lo=-0.9,hi=5.0):
    for _ in range(200):
        m=(lo+hi)/2
        if npv(m,cfs)>0: lo=m
        else: hi=m
    return m

# 25-1 NPV / IRR
c="tv"; I=10_000_000; A=[3_500_000]*5; r=0.25
cfs=[-I]+A; put(c+".I",tr(I)); put(c+".A",tr(A[0])); put(c+".r",pct(r,0))
for t in range(1,6): put(f"{c}.pv{t}",tr(A[0]/(1+r)**t))
put(c+".pvsum",tr(npv(r,[0]+A))); put(c+".npv",money(npv(r,cfs))); put(c+".irr",pct(irr(cfs),1))
put(c+".npv35",money(npv(0.35,cfs)))
put(c+".topnakit",tr(sum(A)))

# 25-2 krediler: TL vs döviz, reel maliyet, eşit taksit
c="ln"; itl=0.50; iusd=0.09; dep=0.35; inf=0.35
put(c+".itl",pct(itl,0)); put(c+".iusd",pct(iusd,0)); put(c+".dep",pct(dep,0))
eff=(1+iusd)*(1+dep)-1; put(c+".eff_usd",pct(eff,2))
put(c+".be_dep",pct((1+itl)/(1+iusd)-1,1))
put(c+".inf",pct(inf,0)); put(c+".reel_tl",pct((1+itl)/(1+inf)-1,2)); put(c+".reel_usd",pct((1+eff)/(1+inf)-1,2))
P=10_000_000; m=0.035; n=12; pay=P*m/(1-(1+m)**-n)
put(c+".P",tr(P)); put(c+".m",pct(m,1)); put(c+".n",str(n)); put(c+".taksit",tr(pay)); put(c+".topode",tr(pay*n)); put(c+".topfaiz",tr(pay*n-P))
put(c+".yillik_bilesik",pct((1+m)**12-1,1)); put(c+".yillik_basit",pct(m*12,0))

# 25-6 tahvil/bono
c="bd"; F=100; p=80; put(c+".F",tr(F)); put(c+".p",tr(p)); put(c+".y",pct(F/p-1,0))
cpn=0.30
def bprice(y): return sum(cpn*F/(1+y)**t for t in (1,2))+F/(1+y)**2
for y,k in ((0.30,"a"),(0.35,"b"),(0.25,"c")):
    put(f"{c}.y_{k}",pct(y,0)); put(f"{c}.pr_{k}",tr(bprice(y),2)); put(f"{c}.ch_{k}",pct(bprice(y)/bprice(0.30)-1,1))
put(c+".kupon",pct(cpn,0))
# 3 aylık bono: 1 yıllık eşdeğer
p3=92; put(c+".p3",tr(p3)); put(c+".d3",pct(F/p3-1,2)); put(c+".y3",pct((F/p3)**4-1,1))

# 26-4 değerleme: çarpan ve İNA
c="va"; ebitda=40_000_000; mult=5; nd=60_000_000
put(c+".ebitda",tr(ebitda)); put(c+".mult",tr(mult)); put(c+".ev",tr(ebitda*mult)); put(c+".nd",tr(nd)); put(c+".eq",tr(ebitda*mult-nd))
for mm,k in ((4,"lo"),(6,"hi")): put(f"{c}.mult_{k}",tr(mm)); put(f"{c}.eq_{k}",tr(ebitda*mm-nd)); put(f"{c}.eqch_{k}",pct((ebitda*mm-nd)/(ebitda*mult-nd)-1,0))
fcf=25_000_000; wacc=0.30; g=0.20
put(c+".fcf",tr(fcf)); put(c+".wacc",pct(wacc,0)); put(c+".g",pct(g,0)); put(c+".tv",tr(fcf/(wacc-g)))
put(c+".g2",pct(0.18,0)); put(c+".tv2",tr(fcf/(wacc-0.18))); put(c+".tvch",pct((fcf/(wacc-0.18))/(fcf/(wacc-g))-1,1))

# 30-1 vadeli kur (forward)
c="fw"; S=34.0; itl=0.45; iusd=0.05; d=90; amt=500_000
Fw=S*(1+itl*d/360)/(1+iusd*d/360)
put(c+".S",tr(S,2)); put(c+".itl",pct(itl,0)); put(c+".iusd",pct(iusd,0)); put(c+".d",str(d)); put(c+".F",tr(Fw,2))
put(c+".prim",pct(Fw/S-1,2)); put(c+".amt",tr(amt)); put(c+".tl_f",tr(amt*Fw))
for s,k in ((32.0,"lo"),(40.0,"hi")):
    put(f"{c}.s_{k}",tr(s,2)); put(f"{c}.tl_{k}",tr(amt*s)); put(f"{c}.diff_{k}",money(amt*s-amt*Fw))

# 31-1 yatırım bütçeleme: depo otomasyonu
c="cb"; I=15_000_000; s=6_000_000; r=0.30; n=5
cfs=[-I]+[s]*n; put(c+".I",tr(I)); put(c+".s",tr(s)); put(c+".r",pct(r,0)); put(c+".n",str(n))
put(c+".npv",money(npv(r,cfs))); put(c+".irr",pct(irr(cfs),1)); put(c+".payback",tr(I/s,1))
# tasarruf enflasyonla artarsa (%25/yıl)
cf2=[-I]+[s*1.25**t for t in range(n)]; put(c+".gs",pct(0.25,0)); put(c+".npv2",money(npv(r,cf2))); put(c+".irr2",pct(irr(cf2),1))
# 3 yıl ömür
cf3=[-I]+[s]*3; put(c+".npv3",money(npv(r,cf3)))

# 31-2 sermaye maliyeti (AOSM)
c="wc"; we=0.6; wd=0.4; ke=0.45; kd=0.48; t=0.25
kd_a=kd*(1-t); w=we*ke+wd*kd_a
put(c+".we",pct(we,0)); put(c+".wd",pct(wd,0)); put(c+".ke",pct(ke,0)); put(c+".kd",pct(kd,0)); put(c+".t",pct(t,0))
put(c+".kd_a",pct(kd_a,0)); put(c+".wacc",pct(w,1)); put(c+".roic",pct(0.35,0)); put(c+".spread",tr((0.35-w)*100,1))
put(c+".ic",tr(80_000_000)); put(c+".ek_deger",money(80_000_000*(0.35-w)))

# 31-4 borç mu özkaynak mı
c="lv"; A=100_000_000; ebit=30_000_000; t=0.25
roe0=ebit*(1-t)/A; put(c+".A",tr(A)); put(c+".ebit",tr(ebit)); put(c+".t",pct(t,0)); put(c+".roa",pct(ebit/A,0)); put(c+".roe0",pct(roe0,1))
D=50_000_000; E=A-D
for i,k in ((0.40,"a"),(0.20,"b")):
    intr=D*i; ni=(ebit-intr)*(1-t); put(f"{c}.i_{k}",pct(i,0)); put(f"{c}.int_{k}",tr(intr)); put(f"{c}.ni_{k}",tr(ni)); put(f"{c}.roe_{k}",pct(ni/E,1))
put(c+".D",tr(D)); put(c+".E",tr(E))
# FAVÖK düşerse (ebit 15M), i=40%
ni=(15_000_000-D*0.40)*(1-t) if 15_000_000-D*0.40>0 else (15_000_000-D*0.40)
put(c+".ebit_lo",tr(15_000_000)); put(c+".ni_lo",money(ni)); put(c+".ni_lo_abs",tr(abs(ni))); put(c+".icr_lo",tr(15_000_000/(D*0.40),2)); put(c+".icr_a",tr(ebit/(D*0.40),2))

# 31-5 aile şirketi: ilişkili taraf alımı
c="ag"; buy=20_000_000; prem=0.10; minority=0.40
put(c+".alim",tr(buy)); put(c+".prim",pct(prem,0)); put(c+".kayip",tr(buy*prem)); put(c+".azinlik",pct(minority,0)); put(c+".azinlik_kayip",tr(buy*prem*minority))

# 31-8 birleşme/satın alma
c="ma"; sa=50_000_000; syn=3_000_000; r=0.30; integ=5_000_000; price=60_000_000
pv_syn=syn/r; maxp=sa+pv_syn-integ
put(c+".sa",tr(sa)); put(c+".syn",tr(syn)); put(c+".r",pct(r,0)); put(c+".pv_syn",tr(pv_syn)); put(c+".integ",tr(integ))
put(c+".maxp",tr(maxp)); put(c+".price",tr(price)); put(c+".kayip",tr(price-maxp))
put(c+".ebitda",tr(10_000_000)); put(c+".mult_price",tr(price/10_000_000,1))
# sinerji yarısı gerçekleşirse
put(c+".maxp_half",tr(sa+pv_syn/2-integ))

# 31-9 üç tablo modeli
c="ts"; ni=8_000_000; dep=2_000_000; dar=10_000_000; dinv=5_000_000; dap=3_000_000; capex=4_000_000
cfo=ni+dep-dar-dinv+dap
put(c+".ni",tr(ni)); put(c+".dep",tr(dep)); put(c+".dar",tr(dar)); put(c+".dinv",tr(dinv)); put(c+".dap",tr(dap))
put(c+".cfo",money(cfo)); put(c+".capex",tr(capex)); put(c+".fcf",money(cfo-capex)); put(c+".fcf_abs",tr(abs(cfo-capex)))
put(c+".s0",tr(100_000_000)); put(c+".s1",tr(125_000_000)); put(c+".gr",pct(0.25,0))

# 31-10 senaryo ve duyarlılık
c="sc"; S=200_000_000; gm=0.20; fx=30_000_000
base=S*gm-fx; put(c+".S",tr(S)); put(c+".gm",pct(gm,0)); put(c+".fx",tr(fx)); put(c+".base",tr(base))
v=S*0.9*gm-fx; put(c+".vol",money(v)); put(c+".vol_ch",pct(v/base-1,0))
p=S*0.97-S*(1-gm)-fx; put(c+".price",money(p)); put(c+".price_ch",pct(p/base-1,0))
k=S-S*(1-gm)*1.05-fx; put(c+".cost",money(k)); put(c+".cost_ch",pct(k/base-1,0))
f=base-fx*0.10; put(c+".fix",money(f)); put(c+".fix_ch",pct(f/base-1,0))
worst=S*0.9*0.97-S*0.9*(1-gm)*1.05-fx*1.10; put(c+".worst",money(worst))

open(__file__.replace(".py",".out"),"w").write("\n".join(OUT)+"\n")
print("\n".join(OUT))
