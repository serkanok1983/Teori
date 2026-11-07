---
id: kb-fmcg-4-7-launch-forecasting
title: "Lansman tahmini: Deneme ve tekrar alma ile ilk yıl hacmi"
summary: "Yeni bir ürünün ilk yıl satışı, kaç hanenin ürünü deneyeceğine ve denemeden sonra kaçının tekrar alacağına bağlıdır. Bu kart deneme-tekrar mantığıyla basit bir tahmin kurmayı ve dağıtımın tahmini nasıl değiştirdiğini anlatır."
course: fmcg
category: strateji-ve-portfoy
tags: [strateji, inovasyon, analitik, dagitim]
roles: [uretici-sahibi, uretici-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: ileri
source_lessons: [FMCG-4.7]
reading_minutes: 3
key_points:
  - "İlk yıl hacmi, deneme hacmi ile tekrar alım hacminin toplamıdır."
  - "Deneme; hedef hane sayısı, bilinirlik, dağıtım ve deneme oranının çarpımıyla kabaca tahmin edilir."
  - "Uzun vadeli başarıyı deneme değil, tekrar alma belirler; denemesi yüksek ama tekrarı düşük ürün söner."
  - "Dağıtım varsayımı tahminin en hassas kalemlerinden biridir; satış ekibinin taahhüdüyle uyumlu olmalıdır."
glossary_terms: [deneme-tekrar, penetrasyon, agirlikli-dagitim]
related: [kb-fmcg-4-5-stage-gate-innovation, kb-fmcg-3-2-repeat-buying-patterns, kb-fmcg-3-4-mental-physical-availability, kb-fmcg-3-8-market-research-toolkit, kb-fmcg-11-2-demand-forecasting]
sources:
  - title: "NEWS: A Decision-Oriented Model for New Product Analysis and Forecasting"
    authors: "Pringle, L. G.; Wilson, R. D.; Brody, E. I."
    year: 1982
    type: article
    doi: "10.1287/mksc.1.1.1"
    url: "https://doi.org/10.1287/mksc.1.1.1"
    verified: true
    checked_on: 2026-10-28
    note: "Marketing Science 1(1), 1–29."
  - title: "A New Product Growth for Model Consumer Durables"
    authors: "Bass, F. M."
    year: 1969
    type: article
    doi: "10.1287/mnsc.15.5.215"
    url: "https://doi.org/10.1287/mnsc.15.5.215"
    verified: true
    checked_on: 2026-10-28
    note: "Management Science 15(5), 215–227."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Lansman tahmini üretim planını, ambalaj alımını, stok seviyesini ve zincirlere verilen sözleri belirler. Tahmin çok yüksekse son kullanma tarihi geçen stok, çok düşükse boş raf ve kaçan fırsat çıkar. Bu kart, basit bir deneme-tekrar modeliyle mantıklı bir başlangıç tahmini kurmanızı sağlar.

## Temel fikir

**Hacmin iki parçası.** Yeni bir ürünün satışı iki kaynaktan gelir:

- **Deneme** (*trial*): Ürünü ilk kez alan haneler.
- **Tekrar** (*repeat*): Deneyip beğenen ve yeniden alan haneler.

**Denemeyi çarpanlara ayırmak.** Deneyen hane sayısı kabaca şu çarpımdır: hedef hane sayısı × bilinirlik × dağıtım × deneme oranı. Bu mantık, Pringle, Wilson ve Brody'nin (1982) NEWS modeli gibi pazarlama karar modellerinde daha ayrıntılı biçimde kullanılır. Bu modellerde reklam, promosyon ve dağıtım gibi değişkenler deneme ve tekrar alma üzerinden satış tahminine bağlanır.

**Yayılma modelleri.** Bass (1969), yeni ürünlerin benimsenmesini yenilikçi ve taklitçi alıcıların etkileşimiyle açıklayan bir model önerir. Model dayanıklı tüketim malları için geliştirilmiştir. Hızlı tüketimde tekrar alma çok önemli olduğu için deneme-tekrar yaklaşımı genellikle daha pratiktir.

**Tekrar alma belirleyicidir.** Güçlü bir lansman kampanyası denemeyi yükseltebilir. Ürün beklentiyi karşılamıyorsa tekrar düşer ve satış ikinci yılda söner. Bu yüzden test pazarında deneme kadar tekrar oranını da izlemek gerekir.

**Tahmini izlemek.** Lansmandan sonra ilk haftalarda deneme ve tekrar alım oranlarını, dağıtım düzeyini ve stoksuzluğu yakından izleyin. Tahminle gerçekleşme arasındaki fark erken görülürse üretim, promosyon ve dağıtım planı zamanında düzeltilebilir. Lansman tahminlerinin geçmiş doğruluğunu kayıt altına almak, sonraki lansmanlarda varsayımların iyileştirilmesini sağlar.

## Bir örnek

> **Örnek (temsili rakamlar):** Hane sayısı ve oranlar varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b2.py` ile yapılmıştır.

- Hedef hane: 20.000.000
- Yıl sonu bilinirlik: %40
- Ağırlıklı dağıtım: %60
- Bilen ve ürüne ulaşabilen hanelerde deneme oranı: %20
- Deneyenlerin tekrar alma oranı: %35; tekrarlayan hane yılda ortalama 4 adet daha alıyor. Deneme 1 adet.

Hesap:

- Deneyen hane: 20.000.000 × 0,40 × 0,60 × 0,20 = **960.000**
- Tekrarlayan hane: 960.000 × 0,35 = **336.000**
- İlk yıl hacmi: 960.000 + 336.000 × 4 = **2.304.000 adet**
- Hacmin %41,7'si denemeden geliyor.

Satış ekibi yıl sonunda %60 yerine %45 ağırlıklı dağıtıma ulaşırsa, diğer her şey aynıyken hacim **1.728.000 adede** düşer. Dağıtım varsayımını satış ekibinin gerçekçi taahhüdüne göre koyun.

## Sık yapılan hatalar

- **Dağıtımı ilk günden tam varsaymak.** Listeleme, zincir onayı ve sevkiyat zaman alır; dağıtım ay ay artar.
- **Anket niyetini doğrudan deneme oranı saymak.** "Kesin alırım" diyenlerin hepsi almaz; geçmiş lansmanlarınızdan bir düzeltme katsayısı çıkarın.
- **Tekrar oranını iyimser koymak.** Test verisi yoksa benzer ürünlerinizin tekrar oranını kullanın.
- **Yükleme satışını başarı sanmak.** Kanala ilk sevkiyat, tüketicinin denemesi değildir.

## Pratikte nasıl uygulanır?

- [ ] Modeli aylık kurun: bilinirlik ve dağıtımı ay ay artan biçimde girin.
- [ ] Her varsayımın kaynağını yazın: anket, test pazarı, geçmiş lansmanlar, satış ekibinin taahhüdü.
- [ ] İyimser, beklenen ve kötümser senaryo hazırlayın; üretim ve stok planını beklenen senaryoya, ambalaj alımını riskle dengeli kurun.
- [ ] Lansmandan sonra gerçekleşen deneme ve tekrarı tahminle karşılaştırın, modeli güncelleyin.

## Daha fazlası

- Pringle, L. G.; Wilson, R. D.; Brody, E. I. (1982). *NEWS: A Decision-Oriented Model for New Product Analysis and Forecasting.* Marketing Science 1(1), 1–29. https://doi.org/10.1287/mksc.1.1.1
- Bass, F. M. (1969). *A New Product Growth for Model Consumer Durables.* Management Science 15(5), 215–227. https://doi.org/10.1287/mnsc.15.5.215
