---
id: kb-ea-26-5-van-sales-presales
title: "Araçtan satış ve ön satış: Araç stoğu, yolda fatura ve gün sonu mutabakatı"
summary: "Ön satış ile araçtan satış modellerinin farkını, araçtan satışta cihazdan fatura ve e-Arşiv/e-Fatura düzenlemeyi, araç stoğunun takibini, nakit ve kart tahsilatını ve gün sonunda stok ile kasanın mutabakatını anlatır."
course: ea
category: saha-satis-ve-dms
tags: [aracli-satis, on-satis, e-arsiv, gun-sonu, tahsilat]
roles: [bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, saha-satis-temsilcisi, depo-lojistik-muduru]
level: temel
source_lessons: [EA-26.5]
reading_minutes: 3
key_points:
  - "Ön satışta sipariş bugün alınır, teslimat sonra yapılır; araçtan satışta satış ve teslimat aynı anda olur."
  - "Araçtan satışta araç bir depo gibi yönetilir; yükleme, satış, iade ve kalan stok izlenir."
  - "Faturanın yolda düzenlenmesi için cihazın e-belge altyapısıyla bağlantısı gerekir."
  - "Gün sonu mutabakatında stok ve kasa ayrı ayrı sayılıp sistemle karşılaştırılır."
  - "Farklar aynı gün açıklanmalı ve onaylanmalıdır."
glossary_terms: [aractan-satis, on-satis, gun-sonu-mutabakati, e-arsiv-fatura]
related: [kb-ea-26-3-offline-mode-for-managers, kb-ea-37-2-e-fatura-scenarios, kb-ea-37-2-e-irsaliye-practice, kb-ea-20-5-inventory-in-erp, kb-ea-31-3-route-planning-sales-vs-delivery]
sources:
  - title: "e-Belge portalı"
    authors: "Gelir İdaresi Başkanlığı"
    year: 2026
    type: web
    url: "https://ebelge.gib.gov.tr/"
    verified: false
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Hızlı tüketimde iki temel dağıtım modeli vardır. Hangisini seçtiğiniz; araç, cihaz, e-belge ve kasa süreçlerinizi baştan belirler. Bu kart iki modeli ve araçtan satışın sistem gereksinimlerini anlatır.

## Temel fikir

**Ön satış (pre-sales).** Temsilci noktayı ziyaret edip sipariş alır. Sipariş depoya gider, ertesi gün dağıtım aracıyla teslim edilir. Fatura genellikle depoda ya da teslimatta düzenlenir.

**Araçtan satış (van sales).** Temsilci aracındaki ürünle noktaya gider; satış, teslimat, fatura ve tahsilat aynı ziyarette yapılır. Küçük ve sık alım yapan noktalar için uygundur.

Araçtan satışın sistem gereksinimleri:

- **Araç stoğu:** Araç ERP'de ayrı bir depo olarak tanımlanır. Sabah yükleme, gün içi satış ve iade, akşam boşaltma hareketleri izlenir.
- **Yolda fatura:** Cihazdan düzenlenen faturanın alıcının durumuna göre e-Fatura veya e-Arşiv olarak oluşturulması ve entegratöre iletilmesi gerekir. Bağlantı yoksa belgenin nasıl ve ne zaman iletileceği önceden kurgulanmalıdır.
- **Tahsilat:** Nakit, kart (mobil POS) veya vadeli satış; her biri ayrı kaydedilir.
- **Gün sonu mutabakatı:**
  - Stok: Yüklenen − satılan + iade alınan = araçta kalması gereken.
  - Kasa: Nakit tahsilat kaydı ile teslim edilen nakit.

### Araçtan satışta kontrol ve risk

Araçtan satış modelinde stok ve nakit sahada dolaştığı için, kontrol mekanizmaları ön satışa göre daha sıkı olmalıdır. Dikkat edilmesi gereken başlıca konular şunlardır:

- **Araç yükleme kontrolü:** Araca yüklenen ürünler, sürücü ve depo sorumlusu tarafından birlikte sayılarak sisteme kaydedilmelidir. Yükleme sırasındaki farklar, gün sonu mutabakatını karmaşık hâle getirir.
- **Nakit yönetimi:** Araçta taşınan nakit miktarı sınırlandırılmalı; gün içinde bankaya yatırma veya kartlı ve elektronik tahsilat teşvik edilmelidir. Nakit taşımanın güvenlik riski de göz önünde bulundurulmalıdır.
- **Fiyat ve iskonto yetkisi:** Sürücü satıcının verebileceği iskontolar sistemde sınırlandırılmalıdır. Yetki dışı iskontolar onaya düşmelidir.
- **Gün sonu mutabakatı:** Araçtan dönen stok, satılan miktar ve tahsil edilen tutar her gün karşılaştırılmalıdır. Farklar, nedenleriyle birlikte kayda alınmalı ve tekrarlayan farklar incelenmelidir.
- **İade ve hasarlı ürünler:** Sahada alınan iadeler ve hasarlı ürünler ayrı olarak kaydedilmeli ve depoya dönüşte kontrol edilmelidir.

**Belge düzeni.** Yolda düzenlenen fatura ve irsaliyelerin elektronik belge yükümlülüklerine uygun olması, cihaz ve bağlantı altyapısını gerektirir. Bağlantı kesildiğinde belgelerin nasıl düzenleneceği önceden planlanmalıdır. Güncel belge yükümlülükleri için mali müşavirinize başvurmanız önerilir.

**Model seçimi.** Hangi müşteri grubunda araçtan satışın, hangisinde ön satışın daha verimli olduğu, sipariş büyüklüğü ve ziyaret maliyetiyle birlikte düzenli olarak değerlendirilmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b6.py` ile yapılmıştır.

Bir araca sabah 300 koli yükleniyor; gün içinde 240 koli satılıyor. Akşam araçta **60** koli kalması gerekirken 55 koli sayılıyor. Eksik **5** koli, koli başı 250 TL'den **1.250,00 TL**. Kasada sistemdeki nakit 38.000 TL, teslim edilen 37.600 TL: fark **400,00 TL**. Sorumlu, farkların nedenini (hasarlı ürün, kayda girmemiş iade) aynı akşam açıklıyor ve bölge müdürü onaylıyor.

## Sık yapılan hatalar

- Aracı depo olarak tanımlamayıp stoğu Excel'de izlemek.
- E-belge kurgusunu çevrimdışı senaryoyu düşünmeden yapmak.
- Gün sonu farklarını haftalık toplu kapatmak.
- İadeleri satış belgesinden ayrı ve kontrolsüz almak.

## Pratikte nasıl uygulanır?

- [ ] Hangi müşteri grupları için hangi modeli kullanacağınızı belirleyin.
- [ ] Araç depolarını ve yükleme–boşaltma hareketlerini ERP'de tanımlayın.
- [ ] Yolda fatura kurgusunu entegratörünüzle test edin.
- [ ] Gün sonu mutabakatını zorunlu ve onaylı bir adım yapın.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın. Yolda düzenlenen e-belgelerin senaryo ve süre kurallarını mali müşavirinize ve entegratörünüze doğrulatın.

## Daha fazlası

- Gelir İdaresi Başkanlığı e-Belge portalı (doğrulanmadı): https://ebelge.gib.gov.tr/
