---
id: kb-fmcg-13-4-b2b-buying-behaviour
title: "Kurumsal satın alma davranışı: Müşteriler nasıl karar verir?"
summary: "Kurumsal müşteriler, bireysel tüketicilerden farklı olarak birden fazla kişinin katıldığı, kurallara bağlı ve toplam maliyete odaklı bir süreçle karar verir. Bu kart satın alma merkezi modelini, karar türlerini ve toplam sahip olma maliyeti yaklaşımını anlatır."
course: fmcg
category: satis-teknikleri
tags: [satis-teknikleri, kurumsal-satis, musteri-davranisi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: orta
source_lessons: [FMCG-13.4]
reading_minutes: 3
key_points:
  - "Webster ve Wind, kurumsal satın almayı kullanıcı, etkileyici, alıcı, karar verici ve bilgi akışını kontrol eden kişilerden oluşan bir satın alma merkezi olarak tanımlar."
  - "Kararlar çevresel, kurumsal, kişiler arası ve bireysel etkenlerden etkilenir."
  - "Sheth'in modeli, satın alma merkezindeki kişilerin farklı beklentilerini ve bunlardan doğan çatışmaların nasıl çözüldüğünü vurgular."
  - "Kurumsal müşteri, birim fiyattan çok toplam maliyete bakar."
  - "Yeni alım, değiştirilmiş yeniden alım ve rutin yeniden alım farklı satış yaklaşımları gerektirir."
glossary_terms: [satin-alma-merkezi, hizmet-maliyeti, vade, katki-payi]
related: [kb-fmcg-13-2-strategic-selling, kb-fmcg-13-5-retail-buyer-decisions, kb-fmcg-13-14-negotiation-structure, kb-fmcg-10-1-key-account-management]
sources:
  - title: "A General Model for Understanding Organizational Buying Behavior"
    authors: "Webster, F. E.; Wind, Y."
    year: 1972
    type: article
    doi: "10.1177/002224297203600204"
    url: "https://doi.org/10.1177/002224297203600204"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Marketing 36(2), 12–19."
  - title: "A Model of Industrial Buyer Behavior"
    authors: "Sheth, J. N."
    year: 1973
    type: article
    doi: "10.1177/002224297303700408"
    url: "https://doi.org/10.1177/002224297303700408"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Marketing 37(4), 50–56."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Bir otel zincirine ya da toptancıya ürün satarken karşınızda tek bir alıcı yoktur. Bir kişi fiyatla, bir başkası teslimat güvenilirliğiyle, bir diğeri depo alanıyla ilgilenir. Bu kart, kurumsal müşterilerin nasıl karar verdiğini anlamanızı ve önerinizi bu sürece göre hazırlamanızı sağlar.

## Temel fikir

**Satın alma merkezi.** Webster ve Wind'in 1972'de *Journal of Marketing*'de yayımlanan modeli, kurumsal satın almayı bir grup kararı olarak ele alır. Satın alma merkezinde (*buying centre*) şu roller bulunur:

- **Kullanıcılar:** Ürünü kullanacak kişiler
- **Etkileyiciler:** Ölçütleri belirleyen ya da görüş bildiren kişiler
- **Alıcılar:** Tedarikçiyle resmî olarak pazarlık yapan ve siparişi veren kişiler
- **Karar vericiler:** Son onayı veren kişiler
- **Kapı bekçileri:** Bilgi akışını ve satıcının kime ulaşabileceğini kontrol eden kişiler

Model, kararların dört düzeyde etkilendiğini anlatır: çevresel (ekonomi, mevzuat, rekabet), kurumsal (şirketin hedefleri, yapısı, kuralları), kişiler arası (satın alma merkezindeki ilişkiler) ve bireysel (kişinin deneyimi, motivasyonu, risk algısı).

**Sheth'in modeli.** Sheth'in 1973 tarihli modeli, satın alma merkezindeki farklı kişilerin farklı geçmişleri ve bilgi kaynakları nedeniyle farklı beklentiler geliştirdiğini vurgular. Bu beklentiler çatıştığında, karar problem çözme, ikna, pazarlık ya da politik süreçlerle verilir. Satıcı için sonuç şudur: Her kişinin beklentisi ayrı ayrı anlaşılmalıdır.

**Karar türleri.** Kurumsal pazarlamada yaygın olarak üç satın alma durumu ayrılır:

- **Yeni alım:** Müşteri ilk kez bu kategoride tedarikçi arıyor; bilgi ihtiyacı ve risk algısı yüksektir.
- **Değiştirilmiş yeniden alım:** Müşteri mevcut tedarikçisini ya da koşulları yeniden değerlendiriyor; rakip için fırsattır.
- **Rutin yeniden alım:** Müşteri alışık olduğu tedarikçiden sipariş veriyor; mevcut tedarikçinin hizmet kalitesini koruması gerekir.

**Toplam sahip olma maliyeti.** Kurumsal alıcı, birim fiyatın yanında teslimat, depolama, fire, ödeme koşulları ve iş yükü gibi maliyetlere de bakar. Daha ucuz bir teklif, toplamda daha pahalı olabilir.

## Bir örnek

> **Örnek (temsili rakamlar):** Fiyat ve maliyet kalemleri varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b8.py` ile yapılmıştır.

Bir otel zinciri, iki tedarikçinin tekliflerini koli başına maliyetle karşılaştırıyor:

| Kalem (TL/koli) | Tedarikçi A | Tedarikçi B |
|---|---:|---:|
| Birim fiyat | 100 | 96 |
| Teslimat ve depolama | 3 | 6 |
| Fire ve iade | 2 | 4 |
| **Toplam** | **105** | **106** |

B'nin birim fiyatı daha düşük, ama seyrek teslimat nedeniyle daha fazla stok tutulması ve daha yüksek fire, toplam maliyeti A'nın üzerine çıkarıyor. A'nın satış temsilcisi, fiyatı düşürmek yerine bu tabloyu satın alma ve operasyon ekipleriyle birlikte hazırlıyor. Bu kalemlerin değerleri müşterinin kendi verisiyle doğrulanmalıdır.

## Sık yapılan hatalar

- **Yalnızca alıcıyla konuşmak.** Kullanıcılar ve etkileyiciler kararı belirleyebilir.
- **Fiyatla rekabet etmek.** Toplam maliyet avantajı gösterilmeden indirim verilir.
- **Kapı bekçisini düşman görmek.** Bu kişiyle iyi ilişki, diğer kişilere ulaşmanın yoludur.
- **Rutin yeniden alımı güvence saymak.** Hizmet aksarsa müşteri değiştirilmiş yeniden alıma geçer.

## Pratikte nasıl uygulanır?

- [ ] Her büyük kurumsal müşteride satın alma merkezini belirleyin.
- [ ] Her rol için beklentiyi ve başarı ölçütünü yazın.
- [ ] Müşterinin hangi satın alma durumunda olduğunu belirleyin.
- [ ] Toplam maliyet karşılaştırmasını müşterinin verisiyle hazırlayın.
- [ ] Rutin müşterilerde hizmet performansını düzenli raporlayın.

## Daha fazlası

- Webster, F. E.; Wind, Y. (1972). *A General Model for Understanding Organizational Buying Behavior.* Journal of Marketing 36(2), 12–19. https://doi.org/10.1177/002224297203600204
- Sheth, J. N. (1973). *A Model of Industrial Buyer Behavior.* Journal of Marketing 37(4), 50–56. https://doi.org/10.1177/002224297303700408
