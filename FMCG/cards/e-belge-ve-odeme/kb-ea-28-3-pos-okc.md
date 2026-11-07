---
id: kb-ea-28-3-pos-okc
title: "Mağaza kasası ve ÖKC: Yeni nesil yazar kasa ve ERP bağlantısı"
summary: "Perakende noktalarındaki kasa yazılımlarını, yeni nesil ödeme kaydedici cihazların (ÖKC) rolünü, Z raporu ve gün sonu mutabakatını ve kasa verisinin ERP'ye aktarılmasını anlatır."
course: ea
category: e-belge-ve-odeme
tags: [okc, yazar-kasa, pos, z-raporu, perakende]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, it-yoneticisi]
level: orta
source_lessons: [EA-28.3]
reading_minutes: 3
key_points:
  - "Yeni nesil ÖKC, satış kayıtlarını mali hafızada tutan ve GİB sistemine bağlı çalışan cihazdır."
  - "Kasa yazılımı ürün, fiyat ve kampanyayı yönetir; ÖKC mali belgeyi üretir."
  - "Z raporu, günün mali satış toplamını gösterir ve kapanışta alınır."
  - "Gün sonunda kasa yazılımı, Z raporu ve banka POS toplamları karşılaştırılır."
  - "Kasa verisinin ERP'ye günlük aktarımı stok ve muhasebe için gereklidir."
glossary_terms: [okc, z-raporu, kasa-yazilimi]
related: [kb-ea-37-1-e-document-map, kb-ea-28-4-card-virtual-pos, kb-ea-20-5-inventory-in-erp, kb-ea-38-1-payment-systems-tr]
sources:
  - title: "Ödeme Kaydedici Cihazlar"
    authors: "Gelir İdaresi Başkanlığı"
    year: 2026
    type: web
    url: "https://www.gib.gov.tr/"
    verified: false
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Kendi mağazası veya satış noktası olan firmalarda kasa, hem satış hem vergi hem stok açısından kritik bir noktadır. Bu kart, kasa yazılımı ile **ödeme kaydedici cihaz** (ÖKC) arasındaki farkı ve kasa verisinin ERP'ye nasıl bağlanacağını anlatır.

## Temel fikir

**İki ayrı katman:**

- **Kasa yazılımı:** Ürün kartı, fiyat, kampanya, sadakat ve satış ekranı. Mağaza yönetiminin parçasıdır.
- **ÖKC (yeni nesil yazar kasa):** Mali belgeyi üreten, kayıtları mali hafızada tutan ve Gelir İdaresi Başkanlığının sistemine bilgi gönderen cihaz. Bazı modeller banka POS işlevini de içerir.

Kasa yazılımı ile ÖKC arasında bir entegrasyon bulunur; satış yazılımda oluşur, mali fiş cihazdan çıkar.

**Z raporu.** Gün sonunda alınan, günün mali satış toplamlarını gösteren rapordur. Gün içindeki ara raporlara X raporu denir.

**Gün sonu mutabakatı:**

- Kasa yazılımı satış toplamı
- Z raporu toplamı
- Banka POS toplamları ve nakit sayımı

Bu üçü tutmalıdır. Fark varsa iptal, iade veya yazılımda kalan fiş aranır.

**ERP'ye aktarım.** Satışlar ürün bazında ERP'ye aktarılır; stok düşer, gelir ve tahsilat muhasebeleşir. Aktarım günlük olmalı; haftalık aktarım stok bilgisinin yanlış görünmesine yol açar.

### Mağaza operasyonunda kontrol noktaları

Kasa ve ÖKC süreçleri, hem nakit kontrolü hem de vergi uyumu açısından günlük disiplin gerektirir. İzlenmesi gereken başlıca konular şunlardır:

- **Gün sonu kapanışı:** Her kasa için gün sonu raporu alınmalı; nakit, kart ve diğer ödeme türlerinin toplamları kasa yazılımı ve banka kayıtlarıyla karşılaştırılmalıdır. Farklar, nedenleriyle birlikte kaydedilmelidir.
- **İade ve iptal işlemleri:** Fiş iptalleri ve iadeler, yetkili bir kişinin onayıyla yapılmalıdır. Bu işlemlerin sıklığı kasiyer bazında izlenmelidir; olağan dışı artışlar incelenmelidir.
- **Fiyat ve ürün güncellemeleri:** Merkezden yapılan fiyat değişikliklerinin kasalara zamanında ve doğru aktarıldığı kontrol edilmelidir. Raf etiketi ile kasa fiyatı arasındaki farklar müşteri şikâyetine yol açar.
- **Bağlantı kesintileri:** Kasa yazılımı ile merkez arasındaki bağlantı kesildiğinde satışların nasıl kaydedileceği ve bağlantı geri geldiğinde nasıl aktarılacağı tanımlanmalıdır.
- **Cihaz bakımı:** ÖKC'lerin bakım ve güncelleme yükümlülükleri, yetkili servisle birlikte izlenmelidir.

**ERP'ye aktarımın doğrulanması.** Mağaza satışlarının ERP'ye aktarımından sonra, stok düşüşleri, satış hasılatı ve tahsilat tutarlarının ÖKC raporlarıyla tutarlı olduğu düzenli olarak kontrol edilmelidir.

**Mevzuat takibi.** ÖKC'lere ilişkin teknik ve idari düzenlemeler değişebilir; güncel yükümlülükler için mali müşavirinize ve resmî duyurulara başvurmanız önerilir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b6.py` ile yapılmıştır.

Bir mağazada gün sonunda kasa yazılımı 48.400 TL, Z raporu 48.250 TL satış gösteriyor. Fark **150,00 TL**. İnceleme, kasa yazılımında kalan ama ÖKC'ye gitmeden iptal edilmiş bir fişi ortaya çıkarıyor. İptal kaydı düzeltiliyor ve ERP aktarımı Z raporu toplamıyla yapılıyor.

## Sık yapılan hatalar

- Kasa yazılımı ile ÖKC'yi aynı şey sanmak.
- Gün sonu mutabakatını yalnızca nakit sayımına indirgemek.
- ERP aktarımını haftalık yapmak.
- Cihaz değişikliği ve servis süreçlerini belgelememek.

## Pratikte nasıl uygulanır?

- [ ] Her mağazanın kasa yazılımı ve ÖKC modelini envanterleyin.
- [ ] Gün sonu mutabakat formunu standartlaştırın.
- [ ] ERP aktarımını günlük ve otomatik hale getirin.
- [ ] Kasa farklarını mağaza bazında aylık izleyin.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın. ÖKC kullanım zorunluluğu, istisnalar ve e-belge ile ilişkisi için mali müşavirinizin görüşünü alın.

## Daha fazlası

- Gelir İdaresi Başkanlığı (doğrulanmadı): https://www.gib.gov.tr/
