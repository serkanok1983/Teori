#!/usr/bin/env python3
"""ECO kartları, 2. parti (b2): örneklerdeki tüm rakamlar. Çıktı: cards_numbers_eco_b2.out
Biçim: <kart>.<anahtar> = <Türkçe biçimli değer>. Tüm rakamlar temsilidir; gerçek faiz, kur veya enflasyon verisi değildir."""
OUT=[]
def tr(x,d=0):
    s=f"{x:,.{d}f}"; return s.replace(",","X").replace(".",",").replace("X",".")
def pct(x,d=1): return ("−%" if x<0 else "%")+tr(abs(x)*100,d)
def put(k,v): OUT.append(f"{k} = {v}")

# 12-3 asil-vekil: ciro primi vs brüt kâr primi
c="pa"; cx,mx=100_000,0.08; cy,my=70_000,0.18
gx,gy=cx*mx,cy*my
put(c+".cx",tr(cx)); put(c+".cy",tr(cy)); put(c+".mx",pct(mx,0)); put(c+".my",pct(my,0))
put(c+".gx",tr(gx)); put(c+".gy",tr(gy)); put(c+".kayip",tr(gy-gx))
put(c+".px_ciro",tr(cx*0.01)); put(c+".py_ciro",tr(cy*0.01))
put(c+".px_bk",tr(gx*0.08)); put(c+".py_bk",tr(gy*0.08))

# 13-1 sezgisel yanılgılar: aşırı güven ve planlama yanılgısı
c="hb"; hit=6; n=10; put(c+".isabet",pct(hit/n,0)); put(c+".hedef",pct(0.9,0))
plan=[3,2,4,3,3]; act=[4.5,3,6,4,5]
put(c+".plan_ort",tr(sum(plan)/len(plan),1)); put(c+".gercek_ort",tr(sum(act)/len(act),1))
put(c+".asim",pct(sum(act)/sum(plan)-1,0))

# 14-1 GSYH: nominal, reel, deflatör
c="gdp"; n0,n1=100,160; d0,d1=100,145
real=(n1/n0)/(d1/d0)-1
put(c+".nom",pct(n1/n0-1,0)); put(c+".defl",pct(d1/d0-1,0)); put(c+".reel",pct(real,2))
# şirket: reel hacim büyümesi vs ekonomi
put(c+".sirket_hacim",pct(0.06,0)); put(c+".ekonomi",pct(0.03,0))
put(c+".pay_artis",pct(1.06/1.03-1,2))

# 14-2 enflasyon ölçümü: kendi maliyet sepeti
c="inf"; w={"personel":(0.40,0.50),"akaryakit":(0.25,0.30),"kira":(0.20,0.60),"diger":(0.15,0.40)}
tot=0
for k,(a,b) in w.items():
    put(f"{c}.w_{k}",pct(a,0)); put(f"{c}.r_{k}",pct(b,0)); put(f"{c}.katki_{k}",tr(a*b*100,1)); tot+=a*b
put(c+".sepet",pct(tot,1)); put(c+".tufe",pct(0.40,0)); put(c+".ufe",pct(0.35,0))
put(c+".fark_puan",tr((tot-0.40)*100,1))
# baz etkisi: aylık oranlar
m_old=[0.03]*11+[0.08]; m_new=[0.03]*12
import math
y_old=math.prod(1+x for x in m_old)-1; y_new=math.prod(1+x for x in m_new)-1
put(c+".yil_eski",pct(y_old,1)); put(c+".yil_yeni",pct(y_new,1))

# 50-4 politika faizi ve kredi maliyeti
c="pr"; K=10_000_000; r1=0.50; r2=0.45; g=90
i1=K*r1*g/365; i2=K*r2*g/365
put(c+".kredi",tr(K)); put(c+".r1",pct(r1,0)); put(c+".r2",pct(r2,0)); put(c+".gun",g)
put(c+".faiz1",tr(i1)); put(c+".faiz2",tr(i2)); put(c+".fark",tr(i1-i2))
# vadeli satış finansmanı: 60 gün vade, 20M alacak
A=20_000_000; put(c+".alacak",tr(A)); put(c+".alacak_maliyet",tr(A*r1*60/365))

# 18-3 Fisher: reel faiz
c="fi"; i=0.50; pe=0.40
put(c+".i",pct(i,0)); put(c+".pe",pct(pe,0)); put(c+".reel",pct((1+i)/(1+pe)-1,2)); put(c+".yaklasik",pct(i-pe,0))
vf=0.04; y=(1+vf)**12-1
put(c+".vade_farki",pct(vf,0)); put(c+".vade_yillik",pct(y,1)); put(c+".vade_reel",pct((1+y)/(1+pe)-1,1))
# negatif reel faiz örneği
i2=0.45; pe2=0.55; put(c+".i2",pct(i2,0)); put(c+".pe2",pct(pe2,0)); put(c+".reel2",pct((1+i2)/(1+pe2)-1,1))

# 19-3 arz şoku: maliyet enflasyonu ve fiyat
c="ss"; P=100; C=82
sh={"hammadde":(0.50,0.20),"enerji":(0.10,0.80),"iscilik":(0.15,0),"lojistik":(0.10,0),"diger":(0.15,0)}
ci=sum(a*b for a,b in sh.values())
for k,(a,b) in sh.items(): put(f"{c}.w_{k}",pct(a,0))
put(c+".enerji_artis",pct(0.80,0)); put(c+".hammadde_artis",pct(0.20,0))
put(c+".maliyet_artis",pct(ci,0)); put(c+".P",tr(P)); put(c+".C",tr(C)); put(c+".C1",tr(C*(1+ci),2))
put(c+".marj_tl",tr(P-C)); put(c+".marj_pct",pct((P-C)/P,0))
p_pct=C*(1+ci)/(C/P); p_tl=C*(1+ci)+(P-C)
put(c+".fiyat_pct",tr(p_pct,2)); put(c+".fiyat_pct_artis",pct(p_pct/P-1,0))
put(c+".fiyat_tl",tr(p_tl,2)); put(c+".fiyat_tl_artis",pct(p_tl/P-1,2))
put(c+".marj_tl_pct_sonra",pct((p_tl-C*(1+ci))/p_tl,1))

# 21-1 para politikası: reel faiz ve stok tutma kararı
c="mp"; i=0.45; S=20_000_000
for tag,pi in (("a",0.30),("b",0.50)):
    put(f"{c}.pe_{tag}",pct(pi,0)); put(f"{c}.reel_{tag}",pct((1+i)/(1+pi)-1,2))
    put(f"{c}.kazanc_{tag}",tr(S*pi)); put(f"{c}.net_{tag}",tr(S*pi-S*i))
put(c+".i",pct(i,0)); put(c+".stok",tr(S)); put(c+".faiz",tr(S*i))

# 22-1 nominal ve reel kur
c="fx"; e0,e1=30,36; tr_inf=0.25; us_inf=0.03
put(c+".e0",tr(e0)); put(c+".e1",tr(e1)); put(c+".nom",pct(e1/e0-1,0))
put(c+".tr_inf",pct(tr_inf,0)); put(c+".us_inf",pct(us_inf,0))
real=(e1/e0)*(1+us_inf)/(1+tr_inf)-1; put(c+".reel",pct(real,2))
usd=1_000_000; put(c+".usd",tr(usd)); put(c+".tl0",tr(usd*e0)); put(c+".tl1",tr(usd*e1))
# yerli rakibin maliyeti enflasyonla artarsa
dom0=usd*e0; dom1=dom0*(1+tr_inf); put(c+".yerli1",tr(dom1))
put(c+".ithal_fark",pct((usd*e1)/dom1-1,1))

# 23-2 kur krizi: döviz borcu
c="cc"; D=2_000_000; e0,e1=30,45; E=50_000_000
put(c+".borc_usd",tr(D)); put(c+".e0",tr(e0)); put(c+".e1",tr(e1)); put(c+".dep",pct(e1/e0-1,0))
put(c+".borc0",tr(D*e0)); put(c+".borc1",tr(D*e1)); put(c+".zarar",tr(D*(e1-e0)))
put(c+".oz0",tr(E)); put(c+".oz1",tr(E-D*(e1-e0))); put(c+".oz_kayip",pct(D*(e1-e0)/E,0))
# hedge: forward maliyeti örnek yıllık %25 TL-USD faiz farkı, 6 ay
put(c+".hedge_maliyet",tr(D*e0*0.25*0.5))

# 24-3 kriz dersleri: likidite tamponu
c="lb"; tah=40_000_000; ode=38_000_000; dus=0.30; ode_dus=0.10; ay=3
acik=tah*(1-dus)-ode*(1-ode_dus)
put(c+".tah",tr(tah)); put(c+".ode",tr(ode)); put(c+".dus",pct(dus,0)); put(c+".ode_dus",pct(ode_dus,0))
put(c+".acik_ay",tr(-acik)); put(c+".ay",ay); put(c+".tampon",tr(-acik*ay))
put(c+".ode_sonra",tr(ode*(1-ode_dus))); put(c+".tah_sonra",tr(tah*(1-dus)))

# 4-2 risk ve sigorta
c="ri"; p=0.01; L=20_000_000; prim=300_000; E=15_000_000
put(c+".p",pct(p,0)); put(c+".L",tr(L)); put(c+".bek",tr(p*L)); put(c+".prim",tr(prim)); put(c+".oz",tr(E))
put(c+".fark",tr(prim-p*L))
m=1_000_000; prim2=220_000
put(c+".muaf",tr(m)); put(c+".prim2",tr(prim2)); put(c+".tasarruf",tr(prim-prim2)); put(c+".ek_bek",tr(p*m))
# sık küçük hasar: araç filo
n=40; ph=0.15; h=60_000; put(c+".arac",n); put(c+".hasar_p",pct(ph,0)); put(c+".hasar",tr(h)); put(c+".filo_bek",tr(n*ph*h))
put(c+".filo_prim",tr(n*ph*h*1.35)); put(c+".filo_fark",tr(n*ph*h*0.35))

open(__file__.replace(".py",".out"),"w",encoding="utf-8").write("\n".join(OUT)+"\n")
print("\n".join(OUT))
