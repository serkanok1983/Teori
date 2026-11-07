---
id: kb-eco-31-10-scenario-sensitivity
title: "Senaryo ve duyarlılık analizi: Bütçe hangi varsayıma en çok bağlı?"
summary: "Bütçe kârının hacim, fiyat, maliyet ve sabit gider varsayımlarındaki küçük değişikliklere ne kadar duyarlı olduğunu tek değişkenli duyarlılık ve birleşik kötü senaryoyla ölçmeyi ve sonuçları karar ve önlem planına bağlamayı anlatır."
course: eco
category: kurumsal-finans
tags: [planlama, risk-yonetimi, finansal-modelleme]
roles: [finans-muduru]
level: ileri
source_lessons: [ECO-31.10, ECO-37.2]
reading_minutes: 3
key_points:
  - "Duyarlılık analizi, bir varsayımı değiştirip diğerlerini sabit tutarak sonucun ne kadar değiştiğini gösterir."
  - "Düşük marjlı işlerde fiyat ve maliyetteki küçük değişimler kârı hacimden çok daha fazla etkiler."
  - "Senaryo analizi, birlikte gerçekleşmesi muhtemel değişiklikleri tek bir tabloda birleştirir."
  - "Her kötü senaryo için önceden belirlenmiş bir önlem listesi olmalıdır."
glossary_terms: [duyarlilik-analizi, senaryo-analizi]
related: [kb-eco-31-9-three-statement-model, kb-eco-32-3-risk-management-stress-test, kb-eco-39-4-budgeting-standard-costs, kb-eco-13-1-heuristics-biases]
sources:
  - title: "Principles of Finance"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-finance/pages/1-why-it-matters"
    verified: true
    checked_on: 2026-10-28
  - title: "Principles of Accounting, Volume 2: Managerial Accounting"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-managerial-accounting/pages/1-why-it-matters"
    verified: true
    checked_on: 2026-10-28
  - title: "Valuation: Measuring and Managing the Value of Companies"
    authors: "Koller, T.; Goedhart, M.; Wessels, D. (McKinsey & Company)"
    year: 2020
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

Bütçe tek bir rakam setine dayanır; gerçekleşme hiçbir zaman tam olarak böyle olmaz. Bu kart, hangi varsayımın kârınızı en çok etkilediğini bulmanızı ve kötü bir senaryoda ne yapacağınızı önceden planlamanızı sağlar.

## Temel fikir

**Duyarlılık analizi** (*sensitivity analysis*): Bir varsayımı (ör. hacim, fiyat, ürün maliyeti, sabit gider) belirli bir oranda değiştirip diğerlerini sabit tutarsınız. Hangi değişkenin sonucu en çok etkilediğini görürsünüz.

**Senaryo analizi** (*scenario analysis*): Gerçekte değişkenler birlikte hareket eder. Ekonomik daralmada hacim düşer, rakipler fiyat kırar, kur maliyetleri artırır. Kötü, temel ve iyi senaryoları tutarlı varsayım setleriyle kurarsınız.

Distribütörlerin ve üreticilerin önemli bir kısmında brüt marj düşük, sabit giderler yüksektir. Bu yapıda:

- Hacimdeki düşüş, katkı payı oranında kârı etkiler.
- Fiyattaki düşüş ise doğrudan kâra yansır; çünkü maliyet aynı kalır.
- Ürün maliyetindeki artış da, satış fiyatına yansıtılamazsa, doğrudan kârdan düşer.

Bu yüzden düşük marjlı işletmelerde %3'lük bir fiyat kaybı %10'luk bir hacim kaybından daha tehlikeli olabilir.

### Senaryoları nasıl kurarsınız?

1. **Kritik değişkenleri belirleyin:** Duyarlılık analizi, sonucu en çok etkileyen birkaç değişkeni gösterir. Senaryolar bu değişkenler üzerine kurulur.
2. **Tutarlı hikâyeler yazın:** Her senaryo bir ekonomik anlatıya dayanmalıdır. Örneğin "kur şoku" senaryosunda ithal ürün maliyeti artar, iç talep daralır ve faizler yükselir.
3. **Nakit ve finansmanı da gösterin:** Senaryolar yalnızca kârı değil, nakit ihtiyacını ve kredi limitlerinin yetip yetmediğini de göstermelidir.
4. **Eylem planı ekleyin:** Kötü senaryo gerçekleşirse hangi giderlerin kısılacağını, hangi yatırımların erteleneceğini önceden belirleyin.

### Başabaş analizi

Duyarlılık analizinin pratik bir biçimi, kritik değişkenin hangi değerde kârın sıfırlandığını bulmaktır. "Fiyat ne kadar düşerse zarar ederiz?" veya "hacim ne kadar düşerse nakit açığı oluşur?" sorularının cevabı, yönetimin risk iştahını tartışmasını kolaylaştırır.

### Sık rastlanan tuzak

Senaryoları yalnızca yıllık bütçe döneminde hazırlamak. Ekonomik koşullar hızla değiştiğinde senaryoları çeyreklik güncellemek ve gerçekleşmeyi hangi senaryoya yakın olduğuna göre izlemek daha değerlidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Ciro, marj ve gider tutarları varsayımsaldır. Değişkenler birbirinden bağımsız ele alınmıştır. Hesaplar `scripts/cards_numbers_eco_b3.py` ile yapılmıştır.

Bir distribütörün bütçesi: ciro 200.000.000 TL, brüt marj %20, sabit gider 30.000.000 TL. Faaliyet kârı **10.000.000 TL**.

| Değişiklik (diğerleri sabit) | Faaliyet kârı (TL) | Bütçeye göre |
|---|---|---|
| Hacim −%10 | 6.000.000 | −%40 |
| Satış fiyatı −%3 | 4.000.000 | −%60 |
| Ürün maliyeti +%5 (fiyata yansıtılamaz) | 2.000.000 | −%80 |
| Sabit gider +%10 | 7.000.000 | −%30 |

Fiyattaki %3'lük kayıp, hacimdeki %10'luk kayıptan daha fazla zarar veriyor. Dört değişikliğin birlikte gerçekleştiği kötü senaryoda faaliyet sonucu **−9.600.000 TL**.

## Sık yapılan hatalar

- Yalnızca hacim senaryosu kurup fiyat ve maliyet değişimlerini göz ardı etmek.
- İyi ve kötü senaryoları gerçekçi olmayan dar aralıklarla (±%2) kurmak.
- Senaryoları hazırlayıp önlem planına bağlamamak.
- Kötü senaryoyu "olmayacak" diye yönetime sunmaktan kaçınmak.
- Nakit etkisini (alacak, stok) senaryolara dahil etmemek.

## Pratikte nasıl uygulanır?

- [ ] Bütçenin en kritik 4–6 varsayımını belirleyin ve her biri için duyarlılık tablosu hazırlayın.
- [ ] Kötü, temel ve iyi senaryoları tutarlı varsayım setleriyle kurun.
- [ ] Her senaryonun kâr, nakit ve kredi ihtiyacı etkisini gösterin.
- [ ] Kötü senaryo için tetikleyici göstergeler ve önlem listesi belirleyin.
- [ ] Senaryoları her çeyrek gerçekleşen verilerle güncelleyin.

## Daha fazlası

- OpenStax (2026). *Principles of Finance*. https://openstax.org/books/principles-finance/pages/1-why-it-matters
- OpenStax (2026). *Principles of Accounting, Volume 2: Managerial Accounting*. https://openstax.org/books/principles-managerial-accounting/pages/1-why-it-matters
- Koller, T.; Goedhart, M.; Wessels, D. (McKinsey & Company) (2020). *Valuation: Measuring and Managing the Value of Companies*.
