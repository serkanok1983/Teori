---
id: kb-ea-35-1-document-archive-retention
title: "Belge arşivi ve saklama süreleri"
summary: "Ticari belgelerin, sözleşmelerin ve personel dosyalarının elektronik arşivde nasıl düzenleneceğini; saklama sürelerinin belirlenmesini, erişim yetkilerini ve süre sonunda imha sürecini anlatır."
course: ea
category: bt-yonetisimi-ve-guvenlik
tags: [arsiv, saklama-suresi, dms, belge-yonetimi, kvkk]
roles: [finans-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-35.1]
reading_minutes: 3
key_points:
  - "Belge arşivi, belgelerin bulunabilir, değiştirilemez ve yetkili kişilerce erişilebilir olmasını sağlar."
  - "Saklama süreleri belge türüne göre mevzuattan ve şirket politikasından belirlenir."
  - "Kişisel veri içeren belgeler, saklama amacı sona erince silinmeli veya anonimleştirilmelidir."
  - "Arşivde belge türü, tarih, karşı taraf gibi üst veriler aramayı mümkün kılar."
  - "Saklama ve imha politikası yazılı olmalı ve uygulandığı kayıt altına alınmalıdır."
glossary_terms: [saklama-suresi, ust-veri, imha-politikasi]
related: [kb-ea-35-2-e-signature-kep-seal, kb-ea-37-4-e-defter-e-arsiv, kb-ea-33-1-hr-systems]
sources:
  - title: "6102 sayılı Türk Ticaret Kanunu"
    authors: "T.C."
    year: 2011
    type: law
    url: "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6102.pdf"
    verified: true
    checked_on: 2026-10-28
    note: "Mevzuat Bilgi Sistemi resmî PDF metni açıldı, kanun adı ve numarası eşleşti (2026-10-28)."
  - title: "6698 sayılı Kişisel Verilerin Korunması Kanunu"
    authors: "T.C."
    year: 2016
    type: law
    url: "https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6698.pdf"
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

Bir denetimde, davada veya müşteri itirazında aranan belgeyi bulamamak ciddi sonuçlar doğurur. Öte yandan kişisel veri içeren belgeleri gereğinden uzun saklamak da risktir. Bu kart, arşiv ve saklama süresi yönetimini anlatır.

## Temel fikir

**Elektronik arşivin temel özellikleri:**

- **Üst veri:** Belge türü, tarih, karşı taraf, ilgili sipariş veya sözleşme numarası. Arama bunlarla yapılır.
- **Değiştirilemezlik:** Arşive alınan belgenin sürümü kaydedilir; değişiklik yeni sürüm olarak tutulur.
- **Erişim yetkileri:** Personel dosyalarına İK, sözleşmelere hukuk ve ilgili yöneticiler erişir.
- **Bağlantı:** ERP kaydından ilgili belgeye tek tıkla ulaşmak.

**Saklama süreleri.** Türk Ticaret Kanunu, ticari defter ve belgeler için saklama yükümlülüğü getirir; vergi mevzuatında da ayrı süreler bulunur. Personel dosyaları ve diğer belgeler için süreler farklı olabilir. Her belge türü için süre, hukuki dayanağıyla birlikte bir tabloda tutulmalıdır.

**İmha.** 6698 sayılı Kanun, kişisel verilerin işlenme amacı ortadan kalktığında silinmesini, yok edilmesini veya anonim hale getirilmesini öngörür. Süresi dolan belgelerin imhası bir politika çerçevesinde yapılmalı ve kayda geçirilmelidir.

### Arşiv politikasını hazırlamak

Belge arşivi, ancak yazılı bir politikaya dayandığında tutarlı yönetilebilir. Politikanın kapsaması gereken başlıca konular şunlardır:

- **Belge türleri envanteri:** Şirkette üretilen ve alınan belge türleri listelenmelidir: faturalar, sözleşmeler, personel dosyaları, yazışmalar, teslim belgeleri ve kalite kayıtları gibi.
- **Saklama süreleri:** Her belge türü için yasal ve iş ihtiyacına dayanan saklama süresi belirlenmelidir. Süreler farklı kanunlardan kaynaklanabilir ve değişebilir; bu nedenle tablo, hukuk danışmanı ve mali müşavirle birlikte hazırlanmalı ve düzenli olarak gözden geçirilmelidir.
- **Sorumluluk:** Her belge türünün arşivlenmesinden sorumlu birim ve kişi tanımlanmalıdır.
- **Saklama ortamı:** Hangi belgelerin elektronik, hangilerinin fiziki olarak saklanacağı ve fiziki belgelerin taranması durumunda asıllarının ne olacağı belirlenmelidir.
- **İmha süreci:** Saklama süresi dolan belgelerin imhası, onaylı bir listeyle yapılmalı ve imha kaydı tutulmalıdır.

**Kişisel veri boyutu.** Kişisel veri içeren belgeler, yalnızca gerekli olduğu süre boyunca saklanmalıdır. Saklama süresi dolduğunda silme, yok etme veya anonim hâle getirme yükümlülüğü doğabilir. Bu nedenle kişisel veri envanteri ile arşiv politikasının birbiriyle uyumlu olması gerekir.

**Yasal saklama askısı.** Bir dava veya inceleme söz konusu olduğunda, ilgili belgelerin imhası durdurulmalıdır. Arşiv sisteminin bu askıyı uygulayabilmesi önemlidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b7.py` ile yapılmıştır.

Bir distribütör yılda yaklaşık 60.000 belge (irsaliye, sözleşme, yazışma, personel evrakı) üretiyor. On yıllık saklama varsayımıyla arşivde **600.000** belge birikecek. Şirket her belge türüne üst veri şablonu ve saklama süresi atıyor; süresi dolan kayıtlar yılda bir imha listesine düşüyor ve onayla siliniyor.

## Sık yapılan hatalar

- Belgeleri ortak klasörlerde, adlandırma kuralı olmadan tutmak.
- Saklama süresini belge türüne göre belirlememek.
- Kişisel veri içeren belgeleri süresiz saklamak.
- İmhayı kayıt altına almamak.

## Pratikte nasıl uygulanır?

- [ ] Belge türleri ve saklama süreleri tablosunu hazırlayın.
- [ ] Her tür için üst veri şablonu tanımlayın.
- [ ] Erişim yetkilerini rol bazında belirleyin.
- [ ] Yıllık imha sürecini kurun ve kayıt altına alın.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın. Belge türlerine göre saklama sürelerini ve imha koşullarını avukatınız ve mali müşavirinizle doğrulayın.

## Daha fazlası

- 6102 sayılı Türk Ticaret Kanunu: https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6102.pdf
- 6698 sayılı Kişisel Verilerin Korunması Kanunu: https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6698.pdf
