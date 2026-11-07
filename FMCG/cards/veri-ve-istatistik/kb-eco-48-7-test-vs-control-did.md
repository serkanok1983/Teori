---
id: kb-eco-48-7-test-vs-control-did
title: "Test ve kontrol bölgesi: Fark-içinde-fark yöntemi"
summary: "Bir kampanya, fiyat değişikliği veya yeni dağıtım modelinin etkisini, test bölgesindeki değişimi benzer bir kontrol bölgesindeki değişimle karşılaştırarak ölçen fark-içinde-fark yöntemini ve varsayımlarını anlatır."
course: eco
category: veri-ve-istatistik
tags: [istatistik, deney, kampanya, etki-analizi]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: ileri
source_lessons: [ECO-48.7]
reading_minutes: 3
key_points:
  - "Önce-sonra karşılaştırması, kampanyanın etkisini genel eğilimle karıştırır."
  - "Fark-içinde-fark, test grubundaki değişimden kontrol grubundaki değişimi çıkarır."
  - "Temel varsayım: Uygulama olmasaydı iki grup benzer eğilimi izleyecekti (paralel eğilim)."
  - "Uygulama öncesi dönemlerde iki grubun eğilimini karşılaştırmak, varsayımı sınamanın en basit yoludur."
glossary_terms: [fark-icinde-fark, kontrol-grubu, paralel-egilim]
related: [kb-eco-47-4-ab-testing-significance, kb-eco-47-5-correlation-regression-basics, kb-eco-49-1-time-series-seasonality, kb-eco-47-3-sampling-confidence]
sources:
  - title: "Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania: Reply"
    authors: "Card, D.; Krueger, A. B."
    year: 2000
    type: article
    doi: "10.1257/aer.90.5.1397"
    url: "https://doi.org/10.1257/aer.90.5.1397"
    verified: true
    checked_on: 2026-10-28
    note: "American Economic Review 90(5). Asgari ücret ve istihdam tartışması; aynı zamanda fark-içinde-fark yöntemine klasik örnek."
  - title: "Using the Longitudinal Structure of Earnings to Estimate the Effect of Training Programs"
    authors: "Ashenfelter, O.; Card, D."
    year: 1984
    type: article
    doi: "10.3386/w1489"
    url: "https://doi.org/10.3386/w1489"
    verified: true
    checked_on: 2026-10-28
    note: "NBER Working Paper 1489. Fark-içinde-fark yaklaşımının erken uygulaması."
  - title: "How Much Should We Trust Differences-in-Differences Estimates?"
    authors: "Bertrand, M.; Duflo, E.; Mullainathan, S."
    year: 2002
    type: article
    doi: "10.3386/w8841"
    url: "https://doi.org/10.3386/w8841"
    verified: true
    checked_on: 2026-10-28
    note: "NBER Working Paper 8841."
  - title: "Introductory Statistics 2e"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/introductory-statistics-2e/pages/1-introduction"
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

Kampanyalar, yeni satış modelleri veya fiyat değişiklikleri genellikle önce bir bölgede denenir. Ancak dönem içinde enflasyon, mevsim ve pazar genelindeki değişimler de satışı etkiler. Bu kart, uygulamanın gerçek etkisini ayıklamak için kontrol bölgesi kullanmayı anlatır.

## Temel fikir

**Önce-sonra hatası:** Test bölgesindeki satış artışının tamamını kampanyaya bağlamak. Oysa artışın bir kısmı her yerde yaşanan genel eğilimdir.

**Fark-içinde-fark (FİF):**

Etki = (Test bölgesindeki değişim) − (Kontrol bölgesindeki değişim)

Kontrol bölgesi, uygulama yapılmasaydı test bölgesinde ne olacağının tahminini verir. Yöntem, ekonomide asgari ücret ve eğitim programlarının etkisini ölçmek için yaygın biçimde kullanılmıştır (Ashenfelter ve Card, 1984; Card ve Krueger, 2000).

**Paralel eğilim varsayımı:** Uygulama olmasaydı iki bölgenin satışları benzer oranda değişecekti. Uygulama öncesi aylarda iki bölgenin eğilimleri karşılaştırılarak kontrol edilir.

**Dikkat:** Tek bir test ve tek bir kontrol bölgesiyle yapılan analizlerde standart hatalar olduğundan küçük görünebilir (Bertrand, Duflo ve Mullainathan, 2002). Mümkünse birden fazla bölge kullanın.

### Kontrol bölgesini nasıl seçersiniz?

- **Benzerlik:** Kontrol bölgesi, müşteri yapısı, kanal karması ve geçmiş satış eğilimi bakımından test bölgesine benzemeli.
- **Bulaşma olmamalı:** Test bölgesindeki kampanya kontrol bölgesine taşmamalı. Örneğin komşu ilçelerdeki bayiler aynı toptancıdan alım yapıyorsa, kampanya kontrol bölgesindeki satışları da etkileyebilir.
- **Eş zamanlı olaylar:** Uygulama dönemi boyunca sadece test bölgesini etkileyen başka bir gelişme (yeni rakip, yol çalışması, büyük bir müşteri kaybı) olmamalı.
- **Rastgele seçim:** Mümkünse hangi bölgelerin test olacağını kura ile belirleyin. Satış ekibinin "en iyi bölgeleri" seçmesi sonucu yukarı yanlı yapar.

### Sonucu nasıl raporlarsınız?

Tek bir etki rakamı yerine bir aralık verin ve varsayımları açıkça yazın: kontrol bölgesi, ölçüm dönemi, paralel eğilim kontrolü. Etkiyi kampanya maliyetiyle karşılaştırarak artış başına maliyeti hesaplayın. Kampanya sona erdikten sonraki birkaç haftaya da bakın; bazı kampanyalar yalnızca satışı öne çeker ve sonraki dönemde düşüş yaratır. Bu durumda net etki ilk görünenden küçüktür.

## Bir örnek

> **Örnek (temsili rakamlar):** Bölge satışları varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b7.py` ile yapılmıştır.

Bir distribütör, bir bölgede bayilere yeni bir hacim primi sistemi deniyor. Benzer büyüklükteki komşu bölge kontrol olarak seçiliyor. Aylık satış (bin TL):

| | Önce | Sonra | Değişim |
|---|---|---|---|
| Test bölgesi | 1.000 | 1.150 | %15 |
| Kontrol bölgesi | 800 | 880 | %10 |

- Önce-sonra yorumu: Satış 150 bin TL arttı.
- Kontrol bölgesine göre: Uygulama olmasaydı test bölgesinin satışı yaklaşık 1.100 bin TL olacaktı.
- **Fark-içinde-fark: 5 puan, yaklaşık 50 bin TL/ay.**

Hacim priminin aylık maliyeti 50 bin TL'yi aşıyorsa sistem, görünürdeki büyük artışa rağmen kârsızdır.

## Sık yapılan hatalar

- Önce-sonra karşılaştırmasıyla yetinmek.
- Kontrol bölgesini, test bölgesinden çok farklı büyüklük veya yapıda seçmek.
- Uygulama öncesi eğilimleri kontrol etmemek.
- Kontrol bölgesinin de uygulamadan etkilenmesini (ör. bayilerin sınır ötesinden alım yapması) göz ardı etmek.
- Test süresini satış döngüsünden kısa tutmak; siparişleri aylık veren bayilerde birkaç haftalık test yanıltır.

## Pratikte nasıl uygulanır?

- [ ] Uygulamadan önce test ve kontrol bölgelerini belirleyin.
- [ ] En az 6–12 aylık uygulama öncesi veriyle iki bölgenin eğilimini karşılaştırın.
- [ ] Etkiyi hem yüzde hem tutar olarak hesaplayın ve uygulamanın maliyetiyle karşılaştırın.
- [ ] Mümkünse birden fazla test ve kontrol bölgesi kullanın.
- [ ] Kampanya bittikten sonraki birkaç haftayı da ölçüp satışın yalnızca öne çekilip çekilmediğini kontrol edin.

## Daha fazlası

- Card, D.; Krueger, A. B. (2000). *Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania: Reply*. https://doi.org/10.1257/aer.90.5.1397
- Ashenfelter, O.; Card, D. (1984). *Using the Longitudinal Structure of Earnings to Estimate the Effect of Training Programs*. https://doi.org/10.3386/w1489
- Bertrand, M.; Duflo, E.; Mullainathan, S. (2002). *How Much Should We Trust Differences-in-Differences Estimates?*. https://doi.org/10.3386/w8841
- OpenStax (2026). *Introductory Statistics 2e*. https://openstax.org/books/introductory-statistics-2e/pages/1-introduction
