---
id: kb-fmcg-5-7-rgm-system
title: "Gelir büyüme yönetimi: Fiyat, karma, promosyon ve ticari koşulları birlikte yönetmek"
summary: "Gelir büyüme yönetimi, net gelir ve kârı etkileyen kaldıraçları tek bir çerçevede yönetme yaklaşımıdır. Bu kart kaldıraçları, büyümeyi kaldıraçlara ayıran köprü analizini ve bu işin organizasyonda nasıl kurulacağını anlatır."
course: fmcg
category: fiyatlama-ve-promosyon
tags: [fiyatlama, promosyon, analitik, strateji]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: ileri
source_lessons: [FMCG-5.7]
reading_minutes: 3
key_points:
  - "Gelir büyüme yönetimi fiyat, fiyat-paket mimarisi, ürün karması, promosyon ve ticari koşulları ayrı ayrı değil birlikte ele alır."
  - "Net gelir değişimini kaldıraçlara ayıran bir köprü, büyümenin nereden geldiğini gösterir."
  - "Kaldıraçlar birbirini etkiler; fiyat artışı ticari koşullarla yenilirse net etki küçülür."
  - "Bu iş, pazarlama, satış ve finansın ortak verisi ve ortak toplantısı olmadan yürümez."
glossary_terms: [gelir-buyume-yonetimi, fiyat-hacim-karma-analizi, ticari-harcama]
related: [kb-fmcg-5-1-price-elasticity, kb-fmcg-5-3-price-pack-architecture, kb-fmcg-5-4-promotion-economics, kb-fmcg-5-5-trade-spend-roi, kb-fmcg-2-6-price-volume-mix-variance]
sources:
  - title: "Marketing Management"
    authors: "Kotler, P.; Keller, K. L."
    year: 2016
    type: book
    verified: false
    note: "Kitap; baskı yılı kontrol edilmedi."
  - title: "How Promotions Work"
    authors: "Blattberg, R. C.; Briesch, R.; Fox, E. J."
    year: 1995
    type: article
    doi: "10.1287/mksc.14.3.G122"
    url: "https://doi.org/10.1287/mksc.14.3.G122"
    verified: true
    checked_on: 2026-10-28
    note: "Marketing Science 14(3), G122–G132."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Fiyatı pazarlama, promosyonu marka ekibi, zincir koşullarını kilit müşteri ekibi, maliyeti finans yönetiyorsa, her birinin kararı diğerinin etkisini silebilir. Gelir büyüme yönetimi (*revenue growth management*, RGM) bu kararları tek bir çerçevede toplar. Bu kart, çerçevenin ana parçalarını ve pratik bir başlangıcı anlatır.

## Temel fikir

**Kaldıraçlar.** Uygulamada RGM genellikle beş kaldıraç üzerinden kurulur:

1. **Fiyat:** Liste fiyatı ve raf fiyatı konumu.
2. **Fiyat-paket mimarisi:** Hangi boyut, hangi fiyat noktası, hangi kanal.
3. **Ürün karması:** Daha kârlı ürün ve paketlerin satıştaki payı.
4. **Promosyon:** Hangi promosyonun, ne sıklıkla, hangi derinlikte yapılacağı.
5. **Ticari koşullar:** İskontolar, primler, ücretler ve bunların performansa bağlanması.

Bu kaldıraçların her biri pazarlama literatüründe ayrı ayrı incelenir. Kotler ve Keller fiyat ve ürün kararlarını, Blattberg, Briesch ve Fox (1995) promosyonları ele alır. RGM ise bir uygulayıcı yaklaşımıdır; tek bir akademik tanımı yoktur.

**Köprü analizi.** Net gelirin bir yıldan diğerine değişimini kaldıraçlara ayırmak, büyümenin kaynağını görünür kılar. Fiyat-hacim-karma analizinin genişletilmiş hâlidir.

**Etkileşim.** Kaldıraçlar birbirini etkiler. Fiyat artışı hacmi düşürebilir. Promosyon derinliğini azaltmak hacmi düşürür ama net fiyatı artırır. Ticari koşullarda verilen taviz, liste fiyatı artışının etkisini yiyebilir. Bu yüzden kararlar aynı masada, aynı veriyle alınmalıdır.

**Organizasyon ve yönetişim.** RGM'nin bir yöntem olarak işlemesi için karar haklarının net olması gerekir. Liste fiyatı, paket ve boy kararları, promosyon takvimi ve ticari koşullar genellikle farklı ekiplerin elindedir: pazarlama, satış, kilit müşteri yönetimi ve finans. Ortak bir aylık ya da üç aylık toplantıda bu kararların birlikte gözden geçirilmesi, bir kaldıracın diğerinin etkisini silmesini önler. Ortak bir veri tabanı ve aynı tanımlar (net satış, baz satış, ticari harcama) bu toplantının temelidir. Promosyon sonrası değerlendirmelerin sistematik yapılması ve sonuçların bir sonraki yılın planına aktarılması, RGM'yi tek seferlik bir projeden sürekli bir sürece dönüştürür.

## Bir örnek

> **Örnek (temsili rakamlar):** Değerler milyon TL, varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b3.py` ile yapılmıştır.

Geçen yıl net gelir 100 milyon TL. Bu yılın köprüsü:

| Kaldıraç | Etki | Kümülatif |
|---|---|---|
| Fiyat | +8,0 | 108,0 |
| Karma | +2,0 | 110,0 |
| Promosyon verimliliği | +1,5 | 111,5 |
| Ticari koşullar | −0,5 | 111,0 |
| Hacim | −3,0 | 108,0 |

Net gelir %8 arttı, ama hacim düştü. Büyümenin tamamı fiyat, karma ve promosyon verimliliğinden geliyor. Ekip şu soruları sormalıdır: Hacim kaybı fiyat artışının beklenen sonucu mu, yoksa dağıtım ya da rakip kaynaklı mı? Ticari koşullardaki 0,5 milyonluk kayıp hangi müşteride ve neden oluştu?

## Sık yapılan hatalar

- **Kaldıraçları ayrı ekiplere bırakmak.** Her ekip kendi hedefini tutarken toplam kâr düşebilir.
- **Yalnızca fiyata bakmak.** Karma ve promosyon verimliliği çoğu zaman fiyat kadar katkı sağlar.
- **Veriyi ortaklaştırmamak.** Pazarlama, satış ve finansın farklı rakamlarla toplantıya gelmesi kararı geciktirir.
- **Hacim kaybını görmezden gelmek.** Sürekli fiyat ve karma ile büyüyen ama hacim kaybeden marka, zamanla pazarda zayıflar.

## Pratikte nasıl uygulanır?

- [ ] Net gelir köprüsünü aylık ya da çeyreklik olarak hazırlayın.
- [ ] Her kaldıraç için bir sorumlu ve bir gösterge belirleyin.
- [ ] Pazarlama, satış ve finansın katıldığı düzenli bir RGM toplantısı kurun.
- [ ] Büyük fiyat, promosyon ve ticari koşul kararlarını bu toplantıda, köprü üzerindeki etkisiyle birlikte değerlendirin.

## Daha fazlası

- Kotler, P.; Keller, K. L. (2016). *Marketing Management.* (kaynak doğrulanmadı)
- Blattberg, R. C.; Briesch, R.; Fox, E. J. (1995). *How Promotions Work.* Marketing Science 14(3), G122–G132. https://doi.org/10.1287/mksc.14.3.G122
