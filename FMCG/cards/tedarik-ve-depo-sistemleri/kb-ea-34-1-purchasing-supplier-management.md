---
id: kb-ea-34-1-purchasing-supplier-management
title: "Satın alma ve tedarikçi yönetimi sistemleri"
summary: "Satın alma talebinden siparişe, teklif toplamaya, onay akışlarına ve tedarikçi performansının izlenmesine kadar satın alma süreçlerinin sistemde nasıl yönetildiğini anlatır."
course: ea
category: tedarik-ve-depo-sistemleri
tags: [satin-alma, tedarikci, teklif, onay-akisi, procure-to-pay]
roles: [uretici-sahibi, uretici-yonetici, finans-muduru]
level: orta
source_lessons: [EA-34.1]
reading_minutes: 2
key_points:
  - "Satın alma süreci talep, teklif, onay, sipariş, mal kabul ve fatura eşleştirme adımlarından oluşur."
  - "Teklif karşılaştırması fiyatın yanında vade, teslim süresi ve kaliteyi de içermelidir."
  - "Onay akışları tutar ve kategoriye göre kurgulanır."
  - "Tedarikçi performansı zamanında teslim, kalite ve fiyat uyumu ile izlenir."
  - "Sözleşme ve fiyat anlaşmaları sistemde tutulursa siparişler otomatik kontrol edilir."
glossary_terms: [satin-alma-talebi, tedarikci-performansi]
related: [kb-ea-20-3-procure-to-pay, kb-ea-32-2-food-safety-traceability, kb-ea-29-3-drp-inventory-planning]
sources:
  - title: "Purchasing and Supply Chain Management"
    authors: "Monczka, R. M. ve diğ."
    year: 2020
    type: book
    verified: false
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

Satın alma kararları e-posta ve telefonla verildiğinde kimin neyi hangi fiyata aldığı görünmez. Bu kart, satın alma ve tedarikçi yönetiminin sistemde nasıl kurulduğunu anlatır.

## Temel fikir

**Süreç adımları:**

1. **Satın alma talebi:** İhtiyacı olan birim talebi sisteme girer.
2. **Teklif:** Birden fazla tedarikçiden fiyat, vade ve teslim süresi alınır.
3. **Onay:** Tutar ve kategoriye göre tanımlı onay akışı.
4. **Sipariş:** Onaylı teklif siparişe dönüşür ve tedarikçiye gönderilir.
5. **Mal kabul ve fatura eşleştirme:** Sipariş, mal kabul ve fatura karşılaştırılır.

**Tedarikçi ana verisi.** Vergi numarası, banka bilgisi, ödeme koşulu, sertifikalar. Banka bilgisi değişikliği ayrıca onaylanmalıdır; dolandırıcılık riskinin yüksek olduğu bir alandır.

**Tedarikçi performansı.** Monczka ve arkadaşları, tedarikçilerin düzenli ve ölçülebilir kriterlerle değerlendirilmesini önerir:

- Zamanında teslim oranı,
- Kalite (iade, ret oranı),
- Fiyat ve sözleşme uyumu,
- İletişim ve esneklik.

**Sözleşmeler.** Yıllık fiyat anlaşmaları sistemde tutulduğunda, anlaşma dışı fiyatlı sipariş otomatik uyarı verir.

### Satın alma sisteminde kontrol noktaları

Satın alma süreci, şirketin parasının dışarı çıktığı yerdir; bu nedenle iç kontrolün en sıkı olması gereken alanlardan biridir. Sistemde kurulması gereken temel kontroller şunlardır:

- **Onay limitleri:** Talep ve siparişler, tutara ve harcama türüne göre farklı onay seviyelerinden geçmelidir. Siparişi bölerek limitin altında kalma girişimleri raporla izlenmelidir.
- **Görevler ayrılığı:** Tedarikçiyi açan, siparişi veren, malı teslim alan ve ödemeyi onaylayan kişiler aynı olmamalıdır.
- **Tedarikçi ana verisi değişiklikleri:** Özellikle banka hesap bilgisinin değiştirilmesi, dolandırıcılık girişimlerinin sık hedefidir. Bu değişiklikler ikinci bir kişinin onayına ve tedarikçiyle bağımsız bir kanaldan teyide bağlanmalıdır.
- **Üçlü eşleştirme:** Sipariş, mal kabul ve fatura miktar ve fiyat olarak eşleşmeden ödeme yapılmamalıdır.

**Harcama analizi.** Tüm satın almaların tedarikçi, kategori ve birim bazında görülebilmesi, pazarlık gücünü artırır. Aynı ürünün farklı birimler tarafından farklı fiyatlarla alındığı durumlar genellikle bu analizle ortaya çıkar. Bunun için malzeme ve hizmet kategorilerinin tutarlı tanımlanması gerekir.

**Tedarikçi ilişkisi.** Monczka ve arkadaşları, tedarikçileri stratejik önemlerine göre farklı yönetmeyi önerir: kritik tedarikçilerle uzun vadeli iş birliği ve düzenli performans görüşmesi; sıradan kalemlerde ise basit ve hızlı satın alma süreçleri. Sistem, bu ayrımı tedarikçi sınıfı gibi bir alanla desteklemelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b7.py` ile yapılmıştır.

Bir ambalaj malzemesi için üç teklif geliyor: 100, 96 ve 98 TL. En düşük fiyat **96** TL ama bu tedarikçinin son 200 siparişinden 184'ü zamanında: **%92,0**. Satın alma ekibi fiyatı ve teslim performansını birlikte değerlendirerek karar veriyor ve gerekçeyi sisteme yazıyor.

## Sık yapılan hatalar

- Siparişi önce verip talebi sonra sisteme girmek.
- Tek teklifle düzenli alım yapmak.
- Tedarikçi banka bilgisi değişikliğini e-postayla kabul etmek.
- Tedarikçi performansını hiç ölçmemek.

## Pratikte nasıl uygulanır?

- [ ] Tutar bazlı onay matrisini tanımlayın.
- [ ] Belirli tutarın üzerinde çoklu teklifi zorunlu yapın.
- [ ] Banka bilgisi değişikliği için ikinci onay ekleyin.
- [ ] Ana tedarikçiler için üç aylık performans kartı hazırlayın.

## Daha fazlası

- Monczka ve diğ., *Purchasing and Supply Chain Management* (kitap; doğrulanmadı).
- Magal ve Word, *Integrated Business Processes with ERP Systems* (kitap; doğrulanmadı).
