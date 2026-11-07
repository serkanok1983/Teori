---
id: kb-eco-47-4-ab-testing-significance
title: "A/B testi ve istatistiksel anlamlılık: Fark gerçek mi, şans mı?"
summary: "Kampanya, fiyat veya sayfa tasarımı denemelerinde iki grup arasındaki farkın şanstan kaynaklanıp kaynaklanmadığını p-değeri ile değerlendirmeyi, gereken örneklem büyüklüğünü ve sık yapılan test hatalarını anlatır."
course: eco
category: veri-ve-istatistik
tags: [istatistik, deney, kampanya, e-ticaret]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: ileri
source_lessons: [ECO-47.4]
reading_minutes: 3
key_points:
  - "A/B testinde gruplar rastgele ayrılır; tek fark denenen değişiklik olmalıdır."
  - "p-değeri, gerçekte fark yokken en az bu kadar büyük bir farkın şans eseri görülme olasılığıdır."
  - "Küçük farkları güvenilir biçimde yakalamak için çok büyük örneklem gerekir."
  - "Test süresini ve başarı ölçütünü baştan belirleyin; sonuçlara bakarak testi erken durdurmayın."
glossary_terms: [ab-testi, p-degeri, istatistiksel-anlamlilik, istatistiksel-guc]
related: [kb-eco-47-3-sampling-confidence, kb-eco-48-7-test-vs-control-did, kb-eco-47-1-descriptive-statistics, kb-eco-13-1-heuristics-biases]
sources:
  - title: "Controlled experiments on the web: survey and practical guide"
    authors: "Kohavi, R.; Longbotham, R.; Sommerfield, D.; Henne, R. M."
    year: 2008
    type: article
    doi: "10.1007/s10618-008-0114-1"
    url: "https://doi.org/10.1007/s10618-008-0114-1"
    verified: true
    checked_on: 2026-10-28
    note: "Data Mining and Knowledge Discovery 18(1). Test-kontrol deneylerinde pratik tuzaklar."
  - title: "Introductory Statistics 2e"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/introductory-statistics-2e/pages/1-introduction"
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

B2B sipariş portalında yeni bir tasarım, bayi uygulamasında yeni bir kampanya mesajı veya bir e-ticaret sayfasında farklı bir fiyat gösterimi denediğinizde, "Yeni hâli daha mı iyi?" sorusunu sayılarla yanıtlamanız gerekir. Bu kart, iki grup arasındaki farkın şanstan kaynaklanıp kaynaklanmadığını değerlendirmenizi sağlar. Kohavi ve arkadaşları (2008), çevrimiçi deneylerin pratik kurallarını ayrıntılı biçimde anlatır.

## Temel fikir

**A/B testi:** Kullanıcılar veya müşteriler rastgele iki gruba ayrılır. A grubu mevcut durumu (kontrol), B grubu değişikliği (test) görür.

**p-değeri:** Gerçekte iki grup arasında fark yokken, gözlenen kadar büyük bir farkın şans eseri ortaya çıkma olasılığı. Uygulamada sık kullanılan eşik 0,05'tir.

**İstatistiksel güç:** Gerçekte var olan bir farkı yakalama olasılığı. Genellikle %80 hedeflenir.

**Örneklem büyüklüğü:** Beklenen fark küçüldükçe gereken gözlem sayısı hızla artar. Testi başlatmadan önce hesaplanmalıdır.

### B2B'de A/B testinin zorlukları

Distribütör ve üreticilerde test birimi çoğu zaman tek bir kullanıcı değil, bir bayi, mağaza veya bölgedir. Bu durumda:

- **Gözlem sayısı azdır:** Birkaç yüz bayiyle küçük etkileri yakalamak zordur. Testin süresini uzatmak veya daha büyük etki beklenen değişiklikleri test etmek gerekebilir.
- **Birimler birbirinden farklıdır:** Büyük ve küçük bayileri ayrı gruplarda eşleştirip her grupta rastgele dağıtım yapmak (tabakalı rastgeleleştirme), karşılaştırmayı daha güvenilir kılar.
- **Bulaşma olabilir:** Aynı satış temsilcisi iki gruptaki bayilere de gidiyorsa uygulamalar karışabilir.

### Sık yapılan istatistik hataları

- **Sonucu sürekli kontrol edip anlamlı çıkınca durdurmak:** Bu, şans eseri farkları gerçek sanma olasılığını artırır. Süreyi ve örneklemi baştan belirleyin.
- **Çok sayıda ölçüte bakıp anlamlı çıkanı raporlamak:** Testten önce birincil başarı ölçütünü tek bir ölçüt olarak belirleyin.
- **İstatistiksel anlamlılığı ticari önemle karıştırmak:** Anlamlı ama çok küçük bir fark, uygulama maliyetini karşılamayabilir. Kararı etki büyüklüğü ve maliyetle birlikte verin.

## Bir örnek

> **Örnek (temsili rakamlar):** Ziyaret ve sipariş sayıları varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b7.py` ile yapılmıştır.

Bir distribütör, bayi sipariş portalında yeni bir sepet sayfasını deniyor. Her gruba 5.000 ziyaret düşüyor.

- Kontrol: 200 sipariş, dönüşüm %4,0
- Test: 230 sipariş, dönüşüm %4,6
- Göreli artış: %15

İki oran testinde z = 1,48, p-değeri ≈ 0,14. Eşik 0,05 olduğundan fark **istatistiksel olarak anlamlı değil**; şanstan kaynaklanıyor olabilir.

Bu büyüklükte bir farkı %80 güçle yakalamak için grup başına yaklaşık 17.941 ziyaret gerekirdi. Doğru karar: "Yeni sayfa kötü" değil, "test yetersiz"; testi yeterli süre boyunca sürdürmek.

## Sık yapılan hatalar

- Sonuçlara her gün bakıp anlamlı görünür görünmez testi durdurmak.
- Çok sayıda ölçütü aynı anda test edip anlamlı çıkanı seçmek.
- Grupları rastgele değil, bölge veya müşteri tipine göre ayırmak.
- "Anlamlı değil" sonucunu "fark yok" diye okumak.
- İstatistiksel anlamlılığı ekonomik önemle karıştırmak.

## Pratikte nasıl uygulanır?

- [ ] Testten önce başarı ölçütünü, beklenen etkiyi ve örneklem büyüklüğünü yazın.
- [ ] Grupları rastgele atayın ve gruplar arasında başka fark olmadığını kontrol edin.
- [ ] Testi önceden belirlenen süre dolana kadar sürdürün.
- [ ] Sonucu p-değeri ve güven aralığıyla birlikte raporlayın.
- [ ] Anlamlı sonuçların ekonomik etkisini (ek ciro, ek kâr) ayrıca hesaplayın.

## Daha fazlası

- Kohavi, R.; Longbotham, R.; Sommerfield, D.; Henne, R. M. (2008). *Controlled experiments on the web: survey and practical guide*. https://doi.org/10.1007/s10618-008-0114-1
- OpenStax (2026). *Introductory Statistics 2e*. https://openstax.org/books/introductory-statistics-2e/pages/1-introduction
