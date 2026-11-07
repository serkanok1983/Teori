# Temsili rakamlar - FMCG batch 7 (11-8, 11-9, 12-x)
def tr(x,d=0):
    s=f"{x:,.{d}f}"; return s.replace(",","X").replace(".",",").replace("X",".")
print("11-8 soguk zincir")
val=500000; p0=0.02; p1=0.005; mon=1500; n=400
e0=val*p0; e1=val*p1; net=e0-e1-mon
print("beklenen kayip once",tr(e0),"sonra",tr(e1),"izleme",tr(mon),"net/sevkiyat",tr(net),"yillik",tr(net*n))
raf=10; zincir=4; print("raf omru",raf,"zincirde",zincir,"kalan",raf-zincir, "kalan oran %",tr((raf-zincir)/raf*100))
print("11-9 VMI")
S=50000000; d0=30; d1=20; oos0=0.06; oos1=0.03; lostshare=0.5
cap=S/365*(d0-d1); rec=S*(oos0-oos1)*lostshare
print("serbest stok",tr(cap),"kurtarilan satis",tr(rec))
print("12-1 kocluk")
saat=160; k0=0.10; k1=0.25; reps=8
print("kocluk saat/temsilci once",tr(saat*k0/reps,1),"sonra",tr(saat*k1/reps,1))
print("12-2 dijital")
r=120; a0=0.45; a1=0.85; dk=30; gun=220
print("aktif once",r*a0,"sonra",r*a1,"tasarruf saat (tam kullanim)",tr(r*a1*dk/60*gun))
print("12-3 test")
lift=3.2; se=1.5
print("GA %95",tr(lift-1.96*se,2),tr(lift+1.96*se,2))
se2=2.0; print("se2 GA",tr(lift-1.96*se2,2),tr(lift+1.96*se2,2))
print("12-4 ambalaj")
ton=120; red=0.10; kg=20
print("azalan ton",tr(ton*red),"tasarruf",tr(ton*red*1000*kg))
print("12-5 kayit disi")
c=10000000; gm=0.25; off=0.03
print("kayit disi",tr(c*off),"gercek marj %",tr((c*gm-c*off)/c*100,1))
print("12-6 marka")
hh=10000000; p0=0.20; p1=0.23; f=4; sp=50
r0=hh*p0*f*sp; r1=hh*p1*f*sp
print("ciro once",tr(r0),"sonra",tr(r1),"fark",tr(r1-r0))
f1=4.2; r2=hh*p0*f1*sp; print("yalniz siklik 4,2",tr(r2),"fark",tr(r2-r0))
print("12-7 bayi")
s=80000000; gm0=0.12; opex0=9000000; gm1=0.13; opex1=8200000
e0=s*gm0-opex0; e1=s*gm1-opex1
print("brut once",tr(s*gm0),"faaliyet kari once",tr(e0),"brut sonra",tr(s*gm1),"kar sonra",tr(e1))
dso0=75; dso1=55; print("alacak serbest",tr(s/365*(dso0-dso1)))
