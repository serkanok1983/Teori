# Temsili rakamlar - FMCG batch 8 (13-x)
def tr(x,d=0):
    s=f"{x:,.{d}f}"; return s.replace(",","X").replace(".",",").replace("X",".")
print("13-2 spin"); cat=200000; oos=0.06; rec=0.5
print("aylik kayip",tr(cat*oos),"kurtarilan aylik",tr(cat*oos*rec),"yillik",tr(cat*oos*rec*12))
print("13-2 stratejik"); v=2400000
for p in (0.2,0.5): print("olasilik",p,"beklenen",tr(v*p))
print("13-3 meddic"); n=10; out=4; h=6; print("kazanilan saat",out*h)
print("13-4 TCO")
A=(100,3,2); B=(96,6,4); print("A",sum(A),"B",sum(B))
print("13-5 alici")
sales=8000; m=0.25; metre=1.5; old=1000
print("yeni urun kar/metre/hafta",tr(sales*m/metre),"eski",old,"fark",tr(sales*m/metre-old))
print("13-6 sosyal kanit"); print("oran %",tr(120/150*100))
print("13-7 cerceve"); print("10+1 bedava etkin indirim %",tr(1/11*100,2))
mk=1800; print("aylik kayip",tr(mk),"yillik",tr(mk*12))
print("13-8 huni")
t=30
for a,b,c in ((0.4,0.5,0.6),(0.4,0.6,0.6)):
    r=a*b*c; print("donusum",tr(r*100,1),"gerekli ziyaret",tr(t/r))
print("13-9 segment")
N=1000; shares=[(0.10,0.50),(0.30,0.35),(0.60,0.15)]
for s,p in shares: print("pay",s,"nokta",int(N*s),"potansiyel payi",p,"nokta basi endeks",tr(p/s,2))
print("13-11 upsell"); b=1000; it=150; r=0.30; print("ort artis",tr(it*r),"%",tr(it*r/b*100,1))
print("13-13 CLV"); m=24000; d=0.30
for r in (0.8,0.9): print("tutma",r,"CLV",tr(m*r/(1+d-r)))
print("13-14 muzakere"); print("ZOPA 5-6 puan; tavizler 2,0 + 1,0 + 0,5 =",tr(2.0+1.0+0.5,1))
print("13-16 tahmin")
deals=[(1000000,0.6),(500000,0.3),(2000000,0.1)]; w=sum(a*p for a,p in deals)
base=4000000; print("agirlikli",tr(w),"toplam",tr(base+w),"ham toplam",tr(sum(a for a,_ in deals)))
print("13-17 vade farki"); P=10000; i=0.03
print("60 gun vade farki",tr(P*((1+i)**2-1)),"30 gun",tr(P*i))

# 13-8 ek: iyilestirmenin tasarruf ettigi ziyaret
import math as _m
_v1 = _m.ceil(30/(0.4*0.5*0.6)); _v2 = round(30/(0.4*0.6*0.6))
print("13-8 ziyaret tasarrufu", _v1 - _v2)
