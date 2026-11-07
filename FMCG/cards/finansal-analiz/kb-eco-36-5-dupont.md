---
id: kb-eco-36-5-dupont
title: "DuPont analizi: Özkaynak kârlılığı nereden geliyor?"
summary: "Özkaynak kârlılığını net kâr marjı, varlık devir hızı ve finansal kaldıraç olarak üçe ayıran DuPont analizini, düşük marjlı ama hızlı dönen bir distribütör ile yüksek marjlı ama yavaş dönen bir şirketi karşılaştırarak ve iyileştirme önceliklerini belirleyerek anlatır."
course: eco
category: finansal-analiz
tags: [finansal-analiz, karlilik]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [ECO-36.5]
reading_minutes: 3
key_points:
  - "ROE = Net kâr marjı × Varlık devir hızı × Finansal kaldıraç."
  - "Distribütörler düşük marjı yüksek varlık devir hızıyla telafi eder."
  - "Kaldıraçla yükseltilmiş ROE daha risklidir."
  - "Analiz, hangi kalemi iyileştirmenin ROE'ye en çok katkı yapacağını gösterir."
glossary_terms: [dupont-analizi, varlik-devir-hizi, finansal-kaldirac, ozkaynak-karliligi]
related: [kb-eco-36-4-ratios-profitability-leverage, kb-eco-38-1-distributor-financial-statements, kb-eco-38-2-cash-conversion-cycle, kb-eco-31-9-three-statement-model]
sources:
  - title: "Principles of Accounting, Volume 1: Financial Accounting"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters"
    verified: true
    checked_on: 2026-10-28
  - title: "Valuation: Measuring and Managing the Value of Companies"
    authors: "Koller, T.; Goedhart, M.; Wessels, D. (McKinsey & Company)"
    year: 2020
    type: book
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

İki şirketin özkaynak kârlılığı aynı olabilir, ama birinin kârlılığı yüksek marjdan, diğerininki yüksek borçtan geliyor olabilir. DuPont analizi bu farkı görünür kılar ve iyileştirme için nereye odaklanmanız gerektiğini gösterir.

## Temel fikir

Özkaynak kârlılığı üç bileşene ayrılır:

**ROE = (Net kâr / Net satışlar) × (Net satışlar / Toplam varlıklar) × (Toplam varlıklar / Özkaynak)**

1. **Net kâr marjı:** Her 100 TL satıştan kalan kâr. Fiyatlama, maliyet ve gider yönetimiyle ilgilidir.
2. **Varlık devir hızı:** Her 1 TL varlıkla yapılan satış. Alacak, stok ve duran varlık verimliliğiyle ilgilidir.
3. **Finansal kaldıraç:** Varlıkların ne kadarının özkaynakla finanse edildiği. Yüksek kaldıraç ROE'yi artırır ama riski de artırır.

Distribütörler için ikinci bileşen kritik önemdedir: Marjlar düşük olduğundan, alacak ve stok süresindeki küçük iyileşmeler varlık devir hızını ve dolayısıyla ROE'yi belirgin şekilde artırır.

### Bileşenleri daha da ayırmak

Varlık devir hızını, varlık kalemlerine göre ayrıştırabilirsiniz: alacak devir hızı, stok devir hızı ve duran varlık devir hızı. Böylece ROE'deki değişimin hangi varlık kaleminden geldiğini görürsünüz.

Net kâr marjını da ayırabilirsiniz: **faaliyet kâr marjı × faiz etkisi × vergi etkisi**. Bu genişletilmiş biçim, kârlılık değişiminin ticari performanstan mı, finansman maliyetinden mi yoksa vergiden mi kaynaklandığını gösterir.

### Karar için kullanmak

DuPont analizini bir hedef ağacı olarak kullanabilirsiniz. Örneğin ROE'yi artırmak için üç yol vardır:

- **Marjı artırmak:** Fiyatlama disiplini, ürün karması, gider kontrolü.
- **Devir hızını artırmak:** Alacak vadesini kısaltmak, yavaş dönen stoğu azaltmak, kullanılmayan varlıkları elden çıkarmak.
- **Kaldıracı artırmak:** Daha fazla borç kullanmak. En kolay ama en riskli yoldur; faiz oranları yüksekken ROE'yi artırmak yerine düşürebilir.

Aynı ROE'ye sahip iki şirketin risk profili, bu bileşenlerin dağılımına göre çok farklı olabilir. Yüksek kaldıraçla elde edilen ROE, faiz artışlarına ve satış düşüşlerine karşı daha kırılgandır.

## Bir örnek

> **Örnek (temsili rakamlar):** İki şirketin rakamları varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b5.py` ile yapılmıştır.

| | A: Distribütör | B: Üretici |
|---|---|---|
| Net satışlar (TL) | 200.000.000 | 120.000.000 |
| Net kâr (TL) | 3.000.000 | 3.600.000 |
| Toplam varlıklar (TL) | 90.000.000 | 100.000.000 |
| Özkaynak (TL) | 30.000.000 | 50.000.000 |
| Net kâr marjı | %1,5 | %3,0 |
| Varlık devir hızı | 2,22 | 1,20 |
| Finansal kaldıraç | 3,00 | 2,00 |
| **ROE** | **%10,0** | **%7,2** |

A'nın marjı B'nin yarısı, ama varlıklarını neredeyse iki kat hızlı döndürüyor ve daha fazla borç kullanıyor. A'nın ROE'si daha yüksek; ancak bunun bir kısmı kaldıraçtan geldiği için A, faiz artışlarına ve kredi daralmasına daha duyarlı.

A için en sağlıklı iyileştirme yolu, borcu artırmak değil, alacak ve stok sürelerini kısaltarak varlık devir hızını yükseltmektir.

## Sık yapılan hatalar

- ROE'yi tek başına değerlendirip kaynağına bakmamak.
- Kaldıraçla gelen ROE artışını operasyonel başarı sanmak.
- Farklı iş modellerini (distribütör ve üretici) yalnızca marjla karşılaştırmak.
- Varlık devir hızını yıl sonu bilançosuna göre hesaplayıp mevsimselliği göz ardı etmek.
- Analizi yapıp sonucu somut hedeflere çevirmemek.
- DuPont bileşenlerini farklı tanımlarla hesaplayıp yıllar arasında karşılaştırmak.

## Pratikte nasıl uygulanır?

- [ ] Son üç yılın DuPont ayrıştırmasını hazırlayın ve hangi bileşenin değiştiğini inceleyin.
- [ ] Varlık devir hızını alacak, stok ve duran varlık bileşenlerine ayırın.
- [ ] Her bileşen için iyileştirme hedefi belirleyin (ör. DSO'da 5 gün azalma).
- [ ] Kaldıraç için bir üst sınır belirleyin.
- [ ] Bütçe ve planlarda ROE hedefini bu üç bileşen üzerinden kurun.
- [ ] DuPont ağacını yıllık bütçenizin hedef yapısına dönüştürün.

## Daha fazlası

- OpenStax (2026). *Principles of Accounting, Volume 1: Financial Accounting*. https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters
- Koller, T.; Goedhart, M.; Wessels, D. (McKinsey & Company) (2020). *Valuation: Measuring and Managing the Value of Companies*.
