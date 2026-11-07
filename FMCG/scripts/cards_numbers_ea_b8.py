# EA batch 8 temsili rakamlar
def tr(x,d=2):
    s=f"{x:,.{d}f}"; return s.replace(',','X').replace('.',',').replace('X','.')
# 35-2 e-imza: 400 sozlesme x 3 gun kargo -> 1 gun
print("35-2 sozlesme",400,"sure gun once/sonra",3,1,"toplam gun tasarrufu",400*2)
# 37-2 e-fatura senaryo: 1000 fatura, 12 red
print("37-2a red orani %", tr(100*12/1000,1))
# 37-2 e-irsaliye: 900 irsaliye/ay, 27 hatali plaka
print("37-2b hata orani %", tr(100*27/900,1))
# 37-3 entegrasyon maliyet (varsayimsal): 3000 belge/ay x 0,40
print("37-3 aylik kontor", tr(3000*0.40), "yillik", tr(3000*0.40*12))
# 37-4 e-defter: 12 ay, 2 gecikme riski
print("37-4 ay",12)
# 38-1 odeme: havale 500.000, vade 30 gun, DBS
inv=500000; days=30; rate=0.36; print("38-1 30 gun finansman maliyeti (yillik %36 varsayim)", tr(inv*rate*days/365))
# 38-3 Findeks: 200 bayi, 30 risk
print("38-3 riskli bayi %", tr(100*30/200,1))
# 39-1 low-code: 15 form, 2 gun vs 10 gun
print("39-1 gun tasarrufu", 15*(10-2))
# 39-2 RPA: 1200 islem/ay x 4 dk
m=1200*4/60; print("39-2 aylik saat", tr(m,1))
# 39-3 genai: 20 kisi x 2 saat/hafta
print("39-3 haftalik saat",20*2,"kontrol orani %",tr(100*0.2,0))
# 39-4 asistan: 50 soru, 44 dogru
print("39-4 dogruluk %", tr(100*44/50,1))
# 39-5 ML: oneri kabul 1000 oneri 180 kabul
print("39-5 kabul %", tr(100*180/1000,1))
# 40-4 SFA-ERP: 5000 siparis, 75 hata
print("40-4 hata %", tr(100*75/5000,1))
# 41-1 vaka: 9 sistem, 14 arayuz
print("41-1 sistem",9,"arayuz",14)
# 41-5 cutover: 48 saat pencere, 36 gorev
print("41-5 pencere saat",48,"gorev",36,"acik bakiye mutabakati 1.250 musteri")
