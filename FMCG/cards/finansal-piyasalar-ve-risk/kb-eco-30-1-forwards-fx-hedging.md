---
id: kb-eco-30-1-forwards-fx-hedging
title: "Vadeli kur sözleşmesi ile kur riskinden korunma"
summary: "Vadeli kurun faiz farkından nasıl hesaplandığını, ithalat ödemesini vadeli sözleşmeyle sabitlemenin kur yükseldiğinde ve düştüğünde sonuçlarını ve korunma politikasını nasıl kuracağınızı anlatır."
course: eco
category: finansal-piyasalar-ve-risk
tags: [kur, risk-yonetimi, turev, ithalat]
roles: [finans-muduru]
level: ileri
source_lessons: [ECO-30.1, ECO-32.2]
reading_minutes: 3
key_points:
  - "Vadeli kur, bugünkü kur ile iki para birimi arasındaki faiz farkından türetilir; bir kur tahmini değildir."
  - "Vadeli sözleşme kuru sabitler: Kur yükselirse kazanırsınız, düşerse fırsat kaybı yaşarsınız."
  - "Korunmanın amacı kazanç sağlamak değil, maliyet ve marjı öngörülebilir kılmaktır."
  - "Korunma oranı, vade ve araçları yazılı bir politikayla belirleyin."
glossary_terms: [vadeli-kur, kur-riski]
related: [kb-eco-22-1-exchange-rates-real-nominal, kb-eco-23-2-currency-crises-business, kb-eco-34-8-fx-transactions, kb-eco-32-3-risk-management-stress-test]
sources:
  - title: "Türkiye Cumhuriyet Merkez Bankası (resmî site)"
    authors: "TCMB"
    year: 2026
    type: web
    url: "https://www.tcmb.gov.tr"
    verified: true
    checked_on: 2026-10-28
  - title: "Principles of Finance"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-finance/pages/1-why-it-matters"
    verified: true
    checked_on: 2026-10-28
  - title: "IFRS 9 Financial Instruments"
    authors: "IFRS Foundation"
    year: 2026
    type: standard
    url: "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/"
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

Dolar bazlı bir ithalat siparişi verdiniz, ödeme 90 gün sonra. Ürünü TL olarak bugünden fiyatladınız. Kur 90 günde yükselirse marjınız erir. Bu kart, vadeli kur sözleşmesinin (*forward*) mantığını ve maliyetini anlatır.

## Temel fikir

Vadeli kur sözleşmesi, belirli bir tutarda dövizi gelecekteki bir tarihte bugünden belirlenen kurdan alma ya da satma anlaşmasıdır. Bankalar bu kuru bir tahmine göre değil, faiz farkına göre belirler:

Vadeli kur ≈ Spot kur × (1 + TL faizi × gün/360) / (1 + döviz faizi × gün/360)

Sezgisel açıklama: Banka bugün dövizi alıp size vadede teslim etmek için TL borçlanıp döviz tutar. TL faizi ile döviz faizi arasındaki fark, vadeli kurun spot kurdan yüksek olmasına yol açar. Bu fark (*forward primi*) korunmanın maliyeti gibi görünür, ama aslında faiz farkının yansımasıdır.

**Sonuçlar:**

- Kur vadeli kurun üzerine çıkarsa: Daha ucuza döviz aldığınız için kazanırsınız.
- Kur vadeli kurun altında kalırsa: Spot piyasadan daha ucuza alabilecekken sözleşme kuruyla ödersiniz. Bu bir fırsat kaybıdır.

Her iki durumda da maliyetinizi önceden bildiğiniz için fiyatlama ve marj öngörülebilir olur. Opsiyonlar ise belli bir prim karşılığında yukarı yönlü riski sınırlayıp aşağı yönlü kazancı korur.

Muhasebede korunma işlemlerinin nasıl kaydedileceği raporlama çerçevesine (ör. TFRS 9 korunma muhasebesi) bağlıdır; bu konuda mali müşavirinizle çalışın.

### Korunma politikası

Korunmayı işlem bazında ve kur tahminine göre yapmak, korunmayı spekülasyona dönüştürür. Bunun yerine yazılı bir politika belirleyin:

- **Neyi korursunuz?** Kesinleşmiş döviz borçlarını, sipariş verilmiş ithalatları veya gelecek birkaç ayın tahmini alımlarını.
- **Ne kadarını?** Örneğin kesinleşmiş borçların tamamını, tahmini alımların ise bir kısmını. Tahmin kesinleştikçe oran artırılır.
- **Hangi araçlarla?** Vadeli işlemler, opsiyonlar veya doğal korunma.
- **Kim karar verir?** Yetki sınırları ve onay süreci.

### Vadeli işlemlerin pratik yönleri

- Banka, vadeli işlem için limit tahsis eder ve teminat isteyebilir. Bu limit diğer kredi limitlerinizi etkiler.
- Vadeli kur, bankanın kotasyonuna ve marjına göre değişir. Birden fazla bankadan fiyat almak maliyeti düşürür.
- Kur sizin lehinize hareket ettiğinde "keşke korunmasaydık" demek yaygındır. Korunmanın amacı kazanç değil, öngörülebilirliktir; başarısını marjın istikrarına göre değerlendirin.
- Satış fiyatlarınızı kısa sürede kura göre güncelleyebiliyorsanız, korunma ihtiyacınız daha düşüktür.

## Bir örnek

> **Örnek (temsili rakamlar):** Kur ve faiz oranları varsayımsaldır; banka teklifleri, işlem maliyetleri ve marjlar dahil değildir. Hesaplar `scripts/cards_numbers_eco_b3.py` ile yapılmıştır.

500.000 dolarlık ithalat ödemesi 90 gün sonra. Spot kur 34,00 TL, TL faizi %45, dolar faizi %5.

- Vadeli kur = 34 × (1 + 0,45 × 90/360) / (1 + 0,05 × 90/360) = **37,36 TL** (spot kura göre %9,88 yüksek).
- Sözleşmeyle ödeme 18.679.012 TL'ye sabitlenir.

| Vadede kur | Korunmasız ödeme (TL) | Korunmasıza göre sözleşmenin farkı (TL) |
|---|---|---|
| 32,00 | 16.000.000 | -2.679.012 (fırsat kaybı) |
| 40,00 | 20.000.000 | 1.320.988 (kazanç) |

Satış fiyatınızı 37,36 TL kurla hesapladıysanız, her iki senaryoda da marjınız korunur.

## Sık yapılan hatalar

- Vadeli kuru piyasanın kur tahmini sanmak.
- Korunma işlemini, kur düştüğünde "zarar" diye değerlendirip politikayı bırakmak.
- Ödeme tutarının tamamından fazlasını korumak; spekülatif pozisyona düşmek.
- Satış fiyatlarını spot kurla, maliyeti vadeli kurla hesaplamak.
- Banka teklifindeki marjı ve teminat koşullarını karşılaştırmamak.

## Pratikte nasıl uygulanır?

- [ ] Döviz ödemelerinizi vade tarihine göre listeleyin.
- [ ] Yazılı bir korunma politikası belirleyin: hangi oranı (ör. kesinleşmiş ödemelerin belirli bir yüzdesi), hangi vadeye kadar, hangi araçlarla koruyacağınızı netleştirin.
- [ ] Fiyatlamada kullandığınız kur ile korunma kurunu eşleştirin.
- [ ] En az iki bankadan teklif alıp vadeli kurları karşılaştırın.
- [ ] Muhasebe ve vergi etkisini mali müşavirinizle teyit edin.

## Daha fazlası

- TCMB (2026). *Türkiye Cumhuriyet Merkez Bankası (resmî site)*. https://www.tcmb.gov.tr
- OpenStax (2026). *Principles of Finance*. https://openstax.org/books/principles-finance/pages/1-why-it-matters
- IFRS Foundation (2026). *IFRS 9 Financial Instruments*. https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/
