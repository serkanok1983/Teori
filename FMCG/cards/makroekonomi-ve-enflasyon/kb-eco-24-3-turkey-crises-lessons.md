---
id: kb-eco-24-3-turkey-crises-lessons
title: "Krizlerden dersler: Likidite tamponu ve kriz senaryosu"
summary: "Ekonomik krizlerin şirketleri genellikle kârsızlıktan değil nakitsizlikten vurduğunu, krizlerde tahsilat ve ödeme dengesinin nasıl bozulduğunu ve kaç aylık likidite tamponu tutmanız gerektiğini anlatır."
course: eco
category: makroekonomi-ve-enflasyon
tags: [kriz, nakit-akisi, risk-yonetimi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru]
level: orta
source_lessons: [ECO-24.2, ECO-24.3, ECO-24.4]
reading_minutes: 3
key_points:
  - "Krizlerde şirketler çoğunlukla nakit sıkışıklığı nedeniyle zor duruma düşer."
  - "Tahsilatlar ödemelerden daha hızlı daralır; aradaki fark kendi kaynağınızla kapatılmak zorundadır."
  - "Likidite tamponunu, kriz senaryosundaki aylık nakit açığı ile kaç ay dayanmak istediğinizin çarpımı olarak belirleyin."
  - "Kriz planı, kriz başlamadan yazılmalı ve tetikleyicileri tanımlanmalıdır."
glossary_terms: [likidite-tamponu]
related: [kb-eco-23-2-currency-crises-business, kb-eco-32-3-risk-management-stress-test, kb-eco-38-2-cash-conversion-cycle, kb-eco-50-4-tcmb-policy-rate-credit]
sources:
  - title: "The Twin Crises: The Causes of Banking and Balance-of-Payments Problems"
    authors: "Kaminsky, G. L.; Reinhart, C. M."
    year: 1999
    type: article
    doi: "10.1257/aer.89.3.473"
    url: "https://doi.org/10.1257/aer.89.3.473"
    verified: true
    checked_on: 2026-10-28
    note: "American Economic Review 89(3)."
  - title: "Türkiye Cumhuriyet Merkez Bankası (resmî site)"
    authors: "TCMB"
    year: 2026
    type: web
    url: "https://www.tcmb.gov.tr"
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

Türkiye ekonomisi son on yıllarda birden fazla finansal kriz ve sert kur dalgalanması yaşadı. Bu dönemlerden geçen işletmelerin ortak deneyimi şudur: Kâğıt üzerinde kârlı olan pek çok şirket, nakdi bittiği için zorlandı. Bu kart, krizlere karşı likidite planını somut bir hesapla kurmanızı sağlar.

## Temel fikir

Krizlerin şirket düzeyindeki etkileri genellikle aynı sırayı izler:

1. **Kredi daralması:** Bankalar limitleri kısar, faizler yükselir, vadeler kısalır.
2. **Tahsilat bozulması:** Müşteriler ödemeleri geciktirir, çek ve senet karşılıksız çıkabilir, bazı müşteriler hiç ödeyemez.
3. **Satış düşüşü:** Talep daralır, siparişler ertelenir.
4. **Ödeme baskısı:** Tedarikçiler de sıkıştığı için vade kısaltır ya da peşin ister.

Bu dört etki birleşince tahsilatlar ödemelerden daha hızlı düşer. Aradaki açığı kapatacak kaynak yoksa, şirket kârlı olsa bile ödeme güçlüğüne girer. Kaminsky ve Reinhart (1999), krizlerden önce genellikle hızlı kredi büyümesi yaşandığını gösterir; iyi zamanlarda kolay kredi, kötü zamanlarda kırılganlığı artırır.

**Likidite tamponu**, kriz senaryosunda oluşacak nakit açığını belirli bir süre karşılayacak nakit ve kullanılmamış taahhütlü kredi limitidir. Tamponun büyüklüğü, kriz senaryosundaki aylık açık ile kaç ay dayanmak istediğinize bağlıdır.

### Krizlerden şirketler için çıkarılan dersler

- **Döviz açık pozisyonu:** TL ile kazanıp dövizle borçlanan şirketler, büyük kur sıçramalarında en çok zarar gören gruptur. Döviz borcunu döviz geliri veya korunma araçlarıyla eşleştirmek temel bir disiplindir.
- **Kısa vadeli finansman:** Uzun vadeli varlıkları kısa vadeli kredilerle finanse eden şirketler, bankalar limitleri kıstığında yeniden finansman bulamaz.
- **Müşteri yoğunlaşması:** Cironun büyük kısmını birkaç müşteriden elde eden şirketler, o müşterilerin sorunlarını doğrudan devralır.
- **Kayıt ve şeffaflık:** Kriz dönemlerinde bankalar, mali tabloları güvenilir ve ilişkisi güçlü müşterilerine öncelik verir.

### Kriz anında ilk adımlar

1. Haftalık nakit akışı tahminine geçin; aylık plan yetersiz kalır.
2. Müşteri limitlerini ve vadeleri yeniden gözden geçirin; riskli müşterilerde sevkiyatı teminata bağlayın.
3. Ertelenebilir yatırımları ve harcamaları durdurun.
4. Bankalar ve büyük tedarikçilerle erken ve açık iletişim kurun.
5. Stok seviyesini talepteki düşüşe göre hızla ayarlayın.

Krizler aynı zamanda güçlü bilançolu şirketler için pazar payı kazanma ve uygun fiyatla varlık satın alma fırsatı yaratır.

## Bir örnek

> **Örnek (temsili rakamlar):** Tahsilat, ödeme ve daralma oranları varsayımsaldır; gerçek bir krizin verisini temsil etmez. Hesaplar `scripts/cards_numbers_eco_b2.py` ile yapılmıştır.

Bir distribütörün normal dönemde aylık tahsilatı 40.000.000 TL, ödemeleri 38.000.000 TL.

Kriz senaryosu:

- Tahsilat %30 düşüyor: **28.000.000 TL**.
- Ödemeler yalnızca %10 düşüyor (maaş, kira, vergi kısa sürede azaltılamaz): **34.200.000 TL**.
- Aylık nakit açığı **6.200.000 TL**.

Üç aylık bir kriz dönemine dayanmak için gereken tampon **18.600.000 TL**'dir. Bu tutarın bir kısmı nakit, bir kısmı taahhütlü ve iptal edilemez kredi limiti olabilir.

## Sık yapılan hatalar

- Kriz planını kriz başladıktan sonra yapmak.
- Bankanın verdiği limiti "her zaman kullanılabilir" saymak; kriz anında limitler kısılabilir.
- Büyüme dönemlerinde tüm nakdi stok ve vadeye yatırmak.
- Müşteri riskini yoğunlaşmış tutmak; büyük bir müşterinin ödeyememesi tüm planı bozar.
- Kriz sırasında maliyet kesintilerini geç ve parça parça yapmak.

## Pratikte nasıl uygulanır?

- [ ] Normal ve kriz senaryosu için 13 haftalık nakit akış tablosu hazırlayın.
- [ ] Kaç aylık açığa dayanmak istediğinize yönetimle birlikte karar verin ve tampon hedefini yazılı hâle getirin.
- [ ] Tamponun bir kısmını birden fazla bankada taahhütlü kredi limiti olarak tutun.
- [ ] Erken uyarı göstergeleri belirleyin: gecikme oranı, karşılıksız çek sayısı, banka limit kullanımı.
- [ ] Kriz anında devreye girecek önlemleri (yatırım erteleme, stok azaltma, vade politikası) önceden sıralayın.

## Daha fazlası

- Kaminsky, G. L.; Reinhart, C. M. (1999). *The Twin Crises: The Causes of Banking and Balance-of-Payments Problems*. https://doi.org/10.1257/aer.89.3.473
- TCMB (2026). *Türkiye Cumhuriyet Merkez Bankası (resmî site)*. https://www.tcmb.gov.tr
- CORE Econ (2026). *The Economy 2.0*. https://www.core-econ.org/the-economy/
