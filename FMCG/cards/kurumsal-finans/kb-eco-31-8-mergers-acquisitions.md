---
id: kb-eco-31-8-mergers-acquisitions
title: "Satın alma ve birleşme: Bir distribütörü almak için en fazla ne ödemeli?"
summary: "Hedef şirketin tek başına değerine sinerjilerin bugünkü değerini ekleyip entegrasyon maliyetlerini düşerek azami fiyatı hesaplamayı, sinerjilerin neden çoğu zaman abartıldığını ve durum tespiti sürecinde nelere bakılacağını anlatır."
course: eco
category: kurumsal-finans
tags: [birlesme-satin-alma, degerleme, kurumsal-finans]
roles: [uretici-sahibi, bayi-sahibi]
level: ileri
source_lessons: [ECO-31.8]
reading_minutes: 3
key_points:
  - "Azami fiyat = hedefin tek başına değeri + sinerjilerin bugünkü değeri − entegrasyon maliyetleri."
  - "Sinerjinin tamamını fiyat olarak satıcıya öderseniz, satın alma size değer yaratmaz."
  - "Maliyet sinerjileri gelir sinerjilerinden daha gerçekçidir; gelir sinerjisine daha temkinli yaklaşın."
  - "Durum tespiti finansal, vergi, hukuki ve ticari boyutları birlikte kapsamalıdır."
glossary_terms: [sinerji, durum-tespiti, firma-degeri]
related: [kb-eco-26-4-business-valuation-basics, kb-eco-7-5-auctions-tenders, kb-eco-31-5-agency-governance-family-firm, kb-eco-13-1-heuristics-biases]
sources:
  - title: "New Evidence and Perspectives on Mergers"
    authors: "Andrade, G.; Mitchell, M.; Stafford, E."
    year: 2001
    type: article
    doi: "10.1257/jep.15.2.103"
    url: "https://doi.org/10.1257/jep.15.2.103"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Economic Perspectives 15(2)."
  - title: "Valuation: Measuring and Managing the Value of Companies"
    authors: "Koller, T.; Goedhart, M.; Wessels, D. (McKinsey & Company)"
    year: 2020
    type: book
    verified: true
    checked_on: 2026-10-28
  - title: "Rekabet Kurumu (resmî site)"
    authors: "Rekabet Kurumu"
    year: 2026
    type: web
    url: "https://www.rekabet.gov.tr"
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

Distribütör konsolidasyonu sık görülür: Bir bölge distribütörü komşu bölgeyi satın alır, bir üretici kendi dağıtımını kurmak için bir distribütörü devralır. Bu kart, satın alma fiyatını mantıklı bir üst sınırda tutmanızı ve sık yapılan hatalardan kaçınmanızı sağlar.

## Temel fikir

**Tek başına değer:** Hedef şirketin, mevcut yönetimiyle ve sizin müdahaleniz olmadan sahip olduğu değer.

**Sinerji:** Birleşme sonrası ortaya çıkan ek değer. Distribütörlerde tipik sinerjiler: ortak depo ve araç kullanımı, rota optimizasyonu, genel giderlerin birleştirilmesi, satın alma gücü. Gelir sinerjileri (çapraz satış, yeni marka) daha belirsizdir.

**Entegrasyon maliyetleri:** Sistem geçişi, kıdem tazminatı ödemeleri, depo taşıma, marka değişikliği, yönetim zamanı.

Azami fiyat = tek başına değer + sinerjilerin bugünkü değeri − entegrasyon maliyetleri

Andrade, Mitchell ve Stafford (2001), birleşmelerde kazancın büyük kısmının hedef şirket ortaklarına gittiğini, satın alan şirket ortaklarının getirisinin ise sınırlı olduğunu gösterdi. Bunun bir nedeni rekabetçi teklif süreçleri ve iyimser sinerji tahminleridir (bkz. kazananın laneti).

Belirli büyüklük eşiklerini aşan birleşme ve devralmalar, Rekabet Kurumu iznine tabi olabilir; bunu işlem takvimine erkenden dahil edin.

### Satın alma sürecinin adımları

1. **Hedef belirleme:** Stratejik uyum, bölge, ürün yelpazesi ve tedarikçi portföyü.
2. **Ön değerlendirme:** Gizlilik sözleşmesi imzalanır, özet finansal bilgiler incelenir.
3. **Niyet mektubu:** Fiyat aralığı, yapı ve özel inceleme süresi belirlenir.
4. **Özel inceleme (due diligence):** Finansal, vergi, hukuki, SGK, ticari ve operasyonel inceleme. Distribütörlerde alacakların tahsil edilebilirliği, stok kalitesi, tedarikçi sözleşmelerinin devredilebilirliği ve kilit çalışanlar öne çıkar.
5. **Sözleşme:** Fiyat ayarlamaları, beyan ve tekeffüller, tazminat hükümleri.
6. **Entegrasyon:** İlk gün planı, sistem ve süreç birleştirme.

### Distribütörlerde özel riskler

- **Tedarikçi onayı:** Distribütörlük sözleşmeleri çoğu zaman kontrol değişikliğinde tedarikçinin onayını veya fesih hakkını öngörür. Onay alınamazsa satın alınan değerin büyük kısmı kaybolabilir.
- **Müşteri kaybı:** Birleşme sonrası müşterilerin bir kısmı rakiplere geçebilir.
- **Gizli yükümlülükler:** Vergi, SGK ve kıdem tazminatı yükümlülükleri; bunlara karşı satıcıdan teminat veya fiyat düşümü isteyin.

Varlık alımı ile hisse alımı arasındaki tercih, vergi ve yükümlülük devri açısından farklı sonuçlar doğurur; bu kararı avukatınız ve vergi danışmanınızla birlikte verin.

## Bir örnek

> **Örnek (temsili rakamlar):** Değer, sinerji ve maliyet tutarları varsayımsaldır. Sinerjilerin kalıcı ve sabit olduğu varsayılmıştır. Hesaplar `scripts/cards_numbers_eco_b3.py` ile yapılmıştır.

Bir distribütör, komşu bölgedeki bir distribütörü almayı düşünüyor.

- Hedefin tek başına değeri: 50.000.000 TL.
- Beklenen yıllık maliyet sinerjisi: 3.000.000 TL. %30 iskonto oranıyla bugünkü değeri 10.000.000 TL.
- Entegrasyon maliyeti: 5.000.000 TL.
- **Azami fiyat: 55.000.000 TL.**

Satıcı 60.000.000 TL istiyor (hedefin FAVÖK'ü 10.000.000 TL; yani 6,0 kat). Bu fiyatla alıcı **5.000.000 TL** değer kaybeder. Sinerjinin yalnızca yarısı gerçekleşirse azami fiyat 50.000.000 TL'ye iner; bu da hedefin tek başına değerine eşittir.

## Sık yapılan hatalar

- Sinerjinin tamamını fiyata ekleyip satıcıya vermek.
- Entegrasyon maliyetlerini ve süresini küçük görmek.
- Müşteri ve çalışan kaybını hesaba katmamak.
- Üreticinin onayını almadan bir distribütörlük bölgesini devralmayı varsaymak.
- Durum tespitinde vergi, SGK ve dava risklerini incelememek.

## Pratikte nasıl uygulanır?

- [ ] Teklif vermeden önce azami fiyatı hesaplayın ve yazılı hâle getirin.
- [ ] Sinerjileri maliyet ve gelir olarak ayırın; her biri için sorumlu ve zaman çizelgesi belirleyin.
- [ ] Durum tespitinde finansal tablolar, alacak kalitesi, stok, vergi, SGK, sözleşmeler ve davaları inceleyin.
- [ ] Üretici sözleşmelerinin devri ve bölge haklarını yazılı olarak teyit edin.
- [ ] Rekabet Kurumu bildirimi, vergi ve hukuki konular için uzman danışmanlarla çalışın.

## Daha fazlası

- Andrade, G.; Mitchell, M.; Stafford, E. (2001). *New Evidence and Perspectives on Mergers*. https://doi.org/10.1257/jep.15.2.103
- Koller, T.; Goedhart, M.; Wessels, D. (McKinsey & Company) (2020). *Valuation: Measuring and Managing the Value of Companies*.
- Rekabet Kurumu (2026). *Rekabet Kurumu (resmî site)*. https://www.rekabet.gov.tr
