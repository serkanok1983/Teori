---
id: kb-eco-49-1-time-series-seasonality
title: "Zaman serileri ve mevsimsellik: Aylık satışları doğru okumak"
summary: "Aylık satış verilerinde mevsimselliğin aydan aya karşılaştırmaları nasıl yanılttığını, mevsimsel endeksle arındırmayı, yıllık karşılaştırmayı ve enflasyonla reel büyümeyi ayırmayı anlatır."
course: eco
category: veri-ve-istatistik
tags: [istatistik, zaman-serisi, tahmin, satis]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, depo-lojistik-muduru]
level: ileri
source_lessons: [ECO-49.1]
reading_minutes: 2
key_points:
  - "Mevsimsel ürünlerde aydan aya değişim, büyük ölçüde mevsim etkisini yansıtır."
  - "Mevsimsel endeks, bir ayın yıllık ortalamaya göre tipik düzeyini gösterir."
  - "Mevsimsellikten arındırılmış veri veya geçen yılın aynı ayıyla karşılaştırma eğilimi daha iyi gösterir."
  - "Yüksek enflasyonda nominal büyüme reel büyümeyle karıştırılmamalıdır."
glossary_terms: [zaman-serisi, mevsimsellik, mevsimsel-endeks, reel-buyume]
related: [kb-eco-47-1-descriptive-statistics, kb-eco-47-5-correlation-regression-basics, kb-eco-2-5-growth-rates-and-logs, kb-eco-14-2-inflation-measurement-tufe-ufe, kb-eco-14-1-gdp-real-nominal]
sources:
  - title: "Forecasting: Principles and Practice (3rd ed.)"
    authors: "Hyndman, R. J.; Athanasopoulos, G."
    year: 2021
    type: book
    url: "https://otexts.com/fpp3/"
    verified: true
    checked_on: 2026-10-28
  - title: "Türkiye İstatistik Kurumu (resmî site)"
    authors: "TÜİK"
    year: 2026
    type: web
    url: "https://www.tuik.gov.tr"
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

Aralık ayında satışlar kasıma göre %30 arttığında bu iyi bir haber midir? Mevsimsel ürünlerde bu soru yanıltıcıdır. Bu kart, satış verisindeki mevsim etkisini ayıklamanızı ve gerçek eğilimi görmenizi sağlar. Hyndman ve Athanasopoulos'un açık erişimli kitabı bu konudaki yöntemleri ayrıntılı biçimde anlatır.

## Temel fikir

Bir zaman serisi genellikle üç bileşenden oluşur:

- **Eğilim:** Uzun dönemli artış veya azalış.
- **Mevsimsellik:** Her yıl aynı dönemlerde tekrarlanan dalgalanma (bayramlar, yaz, yılbaşı, okul dönemi).
- **Düzensiz bileşen:** Tek seferlik olaylar ve rastlantısal oynamalar.

**Mevsimsel endeks:** Bir ayın satışının yıllık aylık ortalamaya oranı, birkaç yılın ortalaması alınarak hesaplanır. Aralık endeksi 1,25 ise aralık satışları tipik olarak ortalamanın %25 üzerindedir.

**Arındırılmış satış** = Gerçek satış ÷ Mevsimsel endeks.

**Yıllık karşılaştırma:** Geçen yılın aynı ayıyla karşılaştırma mevsimselliği büyük ölçüde ortadan kaldırır, ama enflasyonu ortadan kaldırmaz.

Ramazan ve Kurban Bayramı her yıl yaklaşık 11 gün öne kaydığı için ay bazında mevsimsellik yıldan yıla değişebilir; bayram etkisini ayrı izlemek gerekir.

### Mevsimsellikle ne yaparsınız?

- **Satış hedefleri:** Yıllık hedefi aylara eşit bölmek yerine mevsimsel endekslere göre dağıtın. Aksi hâlde satış ekibi düşük sezonda hep hedefin altında, yüksek sezonda hep üstünde görünür.
- **Stok ve satın alma:** Yüksek sezondan önce stok birikir ve nakit bağlanır. Mevsimsel endeks, hem stok planına hem de nakit bütçesine girdi olmalıdır.
- **Personel ve araç kapasitesi:** Yoğun dönemler için geçici kapasite planlamasını önceden yapın.

### Reel ve nominal karşılaştırma

Yüksek enflasyonda nominal satışlar her ay artıyor görünebilir. Gerçek bir artış olup olmadığını anlamak için ya miktar bazında (koli, ton) ya da fiyat endeksiyle düzeltilmiş tutarlarla karşılaştırma yapın. Eğilimi görmek için mevsimsellikten arındırılmış ve enflasyondan arındırılmış serileri birlikte kullanın.

### Basit tahmin yöntemleri

Mevsimsel naif yöntem (geçen yılın aynı ayı × büyüme oranı) çoğu zaman şaşırtıcı derecede iyi bir başlangıç noktasıdır. Daha karmaşık yöntemleri, bu basit yönteme göre gerçekten daha iyi tahmin yapıp yapmadıklarını test ederek kullanın.

## Bir örnek

> **Örnek (temsili rakamlar):** Satışlar, endeksler ve enflasyon oranı varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b7.py` ile yapılmıştır.

Bir distribütörün kasım satışı 1.000, aralık satışı 1.300 (bin TL). Aydan aya artış %30.

Mevsimsel endeksler: kasım 0,95, aralık 1,25.

- Arındırılmış kasım: 1.053
- Arındırılmış aralık: 1.040
- **Arındırılmış değişim: %1,2 düşüş.**

Geçen yılın aralık satışı 1.150; nominal yıllık artış %13,0. Aynı dönemde fiyatlar ortalama %30 arttıysa reel değişim **%13,0 düşüş**. Yani hem mevsim hem enflasyon etkisi ayıklandığında satışlar geriliyor.

## Sık yapılan hatalar

- Mevsimsel ürünlerde aydan aya değişimi performans ölçüsü olarak kullanmak.
- Bayram kaymalarını göz ardı ederek ay bazında yıllık karşılaştırma yapmak.
- Nominal büyümeyi reel büyüme gibi sunmak.
- Tek bir yılın verisinden mevsimsel endeks hesaplamak.

## Pratikte nasıl uygulanır?

- [ ] En az üç yıllık aylık veriyle ürün grubu bazında mevsimsel endeks hesaplayın.
- [ ] Yönetim raporlarına arındırılmış satış ve yıllık değişimi ekleyin.
- [ ] Bayram dönemlerini ayrı bir değişken olarak işaretleyin.
- [ ] Nominal büyümenin yanında, uygun bir fiyat endeksiyle hesaplanmış reel büyümeyi raporlayın.

## Daha fazlası

- Hyndman, R. J.; Athanasopoulos, G. (2021). *Forecasting: Principles and Practice (3rd ed.)*. https://otexts.com/fpp3/
- TÜİK (2026). *Türkiye İstatistik Kurumu (resmî site)*. https://www.tuik.gov.tr
