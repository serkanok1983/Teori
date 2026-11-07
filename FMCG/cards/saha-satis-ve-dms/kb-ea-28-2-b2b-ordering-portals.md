---
id: kb-ea-28-2-b2b-ordering-portals
title: "B2B sipariş portalları: Bayi ve noktaların kendi siparişini vermesi"
summary: "Bayi ve perakende noktalarının web veya mobil portal üzerinden sipariş verdiği B2B kanalları; fiyat ve stok gösterimini, kredi limiti kontrolünü, saha ekibiyle çakışmayı ve benimsenmeyi artırma yollarını anlatır."
course: ea
category: saha-satis-ve-dms
tags: [b2b, portal, e-ticaret, bayi, self-servis]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, it-yoneticisi]
level: orta
source_lessons: [EA-28.2]
reading_minutes: 2
key_points:
  - "B2B portal, müşterinin sipariş, fatura, ekstre ve ödemeyi kendi başına yapmasını sağlar."
  - "Portal, ERP ile aynı fiyat, stok ve kredi limiti bilgisini göstermelidir."
  - "Portal siparişi satış temsilcisinin primini etkilemiyorsa temsilci portalı destekler."
  - "Benimsenme oranı izlenmeli ve teşvik edilmelidir."
  - "Portal, saha ziyaretinin yerini değil, rutin siparişlerin yükünü alır."
glossary_terms: [b2b-portal, self-servis]
related: [kb-ea-28-1-order-management, kb-ea-26-1-retail-execution-sfa, kb-ea-38-1-payment-systems-tr, kb-ea-33-3-incentive-compensation-systems]
sources:
  - title: "Odoo eCommerce dokümantasyonu"
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

Rutin siparişlerin telefonla, WhatsApp'la veya temsilci ziyaretiyle alınması hem müşteri hem şirket için zaman kaybıdır. **B2B sipariş portalı**, bayi ve noktaların kendi siparişini vermesini sağlar. Bu kart, portalın ne zaman işe yaradığını ve nelere dikkat etmek gerektiğini anlatır.

## Temel fikir

Bir B2B portalda müşteri genellikle şunları yapabilir:

- Kendisine özel fiyatla ürün kataloğunu görmek,
- Stok durumuna göre sipariş vermek,
- Önceki siparişi tekrarlamak,
- Fatura, irsaliye ve cari hesap ekstresini görmek,
- Kartla veya havaleyle ödeme yapmak.

**ERP ile tutarlılık.** Portaldaki fiyat, stok ve kredi limiti ERP ile aynı olmalıdır. Portal ayrı bir fiyat listesi kullanırsa müşteri iki farklı fiyat görür ve güven kaybolur.

**Saha ekibiyle ilişki.** Temsilci, portal siparişlerini kendi satışından düşen bir şey olarak görürse müşteriyi portaldan uzak tutar. Portal siparişlerinin temsilcinin hedef ve primine sayılması bu çatışmayı azaltır.

**Benimsenme.** Portal açmak yetmez. İlk siparişte destek, portala özel küçük avantajlar ve düzenli takip gerekir. Ölçülecek ana gösterge, siparişlerin portal üzerinden gelen payıdır.

### Portal projesinde karar noktaları

Bir B2B portal projesine başlarken aşağıdaki kararlar baştan netleştirilmelidir:

- **Kimin için?** Büyük bayiler ve zincirler genellikle kendi sistemleri üzerinden elektronik veri değişimi tercih eder; portal daha çok orta ve küçük ölçekli müşteriler için değer yaratır. Hedef müşteri grubunu tanımlamak, ekran tasarımından ödeme seçeneklerine kadar birçok kararı belirler.
- **Mobil kullanım:** Küçük işletme sahipleri siparişi çoğu zaman telefondan verir. Portalın mobilde kolay kullanılması, benimsenmenin ön koşuludur.
- **Fiyat ve kampanya gösterimi:** Müşteriye özel fiyat, iskonto ve kampanyalar ERP'deki fiyat motorundan anlık olarak hesaplanmalıdır. Kampanya koşullarının portalda açıkça gösterilmesi, sipariş sonrası itirazları azaltır.
- **Kredi limiti ve vade:** Limiti aşan siparişlerin nasıl ele alınacağı belirlenmelidir: tamamen engellemek mi, onaya göndermek mi, kartla ödeme seçeneği sunmak mı?
- **Sipariş sonrası bilgi:** Siparişin durumu, sevk tarihi ve faturası portalda görülebilirse müşteri hizmetlerine gelen arama sayısı azalır.

**Saha ekibinin rolünün değişmesi.** Portal, temsilcinin işini ortadan kaldırmaz; rutin sipariş alma yükünü azaltarak temsilcinin mağaza içi uygulama, yeni ürün tanıtımı ve müşteri gelişimi gibi işlere daha fazla zaman ayırmasını sağlar. Bu değişikliğin ziyaret sıklığı ve hedeflere nasıl yansıyacağı planlanmalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b6.py` ile yapılmıştır.

Bir distribütör ayda 2.000 sipariş alıyor. Portalın ilk yılında siparişlerin %30'u, yani **600** sipariş portala kayıyor. Telefonla sipariş almanın sipariş başına 25 TL iç maliyeti olduğu varsayılırsa aylık tasarruf **15.000,00 TL**. Bu süre temsilcilere yeni nokta ziyaretleri için açılıyor.

## Sık yapılan hatalar

- Portalda ERP'den farklı fiyat göstermek.
- Kredi limiti kontrolünü portalda atlamak.
- Temsilcilerin primini portal siparişlerinden ayrı tutmak.
- Portalı açıp benimsenmeyi izlememek.

## Pratikte nasıl uygulanır?

- [ ] Hangi müşteri gruplarının portal için uygun olduğunu belirleyin.
- [ ] Fiyat, stok ve kredi limitini ERP'den canlı veya sık aralıklarla alın.
- [ ] Portal siparişlerini temsilci hedefine sayın.
- [ ] Aylık portal payını ve aktif kullanıcı sayısını izleyin.

## Daha fazlası

- Odoo dokümantasyonu (B2B e-ticaret örneği): https://www.odoo.com/documentation/
