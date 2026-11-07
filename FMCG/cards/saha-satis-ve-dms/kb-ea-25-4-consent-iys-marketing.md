---
id: kb-ea-25-4-consent-iys-marketing
title: "Pazarlama otomasyonu, müşteri veri platformu ve İYS ile izin yönetimi"
summary: "Pazarlama otomasyonu ve müşteri veri platformlarının ne işe yaradığını, ticari elektronik ileti gönderiminde onay ve İleti Yönetim Sistemi (İYS) kurallarını, KVKK açık rızası ile ticari ileti onayı arasındaki farkı ve sistemde izinlerin nasıl tutulacağını anlatır."
course: ea
category: saha-satis-ve-dms
tags: [pazarlama-otomasyonu, iys, kvkk, izin, ticari-ileti]
roles: [uretici-sahibi, uretici-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, it-yoneticisi]
level: orta
source_lessons: [EA-25.4]
reading_minutes: 2
key_points:
  - "Pazarlama otomasyonu kampanyaları segment ve tetikleyicilere göre otomatik yürütür."
  - "Müşteri veri platformu farklı kaynaklardaki müşteri verisini tek profilde birleştirir."
  - "Ticari elektronik ileti göndermek için kural olarak alıcının önceden onayı gerekir ve onaylar İYS'ye kaydedilir."
  - "KVKK açık rızası ile ticari ileti onayı farklı hukuki konulardır; ikisi ayrı yönetilmelidir."
  - "Gönderim öncesi liste İYS'deki güncel izin durumuyla karşılaştırılmalıdır."
glossary_terms: [iys, ticari-elektronik-ileti, pazarlama-otomasyonu, kvkk, acik-riza]
related: [kb-ea-15-5-kvkk-basics, kb-ea-25-1-crm-basics, kb-ea-25-5-customer-service-cases]
sources:
  - title: "İleti Yönetim Sistemi"
    authors: "İYS"
    year: 2026
    type: web
    url: "https://iys.org.tr/"
    verified: true
    checked_on: 2026-10-28
  - title: "6563 sayılı Elektronik Ticaretin Düzenlenmesi Hakkında Kanun"
    authors: "T.C. Cumhurbaşkanlığı Mevzuat Bilgi Sistemi"
    year: 2014
    type: law
    url: "https://www.mevzuat.gov.tr/"
    verified: true
    checked_on: 2026-10-28
  - title: "Kişisel Verileri Koruma Kurumu"
    authors: "KVKK"
    year: 2026
    type: web
    url: "https://www.kvkk.gov.tr/"
    verified: true
    checked_on: 2026-10-28
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Üreticiler tüketicilere ve satış noktalarına SMS, e-posta ve arama yoluyla kampanya duyurmak ister. Bu kart, bunu yapan sistemleri ve Türkiye'deki izin kurallarının sistem tarafını anlatır.

## Temel fikir

**Pazarlama otomasyonu.** Kampanyaları segmentlere ve tetikleyicilere göre otomatik yürütür. Örnek: "Son 30 gündür sipariş vermeyen noktalara hatırlatma mesajı gönder."

**Müşteri veri platformu (CDP).** CRM, e-ticaret, sadakat programı ve saha satış verilerini tek bir müşteri profilinde birleştirir. Pazarlama otomasyonunun hangi kişiye ne göndereceğini bu profil belirler.

**Ticari elektronik ileti ve İYS.** 6563 sayılı Kanun ve ilgili yönetmelik kapsamında, mal ve hizmet tanıtımı amaçlı SMS, e-posta ve arama için kural olarak alıcının **önceden onayı** gerekir. Onaylar ve retler **İleti Yönetim Sistemi'ne (İYS)** kaydedilir; alıcılar izinlerini İYS üzerinden de görebilir ve geri alabilir. Tacir ve esnaf alıcılar için farklı kurallar bulunmaktadır; bu istisnaların kapsamını hukuk danışmanınızla netleştirin.

**KVKK ile farkı.** Kişisel verilerin pazarlama amacıyla işlenmesi için KVKK kapsamında ayrı bir hukuki dayanak (çoğu durumda açık rıza) ve aydınlatma gerekir. İYS onayı KVKK yükümlülüklerini, KVKK açık rızası da İYS onayını karşılamaz.

**Sistem tarafında yapılması gerekenler:**

- Her kişi için kanal bazında (SMS, e-posta, arama) izin durumu ve tarihi,
- İzinlerin İYS ile düzenli senkronizasyonu,
- Gönderim öncesi otomatik izin kontrolü,
- Ret taleplerinin tüm sistemlere hızla yansıtılması.

### İzin kayıtlarının kanıt değeri

Bir şikâyet veya inceleme durumunda, iletinin gönderildiği tarihte geçerli bir izin bulunduğunun kanıtlanması gerekebilir. Bu nedenle her izin için kaynağı (form, sözleşme, çağrı kaydı), tarihi, kanalı ve izin metninin o tarihteki sürümü saklanmalıdır. Ret ve izin geri alma talepleri de aynı titizlikle kaydedilmeli ve tüm gönderim araçlarına hızla yansıtılmalıdır. Pazarlama otomasyonu aracının, her gönderimden önce güncel izin durumunu kontrol etmesi en güvenli yoldur. Ticari ileti ile bilgilendirme iletisi arasındaki ayrım ve güncel kurallar için hukuk danışmanınıza başvurmanız önerilir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b5.py` ile yapılmıştır.

Bir üretici, sadakat programındaki 50.000 tüketiciye SMS kampanyası planlıyor. Gönderim öncesi liste İYS'deki izin durumuyla karşılaştırılıyor: SMS izni olan 32.000 kişi kalıyor. Gönderilebilir oran **%64,0**; **18.000** kişi listeden çıkarılıyor. Pazarlama ekibi, izin oranını artırmak için sadakat programı kayıt ekranındaki izin metnini hukuk danışmanıyla yeniden düzenliyor.

## Sık yapılan hatalar

- Eski müşteri listelerine izin kontrolü yapmadan toplu SMS göndermek.
- İYS onayını KVKK açık rızası yerine saymak (veya tersi).
- Ret taleplerini yalnızca bir sistemde güncellemek.
- İzin tarihini ve kaynağını kaydetmemek.

## Pratikte nasıl uygulanır?

- [ ] Tüm kanallardaki izinleri tek bir izin tablosunda toplayın.
- [ ] Gönderim aracınıza İYS kontrolünü zorunlu adım olarak ekleyin.
- [ ] İzin ve aydınlatma metinlerini avukatınıza kontrol ettirin.
- [ ] Ret taleplerinin tüm sistemlere yansıma süresini ölçün.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın. Ticari ileti onayı, tacir ve esnafa yönelik istisnalar ve KVKK yükümlülükleri hukuki yorum gerektirir; kampanya kurgusunu bir avukata doğrulatın.

## Daha fazlası

- İleti Yönetim Sistemi: https://iys.org.tr/
- 6563 sayılı Kanun: https://www.mevzuat.gov.tr/
- Kişisel Verileri Koruma Kurumu: https://www.kvkk.gov.tr/
