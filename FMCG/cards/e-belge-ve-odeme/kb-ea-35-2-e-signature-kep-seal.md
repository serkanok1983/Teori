---
id: kb-ea-35-2-e-signature-kep-seal
title: "Elektronik imza, mali mühür ve KEP"
summary: "Güvenli elektronik imza, mali mühür ve kayıtlı elektronik posta (KEP) kavramlarını, hangi işte hangisinin kullanıldığını ve iş sistemlerine nasıl bağlandığını genel çerçevede anlatır."
course: ea
category: e-belge-ve-odeme
tags: [e-imza, mali-muhur, kep, hukuk, belge]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-35.2]
reading_minutes: 3
key_points:
  - "Güvenli elektronik imza, 5070 sayılı Kanun çerçevesinde kişiye bağlı bir imza aracıdır."
  - "Mali mühür, bir kişiye değil kuruma ait olup e-belgelerin imzalanmasında kullanılır."
  - "KEP, gönderim ve teslimi ispat edilebilir biçimde kayda geçiren elektronik posta hizmetidir."
  - "Hangi işlemde hangi aracın yeterli olduğu hukukçuyla teyit edilmelidir."
  - "AB'de benzer çerçeve eIDAS düzenlemesiyle kurulmuştur; iki sistem birebir aynı değildir."
glossary_terms: [guvenli-elektronik-imza, mali-muhur, kep]
related: [kb-ea-35-1-document-archive-retention, kb-ea-37-1-e-document-map, kb-ea-37-2-e-fatura-scenarios]
sources:
  - title: "5070 sayılı Elektronik İmza Kanunu"
    authors: "TBMM"
    year: 2004
    type: web
    url: "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5070.pdf"
    verified: true
    checked_on: 2026-10-28
    note: "Mevzuat Bilgi Sistemi resmî PDF metni açıldı, kanun adı ve numarası eşleşti (2026-10-28)."
  - title: "Gelir İdaresi Başkanlığı"
    authors: "GİB"
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

Sözleşmeler, bayi anlaşmaları ve resmî yazışmalar hâlâ kâğıt, kargo ve ıslak imzayla ilerliyorsa süreç günlerce uzar. Bu kart, dijital imza ve tebligat araçlarını ayırt etmenize ve iş sistemlerinize doğru yerde bağlamanıza yardım eder.

## Temel fikir

**Üç ayrı araç:**

- **Güvenli elektronik imza:** Bir kişiye bağlı nitelikli sertifikayla atılan imzadır. 5070 sayılı Kanun bu imzanın hukuki çerçevesini düzenler.
- **Mali mühür:** Kişiye değil, kuruma (vergi mükellefine) ait bir elektronik sertifikadır. E-fatura, e-defter gibi belgelerin kurum adına imzalanmasında kullanılır.
- **KEP (kayıtlı elektronik posta):** Gönderimin ve teslimin zamanını ispatlanabilir biçimde kayda alan e-posta hizmetidir. Resmî bildirim ve ihtar gibi yazışmalarda kullanılır.

**Sistem tarafı:** Sözleşme yönetimi, satın alma veya İK sistemi imza akışını başlatır; imzalı belge ve imza doğrulama bilgisi arşive gider. Mali mühür genellikle e-belge entegratörü veya ERP tarafında, sunucu üzerinde kullanılır.

**AB karşılaştırması:** AB'de eIDAS düzenlemesi basit, gelişmiş ve nitelikli imza düzeylerini tanımlar. Türkiye çerçevesi benzer amaçlara hizmet eder ancak terimler ve sonuçları birebir aynı değildir; sınır ötesi işlerde hukuki destek gerekir.

### Kullanım alanlarını ve sorumlulukları belirlemek

Elektronik imza, mali mühür ve KEP'in şirket içinde doğru kullanılması için hangi işlerde hangi aracın kullanılacağının ve kimin sorumlu olduğunun belirlenmesi gerekir:

- **Kullanım envanteri:** Hangi belge ve işlemlerde elektronik imza, hangilerinde mali mühür, hangi yazışmalarda KEP kullanıldığı bir listede toplanmalıdır. Bu liste, yeni bir süreç tasarlanırken de başvuru kaynağı olur.
- **Sertifika takibi:** Elektronik imza ve mali mühür sertifikalarının geçerlilik süreleri sınırlıdır. Bitiş tarihleri bir takvimde izlenmeli ve yenileme işlemleri süresi dolmadan başlatılmalıdır. Süresi dolan bir sertifika, e-belge gönderimini durdurabilir.
- **Yetkili kişiler:** Elektronik imza kişiye özeldir; başkası tarafından kullanılmamalıdır. İmza yetkisinin şirketin imza sirküleriyle uyumlu olması gerekir.
- **Görevden ayrılma:** Elektronik imza sahibi bir çalışan şirketten ayrıldığında, imzanın şirket adına kullanımının sona erdirilmesi ve gerekli bildirimlerin yapılması gerekir.
- **KEP kutusunun takibi:** KEP adresine gelen tebligat ve yazışmalar düzenli olarak kontrol edilmelidir. Okunmayan bir tebligat, süre kaçırılmasına ve hukuki sonuçlara yol açabilir.

**Sistem entegrasyonu.** E-belge sistemlerinde mali mühür genellikle entegratör veya sunucu üzerinde kullanılır; bu durumda mühre erişimin güvenliği ve yedekliliği önemlidir. Uygulamadaki yasal ayrıntılar ve güncel yükümlülükler için hukuk danışmanınıza ve mali müşavirinize başvurmanız önerilir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b8.py` ile yapılmıştır.

Bir dağıtıcı yılda 400 bayi sözleşmesi yeniliyor. Kargo ve ıslak imzayla her sözleşme ortalama 3 gün sürüyor. Elektronik imzaya geçince süre 1 güne iniyor; yılda toplam **800** sözleşme-günü kazanılıyor. Şirket, bayiye ihtar gönderimleri için ayrıca KEP kullanmaya başlıyor.

## Sık yapılan hatalar

- Taranmış ıslak imzayı elektronik imza sanmak.
- Mali mühürü bir çalışanın kişisel imzası gibi kullanmak.
- Sertifika süresinin dolmasını takip etmemek.
- İmzalı belgeyi doğrulama bilgisi olmadan arşivlemek.
- Hangi belgenin hangi imzayı gerektirdiğini hukukçuya sormadan karar vermek.

## Pratikte nasıl uygulanır?

- [ ] Belge türlerini listeleyin ve her biri için gereken imza düzeyini avukatınızla belirleyin.
- [ ] Sertifika sahiplerini ve bitiş tarihlerini bir takvimde izleyin.
- [ ] İmza akışını sözleşme veya İK sistemine bağlayın.
- [ ] İmzalı belgeleri doğrulama bilgisiyle birlikte arşivleyin.
- [ ] Resmî bildirimler için KEP adresi edinmeyi değerlendirin.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın. İmza ve tebligat konularında hangi aracın hukuken yeterli olduğunu mutlaka avukatınızla teyit edin.

## Daha fazlası

- 5070 sayılı Elektronik İmza Kanunu (mevzuat.gov.tr; doğrulanmadı).
- Mali mühür ve e-belge duyuruları için GİB sitesi (doğrulanmadı).
