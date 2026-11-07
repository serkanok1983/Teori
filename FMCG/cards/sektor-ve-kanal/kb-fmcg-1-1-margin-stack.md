---
id: kb-fmcg-1-1-margin-stack
title: "Marj zinciri: Raf fiyatındaki pay kime gidiyor, teslimat kârı nasıl eritir?"
summary: "Raf fiyatı, zincirdeki her aşamanın kendi marjını eklemesiyle oluşur. Bu kart adet başı marjın teslimat maliyetiyle nasıl eridiğini ve bağımsız marjların toplam kanal kârını neden düşürebileceğini sayılarla gösterir."
course: fmcg
category: sektor-ve-kanal
tags: [marj, fiyatlama, bayi, kar-orani]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: temel
source_lessons: [FMCG-1.1]
reading_minutes: 4
key_points:
  - "Adet başına brüt kâr ancak teslimat, ziyaret ve vade maliyetleri düşüldükten sonra kâra dönüşür."
  - "Sabit teslimat maliyeti küçük siparişte adet başı kârın büyük kısmını yer; sipariş büyüklüğü kârlılığın ana kaldıracıdır."
  - "Her aşama kendi marjını bağımsız eklediğinde raf fiyatı yükselir, hacim düşer ve kanalın toplam kârı azalabilir (çift marjinalleşme)."
  - "Ticari şartlar ve ortak iş planları, zincirdeki marjları birlikte yönetmenin araçlarıdır."
glossary_terms: [marj, cift-marjinallesme, hizmet-maliyeti, minimum-siparis-buyuklugu]
related: [kb-fmcg-1-1-margin-vs-markup, kb-fmcg-1-3-channel-actors, kb-fmcg-6-3-cost-to-serve, kb-fmcg-10-7-joint-business-planning, kb-fmcg-7-1-distributor-pnl]
sources:
  - title: "Vertical Integration and Antitrust Policy"
    authors: "Spengler, J. J."
    year: 1950
    type: article
    doi: "10.1086/256964"
    url: "https://doi.org/10.1086/256964"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Political Economy 58(4), 347–352."
  - title: "Competitive Advantage: Creating and Sustaining Superior Performance"
    authors: "Porter, M. E."
    year: 1985
    type: book
    verified: false
    note: "Kitap; künye kontrol edilmedi."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Marj yüzdesi kâğıt üzerinde iyi görünse de bayinin cebine kalan para, ürünü markete götürmenin maliyetine bağlıdır. Bu kart iki soruya cevap verir: Adet başı marj, teslimat maliyetinden sonra ne kadar kâr bırakır? Zincirdeki herkes kendi marjını koruduğunda toplam kanal neden kaybeder? Minimum sipariş, rota ve ticari şart kararlarında bu iki soruyu sormanız gerekir.

## Temel fikir

**Marj zinciri**, ürünün üreticiden rafa kadar her el değiştirdiğinde fiyata eklenen marjların toplu görüntüsüdür. Raf fiyatının hesabı marj ile ekleme oranı kartında anlatıldı. Burada iki sonuca odaklanıyoruz.

**1. Marj, kâr değildir.** Bayi bir koli satıp koli başına brüt kâr elde eder. Ama her teslimatın sabite yakın bir maliyeti vardır: araç, şoför, toplama, yükleme ve ziyaret süresi. Bu maliyet siparişin büyüklüğünden pek etkilenmez. Küçük siparişte brüt kârın çoğu teslimata gider. Bu nedenle bayi için kritik rakam yalnızca marj yüzdesi değil, **teslimat başına net katkıdır**. Bu bakışın sistemli hâline **hizmet maliyeti** (*cost-to-serve*) denir.

**2. Bağımsız marjlar kanalı küçültebilir.** Üretici ve perakendeci birbirinden bağımsız fiyat koyduğunda her biri kendi kârını en yükseğe çıkaracak marjı seçer. Sonuçta raf fiyatı, kanal tek elden yönetilseydi seçilecek fiyattan yüksek olur, satış hacmi düşer ve iki tarafın toplam kârı azalır. İktisatta buna **çift marjinalleşme** denir (Spengler, 1950). Sonucun sade anlamı şudur: "Herkes payını korusun" yaklaşımı, pastanın kendisini küçültebilir.

Bu, marjların düşürülmesi gerektiği anlamına gelmez. Hacim artışına bağlı primler, ortak promosyonlar ve ortak iş planları, zincirdeki tarafların fiyatı birlikte düşünmesini sağlayan araçlardır. Porter'ın (1985) değer zinciri fikri de aynı noktaya varır: Değer, halkalar arasındaki ilişkinin nasıl yönetildiğine bağlıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek bir firmaya ait değildir; tüm hesaplar `scripts/cards_numbers_fmcg_b1.py` ile yapılmıştır.

**1. Aynı marj, farklı sipariş büyüklüğü**

Varsayımlar: Bayi adet başına 4,09 TL brüt kâr ediyor, kolide 12 adet var, her teslimatın tam yüklü maliyeti 350 TL.

| Sipariş | Adet | Brüt kâr | Teslimat sonrası |
|---|---|---|---|
| 40 koli | 480 | 1.963,20 TL | 1.613,20 TL |
| 10 koli | 120 | 490,80 TL | 140,80 TL |

Marj yüzdesi aynı kaldığı hâlde büyük sipariş, küçük siparişin yaklaşık **11,5 katı** net katkı bırakıyor. Teslimat maliyetini karşılamak için gereken sipariş 350 ÷ (12 × 4,09) = **7,13 koli**. Bunun altındaki siparişler zarar ettirir.

**2. Çift marjinalleşme**

Varsayımlar: Talep q = 1.000 − 20 × P, üretim maliyeti 10 TL/adet.

- **Tek elden yönetilen kanal:** Kârı en yüksek yapan fiyat 30,00 TL, satış 400 adet, toplam kâr **8.000,00 TL**.
- **Bağımsız üretici ve perakendeci:** Üretici kendi kârını en yükseğe çıkaran 30,00 TL toptan fiyatı seçer. Perakendeci de bunun üzerine kendi marjını koyup rafa 40,00 TL'den çıkarır. Satış 200 adete iner. Perakendeci 2.000,00 TL, üretici 4.000,00 TL kazanır; toplam **6.000,00 TL**.

Fiyat 30 TL'den 40 TL'ye çıkıyor, hacim yarıya iniyor ve kanal 2.000 TL kaybediyor. Tüketici de daha pahalıya alıyor.

## Sık yapılan hatalar

- Marj yüzdesine bakıp küçük siparişlerin de kârlı olduğunu varsaymak.
- Teslimat maliyetini "zaten araç gidiyor" diyerek sıfır saymak; araç, şoför ve zaman bedava değildir.
- Minimum sipariş tutarını maliyet hesabı yapmadan, alışkanlıkla belirlemek.
- Zincirdeki her tarafın kendi marjını ayrı ayrı savunması ve toplam hacmi kimsenin sahiplenmemesi.
- Marj görüşmelerini yalnızca yüzdeyle yapmak; adet ve teslimat başına TL'yi konuşmamak.

## Pratikte nasıl uygulanır?

- [ ] Bayi olarak bir teslimatın tam yüklü maliyetini (araç, yakıt, şoför, toplama, ziyaret süresi) bir kez hesaplayın.
- [ ] Bu maliyeti adet başı brüt kâra bölerek başabaş sipariş büyüklüğünü bulun; minimum sipariş kuralını buna göre gözden geçirin.
- [ ] Müşterilerinizi ortalama sipariş büyüklüğüne göre sıralayın; başabaşın altında kalanlar için ziyaret sıklığını veya teslimat gününü değiştirin.
- [ ] Satış şefleri ve temsilciler için sipariş başına net katkıyı gösteren basit bir rapor hazırlayın.
- [ ] Üretici olarak ticari şartlarınızı, raf fiyatını gereksiz yükselten marj yığılmasını azaltacak biçimde (hacim primleri, ortak promosyon) tasarlayın.
- [ ] Zincir ve bayi görüşmelerinde yüzdelerin yanında toplam kanal hacmini ve kârını da masaya koyun.

## Daha fazlası

- Spengler, J. J. (1950). *Vertical Integration and Antitrust Policy.* Journal of Political Economy 58(4), 347–352. https://doi.org/10.1086/256964
- Porter, M. E. (1985). *Competitive Advantage: Creating and Sustaining Superior Performance.* (kaynak doğrulanmadı)
