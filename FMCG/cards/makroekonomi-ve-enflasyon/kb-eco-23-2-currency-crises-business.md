---
id: kb-eco-23-2-currency-crises-business
title: "Kur krizleri ve şirketler: Döviz borcu ve açık pozisyon nasıl yönetilir?"
summary: "Kur krizlerinin nasıl ortaya çıktığını, TL gelirle döviz borcu taşıyan bir şirketin özkaynağının bir kur şokunda nasıl eridiğini ve açık pozisyonu sınırlamanın yollarını anlatır."
course: eco
category: makroekonomi-ve-enflasyon
tags: [kur, risk-yonetimi, finansman, kriz]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [ECO-23.2]
reading_minutes: 3
key_points:
  - "Kur krizi, bir ülke parasının kısa sürede sert biçimde değer kaybetmesidir; genellikle sermaye çıkışı ve rezerv kaybıyla birlikte gelir."
  - "Geliri TL, borcu döviz olan şirket için kur şoku doğrudan özkaynak kaybıdır."
  - "Döviz pozisyonunu (döviz varlıklar eksi döviz yükümlülükler) düzenli ölçün ve bir sınır belirleyin."
  - "Korunmanın bir maliyeti vardır; ama korunmamanın maliyeti kriz anında şirketi batırabilir."
glossary_terms: [doviz-pozisyonu, kur-riski]
related: [kb-eco-22-1-exchange-rates-real-nominal, kb-eco-30-1-forwards-fx-hedging, kb-eco-24-3-turkey-crises-lessons, kb-eco-32-3-risk-management-stress-test]
sources:
  - title: "A Model of Balance-of-Payments Crises"
    authors: "Krugman, P."
    year: 1979
    type: article
    doi: "10.2307/1991793"
    url: "https://doi.org/10.2307/1991793"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Money, Credit and Banking 11(3)."
  - title: "The Twin Crises: The Causes of Banking and Balance-of-Payments Problems"
    authors: "Kaminsky, G. L.; Reinhart, C. M."
    year: 1999
    type: article
    doi: "10.1257/aer.89.3.473"
    url: "https://doi.org/10.1257/aer.89.3.473"
    verified: true
    checked_on: 2026-10-28
    note: "American Economic Review 89(3)."
  - title: "Fear of Floating"
    authors: "Calvo, G. A.; Reinhart, C. M."
    year: 2000
    type: article
    doi: "10.3386/w7993"
    url: "https://doi.org/10.3386/w7993"
    verified: true
    checked_on: 2026-10-28
    note: "NBER Working Paper 7993."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Döviz kredisi genellikle TL kredisinden düşük faizli görünür. Tedarikçiler de dolar ya da avro bazlı vade sunar. Ama TL ile satış yapan bir şirket için bu borç, sessiz bir risktir. Bu kart, kur krizlerinin mantığını ve döviz pozisyonunuzu nasıl yöneteceğinizi anlatır.

## Temel fikir

**Kur krizi**, bir ülke parasının kısa sürede sert değer kaybıdır. Akademik literatür birkaç mekanizma tanımlar:

- **Temel dengesizlikler:** Krugman (1979), sabit kuru savunan bir merkez bankasının rezervleri tükenirken spekülatif bir saldırıyla kurun aniden çöktüğü bir model sundu.
- **İkiz krizler:** Kaminsky ve Reinhart (1999), bankacılık ve kur krizlerinin sıklıkla birlikte görüldüğünü ve krizlerden önce genellikle kredi genişlemesi yaşandığını gösterdi.
- **Dalgalanma korkusu:** Calvo ve Reinhart (2000), borcu döviz cinsinden olan gelişmekte olan ülkelerin kur hareketlerine karşı neden hassas olduğunu tartıştı.

Şirket açısından kritik kavram **döviz pozisyonudur**: döviz cinsinden varlıklar (döviz alacak, mevduat) eksi döviz cinsinden yükümlülükler (döviz kredisi, döviz bazlı tedarikçi borcu). Pozisyon negatifse (kısa pozisyon), kur arttıkça şirket kaybeder.

Kayıp yalnızca muhasebe kaydı değildir: Borcu ödemek için gereken TL artar, bankalar teminat ister, kredi limitleri daralabilir ve tedarikçiler peşin ödeme talep edebilir.

## Bir örnek

> **Örnek (temsili rakamlar):** Kur, borç ve özkaynak tutarları varsayımsaldır; korunma maliyeti örnek bir faiz farkıyla hesaplanmıştır. Hesaplar `scripts/cards_numbers_eco_b2.py` ile yapılmıştır.

Bir distribütör tüm gelirini TL olarak elde ediyor, ama 2.000.000 dolar döviz kredisi var. Özkaynağı 50.000.000 TL.

- Kur 30 TL iken borcun TL karşılığı 60.000.000 TL.
- Bir kriz döneminde kur 45 TL'ye çıkıyor (%50 artış). Borç **90.000.000 TL** oluyor.
- Kur farkı zararı **30.000.000 TL**; özkaynak 20.000.000 TL'ye iniyor, yani **%60** kayıp.

Borcun 6 aylık kısmını vadeli kur sözleşmesiyle korumanın maliyeti, yıllık %25 örnek faiz farkıyla yaklaşık 7.500.000 TL'dir. Bu tutar yüksek görünür, ama kriz senaryosundaki kayıpla kıyaslanmalıdır.

## Sık yapılan hatalar

- Döviz kredisini yalnızca faiz oranına bakarak TL kredisine tercih etmek.
- Döviz bazlı tedarikçi borçlarını pozisyon hesabına katmamak.
- "Kur bu kadar artmaz" varsayımıyla stres testi yapmamak.
- Kur farkı zararını yalnızca dönem sonunda fark etmek.
- Kriz başladıktan sonra korunma aramak; bu aşamada vadeli işlem fiyatları ve banka limitleri çok daha elverişsizdir.
- Müşterilere verilen sabit TL fiyatlı uzun vadeli teklifleri kriz döneminde güncellememek.

## Pratikte nasıl uygulanır?

- [ ] Döviz pozisyonunuzu para birimi bazında aylık hesaplayın ve yönetim raporuna ekleyin.
- [ ] Özkaynağa oranla bir azami açık pozisyon sınırı belirleyin.
- [ ] Kurda %30 ve %50 artış senaryolarıyla stres testi yapın; nakit ve özkaynak etkisini görün.
- [ ] Döviz gelirleriniz yoksa döviz borcunu sınırlayın ya da vadeli işlemlerle korunun.
- [ ] Kur riskini nasıl yöneteceğinize mali danışmanınız ve bankanızla birlikte karar verin.
- [ ] Teklif ve sözleşmelere kur değişimine bağlı fiyat güncelleme maddesi ekleyin.
- [ ] Döviz pozisyonunuzu ve kısa vadeli döviz borçlarınızı haftalık olarak raporlayın.

## Daha fazlası

- Krugman, P. (1979). *A Model of Balance-of-Payments Crises*. https://doi.org/10.2307/1991793
- Kaminsky, G. L.; Reinhart, C. M. (1999). *The Twin Crises: The Causes of Banking and Balance-of-Payments Problems*. https://doi.org/10.1257/aer.89.3.473
- Calvo, G. A.; Reinhart, C. M. (2000). *Fear of Floating*. https://doi.org/10.3386/w7993
