---
id: kb-eco-25-1-time-value-npv-irr
title: "Paranın zaman değeri: Net bugünkü değer ve iç verim oranı"
summary: "Bugünkü bir liranın gelecekteki bir liradan neden değerli olduğunu, gelecekteki nakit akışlarını iskonto ederek net bugünkü değeri hesaplamayı ve iç verim oranını sermaye maliyetiyle karşılaştırmayı anlatır."
course: eco
category: kurumsal-finans
tags: [finans, yatirim, karar-verme]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: temel
source_lessons: [ECO-25.1]
reading_minutes: 3
key_points:
  - "Gelecekteki nakit, bugünkü nakitten daha az değerlidir; aradaki farkı iskonto oranı belirler."
  - "Net bugünkü değer, tüm nakit akışlarının bugüne iskonto edilmiş toplamıdır; pozitifse yatırım değer yaratır."
  - "İç verim oranı, net bugünkü değeri sıfır yapan orandır; sermaye maliyetinden yüksekse yatırım kabul edilebilir."
  - "Toplam nakit girişinin yatırımdan büyük olması, yatırımın kârlı olduğu anlamına gelmez."
glossary_terms: [net-bugunku-deger, ic-verim-orani, iskonto-orani]
related: [kb-eco-31-1-capital-budgeting, kb-eco-31-2-cost-of-capital, kb-eco-18-3-real-vs-nominal-interest-fisher, kb-eco-1-1-opportunity-cost-sunk-cost]
sources:
  - title: "Principles of Finance"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-finance/pages/1-why-it-matters"
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

Yeni bir depo, araç filosu, el terminali yatırımı ya da uzun vadeli bir tedarik anlaşması... Hepsinde bugün para ödeyip gelecekte nakit kazanırsınız. Bu kart, farklı zamanlardaki nakit akışlarını tek bir ölçüye getirip "bu yatırım değer mi?" sorusunu yanıtlamanızı sağlar.

## Temel fikir

Bugünkü 100 TL'yi faize yatırırsanız bir yıl sonra daha fazla paranız olur. Bu yüzden bir yıl sonra alacağınız 100 TL bugün 100 TL'den azdır. Gelecekteki nakdi bugüne çevirmeye **iskonto** denir:

Bugünkü değer = Gelecekteki nakit / (1 + r)ᵗ

Burada r **iskonto oranı**dır; genellikle şirketin sermaye maliyeti ya da yatırımın riskine uygun getiri beklentisidir. Yüksek enflasyon ve yüksek faiz ortamında r de yüksektir; uzak yıllardaki nakit akışları çok daha az değerli hâle gelir.

- **Net bugünkü değer (NBD, *net present value*):** Tüm nakit akışlarının (başlangıç yatırımı dahil) bugünkü değerlerinin toplamı. NBD > 0 ise yatırım, sermaye maliyetinin üzerinde getiri sağlar.
- **İç verim oranı (İVO, *internal rate of return*):** NBD'yi sıfır yapan iskonto oranı. İVO sermaye maliyetinden yüksekse yatırım kabul edilebilir.

İki ölçü genellikle aynı kararı verir. Projeler karşılaştırılırken ya da nakit akışlarının işareti birden çok kez değişirken İVO yanıltabilir; böyle durumlarda NBD'yi esas alın.

Tutarlılık kuralı: Nakit akışları nominal ise nominal iskonto oranı, reel ise reel iskonto oranı kullanın.

## Bir örnek

> **Örnek (temsili rakamlar):** Yatırım tutarı, nakit akışları ve iskonto oranı varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b3.py` ile yapılmıştır.

Bir distribütör 10.000.000 TL'lik bir yatırımla 5 yıl boyunca her yıl 3.500.000 TL nakit tasarruf bekliyor. Toplam nakit girişi 17.500.000 TL; ilk bakışta çok kârlı görünüyor. İskonto oranı %25.

| Yıl | Nakit akışı (TL) | Bugünkü değer (TL) |
|---|---|---|
| 1 | 3.500.000 | 2.800.000 |
| 2 | 3.500.000 | 2.240.000 |
| 3 | 3.500.000 | 1.792.000 |
| 4 | 3.500.000 | 1.433.600 |
| 5 | 3.500.000 | 1.146.880 |

- Bugünkü değerler toplamı: 9.412.480 TL.
- NBD = 9.412.480 − 10.000.000 = **−587.520 TL**.
- İVO **%22,1**; sermaye maliyeti olan %25'in altında.

İskonto oranı %25 iken yatırım değer kaybettirir. Oran %35 olsaydı NBD −2.230.135 TL olurdu.

## Sık yapılan hatalar

- Nakit girişlerini iskonto etmeden toplayıp yatırım tutarıyla karşılaştırmak.
- Nominal nakit akışlarını reel oranla (ya da tersini) iskonto etmek.
- Kâr rakamlarını nakit akışı yerine kullanmak; işletme sermayesi ihtiyacını unutmak.
- İskonto oranını, riskten bağımsız olarak "bankadaki mevduat faizi" kabul etmek.
- Farklı büyüklükteki projeleri yalnızca İVO'ya göre sıralamak; büyük bir projenin NBD'si, İVO'su daha düşük olsa da daha yüksek olabilir.
- Nakit akışlarını yıl sonunda varsaymak yerine gerçekleştikleri döneme göre yerleştirmemek.

## Pratikte nasıl uygulanır?

- [ ] Her yatırım teklifinde yıllara göre nakit akışı tablosu isteyin; kâr değil nakit esas alınsın.
- [ ] Şirket için standart bir iskonto oranı (sermaye maliyeti) belirleyin ve yılda bir güncelleyin.
- [ ] NBD ve İVO'yu birlikte raporlayın; çelişki olursa NBD'ye göre karar verin.
- [ ] Nakit akışlarının nominal mi reel mi olduğunu tabloda açıkça yazın.
- [ ] İskonto oranı ve tasarruf tahmini için duyarlılık tablosu ekleyin.
- [ ] Yatırım tablolarınızda NBD, İVO ve geri ödeme süresini birlikte gösterin.

## Daha fazlası

- OpenStax (2026). *Principles of Finance*. https://openstax.org/books/principles-finance/pages/1-why-it-matters
- CORE Econ (2026). *The Economy 2.0*. https://www.core-econ.org/the-economy/
