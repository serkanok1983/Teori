---
id: kb-fmcg-9-4-osa-out-of-stock
title: "Raf bulunurluğu ve stoksuzluk"
summary: "Ürün rafta yoksa satılamaz. Bu kart stoksuzluğun boyutunu, tüketicinin nasıl tepki verdiğini, kaybın üretici ile perakendeci arasında nasıl paylaştığını ve stoksuzluğun nedenlerine göre nasıl azaltılacağını anlatır."
course: fmcg
category: perakende-uygulama
tags: [perakende, raf, tedarik-zinciri]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, saha-satis-temsilcisi, depo-lojistik-muduru]
level: temel
source_lessons: [FMCG-9.4]
reading_minutes: 3
key_points:
  - "Stoksuzluk, tüketicinin aradığı ürünü rafta bulamamasıdır; depoda stok olması ürünün rafta olduğu anlamına gelmez."
  - "Büyük bir çalışmada dünya ortalaması yaklaşık %8,3 bulundu; promosyondaki ürünlerde oran genellikle daha yüksektir."
  - "Tüketiciler stoksuzlukta mağaza değiştirir, marka değiştirir, aynı markanın başka ürününü alır, alımı erteler ya da hiç almaz."
  - "Nedenlerin büyük kısmı mağaza düzeyindedir: sipariş ve tahmin hataları ile raf dolumu."
  - "Kaybın bir kısmını üretici, bir kısmını perakendeci yaşar; bu ortak bir sorundur."
glossary_terms: [stoksuzluk, raf-bulunurlugu, siparis-karsilama-orani]
related: [kb-fmcg-9-3-shelf-space-planogram, kb-fmcg-9-5-perfect-store, kb-fmcg-11-4-safety-stock, kb-fmcg-11-9-vmi-cpfr, kb-fmcg-11-2-demand-forecasting]
sources:
  - title: "Desperately Seeking Shelf Availability: An Examination of the Extent, the Causes, and the Efforts to Address Retail Out-of-Stocks"
    authors: "Corsten, D.; Gruen, T."
    year: 2003
    type: article
    doi: "10.1108/09590550310507731"
    url: "https://doi.org/10.1108/09590550310507731"
    verified: true
    checked_on: 2026-10-28
    note: "International Journal of Retail & Distribution Management 31(12), 605–617."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Üreticinin fabrikasında ve dağıtıcının deposunda stok olabilir, ama tüketici rafın önünde ürünü bulamıyorsa satış kaybedilir. Bu kart, stoksuzluğun maliyetini hesaplamanızı ve nedenine göre doğru çözümü seçmenizi sağlar.

## Temel fikir

**Raf bulunurluğu** (*on-shelf availability*, OSA), tüketicinin aradığı anda ürünün rafta satışa hazır olmasıdır. **Stoksuzluk** (*out-of-stock*, OOS) bunun tersidir.

**Boyut.** Gruen, Corsten ve Bharadwaj'ın sanayi kuruluşları için hazırladığı geniş kapsamlı çalışma (2002), dünya genelinde ortalama stoksuzluk oranını yaklaşık **%8,3** olarak buldu. Corsten ve Gruen (2003), bu tür bulguları ve nedenlerini özetler. Promosyondaki ürünlerde stoksuzluk genellikle daha yüksektir, çünkü talep artışı tahmin ve dolum kapasitesini zorlar.

**Tüketici tepkisi.** Aynı çalışmada tüketicilerin stoksuzluğa verdiği tepkiler yaklaşık olarak şöyle dağıldı:

| Tepki | Pay |
|---|---|
| Başka mağazadan alır | %31 |
| Başka marka alır | %26 |
| Aynı markanın başka ürününü alır | %19 |
| Alımı erteler | %15 |
| Hiç almaz | %9 |

Bu dağılım kategoriye ve ülkeye göre değişir, ama genel bir ders verir: Stoksuzluk hem üreticiye hem perakendeciye kayıp yaşatır. Üretici, marka değişikliğinde ve hiç almamada kesin olarak kaybeder; tüketici ürünü başka mağazadan alırsa üretici satışı korur. Perakendeci ise mağaza değişikliğinde ve hiç almamada kaybeder.

**Nedenler.** Çalışma, stoksuzluk nedenlerinin büyük kısmının (yaklaşık %70–75) mağaza düzeyinde olduğunu gösterdi:

- **Sipariş ve tahmin hataları** (yaklaşık %47): Yanlış sipariş miktarı, gecikmiş sipariş, sistem stoku ile gerçek stok arasındaki fark.
- **Raf dolumu** (yaklaşık %25): Ürün depoda ama rafta değil.
- **Tedarik tarafı:** Merkez depo ya da üretici kaynaklı aksamalar.

Bu nedenle stoksuzluk yalnızca tedarik zinciri sorunu değildir; mağaza süreçleri ve saha ekibi de çözümün parçasıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Satış adedi, stoksuzluk oranı ve birim katkı varsayımdır; tepki dağılımı yukarıdaki tablodan alınmıştır; hesaplar `scripts/cards_numbers_fmcg_b5.py` ile yapılmıştır.

Bir ürün bir zincirde haftada 200 adet satıyor ve zamanın %8'inde rafta yok. Haftada yaklaşık **16** adetlik talep stoksuzlukla karşılaşıyor.

- **Üretici kaybı:** Marka değiştirme (%26) ve hiç almama (%9): 16 × %35 = **5,6** adet/hafta. Başka mağazadan alanların ürünü bulduğu, erteleyenlerin ise sonra aldığı varsayılıyor.
- **Perakendeci kaybı:** Mağaza değiştirme (%31) ve hiç almama (%9): 16 × %40 = **6,4** adet/hafta.

Üretici için yıllık kayıp 5,6 × 52 = yaklaşık **291,2** adet. Birim katkı 40 TL ise yıllık **11.648 TL**, tek bir ürün ve tek bir zincir için. Ana ürünler ve bütün müşteriler toplandığında rakam, raf bulunurluğu için ayrılacak saha ve tedarik bütçesini rahatça gerekçelendirir.

## Sık yapılan hatalar

- **Depo stokunu raf stoku saymak.** Sistem stoku çoğu zaman gerçeği yansıtmaz.
- **Bütün suçu tedarik zincirine atmak.** Nedenlerin büyük kısmı mağaza süreçlerindedir.
- **Promosyonlarda bulunurluğu planlamamak.** Promosyon, stoksuzluğun en sık görüldüğü dönemdir.
- **Stoksuzluğu ölçmemek.** Ölçmeden yönetilemez; mağaza denetimi ya da satış verisi analiziyle ölçün.
- **Perakendeciyle ortak hedef koymamak.** İki taraf da kaybediyor; çözüm de ortak olmalıdır.

## Pratikte nasıl uygulanır?

- [ ] Ana ürünlerde raf bulunurluğunu mağaza ziyaretlerinde ya da satış verisindeki sıfır satış günlerinden ölçün.
- [ ] Stoksuzluk nedenlerini sınıflandırın: sipariş, raf dolumu, depo, üretici.
- [ ] Mağaza düzeyindeki nedenler için temsilci ve merchandiser rutinleri tanımlayın.
- [ ] Promosyon öncesinde stok ve teslimat planını perakendeciyle birlikte yapın.
- [ ] Bulunurluğu ortak iş planına bir hedef olarak ekleyin.

## Daha fazlası

- Corsten, D.; Gruen, T. (2003). *Desperately Seeking Shelf Availability: An Examination of the Extent, the Causes, and the Efforts to Address Retail Out-of-Stocks.* International Journal of Retail & Distribution Management 31(12), 605–617. https://doi.org/10.1108/09590550310507731
