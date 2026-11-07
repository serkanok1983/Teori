---
id: kb-fmcg-8-13-sales-analytics
title: "Satış analitiği: Nokta düzeyinde veriden karar çıkarmak"
summary: "Satış verisi, toplam rakamların ötesinde, nokta ve ürün düzeyinde okunduğunda asıl değerini verir. Bu kart nokta yoğunlaşmasını, kaybedilen noktaları, ürün boşluklarını ve bu analizlerden somut aksiyon listesi çıkarmayı anlatır."
course: fmcg
category: saha-satis-ekibi
tags: [saha-satis, analitik]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, it-yoneticisi]
level: orta
source_lessons: [FMCG-8.13]
reading_minutes: 3
key_points:
  - "Satışın küçük bir nokta grubunda yoğunlaşması yaygındır; bu grup ayrı bir hizmet modeli gerektirir."
  - "Belirli bir süredir sipariş vermeyen noktalar, kayıp sayılmadan önce geri kazanma listesine alınmalıdır."
  - "Benzer noktalarla karşılaştırma, bir noktanın hangi ürünlerde potansiyelinin altında kaldığını gösterir."
  - "Analitiğin çıktısı rapor değil, temsilcinin bir sonraki ziyarette yapacağı belirli bir iştir."
  - "Müşteri değeri hesabı, hangi noktaya ne kadar kaynak ayrılacağına karar vermeye yardımcı olur."
glossary_terms: [nokta-evreni, sayisal-dagitim, sfa]
related: [kb-fmcg-8-10-sfa-data-driven-selling, kb-fmcg-8-3-salesperson-performance-drivers, kb-fmcg-6-2-outlet-universe-segmentation, kb-fmcg-12-3-analytics-for-decisions, kb-fmcg-13-9-prospecting-account-segmentation]
sources:
  - title: "A Customer Lifetime Value Framework for Customer Selection and Resource Allocation Strategy"
    authors: "Venkatesan, R.; Kumar, V."
    year: 2004
    type: article
    doi: "10.1509/jmkg.68.4.106.42728"
    url: "https://doi.org/10.1509/jmkg.68.4.106.42728"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Marketing 68(4), 106–125."
  - title: "Building a Winning Sales Force"
    authors: "Zoltners, A. A.; Sinha, P.; Lorimer, S. E."
    year: 2009
    type: book
    verified: false
    note: "Kitap; künye kontrol edilmedi."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Aylık satış raporu "hedefin %96'sı" der, ama hangi noktaların düştüğünü, hangi ürünlerin eksik olduğunu ve temsilcinin yarın ne yapması gerektiğini söylemez. Bu kart, satış verisinden haftalık bir aksiyon listesi üreten birkaç temel analizi anlatır.

## Temel fikir

**1. Yoğunlaşma analizi.** Noktalar satışa göre büyükten küçüğe sıralanır ve kümülatif pay hesaplanır. Çoğu bölgede satışın büyük kısmı noktaların küçük bir bölümünden gelir. Bu grup, kaybedildiğinde etkisi en büyük olan gruptur. Ziyaret sıklığı, hizmet seviyesi ve şef ilgisi bu gruba göre ayarlanmalıdır.

**2. Kayıp ve uyuyan noktalar.** Belirli bir süredir (örneğin 60 gün) sipariş vermeyen noktalar listelenir. Bazıları kapanmış, bazıları rakibe geçmiş, bazıları ise yalnızca ihmal edilmiştir. Bu liste, temsilcinin bir sonraki rotasına geri kazanma ziyareti olarak eklenir.

**3. Ürün boşluğu.** Her nokta, benzer büyüklük ve tipteki noktalarla karşılaştırılır. Benzer noktalarda iyi satan ama bu noktada hiç olmayan ürünler, en kolay büyüme fırsatıdır.

**4. Eğilim analizi.** Son üç ayın satışı, bir önceki yılın aynı dönemiyle karşılaştırılır. Sürekli düşen noktalar, bir sorunun erken işareti olabilir: rakip girişi, fiyat sorunu, hizmet aksaması.

**5. Müşteri değeri.** Venkatesan ve Kumar (2004), müşteri yaşam boyu değerini, müşteri seçimi ve kaynak dağıtımı için bir çerçeve olarak kullanmayı önerdi. Çalışmalarında, kaynakları beklenen gelecek değere göre dağıtmanın, geçmiş satışa göre dağıtmaktan daha iyi sonuç verdiğini gösterdiler. Hızlı tüketimde bunun sade bir karşılığı, noktaları yalnızca bugünkü satışa göre değil, büyüme potansiyeline ve hizmet maliyetine göre de değerlendirmektir.

**Rapordan aksiyona.** Zoltners, Sinha ve Lorimer, satış ekibine verilen bilginin değerinin, temsilcinin karar ve davranışlarını değiştirmesine bağlı olduğunu vurgular. Bu nedenle her analizin sonunda "kim, hangi noktada, ne yapacak?" sorusunun cevabı olmalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Nokta sayıları, satış payları ve sipariş tutarı varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b5.py` ile yapılmıştır.

Bir dağıtıcının 1.800 aktif noktası var. Analiz şunları gösteriyor:

- **Yoğunlaşma:** En büyük 360 nokta (%20) satışın %52'sini oluşturuyor. Bu noktalar haftalık ziyaret ve şef takibine alınıyor.
- **Uyuyan noktalar:** 210 nokta son 60 günde sipariş vermemiş. Temsilciler iki hafta içinde hepsini ziyaret ediyor. Yarısı (105 nokta) ayda ortalama 1.500 TL ile yeniden sipariş vermeye başlarsa yıllık **1.890.000 TL** satış geri kazanılır.
- **Ürün boşluğu:** Orta büyüklükteki noktaların üçte birinde, benzer noktalarda en çok satan beş üründen en az ikisi yok. Bu ürünler SFA'da öneri olarak gösteriliyor.

Her temsilci pazartesi sabahı, kendi bölgesi için kısa bir liste alıyor: geri kazanılacak noktalar, ürün boşluğu olan noktalar ve satışı düşen büyük noktalar.

## Sık yapılan hatalar

- **Yalnızca toplamlara bakmak.** Bölge toplamı hedefte görünürken önemli noktalar kaybediliyor olabilir.
- **Uyuyan noktaları hemen kayıp saymak.** Birçoğu tek bir ziyaretle geri kazanılabilir.
- **Analizi temsilciye ulaştırmamak.** Yönetim raporunda kalan analiz sahada davranışı değiştirmez.
- **Çok uzun listeler.** Temsilci yüz maddelik listeyi uygulamaz; en önemli on maddeyi verin.
- **Hizmet maliyetini unutmak.** Satışı yüksek ama hizmet maliyeti çok yüksek bir nokta, göründüğü kadar değerli olmayabilir.

## Pratikte nasıl uygulanır?

- [ ] Nokta düzeyinde satış, ürün ve ziyaret verisini tek bir tabloda birleştirin.
- [ ] Yoğunlaşma, uyuyan nokta ve ürün boşluğu analizlerini her ay otomatik çalıştırın.
- [ ] Her temsilciye haftalık en fazla on maddelik bir aksiyon listesi verin.
- [ ] Listedeki maddelerin sonuçlarını izleyin: Kaç nokta geri kazanıldı, kaç ürün listelendi?
- [ ] Yılda bir, kaynak dağıtımını (ziyaret sıklığı, şef zamanı) nokta değerine göre yeniden ayarlayın.

## Daha fazlası

- Venkatesan, R.; Kumar, V. (2004). *A Customer Lifetime Value Framework for Customer Selection and Resource Allocation Strategy.* Journal of Marketing 68(4), 106–125. https://doi.org/10.1509/jmkg.68.4.106.42728
- Zoltners, A. A.; Sinha, P.; Lorimer, S. E. (2009). *Building a Winning Sales Force.* (kaynak doğrulanmadı)
