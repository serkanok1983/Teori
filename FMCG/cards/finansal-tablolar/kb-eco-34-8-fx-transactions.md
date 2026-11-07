---
id: kb-eco-34-8-fx-transactions
title: "Dövizli işlemler ve kur farkı: İthal ürünün kârı ödeme gününe kadar değişir"
summary: "Dövizli alış ve satışların işlem tarihindeki kurla kaydedilmesini, dönem sonu değerlemesinde ve ödeme anında oluşan kur farklarını, kur farkının brüt marjı nasıl eritebileceğini ve dövizli işlemler için fiyatlama ve korunma kararlarını anlatır."
course: eco
category: finansal-tablolar
tags: [muhasebe, kur-riski, ithalat]
roles: [finans-muduru]
level: ileri
source_lessons: [ECO-34.8]
reading_minutes: 3
key_points:
  - "Dövizli işlemler işlem tarihindeki kurla kaydedilir; döviz borç ve alacaklar dönem sonunda değerlenir."
  - "Ödeme gününe kadar kurdaki her hareket kur farkı geliri veya gideri yaratır."
  - "Kur farkı gelir tablosunda brüt kârın altında görünür; bu yüzden ürün kârlılığı olduğundan yüksek görünebilir."
  - "Döviz borcu ile TL satış arasındaki vade uyumsuzluğu yönetilmelidir."
glossary_terms: [kur-farki, kur-riski, vadeli-kur]
related: [kb-eco-22-1-exchange-rates-real-nominal, kb-eco-23-2-currency-crises-business, kb-eco-32-3-risk-management-stress-test, kb-eco-35-2-inflation-accounting]
sources:
  - title: "IAS 21 The Effects of Changes in Foreign Exchange Rates"
    authors: "IFRS Foundation"
    year: 2026
    type: standard
    url: "https://www.ifrs.org/issued-standards/list-of-standards/ias-21-the-effects-of-changes-in-foreign-exchange-rates/"
    verified: true
    checked_on: 2026-10-28
  - title: "213 sayılı Vergi Usul Kanunu"
    authors: "T.C. Resmî Gazete / Mevzuat Bilgi Sistemi"
    year: 1961
    type: law
    url: "https://www.mevzuat.gov.tr/MevzuatMetin/1.4.213.pdf"
    verified: true
    checked_on: 2026-10-28
    note: "Mevzuat Bilgi Sistemi resmî PDF metni açıldı, kanun adı ve numarası eşleşti (2026-10-28)."
  - title: "Principles of Accounting, Volume 1: Financial Accounting"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters"
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

İthal ürün satan ya da döviz bazlı fiyat listesiyle çalışan bir distribütör için kâr, faturanın kesildiği gün değil ödemenin yapıldığı gün belli olur. Bu kart, kur farkının nasıl oluştuğunu ve ürün kârlılığınızı nasıl etkilediğini görmenizi sağlar.

## Temel fikir

**Kayıt (TMS 21):**

- Dövizli bir alış ya da satış, işlem tarihindeki kurla TL'ye çevrilerek kaydedilir.
- Dönem sonunda döviz cinsinden borç ve alacaklar o günkü kurla yeniden değerlenir; fark kur farkı geliri veya gideri olarak kaydedilir.
- Ödeme veya tahsilat gününde, son değerleme kuru ile ödeme kuru arasındaki fark yine kur farkı olarak kaydedilir.

Vergi açısından değerlemede hangi kurun kullanılacağı Vergi Usul Kanunu'nda düzenlenir; uygulamayı mali müşavirinizle teyit edin.

**Yönetim açısından sorun:** Kur farkı gelir tablosunda genellikle finansman giderleri arasında, brüt kârın altında yer alır. Bu yüzden ürün bazlı brüt marj raporu ithal ürünleri olduğundan kârlı gösterebilir. Ürün kârlılığını kur farkıyla birlikte izlemek gerekir.

**Korunma yolları:** Döviz borcunu döviz geliriyle eşleştirmek, satış fiyatını dövize endekslemek, ödeme vadesini kısaltmak ya da vadeli kur sözleşmesi yapmak.

### Kur riskini ölçmek: döviz pozisyonu

Döviz pozisyonu, döviz cinsinden varlıklar (döviz alacakları, döviz mevduatı, dövize endeksli alacaklar) ile döviz cinsinden yükümlülükler (döviz kredileri, ithalat borçları) arasındaki farktır.

- **Kısa pozisyon:** Döviz borcu, döviz varlığından fazla. Kur yükseldiğinde zarar edersiniz. İthalatçı distribütörlerde tipik durumdur.
- **Uzun pozisyon:** Döviz varlığı fazla. Kur yükseldiğinde kazanırsınız. İhracatçı üreticilerde görülür.

Pozisyonu para birimi ve vade bazında ayrı ayrı izleyin. Bilançoda görünmeyen ama kesinleşmiş sipariş ve sözleşmeler de ekonomik olarak pozisyonun parçasıdır.

### Stok etkisi

İthal ürünlerin stoğu TL olarak kayıtlıdır, ama yerine koyma maliyeti dövize bağlıdır. Kur yükseldiğinde döviz borcunda kur farkı zararı oluşur; aynı anda stok değeri ekonomik olarak artar ve fiyatlara yansıtılabilir. Muhasebe bu iki etkiyi farklı satırlarda ve farklı zamanlarda gösterdiği için, yönetim raporunda ikisini birlikte değerlendirin.

### Fiyatlama

Dövize endeksli fiyat listesi kullanıyorsanız, faturalama kuru (fatura günü, sipariş günü veya ödeme günü kuru) sözleşmede açıkça belirlenmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Kurlar ve tutarlar varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b5.py` ile yapılmıştır.

Bir distribütör 100.000 dolarlık ürünü 60 gün vadeyle ithal ediyor. Fatura tarihinde kur 34 TL; maliyet 3.400.000 TL olarak kaydediliyor.

- Ay sonu kur 35 TL: 100.000 TL kur farkı gideri.
- Ödeme günü kur 36 TL: 100.000 TL ek kur farkı gideri.
- Toplam kur farkı 200.000 TL; ödenen tutar 3.600.000 TL.

Ürünler fatura tarihindeki maliyete %12 marj eklenerek 3.808.000 TL'ye peşin satılmış. Brüt kâr raporu 408.000 TL gösteriyor; kur farkı sonrası gerçek kâr yalnızca **208.000 TL**. Kârın yaklaşık yarısı kura gitmiş.

## Sık yapılan hatalar

- Ürün kârlılığını kur farkını dahil etmeden ölçmek.
- Döviz bazlı alım yapıp TL ile, uzun vadeyle satmak.
- Fiyat listesini fatura günündeki kura göre belirleyip ödeme günündeki kuru dikkate almamak.
- Dönem sonu kur değerlemesini yapmayıp kârı yüksek göstermek.
- Korunma maliyetini, korunmamanın beklenen maliyetiyle karşılaştırmamak.

## Pratikte nasıl uygulanır?

- [ ] Döviz pozisyonunuzu (döviz varlık ve borçları, vadeleriyle) haftalık izleyin.
- [ ] Ürün ve tedarikçi bazlı kârlılık raporuna kur farkını dağıtın.
- [ ] İthal ürünlerde fiyatlamayı beklenen ödeme günü kuruna göre yapın.
- [ ] Açık pozisyon için bir üst sınır belirleyin ve aşan kısmı korunma araçlarıyla kapatmayı değerlendirin.
- [ ] Kur değerlemesinin vergi açısından uygulamasını mali müşavirinizle teyit edin.

## Daha fazlası

- IFRS Foundation (2026). *IAS 21 The Effects of Changes in Foreign Exchange Rates*. https://www.ifrs.org/issued-standards/list-of-standards/ias-21-the-effects-of-changes-in-foreign-exchange-rates/
- T.C. Resmî Gazete / Mevzuat Bilgi Sistemi (1961). *213 sayılı Vergi Usul Kanunu*. https://www.mevzuat.gov.tr/MevzuatMetin/1.4.213.pdf
- OpenStax (2026). *Principles of Accounting, Volume 1: Financial Accounting*. https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters
