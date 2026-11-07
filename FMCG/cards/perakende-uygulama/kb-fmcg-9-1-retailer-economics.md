---
id: kb-fmcg-9-1-retailer-economics
title: "Perakendecinin ekonomisi: Marj, devir hızı ve raf verimliliği"
summary: "Perakendeci bir kategoriye ya da ürüne yalnızca marjına göre değil, stok devir hızına ve raf alanının verimliliğine göre de bakar. Bu kart perakendecinin kâr yapısını, ön ve arka marjı, stok yatırımının brüt kâr getirisini ve üreticinin bunu satış görüşmesinde nasıl kullanacağını anlatır."
course: fmcg
category: perakende-uygulama
tags: [perakende, finans, kilit-musteri]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: temel
source_lessons: [FMCG-9.1]
reading_minutes: 3
key_points:
  - "Perakendecinin kârı ön marj, arka marj ve faaliyet giderleri arasındaki küçük bir farktır."
  - "Düşük marjlı ama hızlı dönen bir ürün, yüksek marjlı ama yavaş dönen bir üründen daha fazla getiri sağlayabilir."
  - "Stok yatırımının brüt kâr getirisi, marj ile devir hızını tek göstergede birleştirir."
  - "Raf alanı kıt olduğu için perakendeci metrekare ya da raf metresi başına kârı da izler."
  - "Üreticinin önerisi, perakendecinin bu göstergelerine etkisiyle anlatıldığında daha ikna edicidir."
glossary_terms: [gmroi, arka-marj, ciro-primi, stok-gun-sayisi]
related: [kb-fmcg-9-2-formats-private-label, kb-fmcg-9-3-shelf-space-planogram, kb-fmcg-10-2-trade-terms, kb-fmcg-10-6-category-management, kb-fmcg-1-1-margin-stack]
sources:
  - title: "An Empirical Analysis of the Determinants of Retail Margins: The Role of Store-Brand Share"
    authors: "Ailawadi, K. L.; Harlam, B."
    year: 2004
    type: article
    doi: "10.1509/jmkg.68.1.147.24027"
    url: "https://doi.org/10.1509/jmkg.68.1.147.24027"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Marketing 68(1), 147–165."
  - title: "Category Management Association"
    authors: "Category Management Association"
    year: 2026
    type: web
    url: "https://www.categorymanagement.org/"
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

Üreticinin satış ekibi genellikle kendi ürününün satış hacmini ve marjını anlatır. Zincirin kategori yöneticisi ise başka sorular sorar: Bu ürün rafta ne kadar yer kaplıyor, stokta ne kadar kalıyor, metre başına ne kazandırıyor? Bu kart, perakendecinin bakış açısını ve göstergelerini anlamanızı sağlar.

## Temel fikir

**Perakendecinin kâr yapısı.**

- **Ön marj:** Raf satış fiyatı ile fatura üzerindeki alış fiyatı arasındaki fark.
- **Arka marj:** Faturada görünmeyen gelirler: ciro primleri, listeleme ücretleri, teşhir ve promosyon katkıları. Bazı pazarlarda arka marj, perakendecinin kârının önemli bir kısmını oluşturur.
- **Faaliyet giderleri:** Personel, kira, enerji, lojistik, fire.

Fark genellikle satışın birkaç yüzdesi kadardır. Bu nedenle perakendeci, küçük marj değişikliklerine çok duyarlıdır.

**Mağaza markası ve marj.** Ailawadi ve Harlam (2004), mağaza markası payı yüksek olan perakendecilerin bu ürünlerden yüzde olarak daha yüksek marj elde ettiğini, ancak birim başına kazancın her zaman daha yüksek olmadığını gösterdi. Bu bulgu, perakendecinin hem yüzde marja hem de lira olarak kazanca baktığını hatırlatır.

**Devir hızı.** Stok devir hızı = yıllık satılan malın maliyeti / ortalama stok değeri. Hızlı dönen bir ürün, perakendecinin daha az sermaye bağlamasını sağlar.

**Stok yatırımının brüt kâr getirisi** (GMROI) = yıllık brüt kâr / maliyet üzerinden ortalama stok değeri. Bu gösterge, marj ile devir hızını birleştirir: "Stoka bağladığım her lira yılda kaç lira brüt kâr getiriyor?"

**Raf verimliliği.** Raf alanı sınırlıdır. Perakendeci, raf metresi ya da yüz başına satış ve kârı izler. Bir ürünün rafta kalması, aynı alanı kullanabilecek başka bir üründen daha fazla kazandırmasına bağlıdır.

**Kategori bakışı.** Kategori yönetimi yaklaşımında perakendeci tek tek ürünlere değil, kategorinin toplam satış ve kârına bakar (Category Management Association kaynakları bu bakışı anlatır). Bir ürünün eklenmesi, kategorinin toplamını artırıyorsa değerlidir; yalnızca başka ürünlerden satış çalıyorsa değildir.

## Bir örnek

> **Örnek (temsili rakamlar):** Marjlar, devir hızları ve satış tutarı varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b5.py` ile yapılmıştır.

Bir perakendecinin kâr yapısı, satışa oranla: ön marj %24, arka marj %4, faaliyet giderleri %22. Faaliyet kârı: **%6**. Arka marjdaki bir puanlık kayıp, kârın altıda birine denk gelir.

Aynı perakendecide yıllık satışı 1.000.000 TL olan iki kategori:

| | Kategori A | Kategori B |
|---|---|---|
| Brüt marj | %30 | %18 |
| Brüt kâr | 300.000 TL | 180.000 TL |
| Yıllık stok devir hızı | 6 | 14 |
| Ortalama stok (maliyet) | 116.667 TL | 58.571 TL |
| **GMROI** | **2,57** | **3,07** |

Kategori A'nın marjı çok daha yüksek, ama stoka bağlanan her lira için B daha fazla brüt kâr getiriyor. B kategorisinde ürün satan bir üretici, düşük marjı savunmak yerine bu getiriyi anlatabilir: "Ürünümüz rafta hızlı dönüyor; stoka bağladığınız sermaye için kategorideki en iyi getirilerden birini sağlıyor."

## Sık yapılan hatalar

- **Yalnızca yüzde marjı konuşmak.** Perakendeci lira olarak kazanca ve devir hızına da bakar.
- **Arka marjı görmezden gelmek.** Fatura dışı koşullar, perakendecinin kâr hesabının önemli bir parçasıdır.
- **Kategori yerine ürünü savunmak.** Ürününüzün kategoriye katkısını gösteremiyorsanız raf kaybedebilirsiniz.
- **Raf alanını bedava saymak.** Her yüz, başka bir ürünün alabileceği bir alandır.
- **Perakendecinin giderlerini bilmemek.** Teşhir ya da sık teslimat talebiniz perakendeciye de maliyet yaratır.

## Pratikte nasıl uygulanır?

- [ ] Ana müşterilerinizin kategorinizdeki marj, devir hızı ve raf payı verilerini öğrenmeye çalışın.
- [ ] Ürünleriniz için GMROI ve raf metresi başına kâr tahmini hazırlayın.
- [ ] Listeleme ve raf görüşmelerinde, önerinizin kategorinin toplam kârına etkisini gösterin.
- [ ] Ticari koşul pazarlığında ön ve arka marjın toplam etkisini birlikte hesaplayın.
- [ ] Satış ekibinize perakendecinin göstergelerini anlatan kısa bir eğitim verin.

## Daha fazlası

- Ailawadi, K. L.; Harlam, B. (2004). *An Empirical Analysis of the Determinants of Retail Margins: The Role of Store-Brand Share.* Journal of Marketing 68(1), 147–165. https://doi.org/10.1509/jmkg.68.1.147.24027
- Category Management Association (2026). *Category Management Association.* https://www.categorymanagement.org/
