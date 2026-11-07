# EA batch 7 temsili rakamlar
def tr(x,d=2):
    s=f"{x:,.{d}f}"; return s.replace(',','X').replace('.',',').replace('X','.')
# 30-1 depo KPI
lines=5000; err=40; print("30-1 toplama dogrulugu %", tr(100*(lines-err)/lines,1))
orders=1200; ontime=1128; print("30-1 zamaninda sevk %", tr(100*ontime/orders,1))
hours=320; print("30-1 saat basina satir", tr(lines/hours,1))
# 30-2 slotting
before=2.0; after=1.4; print("30-2 satir basi dk once/sonra",before,after,"tasarruf %",tr(100*(before-after)/before,1))
print("30-2 gunluk 3000 satir saat tasarrufu", tr(3000*(before-after)/60,1))
# 30-3 WMS stok dogrulugu
loc=2000; ok=1940; print("30-3 lokasyon dogrulugu %", tr(100*ok/loc,1))
# 30-4 geri cagirma
lots=1; pallets=36; stores=48; print("30-4 parti palet nokta",lots,pallets,stores)
# 31-1 TMS
km=42000; fuel=11760; print("31-1 100km yakit L", tr(100*fuel/km,1))
idle=180; print("31-1 rolanti saat",idle,"x 2 L/saat =",idle*2,"L")
# 31-3 rota
d1=180; d2=150; print("31-3 km once/sonra",d1,d2,"azalma %",tr(100*(d1-d2)/d1,1))
# 32-1 OEE
planned=480; down=60; run=planned-down; ideal=1.0; out=378; good=370
A=run/planned; P=out*ideal/run; Q=good/out
print("32-1 A P Q OEE %", tr(100*A,1),tr(100*P,1),tr(100*Q,1),tr(100*A*P*Q,1))
# 32-2 izlenebilirlik
print("32-2 hammadde partisi 1 -> uretim partisi 3 -> sevk 14 musteri")
# 32-4 bakim
fails=4; hrs=2000; print("32-4 MTBF saat", tr(hrs/fails,0)); rep=12; print("32-4 MTTR saat", tr(rep/fails,1))
# 33-1 IK
hc=250; leavers=30; print("33-1 devir orani %", tr(100*leavers/hc,1))
# 33-2 bordro (varsayimsal oranlar)
gross=50000; emp=0.15; tax=0.15
d1=gross*emp; base=gross-d1; t=base*tax; print("33-2 kesinti1",tr(d1),"matrah",tr(base),"vergi",tr(t),"net",tr(gross-d1-t))
# 33-3 prim
target=1_000_000; actual=1_080_000; bonus=20000
ach=actual/target; print("33-3 gerceklesme %",tr(100*ach,1),"prim",tr(bonus*min(ach,1.2)))
# 34-1 satin alma
price=[100,96,98]; print("34-1 teklifler",price,"en dusuk",min(price))
po=200; ontime=184; print("34-1 tedarikci zamaninda %", tr(100*ontime/po,1))
# 35-1 arsiv
docs=60000; print("35-1 yillik belge",tr(docs,0),"10 yilda",tr(docs*10,0))
