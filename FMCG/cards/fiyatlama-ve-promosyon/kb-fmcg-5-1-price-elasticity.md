---
id: kb-fmcg-5-1-price-elasticity
title: "Fiyat esnekliği: Fiyat değişince hacim ne kadar değişir?"
summary: "Fiyat esnekliği, fiyattaki yüzde değişime karşı satış hacmindeki yüzde değişimdir. Bu kart esnekliği hesaplamayı, onu kâr hesabına bağlamayı, çapraz esnekliği ve esnekliği hangi etkenlerin değiştirdiğini anlatır."
course: fmcg
category: fiyatlama-ve-promosyon
tags: [fiyatlama, analitik, rekabet]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: orta
source_lessons: [FMCG-5.1, FMCG-5.2, ECO-1.4]
reading_minutes: 3
key_points:
  - "Fiyat esnekliği, hacimdeki yüzde değişimin fiyattaki yüzde değişime oranıdır; hızlı tüketimde genellikle negatiftir."
  - "Esneklik −1'den küçükse (mutlak değeri 1'den büyükse) fiyat artışı ciroyu düşürür; ama kâr kararı katkı payıyla verilir."
  - "Fiyat artışında katkıyı korumak için kabul edilebilir hacim kaybı, eski ve yeni birim katkı oranıyla hesaplanır."
  - "Çapraz esneklik, bir ürünün fiyatı değişince başka bir ürünün hacminin nasıl değiştiğini gösterir."
glossary_terms: [capraz-fiyat-esnekligi, katki-payi]
related: [kb-fmcg-5-3-price-pack-architecture, kb-fmcg-5-4-promotion-economics, kb-fmcg-5-6-pricing-in-high-inflation, kb-fmcg-2-3-contribution-breakeven, kb-fmcg-3-5-brand-equity]
sources:
  - title: "New Empirical Generalizations on the Determinants of Price Elasticity"
    authors: "Bijmolt, T. H. A.; van Heerde, H. J.; Pieters, R. G. M."
    year: 2005
    type: article
    doi: "10.1509/jmkr.42.2.141.62296"
    url: "https://doi.org/10.1509/jmkr.42.2.141.62296"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Marketing Research 42(2), 141–156."
  - title: "Determinants of Store-Level Price Elasticity"
    authors: "Hoch, S. J.; Kim, B.-D.; Montgomery, A. L.; Rossi, P. E."
    year: 1995
    type: article
    doi: "10.1177/002224379503200104"
    url: "https://doi.org/10.1177/002224379503200104"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Marketing Research 32(1), 17–29."
  - title: "Implications of Market Structure for Elasticity Structure"
    authors: "Russell, G. J.; Bolton, R. N."
    year: 1988
    type: article
    doi: "10.1177/002224378802500301"
    url: "https://doi.org/10.1177/002224378802500301"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Marketing Research 25(3), 229–241."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

"Fiyatı %10 artırırsak ne kadar hacim kaybederiz ve bu kayıp kabul edilebilir mi?" Fiyat esnekliği (*price elasticity*) bu sorunun ilk yarısını, katkı hesabı ikinci yarısını cevaplar. Bu kart ikisini birlikte kullanmayı gösterir.

## Temel fikir

**Tanım.** Esneklik = hacimdeki yüzde değişim / fiyattaki yüzde değişim. Fiyat arttığında hacim genellikle düştüğü için sonuç negatiftir.

- Mutlak değer 1'den büyükse talep **esnek**tir: Fiyat artışı ciroyu düşürür.
- Mutlak değer 1'den küçükse talep **esnek değildir**: Fiyat artışı ciroyu artırır.

İki nokta arasındaki değişimi ölçerken başlangıç değeri yerine iki değerin ortalamasını baz almak (*ark esnekliği*, *arc elasticity*) artış ve azalış yönünde aynı sonucu verir.

**Esnekliği ne belirler?** Bijmolt, van Heerde ve Pieters (2005), çok sayıda çalışmayı bir araya getiren meta-analizlerinde esnekliğin ürün kategorisine, ürün yaşam döngüsü aşamasına, ölçüm yöntemine ve diğer etkenlere göre değiştiğini inceler. Hoch ve arkadaşları (1995), mağaza düzeyinde esnekliğin mağazanın müşteri profili ve rekabet ortamıyla ilişkili olduğunu gösterir. Kısacası tek bir "kategori esnekliği" yoktur; kanala, mağazaya ve döneme göre değişir.

**Çapraz esneklik** (*cross-price elasticity*). Bir ürünün fiyatı değiştiğinde başka bir ürünün hacmindeki yüzde değişimdir. Pozitifse ürünler birbirinin ikamesidir. Russell ve Bolton (1988), pazar yapısıyla esneklik yapısı arasındaki ilişkiyi inceler: Birbirine yakın ürünler arasındaki çapraz etkiler daha güçlüdür. Kendi portföyünüzde bir ürünün fiyatını düşürmek, kardeş ürünün satışını çalabilir.

**Kâr bağlantısı.** Ciro artsa da kâr düşebilir ya da tersi olabilir. Kararı birim katkıyla verin. Fiyat artışında katkıyı korumak için kabul edilebilir en büyük hacim kaybı: 1 − (eski birim katkı / yeni birim katkı).

## Bir örnek

> **Örnek (temsili rakamlar):** Fiyat, hacim ve maliyet varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b2.py` ile yapılmıştır.

Net fiyatı 20 TL'den 22 TL'ye çıkardınız; haftalık hacim 1.000'den 920 adede düştü. Değişken maliyet 14 TL.

- Ark esnekliği: (−80 / 960) / (2 / 21) ≈ **−0,88**
- Ciro: 20.000 TL → **20.240 TL**
- Katkı: (20 − 14) × 1.000 = 6.000 TL → (22 − 14) × 920 = **7.360 TL**

Katkıyı korumak için izin verilen hacim kaybı: 1 − 6 / 8 = **%25,00**. Gerçek kayıp %8 olduğu için artış kâr açısından doğru bir karardı. Rakipler de fiyat artırdıysa bu esneklik, tek başına artış yapsaydınız göreceğiniz esneklikten düşük olabilir.

## Sık yapılan hatalar

- **Ciroya bakıp karar vermek.** Esnek talepte bile fiyat artışı katkıyı artırabilir.
- **Promosyon esnekliğini normal fiyat esnekliği sanmak.** Geçici indirimde tüketici stok yapar; kalıcı fiyat değişikliğine tepkisi farklıdır.
- **Rakip tepkisini unutmak.** Rakipler fiyat izlerse hacim kaybı daha az, izlemezse daha fazla olur.
- **Tek bir esneklik rakamını her kanala uygulamak.** İndirim marketi ile bakkalda tepkiler farklıdır.

## Pratikte nasıl uygulanır?

- [ ] Geçmiş fiyat değişikliklerinizi ve hacim etkilerini kanal bazında kaydedin; promosyon dönemlerini ayırın.
- [ ] Her fiyat kararından önce izin verilen hacim kaybını hesaplayın.
- [ ] Portföyünüzdeki ürünler arasındaki geçişleri (çapraz etkiyi) panel ya da satış verisiyle izleyin.
- [ ] Mümkünse önce bir bölgede ya da kanalda deneyin, sonra yaygınlaştırın.

## Daha fazlası

- Bijmolt, T. H. A.; van Heerde, H. J.; Pieters, R. G. M. (2005). *New Empirical Generalizations on the Determinants of Price Elasticity.* Journal of Marketing Research 42(2), 141–156. https://doi.org/10.1509/jmkr.42.2.141.62296
- Hoch, S. J.; Kim, B.-D.; Montgomery, A. L.; Rossi, P. E. (1995). *Determinants of Store-Level Price Elasticity.* Journal of Marketing Research 32(1), 17–29. https://doi.org/10.1177/002224379503200104
- Russell, G. J.; Bolton, R. N. (1988). *Implications of Market Structure for Elasticity Structure.* Journal of Marketing Research 25(3), 229–241. https://doi.org/10.1177/002224378802500301
