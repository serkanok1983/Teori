---
id: kb-fmcg-8-10-sfa-data-driven-selling
title: "Satış otomasyonu (SFA) ve veriyle satış"
summary: "Satış otomasyon sistemi, temsilcinin elindeki tablet ya da telefon üzerinden sipariş, ziyaret ve mağaza verisini toplar. Bu kart SFA'nın temel işlevlerini, önerilen sipariş ve zorunlu ürün uyarılarını, sistemi benimsetmeyi ve veri kalitesini anlatır."
course: fmcg
category: saha-satis-ekibi
tags: [saha-satis, dijital, analitik]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, it-yoneticisi]
level: temel
source_lessons: [FMCG-8.10, EA-25.3]
reading_minutes: 3
key_points:
  - "SFA; ziyaret planı, sipariş, mağaza kontrolü, tahsilat ve raporlamayı tek bir uygulamada toplar."
  - "Sistemin asıl değeri veri toplamak değil, temsilciye ziyaret sırasında ne yapacağını söylemektir."
  - "Önerilen sipariş ve zorunlu ürün uyarıları, dağıtım ve sepet büyüklüğünü doğrudan artırabilir."
  - "Araştırmalar, müşteri ilişkileri yazılımlarının faydasının büyük ölçüde ürettikleri müşteri bilgisinin kullanılmasından geldiğini gösterir."
  - "Veri kalitesi izlenmezse sistem yanlış kararları hızlandırır."
glossary_terms: [sfa, erp, zorunlu-urun-listesi, sayisal-dagitim]
related: [kb-fmcg-8-2-structured-sales-call, kb-fmcg-8-13-sales-analytics, kb-fmcg-8-5-territory-routing, kb-fmcg-12-2-change-digital-transformation, kb-fmcg-9-5-perfect-store]
sources:
  - title: "Why Do Customer Relationship Management Applications Affect Customer Satisfaction?"
    authors: "Mithas, S.; Krishnan, M. S.; Fornell, C."
    year: 2005
    type: article
    doi: "10.1509/jmkg.2005.69.4.201"
    url: "https://doi.org/10.1509/jmkg.2005.69.4.201"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Marketing 69(4), 201–209."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Kâğıt siparişten tablete geçmek tek başına satışı artırmaz. Artış, sistemin temsilciye doğru zamanda doğru bilgiyi vermesinden gelir: Bu noktada hangi ürün eksik, geçen ay ne alındı, hangi promosyon aktif? Bu kart, SFA yatırımından gerçek fayda almanızı sağlar.

## Temel fikir

**SFA'nın temel işlevleri.**

- **Ziyaret planı ve rota:** Günün noktaları, sırası ve konumu.
- **Sipariş:** Fiyat, iskonto ve promosyonların otomatik uygulanması; siparişin anında ERP'ye aktarılması.
- **Mağaza kontrolü:** Bulunurluk, raf payı, fiyat etiketi ve teşhir verisinin toplanması; gerektiğinde fotoğraf.
- **Tahsilat:** Açık alacak, vade ve tahsil edilen tutar.
- **Raporlama:** Temsilci, şef ve yönetici için günlük göstergeler.

**Veriden aksiyona.** SFA'nın asıl gücü, toplanan veriyi ziyaret sırasında öneriye dönüştürmesidir:

- **Önerilen sipariş:** Noktanın geçmiş satışına, mevcut stoğuna ve sezona göre hesaplanan sipariş önerisi.
- **Zorunlu ürün uyarısı:** Noktada bulunması gereken ama bulunmayan ürünlerin listesi.
- **Fırsat uyarısı:** Benzer noktalarda iyi satan ama bu noktada hiç denenmemiş ürünler.
- **Tahsilat uyarısı:** Vadesi geçmiş alacak varsa siparişten önce hatırlatma.

**Benimseme.** Mithas, Krishnan ve Fornell (2005), müşteri ilişkileri yönetimi (CRM) uygulamalarının müşteri memnuniyetine katkısının büyük ölçüde müşteri bilgisini artırmaları yoluyla ortaya çıktığını gösterdi. Yani değer, yazılımın kendisinden değil, ürettiği bilginin kullanılmasından gelir. Sahada bunun anlamı şudur: Temsilci sistemi yalnızca sipariş girmek için kullanıyorsa, öneri ve uyarıların değeri ortaya çıkmaz. Sistem hızlı, çevrimdışı çalışabilen ve temsilcinin işini kolaylaştıran bir araç olmalıdır.

**Veri kalitesi.** Konum verisi olmayan ziyaretler, sahte mağaza kontrolleri, eksik ürün kodları sistemi güvenilmez kılar. Veri kalitesi göstergeleri (konumlu ziyaret oranı, fotoğraf doğrulama oranı, eksik alan oranı) düzenli izlenmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Nokta sayıları, satış hızı ve fiyat varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b5.py` ile yapılmıştır.

Bir dağıtıcının 1.800 aktif noktası var. Zorunlu listedeki bir ürün 1.080 noktada bulunuyor: sayısal dağıtım **%60,0**. SFA'ya zorunlu ürün uyarısı eklendikten sonra temsilciler ürün eksik olan noktalarda öneriyi sunuyor. Altı ay sonra ürün 1.350 noktada: sayısal dağıtım **%75,0**.

Ek 270 noktanın her biri haftada 4 adet, adedi 25 TL'den satıyorsa yıllık ek satış **1.404.000 TL** olur. Bu artış yalnızca uyarıdan gelmeyebilir; aynı dönemde fiyat ya da reklam değişikliği varsa bunlar ayrıştırılmalıdır. Bir bölgede uyarıyı açıp diğerinde kapalı tutmak, etkiyi ölçmenin en güvenilir yoludur.

## Sık yapılan hatalar

- **Sistemi veri toplama aracı olarak görmek.** Temsilciye geri dönmeyen veri, ek iş yükü olarak algılanır.
- **Çok fazla alan.** Her ziyarette otuz soru, temsilcinin kısa yoldan doldurmasına yol açar.
- **Çevrimdışı çalışmayan uygulama.** Bağlantı sorunu olan bölgelerde sipariş kaybolur.
- **Önerilen siparişi zorunlu kılmak.** Temsilci ve nokta sahibi öneriyi düzeltemiyorsa güven kaybolur.
- **Veri kalitesini izlememek.** Hatalı veriyle verilen kararlar, sistemsiz kararlardan kötü olabilir.

## Pratikte nasıl uygulanır?

- [ ] SFA'dan beklediğiniz iki ya da üç somut sonucu belirleyin; örneğin dağıtım ve kalem sayısı.
- [ ] Mağaza kontrolü sorularını en önemli birkaç konuya indirin.
- [ ] Önerilen sipariş ve zorunlu ürün uyarılarını bir pilot bölgede deneyin ve kontrol bölgesiyle karşılaştırın.
- [ ] Veri kalitesi göstergelerini haftalık raporlayın.
- [ ] Temsilcilerden düzenli geri bildirim alın ve uygulamayı buna göre sadeleştirin.

## Daha fazlası

- Mithas, S.; Krishnan, M. S.; Fornell, C. (2005). *Why Do Customer Relationship Management Applications Affect Customer Satisfaction?.* Journal of Marketing 69(4), 201–209. https://doi.org/10.1509/jmkg.2005.69.4.201
