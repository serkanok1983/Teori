---
id: kb-ea-30-3-wms-what-it-does
title: "Depo yönetim sistemi (WMS): ERP'nin ötesinde ne yapar?"
summary: "Lokasyon bazlı stok, el terminaliyle yönlendirilmiş görevler, dalga planlama ve stok doğruluğu gibi WMS yeteneklerini; ERP stok modülüyle farkını ve ne zaman ayrı bir WMS'e ihtiyaç duyulduğunu anlatır."
course: ea
category: tedarik-ve-depo-sistemleri
tags: [wms, depo, el-terminali, lokasyon, erp]
roles: [depo-lojistik-muduru, it-yoneticisi]
level: ileri
source_lessons: [EA-30.3]
reading_minutes: 2
key_points:
  - "ERP stoğu genellikle depo düzeyinde, WMS ise raf lokasyonu düzeyinde izler."
  - "WMS, çalışanlara el terminaliyle görev verir ve her hareketi barkodla doğrular."
  - "Dalga planlama, siparişleri sevk saatine ve araçlara göre gruplar."
  - "Ayrı WMS, lokasyon sayısı, sipariş hacmi ve parti/son kullanma takibi arttıkça gerekli hale gelir."
  - "WMS ile ERP arasında stok ve sipariş arayüzü açıkça tanımlanmalıdır."
glossary_terms: [wms, el-terminali, dalga-planlama]
related: [kb-ea-30-1-warehouse-operations-kpis, kb-ea-30-2-slotting-picking, kb-ea-30-4-barcodes-traceability, kb-ea-20-5-inventory-in-erp]
sources:
  - title: "Warehouse Management"
    authors: "Richards, G."
    year: 2021
    type: book
    verified: false
  - title: "Odoo Inventory dokümantasyonu"
    authors: "Odoo S.A."
    year: 2026
    type: web
    url: "https://www.odoo.com/documentation/"
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

Depo büyüdükçe "stok sistemde var ama rafta bulamıyoruz" sorunu artar. Bu kart, depo yönetim sisteminin (WMS) ERP stok modülünden farkını ve ne zaman gerekli olduğunu anlatır.

## Temel fikir

**ERP stok modülü** genellikle şunları bilir: hangi depoda ne kadar stok var, hangi giriş ve çıkışlar olmuş.

**WMS** ise depo içini yönetir:

- **Lokasyon bazlı stok:** Her ürünün hangi raf gözünde, hangi partiyle durduğu.
- **Yönlendirilmiş görevler:** Çalışana el terminalinden "şu lokasyondan şu kadar al" komutu verilir; okutma ile doğrulanır.
- **Yerleştirme ve ikmal kuralları:** Gelen mal için önerilen lokasyon, toplama gözü boşaldığında ikmal görevi.
- **Dalga planlama:** Siparişlerin sevk saatine ve araca göre gruplanması.
- **Parti ve son kullanma tarihi:** İlk süresi dolan ilk çıkar (FEFO) gibi kuralların zorlanması.
- **Dönüşümlü sayım ve stok doğruluğu.**

Bazı ERP'ler bu yeteneklerin bir kısmını kendi içinde sunar; Odoo'nun stok modülündeki lokasyon ve rota yapısı buna örnektir. Ayrı bir WMS genellikle lokasyon sayısı, sipariş hacmi ve izlenebilirlik ihtiyacı büyüdüğünde gündeme gelir.

**Entegrasyon.** ERP siparişi ve ürün ana verisini WMS'e gönderir; WMS sevkiyat ve stok hareketlerini ERP'ye bildirir. Stoğun hangi sistemde "asıl" olduğu baştan kararlaştırılmalıdır.

### WMS'ye ne zaman ihtiyaç var?

Her depo için ayrı bir WMS gerekmez. ERP'nin stok modülü, küçük ve basit depolarda çoğu zaman yeterlidir. WMS ihtiyacını gösteren işaretler şunlardır:

- **Lokasyon sayısı ve karmaşıklık:** Ürünlerin nerede olduğunu yalnızca deneyimli çalışanlar biliyorsa ve yeni çalışanların alışması uzun sürüyorsa, lokasyon bazlı yönetim gerekir.
- **Parti ve son kullanma tarihi:** Gıda, kozmetik veya ilaç gibi ürünlerde ilk süresi dolanın ilk çıkması kuralı elle izlenemiyorsa WMS önemli bir kontrol sağlar.
- **Sipariş profili:** Çok sayıda küçük sipariş ve çok kalemli toplama, dalga planlama ve yönlendirilmiş görevler olmadan verimli yapılamaz.
- **Stok doğruluğu sorunları:** Sayım farkları sık ve büyükse, okutma ile doğrulanan hareketler hataları azaltır.
- **Müşteri gereksinimleri:** Bazı zincir müşteriler, palet etiketi, sevk bildirimi ve izlenebilirlik bilgisi talep eder.

**Proje dikkat noktaları.** WMS projesi, depo süreçlerinin yeniden tasarlanması anlamına gelir. Lokasyon adresleme, etiketleme, el terminali ve kablosuz ağ kapsamı gibi fiziksel hazırlıklar, yazılım kadar zaman alır. Canlıya geçişten önce tüm depoda doğru bir sayım yapılması, sistemin güvenilir bir başlangıç verisiyle çalışmasını sağlar.

**Çalışan benimsemesi.** El terminaliyle çalışmak, ilk haftalarda hızı düşürebilir. Operatörlerin sürece erken dahil edilmesi ve ekran akışlarının sade tasarlanması, geçişi kolaylaştırır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b7.py` ile yapılmıştır.

Bir distribütör WMS kurduktan sonraki ilk dönüşümlü sayımda 2.000 lokasyonun 1.940'ında sistem ile sayım tutuyor: lokasyon doğruluğu **%97,0**. Tutmayan lokasyonların çoğunun okutulmadan yapılan hareketlerden kaynaklandığı görülüyor ve el terminali dışında hareket yasaklanıyor.

## Sık yapılan hatalar

- WMS'i ERP'nin yerine geçecek bir sistem sanmak.
- Lokasyonları barkodlamadan WMS'e geçmek.
- Okutmadan hareket yapılmasına izin vermek.
- Stoğun asıl kaydının hangi sistemde olduğunu belirsiz bırakmak.

## Pratikte nasıl uygulanır?

- [ ] Mevcut ERP'nizin lokasyon ve parti yeteneklerini kontrol edin.
- [ ] Lokasyon, sipariş ve parti ihtiyacınızı sayısal olarak çıkarın.
- [ ] Lokasyon barkodlamayı WMS seçiminden önce tamamlayın.
- [ ] ERP–WMS arayüzünü yazılı tanımlayın.

## Daha fazlası

- Richards, *Warehouse Management* (kitap; doğrulanmadı).
- Odoo dokümantasyonu: https://www.odoo.com/documentation/
