---
id: kb-ea-37-4-e-defter-e-arsiv
title: "E-defter ve e-arşiv"
summary: "E-defterin oluşturulması ve berat kavramını, e-arşiv fatura ve elektronik saklama yükümlülüklerini, ERP defterleriyle mutabakatın nasıl yapılacağını genel çerçevede anlatır."
course: ea
category: e-belge-ve-odeme
tags: [e-defter, e-arsiv, berat, saklama, mutabakat]
roles: [finans-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-37.4]
reading_minutes: 2
key_points:
  - "E-defter, yasal defterlerin elektronik ortamda belirli formatta oluşturulup imzalanmasıdır."
  - "Berat, e-defterin teslim edildiğini gösteren onay belgesidir."
  - "E-arşiv fatura, e-fatura kullanıcısı olmayan alıcılara düzenlenen elektronik faturadır."
  - "E-defter verisi ERP'deki yevmiye ve mizanla mutabık olmalıdır."
  - "Süreler, saklama ve beyan kuralları değişebileceği için mali müşavir kontrolü şarttır."
glossary_terms: [e-defter, berat, e-arsiv-fatura]
related: [kb-ea-37-3-e-document-integration-routes, kb-ea-22-1-chart-of-accounts-tekduzen, kb-ea-35-1-document-archive-retention, kb-ea-37-1-e-document-map]
sources:
  - title: "e-Defter ve e-Arşiv duyuruları"
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

E-defter, muhasebe kayıtlarının resmî karşılığıdır. ERP'deki kayıt ile resmî defter farklılaşırsa sorun genellikle aylar sonra fark edilir. Bu kart, e-defter ve e-arşivin iş sistemleriyle ilişkisini anlatır.

## Temel fikir

**E-defter:** Yevmiye ve büyük defter gibi yasal defterlerin belirli bir elektronik formatta oluşturulması ve mali mühür veya elektronik imzayla imzalanmasıdır. Genellikle ERP veya entegratör çözümü tarafından üretilir.

**Berat:** E-defterin teslim edildiğini gösteren onay dosyasıdır. Beratlar saklanmalı ve dönem kapanışında kontrol edilmelidir.

**E-arşiv fatura:** E-fatura kullanıcısı olmayan alıcılara (örneğin nihai tüketici) düzenlenen elektronik faturadır. Raporlama ve saklama kuralları vardır.

**Saklama:** Elektronik belgeler, yasal süre boyunca bütünlüğü korunarak ve erişilebilir biçimde saklanmalıdır.

**Mutabakat:** Her ay e-defter toplamları, ERP'deki mizan ile karşılaştırılmalıdır. Defter kapandıktan sonra ERP'de geriye dönük kayıt yapılmasını engelleyen bir dönem kilidi kullanılmalıdır.

### Sistem açısından hazırlık ve kontrol

E-defter ve e-arşiv süreçleri, muhasebe kayıtlarının doğruluğuna ve sistemin düzenli çalışmasına doğrudan bağlıdır. BT ve finans ekiplerinin birlikte izlemesi gereken başlıca konular şunlardır:

- **Dönem kapanışı disiplini:** E-defter oluşturulmadan önce ilgili dönemin kayıtları tamamlanmış ve kontrol edilmiş olmalıdır. Kapanıştan sonra geriye dönük kayıt açılmasını önleyen dönem kilitleri ERP'de kullanılmalıdır.
- **Yevmiye ve hesap planı tutarlılığı:** Hesap planındaki değişiklikler ve kayıt numaralandırması, defterin teknik kontrollerinden geçebilmesi için tutarlı olmalıdır.
- **Takvim:** Defterlerin ve beratların hazırlanma ve yükleme tarihleri bir takvimde izlenmeli, sorumlular adıyla belirlenmelidir. Güncel süreler için mali müşavirinize ve resmî duyurulara başvurun.
- **Saklama ve erişim:** Elektronik belgelerin ve beratların yasal saklama süresi boyunca okunabilir biçimde korunması gerekir. Saklama hizmeti bir entegratörden alınıyorsa, sözleşmede veriye erişim ve hizmetin sona ermesi durumunda verinin teslimi açıkça düzenlenmelidir.
- **E-arşiv raporlaması:** E-arşiv faturalarının raporlanması ve iptal işlemleri için entegratör ekranları düzenli kontrol edilmelidir. İptal edilen faturaların ERP'de de iptal edildiğinden emin olun.

**Denetime hazırlık.** Bir inceleme sırasında istenebilecek defter, berat ve faturaların hızla bulunabilmesi için bir arşiv düzeni ve erişim prosedürü hazırlayın. Yıllık olarak bir örneklem üzerinden belgelerin bütünlüğünü ve erişilebilirliğini test etmek iyi bir uygulamadır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b8.py` ile yapılmıştır.

Bir şirket 12 aylık dönemin her ayı için e-defter oluşturuyor. Bir ay, defter yüklendikten sonra ERP'de geriye dönük kayıt yapıldığı fark ediliyor; mizan ile e-defter tutmuyor. Şirket bundan sonra her ay için dönem kilidi ve kapanış kontrol listesi uygulamaya başlıyor.

## Sık yapılan hatalar

- E-defter yüklendikten sonra ERP'de kapanmış döneme kayıt atmak.
- Beratları saklamamak veya kontrol etmemek.
- E-arşiv fatura raporlamasını entegratöre bırakıp izlememek.
- Saklama sorumluluğunu belirsiz bırakmak.

## Pratikte nasıl uygulanır?

- [ ] ERP'de aylık dönem kilidi kullanın.
- [ ] Her ay mizan–e-defter mutabakatı yapın.
- [ ] Beratları arşivde belge türü olarak saklayın.
- [ ] Yükleme takvimini ve sorumluyu mali müşavirinizle belirleyin.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın. E-defter yükleme süreleri, saklama ve düzeltme usullerini mutlaka mali müşavirinizle teyit edin.

## Daha fazlası

- GİB e-Belge portalı, e-Defter ve e-Arşiv bölümleri (doğrulanmadı).
