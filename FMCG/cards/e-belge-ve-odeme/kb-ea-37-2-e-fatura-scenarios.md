---
id: kb-ea-37-2-e-fatura-scenarios
title: "E-fatura senaryoları ve teknik yapısı"
summary: "E-faturanın UBL-TR formatını, temel ve ticari fatura senaryolarını, zarf ve uygulama yanıtı kavramlarını, ETTN ve görüntüleme şablonlarını iş tarafı için anlaşılır biçimde anlatır."
course: ea
category: e-belge-ve-odeme
tags: [e-fatura, ubl-tr, senaryo, ettn, entegrasyon]
roles: [finans-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-37.2]
reading_minutes: 2
key_points:
  - "E-fatura, UBL-TR adı verilen XML tabanlı bir standartla oluşturulur."
  - "Temel fatura ve ticari fatura senaryoları, alıcının faturaya yanıt verip veremeyeceğiyle ayrışır."
  - "Her faturanın ETTN adı verilen tekil bir kimliği vardır."
  - "Fatura mali mühür ile imzalanır; görüntüsü XSLT şablonuyla oluşturulur."
  - "Senaryo ve kurallar değişebileceği için güncel GİB kılavuzları ve mali müşavir kontrolü gerekir."
glossary_terms: [ubl-tr, ettn, ticari-fatura]
related: [kb-ea-37-1-e-document-map, kb-ea-37-3-e-document-integration-routes, kb-ea-35-2-e-signature-kep-seal, kb-ea-20-2-order-to-cash]
sources:
  - title: "e-Fatura teknik kılavuzları"
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

E-fatura bir PDF değildir; yapılandırılmış bir veri dosyasıdır. Bu kart, iş tarafındaki kişinin entegratör veya BT ekibiyle aynı dili konuşabilmesi için temel kavramları anlatır.

## Temel fikir

- **UBL-TR:** Uluslararası UBL standardının Türkiye'ye uyarlanmış hâlidir. Fatura satırları, vergiler ve taraflar XML içinde alan alan yer alır.
- **Senaryolar:**
  - **Temel fatura:** Alıcı sistem üzerinden kabul veya red yanıtı vermez; itiraz sistem dışında yürür.
  - **Ticari fatura:** Alıcı belirli süre içinde sistem üzerinden kabul veya red yanıtı verebilir.
- **Zarf:** Faturanın taşındığı elektronik paket; gönderim durumu zarf üzerinden izlenir.
- **Uygulama yanıtı:** Ticari faturada alıcının kabul/red cevabı.
- **ETTN:** Her faturaya verilen tekil kimlik (UUID). Mükerrer kaydı önlemek için ERP'de saklanmalıdır.
- **XSLT şablonu:** Faturanın insan tarafından okunur görüntüsünü üretir; logo ve düzen buradan gelir.
- **Mali mühür:** Fatura kurum adına elektronik olarak imzalanır.

### Senaryo seçimini ERP'ye doğru tanımlamak

E-fatura hatalarının önemli bir kısmı, teknik sorunlardan değil, ana veri ve iş kurallarının yanlış tanımlanmasından kaynaklanır. ERP'de dikkat edilmesi gereken noktalar şunlardır:

- **Alıcının mükellefiyet durumu:** Faturanın e-fatura mı, e-arşiv mi olarak düzenleneceği, alıcının kayıtlı kullanıcı olup olmamasına bağlıdır. Bu bilgi, kayıtlı kullanıcı listesinden düzenli olarak güncellenmeli ve elle girilmemelidir.
- **Senaryo kuralları:** Müşteri bazında hangi senaryonun kullanılacağı ana veride tanımlanmalıdır. Kabul veya ret yanıtı gerektiren senaryolarda, yanıtların ERP'ye geri alınması ve sürenin izlenmesi gerekir.
- **Fatura tipleri:** Satış, iade, tevkifatlı veya istisna gibi fatura tipleri, ERP'deki işlem türleriyle eşleştirilmelidir. Yanlış tip, hem alıcının itirazına hem de vergi hatasına yol açabilir.
- **Birim ve kod eşleştirmeleri:** Ölçü birimleri, vergi kodları ve istisna kodları standart kod listeleriyle eşleştirilmelidir.
- **Görsel şablon:** Faturanın görüntüsü, müşterinin ihtiyaç duyduğu bilgileri (sipariş numarası, irsaliye numarası, ödeme bilgisi) içermelidir.

**Test ve değişiklik yönetimi.** Mevzuat veya kod listelerinde değişiklik olduğunda, entegratör ve ERP tarafındaki uyarlamaların test ortamında denenmesi gerekir. Değişiklik takvimini mali müşavirinizle ve entegratörünüzle birlikte izleyin. Ret edilen faturaların nedenleri sınıflandırılarak raporlanırsa, tekrarlayan hatalar kaynağında düzeltilebilir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b8.py` ile yapılmıştır.

Bir dağıtıcı ayda 1.000 ticari fatura kesiyor; bunlardan 12'si alıcı tarafından reddediliyor. Red oranı **%1,2**. İnceleme, reddin çoğunun yanlış fiyat listesinden geldiğini gösteriyor. Ekip, red yanıtlarını ERP'de otomatik bir iş kuyruğuna düşürüyor.

## Sık yapılan hatalar

- E-faturayı PDF gibi görmek ve XML verisini kontrol etmemek.
- ETTN'yi ERP'de saklamamak; mükerrer veya kayıp kayıt oluşması.
- Ticari faturada red yanıtlarını takip etmemek.
- Görüntü şablonunu değiştirip veriyi değişmiş sanmak.

## Pratikte nasıl uygulanır?

- [ ] Hangi müşterilere hangi senaryoyla fatura kestiğinizi mali müşavirinizle belirleyin.
- [ ] ETTN ve gönderim durumunu ERP'deki fatura kaydına bağlayın.
- [ ] Red ve hata yanıtları için bir iş kuyruğu ve sorumlu tanımlayın.
- [ ] GİB kılavuz güncellemelerini entegratörünüzle düzenli kontrol edin.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın. Senaryo seçimi ve iade/red uygulamalarını mutlaka mali müşaviriniz ve entegratörünüzle teyit edin.

## Daha fazlası

- GİB e-Belge portalı ve UBL-TR kılavuzları (doğrulanmadı).
