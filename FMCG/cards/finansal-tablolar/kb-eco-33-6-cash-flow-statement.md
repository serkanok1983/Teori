---
id: kb-eco-33-6-cash-flow-statement
title: "Nakit akış tablosu: Kâr eden şirketin kasası neden boşalır?"
summary: "Nakit akış tablosunun işletme, yatırım ve finansman faaliyetleri bölümlerini, dolaylı yöntemle net kârdan işletme nakit akışına geçişi ve bir distribütörün büyürken neden nakit tükettiğini anlatır."
course: eco
category: finansal-tablolar
tags: [finansal-tablolar, nakit-akisi, isletme-sermayesi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: temel
source_lessons: [ECO-33.6]
reading_minutes: 3
key_points:
  - "Nakit akış tablosu nakdin nereden geldiğini ve nereye gittiğini üç bölümde gösterir: işletme, yatırım, finansman."
  - "Dolaylı yöntemde net kâra amortisman eklenir, işletme sermayesindeki değişimler düzeltilir."
  - "Alacak ve stok artışı nakit tüketir; tedarikçi borcu artışı nakit sağlar."
  - "Kâr eden ama işletme nakit akışı negatif olan bir şirket, büyümesini borçla finanse ediyordur."
glossary_terms: [nakit-akis-tablosu, isletme-sermayesi, serbest-nakit-akisi]
related: [kb-eco-33-4-income-statement, kb-eco-33-5-balance-sheet, kb-eco-36-6-cash-flow-vs-profit, kb-eco-38-2-cash-conversion-cycle]
sources:
  - title: "IAS 7 Statement of Cash Flows"
    authors: "IFRS Foundation"
    year: 2026
    type: standard
    url: "https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/"
    verified: true
    checked_on: 2026-10-28
  - title: "Principles of Accounting, Volume 1: Financial Accounting"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters"
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

"Kâr ediyoruz ama para yok" cümlesi, dağıtım işinde çok sık duyulur. Nakit akış tablosu bu çelişkiyi açıklar. Bu kart, tabloyu okumanızı ve nakit sorununun kaynağını bulmanızı sağlar.

## Temel fikir

TMS 7 nakit akışlarını üç bölümde sınıflandırır:

1. **İşletme faaliyetleri:** Esas işten doğan nakit. Dolaylı yöntemde net kârdan başlanır:
   - Nakit çıkışı gerektirmeyen giderler (amortisman, karşılıklar) eklenir.
   - Alacak ve stok artışı düşülür (nakit bağlar).
   - Tedarikçi borcu artışı eklenir (nakit sağlar).
2. **Yatırım faaliyetleri:** Araç, depo, ekipman alımları ve satışları.
3. **Finansman faaliyetleri:** Kredi kullanımı ve geri ödemesi, sermaye artışı, kâr payı ödemesi.

Üç bölümün toplamı, dönem başı ve dönem sonu nakit arasındaki farka eşittir. İşletme nakit akışından yatırım harcamaları düşüldüğünde **serbest nakit akışı** bulunur; bu, borç ödemek ve ortaklara dağıtmak için gerçekten kalan paradır.

### Tabloyu nasıl okursunuz?

Üç bölümün işaretlerine birlikte bakmak, şirketin hangi aşamada olduğunu gösterir:

- **İşletme (+), yatırım (−), finansman (−):** Sağlıklı, olgun bir işletme. Esas iş nakit üretiyor; bu nakitle hem yatırım yapılıyor hem borç ödeniyor.
- **İşletme (+), yatırım (−), finansman (+):** Büyüyen işletme. Yatırımlar kısmen borçla finanse ediliyor; borcun geri ödeme planı izlenmeli.
- **İşletme (−), finansman (+):** Esas iş nakit tüketiyor ve açık borçla kapatılıyor. Hızlı büyüyen bir distribütörde geçici olarak görülebilir, ama birkaç dönem sürerse ciddi bir uyarıdır.
- **İşletme (−), yatırım (+):** Şirket faaliyetlerini sürdürmek için varlık satıyor olabilir.

### Distribütör için kritik satırlar

İşletme faaliyetleri bölümündeki **ticari alacak** ve **stok** değişimleri, distribütörlerde çoğu zaman net kârdan daha büyüktür. Kâr artarken işletme nakit akışı azalıyorsa, önce bu iki satıra bakın. Ayrıca faiz ödemelerinin hangi bölümde gösterildiğine dikkat edin; şirketler bu konuda farklı tercihler yapabildiğinden karşılaştırma yaparken dipnotları okuyun.

## Bir örnek

> **Örnek (temsili rakamlar):** Tutarlar varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b4.py` ile yapılmıştır.

Hızla büyüyen bir distribütörün yıllık nakit akışı (TL):

| Kalem | Tutar |
|---|---|
| Net kâr | 3.000.000 |
| Amortisman | 2.000.000 |
| Alacak artışı | -6.000.000 |
| Stok artışı | -4.000.000 |
| Tedarikçi borcu artışı | 3.000.000 |
| **İşletme faaliyetlerinden nakit** | **-2.000.000** |
| Araç ve ekipman alımı | -3.000.000 |
| **Yatırım faaliyetlerinden nakit** | **-3.000.000** |
| Yeni kredi | 6.000.000 |
| Kâr payı ödemesi | -1.000.000 |
| **Finansman faaliyetlerinden nakit** | **5.000.000** |
| **Nakit değişimi** | **0** |

Şirket 3.000.000 TL kâr etmiş, ama işletme faaliyetleri nakit tüketmiş. Büyüme, alacak ve stokta bağlanan parayla finanse edilmiş; açık yeni krediyle kapatılmış. Üstelik borçla finanse edilen bir dönemde kâr payı da dağıtılmış.

## Sık yapılan hatalar

- Yalnızca gelir tablosuna bakıp nakit durumunu varsaymak.
- Büyüme planlarında alacak ve stok artışının nakit ihtiyacını hesaplamamak.
- İşletme nakit akışı negatifken kâr payı dağıtmak.
- Yatırım harcamalarını kısa vadeli kredilerle finanse etmek.
- Faiz ödemelerinin hangi bölümde sınıflandırıldığını kontrol etmeden şirketleri karşılaştırmak (TMS 7 bu konuda seçenek tanır).
- Kredi kullanımıyla artan nakit bakiyesini işletme başarısı sanmak.

## Pratikte nasıl uygulanır?

- [ ] Aylık yönetim raporuna dolaylı yöntemle basit bir nakit akış tablosu ekleyin.
- [ ] Büyüme bütçesini, alacak ve stok artışının nakit etkisiyle birlikte hazırlayın.
- [ ] Serbest nakit akışını izleyin ve kâr payı kararlarını buna göre verin.
- [ ] Uzun ömürlü yatırımları uzun vadeli kaynaklarla finanse edin.
- [ ] İşletme nakit akışı arka arkaya negatifse nedenini (vade, stok, marj) analiz edin.
- [ ] Nakit akış tablosunu aylık yönetim raporunuza ekleyin ve işletme nakit akışını net kârla karşılaştırın.

## Daha fazlası

- IFRS Foundation (2026). *IAS 7 Statement of Cash Flows*. https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/
- OpenStax (2026). *Principles of Accounting, Volume 1: Financial Accounting*. https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters
- Koller, T.; Goedhart, M.; Wessels, D. (McKinsey & Company) (2020). *Valuation: Measuring and Managing the Value of Companies*.
