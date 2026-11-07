#!/usr/bin/env python3
"""ECO kartları, 1. parti (b1): örneklerdeki tüm rakamlar. Çıktı: cards_numbers_eco_b1.out
Biçim: <kart>.<anahtar> = <Türkçe biçimli değer>. Tüm rakamlar temsilidir."""
import math
OUT=[]
def tr(x,d=0):
    s=f"{x:,.{d}f}"; return s.replace(",","X").replace(".",",").replace("X",".")
def pct(x,d=1): return ("−%" if x<0 else "%")+tr(abs(x)*100,d)
def put(k,v): OUT.append(f"{k} = {v}")

# 1-1 fırsat maliyeti / batık maliyet
c="oc"
kira=150_000; maas_alt=90_000; muh_kar=4_000_000
put(c+".kira_ay",tr(kira)); put(c+".kira_yil",tr(kira*12))
put(c+".maas_ay",tr(maas_alt)); put(c+".maas_yil",tr(maas_alt*12))
put(c+".muh_kar",tr(muh_kar)); put(c+".ekon_kar",tr(muh_kar-kira*12-maas_alt*12))
batik=2_000_000; ek=1_500_000; ek_katki=1_200_000; alt_katki=1_800_000
put(c+".batik",tr(batik)); put(c+".ek",tr(ek)); put(c+".ek_katki",tr(ek_katki)); put(c+".alt_katki",tr(alt_katki))
put(c+".devam_net",tr(ek_katki-ek)); put(c+".alt_net",tr(alt_katki-ek)); put(c+".fark",tr(alt_katki-ek_katki))

# 1-3 arz-talep: Qd=a-bP, Qs=-c+dP
c="sd"; a,b,cc,d=10_000,40,2_000,60
P=(a+cc)/(b+d); Q=a-b*P
put(c+".p0",tr(P)); put(c+".q0",tr(Q))
a2=11_000; P2=(a2+cc)/(b+d); Q2=a2-b*P2
put(c+".p_talep",tr(P2)); put(c+".q_talep",tr(Q2))
sh=10; P3=(a+cc+d*sh)/(b+d); Q3=a-b*P3
put(c+".p_maliyet",tr(P3)); put(c+".q_maliyet",tr(Q3)); put(c+".yansima",pct((P3-P)/sh,0)); put(c+".yansima_tl",tr(P3-P))
put(c+".ciro0",tr(P*Q)); put(c+".ciro_maliyet",tr(P3*Q3))

# 1-5 vergi yükü ve tavan fiyat (aynı model)
c="ti"; t=10
Pb=(a+cc+d*t)/(b+d); Qt=a-b*Pb; Ps=Pb-t
put(c+".p0",tr(P)); put(c+".q0",tr(Q)); put(c+".pb",tr(Pb)); put(c+".ps",tr(Ps)); put(c+".qt",tr(Qt))
put(c+".alici_pay",pct((Pb-P)/t,0)); put(c+".satici_pay",pct((P-Ps)/t,0))
put(c+".alici_tl",tr(Pb-P)); put(c+".satici_tl",tr(P-Ps)); put(c+".vergi_gelir",tr(t*Qt)); put(c+".hacim_kayip",tr(Q-Qt))
put(c+".formul_alici",pct(d/(b+d),0))
cap=110; put(c+".tavan",tr(cap)); put(c+".qd_tavan",tr(a-b*cap)); put(c+".qs_tavan",tr(-cc+d*cap)); put(c+".kitlik",tr((a-b*cap)-(-cc+d*cap)))

# 2-5 büyüme oranları
c="gr"; s0=100_000_000; s1=165_000_000; inf=0.50
put(c+".s0",tr(s0)); put(c+".s1",tr(s1)); put(c+".nom",pct(s1/s0-1)); put(c+".inf",pct(inf,0)); put(c+".reel",pct((s1/s0)/(1+inf)-1))
put(c+".yanlis_reel",pct(s1/s0-1-inf))
m=0.03; put(c+".aylik",pct(m,0)); put(c+".yillik_bilesik",pct((1+m)**12-1,2)); put(c+".yillik_basit",pct(m*12,0))
s3=300_000_000; put(c+".s3",tr(s3)); put(c+".cagr",pct((s3/s0)**(1/3)-1,2)); put(c+".ort_basit",pct((s3/s0-1)/3,2))
put(c+".ln",tr(math.log(s1/s0),4)); put(c+".ln_inf",tr(math.log(1+inf),4)); put(c+".ln_reel",tr(math.log(s1/s0)-math.log(1+inf),4))
put(c+".yukari_asagi",pct(1.5*0.5-1,0))
put(c+".ikiye_katlanma",tr(math.log(2)/math.log(1+m),1))

# 5-5 ölçek ekonomisi
c="sc"; F=1_200_000; v=12
for qv in (50_000,100_000,200_000):
    put(f"{c}.ac_{qv//1000}",tr((F+v*qv)/qv,2)); put(f"{c}.tc_{qv//1000}",tr(F+v*qv))
put(c+".F",tr(F)); put(c+".v",tr(v))
F2=1_800_000; v2=6; q2=200_000; put(c+".F2",tr(F2)); put(c+".v2",tr(v2))
ac_b=(F2+v2*q2)/q2; ac_b100=(F2+v2*100_000)/100_000; ac_200=(F+v*q2)/q2
put(c+".ac_buyuk",tr(ac_b,2)); put(c+".ac_buyuk_100",tr(ac_b100,2))
put(c+".tasarruf_koli",tr(ac_200-ac_b,2)); put(c+".tasarruf_ay",tr((ac_200-ac_b)*q2))
# bölüşülmüş araç: kapsam ekonomisi
arac=95_000; put(c+".arac",tr(arac)); put(c+".iki_arac",tr(2*arac)); put(c+".ortak_arac",tr(arac*1.25)); put(c+".kapsam_tasarruf",tr(2*arac-arac*1.25))

# 6-4 fiyat farklılaştırma: kademeli iskonto
c="pd"; liste=100; mal=80; isk=96
qa=8; put(c+".liste",tr(liste)); put(c+".mal",tr(mal)); put(c+".isk",tr(isk))
put(c+".a_once",tr(qa*(liste-mal))); qa2=10; put(c+".a_sonra",tr(qa2*(isk-mal)))
qb=15; put(c+".b_kayip",tr(qb*(liste-isk))); put(c+".b_once",tr(qb*(liste-mal))); put(c+".b_sonra",tr(qb*(isk-mal)))
nA=40; nB=25; nC=60; qc=4
once=nA*qa*(liste-mal)+nB*qb*(liste-mal)+nC*qc*(liste-mal)
sonra=nA*qa2*(isk-mal)+nB*qb*(isk-mal)+nC*qc*(liste-mal)
put(c+".nA",nA); put(c+".nB",nB); put(c+".nC",nC); put(c+".qc",qc)
put(c+".toplam_once",tr(once)); put(c+".toplam_sonra",tr(sonra)); put(c+".fark",tr(sonra-once))
put(c+".hacim_once",tr(nA*qa+nB*qb+nC*qc)); put(c+".hacim_sonra",tr(nA*qa2+nB*qb+nC*qc))
# alternatif eşik 16 koli
put(c+".b_esik16",tr(nA*qa*(liste-mal)+nB*qb*(liste-mal)+nC*qc*(liste-mal)))

# 7-1 oyun teorisi
c="gt"; K,D,S,B=10,13,6,7
put(c+".k",K); put(c+".d",D); put(c+".s",S); put(c+".b",B)
dl=(D-K)/(D-B); put(c+".delta",tr(dl,2))
put(c+".isbirligi_deger",tr(K/(1-0.8),0)); put(c+".sapma_deger",tr(D+B*0.8/(1-0.8),0))

# 7-5 ihale
c="au"; hacim=50_000; urun=78; lojistik=4; iade=1.5; ek_isk=1.5
tm=urun+lojistik+iade+ek_isk; put(c+".hacim",tr(hacim)); put(c+".urun",tr(urun)); put(c+".lojistik",tr(lojistik)); put(c+".iade",tr(iade,2)); put(c+".ek_isk",tr(ek_isk,2))
put(c+".tm",tr(tm,2)); put(c+".gorunen",tr(urun+lojistik,2))
r=0.45; vade=90; fin=tm*r*vade/365; put(c+".fin",tr(fin,2)); put(c+".tam",tr(tm+fin,2))
for bid in (88,92,96):
    put(f"{c}.kar_{bid}",tr((bid-tm-fin)*hacim)); put(f"{c}.kar_birim_{bid}",tr(bid-tm-fin,2))

# 7-7 oligopol
c="ol"; A=200; mc=50
qc_=(A-mc)/3; Pc=A-2*qc_; put(c+".cq",tr(qc_)); put(c+".cp",tr(Pc)); put(c+".cpi",tr((Pc-mc)*qc_))
Qm=(A-mc)/2; Pm=A-Qm; put(c+".mq",tr(Qm)); put(c+".mq_each",tr(Qm/2,1)); put(c+".mp",tr(Pm)); put(c+".mpi_each",tr((Pm-mc)*Qm/2,1))
qd=(A-mc-Qm/2)/2; Pd=A-qd-Qm/2; put(c+".dq",tr(qd,2)); put(c+".dp",tr(Pd,2)); put(c+".dpi",tr((Pd-mc)*qd,2)); put(c+".diger_pi",tr((Pd-mc)*Qm/2,2))
put(c+".bp",tr(mc))

# 8-2 dikey ilişkiler: çift marjinalleşme, P=200-Q, c=40
c="vr"; A=200; mc=40
Qi=(A-mc)/2; Pi=A-Qi; put(c+".iq",tr(Qi)); put(c+".ip",tr(Pi)); put(c+".ipi",tr((Pi-mc)*Qi))
w=(A+mc)/2; Qs=(A-w)/2; Ps=A-Qs; put(c+".w",tr(w)); put(c+".sq",tr(Qs)); put(c+".sp",tr(Ps)); put(c+".uret_pi",tr((w-mc)*Qs)); put(c+".bayi_pi",tr((Ps-w)*Qs)); put(c+".top_pi",tr((w-mc)*Qs+(Ps-w)*Qs))
put(c+".kayip",tr((Pi-mc)*Qi-((w-mc)*Qs+(Ps-w)*Qs)))

# 9-2 ücret artışı
c="mw"; n=40; brut=50_000; yuk=0.20; artis=0.30; ciro=40_000_000; bm=0.12
pers=n*brut*(1+yuk); put(c+".n",n); put(c+".brut",tr(brut)); put(c+".yuk",pct(yuk,0)); put(c+".artis",pct(artis,0))
put(c+".pers",tr(pers)); put(c+".ciro",tr(ciro)); put(c+".bk",tr(ciro*bm)); put(c+".bm",pct(bm,0))
ek=n*brut*artis*(1+yuk); put(c+".ek",tr(ek)); put(c+".ek_yil",tr(ek*12))
put(c+".pay_once",pct(pers/(ciro*bm),0)); put(c+".pay_sonra",pct((pers+ek)/(ciro*bm),0)); put(c+".fiyat_gerek",pct(ek/ciro,2))
vis=25; gun=24; temsil=12; put(c+".ziyaret",vis); put(c+".temsilci",temsil)
put(c+".ziyaret_ek",tr(vis*(1+0.10),1))

# 12-1 ters seçim
c="as"; sat=50_000; mar=0.10; good,risky=80,20; pg,pr=0.01,0.15
put(c+".sat",tr(sat)); put(c+".mar",pct(mar,0)); put(c+".kat",tr(sat*mar)); put(c+".pg",pct(pg,0)); put(c+".pr",pct(pr,0))
put(c+".kayip_g",tr(pg*sat)); put(c+".kayip_r",tr(pr*sat)); put(c+".net_g",tr(sat*mar-pg*sat)); put(c+".net_r",tr(sat*mar-pr*sat))
put(c+".ort_temerrut",pct((good*pg+risky*pr)/(good+risky),1))
tot=good*(sat*mar-pg*sat)+risky*(sat*mar-pr*sat); put(c+".toplam",tr(tot))
rk=5; tot2=good*(sat*mar-pg*sat)+rk*(sat*mar-pr*sat); put(c+".kalan_r",rk); put(c+".toplam2",tr(tot2)); put(c+".fark",tr(tot2-tot))
put(c+".good",good); put(c+".risky",risky)

open(__file__.replace(".py",".out"),"w",encoding="utf-8").write("\n".join(OUT)+"\n")
print("\n".join(OUT))
