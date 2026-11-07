---
id: kb-ea-22-2-multi-currency-inflation-adjust-in-erp
title: "ERP'de çoklu para birimi, paralel defter ve enflasyon düzeltmesi"
summary: "Dövizli işlemlerin ERP'de nasıl kaydedildiğini ve kur farkının nasıl hesaplandığını, yasal ve yönetim raporları için paralel defter mantığını ve TMS 29 ile VUK kapsamındaki enflasyon düzeltmesinin sistemde nasıl ele alındığını anlatır."
course: ea
category: erp
tags: [erp, doviz, kur-farki, enflasyon-muhasebesi, paralel-defter]
roles: [finans-muduru, it-yoneticisi]
level: ileri
source_lessons: [EA-22.2]
reading_minutes: 2
key_points:
  - "Dövizli işlemler hem işlem para biriminde hem yerel para biriminde tutulur."
  - "Fatura ile ödeme arasındaki kur değişimi kur farkı olarak kaydedilir; dönem sonunda açık kalemler değerlenir."
  - "Paralel defter, aynı işlemin farklı muhasebe kurallarına göre ayrı raporlanmasını sağlar."
  - "Enflasyon düzeltmesi, parasal olmayan kalemlerin endeksle yeniden ifade edilmesidir."
  - "Yasal düzenlemeler sık değiştiği için hangi dönemde hangi düzeltmenin zorunlu olduğunu mali müşavirinizle teyit edin."
glossary_terms: [kur-farki, paralel-defter, enflasyon-duzeltmesi]
related: [kb-ea-22-1-chart-of-accounts-tekduzen, kb-ea-22-3-consolidation-close-systems, kb-eco-35-2-inflation-accounting, kb-eco-32-4-finance-in-high-inflation]
sources:
  - title: "Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu (TMS/TFRS)"
    authors: "KGK"
    year: 2026
    type: web
    url: "https://www.kgk.gov.tr/"
    verified: true
    checked_on: 2026-10-28
  - title: "213 sayılı Vergi Usul Kanunu"
    authors: "T.C. Cumhurbaşkanlığı Mevzuat Bilgi Sistemi"
    year: 1961
    type: law
    url: "https://www.mevzuat.gov.tr/"
    verified: true
    checked_on: 2026-10-28
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Türkiye'de birçok üretici hammaddeyi dövizle alır, bazı bayiler ithal ürün satar. Yüksek enflasyon dönemlerinde ise finansal tabloların enflasyona göre düzeltilmesi gündeme gelir. Bu kart, bu iki konunun ERP'de nasıl ele alındığını yönetici diliyle anlatır.

## Temel fikir

**Dövizli işlemler.** ERP, dövizli bir faturayı hem döviz tutarıyla hem de işlem günündeki kurla TL karşılığıyla kaydeder. Ödeme farklı bir kurla yapıldığında aradaki fark **kur farkı** olarak gelir veya gider hesabına gider. Dönem sonunda hâlâ açık olan dövizli alacak ve borçlar, dönem sonu kuruyla değerlenir. Bunun için kur tablosunun her gün güncellenmesi ve hangi kur türünün kullanılacağının (ör. döviz alış, döviz satış) tanımlanması gerekir.

**Paralel defterler.** Bazı firmalar yasal kayıtlarını Vergi Usul Kanunu'na göre, finansal raporlarını TMS/TFRS'ye göre, grup raporlarını da başka bir para birimiyle hazırlamak zorundadır. ERP'deki **paralel defter** özelliği, aynı işlemin farklı kurallara göre ayrı defterlerde tutulmasını sağlar. Böylece yıl sonunda Excel'de dönüşüm tabloları hazırlamak gerekmez.

**Enflasyon düzeltmesi.** TMS 29 ve VUK kapsamındaki enflasyon düzeltmesinin özü, stok, sabit kıymet ve özkaynak gibi **parasal olmayan kalemlerin** fiyat endeksiyle yeniden ifade edilmesidir. ERP'de bu iş için:

- Kalemlerin edinim tarihlerinin doğru tutulması,
- Endeks tablosunun sisteme girilmesi,
- Düzeltme kayıtlarının ayrı bir kayıt tipiyle oluşturulması gerekir.

Hangi dönemler için hangi düzeltmenin zorunlu olduğu yasal düzenlemelerle değişebildiği için, bu kart güncel uygulama durumunu bilerek belirtmez.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; kurlar ve endeks katsayısı uydurmadır. Hesaplar `scripts/cards_numbers_ea_b5.py` ile yapılmıştır.

Bir üretici 10.000 EUR'luk hammadde faturasını 35,00 kurla kaydediyor: **350.000,00 TL**. Ödeme günü kur 36,20: ödenen tutar **362.000,00 TL**. ERP aradaki **12.000,00 TL**'yi kur farkı gideri olarak kaydediyor.

Aynı firmanın 1.000.000,00 TL'lik bir makinesi için düzeltme katsayısı 1,40 kabul edilsin. Düzeltilmiş değer **1.400.000,00 TL**, düzeltme farkı **400.000,00 TL** olur. Makinenin edinim tarihi sistemde yanlış girilmişse katsayı da yanlış seçilir.

## Sık yapılan hatalar

- Kur tablosunu elle ve düzensiz güncellemek.
- Yasal ve yönetim raporlarını ayrı Excel dosyalarında yeniden üretmek.
- Sabit kıymet ve stokların edinim tarihlerini veri taşımada kaybetmek.
- Enflasyon düzeltmesini yıl sonuna bırakıp sistem hazırlığını yapmamak.

## Pratikte nasıl uygulanır?

- [ ] Kur kaynağını ve kur türünü yazılı olarak belirleyin; günlük otomatik aktarım kurun.
- [ ] Hangi raporların hangi muhasebe kuralına göre hazırlandığını listeleyin.
- [ ] Edinim tarihlerinin ERP'de eksiksiz olduğunu kontrol edin.
- [ ] Düzeltme sürecini mali müşavirinizle birlikte test edin.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın. Enflasyon düzeltmesinin vergi ve finansal raporlama kapsamındaki güncel uygulama durumunu mutlaka mali müşavirinize veya bağımsız denetçinize doğrulatın.

## Daha fazlası

- Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu: https://www.kgk.gov.tr/
- Vergi Usul Kanunu: https://www.mevzuat.gov.tr/
