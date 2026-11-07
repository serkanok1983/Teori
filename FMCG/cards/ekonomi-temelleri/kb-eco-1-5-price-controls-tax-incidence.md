---
id: kb-eco-1-5-price-controls-tax-incidence
title: "Vergi ve fiyat tavanı: Yükü kim taşır, raf neden boşalır?"
summary: "Satışa konan bir verginin yükünün alıcı ile satıcı arasında nasıl paylaşıldığını ve fiyat tavanının neden kıtlık yarattığını, dağıtım ve üretim kararları açısından anlatır."
course: eco
category: ekonomi-temelleri
tags: [vergi, fiyatlama, regulasyon]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [ECO-1.5, ECO-11.4, ECO-42.2]
reading_minutes: 3
key_points:
  - "Verginin yasal olarak kimden alındığı, ekonomik yükü kimin taşıdığını belirlemez."
  - "Yük, fiyata daha az duyarlı olan tarafa daha çok biner."
  - "Vergi satılan miktarı düşürür; bu kayıp ne devlete ne şirkete gelir olarak geçer."
  - "Piyasa fiyatının altında bir fiyat tavanı, talep fazlası ve raf boşluğu yaratır."
  - "Vergi veya tavan değişikliğinde fiyat, hacim ve stok planını birlikte güncelleyin."
glossary_terms: [vergi-yansimasi, piyasa-dengesi, talep-esnekligi]
related: [kb-eco-1-3-supply-demand, kb-eco-43-5-otv-stamp-duty, kb-eco-43-4-kdv-vat, kb-eco-42-1-tax-basics-average-marginal]
sources:
  - title: "Principles of Economics 3e, §3.1 Demand, Supply, and Equilibrium in Markets for Goods and Services"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-economics-3e/pages/3-1-demand-supply-and-equilibrium-in-markets-for-goods-and-services"
    verified: true
    checked_on: 2026-10-28
  - title: "The Economy 2.0"
    authors: "CORE Econ"
    year: 2026
    type: web
    url: "https://www.core-econ.org/the-economy/"
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

Bir ürün grubuna yeni bir vergi geldiğinde ya da mevcut vergi artırıldığında iki soru sorulur: Fiyat ne kadar artar ve hacim ne kadar düşer? Fiyatlara üst sınır konduğunda ise başka bir sorun çıkar: Ürün rafta bulunmaz olur. Bu kart, bu iki durumu basit bir arz-talep çerçevesiyle tahmin etmenize yardım eder.

## Temel fikir

**Vergi yansıması** (*tax incidence*), bir verginin gerçek yükünün kimin cebinden çıktığını anlatır. Yasa vergiyi satıcıdan ister; ama satıcı fiyatı artırarak yükün bir kısmını alıcıya aktarabilir. Ne kadar aktarabileceği, iki tarafın fiyata ne kadar duyarlı olduğuna bağlıdır:

- Alıcılar fiyata az duyarlıysa (alışkanlık ürünü, alternatifi az ürün), yükün çoğu alıcıya geçer.
- Alıcılar çok duyarlıysa (ikame ürün bol, özel marka güçlü), yükün çoğu satıcıda kalır.

Vergi, alıcının ödediği fiyat ile satıcının elinde kalan fiyat arasına bir kama sokar. Satılan miktar düşer. Bu düşüşün yarattığı kayıp, kimseye gelir olarak geçmez; ekonomide buna verimlilik kaybı denir.

**Fiyat tavanı** (*price ceiling*), piyasa fiyatının altında bir üst sınırdır. Bu fiyattan alıcılar daha çok, satıcılar daha az satmak ister. Sonuç kıtlıktır: kuyruk, kota, raf boşluğu, kayıt dışı satış ve ürünün daha düşük tavanlı başka bir kalıba taşınması.

## Bir örnek

> **Örnek (temsili rakamlar):** Doğrusal talep (Miktar = 10.000 − 40 × Fiyat) ve arz (Miktar = −2.000 + 60 × Fiyat) varsayılmıştır; rakamlar `scripts/cards_numbers_eco_b1.py` ile hesaplanmıştır. Vergi tutarı gerçek bir oranı temsil etmez.

**Vergisiz denge:** Fiyat 120 TL, miktar 5.200 koli.

**Koli başına 10 TL vergi:**

- Alıcının ödediği fiyat **126 TL** olur: alıcı vergiden 6 TL (%60) taşır.
- Satıcının elinde kalan fiyat **116 TL** olur: satıcı 4 TL (%40) taşır.
- Satılan miktar 4.960 koliye iner; **240 koli** satış kaybolur.
- Devletin vergi geliri 49.600 TL'dir.

Bu örnekte satıcılar fiyata daha duyarlı olduğu (arz eğimi 60, talep eğimi 40) için yükün çoğu alıcıya geçer. Vergiyi yasal olarak alıcının ödediğini varsaysanız da sonuç aynı çıkar.

**Fiyat tavanı 110 TL:** Bu fiyattan alıcılar 5.600 koli istemektedir, satıcılar ise yalnızca 4.600 koli sunar. **1.000 koli** talep karşılanamaz. Bayi açısından bu, sipariş karşılama oranının düşmesi ve müşteriler arasında dağıtım kararı vermek zorunda kalmak demektir.

## Sık yapılan hatalar

- Vergi artışının tamamının fiyata yansıyacağını varsayıp hacim planını değiştirmemek.
- Verginin yalnızca fiyatı etkilediğini düşünmek; oysa ürün karması, kalıp ve kanal tercihi de değişir.
- Fiyat tavanı döneminde kıt malı ilk gelen müşteriye vermek; bu, kilit müşterileri kaçırabilir.
- Tavanın kalkacağı dönemde stok biriktirip mevzuata aykırı stokçuluk riskine girmek; bu konuda hukuk görüşü alın.
- Rakiplerin farklı vergi grubundaki ikame ürünlerini hesaba katmamak.

## Pratikte nasıl uygulanır?

- [ ] Vergi değişikliği duyurulduğunda etkilenen ürünlerin listesini ve geçerlilik tarihini resmî kaynaktan doğrulayın.
- [ ] Geçmiş fiyat artışlarındaki hacim tepkisinden alıcı duyarlılığını kabaca tahmin edin.
- [ ] Fiyat, hacim ve brüt kâr etkisini en az iki senaryo (yüksek ve düşük yansıma) için hesaplayın.
- [ ] Tavan veya kota dönemlerinde kıt ürünü hangi müşteri segmentine nasıl dağıtacağınızı yazılı bir kurala bağlayın.
- [ ] Üretici olarak, vergi değişikliğinin raf fiyatına yansıma takvimini bayilerle önceden paylaşın.

## Daha fazlası

- OpenStax (2026). *Principles of Economics 3e, §3.1 Demand, Supply, and Equilibrium in Markets for Goods and Services*. https://openstax.org/books/principles-economics-3e/pages/3-1-demand-supply-and-equilibrium-in-markets-for-goods-and-services
- CORE Econ (2026). *The Economy 2.0*. https://www.core-econ.org/the-economy/
