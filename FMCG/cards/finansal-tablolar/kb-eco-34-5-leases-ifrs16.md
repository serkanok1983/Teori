---
id: kb-eco-34-5-leases-ifrs16
title: "Kiralamalar ve TFRS 16: Kira gideri neden bilançoya taşınır?"
summary: "TFRS 16 kapsamında kiracıların depo, araç ve ekipman kiralamalarını kullanım hakkı varlığı ve kira yükümlülüğü olarak bilançoya almasını, gelir tablosunda kira giderinin yerini amortisman ve faizin almasını ve bunun FAVÖK, borç oranları ve banka kovenantları üzerindeki etkisini anlatır."
course: eco
category: finansal-tablolar
tags: [muhasebe, kiralama, tfrs]
roles: [finans-muduru]
level: ileri
source_lessons: [ECO-34.5]
reading_minutes: 3
key_points:
  - "TFRS 16'da kiracı, çoğu kiralamayı kullanım hakkı varlığı ve kira yükümlülüğü olarak bilançoya alır."
  - "Gelir tablosunda kira gideri yerine amortisman ve faiz gideri görünür; ilk dönemlerde toplam gider daha yüksektir."
  - "FAVÖK yükselir, net borç artar; bu, banka kovenantlarını etkileyebilir."
  - "Kısa süreli ve düşük değerli kiralamalar için muafiyetler vardır."
glossary_terms: [kullanim-hakki-varligi, kira-yukumlulugu, favok]
related: [kb-eco-34-3-fixed-assets-depreciation, kb-eco-35-1-reporting-regimes-tr, kb-eco-33-5-balance-sheet, kb-eco-36-4-ratios-profitability-leverage]
sources:
  - title: "IFRS 16 Leases"
    authors: "IFRS Foundation"
    year: 2026
    type: standard
    url: "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/"
    verified: true
    checked_on: 2026-10-28
  - title: "Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu (resmî site)"
    authors: "KGK"
    year: 2026
    type: web
    url: "https://www.kgk.gov.tr"
    verified: true
    checked_on: 2026-10-28
    note: "TFRS/TMS ve BOBİ FRS metinlerinin Türkiye'deki yayımcısı."
  - title: "Principles of Accounting, Volume 1: Financial Accounting"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters"
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

Depo, araç filosu ve forklift kiralamaları, distribütörlerin en büyük sabit giderleri arasındadır. Şirketiniz TFRS'ye göre raporlama yapıyorsa ya da bir TFRS raporlayıcısıyla karşılaştırılıyorsa, bu kiralamaların tablolara yansıması değişir. Bu kart, değişikliği anlamanızı ve bankalarla konuşurken doğru rakamları kullanmanızı sağlar.

## Temel fikir

**Kiracı muhasebesi (TFRS 16):**

- Kiralama başlangıcında gelecekteki kira ödemelerinin bugünkü değeri **kira yükümlülüğü** olarak kaydedilir.
- Aynı tutar (artı bazı doğrudan maliyetler) **kullanım hakkı varlığı** olarak kaydedilir.
- Varlık, kiralama süresi boyunca amortismana tabi tutulur.
- Yükümlülük üzerinden faiz gideri hesaplanır; ödemeler yükümlülüğü azaltır.

**Muafiyetler:** Kısa süreli (12 ay veya daha kısa) ve düşük değerli varlık kiralamalarında, kira gideri doğrusal olarak kaydedilebilir.

**Etkiler:**

- FAVÖK yükselir, çünkü kira gideri yerine amortisman ve faiz görünür.
- Net borç ve borç/özkaynak oranı artar.
- İlk yıllarda faiz yüksek olduğu için toplam gider kira ödemesinden fazladır; ilerleyen yıllarda azalır.
- Nakit akışı değişmez; yalnızca sınıflandırma değişir.

TFRS'nin hangi şirketler için zorunlu olduğu ve vergi kayıtlarında kiralamanın nasıl ele alındığı ayrı konulardır; şirketinizin durumunu mali müşavirinizle netleştirin.

### Kiralama süresini belirlemek

Kira yükümlülüğünün tutarı, kiralama süresine bağlıdır. Süre yalnızca sözleşmedeki ilk dönem değildir; kullanılması makul ölçüde kesin olan uzatma seçenekleri de süreye dahil edilir. Depo kiralarında sözleşmenin bir yıllık olup her yıl yenilenmesi yaygındır; ancak depoya yaptığınız büyük yatırımlar uzun süre kalmayı makul ölçüde kesin kılıyorsa, süre daha uzun belirlenebilir. Bu yargı, borç tutarını önemli ölçüde değiştirir.

### İskonto oranı

Kira ödemelerinin bugünkü değeri, kiralamadaki zımni faiz oranıyla, bu belirlenemiyorsa kiracının alternatif borçlanma faiziyle hesaplanır. Yüksek faiz ortamında iskonto oranı yükümlülüğü belirgin biçimde etkiler.

### Kira artışları

Enflasyona endeksli kira artışları, gerçekleştikçe yükümlülüğün yeniden ölçülmesini gerektirir. Bu yüzden enflasyonun yüksek olduğu dönemlerde kiralama kayıtları sık güncellenir.

### Yönetim için anlamı

Kredi sözleşmelerindeki net borç/FAVÖK gibi taahhütlerin TFRS 16 öncesi mi sonrası tanımla hesaplandığını bankanızla netleştirin. Kirala ya da satın al kararını muhasebe gösterimine göre değil, nakit akışlarına ve esnekliğe göre verin.

## Bir örnek

> **Örnek (temsili rakamlar):** Tutarlar ve iskonto oranı varsayımsaldır; yüksek enflasyon ortamı varsayılmıştır. Hesaplar `scripts/cards_numbers_eco_b4.py` ile yapılmıştır.

Bir distribütör aylık 100.000 TL kirayla 36 aylığına bir depo kiralıyor. Toplam ödeme 3.600.000 TL. Aylık iskonto oranı %3.

- Kira yükümlülüğü ve kullanım hakkı varlığı: **2.183.225 TL.**
- Aylık amortisman: 60.645 TL.
- İlk ay faiz gideri: 65.497 TL.
- İlk ay toplam gider: 126.142 TL; kira ödemesinden 26.142 TL fazla.
- Kiralama süresince toplam faiz gideri: 1.416.775 TL.

FAVÖK'e etkisi: Yıllık 1.200.000 TL kira gideri FAVÖK'ün dışına çıkıyor. Bilançoya ise 2.183.225 TL'lik yeni bir borç ekleniyor.

## Sık yapılan hatalar

- TFRS 16 sonrası FAVÖK artışını performans iyileşmesi sanmak.
- Banka kovenantlarındaki borç tanımının kira yükümlülüklerini içerip içermediğini kontrol etmemek.
- Uzatma opsiyonlarını kiralama süresine dahil edip etmemeyi değerlendirmemek.
- Kira artış maddelerinin (ör. enflasyona endeksli) yükümlülüğe etkisini izlememek.
- TFRS'ye göre raporlayan ve raporlamayan şirketleri düzeltme yapmadan karşılaştırmak.

## Pratikte nasıl uygulanır?

- [ ] Tüm kira sözleşmelerinizi (süre, tutar, artış maddeleri, opsiyonlar) bir listede toplayın.
- [ ] TFRS 16'nın sizin için geçerli olup olmadığını mali müşavirinizle teyit edin.
- [ ] Banka sözleşmelerindeki kovenantların kiralamaları nasıl tanımladığını kontrol edin.
- [ ] Yönetim raporunda FAVÖK'ü kira öncesi ve sonrası olarak iki şekilde gösterin.
- [ ] Yeni kiralama kararlarında satın alma seçeneğiyle karşılaştırma yapın.

## Daha fazlası

- IFRS Foundation (2026). *IFRS 16 Leases*. https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/
- KGK (2026). *Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu (resmî site)*. https://www.kgk.gov.tr
- OpenStax (2026). *Principles of Accounting, Volume 1: Financial Accounting*. https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters
