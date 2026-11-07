---
id: kb-eco-19-3-supply-shocks-cost-inflation
title: "Arz şokları ve maliyet enflasyonu: Enerji ve hammadde zammını fiyata nasıl yansıtmalı?"
summary: "Enerji, hammadde ve kur kaynaklı maliyet artışlarının ürün maliyetine etkisini maliyet yapısına göre hesaplamayı ve fiyat artışını yüzde marjı mı yoksa TL marjı mı koruyarak yapmanın farkını anlatır."
course: eco
category: makroekonomi-ve-enflasyon
tags: [enflasyon, maliyet, fiyatlama]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [ECO-19.3]
reading_minutes: 2
key_points:
  - "Arz şoku, talepten bağımsız olarak maliyetleri artıran olaydır; fiyat artarken hacim düşebilir."
  - "Bir maliyet kalemindeki artışın ürün maliyetine etkisi, o kalemin maliyet içindeki payıyla çarpılarak bulunur."
  - "Yüzde marjı korumak, TL marjı korumaktan daha büyük fiyat artışı gerektirir."
  - "Fiyat artışını parçalara bölüp gerekçelendirmek, müşteri ve kanal kabulünü kolaylaştırır."
glossary_terms: [arz-soku, marj]
related: [kb-eco-1-3-supply-demand, kb-eco-14-2-inflation-measurement-tufe-ufe, kb-fmcg-5-6-pricing-in-high-inflation, kb-eco-22-1-exchange-rates-real-nominal]
sources:
  - title: "The Economy 2.0"
    authors: "CORE Econ"
    year: 2026
    type: web
    url: "https://www.core-econ.org/the-economy/"
    verified: true
    checked_on: 2026-10-28
  - title: "Enflasyon Verileri — Tüketici Fiyatları"
    authors: "TCMB"
    year: 2026
    type: web
    url: "https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Istatistikler/Enflasyon+Verileri"
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

Enerji fiyatı, ambalaj, hammadde ya da kur sıçradığında üretici yeni fiyat listesi hazırlar, distribütör de bunu müşteriye anlatmak zorunda kalır. Bu kart, maliyet artışının ürün maliyetine gerçekte ne kadar yansıdığını hesaplamanızı ve fiyat artışını hangi hedefle (yüzde marj mı, TL marj mı) yapacağınızı belirlemenizi sağlar.

## Temel fikir

**Arz şoku** (*supply shock*), talepten bağımsız olarak üretim maliyetini değiştiren olaydır: enerji fiyatlarında artış, hasat kaybı, küresel hammadde fiyatları, kur hareketi, tedarik zinciri kesintisi. Talep kaynaklı enflasyondan farkı, fiyat artarken hacmin genellikle düşmesidir.

Maliyet etkisi basit bir ağırlıklı ortalama ile hesaplanır:

Ürün maliyetindeki artış = Σ (kalemin maliyet içindeki payı × kalemdeki artış)

Fiyata yansıtırken iki hedef arasında seçim yaparsınız:

- **Yüzde marjı korumak:** Fiyatı maliyetle aynı oranda artırırsınız. Birim başına kazandığınız TL artar; müşteriye "maliyet artışından fazla zam" gibi görünebilir.
- **TL marjı korumak:** Fiyatı yalnızca maliyet artışının TL tutarı kadar artırırsınız. Yüzde marj düşer; ama yüksek enflasyonda sabit giderleriniz de arttığından TL marj yetmeyebilir.

Doğru seçim, kendi faaliyet giderlerinizin ne kadar arttığına ve rakiplerin ne yaptığına bağlıdır. Arz şoku tüm sektörü etkiliyorsa, rakipler de fiyat artıracağından hacim kaybı sınırlı kalabilir.

## Bir örnek

> **Örnek (temsili rakamlar):** Maliyet yapısı ve artış oranları varsayımsaldır; hesaplar `scripts/cards_numbers_eco_b2.py` ile yapılmıştır.

Bir ürünün maliyet yapısı: hammadde %50, enerji %10, işçilik %15, lojistik %10, diğer %15.

Enerji %80, hammadde %20 artıyor; diğer kalemler sabit.

- Maliyet artışı = 0,10 × 0,80 + 0,50 × 0,20 = **%18**.
- Fiyat 100 TL, maliyet 82 TL iken marj 18 TL (%18). Yeni maliyet 96,76 TL.

**Yüzde marjı korumak:** Yeni fiyat **118,00 TL** (%18 artış).

**TL marjı korumak:** Yeni fiyat **114,76 TL** (%14,76 artış); yüzde marj %15,7'e düşer.

Aradaki fark, rakip fiyatları ve kendi gider artışınız ışığında pazarlık alanınızdır.

## Sık yapılan hatalar

- Enerji fiyatı %80 arttı diye ürün fiyatını %80 artırmaya çalışmak; maliyet payını hesaba katmamak.
- Yalnızca doğrudan maliyetlere bakıp lojistik ve faaliyet giderlerindeki artışı unutmak.
- Geçici bir şoku kalıcı fiyat artışıyla karşılamak ya da kalıcı bir şoku geçici sanmak.
- Fiyat artışını müşteriye gerekçesiz duyurmak.
- Distribütör olarak, üretici zammını marjınızı koruyacak şekilde müşteri fiyatına yansıtmayı geciktirmek.
- Maliyet şokunu geçici sayıp fiyat güncellemesini geciktirmek; bu sürede stok eski fiyatla satılır ve yerine koyma maliyeti karşılanmaz.

## Pratikte nasıl uygulanır?

- [ ] Ana ürün gruplarınız için maliyet yapısını (kalem payları) yazılı hâle getirin ve yılda bir güncelleyin.
- [ ] Enerji, hammadde ve kur için aylık izleme tablosu oluşturun; maliyet etkisini otomatik hesaplayın.
- [ ] Fiyat artışlarında yüzde marj ve TL marj seçeneklerini, rakip fiyatlarıyla birlikte değerlendirin.
- [ ] Müşteriye duyurularda artışın kaynağını (ör. enerji ve hammadde) kısa ve sade biçimde açıklayın.
- [ ] Distribütör olarak, eski fiyatlı stoğun ne zaman biteceğini ve yeni fiyatın ne zaman uygulanacağını planlayın.
- [ ] Ana girdi maliyetleri (enerji, ambalaj, navlun) için aylık bir maliyet endeksi tutun ve fiyat güncellemelerini bu endekse bağlayın.

## Daha fazlası

- CORE Econ (2026). *The Economy 2.0*. https://www.core-econ.org/the-economy/
- TCMB (2026). *Enflasyon Verileri — Tüketici Fiyatları*. https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Istatistikler/Enflasyon+Verileri
