---
id: kb-fmcg-9-3-shelf-space-planogram
title: "Raf alanı ve planogram"
summary: "Raf alanı satışı etkiler, ama etkisi sanıldığından çok daha küçüktür ve azalan getirilidir. Bu kart raf alanı esnekliğini, planogram mantığını ve raf payı görüşmelerinde gerçekçi beklenti kurmayı anlatır."
course: fmcg
category: perakende-uygulama
tags: [perakende, raf, kategori-yonetimi]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, saha-satis-temsilcisi]
level: orta
source_lessons: [FMCG-9.3]
reading_minutes: 3
key_points:
  - "Raf alanı esnekliği, raf alanındaki yüzde değişimin satışta yarattığı yüzde değişimdir."
  - "Bir meta-analize göre ortalama raf alanı esnekliği yaklaşık 0,17'dir; yani raf alanını iki katına çıkarmak satışı iki katına çıkarmaz."
  - "Esneklik dürtüsel ürünlerde daha yüksek, temel ihtiyaç ürünlerinde daha düşüktür."
  - "Planogram; ürünlerin raftaki yerini, yüz sayısını ve sırasını tüketicinin karar ağacına göre belirler."
  - "Raf payı, satış payıyla ve kategori kârıyla tutarlı olmalıdır."
glossary_terms: [planogram, raf-payi, raf-bulunurlugu]
related: [kb-fmcg-9-1-retailer-economics, kb-fmcg-9-4-osa-out-of-stock, kb-fmcg-9-5-perfect-store, kb-fmcg-10-6-category-management, kb-fmcg-4-6-sku-rationalisation]
sources:
  - title: "Shelf Space Elasticity: A Meta-Analysis"
    authors: "Eisend, M."
    year: 2014
    type: article
    doi: "10.1016/j.jretai.2013.03.003"
    url: "https://doi.org/10.1016/j.jretai.2013.03.003"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Retailing 90(2), 168–181."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Satış ekipleri çoğu zaman daha fazla raf alanı ister ve bunun satışı orantılı biçimde artıracağını varsayar. Perakendeci ise aynı alanı başka ürünlere verebileceğini bilir. Bu kart, raf alanının satışa gerçek etkisini ve raf görüşmelerini veriye dayandırmayı anlatır.

## Temel fikir

**Raf alanı esnekliği.** Eisend (2014), raf alanı ile satış arasındaki ilişkiyi inceleyen çalışmalardan elde edilen 1.268 esneklik tahminini bir meta-analizde birleştirdi. Ortalama raf alanı esnekliği yaklaşık **0,17** çıktı. Yani raf alanındaki %1'lik artış, satışı ortalama yaklaşık %0,17 artırıyor. Ayrıca:

- Esneklik, temel ürünlerde (*commodities*) en düşük, dürtüsel ürünlerde en yüksek.
- Raf alanı artışlarının etkisi, azaltmaların etkisinden daha büyük bulundu.
- Etki, değişimin büyüklüğü arttıkça oransal olarak azalıyor.

Bu ortalamadır; tek bir ürün için kesin bir tahmin değildir. Ama genel bir ders verir: Raf alanı önemlidir, ama satışın ana belirleyicisi değildir.

**Hesap.** Esneklik sabit kabul edilirse yeni satış = eski satış × (yeni alan / eski alan)^esneklik. Bu formül, artışın azalan getirili olduğunu gösterir.

**Planogram.** Ürünlerin rafta nerede, kaç yüzle ve hangi sırayla duracağını gösteren plandır. İyi bir planogram:

- **Tüketicinin karar ağacını izler:** Örneğin önce kategori tipi, sonra marka, sonra boyut.
- **Satış hızına göre yüz verir:** Hızlı dönen ürüne, stoksuzluk yaşamaması için yeterli yüz.
- **Göz hizasını değerlendirir:** En görünür raflar, kategoriye en çok katkı yapan ürünlere.
- **Uygulanabilirdir:** Mağaza ekibinin ve temsilcinin kolayca uygulayabileceği kadar sade.

**Raf payı ve satış payı.** Genel bir kural olarak, bir markanın raf payı satış payına yakın olmalıdır. Raf payı satış payından çok yüksekse perakendeci alanı geri ister. Çok düşükse stoksuzluk ve kayıp satış riski doğar.

## Bir örnek

> **Örnek (temsili rakamlar):** Satış adedi ve yüz sayıları varsayımdır; esneklik, Eisend (2014) ortalamasıdır; hesaplar `scripts/cards_numbers_fmcg_b5.py` ile yapılmıştır.

Bir ürün rafta 3 yüzle haftada 180 adet satıyor. Satış ekibi 4 yüz istiyor ve "%33 daha fazla alan, %33 daha fazla satış" diyor.

- Esneklik 0,17 ile 3'ten 4 yüze: satış yaklaşık **%5,0** artar, haftada yaklaşık **189,0** adet.
- 3'ten 6 yüze (alanı iki katına çıkarmak): satış yaklaşık **%12,5** artar.

Doğrusal varsayım (%33,3), gerçekçi tahminin altı katından fazla. Perakendeci bu farkı bilir. Daha ikna edici bir argüman şudur: "Ürün 3 yüzle hafta sonları stoksuz kalıyor; 4. yüz, stoksuzluk kaybını azaltacak." Bu durumda ek yüzün değeri, esneklikten çok bulunurluk kazancından gelir.

## Sık yapılan hatalar

- **Raf alanının etkisini doğrusal varsaymak.** Bu, gerçekçi olmayan beklentiler ve güven kaybı yaratır.
- **Raf payını satış payından kopuk istemek.** Perakendeci kategori verisiyle buna itiraz eder.
- **Planogramı tasarlayıp uygulamayı izlememek.** Sahada planogram uyumu çoğu zaman düşüktür.
- **Bütün ürünler için aynı esnekliği varsaymak.** Dürtüsel ürünlerde etki daha yüksektir.
- **Stoksuzluk verisini kullanmamak.** Ek yüz talebinin en güçlü gerekçesi çoğu zaman bulunurluktur.

## Pratikte nasıl uygulanır?

- [ ] Ana müşterilerde raf payınızı ve satış payınızı karşılaştırın.
- [ ] Raf alanı talebini, raf alanı esnekliği ve stoksuzluk verisiyle birlikte hesaplayın.
- [ ] Planogram önerinizi tüketicinin karar ağacına ve kategori kârına dayandırın.
- [ ] Planogram uyumunu mağaza ziyaretlerinde ölçün ve sapmaları düzeltin.
- [ ] Mümkünse bir grup mağazada deneme yapıp sonucu benzer mağazalarla karşılaştırın.

## Daha fazlası

- Eisend, M. (2014). *Shelf Space Elasticity: A Meta-Analysis.* Journal of Retailing 90(2), 168–181. https://doi.org/10.1016/j.jretai.2013.03.003
