---
id: kb-fmcg-4-6-sku-rationalisation
title: "SKU sadeleştirme: Portföyden ürün çıkarmanın hesabı"
summary: "Az satan ürünleri çıkarmak karmaşıklık maliyetini düşürür, ama satışın bir kısmı da kaybolabilir. Bu kart kararın hesabını, talep transferinin önemini ve sadeleştirmeyi zincir ve dağıtıcıyla nasıl yöneteceğinizi anlatır."
course: fmcg
category: strateji-ve-portfoy
tags: [strateji, portfoy, maliyet, perakende]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, depo-lojistik-muduru]
level: orta
source_lessons: [FMCG-4.6]
reading_minutes: 3
key_points:
  - "Ürün çıkarmanın kazancı karmaşıklık maliyetindeki azalmadır; kaybı ise başka ürüne geçmeyen satışın katkısıdır."
  - "Kararın en kritik varsayımı talep transferidir: Çıkan ürünün alıcılarının ne kadarı portföyünüzdeki başka bir ürüne geçer?"
  - "Araştırmalar, tüketicinin algıladığı çeşitliliğin ürün sayısından çok sevdiği ürünün varlığına ve raf düzenine bağlı olabildiğini gösterir."
  - "Sadeleştirme stok eritme, zincir bildirimi ve raf yeniden düzenlemesiyle birlikte planlanmalıdır."
glossary_terms: [sku-sadelestirme, talep-transferi, katki-payi]
related: [kb-fmcg-4-4-portfolio-management, kb-fmcg-9-3-shelf-space-planogram, kb-fmcg-10-6-category-management, kb-fmcg-6-3-cost-to-serve, kb-fmcg-11-4-safety-stock]
sources:
  - title: "Consumers' Perceptions of the Assortment Offered in a Grocery Category: The Impact of Item Reduction"
    authors: "Broniarczyk, S. M.; Hoyer, W. D.; McAlister, L."
    year: 1998
    type: article
    doi: "10.1177/002224379803500203"
    url: "https://doi.org/10.1177/002224379803500203"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Marketing Research 35(2), 166–176."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Portföy kuyruğundaki ürünler küçük görünür, ama her biri ayrı üretim ayarı, ambalaj malzemesi, depo yeri, sipariş satırı ve raf alanı ister. Bu kart, bir grup ürünü çıkarmanın net etkisini hesaplamanızı ve kararı uygulamaya dökmenizi sağlar.

## Temel fikir

**Kazanç tarafı: karmaşıklık maliyeti.** Her SKU'nun portföyde kalmasının maliyeti vardır: üretim hattında ayar ve temizlik süresi, minimum alım miktarları yüzünden fazla ambalaj stoğu, depo yeri, güvenlik stoğu, son kullanma tarihi riski, ana veri ve fiyat listesi bakımı, satış ekibinin anlatım zamanı. Bu maliyetler çoğu zaman genel giderlere dağılmıştır. Ürün bazında tahmin etmek için operasyon ve finans ekipleriyle birlikte çalışın.

**Kayıp tarafı: transfer etmeyen satış.** Ürün çıktığında alıcıların bir kısmı portföyünüzdeki başka bir ürüne geçer. Bu orana **talep transferi** (*demand transfer*) denir. Geçmeyen kısım rakibe ya da başka kategoriye gider. Gerçek kayıp, bu geçmeyen satışın katkısıdır.

**Tüketici algısı.** Broniarczyk, Hoyer ve McAlister (1998), market kategorilerinde ürün azaltmanın tüketicinin çeşitlilik algısını her zaman düşürmediğini inceler. Çalışmaya göre algı, tüketicinin sevdiği ürünün rafta kalmasına ve kategoriye ayrılan raf alanına bağlı olabilir. Bu, iyi planlanmış bir sadeleştirmenin raf önündeki deneyimi bozmayabileceğini gösterir.

**Çıkarma kararını uygulamak.** Bir ürünü listeden çıkarma kararı verildiğinde stokların eritilmesi, ambalaj ve hammadde siparişlerinin durdurulması, perakendecilere ve dağıtıcılara önceden bilgi verilmesi ve raftaki boşluğun hangi ürünle doldurulacağının planlanması gerekir. Çıkarılan ürünün alışverişçilerinin portföydeki diğer ürünlere geçip geçmediği, sonraki aylarda satış verileriyle izlenmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Satış, katkı oranı, transfer oranı ve maliyetler varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b2.py` ile yapılmıştır.

Portföyden 8 SKU çıkarmayı düşünüyorsunuz. Bu ürünlerin toplam yıllık net satışı 6.000.000 TL, katkı oranı %30. Operasyon ekibi SKU başına yıllık karmaşıklık maliyetini 180.000 TL olarak tahmin ediyor. Alıcıların %60'ının portföyünüzdeki başka ürünlere geçeceğini varsayıyorsunuz.

- Kaybedilen katkı: 6.000.000 × (1 − 0,60) × 0,30 = **720.000 TL**
- Karmaşıklık tasarrufu: 8 × 180.000 = **1.440.000 TL**
- Net etki: **+720.000 TL**

Transfer oranı %30 olursa net etki **+180.000 TL**'ye düşer. Kararın yönü değişmiyor, ama marj inceliyor. Bu yüzden transfer oranını mümkünse bir bölgede deneyerek ölçün.

## Sık yapılan hatalar

- **Yalnızca satışa bakmak.** Az satan ama belirli bir zincirde ya da segmentte vazgeçilmez olan ürün, çıkarılınca o müşteriyi kaybettirebilir.
- **Transferi %100 varsaymak.** Tüketici her zaman sizin diğer ürününüze geçmez.
- **Tasarrufu abartmak.** Ürün çıksa da bazı sabit maliyetler kalır; gerçekten azalan maliyeti sayın.
- **Uygulamayı ihmal etmek.** Kalan stok, zincirdeki raf boşluğu ve dağıtıcının elindeki ürünler planlanmazsa iade ve imha maliyeti çıkar.

## Pratikte nasıl uygulanır?

- [ ] Aday SKU'ları katkı ve büyümeye göre listeleyin; stratejik nedenle tutulanları ayrı işaretleyin.
- [ ] Her aday için transfer oranını tahmin edin: panel geçiş verisi, benzer geçmiş çıkışlar ya da bir bölgede deneme.
- [ ] Operasyon ve finansla gerçekten azalacak maliyetleri belirleyin.
- [ ] Net etkiyi farklı transfer oranlarıyla hesaplayın.
- [ ] Çıkış takvimini yapın: üretim durdurma, stok eritme, zincirlere bildirim, planogram güncellemesi.

## Daha fazlası

- Broniarczyk, S. M.; Hoyer, W. D.; McAlister, L. (1998). *Consumers' Perceptions of the Assortment Offered in a Grocery Category: The Impact of Item Reduction.* Journal of Marketing Research 35(2), 166–176. https://doi.org/10.1177/002224379803500203
