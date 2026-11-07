---
id: kb-ea-31-3-route-planning-sales-vs-delivery
title: "Rota planlama: Satış rotası ile dağıtım rotasının farkı"
summary: "Satış temsilcisinin ziyaret rotası ile dağıtım aracının teslimat rotasının farklı amaç ve kısıtlarını, rota optimizasyon yazılımlarının neyi çözdüğünü ve iki planın nasıl uyumlu hale getirileceğini anlatır."
course: ea
category: tedarik-ve-depo-sistemleri
tags: [rota, rota-optimizasyonu, dagitim, satis-rotasi]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, depo-lojistik-muduru]
level: orta
source_lessons: [EA-31.2, EA-31.3]
reading_minutes: 2
key_points:
  - "Satış rotası ziyaret sıklığını, dağıtım rotası günlük teslimatları planlar."
  - "Satış rotası haftalık sabit bir döngüdür; dağıtım rotası her gün siparişlere göre değişir."
  - "Rota optimizasyonu araç kapasitesi, zaman pencereleri ve mesafeyi birlikte dikkate alır."
  - "Satış ve dağıtım günleri uyumlu olmazsa araç aynı bölgeye birçok kez gider."
  - "Doğru nokta konumu her iki rota için de ön koşuldur."
glossary_terms: [rota-optimizasyonu, zaman-penceresi]
related: [kb-ea-31-1-tms-fleet-telematics, kb-ea-26-5-van-sales-presales, kb-ea-28-1-order-management]
sources:
  - title: "Global Logistics and Supply Chain Management"
    authors: "Mangan, J.; Lalwani, C."
    year: 2016
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

Ön satış modelinde iki ayrı rota vardır: temsilcinin ziyaret rotası ve ertesi gün siparişi götüren aracın rotası. İkisi birbirinden habersiz planlandığında araçlar gereksiz yol yapar. Bu kart, iki rotanın farkını ve uyumunu anlatır.

## Temel fikir

**Satış rotası:**

- Amaç: Her noktayı belirlenen sıklıkta ziyaret etmek.
- Genellikle haftalık sabit bir döngüdür (ör. pazartesi A bölgesi).
- Kısıtlar: Ziyaret süresi, nokta sayısı, çalışma saatleri.

**Dağıtım rotası:**

- Amaç: O günün siparişlerini en düşük maliyetle ve zamanında teslim etmek.
- Her gün değişir; siparişe bağlıdır.
- Kısıtlar: Araç kapasitesi, müşteri teslim saatleri (zaman pencereleri), yükleme sırası, sürücü süresi.

**Rota optimizasyonu.** Yazılımlar, noktaların konumu ve kısıtlar verildiğinde toplam mesafeyi veya süreyi azaltan rotayı hesaplar. Sonuç, nokta konumlarının doğruluğuna çok bağlıdır.

**Uyum.** Temsilci pazartesi A bölgesini geziyorsa, siparişler salı aynı bölgeye toplu gitmelidir. Satış rotası bölgeleri dağıtım günleriyle eşleştirildiğinde araç doluluk oranı artar.

### Veri kalitesi ve uygulamada dikkat edilecekler

Rota yazılımının önerisi, ancak beslendiği veri kadar iyidir. Pratikte en sık sorun yaratan veriler şunlardır:

- **Nokta konumu:** Adres metninden üretilen konumlar, özellikle kırsal bölgelerde ve yeni yerleşim alanlarında hatalı olabilir. Temsilcinin ilk ziyarette noktanın konumunu cihazla doğrulaması, en ucuz iyileştirmedir.
- **Ziyaret ve boşaltma süresi:** Büyük bir market ile küçük bir büfede geçen süre çok farklıdır. Tek bir ortalama süre kullanmak rotaları gerçekçi olmaktan çıkarır.
- **Teslim saatleri:** Zincir mağazaların mal kabul saatleri ve şehir içi araç kısıtları sisteme girilmelidir.
- **Araç kapasitesi:** Hem ağırlık hem hacim sınırı dikkate alınmalıdır; içecek gibi ağır ürünlerde ağırlık, atıştırmalık gibi hafif ürünlerde hacim belirleyici olur.

**Planlanan ile gerçekleşenin karşılaştırılması.** Telematik veya mobil uygulama verisiyle, planlanan rota ile sürülen rota düzenli karşılaştırılmalıdır. Sürekli sapma görülen rotalar, ya planın gerçekçi olmadığını ya da sahada bilinmeyen bir kısıt bulunduğunu gösterir. Sürücü ve temsilcinin görüşü alınmadan yapılan rota değişiklikleri genellikle sahada uygulanmaz; bu nedenle değişiklikler küçük bir bölgede denenip sonuçlarına göre yaygınlaştırılmalıdır.

### Ortak planlama toplantısı

Satış ve dağıtım ekiplerinin düzenli aralıklarla birlikte gözden geçirme yapması, iki planın uyumunu korur. Bu toplantıda yeni açılan noktalar, ziyaret günü değişiklikleri, teslim saati talepleri ve gecikme nedenleri ele alınmalıdır. Kararlar müşteri ana verisine işlenmeli; böylece her iki ekip de aynı bilgiyle çalışır. Rota değişikliklerinin müşteriye önceden bildirilmesi, teslimat sırasında yaşanan sorunları azaltır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b7.py` ile yapılmıştır.

Bir aracın günlük ortalama rotası 180 km. Satış ziyaret günleri bölge bazında dağıtım günleriyle eşleştirildikten sonra rota 150 km'ye iniyor: **%16,7** azalma. Aynı araç günde daha fazla nokta teslim edebiliyor.

## Sık yapılan hatalar

- Satış ve dağıtım rotalarını farklı ekiplerin birbirinden habersiz planlaması.
- Nokta konumlarını doğrulamadan optimizasyon yazılımı kullanmak.
- Müşteri teslim saatlerini sisteme girmemek.
- Optimizasyon önerilerini sürücü alışkanlığı nedeniyle uygulamamak.

## Pratikte nasıl uygulanır?

- [ ] Nokta konumlarını doğrulayın.
- [ ] Satış ziyaret günlerini dağıtım bölgeleriyle eşleştirin.
- [ ] Teslim saat aralıklarını müşteri ana verisine ekleyin.
- [ ] Planlanan ve gerçekleşen km'yi haftalık karşılaştırın.

## Daha fazlası

- Mangan ve Lalwani, *Global Logistics and Supply Chain Management* (kitap; doğrulanmadı).
