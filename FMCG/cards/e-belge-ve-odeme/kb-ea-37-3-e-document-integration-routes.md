---
id: kb-ea-37-3-e-document-integration-routes
title: "E-belge entegrasyon yolları"
summary: "E-belge göndermek için GİB portalı, doğrudan entegrasyon ve özel entegratör seçeneklerini; entegratör API'lerini, hata yönetimini, yeniden denemeyi ve tekrarlanabilirliği (idempotency) anlatır."
course: ea
category: e-belge-ve-odeme
tags: [e-belge, entegrator, api, hata-yonetimi, idempotency]
roles: [finans-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-37.3]
reading_minutes: 2
key_points:
  - "E-belge göndermenin üç ana yolu GİB portalı, doğrudan entegrasyon ve özel entegratördür."
  - "Orta ölçekli şirketlerin çoğu özel entegratör üzerinden ERP entegrasyonu kurar."
  - "Entegrasyonda hata kodları, yeniden deneme ve durum sorgulama tasarlanmalıdır."
  - "Aynı belgenin iki kez gönderilmesini önlemek için tekil kimlikle tekrarlanabilirlik sağlanmalıdır."
  - "Yetkili entegratör listesi ve kurallar değişebilir; güncel durum kontrol edilmelidir."
glossary_terms: [ozel-entegrator, idempotency]
related: [kb-ea-37-2-e-fatura-scenarios, kb-ea-37-1-e-document-map, kb-ea-11-6-apis-for-managers, kb-ea-40-4-integrating-sfa-with-erp]
sources:
  - title: "Özel entegratör listesi"
    authors: "GİB"
    year: 2026
    type: web
    url: "https://ebelge.gib.gov.tr/"
    verified: false
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

E-belge zorunluluğu geldiğinde şirketler "nasıl göndereceğiz?" sorusuyla karşılaşır. Seçim, maliyeti, iş yükünü ve hata riskini belirler. Bu kart seçenekleri ve iyi bir entegrasyonun nasıl tasarlanacağını anlatır.

## Temel fikir

**Üç yol:**

1. **GİB portalı:** Belgeler web arayüzünden elle düzenlenir. Az belge kesen işletmeler için uygundur; ERP ile otomatik bağlantı yoktur.
2. **Doğrudan entegrasyon:** Şirket kendi sistemini GİB'e bağlar. Yüksek teknik yeterlilik ve izin gerektirir.
3. **Özel entegratör:** Yetkili bir hizmet sağlayıcı belgeleri sizin adınıza iletir. ERP, entegratörün API'sine bağlanır. Orta ölçekli şirketlerin yaygın tercihidir.

**İyi entegrasyonun unsurları:**

- **Durum sorgulama:** Belge gönderildi mi, ulaştı mı, reddedildi mi?
- **Hata kodları:** Her hata için bir sorumlu ve eylem.
- **Yeniden deneme:** Ağ hatasında belge belirli aralıklarla tekrar gönderilir.
- **Tekrarlanabilirlik (idempotency):** Aynı belge tekil kimliğiyle gönderilir; yeniden denemede ikinci belge oluşmaz.
- **Loglama:** Her çağrının kaydı saklanır.

### Yol seçiminde değerlendirme ölçütleri

Entegrasyon yolunu seçmek, yalnızca teknik bir karar değildir; maliyet, sorumluluk ve risk dengesini de belirler. Seçim yapılırken şu sorular sorulmalıdır:

- **Belge hacmi ve büyüme:** Aylık belge sayısı ve beklenen büyüme, fiyatlandırma modelini doğrudan etkiler. Belge başına ücret ile sabit ücret karşılaştırılmalıdır.
- **İç teknik kapasite:** Kendi altyapınızla doğrudan entegrasyon, sürekli bakım, mevzuat takibi ve güvenlik yönetimi gerektirir. Bu kapasite şirket içinde yoksa özel entegratör kullanmak genellikle daha az riskli olur.
- **ERP uyumu:** ERP sağlayıcınızın hazır bağlantı sunduğu entegratörler, uyarlama süresini kısaltır.
- **Hizmet seviyesi:** Entegratörün kesinti süreleri, destek saatleri, ay sonu yoğunluğunda performansı ve olay bildirim süreleri sözleşmede yazılı olmalıdır.
- **Çıkış koşulları:** Entegratör değiştirildiğinde geçmiş belgelerin ve arşivin nasıl taşınacağı önceden belirlenmelidir.

**Kesinti planı.** Entegratörün veya bağlantının kesilmesi durumunda sevkiyatın durup durmayacağı ve hangi alternatif adımların izleneceği yazılı bir prosedürde yer almalıdır. Kesinti sırasında oluşturulamayan belgelerin daha sonra hangi sırayla ve nasıl gönderileceği de tanımlanmalıdır.

**İzleme panosu.** Gönderilen, bekleyen, hata alan ve yanıt bekleyen belgelerin günlük durumu tek bir ekranda görülebilmelidir. Hata alan belgelerin sorumlusu ve çözüm süresi izlenmelidir. Uygulamadaki ayrıntılar ve güncel yükümlülükler için mali müşavirinize danışmanız önerilir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b8.py` ile yapılmıştır.

Bir şirket ayda 3.000 belge gönderiyor; entegratörün belge başına varsayımsal ücreti 0,40 TL. Aylık maliyet **1.200,00 TL**, yıllık **14.400,00 TL**. Şirket bu tutarı, portalda elle düzenleme için gereken personel süresiyle karşılaştırarak entegratörü seçiyor.

## Sık yapılan hatalar

- Ağ hatasında belgeyi yeni kimlikle tekrar göndermek ve mükerrer belge üretmek.
- Durum sorgulamayı kurmayıp "gönderildi" varsaymak.
- Entegratör sözleşmesinde hizmet düzeyini ve çıkış koşullarını yazmamak.
- Hata yanıtlarını kimsenin izlememesi.

## Pratikte nasıl uygulanır?

- [ ] Aylık belge hacminizi ve büyüme beklentinizi çıkarın.
- [ ] Üç yolu maliyet, iş yükü ve risk açısından karşılaştırın.
- [ ] Entegratörün güncel yetkisini kontrol edin.
- [ ] Yeniden deneme ve tekil kimlik kuralını teknik şartnameye yazın.
- [ ] Hata kuyruğu ve sorumlusunu belirleyin.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın. Seçeceğiniz yolu ve entegratörün yetkisini mutlaka mali müşaviriniz ve entegratörünüzle teyit edin.

## Daha fazlası

- GİB e-Belge portalı, özel entegratör listesi (doğrulanmadı).
