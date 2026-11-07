---
id: kb-eco-36-6-cash-flow-vs-profit
title: "Nakit ve kâr: Büyüme neden nakit yer?"
summary: "Kâr ile işletme nakit akışı arasındaki farkın kaynaklarını, büyüyen bir distribütörde alacak, stok ve tedarikçi borcu sürelerinin ek işletme sermayesi ihtiyacını nasıl belirlediğini ve büyüme planlarını nakit kapasitesine göre nasıl kuracağınızı anlatır."
course: eco
category: finansal-analiz
tags: [nakit-akisi, isletme-sermayesi, buyume]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [ECO-36.6]
reading_minutes: 3
key_points:
  - "Kâr tahakkuk esasına, nakit ise para hareketine dayanır; ikisi arasındaki fark büyük ölçüde işletme sermayesinden gelir."
  - "Büyüyen bir distribütörde her ek satış, alacak ve stokta ek nakit bağlar."
  - "Düşük marjlı işlerde büyümenin nakit ihtiyacı kârı kolayca aşar."
  - "Sürdürülebilir büyüme hızı, kârın ve finansman kapasitesinin işletme sermayesi ihtiyacını karşılayabildiği hızdır."
glossary_terms: [isletme-sermayesi, nakit-donusum-suresi, serbest-nakit-akisi]
related: [kb-eco-33-6-cash-flow-statement, kb-eco-38-2-cash-conversion-cycle, kb-eco-36-7-earnings-quality-red-flags, kb-eco-31-9-three-statement-model]
sources:
  - title: "Does Working Capital Management Affect Profitability of Belgian Firms?"
    authors: "Deloof, M."
    year: 2003
    type: article
    doi: "10.1111/1468-5957.00008"
    url: "https://doi.org/10.1111/1468-5957.00008"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Business Finance & Accounting 30(3–4)."
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

Satışlarınızı hızla artırdığınız bir yılda banka hesabınız boşalıyorsa, bu bir çelişki değil, dağıtım işinin doğasıdır. Bu kart, büyümenin nakit ihtiyacını önceden hesaplamanızı ve büyümeyi finansman kapasitenize göre planlamanızı sağlar.

## Temel fikir

**Fark nereden gelir?**

- **Alacaklar:** Satış kâra yazılır, ama nakit vade sonunda gelir.
- **Stok:** Satın alınan mal nakit çıkışıdır, ama satılana kadar gider olmaz.
- **Tedarikçi borçları:** Nakit çıkışını geciktirir; bu, farkı kısmen kapatır.
- **Amortisman ve karşılıklar:** Gider olarak yazılır ama nakit çıkışı yaratmaz.

**Büyümenin nakit ihtiyacı:** Ek satış × (Alacak süresi + Stok süresi − Tedarikçi süresi) kadar ek işletme sermayesi gerekir (stok ve tedarikçi süreleri maliyet üzerinden hesaplanır). Deloof (2003) gibi çalışmalar, işletme sermayesi yönetimiyle kârlılık arasında ilişki bulunduğunu göstermiştir.

### Kâr eden şirket neden batabilir?

Şirketler kâr etmediği için değil, vadesi gelen borcu ödeyecek nakdi bulamadığı için batar. Kârlı ama hızla büyüyen bir distribütörde tipik zincir şöyledir: Ciro artar, alacak ve stok daha hızlı artar, açık kısa vadeli krediyle kapatılır, faiz gideri yükselir ve bankalar limitleri daralttığında şirket ödeme güçlüğüne düşer.

### Erken uyarı göstergeleri

- **İşletme nakit akışı ÷ net kâr:** Birkaç dönem boyunca belirgin biçimde birin altında kalıyorsa, kâr nakde dönüşmüyor demektir.
- **Nakit dönüşüm döngüsü:** Gün sayısının uzaması, aynı ciro için daha fazla finansman ihtiyacı anlamına gelir.
- **Kısa vadeli kredinin işletme sermayesine oranı:** Artıyorsa büyüme borçla finanse ediliyor.

### Ne yapabilirsiniz?

Büyüme planını yaparken satış hedefinin yanına işletme sermayesi ihtiyacını ve finansman kaynağını da yazın. Vade uzatma taleplerini, finansman maliyeti dahil kârlılığa göre değerlendirin. Tedarikçi vadelerini uzatmak açığı azaltır, ama tedarikçi ilişkisini ve iskontoları da etkiler; erken ödeme iskontosu çoğu zaman banka faizinden daha değerlidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Tutarlar ve süreler varsayımsaldır; satılan malın maliyeti satışların %85'i kabul edilmiştir. Hesaplar `scripts/cards_numbers_eco_b5.py` ile yapılmıştır.

Bir distribütör satışlarını bir yılda 100.000.000 TL'den 150.000.000 TL'ye çıkarıyor. Net kâr marjı %3; net kâr 4.500.000 TL. Alacak süresi 60 gün, stok süresi 45 gün, tedarikçi süresi 30 gün.

| Kalem | Ek nakit ihtiyacı (TL) |
|---|---|
| Alacak artışı | 8.219.178 |
| Stok artışı | 5.239.726 |
| Tedarikçi borcu artışı | −3.493.151 |
| **Toplam ek işletme sermayesi** | **9.965.753** |

Şirket 4.500.000 TL kâr ediyor, ama büyüme 9.965.753 TL nakit bağlıyor. Aradaki 5.465.753 TL'lik açık, yeni kredi ya da sermayeyle kapatılmak zorunda.

## Sık yapılan hatalar

- Büyüme hedefini nakit ihtiyacını hesaplamadan belirlemek.
- Yeni büyük müşterileri uzun vadeyle kazanıp nakit açığını sonradan fark etmek.
- Kâr ettiği için kâr payı dağıtıp büyümeyi borçla finanse etmek.
- Tedarikçi vadelerini uzatmaya çalışırken tedarikçi ilişkisini ve fiyatı riske atmak.
- Satış ekibini yalnızca ciroyla ödüllendirmek.
- Kâr hedeflerine ulaşan satış ekibine, tahsilat gerçekleşmeden prim ödemek.

## Pratikte nasıl uygulanır?

- [ ] Bütçede her büyüme hedefinin işletme sermayesi ihtiyacını hesaplayın.
- [ ] Yeni müşteri ve kanal kararlarında vade ve stok gereksinimini nakit maliyetiyle değerlendirin.
- [ ] Finansman kapasitenizi (banka limitleri, DBS, faktoring) büyüme planıyla eşleştirin.
- [ ] Satış primlerine tahsilat ve vade kriterleri ekleyin.
- [ ] Aylık olarak kâr ile işletme nakit akışı arasındaki farkı raporlayın.
- [ ] Satış primlerinin bir kısmını tahsilata bağlayın.

## Daha fazlası

- Deloof, M. (2003). *Does Working Capital Management Affect Profitability of Belgian Firms?*. https://doi.org/10.1111/1468-5957.00008
- OpenStax (2026). *Principles of Accounting, Volume 1: Financial Accounting*. https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters
- Koller, T.; Goedhart, M.; Wessels, D. (McKinsey & Company) (2020). *Valuation: Measuring and Managing the Value of Companies*.
