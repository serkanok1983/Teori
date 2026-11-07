---
id: kb-ea-26-3-offline-mode-for-managers
title: "Çevrimdışı çalışan mobil uygulamalar: Yöneticiler için senkronizasyon ve çakışma"
summary: "Saha uygulamalarının internet olmadan nasıl çalıştığını, cihazdaki yerel veriyi, senkronizasyonu, aynı kaydın iki yerde değişmesiyle oluşan çakışmaların nasıl çözüldüğünü ve kaybolan cihazların güvenliğini yönetici gözüyle anlatır."
course: ea
category: saha-satis-ve-dms
tags: [mobil, cevrimdisi, senkronizasyon, cakisma, cihaz-guvenligi]
roles: [it-yoneticisi]
level: orta
source_lessons: [EA-26.3, EA-26.4]
reading_minutes: 2
key_points:
  - "Çevrimdışı öncelikli uygulama, işi cihazdaki yerel veriyle yapar ve bağlantı gelince senkronize eder."
  - "Aynı kayıt iki yerde değişirse çakışma oluşur; çözüm kuralı önceden belirlenmelidir."
  - "Sipariş gibi kayıtlar hiç kaybolmamalı; kuyrukta bekleyip sırayla gönderilmelidir."
  - "Fiyat ve limit gibi kritik bilgiler sunucuda kesinleşmelidir."
  - "Kaybolan cihazdaki veriler uzaktan silinebilmeli ve şifrelenmiş olmalıdır."
glossary_terms: [cevrimdisi-oncelikli, senkronizasyon, veri-cakismasi]
related: [kb-ea-26-1-retail-execution-sfa, kb-ea-26-2-field-data-outlet-visit, kb-ea-26-5-van-sales-presales, kb-ea-15-2-user-roles-permissions]
sources:
  - title: "Managing update conflicts in Bayou, a weakly connected replicated storage system"
    authors: "Terry, D.; Theimer, M.; Petersen, K.; Demers, A."
    year: 1995
    type: article
    doi: "10.1145/224056.224070"
    url: "https://doi.org/10.1145/224056.224070"
    verified: true
    checked_on: 2026-10-28
  - title: "Local-first software: you own your data, in spite of the cloud"
    authors: "Kleppmann, M.; Wiggins, A.; van Hardenberg, P.; McGranaghan, M."
    year: 2019
    type: article
    doi: "10.1145/3359591.3359737"
    url: "https://doi.org/10.1145/3359591.3359737"
    verified: true
    checked_on: 2026-10-28
  - title: "Conflict-Free Replicated Data Types"
    authors: "Shapiro, M.; Preguiça, N.; Baquero, C.; Zawirski, M."
    year: 2011
    type: article
    doi: "10.1007/978-3-642-24550-3_29"
    url: "https://doi.org/10.1007/978-3-642-24550-3_29"
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

Saha temsilcisi bir köy bakkalında, bodrum kattaki bir markette ya da çekmeyen bir bölgede sipariş alır. Uygulama "bağlantı yok" diye durursa iş durur. Bu kart, çevrimdışı çalışmanın ne anlama geldiğini ve yöneticilerin hangi kararları vermesi gerektiğini anlatır.

## Temel fikir

**Çevrimdışı öncelikli** (*offline-first*) bir uygulama, işini cihazdaki **yerel veriyle** yapar. Nokta listesi, ürünler, fiyatlar ve açık bakiyeler cihaza önceden indirilir. Temsilcinin girdiği siparişler cihazda bir **kuyrukta** bekler ve bağlantı geldiğinde sunucuya gönderilir.

**Senkronizasyon** iki yönlüdür: Cihazdaki yeni kayıtlar sunucuya, sunucudaki güncellemeler (yeni fiyat, yeni kampanya) cihaza gider. Yalnızca değişen kayıtların gönderilmesi veriyi ve süreyi azaltır.

**Çakışma.** Aynı kayıt iki yerde değişirse ne olur? Örneğin temsilci nokta adresini sahada güncellerken merkez de aynı noktanın kanalını değiştirmiş olabilir. Terry ve arkadaşlarının (1995) Bayou çalışması, bağlantısı kesik cihazlarda bu tür çakışmaların uygulamaya özgü kurallarla çözülmesini anlatır. Kleppmann ve arkadaşları (2019) ve Shapiro ve arkadaşları (2011), çakışmaları otomatik birleştiren veri yapılarını (CRDT) tartışır.

Yönetici açısından önemli kararlar:

- **Hangi bilgide sunucu son sözü söyler?** Fiyat, kredi limiti ve stok sunucuda kesinleşmelidir.
- **Hangi bilgide alan bazında birleştirme yapılır?** Örneğin adres ve telefon farklı alanlarsa ikisi de korunabilir.
- **Siparişler asla kaybolmamalı.** Çift gönderimi önlemek için her siparişin cihazda üretilen benzersiz bir numarası olmalıdır.

**Cihaz güvenliği.** Cihazdaki veri şifrelenmeli, cihaz kaybolursa uzaktan silinebilmeli ve kullanıcı yetkisi sunucudan kapatılabilmelidir.

### Yöneticinin test ederken sorması gerekenler

Çevrimdışı çalışma, kâğıt üzerinde değil sahada sınanmalıdır. Uygulamayı kabul etmeden önce şu senaryoların denenmesi önerilir:

- Temsilci bağlantısız bir bölgede gün boyu sipariş alıp akşam bağlandığında tüm siparişler eksiksiz ve tek kez merkeze ulaşıyor mu?
- Aynı müşterinin bilgisi hem merkezde hem cihazda değiştirildiğinde hangi değer kalıyor ve kullanıcıya bildiriliyor mu?
- Fiyat listesi güncellendiğinde, eski fiyatla alınmış çevrimdışı siparişler nasıl ele alınıyor?
- Cihaz kaybolduğunda üzerindeki veriler uzaktan silinebiliyor mu?

Bu senaryolar sonucunda hangi kuralın uygulandığı, iş birimleriyle birlikte yazılı olarak onaylanmalıdır. Terry ve arkadaşlarının çalışmasında da görüldüğü gibi, çakışma çözümü uygulamaya özgü kurallar gerektirir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b6.py` ile yapılmıştır.

Bir distribütörde ayda 10.000 senkronizasyon yapılıyor; 45'inde çakışma çıkıyor: oran **%0,45**. Çakışmaların çoğu nokta adres bilgisinde. Firma, adres alanlarında alan bazında birleştirme kuralı uyguluyor. Bir gün mobil operatör kesintisi nedeniyle **180** sipariş birkaç saat cihazlarda bekliyor; bağlantı geldiğinde hepsi kayıpsız ve çift kayıt olmadan aktarılıyor.

## Sık yapılan hatalar

- Uygulamanın yalnızca çevrimiçi çalıştığını sahaya çıktıktan sonra fark etmek.
- Çakışma kuralını yazılımcıya bırakıp iş tarafının karar vermemesi.
- Cihazda eski fiyatla alınan siparişin nasıl ele alınacağını belirlememek.
- Kaybolan cihazlar için süreç tanımlamamak.

## Pratikte nasıl uygulanır?

- [ ] Hangi işlemlerin çevrimdışı yapılabileceğini listeleyin.
- [ ] Her veri türü için çakışma kuralını iş tarafıyla belirleyin.
- [ ] Bekleyen sipariş kuyruğunu yöneticilerin görebileceği bir rapora bağlayın.
- [ ] Cihaz şifreleme ve uzaktan silme özelliğini zorunlu kılın.

## Daha fazlası

- Terry ve ark. (1995), Bayou. https://doi.org/10.1145/224056.224070
- Kleppmann ve ark. (2019), Local-first software. https://doi.org/10.1145/3359591.3359737
- Shapiro ve ark. (2011), CRDT. https://doi.org/10.1007/978-3-642-24550-3_29
