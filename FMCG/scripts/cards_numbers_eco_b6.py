#!/usr/bin/env python3
"""ECO kartları, 6. parti (b6): örneklerdeki tüm rakamlar. Çıktı: cards_numbers_eco_b6.out
Tüm rakamlar temsilidir; vergi oranları ve dilimleri örnek orandır, güncel mevzuat değeri değildir."""
OUT=[]
def tr(x,d=0):
    s=f"{x:,.{d}f}"; return s.replace(",","X").replace(".",",").replace("X",".")
def pct(x,d=1): return ("−%" if x<0 else "%")+tr(abs(x)*100,d)
def put(k,v): OUT.append(f"{k} = {v}")
def m(x): return ("-" if x<0 else "")+tr(abs(x))

# 55-1 vaka: yeni zincir müşteri kredi kararı
c="cs"; mon=3e6; gm=0.09; fr=0.035; pd=0.06; lgd=0.60; yr=mon*12; gp=yr*gm
put(c+".mon",tr(mon)); put(c+".gm",pct(gm,0)); put(c+".fr",pct(fr,1)); put(c+".pd",pct(pd,0)); put(c+".lgd",pct(lgd,0)); put(c+".yr",tr(yr)); put(c+".gp",tr(gp))
for k,term in (("t75",75),("t45",45)):
    ead=mon*term/30; fin=ead*fr*12; el=ead*pd*lgd; net=gp-fin-el
    put(f"{c}.{k}_ead",tr(ead)); put(f"{c}.{k}_fin",tr(fin)); put(f"{c}.{k}_el",tr(el)); put(f"{c}.{k}_net",m(net)); put(f"{c}.{k}_net_abs",tr(abs(net)))

# 39-2 ürün maliyeti: geleneksel ve faaliyet tabanlı dağıtım
c="pc"; oh=3e6; qa=100_000; qb=10_000
dma,dla,dmb,dlb=40,10,50,12; pa,pb=85,160
oha_t=oh*0.8/qa; ohb_t=oh*0.2/qb; oha_a=oh*0.5/qa; ohb_a=oh*0.5/qb
for k,v in dict(oh=oh,qa=qa,qb=qb,dma=dma,dla=dla,dmb=dmb,dlb=dlb,pa=pa,pb=pb).items(): put(f"{c}.{k}",tr(v))
put(c+".oha_t",tr(oha_t)); put(c+".ohb_t",tr(ohb_t)); put(c+".oha_a",tr(oha_a)); put(c+".ohb_a",tr(ohb_a))
ua_t=dma+dla+oha_t; ub_t=dmb+dlb+ohb_t; ua_a=dma+dla+oha_a; ub_a=dmb+dlb+ohb_a
put(c+".ua_t",tr(ua_t)); put(c+".ub_t",tr(ub_t)); put(c+".ua_a",tr(ua_a)); put(c+".ub_a",tr(ub_a))
put(c+".ma_t",m(pa-ua_t)); put(c+".mb_t",m(pb-ub_t)); put(c+".ma_a",m(pa-ua_a)); put(c+".mb_a",m(pb-ub_a))

# 39-3 müşteri kârlılığı (hizmet maliyeti)
c="cu"; s=10e6; gm=0.15; co=600; cd=900; r=0.36
put(c+".s",tr(s)); put(c+".gm",pct(gm,0)); put(c+".gp",tr(s*gm)); put(c+".co",tr(co)); put(c+".cd",tr(cd)); put(c+".r",pct(r,0))
for k,o,d,dso in (("x",50,50,30),("y",1000,800,90)):
    ops=o*co+d*cd; fin=s*dso/365*r; pr=s*gm-ops-fin
    put(f"{c}.{k}_o",tr(o)); put(f"{c}.{k}_d",tr(d)); put(f"{c}.{k}_dso",tr(dso)); put(f"{c}.{k}_ops",tr(ops)); put(f"{c}.{k}_fin",tr(fin)); put(f"{c}.{k}_pr",m(pr))

# 39-4 standart maliyet sapmaları
c="sv"; q=10_000; skg=2; sp=30; akg=21_000; ap=33
put(c+".q",tr(q)); put(c+".skg",tr(skg)); put(c+".sp",tr(sp)); put(c+".akg",tr(akg)); put(c+".ap",tr(ap)); put(c+".stdkg",tr(q*skg))
pv=(ap-sp)*akg; qv=(akg-q*skg)*sp
put(c+".pv",tr(pv)); put(c+".qv",tr(qv)); put(c+".tv",tr(pv+qv)); put(c+".std",tr(q*skg*sp)); put(c+".act",tr(akg*ap))

# 39-5 ilgili maliyetler: özel sipariş
c="so"; q=20_000; p=70; vc=60; fc=20; extra=50_000; reg=90
put(c+".q",tr(q)); put(c+".p",tr(p)); put(c+".vc",tr(vc)); put(c+".fc",tr(fc)); put(c+".full",tr(vc+fc)); put(c+".extra",tr(extra)); put(c+".reg",tr(reg))
put(c+".cm",tr(q*(p-vc))); put(c+".net",tr(q*(p-vc)-extra)); put(c+".lost",tr(q*(reg-vc))); put(c+".net2_abs",tr(abs(q*(p-vc)-extra-q*(reg-vc))))
put(c+".acc_loss",tr(q*(vc+fc-p)))

# 42-1 ortalama ve marjinal vergi (örnek dilimler)
c="tx"; br=[(100_000,0.15),(250_000,0.20),(600_000,0.27),(float("inf"),0.35)]
def tax(y):
    t=0;lo=0
    for hi,r in br:
        if y>lo: t+=(min(y,hi)-lo)*r
        lo=hi
    return t
y=400_000; t=tax(y)
put(c+".y",tr(y)); put(c+".t",tr(t)); put(c+".avg",pct(t/y,1)); put(c+".mar",pct(0.27,0))
for i,(hi,r) in enumerate(br): put(f"{c}.r{i+1}",pct(r,0))
put(c+".b1",tr(100_000)); put(c+".b2",tr(250_000)); put(c+".b3",tr(600_000))
bonus=50_000; put(c+".bonus",tr(bonus)); put(c+".bonus_tax",tr(tax(y+bonus)-t)); put(c+".bonus_net",tr(bonus-(tax(y+bonus)-t)))
put(c+".t1",tr(100_000*0.15)); put(c+".t2",tr(150_000*0.20)); put(c+".t3",tr(150_000*0.27))

# 42-8 kayıt dışılık ve fiyat farkı
c="in"; p=100; k=0.20; inf=105; gm=0.15
put(c+".p",tr(p)); put(c+".k",pct(k,0)); put(c+".g",tr(p*(1+k))); put(c+".inf",tr(inf)); put(c+".gap",tr(p*(1+k)-inf)); put(c+".gap_pct",pct((p*(1+k)-inf)/(p*(1+k)),1)); put(c+".gm",pct(gm,0)); put(c+".gp",tr(p*gm))

# 43-1 vergi sistemi genel bakış: bir satışın vergi akışı
c="ov"; s=1e6; pur=700_000; k=0.20; opx=250_000; ct=0.25
put(c+".s",tr(s)); put(c+".pur",tr(pur)); put(c+".k",pct(k,0)); put(c+".ok",tr(s*k)); put(c+".ik",tr(pur*k)); put(c+".nk",tr((s-pur)*k))
put(c+".opx",tr(opx)); put(c+".pbt",tr(s-pur-opx)); put(c+".ct",pct(ct,0)); put(c+".ctx",tr((s-pur-opx)*ct))

# 43-2 stopaj
c="wh"; net=80_000; r=0.20; gross=net/(1-r)
put(c+".net",tr(net)); put(c+".r",pct(r,0)); put(c+".gross",tr(gross)); put(c+".w",tr(gross-net))

# 43-3 kurumlar vergisi
c="ct"; ebt=4e6; kk=500_000; ist=300_000; r=0.25; base=ebt+kk-ist; tx=base*r
put(c+".ebt",tr(ebt)); put(c+".kk",tr(kk)); put(c+".ist",tr(ist)); put(c+".base",tr(base)); put(c+".r",pct(r,0)); put(c+".tx",tr(tx)); put(c+".eff",pct(tx/ebt,1))

# 43-4 KDV
c="vt"; s=1e6; pur=700_000; k=0.20; s2=600_000
put(c+".s",tr(s)); put(c+".pur",tr(pur)); put(c+".k",pct(k,0)); put(c+".ok",tr(s*k)); put(c+".ik",tr(pur*k)); put(c+".pay",tr((s-pur)*k))
put(c+".s2",tr(s2)); put(c+".ok2",tr(s2*k)); put(c+".dev",tr(pur*k-s2*k))

# 43-5 ÖTV ve damga vergisi
c="ot"; b=100; o=0.25; k=0.20; ctr=5e6; dv=0.00948
put(c+".b",tr(b)); put(c+".o",pct(o,0)); put(c+".ov",tr(b*o)); put(c+".kb",tr(b*(1+o))); put(c+".k",pct(k,0)); put(c+".kv",tr(b*(1+o)*k)); put(c+".tot",tr(b*(1+o)*(1+k)))
put(c+".ctr",tr(ctr)); put(c+".dv",tr(dv*1000,2)); put(c+".dvt",tr(ctr*dv))

# 43-6 vergi incelemesi: ceza ve faiz (örnek)
c="vu"; t=100_000; ceza=1.0; fm=0.03; n=18
put(c+".t",tr(t)); put(c+".ceza",tr(t*ceza)); put(c+".fm",pct(fm,0)); put(c+".n",tr(n)); put(c+".faiz",tr(t*fm*n)); put(c+".tot",tr(t+t*ceza+t*fm*n))
put(c+".pis",tr(t+t*fm*n))

OUT+=[l.split(" = ")[0]+"_abs = "+l.split(" = ")[1][1:] for l in list(OUT) if l.split(" = ")[1].startswith("-") and not any(o.startswith(l.split(" = ")[0]+"_abs ") for o in OUT)]
open(__file__.replace(".py",".out"),"w",encoding="utf-8").write("\n".join(OUT)+"\n")
print("\n".join(OUT))
