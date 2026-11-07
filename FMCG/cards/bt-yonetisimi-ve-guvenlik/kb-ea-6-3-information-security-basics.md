---
id: kb-ea-6-3-information-security-basics
title: "Bilgi güvenliği yönetimi: Risk temelli yaklaşım ve temel kontroller"
summary: "Bilgi güvenliğini teknik araçlar listesi yerine risk temelli bir yönetim sistemi olarak ele almayı; ISO/IEC 27001 mantığıyla varlık, tehdit, olasılık ve etki üzerinden önceliklendirmeyi ve bir dağıtım firması için ilk kontrolleri anlatır."
course: ea
category: bt-yonetisimi-ve-guvenlik
tags: [guvenlik, risk, bt-yonetisimi, yedekleme]
roles: [it-yoneticisi]
level: orta
source_lessons: [EA-6.3]
reading_minutes: 3
key_points:
  - "Bilgi güvenliği gizlilik, bütünlük ve erişilebilirliği korumaktır."
  - "ISO/IEC 27001, güvenliği risk değerlendirmesi ve sürekli iyileştirmeyle yürüyen bir yönetim sistemi olarak tanımlar."
  - "Risk puanı olasılık ve etkinin birlikte değerlendirilmesiyle bulunur; önce en yüksek riskler ele alınır."
  - "Her risk için dört seçenek vardır: azaltmak, kabul etmek, aktarmak (ör. sigorta), kaçınmak."
  - "Çoğu firmada en hızlı getiriyi kimlik yönetimi, yedekleme ve güncelleme disiplini sağlar."
glossary_terms: [bilgi-guvenligi]
related: [kb-ea-14-4-backup-disaster-recovery, kb-ea-15-2-user-roles-permissions, kb-ea-15-5-kvkk-basics, kb-ea-6-4-internal-controls-sod]
sources:
  - title: "ISO/IEC 27001:2022 Information security management systems — Requirements"
    authors: "ISO/IEC"
    year: 2022
    type: standard
    verified: false
    note: "iso.org kutudan erişilemedi."
  - title: "NIST Cybersecurity Framework"
    authors: "NIST"
    year: 2024
    type: web
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

Fidye yazılımı, kaybolan bir saha tableti ya da işten ayrılan bir çalışanın hâlâ açık olan ERP hesabı, bir dağıtım firmasında günlerce iş kaybına yol açabilir. Bu kart, **bilgi güvenliğini** (*information security*) bir araç alışverişi olarak değil, risk temelli bir yönetim işi olarak ele almanızı sağlar.

## Temel fikir

Bilgi güvenliğinin üç hedefi vardır: **gizlilik** (bilgiyi yalnızca yetkili görür), **bütünlük** (bilgi doğru ve değiştirilmemiş kalır), **erişilebilirlik** (gerektiğinde ulaşılır).

ISO/IEC 27001, bunları bir **bilgi güvenliği yönetim sistemi** (BGYS, *ISMS*) ile yönetmeyi önerir. Döngü şöyledir:

1. Korunacak varlıkları listeleyin (ERP verisi, müşteri listesi, sunucular, saha cihazları).
2. Tehditleri ve zayıflıkları belirleyin.
3. Her risk için olasılık ve etkiyi puanlayın.
4. Risk işleme kararı verin: azalt, kabul et, aktar, kaçın.
5. Kontrolleri uygulayın, ölçün ve yılda en az bir kez gözden geçirin.

Standardın ekinde kontrol listesi bulunur; firma uygulanabilir olanları seçer ve gerekçesini yazar. NIST Siber Güvenlik Çerçevesi de benzer bir yapıyı ücretsiz erişilebilir biçimde sunar.

### Önceliklendirme: Nereden başlamalı?

Bilgi güvenliği geniş bir alandır ve kaynaklar sınırlıdır. Orta ölçekli bir dağıtım şirketinde, risk temelli bir başlangıç için şu öncelikler önerilir:

- **Varlık envanteri:** Hangi sistemler, cihazlar ve veriler var? Kimin sorumluluğunda? Bilinmeyen bir varlık korunamaz. Saha ekiplerinin mobil cihazları da envanterde yer almalıdır.
- **Kimlik ve erişim:** Çok faktörlü kimlik doğrulama, özellikle e-posta, uzaktan erişim ve yönetici hesapları için ilk uygulanması gereken kontrollerdendir. Ayrılan çalışanların erişimlerinin zamanında kapatılması da kritik önemdedir.
- **Yedekleme ve geri yükleme:** Yedekler düzenli alınmalı, ana sistemden ayrı tutulmalı ve geri yükleme düzenli olarak test edilmelidir. Fidye yazılımı saldırılarında en etkili savunma, test edilmiş yedeklerdir.
- **Güncelleme yönetimi:** İşletim sistemleri, sunucular ve uygulamalar için güvenlik güncellemeleri düzenli uygulanmalıdır.
- **Farkındalık eğitimi:** Oltalama e-postaları, sahte ödeme talepleri ve banka hesap değişikliği dolandırıcılıkları hakkında çalışanlar düzenli olarak bilgilendirilmelidir.

**Olay müdahale planı.** Bir güvenlik olayı yaşandığında kimin aranacağı, hangi sistemlerin izole edileceği, kimlerin bilgilendirileceği ve hangi yasal bildirimlerin yapılacağı önceden yazılı olmalıdır. Kişisel veri ihlallerinde bildirim süreleri kısa olabilir; bu nedenle hukuk danışmanıyla birlikte hazırlık yapılmalıdır.

**Tedarikçi riski.** Bulut hizmetleri, entegratörler ve yazılım tedarikçileri de güvenlik zincirinin parçasıdır. Sözleşmelerde güvenlik yükümlülükleri ve olay bildirimi yer almalıdır. NIST çerçevesi ve ISO/IEC 27001, bu kontrollerin sistematik biçimde ele alınması için yol gösterir.

## Bir örnek

> **Örnek (temsili rakamlar):** Puanlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b2.py` ile yapılmıştır (1–5 ölçeği, puan = olasılık × etki).

| Risk | Olasılık | Etki | Puan |
|---|---|---|---|
| Fidye yazılımı ile sunucuların şifrelenmesi | 3 | 5 | 15 |
| Ayrılan çalışanın hesabının açık kalması | 4 | 3 | 12 |
| Yedeklerin geri yüklenememesi | 2 | 5 | 10 |
| Saha tabletinin kaybolması | 4 | 2 | 8 |

Firma ilk üç riske öncelik veriyor: Dışarıdan erişimde çok faktörlü kimlik doğrulama ve güncel yamalar, İK'dan gelen işten çıkış bildirimiyle aynı gün hesap kapatma, ayda bir yedekten deneme geri yüklemesi. Tablet riski için cihazlara uzaktan silme özelliği açılıyor.

## Sık yapılan hatalar

- Güvenliği yalnızca antivirüs ve güvenlik duvarı satın almak sanmak.
- Risk değerlendirmesini bir kez yapıp güncellememek.
- Yedek alıp geri yüklemeyi hiç denememek.
- Ortak kullanıcı hesapları ("depo1") kullanmak.
- Güvenliği yalnızca BT'nin sorumluluğu görmek.

## Pratikte nasıl uygulanır?

- [ ] Kritik bilgi varlıklarınızı ve sahiplerini tek sayfada listeleyin.
- [ ] En önemli 10 riski olasılık ve etkiyle puanlayın; ilk üçü için sorumlu ve tarih belirleyin.
- [ ] Uzaktan erişen tüm hesaplarda çok faktörlü kimlik doğrulamayı zorunlu yapın.
- [ ] İşten çıkışta hesap kapatmayı İK süreci ile bağlayın.
- [ ] Çalışanlara yılda en az bir kez kısa güvenlik farkındalık eğitimi verin.

## Daha fazlası

- ISO/IEC 27001:2022 (standart; erişilemedi, doğrulanmadı).
- NIST Cybersecurity Framework. https://www.nist.gov/cyberframework
