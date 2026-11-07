---
id: kb-ea-24-2-bank-statement-integration
title: "Banka entegrasyonu: Hesap ekstresi, ödeme dosyası ve otomatik eşleştirme"
summary: "Banka hesap hareketlerinin ERP'ye MT940 veya camt.053 gibi standart biçimlerle aktarılmasını, ISO 20022 tabanlı ödeme dosyalarını, bankayla doğrudan sistem bağlantısını ve tahsilatların otomatik eşleştirilmesini anlatır."
course: ea
category: e-belge-ve-odeme
tags: [banka, entegrasyon, iso-20022, eslestirme, tahsilat]
roles: [finans-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-24.2]
reading_minutes: 3
key_points:
  - "Banka hareketleri elle girilmek yerine standart dosya ya da servislerle ERP'ye aktarılabilir."
  - "MT940 ve camt.053 hesap ekstresi, pain.001 ise ödeme talimatı için kullanılan biçimlerdir."
  - "Türkiye'de bankalar ayrıca kendi web servislerini ve dosya biçimlerini sunar."
  - "Otomatik eşleştirme kuralları; tutar, açıklama ve müşteri referansına dayanır."
  - "Eşleşmeyen kalemler için günlük bir iş listesi tutulmalıdır."
glossary_terms: [hesap-ekstresi, iso-20022, otomatik-eslestirme]
related: [kb-ea-24-1-treasury-cash-forecasting, kb-ea-11-6-apis-for-managers, kb-ea-20-2-order-to-cash, kb-ea-38-1-payment-systems-tr]
sources:
  - title: "ISO 20022 Financial Services Messaging"
    authors: "ISO 20022 Registration Authority"
    year: 2026
    type: web
    url: "https://www.iso20022.org/"
    verified: false
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Birçok firmada muhasebe ekibi her sabah bankalardan ekstreleri indirip tahsilatları tek tek müşteri hesaplarına işler. Bu hem zaman alır hem de hata üretir. Bu kart, banka entegrasyonunun temel yapı taşlarını anlatır.

## Temel fikir

**Hesap ekstresi aktarımı.** Banka hareketleri standart biçimlerde alınabilir:

- **MT940:** SWIFT ağında uzun süredir kullanılan ekstre mesajı.
- **camt.053:** ISO 20022 standardının XML tabanlı gün sonu ekstre mesajı.

Türkiye'de bankalar bunlara ek olarak kendi web servislerini veya dosya biçimlerini sunar. Birçok ERP ve finans yazılımı, Türk bankalarıyla hazır bağlantılarla gelir.

**Ödeme dosyaları.** Tedarikçi ödemeleri ERP'de hazırlanıp bankaya toplu talimat olarak gönderilebilir. ISO 20022'deki **pain.001** mesajı bu amaçla kullanılır. Bankanın onay ve red bilgisi geri döner.

**Bağlantı yöntemleri.**

- İnternet bankacılığından dosya indirme/yükleme (en basit, elle yapılan).
- Bankanın web servisleri veya API'leri.
- **Doğrudan sistem bağlantısı** (*host-to-host*): Firma sistemi ile banka sistemi arasında güvenli, otomatik dosya aktarımı.

**Otomatik eşleştirme.** Gelen bir tahsilatın hangi müşteriye ve hangi faturaya ait olduğu şu kurallarla bulunur:

- Gönderen IBAN'ın müşteri kartında kayıtlı olması,
- Açıklamada fatura veya müşteri numarası geçmesi,
- Tutarın açık bir faturayla birebir eşleşmesi.

Eşleşmeyen kalemler günlük bir iş listesine düşer.

### Eşleştirme kurallarını tasarlamak

Otomatik eşleştirmenin başarısı, kuralların doğru tasarlanmasına ve düzenli iyileştirilmesine bağlıdır. Kurallar genellikle şu sırayla uygulanır:

- **Kesin referans:** Açıklama alanında fatura numarası, müşteri kodu veya özel ödeme referansı varsa, kayıt doğrudan ilgili açık kaleme eşleştirilir.
- **Gönderen bilgisi:** Gönderen hesap numarası veya vergi numarası müşteri ana verisinde kayıtlıysa, ödeme önce müşteriye atanır; ardından tutar ve vadeye göre açık kalemlerle eşleştirilir.
- **Tutar eşleşmesi:** Tutar tek bir açık kalemle birebir uyuşuyorsa eşleştirme önerilir; birden fazla aday varsa kayıt incelemeye düşer.
- **Banka masrafları ve faizler:** Tekrarlayan masraf ve faiz hareketleri, açıklama metnine göre doğrudan ilgili gider hesaplarına kaydedilir.

**İnceleme kuyruğu.** Eşleştirilemeyen hareketler, bir iş kuyruğunda kullanıcıya sunulmalıdır. Kullanıcı elle eşleştirme yaptığında, sistem bu eşleştirmeden öğrenerek yeni bir kural önerebilir; örneğin bir müşterinin yeni banka hesabını ana veriye eklemeyi.

**Güvenlik ve kontrol.** Ödeme dosyalarının oluşturulduktan sonra değiştirilememesi, bankaya gönderilmeden önce ikinci bir kişinin onayı ve dosya toplamlarının ERP ile karşılaştırılması temel kontrollerdir. Banka bağlantı bilgileri ve sertifikalar güvenli biçimde saklanmalıdır.

**Standart formatlar.** ISO 20022 tabanlı mesajlar, daha zengin ve yapılandırılmış bilgi taşıdığı için eşleştirmeyi kolaylaştırır. Bankanızın hangi formatları desteklediğini ve geçiş planlarını düzenli olarak sorgulayın.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b5.py` ile yapılmıştır.

Bir dağıtıcıya ayda 1.000 banka tahsilatı geliyor. Bayilerin IBAN'ları müşteri kartlarına girildikten ve açıklamaya müşteri kodu yazılması istendikten sonra hareketlerin **%87,0**'si otomatik eşleşiyor. Kalan **130** kalem muhasebe ekibinin iş listesine düşüyor. Eşleşmeyenlerin çoğu, birden fazla faturayı tek seferde ödeyen bayilerden geliyor; bunun için "en eski faturadan kapat" kuralı ekleniyor.

## Sık yapılan hatalar

- Müşteri IBAN bilgilerini ERP'de tutmamak.
- Banka bağlantısını kurup eşleşmeyen kalem listesini takip etmemek.
- Ödeme dosyalarını onay akışı olmadan bankaya göndermek.
- Her banka için ayrı, belgelenmemiş bir entegrasyon yapmak.

## Pratikte nasıl uygulanır?

- [ ] Çalıştığınız bankaların hangi bağlantı yöntemlerini sunduğunu öğrenin.
- [ ] Müşteri kartlarına IBAN ve tahsilat referansı alanlarını ekleyin.
- [ ] Eşleştirme oranını ayda bir ölçün.
- [ ] Ödeme talimatları için iki aşamalı onay kurun.

## Daha fazlası

- ISO 20022 (doğrulanmadı): https://www.iso20022.org/
