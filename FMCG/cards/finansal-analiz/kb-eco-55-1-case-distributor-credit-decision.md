---
id: kb-eco-55-1-case-distributor-credit-decision
title: "Vaka: Yeni zincir müşteriye ne kadar vade verilmeli?"
summary: "Bir distribütörün yeni bir zincir market müşterisinin vade talebini brüt kâr, finansman maliyeti ve beklenen kredi zararıyla birlikte değerlendirdiği uygulamalı vaka."
course: eco
category: finansal-analiz
tags: [vaka, kredi-riski, vade, isletme-sermayesi]
roles: [bayi-sahibi, bayi-yonetici, finans-muduru]
level: ileri
source_lessons: [ECO-55.1]
reading_minutes: 3
key_points:
  - "Vade kararı yalnızca satış hacmiyle değil, bağlanan nakdin maliyeti ve beklenen zararla verilir."
  - "Müşteri riski = açık alacak × temerrüt olasılığı × temerrüt hâlinde kayıp oranı."
  - "Uzun vade, iyi görünen bir brüt kârı tamamen eritebilir."
  - "Karşı teklif (daha kısa vade, teminat, DBS) müzakerenin parçası olmalıdır."
glossary_terms: [temerrut-olasiligi, beklenen-kredi-zarari, alacak-tahsil-suresi]
related: [kb-eco-37-3-customer-credit-analysis, kb-eco-37-4-distress-signals-z-score, kb-eco-38-2-cash-conversion-cycle, kb-eco-38-3-distributor-credit-risk-dbs, kb-eco-34-2-receivables-doubtful-debts]
sources:
  - title: "Trade Credit: Theories and Evidence"
    authors: "Petersen, M. A.; Rajan, R. G."
    year: 1997
    type: article
    doi: "10.1093/rfs/10.3.661"
    url: "https://doi.org/10.1093/rfs/10.3.661"
    verified: true
    checked_on: 2026-10-28
    note: "Review of Financial Studies 10(3). Ticari kredinin işlevi."
  - title: "IFRS 9 Financial Instruments"
    authors: "IFRS Foundation"
    year: 2026
    type: standard
    url: "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/"
    verified: true
    checked_on: 2026-10-28
  - title: "Findeks"
    authors: "Kredi Kayıt Bürosu"
    year: 2026
    type: web
    url: "https://www.findeks.com"
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

Satış ekibi büyük bir zincirle anlaşma yapmak ister; zincir ise uzun vade talep eder. Bu vaka, "Bu müşteriyle çalışalım mı, hangi vadeyle?" sorusunu sayılarla yanıtlamanızı sağlar. Önceki kartlarda gördüğünüz kredi analizi, nakit dönüşüm süresi ve beklenen zarar kavramlarını tek bir kararda birleştirir.

## Temel fikir

Bir müşteriye vade vermenin ekonomik sonucu üç kalemden oluşur:

1. **Brüt kâr:** Yıllık satış × brüt kâr marjı.
2. **Finansman maliyeti:** Müşteride bağlı kalan ortalama alacak × sermaye maliyeti. Ortalama alacak yaklaşık olarak aylık satış × (vade ÷ 30) kadardır.
3. **Beklenen kredi zararı:** Açık alacak × temerrüt olasılığı × temerrüt hâlinde kayıp oranı.

Kâr = 1 − 2 − 3. Sonuç negatifse müşteri, cironuzu büyütürken değerinizi azaltır.

### Kararı etkileyen diğer unsurlar

- **Teminat:** Çek, senet, teminat mektubu, DBS veya kredi sigortası, temerrüt hâlinde kayıp oranını düşürür. Ancak teminatın da bir maliyeti vardır ve müşteri bunu fiyatla dengelemek isteyebilir.
- **Kapasite kullanımı:** Deponuzda ve araç filonuzda boş kapasite varsa, yeni müşterinin ek sabit maliyeti düşüktür. Kapasite doluysa yeni müşteri ek yatırım gerektirebilir.
- **Stratejik değer:** Yeni bir bölgeye veya kanala giriş, ilk yıl düşük kârla da olsa değerli olabilir. Bu değeri açıkça yazın ve süreyle sınırlayın.
- **Tedarikçi koşulları:** Hacim artışı tedarikçiden ek prim veya iskonto getiriyorsa, bu da hesaba katılmalıdır.

### Karar kuralı

Vade ve limit kararını kişisel ilişkiye değil, yazılı bir kurala bağlayın. Örneğin: beklenen kâr pozitif değilse vade kısaltılır veya teminat istenir; müşteri bunu kabul etmezse peşin çalışılır. Kuralın istisnalarını kimin onaylayacağını belirleyin. Kararı altı ayda bir, gerçekleşen tahsilat süresi ve kârlılıkla yeniden değerlendirin.

## Bir örnek

> **Örnek (temsili rakamlar):** Müşteri, oranlar ve olasılıklar varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b6.py` ile yapılmıştır.

Zincir, ayda 3.000.000 TL alım ve 75 gün vade öneriyor. Brüt kâr marjınız %9; yıllık brüt kâr 3.240.000 TL. Aylık finansman maliyetiniz %3,5. Kredi ekibi temerrüt olasılığını %6, temerrüt hâlinde kaybı %60 tahmin ediyor.

| | 75 gün | 45 gün |
|---|---|---|
| Ortalama açık alacak | 7.500.000 TL | 4.500.000 TL |
| Yıllık finansman maliyeti | 3.150.000 TL | 1.890.000 TL |
| Beklenen kredi zararı | 270.000 TL | 162.000 TL |
| **Net katkı** | **180.000 TL zarar** | **1.188.000 TL** |

75 gün vadeyle yıllık 36.000.000 TL'lik ciro, şirkete 180.000 TL kaybettiriyor. 45 gün vadeyle aynı müşteri kârlı. Karşı teklif olarak 45 gün vade ya da 75 gün vadeyi DBS veya teminat mektubu karşılığında vermek masaya konabilir.

## Sık yapılan hatalar

- Kararı yalnızca ciro ve brüt kâr üzerinden vermek.
- Finansman maliyetini sıfır saymak, çünkü "zaten kredi kullanmıyoruz" diye düşünmek; özkaynağın da bir maliyeti vardır.
- Temerrüt olasılığını tahmin etmeden, "büyük zincir batmaz" varsayımıyla hareket etmek.
- Sözleşmede vade aşımı için yaptırım (gecikme faizi, sevkiyat durdurma) tanımlamamak.
- Kararı bir kez verip müşterinin ödeme davranışını izlememek.
- Müşterinin diğer tedarikçilere olan borçlarını ve ödeme davranışını araştırmamak.

## Pratikte nasıl uygulanır?

- [ ] Yeni müşteri tekliflerinde yukarıdaki üç kalemli tabloyu standart şablon yapın.
- [ ] Temerrüt olasılığını mali tablolar, Findeks raporu ve ödeme geçmişiyle tahmin edin.
- [ ] Başabaş vadeyi hesaplayın: net katkının sıfıra düştüğü gün sayısı.
- [ ] Uzun vade talebine karşılık teminat, DBS veya fiyat farkı isteyin.
- [ ] İlk altı ay boyunca gerçek tahsilat süresini aylık izleyin.
- [ ] Karar tablosunu standart bir şablona dönüştürüp bütün büyük limit taleplerinde kullanın.

## Daha fazlası

- Petersen, M. A.; Rajan, R. G. (1997). *Trade Credit: Theories and Evidence*. https://doi.org/10.1093/rfs/10.3.661
- IFRS Foundation (2026). *IFRS 9 Financial Instruments*. https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/
- Kredi Kayıt Bürosu (2026). *Findeks*. https://www.findeks.com
