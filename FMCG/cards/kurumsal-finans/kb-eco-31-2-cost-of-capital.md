---
id: kb-eco-31-2-cost-of-capital
title: "Sermaye maliyeti: Şirketin asgari getiri hedefi nasıl belirlenir?"
summary: "Özkaynak ve borç maliyetinin ağırlıklı ortalamasıyla sermaye maliyetini hesaplamayı, faizin vergi kalkanını, yatırılan sermayenin getirisini sermaye maliyetiyle karşılaştırmayı ve bu farkın değer yaratma ile ilişkisini anlatır."
course: eco
category: kurumsal-finans
tags: [kurumsal-finans, sermaye-maliyeti, karlilik]
roles: [finans-muduru]
level: ileri
source_lessons: [ECO-31.2]
reading_minutes: 3
key_points:
  - "Sermaye maliyeti, borç verenlerin ve ortakların beklediği getirinin ağırlıklı ortalamasıdır."
  - "Özkaynak bedava değildir; ortaklar borç verenlerden daha yüksek getiri bekler, çünkü daha fazla risk taşır."
  - "Faiz gideri vergiden düşüldüğü için borcun vergi sonrası maliyeti daha düşüktür."
  - "Yatırılan sermayenin getirisi sermaye maliyetinin altındaysa, şirket kâr etse bile değer kaybettirir."
glossary_terms: [aosm, yatirilan-sermaye-getirisi, ozkaynak-maliyeti]
related: [kb-eco-31-1-capital-budgeting, kb-eco-31-4-debt-vs-equity, kb-eco-25-1-time-value-npv-irr, kb-eco-36-4-ratios-profitability-leverage]
sources:
  - title: "Principles of Finance"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-finance/pages/1-why-it-matters"
    verified: true
    checked_on: 2026-10-28
  - title: "Valuation: Measuring and Managing the Value of Companies"
    authors: "Koller, T.; Goedhart, M.; Wessels, D. (McKinsey & Company)"
    year: 2020
    type: book
    verified: true
    checked_on: 2026-10-28
  - title: "The theory and practice of corporate finance: evidence from the field"
    authors: "Graham, J. R.; Harvey, C. R."
    year: 2001
    type: article
    doi: "10.1016/S0304-405X(01)00044-7"
    url: "https://doi.org/10.1016/S0304-405X(01)00044-7"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Financial Economics 60(2–3). Şirketlerin NBD/İVO ve sermaye maliyeti uygulamaları."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Yatırım değerlendirmesinde iskonto oranı, değerlemede iskonto oranı, bayi kârlılığında "yeterli getiri" eşiği... Hepsinin arkasında sermaye maliyeti vardır. Bu kart, şirketiniz için makul bir asgari getiri oranını nasıl belirleyeceğinizi ve neden "kâr ediyoruz" demenin yetmediğini anlatır.

## Temel fikir

Şirket iki kaynakla finanse edilir: borç ve özkaynak. Her ikisinin de bir maliyeti vardır:

- **Borç maliyeti:** Kredilerin faizi. Faiz gideri vergi matrahından düşüldüğü için vergi sonrası maliyet = faiz × (1 − vergi oranı).
- **Özkaynak maliyeti:** Ortakların, aynı riskteki başka bir yatırımda elde edebilecekleri getiri. Ortaklar borç verenlerden sonra ödendiği için daha fazla risk taşır; bu yüzden beklentileri daha yüksektir. Halka açık şirketlerde genellikle risksiz faiz + risk primi biçiminde tahmin edilir; aile şirketinde ortakların gerçekçi alternatif getirisi iyi bir başlangıçtır.

**Ağırlıklı ortalama sermaye maliyeti (AOSM, *WACC*):**

AOSM = özkaynak payı × özkaynak maliyeti + borç payı × vergi sonrası borç maliyeti

Değer yaratma kuralı: **Yatırılan sermayenin getirisi** (vergi sonrası faaliyet kârı / yatırılan sermaye) AOSM'den yüksekse şirket değer yaratır. Koller ve diğerlerinin değerleme yaklaşımı da bu farkı değerin temel belirleyicisi olarak görür.

Yüksek enflasyonda tüm oranlar nominal olarak yüksektir. Getiri ve maliyeti aynı bazda (ikisi de nominal ya da ikisi de reel) karşılaştırmaya dikkat edin.

### Özkaynak maliyetini nasıl tahmin edersiniz?

Halka açık olmayan bir şirket için özkaynak maliyetini kesin olarak hesaplamak mümkün değildir, ama makul bir aralık belirleyebilirsiniz:

- **Risksiz getiri:** Uzun vadeli devlet tahvili faizi (TL bazında çalışıyorsanız TL tahvil faizi).
- **Risk primi:** Hisse senedi piyasasının risksiz getirinin üzerinde beklenen getirisi, şirketin sektör riskine göre ayarlanır.
- **Küçüklük ve likidite primi:** Halka açık olmayan, küçük şirketlerin hisseleri kolay satılamaz; bu yüzden ortaklar daha yüksek getiri bekler.

Pratikte birçok aile şirketi, ortakların "bu paradan en az ne kadar kazanmalıyız" beklentisini açıkça konuşmadan yatırım yapar. Bu beklentiyi bir oran olarak yazmak, yatırım kararlarına disiplin getirir.

### Hesapta dikkat edilecekler

- **Kredi faizini sermaye maliyeti sanmak:** Borç maliyeti, özkaynak maliyetinden düşüktür. Yalnızca kredi faizini kullanmak, riskli projeleri olduğundan cazip gösterir.
- **Tek bir oranı her projeye uygulamak:** Yeni bir ürün grubuna veya bölgeye giriş, mevcut işten daha riskli olabilir ve daha yüksek bir getiri beklentisi gerektirir.
- **Döviz ve TL nakit akışlarını karıştırmak:** Nakit akışları hangi para birimindeyse iskonto oranı da o para biriminde olmalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Oranlar varsayımsaldır; vergi oranı örnek orandır ve güncel kurumlar vergisi oranını temsil etmez. Hesaplar `scripts/cards_numbers_eco_b3.py` ile yapılmıştır.

Bir üreticinin sermaye yapısı: %60 özkaynak, %40 borç. Ortakların beklediği getiri %45, kredi faizi %48, örnek vergi oranı %25.

- Vergi sonrası borç maliyeti = 0,48 × (1 − 0,25) = %36.
- AOSM = 0,60 × 0,45 + 0,40 × 0,36 = **%41,4**.

Şirketin yatırılan sermayesi 80.000.000 TL, yatırılan sermayenin getirisi %35. Şirket muhasebe kârı yazıyor, ama getiri AOSM'nin -6,4 puan altında. Bu yıl yaklaşık **−5.120.000 TL** ekonomik değer kaybı söz konusu.

## Sık yapılan hatalar

- Özkaynağın maliyetini sıfır kabul edip yalnızca kredi faizine bakmak.
- Banka mevduat faizini şirketin sermaye maliyeti olarak kullanmak.
- Nominal getiriyi reel sermaye maliyetiyle karşılaştırmak.
- Tüm projelere, risk düzeyinden bağımsız olarak aynı oranı uygulamak.
- Defter değerli özkaynakla ağırlık hesaplayıp oranları hiç güncellememek.

## Pratikte nasıl uygulanır?

- [ ] Şirketiniz için yılda bir AOSM tahmini yapın ve varsayımları yazılı hâle getirin.
- [ ] Yatırım ve fiyatlama kararlarında AOSM'yi asgari getiri eşiği olarak kullanın.
- [ ] Yatırılan sermayenin getirisini iş birimi, bölge ya da ürün grubu bazında hesaplayın.
- [ ] Riskli projeler (yeni pazar, yeni kanal) için AOSM'nin üzerine risk primi ekleyin.
- [ ] Vergi etkisini mali müşavirinizle teyit edin.

## Daha fazlası

- OpenStax (2026). *Principles of Finance*. https://openstax.org/books/principles-finance/pages/1-why-it-matters
- Koller, T.; Goedhart, M.; Wessels, D. (McKinsey & Company) (2020). *Valuation: Measuring and Managing the Value of Companies*.
- Graham, J. R.; Harvey, C. R. (2001). *The theory and practice of corporate finance: evidence from the field*. https://doi.org/10.1016/S0304-405X(01)00044-7
