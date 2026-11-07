---
id: kb-eco-34-2-receivables-doubtful-debts
title: "Ticari alacaklar ve şüpheli alacaklar: Yaşlandırma ve karşılık"
summary: "Ticari alacakların yaşlandırma tablosuyla izlenmesini, beklenen kredi zararı yaklaşımıyla karşılık ayırmayı, finansal raporlama ile vergi açısından şüpheli alacak koşulları arasındaki farkı ve tahsilat sürecinin karşılık politikasına nasıl bağlanacağını anlatır."
course: eco
category: finansal-tablolar
tags: [muhasebe, alacak-yonetimi, kredi-riski]
roles: [bayi-sahibi, bayi-yonetici, finans-muduru]
level: orta
source_lessons: [ECO-34.2]
reading_minutes: 3
key_points:
  - "Alacak bakiyesinin toplamı değil, yaşına göre dağılımı risk hakkında bilgi verir."
  - "Finansal raporlamada beklenen kredi zararı yaklaşımıyla, alacağın yaşına göre artan oranlarla karşılık ayrılır."
  - "Vergi açısından şüpheli alacak karşılığı belirli koşullara bağlıdır; finansal raporlamadaki karşılıkla aynı olmayabilir."
  - "Karşılık oranları kendi geçmiş tahsilat verilerinize dayanmalıdır."
glossary_terms: [alacak-yaslandirma, beklenen-kredi-zarari, supheli-alacak]
related: [kb-eco-37-3-customer-credit-analysis, kb-eco-38-3-distributor-credit-risk-dbs, kb-eco-38-2-cash-conversion-cycle, kb-ea-20-2-order-to-cash]
sources:
  - title: "IFRS 9 Financial Instruments"
    authors: "IFRS Foundation"
    year: 2026
    type: standard
    url: "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/"
    verified: true
    checked_on: 2026-10-28
  - title: "213 sayılı Vergi Usul Kanunu"
    authors: "T.C. Resmî Gazete / Mevzuat Bilgi Sistemi"
    year: 1961
    type: law
    url: "https://www.mevzuat.gov.tr/MevzuatMetin/1.4.213.pdf"
    verified: true
    checked_on: 2026-10-28
    note: "Mevzuat Bilgi Sistemi resmî PDF metni açıldı, kanun adı ve numarası eşleşti (2026-10-28)."
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

Distribütörlerin bilançosundaki en büyük varlık çoğu zaman ticari alacaklardır. Bu alacakların bir kısmı hiç tahsil edilemeyecekse, kâr ve özkaynak olduğundan yüksek görünür. Bu kart, alacak riskini ölçmenizi ve karşılığı düzenli olarak ayırmanızı sağlar.

## Temel fikir

**Yaşlandırma tablosu:** Alacakları vadesine göre gruplayın: vadesi gelmemiş ya da 0–30 gün, 31–60 gün, 61–90 gün, 90 günden fazla geciken, hukuki takipte olan.

**Beklenen kredi zararı (TFRS 9):** Ticari alacaklar için basitleştirilmiş yaklaşımda, her yaş grubuna geçmiş tahsilat deneyimine ve geleceğe yönelik beklentilere dayanan bir zarar oranı uygulanır. Böylece zarar, gerçekleşmeden önce tahmin edilip kaydedilir.

**Vergi açısından şüpheli alacak:** Vergi Usul Kanunu, şüpheli alacak karşılığının vergi matrahından düşülebilmesini belirli koşullara bağlar (ör. alacağın dava veya icra safhasında olması gibi). Bu nedenle finansal tablolardaki karşılık ile vergi açısından kabul edilen karşılık farklı olabilir. Koşulların güncel uygulamasını mali müşavirinizle teyit edin.

**Değersiz alacak:** Tahsil imkânı kalmadığı kesinleşen alacaklar kayıtlardan çıkarılır; bunun da vergi mevzuatında ayrı koşulları vardır.

### Muhasebe ile vergi neden farklıdır?

Finansal raporlamada karşılık, beklenen kaybı mümkün olduğunca erken yansıtmayı amaçlar. Vergi mevzuatı ise karşılığın vergi matrahından düşülebilmesini belirli koşullara bağlar. Bu nedenle finansal tablolarınızda ayırdığınız karşılığın bir kısmı vergi açısından henüz gider yazılamayabilir. Bu fark, kayıtlarda izlenmeli ve ertelenmiş vergi hesaplarına yansıtılmalıdır.

### Tahsilat süreciyle bağlantı

Karşılık hesaplamak, tahsilat sürecinin yerini tutmaz. Etkili bir süreçte:

- Vadesi geçen alacak için belirli günlerde hatırlatma, ziyaret ve yazılı ihtar adımları tanımlanır.
- Belirli bir gecikmeden sonra yeni sevkiyat durdurulur.
- Hukuki takip kararı, alacağın tutarı ve teminatlar dikkate alınarak verilir.
- Cari hesap mutabakatları dönemsel olarak yapılır; mutabakatsız alacak, ihtilaf durumunda ispatı zorlaştırır.

### Yönetim raporlaması

Yaşlandırma tablosunu yalnızca dönem sonunda değil, aylık olarak satış ekibiyle birlikte gözden geçirin. Satış primlerinin tahsilata bağlanması, vadesi geçen alacakların büyümesini önlemenin etkili yollarından biridir.

## Bir örnek

> **Örnek (temsili rakamlar):** Tutarlar ve zarar oranları varsayımsaldır; kendi tahsilat geçmişinizden hesaplanmalıdır. Hesaplar `scripts/cards_numbers_eco_b4.py` ile yapılmıştır.

| Yaş grubu | Alacak (TL) | Zarar oranı | Karşılık (TL) |
|---|---|---|---|
| 0–30 gün | 30.000.000 | %1 | 300.000 |
| 31–60 gün | 10.000.000 | %3 | 300.000 |
| 61–90 gün | 5.000.000 | %10 | 500.000 |
| 90+ gün | 3.000.000 | %40 | 1.200.000 |
| Hukuki takipte | 1.000.000 | %100 | 1.000.000 |
| **Toplam** | **49.000.000** | | **3.300.000** |

Toplam karşılık alacakların %6,7'sı. Karşılığın büyük kısmı 90 günü geçen ve hukuki takipteki küçük bir alacak grubundan geliyor. Tahsilat çabasını bu gruba yoğunlaştırmak hem nakit hem kâr için en yüksek getiriyi sağlar.

## Sık yapılan hatalar

- Karşılığı yalnızca vergi açısından kabul edilen tutarla sınırlamak; finansal tablolarda riski eksik göstermek.
- Alacakları müşteri bazında değil yalnızca toplamda izlemek.
- Geciken müşteriye sevkiyata devam etmek.
- Karşılık oranlarını geçmiş verilere dayandırmadan belirlemek.
- Tahsil edilemeyeceği belli olan alacakları yıllarca bilançoda tutmak.
- Hukuki takibe geç kalmak; borçlunun diğer alacaklıları önce davranabilir.

## Pratikte nasıl uygulanır?

- [ ] Haftalık yaşlandırma raporu hazırlayın ve satış ekibiyle paylaşın.
- [ ] Geçmiş 2–3 yılın tahsilat verilerinden yaş grubu bazında zarar oranlarınızı hesaplayın.
- [ ] Belirli bir gecikmeyi aşan müşteriler için sevkiyat durdurma kuralı koyun.
- [ ] Hukuki takip kararını belirli bir gecikme ve tutar eşiğine bağlayın.
- [ ] Vergi açısından şüpheli ve değersiz alacak uygulamasını mali müşavirinizle teyit edin.
- [ ] Tahsil edilemeyen alacakların nedenlerini analiz edip kredi politikasına geri bildirim verin.

## Daha fazlası

- IFRS Foundation (2026). *IFRS 9 Financial Instruments*. https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/
- T.C. Resmî Gazete / Mevzuat Bilgi Sistemi (1961). *213 sayılı Vergi Usul Kanunu*. https://www.mevzuat.gov.tr/MevzuatMetin/1.4.213.pdf
- OpenStax (2026). *Principles of Accounting, Volume 1: Financial Accounting*. https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters
