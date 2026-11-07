---
id: kb-eco-36-4-ratios-profitability-leverage
title: "Kârlılık ve borçluluk oranları: Bankanın baktığı göstergeler"
summary: "Aktif kârlılığı, özkaynak kârlılığı, kullanılan sermaye getirisi, faiz karşılama oranı ve net borç/FAVÖK oranlarının nasıl hesaplandığını, yüksek enflasyonda nasıl yorumlanacağını ve bir distribütörün bu oranları iç hedeflere nasıl bağlayabileceğini anlatır."
course: eco
category: finansal-analiz
tags: [finansal-analiz, karlilik, borcluluk]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [ECO-36.2, ECO-36.4]
reading_minutes: 3
key_points:
  - "Özkaynak kârlılığı ortakların, kullanılan sermaye getirisi ise işin kendisinin getirisini ölçer."
  - "Faiz karşılama oranı ve net borç/FAVÖK, bankaların kredi kararlarında en çok baktığı göstergelerdendir."
  - "Yüksek enflasyonda nominal özkaynak kârlılığı enflasyonla karşılaştırılmalıdır."
  - "Oranlar tek başına değil, eğilim ve benzer şirketlerle karşılaştırma içinde anlam kazanır."
glossary_terms: [ozkaynak-karliligi, roce, faiz-karsilama-orani, net-borc]
related: [kb-eco-36-5-dupont, kb-eco-33-4-income-statement, kb-eco-33-5-balance-sheet, kb-eco-37-4-distress-signals-z-score]
sources:
  - title: "Valuation: Measuring and Managing the Value of Companies"
    authors: "Koller, T.; Goedhart, M.; Wessels, D. (McKinsey & Company)"
    year: 2020
    type: book
    verified: true
    checked_on: 2026-10-28
  - title: "Principles of Accounting, Volume 1: Financial Accounting"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters"
    verified: true
    checked_on: 2026-10-28
  - title: "Principles of Finance"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-finance/pages/1-why-it-matters"
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

Bankanız kredi limitini yenilerken, bir yatırımcı şirketinize bakarken ya da siz büyük bir müşterinizi değerlendirirken aynı oranlar kullanılır. Bu kart, temel kârlılık ve borçluluk oranlarını hesaplamanızı ve doğru yorumlamanızı sağlar.

## Temel fikir

**Kârlılık oranları:**

- **Aktif kârlılığı (ROA)** = Net kâr / Toplam varlıklar.
- **Özkaynak kârlılığı (ROE)** = Net kâr / Özkaynak. Ortakların yatırdığı paranın getirisidir.
- **Kullanılan sermaye getirisi (ROCE)** = Faaliyet kârı / (Özkaynak + Finansal borçlar). İşin, finansman yapısından bağımsız getirisini gösterir.

**Borçluluk oranları:**

- **Faiz karşılama oranı** = Faaliyet kârı / Finansman giderleri. 1'e yaklaştıkça faiz ödemesi kârın tamamını alır.
- **Net borç / FAVÖK:** Borcun, mevcut kârlılıkla kaç yılda ödenebileceğinin kaba göstergesi.

**Enflasyon düzeltmesi:** Yüksek enflasyonda özkaynak kârlılığını enflasyonla karşılaştırın. Reel ROE ≈ (1 + nominal ROE) / (1 + enflasyon) − 1. Negatif reel ROE, ortakların sermayesinin reel olarak küçüldüğü anlamına gelir.

### Oranları doğru hesaplamak

- **Ortalama bakiye kullanın:** Kârlılık oranlarında pay bir dönemin akışı, payda ise belirli bir tarihteki bakiyedir. Dönem başı ve sonu ortalamasını kullanmak, yıl içinde büyüyen şirketlerde daha doğru sonuç verir.
- **Tek seferlik kalemleri ayırın:** Varlık satışı kârı veya olağandışı giderler oranları bozar.
- **FAVÖK'ü dikkatli kullanın:** FAVÖK, amortisman ve işletme sermayesi ihtiyacını göz ardı eder. Yatırım yoğun bir üretici ile hafif varlıklı bir distribütörün FAVÖK'leri doğrudan karşılaştırılamaz.

### Bankalar ne bakar?

Bankalar ve kredi sigorta şirketleri çoğu zaman net borç/FAVÖK ve faiz karşılama oranına bakar. Kredi sözleşmelerinde bu oranlar için üst veya alt sınırlar (taahhütler) bulunabilir. Bu sınırların aşılması krediyi erken geri çağırma hakkı doğurabilir; bu yüzden kendi bütçenizde bu oranları da izleyin.

### Sektör karşılaştırması

Oranları tek başına değil, benzer işletmelerle ve kendi geçmişinizle karşılaştırın. Distribütörlerde düşük marj ve yüksek devir hızı normaldir; üreticilerde ise marj daha yüksek ama varlık yoğunluğu daha fazladır. Farklı iş modellerini aynı eşiklerle değerlendirmek yanıltıcıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Tutarlar ve enflasyon oranı varsayımsaldır. Rakamlar bilanço ve gelir tablosu kartlarındaki örnek şirkete dayanır. Hesaplar `scripts/cards_numbers_eco_b5.py` ile yapılmıştır.

Örnek distribütör: Faaliyet kârı marjı %5, kullanılan sermaye 60.000.000 TL, net borç 25.000.000 TL.

| Oran | Değer |
|---|---|
| Aktif kârlılığı | %3,3 |
| Özkaynak kârlılığı | %10,0 |
| Kullanılan sermaye getirisi | %16,7 |
| Faiz karşılama oranı | 1,67 |
| Net borç / FAVÖK | 2,08 |

Yorum: ROCE makul görünüyor, ama faiz karşılama oranı düşük; faaliyet kârının büyük kısmı faize gidiyor. Enflasyon %45 iken reel özkaynak kârlılığı **−%24,1**: Şirket nominal olarak kâr ediyor, ama ortakların sermayesi reel olarak eriyor.

## Sık yapılan hatalar

- Yalnızca net kâr marjına bakıp varlık ve sermaye kullanımını ihmal etmek.
- Yüksek enflasyonda nominal ROE'yi başarı olarak görmek.
- FAVÖK'ü kira ve TFRS 16 farklarını düzeltmeden karşılaştırmak.
- Yıl sonu bilançosuyla hesaplanan oranların yıl içindeki durumu yansıttığını varsaymak.
- Banka kovenantlarındaki oran tanımlarını kendi hesaplarınızla karşılaştırmamak.

## Pratikte nasıl uygulanır?

- [ ] Bu beş oranı çeyreklik olarak hesaplayıp eğilimini izleyin.
- [ ] Faiz karşılama oranı ve net borç/FAVÖK için iç alt ve üst sınırlar belirleyin.
- [ ] Banka sözleşmelerindeki oran tanımlarını ve eşiklerini bir tabloda toplayın.
- [ ] Yüksek enflasyon dönemlerinde reel ROE'yi de raporlayın.
- [ ] Oranları benzer büyüklükteki distribütörlerin yayımlanmış tablolarıyla karşılaştırmayı deneyin.

## Daha fazlası

- Koller, T.; Goedhart, M.; Wessels, D. (McKinsey & Company) (2020). *Valuation: Measuring and Managing the Value of Companies*.
- OpenStax (2026). *Principles of Accounting, Volume 1: Financial Accounting*. https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters
- OpenStax (2026). *Principles of Finance*. https://openstax.org/books/principles-finance/pages/1-why-it-matters
