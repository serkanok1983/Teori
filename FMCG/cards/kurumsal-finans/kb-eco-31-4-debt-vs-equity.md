---
id: kb-eco-31-4-debt-vs-equity
title: "Borç mu özkaynak mı? Finansal kaldıracın iki yüzü"
summary: "Borcun özkaynak kârlılığını ne zaman artırıp ne zaman azalttığını, faiz oranı varlık getirisinden yüksekken kaldıracın neden zarar verdiğini, faiz karşılama oranını ve borç kapasitesini belirlemeyi anlatır."
course: eco
category: kurumsal-finans
tags: [finansman, kurumsal-finans, risk-yonetimi]
roles: [uretici-sahibi, bayi-sahibi, finans-muduru]
level: ileri
source_lessons: [ECO-31.4]
reading_minutes: 3
key_points:
  - "Borç, varlık getirisi faiz oranından yüksekse özkaynak kârlılığını artırır; düşükse azaltır."
  - "Kaldıraç kârdaki dalgalanmayı büyütür; kötü yılda zararı hızla derinleştirir."
  - "Faiz karşılama oranı (faaliyet kârı / faiz gideri) borç kapasitesinin temel göstergesidir."
  - "Şirketler pratikte önce iç kaynak, sonra borç, en son yeni ortak sermayesi kullanma eğilimindedir."
glossary_terms: [finansal-kaldirac, faiz-karsilama-orani]
related: [kb-eco-31-2-cost-of-capital, kb-eco-36-5-dupont, kb-eco-50-3-working-with-banks, kb-eco-32-3-risk-management-stress-test]
sources:
  - title: "Corporate financing and investment decisions when firms have information that investors do not have"
    authors: "Myers, S. C.; Majluf, N. S."
    year: 1984
    type: article
    doi: "10.1016/0304-405X(84)90023-0"
    url: "https://doi.org/10.1016/0304-405X(84)90023-0"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Financial Economics 13(2). Finansman hiyerarşisi."
  - title: "Determinants of corporate borrowing"
    authors: "Myers, S. C."
    year: 1977
    type: article
    doi: "10.1016/0304-405X(77)90015-0"
    url: "https://doi.org/10.1016/0304-405X(77)90015-0"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Financial Economics 5(2)."
  - title: "The theory and practice of corporate finance: evidence from the field"
    authors: "Graham, J. R.; Harvey, C. R."
    year: 2001
    type: article
    doi: "10.1016/S0304-405X(01)00044-7"
    url: "https://doi.org/10.1016/S0304-405X(01)00044-7"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Financial Economics 60(2–3). Şirketlerin NBD/İVO ve sermaye maliyeti uygulamaları."
  - title: "Testing Trade-Off and Pecking Order Predictions About Dividends and Debt"
    authors: "Fama, E. F.; French, K. R."
    year: 2002
    type: article
    doi: "10.1093/rfs/15.1.1"
    url: "https://doi.org/10.1093/rfs/15.1.1"
    verified: true
    checked_on: 2026-10-28
    note: "Review of Financial Studies 15(1)."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Büyümek için ek kaynak gerekiyor: banka kredisi mi, yoksa ortakların sermaye artırımı mı? Bu kart, borcun özkaynak kârlılığına etkisini hesaplamanızı ve sağlıklı bir borç seviyesine karar vermenizi sağlar.

## Temel fikir

**Kaldıraç etkisi:** Varlıklarınız faaliyet kârı (FVÖK) olarak yüzde x getiri sağlıyorsa ve borcun faizi x'ten düşükse, borçla finanse edilen kısım ortaklara ek getiri bırakır. Faiz x'ten yüksekse borç, özkaynak kârlılığını düşürür. Yüksek faiz dönemlerinde bu, "borçla büyümenin" sanıldığı kadar kârlı olmadığı anlamına gelir.

**Risk:** Faiz gideri sabittir; satış ve kâr dalgalanır. Kötü bir yılda faaliyet kârı faiz giderinin altına düşerse şirket zarar eder ve nakit sıkışır. Myers (1977), yüksek borcun şirketleri değerli yatırımlardan bile vazgeçirebileceğini gösterdi.

**Şirketler pratikte nasıl seçer?** Myers ve Majluf'un (1984) bilgi asimetrisi modelinden doğan hiyerarşi yaklaşımına (*pecking order*) göre şirketler önce iç kaynakları (birikmiş kâr), sonra borcu, en son yeni ortak sermayesini tercih eder. Fama ve French (2002) ve Graham ve Harvey (2001) bu davranışın önemli ölçüde gözlendiğini, ama vergi avantajı ve iflas maliyetleri arasındaki dengenin de rol oynadığını raporladı.

**Faiz karşılama oranı** = FVÖK / faiz gideri. Oran düştükçe şirket kârdaki düşüşlere karşı kırılganlaşır; bankalar da kredi kararında bu orana bakar.

## Bir örnek

> **Örnek (temsili rakamlar):** Varlık, kâr ve faiz tutarları varsayımsaldır; vergi oranı örnek orandır. Hesaplar `scripts/cards_numbers_eco_b3.py` ile yapılmıştır.

Bir distribütörün varlıkları 100.000.000 TL, FVÖK'ü 30.000.000 TL (varlık getirisi %30), örnek vergi oranı %25.

- **Tamamen özkaynakla:** Özkaynak kârlılığı %22,5.
- **50.000.000 TL borç, %40 faizle:** Faiz 20.000.000 TL, net kâr 7.500.000 TL, özkaynak kârlılığı **%15,0**. Faiz varlık getirisinden yüksek olduğu için borç kârlılığı düşürüyor.
- **Aynı borç, %20 faizle:** Net kâr 15.000.000 TL, özkaynak kârlılığı **%30,0**. Faiz düşükken kaldıraç işe yarıyor.

**Kötü yıl:** FVÖK 15.000.000 TL'ye düşerse (%40 faizle) faiz karşılama oranı 1,50 seviyesinden 0,75 seviyesine iner ve şirket 5.000.000 TL zarar eder.

## Sık yapılan hatalar

- Borcun faiz oranını varlık getirisiyle karşılaştırmadan borçla büyümek.
- Yalnızca iyi yıl senaryosuyla borç kapasitesi hesaplamak.
- Kısa vadeli krediyle uzun vadeli yatırım finanse etmek.
- Ortaklardan alınan borçları ve tedarikçi finansmanını kaldıraç hesabına katmamak.
- Banka kredi sözleşmelerindeki finansal taahhütleri (*covenant*) izlememek.
- Ortak borçlarını (ortaklardan alınan borçları) özkaynak gibi görmek; bankalar ve vergi idaresi bunları farklı değerlendirebilir.

## Pratikte nasıl uygulanır?

- [ ] Varlık getirinizi ve ortalama borç maliyetinizi her çeyrek karşılaştırın.
- [ ] Faiz karşılama oranı ve net borç / FAVÖK için şirket içi alt sınırlar belirleyin.
- [ ] Borç planını, kârın %30–50 düştüğü bir stres senaryosuyla test edin.
- [ ] Büyüme finansmanında önce işletme sermayesini iyileştirme seçeneklerini değerlendirin.
- [ ] Sermaye yapısı kararlarında mali danışmanınızla birlikte vergi ve hukuki etkileri gözden geçirin.
- [ ] Ortaklardan alınan borçlar için yazılı sözleşme yapın ve faiz koşullarını vergi danışmanınızla değerlendirin.

## Daha fazlası

- Myers, S. C.; Majluf, N. S. (1984). *Corporate financing and investment decisions when firms have information that investors do not have*. https://doi.org/10.1016/0304-405X(84)90023-0
- Myers, S. C. (1977). *Determinants of corporate borrowing*. https://doi.org/10.1016/0304-405X(77)90015-0
- Graham, J. R.; Harvey, C. R. (2001). *The theory and practice of corporate finance: evidence from the field*. https://doi.org/10.1016/S0304-405X(01)00044-7
- Fama, E. F.; French, K. R. (2002). *Testing Trade-Off and Pecking Order Predictions About Dividends and Debt*. https://doi.org/10.1093/rfs/15.1.1
