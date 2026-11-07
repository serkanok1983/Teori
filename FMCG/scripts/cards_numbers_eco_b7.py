#!/usr/bin/env python3
"""ECO kartları, 7. parti (b7): örneklerdeki tüm rakamlar. Çıktı: cards_numbers_eco_b7.out
Tüm rakamlar temsilidir; prim, vergi, emisyon faktörü ve fiyatlar örnek değerdir."""
import math, statistics as st
OUT=[]
def tr(x,d=0):
    s=f"{x:,.{d}f}"; return s.replace(",","X").replace(".",",").replace("X",".")
def pct(x,d=1): return ("−%" if x<0 else "%")+tr(abs(x)*100,d)
def put(k,v): OUT.append(f"{k} = {v}")

# 44-3 SGK işveren maliyeti
c="sg"; g=50_000; er=0.2275; ee=0.15; inc=0.05
put(c+".g",tr(g)); put(c+".er",pct(er,2)); put(c+".erv",tr(g*er)); put(c+".cost",tr(g*(1+er))); put(c+".ee",pct(ee,0)); put(c+".eev",tr(g*ee))
sev=g/12; put(c+".sev",tr(sev)); put(c+".full",tr(g*(1+er)+sev)); put(c+".mult",tr((g*(1+er)+sev)/g,2))
put(c+".inc",tr(inc*100,0)); put(c+".save",tr(g*inc)); put(c+".save_y",tr(g*inc*12)); put(c+".year",tr((g*(1+er)+sev)*12))

# 40-4 SKDM (CBAM)
c="cb"; q=10_000; e=2.0; e2=1.5; pr=80; price=700
cost=q*e*pr; put(c+".q",tr(q)); put(c+".e",tr(e,1)); put(c+".e2",tr(e2,1)); put(c+".pr",tr(pr)); put(c+".cost",tr(cost)); put(c+".pt",tr(e*pr)); put(c+".price",tr(price)); put(c+".share",pct(e*pr/price,1))
put(c+".cost2",tr(q*e2*pr)); put(c+".save",tr(cost-q*e2*pr))

# 47-1 tanımlayıcı istatistik
c="ds"; v=[12,14,15,15,16,17,18,19,20,74]
put(c+".list","; ".join(tr(x) for x in v)); put(c+".mean",tr(st.mean(v),1)); put(c+".med",tr(st.median(v),1)); put(c+".sd",tr(st.stdev(v),1))
w=v[:-1]; put(c+".mean9",tr(st.mean(w),1)); put(c+".sd9",tr(st.stdev(w),1)); put(c+".max",tr(max(v)))

# 47-3 örneklem ve güven aralığı
c="sm"; n=400; p=0.30; se=math.sqrt(p*(1-p)/n); moe=1.96*se
put(c+".n",tr(n)); put(c+".p",pct(p,0)); put(c+".se",tr(se*100,2)); put(c+".moe",tr(moe*100,1)); put(c+".lo",pct(p-moe,1)); put(c+".hi",pct(p+moe,1))
n3=math.ceil(1.96**2*p*(1-p)/0.03**2); put(c+".n3",tr(n3))

# 47-4 A/B testi
c="ab"; n=5000; x1=200; x2=230; p1=x1/n; p2=x2/n; pp=(x1+x2)/(2*n); se=math.sqrt(pp*(1-pp)*2/n); z=(p2-p1)/se
pv=math.erfc(abs(z)/math.sqrt(2))
put(c+".n",tr(n)); put(c+".x1",tr(x1)); put(c+".x2",tr(x2)); put(c+".p1",pct(p1,1)); put(c+".p2",pct(p2,1)); put(c+".lift",pct(p2/p1-1,0)); put(c+".z",tr(z,2)); put(c+".pv",tr(pv,2))
nreq=math.ceil((1.96+0.8416)**2*(p1*(1-p1)+p2*(1-p2))/(p2-p1)**2); put(c+".nreq",tr(nreq))

# 47-5 korelasyon ve regresyon
c="rg"; x=[10,20,30,40,50,60,70,80]; y=[210,240,245,280,300,295,330,350]
mx,my=st.mean(x),st.mean(y); b=sum((a-mx)*(c2-my) for a,c2 in zip(x,y))/sum((a-mx)**2 for a in x); a0=my-b*mx
r=st.correlation(x,y)
put(c+".xs","; ".join(map(str,x))); put(c+".ys","; ".join(map(str,y))); put(c+".b",tr(b,2)); put(c+".a",tr(a0,1)); put(c+".r",tr(r,2)); put(c+".r2",pct(r*r,0)); put(c+".pred",tr(a0+b*90,0)); put(c+".b1000",tr(b*1000,0))

# 48-7 test ve kontrol, fark-içinde-fark
c="dd"; tb,ta,cb_,ca=1000,1150,800,880
gt=ta/tb-1; gc=ca/cb_-1; did=gt-gc
put(c+".tb",tr(tb)); put(c+".ta",tr(ta)); put(c+".cb",tr(cb_)); put(c+".ca",tr(ca)); put(c+".gt",pct(gt,0)); put(c+".gc",pct(gc,0)); put(c+".did",tr(did*100,0)); put(c+".eff",tr(tb*did)); put(c+".naive",tr(ta-tb)); put(c+".cf",tr(tb*(1+gc)))

# 49-1 mevsimsellik
c="ts"; nov,dec=1000,1300; inov,idec=0.95,1.25; decl=1150; inf=0.30
dn,dd_=nov/inov,dec/idec
put(c+".nov",tr(nov)); put(c+".dec",tr(dec)); put(c+".mom",pct(dec/nov-1,0)); put(c+".inov",tr(inov,2)); put(c+".idec",tr(idec,2)); put(c+".dn",tr(dn)); put(c+".dd",tr(dd_)); put(c+".dmom",pct(dd_/dn-1,1))
put(c+".decl",tr(decl)); put(c+".yoy",pct(dec/decl-1,1)); put(c+".inf",pct(inf,0)); put(c+".real",pct((dec/decl)/(1+inf)-1,1))

# 50-3 bankalarla çalışma: efektif maliyet
c="bk"; L=10e6; rm=0.035; fee=0.01; blk=0.10
intr=L*rm*12; usable=L*(1-blk)-L*fee
put(c+".L",tr(L)); put(c+".rm",pct(rm,1)); put(c+".nom",pct(rm*12,0)); put(c+".comp",pct((1+rm)**12-1,1)); put(c+".fee",pct(fee,0)); put(c+".feev",tr(L*fee)); put(c+".blk",pct(blk,0)); put(c+".blkv",tr(L*blk))
put(c+".int",tr(intr)); put(c+".usable",tr(usable)); put(c+".eff",pct((intr+L*fee)/usable,1))

# 52-1 işletme sigortası: eksik sigorta
c="is"; val=20e6; ins=12e6; loss=5e6; rate=0.0015
put(c+".val",tr(val)); put(c+".ins",tr(ins)); put(c+".loss",tr(loss)); put(c+".pay",tr(loss*ins/val)); put(c+".gap",tr(loss-loss*ins/val)); put(c+".ratio",pct(ins/val,0))
put(c+".rate",tr(rate*1000,1)); put(c+".prem_full",tr(val*rate)); put(c+".prem_low",tr(ins*rate)); put(c+".prem_diff",tr((val-ins)*rate))

# 54-3 sürdürülebilirlik raporlaması: kapsam 1-2 emisyon
c="gv"; dz=200_000; fd=2.68; kwh=1_000_000; fe=0.44; rev=500
s1=dz*fd/1000; s2=kwh*fe/1000
put(c+".dz",tr(dz)); put(c+".fd",tr(fd,2)); put(c+".kwh",tr(kwh)); put(c+".fe",tr(fe,2)); put(c+".s1",tr(s1)); put(c+".s2",tr(s2)); put(c+".tot",tr(s1+s2)); put(c+".rev",tr(rev)); put(c+".int",tr((s1+s2)/rev,2))

OUT+=[l.split(" = ")[0]+"_abs = "+l.split(" = ")[1][1:] for l in list(OUT) if l.split(" = ")[1].startswith("−")]
open(__file__.replace(".py",".out"),"w",encoding="utf-8").write("\n".join(OUT)+"\n")
print("\n".join(OUT))
