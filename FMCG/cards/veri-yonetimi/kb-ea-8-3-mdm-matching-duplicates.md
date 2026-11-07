---
id: kb-ea-8-3-mdm-matching-duplicates
title: "Mükerrer müşteri kayıtlarını bulmak: Eşleştirme ve ana veri yönetimi mimarileri"
summary: "Mükerrer nokta ve müşteri kayıtlarını benzerlik puanıyla bulmayı, hangi alanın hangi kaynaktan alınacağına (hayatta kalma kuralı) karar vermeyi ve ana veri yönetimi (MDM) mimarilerini anlatır."
course: ea
category: veri-yonetimi
tags: [ana-veri, mdm, veri-kalitesi, musteri]
roles: [it-yoneticisi]
level: ileri
source_lessons: [EA-8.3]
reading_minutes: 3
key_points:
  - "Mükerrer kayıtlar, tam eşleşme yerine benzerlik puanı ve birden çok alanla bulunur."
  - "Ad benzerliği tek başına yetmez; vergi no, telefon ve konum ile desteklenmelidir."
  - "Hayatta kalma kuralı, birleşen kayıtlarda her alanın hangi kaynaktan alınacağını belirler."
  - "MDM mimarileri: kayıt defteri, konsolidasyon, birlikte yaşama ve merkezi."
  - "Eşik değerleri iki banda ayrılır: otomatik birleştir ve insan incelemesine gönder."
glossary_terms: [mdm, ana-veri]
related: [kb-ea-8-1-master-data-governance, kb-ea-8-2-data-quality-field, kb-ea-10-1-why-integration-is-hard, kb-ea-18-6-data-migration-opening-balances]
sources:
  - title: "Master Data Management"
    authors: "Loshin, D."
    year: 2009
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

"Yıldız Market", "Yildiz Mrkt." ve "Yıldız Mkt" aynı dükkân mı? Saha uygulaması ile ERP birleştirilirken ya da yeni sisteme geçerken bu soruya binlerce kez cevap vermeniz gerekir. Bu kart, mükerrer kayıtları sistematik bulmayı ve **ana veri yönetimi** (MDM, *master data management*) mimarisini seçmeyi anlatır.

## Temel fikir

**Eşleştirme** üç adımdır:

1. **Standartlaştırma:** Büyük–küçük harf, Türkçe karakterler, "Ltd.", "Şti.", "Mkt." gibi kısaltmalar tek biçime getirilir.
2. **Karşılaştırma:** Ad, adres, vergi no, telefon ve konum için benzerlik puanı hesaplanır.
3. **Karar:** Yüksek puanlı çiftler otomatik birleşir, orta puanlılar bir insanın incelemesine gider, düşük puanlılar ayrı kalır.

Birleşen kayıtta hangi alanın kalacağına **hayatta kalma kuralı** (*survivorship*) karar verir. Örneğin vergi no ERP'den, telefon en son güncellenen kaynaktan, konum saha uygulamasından.

Loshin'in de anlattığı dört MDM mimarisi:

| Mimari | Nasıl çalışır |
|---|---|
| Kayıt defteri (*registry*) | Kayıtlar kaynaklarda kalır, merkez yalnızca eşleşme anahtarlarını tutar |
| Konsolidasyon | Kaynaklardan toplanıp temizlenmiş tek görünüm raporlama için oluşturulur |
| Birlikte yaşama (*coexistence*) | Temiz kayıt merkezde tutulur ve kaynaklara geri yazılır |
| Merkezi | Kayıt yalnızca merkezde açılır, tüm sistemler oradan alır |

Orta ölçekli bir dağıtım firmasında genellikle ERP'nin kendisi merkez olur ve ayrı bir MDM ürünü gerekmez.

### Mükerrer kayıtların önlenmesi

Mükerrer kayıtları sonradan temizlemek, oluşmalarını önlemekten çok daha pahalıdır. Kalıcı çözüm için kaynakta alınacak önlemler şunlardır:

- **Kayıt açarken arama:** Yeni müşteri açılmadan önce sistem, benzer ad, vergi numarası, telefon ve konumla otomatik arama yapmalı ve olası eşleşmeleri kullanıcıya göstermelidir.
- **Zorunlu ve doğrulanan alanlar:** Vergi numarası veya kimlik numarası gibi tekil anahtarlar biçim kontrolünden geçmelidir. Telefon ve adres alanları standart biçimde girilmelidir.
- **Tek kayıt açma yetkisi:** Müşteri kaydını kimlerin açabileceği sınırlandırılmalıdır. Saha temsilcisinin açtığı yeni nokta kaydı, ana veri ekibinin onayından geçtikten sonra aktif hâle gelebilir.
- **Kaynaklar arası anahtar:** Satış uygulaması, ERP ve B2B portal aynı müşteri için aynı anahtarı kullanmalıdır.

**Birleştirmenin etkileri.** İki kaydı birleştirmek, geçmiş siparişler, açık bakiyeler, fiyat anlaşmaları ve prim hesapları gibi bağlı verileri de etkiler. Birleştirme öncesinde hangi kaydın ana kayıt olarak kalacağı, diğerinin nasıl pasife alınacağı ve geçmiş işlemlerin nasıl ilişkilendirileceği belirlenmelidir. Birleştirme işlemlerinin kaydı tutulmalı, gerektiğinde geri alınabilmelidir.

**Sürekli ölçüm.** Olası mükerrer kayıt sayısı düzenli olarak raporlanmalı ve veri kalitesi göstergeleri arasında izlenmelidir. Loshin'in vurguladığı gibi, ana veri yönetimi tek seferlik bir temizlik değil, sahipleri belli kalıcı bir süreçtir.

## Bir örnek

> **Örnek (temsili rakamlar):** İsimler uydurmadır; benzerlikler `scripts/cards_numbers_ea_b2.py` içinde Python `difflib` ile, Türkçe karakterler sadeleştirilerek hesaplanmıştır.

| Kayıt A | Kayıt B | Ad benzerliği |
|---|---|---|
| Yıldız Market | Yildiz Mrkt. | 0,88 |
| Öz Kardeşler Gıda | Oz Kardesler Gida Ltd | 0,89 |
| Deniz Bakkal | Deniz Bakkaliye | 0,89 |
| Yıldız Market | Yıldız Büfe | 0,67 |

İlk üç çift adla yüksek puan alıyor. Ancak "Deniz Bakkal" ile "Deniz Bakkaliye" farklı mahallelerde ve vergi numaraları farklı; bu çift insan incelemesinde ayrı tutuluyor. Kural: ad benzerliği 0,85 üstü ve vergi no ya da telefon eşleşiyorsa otomatik birleştir; yalnızca ad benzerliği yüksekse incelemeye gönder.

## Sık yapılan hatalar

- Yalnızca ad benzerliğine göre otomatik birleştirmek.
- Birleştirilen kayıtların geçmiş işlemlerini yeni kayda bağlamamak.
- Hayatta kalma kuralını yazmadan birleştirmek; doğru telefonu kaybetmek.
- Kaynakta yeni mükerrer oluşumunu engellemeden temizlik yapmak.

## Pratikte nasıl uygulanır?

- [ ] Standartlaştırma kurallarını yazın (kısaltmalar, Türkçe karakterler).
- [ ] En az iki alanın eşleşmesini otomatik birleştirme şartı yapın.
- [ ] Orta bant için bir inceleme listesi ve sorumlu belirleyin.
- [ ] Alan bazında hayatta kalma kurallarını yazın.
- [ ] Yeni kart açılışında mükerrer uyarısı verecek kontrolü sisteme ekletin.

## Daha fazlası

- Loshin, *Master Data Management* (kitap; doğrulanmadı).
