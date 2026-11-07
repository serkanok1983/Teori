---
id: kb-fmcg-5-5-trade-spend-roi
title: "Ticari harcamanın getirisi: Zincire verilen her lira geri dönüyor mu?"
summary: "Ciro primi, raf ücreti, stand, katalog ve indirim katkıları gibi ticari harcamalar çoğu üreticide büyük bir gider kalemidir. Bu kart bu harcamaların getirisini artımsal katkıyla ölçmeyi ve bütçeyi getiriye göre dağıtmayı anlatır."
course: fmcg
category: fiyatlama-ve-promosyon
tags: [promosyon, perakende, analitik, pazarlik]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: ileri
source_lessons: [FMCG-5.5]
reading_minutes: 3
key_points:
  - "Ticari harcamanın getirisi, harcamanın yarattığı artımsal katkının harcamaya oranıyla ölçülür."
  - "Artımsal katkı, harcama olmasaydı da gerçekleşecek satışın çıkarılmasıyla bulunur."
  - "Harcamaların bir kısmı koşulsuz verilir ve hiçbir performansa bağlı değildir; getirisi ölçülemeyen harcama yönetilemez."
  - "Bütçeyi geçmiş yılın dağılımına göre değil, ölçülmüş getiriye göre dağıtın."
glossary_terms: [ticari-harcama, artimsal-hacim, ciro-primi]
related: [kb-fmcg-5-4-promotion-economics, kb-fmcg-2-2-gross-to-net, kb-fmcg-10-2-trade-terms, kb-fmcg-9-6-trade-marketing, kb-fmcg-10-7-joint-business-planning]
sources:
  - title: "How Promotions Work"
    authors: "Blattberg, R. C.; Briesch, R.; Fox, E. J."
    year: 1995
    type: article
    doi: "10.1287/mksc.14.3.G122"
    url: "https://doi.org/10.1287/mksc.14.3.G122"
    verified: true
    checked_on: 2026-10-28
    note: "Marketing Science 14(3), G122–G132."
  - title: "An Empirical Analysis of the Determinants of Retail Margins: The Role of Store-Brand Share"
    authors: "Ailawadi, K. L.; Harlam, B."
    year: 2004
    type: article
    doi: "10.1509/jmkg.68.1.147.24027"
    url: "https://doi.org/10.1509/jmkg.68.1.147.24027"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Marketing 68(1), 147–165."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Ticari harcama (*trade spend*), brüt satış ile net satış arasındaki farkın büyük kısmını oluşturur. Çoğu zaman pazarlama bütçesinden de büyüktür, ama çok daha az ölçülür. Bu kart, her harcama kalemi için "bu para ne getirdi?" sorusunu sormayı ve cevaplamayı gösterir.

## Temel fikir

**Kalemler.** Ticari harcamalar kabaca ikiye ayrılır:

- **Koşulsuz harcamalar:** Yıllık sabit iskontolar, listeleme ücretleri, koşulsuz ciro primleri. Performansa bağlı değildir.
- **Koşullu harcamalar:** Stand, katalog, raf sonu, fiyat indirimi katkısı, hedefe bağlı primler. Belirli bir faaliyet ya da sonuç karşılığında ödenir.

Koşullu harcamaların getirisi ölçülebilir. Koşulsuz harcamalar ise müşteriyle ilişkinin "giriş ücreti" gibidir; bunları da yılda bir kez müşterinin toplam katkısıyla karşılaştırmak gerekir.

**Getiri hesabı.** Getiri = (artımsal katkı − harcama) / harcama. Artımsal katkı, harcamanın yarattığı ek hacmin birim katkıyla çarpımıdır. Ek hacmi ölçmek için baz satışı doğru tahmin etmek gerekir. Blattberg, Briesch ve Fox (1995), promosyonların etkisine dair ampirik genellemeleri derler ve getiri hesabında brüt değil net etkinin kullanılması gerektiğini hatırlatır. Ayrıca perakende aktarımı (*pass-through*) üzerine yapılan araştırmalar, perakendecinin üreticiden aldığı ticari indirimleri rafa yansıtma oranının üreticiden üreticiye ve kategoriden kategoriye büyük farklılık gösterdiğini ve tek tek üreticiler için bu oranın çoğu zaman %100'ün altında kalabildiğini gösterir. Bu, ödediğiniz indirimin bir kısmının rafta fiyat düşüşüne dönüşmeyebileceği anlamına gelir.

**Karşı tarafın bakışı.** Ailawadi ve Harlam (2004), perakende marjlarını belirleyen etkenleri ve mağaza markası payının rolünü inceler. Zincir için ticari harcama bir marj kaynağıdır. Pazarlıkta bu bakışı bilmek, harcamayı performansa bağlamayı kolaylaştırır.

**Ölçümü kurumsallaştırmak.** Ticari harcama getirisinin ölçülmesi için her harcamanın hangi müşteri, hangi ürün ve hangi döneme ait olduğu sistemde doğru kaydedilmelidir. Toplu ve açıklamasız kayıtlar, sonradan analiz yapılmasını engeller. Getirisi ölçülemeyen harcamalar da bir liste hâlinde tutulmalı ve zamanla ölçülebilir koşullara bağlanmalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Harcama, hacim ve katkı varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b3.py` ile yapılmıştır.

Bir zincirde bir aylık stand ve katalog için 150.000 TL ödüyorsunuz. Birim katkınız 15 TL. Analiz, standın baz satışın üstüne 12.000 adet ek satış getirdiğini gösteriyor.

- Artımsal katkı: 12.000 × 15 = **180.000 TL**
- Getiri: (180.000 − 150.000) / 150.000 = **%20**
- Başabaş ek hacim: 150.000 / 15 = **10.000 adet**

Ek satış 8.000 adette kalsaydı getiri **eksi %20** olurdu. Aynı harcama farklı zincirlerde ya da farklı ürünlerde çok farklı sonuç verebilir. Bu yüzden ortalama yerine her uygulamayı ayrı ölçün.

## Sık yapılan hatalar

- **Toplam satışı getiri saymak.** Stand haftasındaki satışın tamamı standın eseri değildir.
- **Koşulsuz harcamayı hiç sorgulamamak.** Her yıl otomatik yenilenen iskontolar zamanla büyür.
- **Rafa yansımayı kontrol etmemek.** Fiyat indirimi katkısı verdiyseniz raf fiyatının gerçekten düştüğünü doğrulayın.
- **Bütçeyi geçen yıla göre dağıtmak.** Getirisi düşük kalemler kendiliğinden küçülmez.

## Pratikte nasıl uygulanır?

- [ ] Bütün ticari harcamaları müşteri, ürün ve kalem bazında tek bir tabloda toplayın.
- [ ] Koşulsuz harcamaların payını hesaplayın ve her yenilemede bir kısmını performansa bağlamayı önerin.
- [ ] Koşullu harcamalar için başabaş ek hacmi önceden hesaplayın.
- [ ] Uygulama sonrası artımsal katkıyı ölçün ve sonuçları bir sonraki yıllık planlamaya taşıyın.

## Daha fazlası

- Blattberg, R. C.; Briesch, R.; Fox, E. J. (1995). *How Promotions Work.* Marketing Science 14(3), G122–G132. https://doi.org/10.1287/mksc.14.3.G122
- Ailawadi, K. L.; Harlam, B. (2004). *An Empirical Analysis of the Determinants of Retail Margins: The Role of Store-Brand Share.* Journal of Marketing 68(1), 147–165. https://doi.org/10.1509/jmkg.68.1.147.24027
