#!/usr/bin/env python3
"""ECO kartları, 5. parti (b5): örneklerdeki tüm rakamlar. Çıktı: cards_numbers_eco_b5.out
Tüm rakamlar temsilidir; vergi ve yasal tutarlar örnek niteliğindedir, güncel mevzuat değeri değildir."""
OUT=[]
def tr(x,d=0):
    s=f"{x:,.{d}f}"; return s.replace(",","X").replace(".",",").replace("X",".")
def pct(x,d=1): return ("−%" if x<0 else "%")+tr(abs(x)*100,d)
def put(k,v): OUT.append(f"{k} = {v}")

# 34-7 karşılıklar ve kıdem tazminatı
c="kv"; n=40; w0=40_000; ten=6; wg=0.40
l0=n*w0*ten; w1=w0*(1+wg); l1=n*w1*(ten+1)
put(c+".n",tr(n)); put(c+".w0",tr(w0)); put(c+".ten",tr(ten)); put(c+".wg",pct(wg,0)); put(c+".w1",tr(w1))
put(c+".l0",tr(l0)); put(c+".l1",tr(l1)); put(c+".dl",tr(l1-l0)); put(c+".dl_m",tr((l1-l0)/12))
put(c+".case",tr(2_000_000))

# 34-8 kur farkı
c="fx"; usd=100_000; e0=34; e1=35; e2=36
put(c+".usd",tr(usd)); put(c+".e0",tr(e0)); put(c+".e1",tr(e1)); put(c+".e2",tr(e2))
put(c+".b0",tr(usd*e0)); put(c+".d1",tr(usd*(e1-e0))); put(c+".d2",tr(usd*(e2-e1))); put(c+".tot",tr(usd*(e2-e0))); put(c+".paid",tr(usd*e2))
gm=0.12; sale=usd*e0*(1+gm); put(c+".gm",pct(gm,0)); put(c+".sale",tr(sale)); put(c+".gp",tr(sale-usd*e0)); put(c+".gp_net",tr(sale-usd*e2))

# 35-1 raporlama rejimleri (aynı şirket, iki çerçeve)
c="rr"; p=10_000_000; kd=1_500_000; ecl=800_000
put(c+".p",tr(p)); put(c+".kd",tr(kd)); put(c+".ecl",tr(ecl)); put(c+".p2",tr(p-kd-ecl)); put(c+".ch",pct(-(kd+ecl)/p,0))

# 35-2 enflasyon muhasebesi
c="ia"; a=2_000_000; i0=100; i1=180; cash=5_000_000; inf=0.50
put(c+".a",tr(a)); put(c+".i0",tr(i0)); put(c+".i1",tr(i1)); put(c+".a1",tr(a*i1/i0)); put(c+".coef",tr(i1/i0,2))
put(c+".cash",tr(cash)); put(c+".inf",pct(inf,0)); put(c+".mloss",tr(cash*inf/(1+inf))); put(c+".mloss_simple",tr(cash*inf)); put(c+".cash_req",tr(cash*(1+inf)))

# 36-4 oranlar
c="rt"; ns=200e6; ebit=10e6; ni=3e6; ta=90e6; eq=30e6; debt=30e6; cash=5e6; fin=6e6; ebitda=12e6; inf=0.45
ce=eq+debt
put(c+".roa",pct(ni/ta,1)); put(c+".roe",pct(ni/eq,1)); put(c+".roce",pct(ebit/ce,1)); put(c+".ce",tr(ce))
put(c+".icr",tr(ebit/fin,2)); put(c+".nd_ebitda",tr((debt-cash)/ebitda,2)); put(c+".nd",tr(debt-cash)); put(c+".inf",pct(inf,0))
put(c+".roe_real",pct((1+ni/eq)/(1+inf)-1,1)); put(c+".em",pct(ebit/ns,0))

# 36-5 DuPont
c="dp"
for p_,nm,ns_,ta_,eq_ in (("a",0.015,200e6,90e6,30e6),("b",0.03,120e6,100e6,50e6)):
    ni_=nm*ns_; at=ns_/ta_; lev=ta_/eq_
    put(f"{c}.{p_}_nm",pct(nm,1)); put(f"{c}.{p_}_ns",tr(ns_)); put(f"{c}.{p_}_ta",tr(ta_)); put(f"{c}.{p_}_eq",tr(eq_)); put(f"{c}.{p_}_ni",tr(ni_))
    put(f"{c}.{p_}_at",tr(at,2)); put(f"{c}.{p_}_lev",tr(lev,2)); put(f"{c}.{p_}_roe",pct(nm*at*lev,1))

# 36-6 nakit ve kâr (büyüme)
c="cp"; s0=100e6; s1=150e6; cogs=0.85; dso=60; dio=45; dpo=30; nm=0.03
d_ar=(s1-s0)*dso/365; d_inv=(s1-s0)*cogs*dio/365; d_ap=(s1-s0)*cogs*dpo/365
ni=s1*nm; dnwc=d_ar+d_inv-d_ap
put(c+".s0",tr(s0)); put(c+".s1",tr(s1)); put(c+".dso",tr(dso)); put(c+".dio",tr(dio)); put(c+".dpo",tr(dpo)); put(c+".nm",pct(nm,0))
put(c+".ni",tr(ni)); put(c+".d_ar",tr(d_ar)); put(c+".d_inv",tr(d_inv)); put(c+".d_ap",tr(d_ap)); put(c+".dnwc",tr(dnwc)); put(c+".gap_abs",tr(abs(ni-dnwc)))

# 36-7 kâr kalitesi
c="eqr"; ni3=8e6; cfo3=-3e6; ta=100e6; dso0=55; dso1=80
put(c+".ni",tr(ni3)); put(c+".cfo_abs",tr(abs(cfo3))); put(c+".acc",tr(ni3-cfo3)); put(c+".ta",tr(ta)); put(c+".ratio",pct((ni3-cfo3)/ta,0))
put(c+".dso0",tr(dso0)); put(c+".dso1",tr(dso1))

# 37-3 müşteri kredi analizi
c="cc"; mon=2e6; term=60; ead=mon*term/30; pd=0.05; lgd=0.60; el=ead*pd*lgd; yr=mon*12; gm=0.08
put(c+".mon",tr(mon)); put(c+".term",tr(term)); put(c+".ead",tr(ead)); put(c+".pd",pct(pd,0)); put(c+".lgd",pct(lgd,0)); put(c+".el",tr(el))
put(c+".yr",tr(yr)); put(c+".gm",pct(gm,0)); put(c+".gp",tr(yr*gm)); put(c+".loss_if",tr(ead*lgd)); put(c+".months",tr(ead*lgd/(mon*gm),1))

# 37-4 Altman Z'' (imalat dışı / halka açık olmayan)
c="z"
def zpp(wc,re,ebit,eqbv,tl,ta): 
    x=[wc/ta,re/ta,ebit/ta,eqbv/tl]; return x,6.56*x[0]+3.26*x[1]+6.72*x[2]+1.05*x[3]
x,zv=zpp(20e6,15e6,10e6,30e6,60e6,90e6)
for i,v in enumerate(x): put(f"{c}.x{i+1}",tr(v,3))
put(c+".z",tr(zv,2))
x2,zv2=zpp(5e6,5e6,2e6,15e6,75e6,90e6)
for i,v in enumerate(x2): put(f"{c}.y{i+1}",tr(v,3))
put(c+".z2",tr(zv2,2))

# 38-1 distribütör tabloları: iki distribütör
c="df"
for p_,ns_,gp_,opex_,ar_,inv_,ap_,ce_ in (("a",200e6,36e6,26e6,40e6,25e6,30e6,60e6),("b",200e6,30e6,22e6,25e6,18e6,28e6,40e6)):
    cogs_=ns_-gp_; ebit_=gp_-opex_
    put(f"{c}.{p_}_gm",pct(gp_/ns_,1)); put(f"{c}.{p_}_ox",pct(opex_/ns_,1)); put(f"{c}.{p_}_em",pct(ebit_/ns_,1))
    put(f"{c}.{p_}_dso",tr(ar_/ns_*365)); put(f"{c}.{p_}_dio",tr(inv_/cogs_*365)); put(f"{c}.{p_}_dpo",tr(ap_/cogs_*365))
    put(f"{c}.{p_}_ccc",tr(ar_/ns_*365+inv_/cogs_*365-ap_/cogs_*365)); put(f"{c}.{p_}_roce",pct(ebit_/ce_,1))

# 38-3 DBS ve kredi riski
c="db"; lim=20e6; mon=15e6; term=45; need=mon*term/30
put(c+".lim",tr(lim)); put(c+".mon",tr(mon)); put(c+".term",tr(term)); put(c+".need",tr(need)); put(c+".gap",tr(need-lim))
put(c+".term2",tr(lim/mon*30))

open(__file__.replace(".py",".out"),"w",encoding="utf-8").write("\n".join(OUT)+"\n")
print("\n".join(OUT))
