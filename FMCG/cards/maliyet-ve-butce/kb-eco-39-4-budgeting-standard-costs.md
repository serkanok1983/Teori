---
id: kb-eco-39-4-budgeting-standard-costs
title: "Bütçe ve standart maliyet: Sapmaları okumak"
summary: "Bütçe ve standart maliyet sisteminin nasıl kurulduğunu, gerçekleşen maliyetle standart arasındaki farkın fiyat ve miktar sapmalarına nasıl ayrıldığını ve esnek bütçenin neden gerekli olduğunu anlatır."
course: eco
category: maliyet-ve-butce
tags: [butce, maliyet, performans]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [ECO-39.4]
reading_minutes: 2
key_points:
  - "Standart maliyet, bir birim için beklenen girdi miktarı ve fiyatıdır."
  - "Toplam sapma, fiyat sapması ile miktar sapmasına ayrılır; her biri farklı bir sorumluyu işaret eder."
  - "Esnek bütçe, gerçekleşen hacme göre yeniden hesaplanan bütçedir."
  - "Yüksek enflasyonda standartlar sık güncellenmezse fiyat sapması anlamını yitirir."
glossary_terms: [standart-maliyet, maliyet-sapmasi, esnek-butce]
related: [kb-eco-39-2-product-costing, kb-eco-39-5-relevant-costs-decisions, kb-eco-32-4-finance-in-high-inflation, kb-eco-31-9-three-statement-model]
sources:
  - title: "Principles of Accounting, Volume 2: Managerial Accounting"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-managerial-accounting/pages/1-why-it-matters"
    verified: true
    checked_on: 2026-10-28
  - title: "Cost and Effect: Using Integrated Cost Systems to Drive Profitability and Performance"
    authors: "Kaplan, R. S.; Cooper, R."
    year: 1998
    type: book
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

Ay sonunda maliyetler bütçeyi aşmışsa, nedenini bilmek gerekir: Hammadde mi pahalandı, fire mi arttı, yoksa daha fazla mı ürettiniz? Bu kart, sapmayı bileşenlerine ayırarak doğru kişiye doğru soruyu sormanızı sağlar.

## Temel fikir

**Standart maliyet:** Bir birim ürün için olması gereken girdi miktarı × olması gereken fiyat.

**Sapma analizi:**

- **Fiyat sapması** = (Gerçek fiyat − Standart fiyat) × Gerçek miktar. Genellikle satın almanın sorumluluğundadır.
- **Miktar sapması** = (Gerçek miktar − Gerçekleşen üretim için standart miktar) × Standart fiyat. Genellikle üretimin sorumluluğundadır.

**Esnek bütçe:** Bütçe sabit bir hacme göre yapılır. Gerçekleşen hacim farklıysa, karşılaştırmayı gerçek hacme göre yeniden hesaplanmış bütçeyle yapmak gerekir. Aksi hâlde daha fazla satış yapan bir ay "maliyet aşımı" gibi görünür.

### Bütçe süreci nasıl kurulur?

1. **Satış bütçesi:** Ürün ve kanal bazında hacim ve fiyat varsayımları. Bütün diğer bütçeler bundan türetilir.
2. **Üretim veya satın alma bütçesi:** Satış hacmi, hedef stok seviyesi ve mevcut stok dikkate alınarak.
3. **Gider bütçeleri:** Değişken giderler hacme, sabit giderler kapasiteye bağlı olarak.
4. **Nakit bütçesi:** Tahsilat ve ödeme vadeleriyle birlikte. Kârlı bir bütçe nakit açığı gösterebilir.

### Sapmaları yorumlamak

Bir sapmanın olumlu ya da olumsuz olması tek başına bir şey söylemez. Satın almanın daha ucuz ama düşük kaliteli hammadde alması olumlu fiyat sapması, ama olumsuz miktar sapması (fire) yaratabilir. Bu yüzden sapmaları birlikte yorumlayın ve önemli sapmalar için neden açıklaması isteyin.

### Yüksek enflasyonda bütçe

Enflasyonun yüksek olduğu dönemlerde yıllık sabit fiyatlı bütçe kısa sürede anlamını yitirir. Fiyat varsayımlarını çeyreklik güncelleyen yuvarlanan bütçe veya fiyat sapmasını ayrı izleyip performans değerlendirmesinde miktar sapmasına odaklanmak daha anlamlıdır. Standartları da en az yılda bir, gerekirse daha sık güncelleyin.

## Bir örnek

> **Örnek (temsili rakamlar):** Standartlar ve gerçekleşenler varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b6.py` ile yapılmıştır.

Bir üretici ayda 10.000 adet ürün üretti. Standart: birim başına 2 kg hammadde, kilogramı 30 TL. Gerçekleşen üretim için standart miktar 20.000 kg, standart maliyet 600.000 TL.

Gerçekte 21.000 kg kullanıldı ve kilogramı 33 TL'ye alındı; gerçek maliyet 693.000 TL.

- Fiyat sapması: (33 − 30) × 21.000 = **63.000 TL aleyhte.**
- Miktar sapması: (21.000 − 20.000) × 30 = **30.000 TL aleyhte.**
- Toplam: 93.000 TL aleyhte.

Satın almaya fiyat artışının nedeni, üretime de fazladan kullanılan hammaddenin nedeni sorulmalı: fire, kalite sorunu veya makine ayarı.

## Sık yapılan hatalar

- Toplam sapmayı tek bir rakam olarak raporlayıp bileşenlerine ayırmamak.
- Sabit bütçeyle karşılaştırma yapıp hacim etkisini maliyet aşımı sanmak.
- Ucuz ama kalitesiz hammadde alarak lehte fiyat sapması yaratıp aleyhte miktar sapmasına yol açmak.
- Yüksek enflasyonda standart fiyatları yıl boyu sabit tutmak.

## Pratikte nasıl uygulanır?

- [ ] En büyük beş maliyet kalemi için standart miktar ve fiyat belirleyin.
- [ ] Aylık raporda fiyat ve miktar sapmasını ayrı gösterin ve sorumlusunu yazın.
- [ ] Bütçe karşılaştırmasını esnek bütçeyle yapın.
- [ ] Belirli bir eşiği (ör. %5) aşan sapmalar için kısa bir açıklama isteyin.
- [ ] Enflasyon dönemlerinde standart fiyatları üç ayda bir güncelleyin.

## Daha fazlası

- OpenStax (2026). *Principles of Accounting, Volume 2: Managerial Accounting*. https://openstax.org/books/principles-managerial-accounting/pages/1-why-it-matters
- Kaplan, R. S.; Cooper, R. (1998). *Cost and Effect: Using Integrated Cost Systems to Drive Profitability and Performance*.
