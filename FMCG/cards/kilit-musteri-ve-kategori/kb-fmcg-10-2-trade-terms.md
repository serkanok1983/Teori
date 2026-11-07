---
id: kb-fmcg-10-2-trade-terms
title: "Ticari koşullar: Fatura altı, fatura dışı ve vade"
summary: "Zincirlerle yapılan anlaşmalar; fatura altı iskontolar, ciro primleri, listeleme ve promosyon katkıları ile ödeme vadesinden oluşur. Bu kart her kalemin üreticinin cebine kalan fiyata etkisini, koşulları sadeleştirmeyi ve 6585 sayılı Kanun açısından dikkat edilecek noktaları anlatır."
course: fmcg
category: kilit-musteri-ve-kategori
tags: [kilit-musteri, fiyatlama, mevzuat, zincir-market]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: orta
source_lessons: [FMCG-10.2]
reading_minutes: 3
key_points:
  - "Ticari koşullar fatura altı indirimler, fatura dışı indirimler ve ödeme vadesinden oluşur."
  - "Cep fiyatı, liste fiyatından bütün indirimler ve vadenin finansman maliyeti düşüldükten sonra kalan fiyattır."
  - "Yüksek faiz ortamında vadenin maliyeti, primlerden daha büyük olabilir."
  - "Koşulların mümkün olduğunca performansa bağlanması, karşılığı olmayan indirimleri azaltır."
  - "6585 sayılı Kanun, karşılığı olmayan bazı ücret ve primleri ve tarım ve gıda ürünlerinde ödeme sürelerini düzenler; sözleşmeler hukuk danışmanıyla kontrol edilmelidir."
glossary_terms: [fiyat-selalesi, cep-fiyati, ciro-primi, ticari-harcama, vade, haksiz-ticari-uygulama, kosullu-prim]
related: [kb-fmcg-10-1-key-account-management, kb-fmcg-10-4-negotiating-with-chains, kb-fmcg-1-5-turkish-fmcg-landscape, kb-fmcg-5-5-trade-spend-roi, kb-fmcg-9-1-retailer-economics]
sources:
  - title: "6585 sayılı Perakende Ticaretin Düzenlenmesi Hakkında Kanun"
    authors: "T.C. Mevzuat Bilgi Sistemi"
    year: 2015
    type: law
    url: "https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6585&MevzuatTur=1&MevzuatTertip=5"
    verified: true
    checked_on: 2026-10-28
    note: "Madde 6 (haksız ticari uygulamalar) ve 7 (ödeme süresi) 7435 sayılı Kanunla 2023'te değişti; metin 2026-10-28'de okundu."
  - title: "6102 sayılı Türk Ticaret Kanunu"
    authors: "T.C. Mevzuat Bilgi Sistemi"
    year: 2011
    type: law
    url: "https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6102&MevzuatTur=1&MevzuatTertip=5"
    verified: true
    checked_on: 2026-10-28
  - title: "Category Management Association"
    authors: "Category Management Association"
    year: 2026
    type: web
    url: "https://www.categorymanagement.org/"
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

Bir zincirle yapılan yıllık anlaşmada onlarca kalem bulunabilir: fatura altı iskonto, yıl sonu ciro primi, yeni mağaza açılış katkısı, listeleme ücreti, promosyon katkısı, broşür bedeli, ödeme vadesi. Her biri ayrı ayrı küçük görünür, ama toplamı liste fiyatının önemli bir kısmını oluşturur. Bu kart, ticari koşulların (*trade terms*) toplam etkisini görmenizi ve pazarlığa hazırlanmanızı sağlar.

## Temel fikir

**Üç grup kalem.**

- **Fatura altı indirimler** (*on-invoice*): Faturada doğrudan düşülen iskontolar. Perakendecinin ön marjını oluşturur.
- **Fatura dışı indirimler** (*off-invoice*): Sonradan ödenen ya da mahsup edilen ciro primleri, listeleme ücretleri, promosyon ve teşhir katkıları. Perakendecinin arka marjını oluşturur.
- **Ödeme vadesi:** Ödemenin kaç gün sonra yapılacağı. Faturada görünmez, ama üreticinin finansman maliyetidir.

**Fiyat şelalesi ve cep fiyatı.** Liste fiyatından başlayıp bütün kalemler sırayla düşüldüğünde, üreticinin cebine kalan fiyat (*pocket price*) bulunur. Bu tablo, hangi kalemin ne kadar "sızdırdığını" gösterir.

**Performansa bağlamak.** Koşulsuz verilen bir prim, perakendecinin davranışını değiştirmez. Aynı tutar bir hedefe (büyüme, bulunurluk, teşhir, sipariş disiplini) bağlandığında, üretici karşılığında bir şey alır. Bu tür primlere koşullu prim denir.

**6585 sayılı Kanun açısından.** Kanunun 6. maddesi, 2023'te yapılan değişiklikle, talebi etkileyen bir hizmet karşılığı olmadan açılış, yenileme, ciro açığı gibi adlarla ücret alınmasını ya da sözleşmede belirtilmemiş prim istenmesini haksız ticari uygulamalar arasında sayar. 7. madde ise tarım ve gıda ürünlerinde ölçek kombinasyonuna göre azami ödeme sürelerini belirler. Ayrıntılar için *Türkiye'de hızlı tüketim* kartına bakın. Pratik sonuç şudur: Her fatura dışı kalem için yazılı sözleşmede bir dayanak ve, gerekiyorsa, karşılık gelen bir hizmet tanımlanmalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Oranlar varsayımdır; vade maliyeti yıllık %40 sermaye maliyetiyle hesaplanmıştır; hesaplar `scripts/cards_numbers_fmcg_b6.py` ile yapılmıştır.

Liste fiyatı 100 TL olan bir ürün için bir zincirle yapılan anlaşma:

| Kalem | TL | Kalan |
|---|---|---|
| Liste fiyatı | | 100,00 |
| Fatura altı iskonto (%8) | −8,00 | 92,00 |
| Ciro primi (faturanın %4'ü) | −3,68 | 88,32 |
| Promosyon katkısı (faturanın %3'ü) | −2,76 | 85,56 |
| Vade maliyeti (60 gün) | −6,05 | **79,51** |

Toplamda liste fiyatının 20,49 TL'si müşteriye ya da finansmana gidiyor. En büyük ikinci kalem, faturada hiç görünmeyen vade. Zincir vadeyi 60 günden 90 güne uzatmak isterse, bu talep birim başına yaklaşık **3,02** TL ek maliyet demektir; neredeyse ciro primi kadar. Ürün tarım ve gıda kapsamındaysa, 90 günlük vadenin 7. maddedeki azami sürelerle uyumu da ayrıca kontrol edilmelidir.

## Sık yapılan hatalar

- **Kalemleri ayrı ayrı pazarlık etmek.** Toplam etkiyi görmeden verilen küçük tavizler birikir.
- **Vadeyi bedava saymak.** Yüksek faiz ortamında vade, en pahalı kalem olabilir.
- **Koşulsuz prim vermek.** Karşılığında davranış değişikliği istenmeyen prim, kalıcı bir fiyat indirimidir.
- **Yazılı dayanağı olmayan kalemleri kabul etmek.** Hem mevzuat riski hem de mutabakat sorunu yaratır.
- **Müşteriler arasında koşulları karşılaştırmamak.** Benzer müşterilere çok farklı cep fiyatları, kanal çatışmasına yol açar.

## Pratikte nasıl uygulanır?

- [ ] Her kilit müşteri için fiyat şelalesini çıkarın ve cep fiyatını hesaplayın.
- [ ] Müşteriler arasında cep fiyatlarını karşılaştırın ve farkları gerekçelendirin.
- [ ] Koşulsuz primleri adım adım koşullu primlere dönüştürün.
- [ ] Vade taleplerini her zaman TL karşılığıyla değerlendirin.
- [ ] Sözleşmelerinizi 6585 sayılı Kanun'un 6. ve 7. maddelerine göre hukuk danışmanınızla gözden geçirin.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın.

## Daha fazlası

- T.C. Mevzuat Bilgi Sistemi (2015). *6585 sayılı Perakende Ticaretin Düzenlenmesi Hakkında Kanun.* https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6585&MevzuatTur=1&MevzuatTertip=5
- T.C. Mevzuat Bilgi Sistemi (2011). *6102 sayılı Türk Ticaret Kanunu.* https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6102.pdf
- Category Management Association (2026). *Category Management Association.* https://www.categorymanagement.org/
