---
id: kb-ea-26-2-field-data-outlet-visit
title: "Saha verisinin modeli: Nokta, rut, ziyaret, sipariş, denetim, fotoğraf ve konum"
summary: "Saha satış sisteminde nokta, rut, ziyaret, sipariş, denetim, fotoğraf ve konumla giriş kayıtlarının birbirine nasıl bağlandığını, hangi alanların zorunlu olması gerektiğini ve veri kalitesinin nasıl kontrol edileceğini anlatır."
course: ea
category: saha-satis-ve-dms
tags: [sfa, veri-modeli, nokta, ziyaret, konum]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, it-yoneticisi]
level: orta
source_lessons: [EA-26.2]
reading_minutes: 2
key_points:
  - "Nokta ana verisi saha sisteminin temelidir; her kayıt bir noktaya bağlanır."
  - "Ziyaret, rut planındaki bir noktaya belirli bir tarihte yapılan gerçek ziyaretin kaydıdır."
  - "Sipariş, denetim ve fotoğraf ziyarete bağlanırsa analiz mümkün olur."
  - "Konumla giriş, ziyaretin gerçekten noktada yapıldığını doğrular."
  - "Zorunlu alanlar ve kontrol kuralları veri kalitesini baştan korur."
glossary_terms: [nokta-ana-verisi, konumla-giris]
related: [kb-ea-26-1-retail-execution-sfa, kb-ea-26-3-offline-mode-for-managers, kb-ea-40-4-integrating-sfa-with-erp, kb-ea-8-1-master-data-governance]
sources:
  - title: "A Strategic Framework for Customer Relationship Management"
    authors: "Payne, A.; Frow, P."
    year: 2005
    type: article
    doi: "10.1509/jmkg.2005.69.4.167"
    url: "https://doi.org/10.1509/jmkg.2005.69.4.167"
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

SFA raporları güvenilmezse, çoğu zaman sorun ekranlarda değil veri modelindedir. Bu kart, saha verisinin hangi parçalardan oluştuğunu ve nasıl bağlanması gerektiğini yönetici diliyle anlatır.

## Temel fikir

Saha sisteminin ana kayıtları:

- **Nokta (outlet):** Bakkal, market, kafe gibi satış noktası. Unvan, vergi numarası, adres, koordinat, kanal, sınıf (A/B/C) ve bağlı olduğu distribütör.
- **Rut:** Bir temsilcinin belirli günlerde ziyaret edeceği noktalar listesi ve sırası.
- **Ziyaret:** Rut planındaki bir noktaya yapılan gerçek ziyaret. Başlangıç–bitiş saati, konum, ziyaret sonucu (sipariş alındı, nokta kapalı, yetkili yok).
- **Sipariş:** Ziyarete bağlı sipariş başlığı ve satırları.
- **Denetim:** Mükemmel mağaza kontrol listesi ve puanları.
- **Fotoğraf:** Raf veya soğutucu görüntüsü; ziyaret ve denetim maddesine bağlı.
- **Konumla giriş:** Temsilcinin cihaz konumu ile noktanın kayıtlı koordinatı arasındaki mesafe.

**Bağlantı kuralı:** Sipariş, denetim ve fotoğraf mutlaka bir **ziyarete**, ziyaret de bir **noktaya** bağlı olmalıdır. Böylece "hangi noktada, hangi ziyarette ne oldu?" sorusu yanıtlanabilir.

**Veri kalitesi kontrolleri:**

- Yeni nokta açılışında vergi numarası ve koordinat zorunlu.
- Aynı vergi numarası ile ikinci nokta açılınca uyarı.
- Konumla girişte belirli bir mesafenin dışındaysa gerekçe zorunlu.
- Ziyaret sonucu boş bırakılamaz.

### Modelin raporlamaya etkisi

Saha verisinin modeli, hangi soruların cevaplanabileceğini belirler. Model tasarlanırken, ileride sorulacak yönetim soruları düşünülmelidir:

- **Ziyaret verimliliği:** Planlanan ziyaretlerin ne kadarı gerçekleşti, ne kadarında sipariş alındı? Bunun için planlı ziyaret ile gerçekleşen ziyaretin ayrı kayıtlar olarak tutulması ve birbirine bağlanması gerekir.
- **Nokta gelişimi:** Bir noktanın zaman içinde ürün çeşitliliği, sipariş sıklığı ve raf payı nasıl değişti? Bu, nokta kodunun kalıcı olmasını ve geçmiş kayıtların korunmasını gerektirir.
- **Uygulama kalitesi:** Denetimlerde hangi kriterlerde sık sorun çıkıyor? Denetim cevaplarının serbest metin yerine yapılandırılmış alanlarda tutulması, analiz imkânı sağlar.
- **Temsilci karşılaştırması:** Farklı bölgelerdeki temsilcilerin sonuçları adil biçimde karşılaştırılabilir mi? Nokta potansiyeli ve bölge özellikleri bilinmeden yapılan kıyaslar yanıltıcıdır.

**Rut ve bölge değişiklikleri.** Rutlar ve temsilci atamaları zamanla değişir. Geçmiş raporların doğru kalması için atamaların geçerlilik tarihleriyle tutulması gerekir; aksi hâlde geçmiş satışlar bugünkü temsilciye yazılır.

**Fotoğraf ve konum verisinin yönetimi.** Fotoğraflar büyük depolama alanı gerektirir ve kişisel veri içerebilir. Saklama süresi, erişim yetkileri ve fotoğrafların hangi amaçla kullanılacağı açıkça tanımlanmalıdır. Konum verisi ise yalnızca ziyaret doğrulaması için ve çalışanlara açıklanmış kurallar çerçevesinde kullanılmalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b6.py` ile yapılmıştır.

40 temsilcili bir distribütörde her temsilci günde 20 ziyaret, ayda 22 gün çalışıyor: ayda **17.600** ziyaret. Her ziyarette ortalama 3 fotoğraf çekildiğinde ayda **52.800** fotoğraf oluşuyor. Ziyaretlerin 1.320'si noktanın kayıtlı konumunun dışında başlatılmış: oran **%7,5**. İnceleme, bunların önemli bir kısmında noktanın koordinatının yanlış kaydedildiğini gösteriyor; nokta ana verisi düzeltiliyor.

## Sık yapılan hatalar

- Siparişi ziyarete bağlamadan ayrı kaydetmek.
- Nokta koordinatlarını bir kez girip hiç kontrol etmemek.
- Fotoğrafları hangi denetim maddesine ait olduğu bilinmeden toplamak.
- Ziyaret sonucunu serbest metin olarak bırakmak.

## Pratikte nasıl uygulanır?

- [ ] Nokta kartındaki zorunlu alanları belirleyin.
- [ ] Ziyaret sonuçları için sabit bir liste tanımlayın.
- [ ] Konum dışı ziyaretleri haftalık olarak raporlayın.
- [ ] Fotoğraf ve denetim maddelerini birbirine bağlayın.

## Daha fazlası

- Payne ve Frow (2005), *Journal of Marketing*. https://doi.org/10.1509/jmkg.2005.69.4.167
