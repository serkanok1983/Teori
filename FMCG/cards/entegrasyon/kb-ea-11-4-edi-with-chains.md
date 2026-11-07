---
id: kb-ea-11-4-edi-with-chains
title: "Zincir marketlerle elektronik veri değişimi (EDI)"
summary: "Zincir marketlerle sipariş, sevk bildirimi ve fatura gibi belgelerin standart biçimlerde elektronik alışverişini (EDI) anlatır; elle sipariş girişinin maliyetini ve EDI projesine hazırlık adımlarını verir."
course: ea
category: entegrasyon
tags: [entegrasyon, edi, zincir-market, siparis, gs1]
roles: [uretici-sahibi, uretici-yonetici, it-yoneticisi]
level: orta
source_lessons: [EA-11.4]
reading_minutes: 3
key_points:
  - "EDI, firmalar arasında sipariş, sevk bildirimi ve fatura gibi belgelerin standart biçimde otomatik değişimidir."
  - "Yaygın standartlar EDIFACT ve onun perakende alt kümesi EANCOM ile GS1 XML'dir."
  - "Sevk bildirimi (DESADV), palet SSCC'leriyle birlikte mal kabulünü hızlandırır."
  - "EDI'nin önkoşulu doğru ana veridir: ürün kodları, koli içi adetler, teslim yeri numaraları."
  - "Türkiye'de fatura tarafı e-fatura ile yürür; EDI daha çok sipariş ve sevk bildirimi için kullanılır."
glossary_terms: [edi, gtin]
related: [kb-ea-8-4-gs1-barcodes-pim, kb-ea-28-1-order-management, kb-ea-37-2-e-fatura-scenarios, kb-ea-10-1-why-integration-is-hard]
sources:
  - title: "EANCOM (GS1)"
    authors: "GS1"
    year: 2026
    type: standard
    verified: false
    note: "gs1.org kutudan erişilemedi."
  - title: "Enterprise Integration Patterns"
    authors: "Hohpe, G.; Woolf, B."
    year: 2003
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

Zincir marketlerin siparişleri portaldan indirilip ERP'ye elle giriliyorsa hem zaman kaybı hem de hatalı sevkiyat kaçınılmazdır. Bu kart, **elektronik veri değişimini** (EDI, *electronic data interchange*) ve bir zincirle EDI'ye başlarken neler gerektiğini anlatır.

## Temel fikir

EDI'de belgeler standart bir yapıda, sistemden sisteme insan müdahalesi olmadan gider. Perakende–tedarikçi ilişkisinde tipik akış:

1. **Sipariş** (ORDERS): Zincir, mağaza veya depo teslim yeriyle siparişi gönderir.
2. **Sipariş yanıtı** (ORDRSP): Tedarikçi miktarları onaylar veya değiştirir.
3. **Sevk bildirimi** (DESADV): Hangi palette hangi üründen kaç adet olduğu, palet SSCC numaralarıyla.
4. **Fatura:** Türkiye'de e-fatura ile gönderilir.

Kullanılan standartlar: Birleşmiş Milletler'in EDIFACT standardı, onun perakendeye uyarlanmış alt kümesi EANCOM ve GS1 XML. Belgeler AS2 gibi güvenli iletim protokolleriyle ya da bir EDI hizmet sağlayıcısı üzerinden taşınır. Çoğu orta ölçekli tedarikçi, standartları kendisi işlemek yerine bir hizmet sağlayıcıyla çalışır.

EDI'nin önkoşulu doğru ana veridir. Zincirin ürün kodunuzla sizin kodunuzun eşlenmesi, koli içi adet, teslim yerlerinin GLN numaraları tutarlı değilse otomatik sipariş otomatik hata üretir.

### EDI projesinde dikkat edilecek noktalar

Zincir marketlerle EDI kurulumu, her zincirin kendi gereksinimleri nedeniyle çoğu zaman beklenenden uzun sürer. Projeyi kolaylaştırmak için şu konulara dikkat edilmelidir:

- **Zincirin gereksinim belgesi:** Her zincir, hangi mesaj türlerini, hangi formatta ve hangi alanlarla beklediğini belirten bir rehber yayımlar. Bu rehber, proje başında ayrıntılı olarak incelenmelidir.
- **Ürün ve lokasyon kodları:** EDI mesajlarında ürünler genellikle barkod numarası, teslimat noktaları ise lokasyon numarasıyla tanımlanır. Bu kodların ERP'de doğru ve eksiksiz tanımlanmış olması, entegrasyonun ön koşuludur.
- **Fiyat uyumu:** Siparişteki fiyat ile faturadaki fiyatın farklı olması, zincirlerde fatura reddinin en yaygın nedenlerinden biridir. Fiyat anlaşmalarının ERP'ye zamanında ve doğru girilmesi gerekir.
- **Sevk bildirimi:** Bazı zincirler, sevkiyattan önce ayrıntılı sevk bildirimi ve palet etiketi talep eder. Bu, depo süreçlerinde barkodlu palet etiketleme gerektirebilir.
- **Test süreci:** Canlıya geçmeden önce, zincirle birlikte tüm mesaj türleri test ortamında denenmelidir.

**Hata yönetimi.** Reddedilen veya işlenemeyen mesajlar için günlük bir kontrol listesi oluşturulmalıdır. Hata nedenleri sınıflandırılarak raporlanırsa, kaynağındaki ana veri veya süreç sorunları düzeltilebilir.

**Hizmet sağlayıcı.** EDI genellikle bir hizmet sağlayıcı üzerinden yapılır. Sağlayıcının zincirlerle hazır bağlantıları olması, kurulum süresini kısaltır. GS1 standartları, mesaj ve kimlik yapısının ortak bir dille tanımlanmasını sağlar.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b3.py` ile yapılmıştır.

Bir üretici, iki zincirden günde ortalama 300 sipariş satırı alıyor. Her satır portaldan okunup ERP'ye ortalama 1,5 dakikada giriliyor:

- Günde 300 × 1,5 = 450 dakika, yani **7,5 saat**; 22 iş günüyle ayda **165 saat**.
- Satırların %1,5'inde miktar veya ürün hatası oluyor: ayda **99** hatalı satır.

EDI'ye geçişte firma önce zincirin ürün kodları ile kendi kodları arasındaki eşleme tablosunu temizliyor, koli içi adetleri doğruluyor ve teslim yerlerinin GLN'lerini sisteme giriyor. Ardından yalnızca sipariş belgesiyle başlıyor; sevk bildirimini ikinci aşamaya bırakıyor.

## Sık yapılan hatalar

- Ana veriyi düzeltmeden EDI'yi açmak.
- Gelen EDI siparişini kimsenin kontrol etmeden otomatik sevke göndermek; anormal miktarlar için eşik koyulmalıdır.
- Sevk bildiriminde palet içeriğini gerçek yüklemeyle eşleştirmemek.
- Tüm belgeleri aynı anda canlıya almak.

## Pratikte nasıl uygulanır?

- [ ] Zincirlerin desteklediği EDI belgelerini ve standartlarını öğrenin.
- [ ] Ürün kodu eşleme, koli içi adet ve GLN bilgilerini doğrulayın.
- [ ] Bir EDI hizmet sağlayıcısı ile kendi entegrasyonunuzu karşılaştırın.
- [ ] Önce siparişle başlayın; anormal miktar için onay eşiği koyun.
- [ ] Sonra sevk bildirimini palet etiketleriyle birlikte devreye alın.

## Daha fazlası

- GS1 EANCOM kılavuzları (erişilemedi; doğrulanmadı).
- Hohpe ve Woolf, *Enterprise Integration Patterns* (kitap; doğrulanmadı).
