---
id: kb-eco-9-2-minimum-wage-labour-costs
title: "Asgari ücret ve işgücü maliyeti: Ücret artışı fiyata ve verimliliğe nasıl yansır?"
summary: "Ücret artışının dağıtım işletmesinin maliyet yapısına etkisini, artışı karşılamak için gereken fiyat veya verimlilik artışını hesaplamayı ve asgari ücretin istihdam etkisine dair temel bulguları anlatır."
course: eco
category: ekonomi-temelleri
tags: [isgucu, maliyet, verimlilik]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [ECO-9.2]
reading_minutes: 3
key_points:
  - "Ücret artışının toplam maliyete etkisi, personel giderinin brüt kâr içindeki payına göre ölçülmelidir."
  - "Brüt ücretin üzerine işveren primleri ve diğer yükler eklenir; maliyet hesabını bu toplamla yapın."
  - "Artış ya fiyata, ya verimliliğe ya da kâra yansır; üçü için ayrı hesap yapın."
  - "Asgari ücretin istihdama etkisi üzerine akademik bulgular karışıktır; tek bir kesin sonuç yoktur."
  - "Güncel asgari ücret ve prim oranlarını resmî kaynaktan kontrol edin."
glossary_terms: [isveren-maliyeti]
related: [kb-eco-44-3-sgk-employer-costs, kb-fmcg-8-4-sales-force-sizing, kb-fmcg-7-1-distributor-pnl, kb-eco-19-3-supply-shocks-cost-inflation]
sources:
  - title: "Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania: Reply"
    authors: "Card, D.; Krueger, A. B."
    year: 2000
    type: article
    doi: "10.1257/aer.90.5.1397"
    url: "https://doi.org/10.1257/aer.90.5.1397"
    verified: true
    checked_on: 2026-10-28
    note: "American Economic Review 90(5). Asgari ücret ve istihdam tartışması; aynı zamanda fark-içinde-fark yöntemine klasik örnek."
  - title: "Sosyal Güvenlik Kurumu (resmî site)"
    authors: "SGK"
    year: 2026
    type: web
    url: "https://www.sgk.gov.tr"
    verified: true
    checked_on: 2026-10-28
  - title: "The Economy 2.0"
    authors: "CORE Econ"
    year: 2026
    type: web
    url: "https://www.core-econ.org/the-economy/"
    verified: true
    checked_on: 2026-10-28
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Asgari ücret ve genel ücret artışları, depo, sevkiyat ve saha satış ekibi kalabalık olan distribütörlerin en büyük maliyet kalemini doğrudan etkiler. Bu kart, ücret artışının kârınıza etkisini önceden hesaplamanızı ve artışı fiyat, verimlilik ve kâr arasında nasıl dengeleyeceğinizi planlamanızı sağlar.

## Temel fikir

**İşveren maliyeti**, brüt ücretin üstüne işveren sigorta primleri, işsizlik sigortası işveren payı ve varsa yemek, yol, prim gibi ek ödemelerin eklenmesiyle bulunur. Planlamayı brüt ücretle değil, bu toplamla yapın.

Ücret artışını karşılamanın üç yolu vardır:

1. **Fiyat:** Gereken fiyat artışı = ek personel maliyeti / ciro. Bu oran genellikle ücret artışından çok daha düşüktür, çünkü personel cironun küçük bir kısmıdır. Ama bunu brüt kârla kıyaslamak gerekir.
2. **Verimlilik:** Kişi başı ziyaret, koli veya sipariş sayısını artırmak (rota optimizasyonu, el terminali, depo düzeni).
3. **Kâr:** Hiçbiri yapılmazsa artış doğrudan kârdan çıkar.

**İstihdam etkisi:** Klasik model, asgari ücretin piyasa ücretinin üstüne çıkmasının istihdamı azaltacağını söyler. Card ve Krueger'in New Jersey fast-food çalışması ve ardından gelen tartışmalar (Card ve Krueger, 2000), etkinin her zaman belirgin olmadığını gösterdi. Bulgular ülkeye, sektöre ve artışın büyüklüğüne göre değişir. Yönetici için ders: Ücret artışının etkisini genel teorilerden değil, kendi maliyet yapınızdan hesaplayın.

## Bir örnek

> **Örnek (temsili rakamlar):** Ücret, işveren yükü oranı ve artış oranı gerçek asgari ücret veya prim oranlarını temsil etmez; hesaplar `scripts/cards_numbers_eco_b1.py` ile yapılmıştır.

Bir distribütörde 40 çalışan var, kişi başı brüt ücret 50.000 TL, işveren yükü örnek olarak brüt ücretin %20'si.

- Aylık personel maliyeti: **2.400.000 TL**.
- Aylık ciro 40.000.000 TL, brüt kâr oranı %12: brüt kâr **4.800.000 TL**.
- Personel maliyeti brüt kârın **%50**'sini tüketiyor.

Ücretlerde %30 artış olursa:

- Ek maliyet ayda **720.000 TL**, yılda **8.640.000 TL**.
- Personelin brüt kârdaki payı **%65**'e çıkar.
- Artışı tamamen fiyatla karşılamak için gereken fiyat artışı: **%1,80**.

**Verimlilik alternatifi:** Saha satış temsilcisi günde 25 ziyaret yapıyor. Rota iyileştirmesiyle ziyaret sayısı %10 artıp 27,5'e çıkarsa, 12 temsilcilik ekip aynı müşteri tabanını daha az fazla mesaiyle karşılar veya ek müşteri alır.

## Sık yapılan hatalar

- Bütçeyi yalnızca brüt ücret artışıyla güncellemek; işveren primleri ve ek ödemeleri atlamak.
- Ücret artışını yılın ortasında fark etmek; fiyat güncellemesini zamanında yapmamak.
- Ücret baskısını personel azaltarak çözmeye çalışıp hizmet seviyesini (teslim süresi, sipariş karşılama) bozmak.
- Ücretler arasındaki farkın daralmasını (deneyimli personelle yeni başlayanın ücretinin eşitlenmesi) yönetmemek; bu, deneyimli personeli kaçırır.
- Teşviklerin ve prim desteklerinin koşullarını kontrol etmeden bütçeye yazmak.

## Pratikte nasıl uygulanır?

- [ ] Yıllık bütçede personel maliyetini işveren maliyeti üzerinden ve en az iki ücret artışı senaryosuyla planlayın.
- [ ] Personel maliyetinin brüt kâra oranını aylık olarak izleyin.
- [ ] Ücret artışı açıklandığında gereken fiyat artışını hesaplayın ve üreticiyle marj görüşmesine bu rakamla gidin.
- [ ] Kişi başı ziyaret, koli ve sipariş verimliliği için hedef koyun; verimlilik projelerini artış öncesinde başlatın.
- [ ] Güncel asgari ücret, prim oranları ve teşvikleri SGK ve resmî duyurulardan, gerekiyorsa mali müşavirinizle kontrol edin.

## Daha fazlası

- Card, D.; Krueger, A. B. (2000). *Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania: Reply*. https://doi.org/10.1257/aer.90.5.1397
- SGK (2026). *Sosyal Güvenlik Kurumu (resmî site)*. https://www.sgk.gov.tr
- CORE Econ (2026). *The Economy 2.0*. https://www.core-econ.org/the-economy/
