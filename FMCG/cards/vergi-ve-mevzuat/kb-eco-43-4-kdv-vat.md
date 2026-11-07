---
id: kb-eco-43-4-kdv-vat
title: "KDV: İndirim mekanizması, devreden KDV ve nakit etkisi"
summary: "Katma değer vergisinin hesaplanan ve indirilecek KDV farkı üzerinden nasıl ödendiğini, devreden KDV'nin nasıl oluştuğunu ve vadeli satışlarda KDV'nin tahsilattan önce ödenmesinin nakit akışına etkisini anlatır."
course: eco
category: vergi-ve-mevzuat
tags: [vergi, kdv, nakit-akisi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: temel
source_lessons: [ECO-43.4]
reading_minutes: 3
key_points:
  - "Ödenecek KDV = Satışlarda hesaplanan KDV − Alışlarda indirilecek KDV."
  - "İndirilecek KDV fazla ise fark sonraki döneme devreder."
  - "KDV, müşteri ödemesini beklemeden beyan döneminde ödenebilir; vade uzadıkça nakit yükü büyür."
  - "Belgesi uygun olmayan alışların KDV'si indirilemez."
glossary_terms: [kdv, devreden-kdv, indirilecek-kdv]
related: [kb-eco-43-1-turkish-tax-system-overview, kb-eco-38-2-cash-conversion-cycle, kb-eco-42-8-informality-tax-compliance, kb-eco-43-6-tax-procedure-inspection]
sources:
  - title: "3065 sayılı Katma Değer Vergisi Kanunu"
    authors: "T.C. Resmî Gazete / Mevzuat Bilgi Sistemi"
    year: 1984
    type: law
    url: "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.3065.pdf"
    verified: true
    checked_on: 2026-10-28
    note: "Mevzuat Bilgi Sistemi resmî PDF metni açıldı, kanun adı ve numarası eşleşti (2026-10-28)."
  - title: "213 sayılı Vergi Usul Kanunu"
    authors: "T.C. Resmî Gazete / Mevzuat Bilgi Sistemi"
    year: 1961
    type: law
    url: "https://www.mevzuat.gov.tr/MevzuatMetin/1.4.213.pdf"
    verified: true
    checked_on: 2026-10-28
    note: "Mevzuat Bilgi Sistemi resmî PDF metni açıldı, kanun adı ve numarası eşleşti (2026-10-28)."
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28

---

## Ne işe yarar?

KDV, distribütörlerin en büyük vergi ödemesidir ve nakit akışını doğrudan etkiler. Bu kart, KDV'nin nasıl hesaplandığını, ne zaman devrettiğini ve vadeli satışlarda neden finansman yükü yarattığını anlatır.

## Temel fikir

KDV, 3065 sayılı Katma Değer Vergisi Kanunu ile düzenlenir.

- **Hesaplanan KDV:** Satış faturalarında müşteriden tahsil edilen KDV.
- **İndirilecek KDV:** Alış ve gider faturalarında ödenen KDV.
- **Ödenecek KDV** = Hesaplanan − İndirilecek. Beyanname dönemsel olarak verilir ve ödeme izleyen dönemde yapılır.
- **Devreden KDV:** İndirilecek KDV hesaplanandan fazlaysa fark sonraki dönemlere aktarılır. Belirli durumlarda (ör. ihracat, indirimli orana tabi teslimler) iade talep edilebilir.

**Nakit etkisi:** KDV fatura tarihine göre doğar. Müşteriye 90 gün vade verdiyseniz, tahsil etmediğiniz KDV'yi beyan döneminde ödemeniz gerekebilir.

### Distribütör için KDV yönetimi

- **Farklı oranlar:** Aynı distribütör farklı KDV oranlarına tabi ürünler satabilir. Alışlar yüksek, satışlar düşük orana tabiyse sürekli devreden KDV birikebilir. Bu, nakdin vergi dairesinde beklemesi anlamına gelir. İade imkânı olup olmadığını ve şartlarını mali müşavirinizle değerlendirin.
- **KDV tevkifatı:** Bazı işlemlerde alıcı, KDV'nin bir kısmını satıcıya ödemek yerine kendisi beyan edip öder. Bu, hem alıcının hem satıcının nakit akışını etkiler. Hangi işlemlerin tevkifata tabi olduğu mevzuatta belirlenmiştir.
- **İade ve iskonto faturaları:** Satış iadelerinde ve fatura sonrası iskontolarda KDV'nin düzeltilmesi gerekir. Ciro primi ve fiyat farkı faturaları da KDV'ye tabidir.
- **İndirim hakkı süresi:** Alış faturalarındaki KDV'yi indirme hakkının belirli bir süre içinde kullanılması gerekir. Geç kaydedilen faturalar indirim hakkını kaybettirebilir.

### Fiyatlamada KDV

Teklif ve fiyat listelerinde fiyatların KDV hariç mi dahil mi olduğunu her zaman açıkça yazın. Perakende müşteriye KDV dahil fiyat, kurumsal müşteriye KDV hariç fiyat söylenir. Oran değişikliğinde, mevcut sözleşmelerdeki fiyatların nasıl güncelleneceği sözleşmede düzenlenmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Tutarlar varsayımsaldır; KDV oranı **örnek oran**dır. Hesaplar `scripts/cards_numbers_eco_b6.py` ile yapılmıştır.

**Normal ay:** KDV hariç 700.000 TL alım, 1.000.000 TL satış; örnek oran %20.

- Hesaplanan KDV: 200.000 TL
- İndirilecek KDV: 140.000 TL
- **Ödenecek KDV: 60.000 TL**

Satışların tamamı vadeliyse bu 60.000 TL, müşteriden tahsilat yapılmadan ödenir.

**Stok yapılan ay:** Alım yine 700.000 TL ama satış 600.000 TL'de kaldı. Hesaplanan KDV 120.000 TL, indirilecek KDV 140.000 TL. Ödeme yok; **20.000 TL KDV sonraki aya devrediyor.** Bu tutar, satışlar normale dönene kadar nakit olarak bağlı kalır.

## Sık yapılan hatalar

- Vadeli satışlarda KDV'nin tahsilattan önce ödenmesini nakit planına almamak.
- Devreden KDV'yi kasada para gibi görmek; yalnızca gelecekteki KDV'den mahsup edilebilir.
- Uygun belgesi olmayan alışların KDV'sini indirmek.
- Kalem bazında farklı KDV oranlarını faturalarda yanlış uygulamak.
- Kısmi veya tam tevkifat uygulanan işlemleri tanımamak.

## Pratikte nasıl uygulanır?

- [ ] Aylık nakit planına ödenecek KDV'yi ve ödeme tarihini ekleyin.
- [ ] Devreden KDV bakiyesini izleyin; büyüyorsa nedenini (stok, indirimli oran, yatırım) analiz edin.
- [ ] Ürün kartlarındaki KDV oranlarını mevzuat değişikliklerinde güncelleyin.
- [ ] Alış faturalarının belge düzenini ve tedarikçi uyumunu kontrol edin.
- [ ] İade hakkı doğuran işlemler için mali müşavirinizle süreci planlayın.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın.

## Daha fazlası

- T.C. Resmî Gazete / Mevzuat Bilgi Sistemi (1984). *3065 sayılı Katma Değer Vergisi Kanunu*. https://www.mevzuat.gov.tr/MevzuatMetin/1.5.3065.pdf
- T.C. Resmî Gazete / Mevzuat Bilgi Sistemi (1961). *213 sayılı Vergi Usul Kanunu*. https://www.mevzuat.gov.tr/MevzuatMetin/1.4.213.pdf
