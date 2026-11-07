#!/usr/bin/env python3
"""EA kartları, 3. parti: örneklerdeki tüm rakamlar. Temsili veriler. Çalıştır: python3 scripts/cards_numbers_ea_b3.py"""
from decimal import Decimal as D, ROUND_HALF_UP
q=lambda x,p="0.01": D(x).quantize(D(p),ROUND_HALF_UP)
def tl(x,p="0.01"):
    n=len(p.split('.')[1]) if '.' in p else 0
    return f"{q(x,p):,.{n}f}".replace(",","X").replace(".",",").replace("X",".")
pct=lambda x,p="0.1": "%"+tl(D(x)*100,p)

print("== kb-ea-10-1 birim eşleme hatası")
koli_ici=24; siparis=10; print("10 koli doğru adet",siparis*koli_ici,"; hatalı okunan adet",siparis,"; fark kat",koli_ici)
price=D("18.50"); print("adet fiyatı 18,50 → doğru tutar",tl(siparis*koli_ici*price),"hatalı",tl(siparis*price))

print("== kb-ea-11-4 EDI ile elle giriş karşılaştırması")
lines=D(300); m=D("1.5"); err=D("0.015"); days=D(22)
print("günlük elle giriş saati",tl(lines*m/60,"0.1"),"ayda",tl(lines*m*days/60,"1"),"saat")
print("ayda hatalı satır",tl(lines*err*days,"1"))

print("== kb-ea-37-1 belge karışımı")
tot=D(1800); ef=D(1250); print("e-fatura payı",pct(ef/tot),"e-arşiv",tot-ef,pct((tot-ef)/tot))

print("== kb-ea-11-6 API sayfalama")
prods=12000; page=100; limit=600; calls=prods//page; print("çağrı",calls,"dakika (limit 600/dk)",tl(D(calls)/limit,"0.01"))
print("tek tek çekilirse çağrı",prods,"dakika",tl(D(prods)/limit,"0.1"))

print("== kb-ea-14-4 RPO / RTO")
backup_h=23; fail_h=16; lost=(24-backup_h)+fail_h; per_h=40
print("kaybedilen saat",lost,"yeniden girilecek sipariş (iş saatleri 08-16, 8 saat)", 8*per_h)
print("15 dk RPO ile en fazla sipariş", tl(D(per_h)*D("0.25"),"1"))
rto_h=6; rev_h=D(150000); print("6 saat RTO, saatlik ciro 150.000 → risk altındaki ciro",tl(rto_h*rev_h,"1"))

print("== kb-ea-15-2 rol tabanlı yetki")
users=120; perms=40; roles=9; print("kişi bazlı atama",users*perms,"; rol tabanlı: rol tanımı",roles,"x",perms,"=",roles*perms,"+ kullanıcı ataması",users)

print("== kb-ea-16-1 abonelik")
u=40; fee=D(1500); print("aylık",tl(u*fee,"1"),"yıllık",tl(u*fee*12,"1"))
print("kullanıcı %25 artarsa yıllık",tl(D(50)*fee*12,"1"))

print("== kb-ea-16-5 bulut sunucu çalışma saati")
full=24*30; office=12*22; print("7/24 saat",full,"mesai",office,"tasarruf",pct(D(full-office)/full))
hourly=D("9.40"); print("saatlik 9,40 TL: 7/24",tl(full*hourly),"mesai",tl(office*hourly))

print("== kb-ea-17-1 ağırlıklı puanlama")
crit={"İşe uygunluk":D("0.30"),"Toplam maliyet":D("0.25"),"Zaman":D("0.15"),"Risk":D("0.15"),"Farklılaşma":D("0.15")}
opts={"Paket olduğu gibi":[3,5,5,4,2],"Paket + ayar":[4,4,4,4,3],"Özel yazılım":[5,2,1,2,5]}
for k,v in opts.items(): print(k,tl(sum(w*s for w,s in zip(crit.values(),v)),"0.01"))

print("== kb-ea-17-2 5 yıllık TSM")
items={"Lisans/abonelik":(0,D(540000)),"Uygulama hizmeti":(D(650000),0),"Veri taşıma":(D(120000),0),"Eğitim":(D(80000),D(20000)),"Entegrasyon bakımı":(D(150000),D(60000)),"İç personel zamanı":(D(300000),D(180000)),"Altyapı/destek":(0,D(90000))}
tot=0; yr1=0
for k,(o,a) in items.items():
    t=o+a*5; tot+=t; yr1+=o+a; print(k,"ilk",tl(o,"1"),"yıllık",tl(a,"1"),"5 yıl",tl(t,"1"))
print("5 yıl TSM",tl(tot,"1"),"1. yıl",tl(yr1,"1"),"abonelik payı",pct(D(540000*5)/tot))

print("== kb-ea-17-3 MoSCoW")
req={"Must":46,"Should":52,"Could":30,"Won't":12}; t=sum(req.values())
for k,v in req.items(): print(k,v,pct(D(v)/t))
print("toplam",t)
