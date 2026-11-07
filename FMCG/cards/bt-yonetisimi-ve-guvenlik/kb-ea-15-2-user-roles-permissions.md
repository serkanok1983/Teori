---
id: kb-ea-15-2-user-roles-permissions
title: "Kullanıcı rolleri ve yetkiler: Rol tabanlı erişim, en az yetki"
summary: "Yetkileri kişilere tek tek değil rollere vermeyi (RBAC), en az yetki ilkesini, ayrılan çalışanın erişiminin kapatılmasını ve periyodik yetki gözden geçirmesini anlatır."
course: ea
category: bt-yonetisimi-ve-guvenlik
tags: [yetki, rbac, guvenlik, erp, denetim]
roles: [finans-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-15.2, EA-15.4]
reading_minutes: 3
key_points:
  - "Rol tabanlı erişimde yetki kişiye değil role verilir; kişiye rol atanır."
  - "En az yetki ilkesi: Herkes yalnızca işini yapmaya yetecek kadar erişime sahip olmalıdır."
  - "Ayrılan ya da görev değiştiren çalışanın yetkisi aynı gün güncellenmelidir."
  - "Yetkiler, iş birimi yöneticisi tarafından en az yılda bir gözden geçirilmelidir."
  - "Rol tasarımı görevler ayrılığı ve değiştirilemez iz kayıtlarıyla birlikte yapılmalıdır."
glossary_terms: [rbac, en-az-yetki, gorevler-ayriligi]
related: [kb-ea-6-4-internal-controls-sod, kb-ea-15-5-kvkk-basics, kb-ea-14-4-backup-disaster-recovery, kb-ea-6-3-information-security-basics]
sources:
  - title: "Role-based access control models"
    authors: "Sandhu, R. S.; Coyne, E. J.; Feinstein, H. L.; Youman, C. E."
    year: 1996
    type: article
    doi: "10.1109/2.485845"
    url: "https://doi.org/10.1109/2.485845"
    verified: true
    checked_on: 2026-10-28
  - title: "NIST Cybersecurity Framework 2.0"
    authors: "NIST"
    year: 2024
    type: standard
    url: "https://www.nist.gov/cyberframework"
    verified: true
    checked_on: 2026-10-28
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Birçok firmada ERP yetkileri "kim ne istediyse verildi" mantığıyla birikir. Bir denetimde ya da veri sızıntısında ilk sorulan soru, kimin neye neden eriştiğidir. Bu kart yetki yönetimini sade bir düzene oturtur.

## Temel fikir

Sandhu ve arkadaşlarının (1996) tanımladığı **rol tabanlı erişim denetimi** (RBAC, *role-based access control*) üç katmandan oluşur: yetkiler (ekran, işlem, veri), roller (ör. "Satış temsilcisi", "Tahsilat sorumlusu") ve kullanıcılar. Yetki role verilir, kullanıcıya rol atanır. Biri işe girdiğinde ya da görev değiştirdiğinde tek tek yetki değil rol değişir.

Destekleyici ilkeler:

- **En az yetki:** Herkes işini yapacak kadar yetkiye sahip olur. "Her şeyi görsün, belki lazım olur" yaklaşımı riski büyütür.
- **Görevler ayrılığı:** Kritik işlemlerin adımları (ör. tedarikçi tanımlama ve ödeme onayı) aynı rolde birleşmemelidir.
- **Yaşam döngüsü:** İşe giriş, görev değişikliği ve ayrılış süreçleri İK ile bağlantılı olmalıdır. Ayrılan çalışanın hesabı aynı gün kapatılır.
- **Periyodik gözden geçirme:** BT değil, iş birimi yöneticisi "bu kişinin bu yetkisi hâlâ gerekli mi" sorusunu yanıtlar.
- **İz kaydı (log):** Kim, ne zaman, hangi kaydı değiştirdi bilgisi silinemez biçimde tutulur; yasal saklama süreleri mali müşavirle teyit edilir.
- **Ayrıcalıklı hesaplar:** Yönetici hesapları az sayıda, kayıt altında ve çok faktörlü doğrulamayla kullanılır.

### Rol tasarımını sürdürülebilir kılmak

Rol tabanlı erişim, başlangıçta düzenli tasarlansa bile zamanla karmaşık hâle gelebilir. Sürdürülebilir bir rol yapısı için şu ilkeler önerilir:

- **İş rollerinden başlayın:** Roller, sistem ekranları yerine iş görevleri üzerinden tanımlanmalıdır: sipariş girişi, fatura onayı, tahsilat kaydı gibi. Bir çalışanın yetkileri, sahip olduğu iş rollerinin birleşiminden oluşur.
- **Rol sayısını kontrol edin:** Her kullanıcı için özel rol açmak, rol tabanlı yaklaşımın amacını ortadan kaldırır. Yeni rol açma talepleri gerekçelendirilmeli ve onaydan geçmelidir.
- **Çakışma kontrolü:** Görevler ayrılığı ilkesine aykırı yetki birleşimleri bir kural listesinde tanımlanmalı ve yeni yetki verilirken otomatik olarak kontrol edilmelidir.
- **Geçici yetkiler:** İzin veya yoğun dönemlerde verilen geçici yetkilerin bitiş tarihi olmalı ve süre dolduğunda otomatik olarak kaldırılmalıdır.
- **Rol sahipleri:** Her rolün içeriğinden sorumlu bir iş sahibi olmalıdır. Rol sahipleri, periyodik gözden geçirmelerde rol içeriğini ve rolü taşıyan kullanıcıları onaylar.

**Gözden geçirmenin kalitesi.** Periyodik yetki gözden geçirmelerinde yöneticilerin listeyi incelemeden onaylaması sık görülen bir sorundur. Listeler anlaşılır iş diliyle hazırlanmalı ve özellikle kritik yetkiler vurgulanmalıdır.

**Teknik hesaplar.** Entegrasyon ve robot hesapları da kullanıcı gibi yetkilendirilmeli ve gözden geçirmeye dahil edilmelidir. NIST'in yaklaşımı, bu tür hesapların da en az yetki ilkesine tabi olmasını önerir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b3.py` ile yapılmıştır.

Bir üreticide 120 ERP kullanıcısı ve sistemde 40 farklı yetki var. Kişi bazlı yönetimde gözden geçirilmesi gereken olası atama sayısı 120 × 40 = **4.800**.

Firma 9 rol tanımlıyor. Gözden geçirilecek nesne sayısı, rollerin yetki tanımı (9 × 40 = **360**) ve **120** kullanıcı–rol atamasına iniyor. Yıllık gözden geçirmede her bölüm müdürü yalnızca kendi ekibinin rol listesini onaylıyor. İlk turda, başka bölüme geçmiş üç çalışanın eski rollerinin de durduğu ortaya çıkıyor.

## Sık yapılan hatalar

- Yeni çalışana "benzer birinin yetkilerini kopyala" diyerek fazla yetki taşımak.
- Ayrılan çalışanın hesabını haftalar sonra kapatmak.
- Ortak kullanıcı adları ("depo1") kullanmak; kimin ne yaptığı izlenemez.
- Gözden geçirmeyi BT'ye bırakmak; BT işin gerektirdiği yetkiyi bilemez.

## Pratikte nasıl uygulanır?

- [ ] Mevcut kullanıcı–yetki listesini dışa aktarın ve benzer profilleri gruplayarak rolleri çıkarın.
- [ ] Her rol için sahibini ve görevler ayrılığı kurallarını yazın.
- [ ] İK'nın giriş, görev değişikliği ve ayrılış bildirimini BT'ye otomatik iletmesini sağlayın.
- [ ] Yetkileri yılda en az bir kez iş birimi yöneticilerine onaylatın.

## Daha fazlası

- Sandhu ve ark. (1996), *IEEE Computer*. https://doi.org/10.1109/2.485845
- NIST Siber Güvenlik Çerçevesi: https://www.nist.gov/cyberframework
