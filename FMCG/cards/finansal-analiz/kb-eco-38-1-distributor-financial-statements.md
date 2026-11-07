---
id: kb-eco-38-1-distributor-financial-statements
title: "Distribütör finansal tabloları: İnce marjlı bir işi doğru okumak"
summary: "Bir distribütörün finansal tablolarını üreticiden ayıran özellikleri, brüt marj, faaliyet gideri oranı, alacak, stok ve tedarikçi süreleri, nakit dönüşüm süresi ve kullanılan sermaye getirisi üzerinden iki distribütörü karşılaştırarak ve yönetim için temel göstergeleri seçerek anlatır."
course: eco
category: finansal-analiz
tags: [finansal-analiz, distributor, isletme-sermayesi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, finans-muduru]
level: temel
source_lessons: [ECO-38.1]
reading_minutes: 3
key_points:
  - "Distribütörlerde marjlar düşük, işletme sermayesi büyük; değer, sermayenin ne kadar hızlı döndüğüyle yaratılır."
  - "Daha yüksek brüt marj, daha yüksek sermaye getirisi anlamına gelmeyebilir."
  - "Nakit dönüşüm döngüsü ve kullanılan sermaye getirisi, brüt marjla birlikte okunmalıdır."
  - "Tedarikçi primleri ve ciro primleri marjın önemli bir kısmını oluşturabilir; muhasebeleştirme şekli tabloları değiştirir."
glossary_terms: [nakit-donusum-suresi, roce, brut-kar]
related: [kb-eco-38-2-cash-conversion-cycle, kb-eco-38-3-distributor-credit-risk-dbs, kb-eco-36-5-dupont, kb-eco-33-4-income-statement]
sources:
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
  - title: "Does Working Capital Management Affect Profitability of Belgian Firms?"
    authors: "Deloof, M."
    year: 2003
    type: article
    doi: "10.1111/1468-5957.00008"
    url: "https://doi.org/10.1111/1468-5957.00008"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Business Finance & Accounting 30(3–4)."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Distribütörlerin finansal tabloları, üretici veya perakendeci tablolarından farklı okunmalıdır. Bu kart, iki distribütörü karşılaştırarak hangi göstergenin neyi anlattığını ve yönetimin hangi göstergelere odaklanması gerektiğini gösterir.

## Temel fikir

**Distribütör tablolarının özellikleri:**

- **Gelir tablosu:** Yüksek ciro, düşük brüt marj. Tedarikçi primleri, ciro primleri ve iskontolar marjın önemli bir kısmını oluşturur.
- **Faaliyet giderleri:** Depo, lojistik, satış ekibi ve araç giderleri ağırlıklıdır; ciroya oranı yakından izlenmelidir.
- **Bilanço:** Varlıkların çoğu alacak ve stoktur; duran varlıklar görece küçüktür.
- **Finansman:** Tedarikçi kredisi ve kısa vadeli banka kredileri ağırlıklıdır.

**Temel göstergeler:**

1. Brüt marj ve faaliyet gideri oranı.
2. Alacak (DSO), stok (DIO) ve tedarikçi (DPO) süreleri, nakit dönüşüm süresi.
3. Kullanılan sermaye getirisi (ROCE).

### Tedarikçi primleri neden önemlidir?

Distribütörlerde ciro primi, raf ve listeleme destekleri, hedef primleri gibi tedarikçiden gelen tutarlar, brüt kârın önemli bir kısmını oluşturabilir. Bu tutarlar:

- Genellikle dönem sonunda ve hedef gerçekleşmesine bağlı olarak kesinleşir. Yıl içi aylık raporlarda tahakkuk edilmezse aylar arasında kâr dalgalanır.
- Satış maliyetinden indirim olarak mı yoksa ayrı bir gelir olarak mı gösterildiklerine göre brüt marj farklı görünür. Karşılaştırma yaparken aynı yöntemi kullanın.
- Tahsilatı gecikebilir; tedarikçiden alacak olarak bilançoda bekler.

### Ciroya oranla düşünmek

Distribütörün bütün gider kalemlerini ciroya oranla izlemek pratik bir yöntemdir: depo gideri, lojistik gideri, satış ekibi gideri ve finansman gideri. Bu oranları bölgeler, kanallar ve yıllar arasında karşılaştırın. Brüt marj sabitken bir gider oranının yükselmesi, verimlilik kaybının ilk işaretidir.

### Yüksek enflasyonda

Stok, enflasyonda değer kazanır ve satış maliyeti düşük görünebilir; brüt marj iyi görünür ama stok yenileme maliyeti daha yüksektir. Bu yüzden marjı, yenileme maliyetiyle de kontrol edin.

## Bir örnek

> **Örnek (temsili rakamlar):** İki distribütörün rakamları varsayımsaldır ve aynı ciroya sahip oldukları kabul edilmiştir. Hesaplar `scripts/cards_numbers_eco_b5.py` ile yapılmıştır.

| Gösterge | Distribütör A | Distribütör B |
|---|---|---|
| Brüt marj | %18,0 | %15,0 |
| Faaliyet gideri / satış | %13,0 | %11,0 |
| Faaliyet kârı marjı | %5,0 | %4,0 |
| Alacak süresi (gün) | 73 | 46 |
| Stok süresi (gün) | 56 | 39 |
| Tedarikçi süresi (gün) | 67 | 60 |
| Nakit dönüşüm döngüsü (gün) | 62 | 24 |
| ROCE | %16,7 | %20,0 |

A'nın brüt marjı ve faaliyet kârı marjı daha yüksek. Ama A, müşterilerine uzun vade veriyor ve daha fazla stok taşıyor; nakit dönüşüm süresi B'nin iki katından fazla. B daha az sermayeyle çalıştığı için sermaye getirisi daha yüksek.

Yorum: A yüksek marjı, uzun vade ve geniş stokla "satın alıyor" olabilir. Hangisinin daha iyi olduğu, A'nın ek marjının bağladığı ek sermayenin maliyetini karşılayıp karşılamadığına bağlıdır.

## Sık yapılan hatalar

- Distribütörleri yalnızca brüt marjla karşılaştırmak.
- Tedarikçi primlerinin maliyetten mi düşüldüğünü yoksa ayrı gelir olarak mı gösterildiğini kontrol etmemek.
- Faaliyet giderlerini ciroya oranlamadan izlemek.
- Nakit dönüşüm döngüsünü yıl sonu bakiyelerine göre hesaplayıp mevsimselliği göz ardı etmek.
- Sermaye maliyetini hesaba katmadan "kârlı büyüme" hedeflemek.
- Ciro artışını başarı ölçütü olarak tek başına kullanmak.

## Pratikte nasıl uygulanır?

- [ ] Aylık yönetim raporunda yukarıdaki sekiz göstergeyi bir tabloda izleyin.
- [ ] Müşteri, kanal ve tedarikçi bazında brüt marj ile nakit dönüşüm süresini birlikte raporlayın.
- [ ] Tedarikçi primlerinin muhasebeleştirilmesini mali müşavirinizle netleştirin.
- [ ] Ticari kararlarda (vade, stok, yeni marka) ROCE etkisini hesaplayın.
- [ ] Göstergeleri, mümkünse yayımlanmış distribütör tablolarıyla karşılaştırın.
- [ ] Aylık raporda brüt marj, gider oranları ve nakit dönüşüm süresini birlikte gösterin.

## Daha fazlası

- OpenStax (2026). *Principles of Accounting, Volume 1: Financial Accounting*. https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters
- Koller, T.; Goedhart, M.; Wessels, D. (McKinsey & Company) (2020). *Valuation: Measuring and Managing the Value of Companies*.
- Deloof, M. (2003). *Does Working Capital Management Affect Profitability of Belgian Firms?*. https://doi.org/10.1111/1468-5957.00008
