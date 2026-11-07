#!/usr/bin/env python3
"""FMCG kartları, parti 5: örnek rakamlar (temsili)."""
def tl(x,d=2): s=f"{x:,.{d}f}"; return s.replace(',','X').replace('.',',').replace('X','.')
def pct(x,d=1): return '%'+tl(x*100,d)
print("== 8-8 prim eğrisi ==")
tb=12000
def pay(a):
    if a<0.90: r=0
    elif a<1.0: r=0.5+(a-0.9)*5
    else: r=1+(a-1.0)*2
    return min(r,1.5)*tb
for a in (0.85,0.90,0.95,1.00,1.10,1.20,1.30): print(pct(a,0),"oran",pct(pay(a)/tb,0),"prim",tl(pay(a),0))
base=35000; print("hedefte değişken pay",pct(tb/(base+tb)))
print("yarışma: ek 300 nokta x 1 kalem x 600 TL x 3 ay =",tl(300*600*3,0),"katkı %30",tl(300*600*3*0.3,0),"ödül bütçesi 40.000")
print("== 8-9 koçluk ==")
def s(sr): return 176*sr*4*600
a,b=s(0.55),s(0.65); print("önce",tl(a,0),"sonra",tl(b,0),"fark/ay",tl(b-a,0),"katkı",tl((b-a)*0.3,0))
day=900000/220; print("şef günü",tl(day,0),"2 gün",tl(2*day,0))
print("== 8-10 SFA ==")
n=1800; p0=1080; p1=1350; print("SD önce",pct(p0/n),"sonra",pct(p1/n),"ek nokta",p1-p0,"yıllık ek satış",tl((p1-p0)*4*52*25,0))
print("== 8-12 beklenti ==")
for nm,pr,bn in (("Plan A",0.3,20000),("Plan B",0.7,12000)): print(nm,"olasılık",pct(pr,0),"prim",tl(bn,0),"beklenen",tl(pr*bn,0))
print("== 8-13 analitik ==")
tot=1800; top=360; print("ilk %20 nokta payı varsayım %52")
lap=210; rec=lap//2; print("kayıp nokta",lap,"geri kazanılan",rec,"yıllık",tl(rec*1500*12,0))
print("== 9-1 GMROI ==")
for nm,m,t in (("A",0.30,6),("B",0.18,14)):
    S=1_000_000; gm=S*m; cogs=S-gm; inv=cogs/t; print(nm,"brüt kâr",tl(gm,0),"ort stok",tl(inv,0),"GMROI",tl(gm/inv))
S=100; fm=24; bm=4; op=22; print("perakendeci: ön marj",fm,"arka marj",bm,"gider",op,"faaliyet kârı",fm+bm-op)
print("== 9-2 PL ==")
bp=100; bmr=0.22; plp=75; plm=0.35; print("marka marj",tl(bp*bmr),"PL marj",tl(plp*plm),"PL fiyat farkı",pct(1-plp/bp,0))
print("== 9-3 raf esnekliği ==")
e=0.17; print("3->4 yüz", pct((4/3)**e-1), "3->6 yüz", pct((6/3)**e-1), "lineer yanlış 3->4",pct(4/3-1))
w=180; print("haftalık 180 adet ->",tl(w*(4/3)**e,1))
print("== 9-4 OSA ==")
d=200; oos=0.08; ex=d*oos; print("maruz kalan talep",tl(ex,0))
r={"Başka mağazadan aynı ürün":0.31,"Başka marka":0.26,"Aynı markanın başka ürünü":0.19,"Erteleme":0.15,"Hiç almama":0.09}
print("üretici kaybı (başka marka+almama)",tl(ex*(r["Başka marka"]+r["Hiç almama"]),1),"perakendeci kaybı (mağaza+almama)",tl(ex*(r["Başka mağazadan aynı ürün"]+r["Hiç almama"]),1))
print("yıllık üretici",tl(ex*0.35*52,0),"x 40 TL =",tl(ex*0.35*52*40,0))
print("== 9-5 mükemmel mağaza ==")
k=[("Bulunurluk (zorunlu liste)",0.35,0.875),("Raf payı",0.25,0.70),("Fiyat etiketi",0.15,1.0),("Teşhir",0.15,0.5),("Planogram uyumu",0.10,0.8)]
print("puan",tl(sum(w*v for _,w,v in k)*100,1))
for n_,w,v in k: print(n_,tl(w*v*100,1))
print("== 9-6 trade marketing ==")
c=3000; u=400; cm=12; print("ek katkı",tl(u*cm,0),"getiri",pct((u*cm-c)/c,0))
u2=200; print("200 adette",tl(u2*cm,0),"getiri",pct((u2*cm-c)/c,0))
print("== 9-7 perakende medya ==")
sp=150000; att=900000; inc=0.40; cm=0.30
print("ROAS",tl(att/sp,1),"artımsal satış",tl(att*inc,0),"iROAS",tl(att*inc/sp,1),"katkı",tl(att*inc*cm,0),"net",tl(att*inc*cm-sp,0))
print("başabaş iROAS",tl(1/cm,2))

# --- ek türetilmiş değerler (kart metinlerinde kullanılanlar)
print("9-4 üretici payı", 0.26+0.09, "perakendeci payı", 0.31+0.09, "yıllık adet", round(16*0.35*52,1))
print("9-5 eksik ürün puanı", round(0.35*0.125*100,1), "raf payı tam", round(0.25*0.30*100,1), "teşhir tam", round(0.15*0.5*100,1))
print("9-6 başabaş adet", 3000/12)
print("8-13 geri kazanım", 105*1500*12)
print("9-2 fark", 26.25-22.00)
