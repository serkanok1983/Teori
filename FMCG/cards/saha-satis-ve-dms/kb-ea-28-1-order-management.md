---
id: kb-ea-28-1-order-management
title: "Sipariş yönetimi: Kanallar, stok rezervasyonu ve tahsis"
summary: "Farklı kanallardan gelen siparişlerin tek bir sipariş yönetim sürecinde toplanmasını, satılabilir stok (ATP) kontrolünü, rezervasyonu, depolar arası tahsisi ve kısmi teslimat kurallarını anlatır."
course: ea
category: saha-satis-ve-dms
tags: [siparis-yonetimi, atp, rezervasyon, tahsis, cok-kanal]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, depo-lojistik-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-28.1]
reading_minutes: 2
key_points:
  - "Sipariş saha uygulaması, B2B portal, EDI veya telefonla gelebilir; hepsi aynı sipariş sürecine girmelidir."
  - "Satılabilir stok (ATP), eldeki stoktan rezerve edilmiş miktarın düşülmesiyle bulunur."
  - "Stok yetmediğinde tahsis kuralları hangi müşterinin önce karşılanacağını belirler."
  - "Kısmi teslimat, bölme ve bekletme kuralları önceden tanımlanmalıdır."
  - "Sipariş durumu müşteriye ve satış ekibine görünür olmalıdır."
glossary_terms: [siparis-yonetimi, satilabilir-stok, stok-rezervasyonu]
related: [kb-ea-20-2-order-to-cash, kb-ea-20-5-inventory-in-erp, kb-ea-28-2-b2b-ordering-portals, kb-ea-26-1-retail-execution-sfa, kb-ea-29-3-drp-inventory-planning]
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

Bir distribütöre siparişler saha temsilcisinden, B2B portaldan, büyük zincirlerin EDI bağlantısından ve telefondan gelir. Her kanal ayrı işlenirse aynı stok iki kez satılır, öncelikler karışır. Bu kart, **sipariş yönetiminin** temel kurallarını anlatır.

## Temel fikir

**Tek giriş noktası.** Kanal ne olursa olsun sipariş aynı kurallarla ERP'ye veya sipariş yönetim sistemine düşmelidir: aynı fiyat motoru, aynı kredi kontrolü, aynı stok kontrolü.

**Satılabilir stok (ATP).** Sistemin "bu siparişi karşılayabilir miyim?" sorusunu yanıtladığı miktardır. En basit haliyle:

- Eldeki stok − başka siparişlere rezerve edilmiş stok (+ gelecek girişler, tanımlıysa)

**Rezervasyon.** Onaylanan sipariş için stok ayrılır; böylece ikinci bir sipariş aynı stoğu göremez. Rezervasyonların süresi ve iptal kuralı belirlenmelidir; yoksa kullanılmayan rezervler stoğu kilitler.

**Tahsis.** Stok yetmediğinde kim önce karşılanır? Seçenekler: sipariş sırası, müşteri önceliği, oransal paylaştırma. Kural yazılı değilse karar telefonla verilir.

**Kaynak depo seçimi ve bölme.** Birden fazla depo varsa sistem eksik miktarı ikinci depodan karşılayabilir; bunun nakliye maliyeti de düşünülmelidir.

**Kısmi teslimat.** Müşteri kısmi teslimat kabul ediyor mu, kalan miktar bekletilecek mi iptal mi edilecek? Bu bilgi müşteri ana verisinde tutulmalıdır.

### Sipariş yönetiminde kurallar ve öncelikler

Sipariş yönetimi sistemi, iş kurallarını açıkça tanımlamayı zorunlu kılar. Bu kurallar yazılmadığında, kararlar her gün farklı kişilerce farklı biçimde verilir. Netleştirilmesi gereken başlıca konular şunlardır:

- **Öncelik sırası:** Stok yetersiz olduğunda hangi sipariş önce karşılanır? Sipariş tarihi, müşteri sınıfı, sözleşme taahhüdü veya kanal önceliği gibi ölçütlerin sırası belirlenmelidir.
- **Rezervasyonun süresi:** Onay bekleyen veya ödemesi alınmamış siparişler için ayrılan stok ne kadar süre bekletilir? Süresiz rezervasyon, satılabilir stoğu gereksiz yere düşürür.
- **Kredi ve stok kontrolünün sırası:** Kredi limiti aşılan bir sipariş için stok ayrılmalı mı? Bu karar hem müşteri deneyimini hem de stok kullanımını etkiler.
- **Kısmi teslim politikası:** Müşteri bazında kısmi teslimin kabul edilip edilmediği ana veride tutulmalıdır. Bazı zincir müşteriler eksik sevkiyatı kabul etmez, bazıları ise eksik kalanların ayrıca gönderilmesini ister.
- **İptal ve değişiklik:** Sipariş hangi aşamaya kadar değiştirilebilir? Toplama başladıktan sonra yapılan değişiklikler depo operasyonunu bozar.

**Sipariş durumlarının görünürlüğü.** Siparişin alındı, onaylandı, toplanıyor, sevk edildi ve faturalandı gibi durumları tüm kanallarda aynı biçimde görünmelidir. Müşteri hizmetleri, satış temsilcisi ve portal aynı bilgiyi gösterdiğinde, "siparişim nerede?" soruları azalır.

**Ölçüm.** Siparişin eksiksiz ve zamanında teslim oranı, sipariş yönetiminin temel başarı göstergesidir. Eksik teslimlerin nedenleri (stok yokluğu, kredi blokajı, depo hatası) ayrı ayrı izlenmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b6.py` ile yapılmıştır.

Bir müşteri 500 koli sipariş veriyor. A deposunda 800 koli var ama 450 kolisi başka siparişlere rezerve; satılabilir stok **350** koli. Sistem 350 koliyi A deposundan, kalan **150** koliyi B deposundan karşılamayı öneriyor. Müşteri kısmi teslimatı kabul ettiği için iki sevkiyat oluşturuluyor.

## Sık yapılan hatalar

- Saha ve portal siparişlerini farklı stok bilgisine göre onaylamak.
- Süresi dolmuş rezervasyonları temizlememek.
- Tahsis kararını yazılı kural yerine kişilere bırakmak.
- Sipariş durumunu satış ekibine görünür kılmamak.

## Pratikte nasıl uygulanır?

- [ ] Tüm sipariş kanallarını ve hangi sisteme düştüklerini çizin.
- [ ] ATP hesabının neleri içerdiğini yazılı tanımlayın.
- [ ] Tahsis ve kısmi teslimat kurallarını belirleyin.
- [ ] Açık rezervasyonları haftalık gözden geçirin.

## Daha fazlası

- Magal ve Word, *Integrated Business Processes with ERP Systems* (kitap; doğrulanmadı).
