---
id: kb-ea-20-5-inventory-in-erp
title: "ERP'de stok: Hareket tipleri, değerleme ve sayım"
summary: "ERP'de stok hareketlerinin (giriş, çıkış, transfer, sayım farkı) nasıl kaydedildiğini, hareketli ortalama ve standart maliyet yöntemlerini, her hareketin muhasebeye etkisini ve dönemsel sayımın rolünü anlatır."
course: ea
category: erp
tags: [erp, stok, degerleme, sayim, depo]
roles: [bayi-sahibi, bayi-yonetici, finans-muduru, depo-lojistik-muduru]
level: orta
source_lessons: [EA-20.5]
reading_minutes: 3
key_points:
  - "Her stok hareketi bir hareket tipiyle kaydedilir ve muhasebeye otomatik yansır."
  - "Hareketli ortalamada her girişten sonra birim maliyet yeniden hesaplanır."
  - "Standart maliyette stok sabit maliyetle tutulur; fark ayrı bir hesaba gider."
  - "Sistem stoğu ile fiziksel stok arasındaki fark sayımla bulunur ve onaylı bir hareketle düzeltilir."
  - "Hareketlerin zamanında girilmemesi stok, maliyet ve sipariş planını birlikte bozar."
glossary_terms: [hareketli-ortalama-maliyet, standart-maliyet, hareket-tipi]
related: [kb-ea-20-3-procure-to-pay, kb-ea-20-2-order-to-cash, kb-ea-20-6-mrp-basics, kb-ea-20-1-what-erp-does]
sources:
  - title: "Integrated Business Processes with ERP Systems"
    authors: "Magal, S. R.; Word, J."
    year: 2011
    type: book
    verified: false
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Sistemde 600 koli görünen ürün rafta 540 koliyse, sipariş planı da maliyet de yanlıştır. Bu kart, ERP'de stoğun nasıl tutulduğunu ve değerlendiğini anlatır.

## Temel fikir

**Hareket tipleri.** ERP'de her stok değişikliği bir hareket tipiyle kaydedilir:

- Satın alma mal kabulü (giriş)
- Satış sevkiyatı (çıkış)
- Depolar arası transfer
- Üretime malzeme çıkışı ve üretimden giriş
- Fire, hurda, numune
- Sayım farkı

Her hareket tipi, hangi muhasebe hesabının etkileneceğini belirler. Örneğin satış sevkiyatı stok hesabını alacaklandırır ve satılan malın maliyeti hesabını borçlandırır.

**Değerleme yöntemleri.** Magal ve Word iki yaygın yöntemi anlatır:

- **Hareketli ortalama:** Her girişten sonra birim maliyet, toplam stok değeri bölü toplam miktar olarak yeniden hesaplanır. Bayi ve dağıtım işlerinde sık kullanılır.
- **Standart maliyet:** Ürün dönem başında belirlenen sabit bir maliyetle tutulur. Gerçek alış fiyatı farklıysa fark, **fiyat farkı hesabına** yazılır. Üretim firmalarında yaygındır; sapmaları görünür kılar.

Türkiye'de yasal kayıtlarda kullanılabilecek değerleme yöntemleri vergi mevzuatıyla belirlenir; yöntem seçimini mali müşavirinizle birlikte yapın.

**Sayım.** Dönemsel veya döngüsel sayım, sistem stoğu ile fiziksel stoğu karşılaştırır. Fark, onaylı bir sayım farkı hareketiyle düzeltilir ve nedeni araştırılır.

### Stok doğruluğunu korumak

ERP'deki stok bilgisinin güvenilir olması, sipariş, satın alma ve finansal raporlamanın temelidir. Stok doğruluğunu korumak için şu uygulamalar önerilir:

- **Hareketlerin zamanında kaydı:** Mal kabul, sevkiyat, iade ve fire işlemlerinin fiziksel hareketle aynı anda sisteme girilmesi gerekir. Gecikmeli kayıtlar, sistemde görünen ile fiziksel stok arasında geçici farklar yaratır ve yanlış kararlara yol açar.
- **Dönüşümlü sayım:** Tüm depoyu yılda bir kez saymak yerine, ürünleri değerine ve hareket hızına göre gruplara ayırarak düzenli aralıklarla saymak, hataların erken bulunmasını sağlar.
- **Fark analizi:** Sayım farklarının yalnızca düzeltilmesi yetmez; nedenleri araştırılmalıdır. Yanlış birim dönüşümü, kayıtsız fire, hatalı toplama veya hırsızlık gibi nedenler ayrı ayrı izlenmelidir.
- **Negatif stoğu engelleyin:** Sistemin negatif stoğa izin vermesi, kayıt hatalarını gizler. Negatif stok oluştuğunda nedeninin hemen araştırılması gerekir.
- **Birim dönüşümleri:** Koli, paket ve adet arasındaki dönüşüm oranlarının doğru tanımlanması, birçok stok farkının önüne geçer.

**Finansal etkiler.** Stok farkları ve değerleme düzeltmeleri, dönem kârını doğrudan etkiler. Sayım sonuçlarının muhasebeye aktarılması, onaylı bir süreçle ve uygun dönemde yapılmalıdır.

**Stokta bekleyen değer.** Yavaş hareket eden ve son kullanma tarihi yaklaşan ürünler düzenli olarak raporlanmalı; indirim, transfer veya imha kararları zamanında verilmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b4.py` ile yapılmıştır.

Bir bayinin deposunda 500 koli, kolisi 20,00 TL'den var. 300 koli daha 24,00 TL'den alınıyor.

- Hareketli ortalama: (500 × 20 + 300 × 24) / 800 = **21,50 TL**
- Stok değeri: **17.200,00 TL**
- 200 koli satıldığında çıkış maliyeti: **4.300,00 TL**; kalan 600 koli: **12.900,00 TL**

Aynı ürün standart maliyetle (21,00 TL) tutulsaydı, 300 kolilik alımda koli başına 3,00 TL'lik fark **900,00 TL** olarak fiyat farkı hesabına giderdi.

## Sık yapılan hatalar

- Sevkiyatı fiilen çıktıktan günler sonra sisteme girmek.
- Fire ve numune çıkışlarını kaydetmeyip farkı yıl sonu sayımında bulmak.
- Sayım farklarını nedenini araştırmadan düzeltmek.
- Standart maliyetleri yıllarca güncellememek.

## Pratikte nasıl uygulanır?

- [ ] Kullandığınız hareket tiplerini ve muhasebe etkilerini bir tabloda listeleyin.
- [ ] Değerleme yöntemini mali müşavirinizle netleştirin.
- [ ] Yüksek değerli ürünler için döngüsel sayım takvimi kurun.
- [ ] Sayım farklarını aylık olarak nedenleriyle raporlayın.

## Daha fazlası

- Magal ve Word, *Integrated Business Processes with ERP Systems* (kitap; doğrulanmadı).
