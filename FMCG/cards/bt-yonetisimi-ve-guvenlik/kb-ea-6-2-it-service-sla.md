---
id: kb-ea-6-2-it-service-sla
title: "BT hizmet yönetimi ve hizmet seviyesi anlaşması (SLA)"
summary: "BT hizmetlerini ITIL mantığıyla olay, problem ve değişiklik süreçlerine ayırmayı; tedarikçi ve iç BT ile hizmet seviyesi anlaşması yazarken erişilebilirlik yüzdesinin gerçekte kaç saat kesinti anlamına geldiğini anlatır."
course: ea
category: bt-yonetisimi-ve-guvenlik
tags: [bt-yonetisimi, sla, tedarikci, destek]
roles: [it-yoneticisi]
level: orta
source_lessons: [EA-6.2]
reading_minutes: 3
key_points:
  - "Olay yönetimi hizmeti hızla geri getirir; problem yönetimi tekrar eden olayın kök nedenini giderir."
  - "Değişiklik yönetimi, canlı sistemde yapılan her değişikliğin kontrollü yapılmasını sağlar."
  - "SLA'daki erişilebilirlik yüzdesini kesinti süresine çevirin: %99,5 ayda yaklaşık 3,6 saat demektir."
  - "Öncelik seviyeleri, iş etkisine göre tanımlanmalı ve her birine yanıt ve çözüm süresi verilmelidir."
  - "SLA ölçülmezse ve yaptırımı yoksa yalnızca bir niyet beyanıdır."
glossary_terms: [sla]
related: [kb-ea-6-1-it-governance-decision-rights, kb-ea-14-4-backup-disaster-recovery, kb-ea-19-3-working-with-it-partners, kb-ea-16-1-cloud-saas-basics]
sources:
  - title: "ITIL 4 (AXELOS)"
    authors: "AXELOS"
    year: 2019
    type: standard
    url: "https://www.axelos.com/certifications/itil-service-management"
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

ERP yavaşladığında, el terminali bağlanmadığında ya da e-fatura gönderilemediğinde kim, ne kadar sürede müdahale edecek? Bu kart, BT hizmetlerini düzenli yönetmenin temel süreçlerini ve tedarikçiyle yazılacak **hizmet seviyesi anlaşmasını** (SLA, *service level agreement*) anlatır.

## Temel fikir

ITIL, BT hizmet yönetimi için yaygın kullanılan bir iyi uygulama çerçevesidir. Yönetici için üç süreç yeterlidir:

- **Olay yönetimi** (*incident*): Kesintiyi en kısa sürede gidermek. Amaç kök neden değil, işin yeniden yürümesidir.
- **Problem yönetimi** (*problem*): Tekrar eden olayların kök nedenini bulup kalıcı çözmek.
- **Değişiklik yönetimi** (*change*): Canlı sistemde güncelleme, ayar ya da yeni sürüm değişikliğini test, onay ve geri dönüş planıyla yapmak.

SLA bu hizmetlerin ölçülebilir hedeflerini yazar:

- **Erişilebilirlik:** Sistemin çalışır olduğu sürenin oranı.
- **Öncelik seviyeleri:** Örneğin P1 (tüm satış durdu), P2 (bir bölge veya önemli bir işlev durdu), P3 (tek kullanıcı veya geçici çözümü olan sorun).
- **Yanıt ve çözüm süreleri:** Her öncelik için ayrı.
- **Ölçüm ve raporlama:** Kim ölçer, ne sıklıkla raporlanır.
- **Yaptırım:** Hedef tutmazsa hizmet bedelinden indirim gibi.

### SLA'yı anlamlı kılmak

Hizmet seviyesi anlaşmaları, çoğu zaman kâğıt üzerinde kalan ve kimsenin izlemediği belgelere dönüşür. SLA'nın gerçekten işe yaraması için şu ilkeler önerilir:

- **İş diliyle tanımlayın:** "Sunucu erişilebilirliği" yerine "sipariş alma hizmeti" gibi kullanıcıların anladığı hizmetler üzerinden tanımlama yapın. Kullanıcı için önemli olan, sunucunun çalışması değil, siparişin girilebilmesidir.
- **Kritik dönemleri belirleyin:** Ay sonu kapanışı, kampanya dönemleri ve sevkiyat saatleri gibi zamanlarda hizmet kesintisinin etkisi çok daha büyüktür. Bu dönemler için daha sıkı hedefler veya destek nöbeti tanımlanabilir.
- **Ölçümü otomatikleştirin:** Yanıt ve çözüm süreleri, talep sisteminden otomatik olarak raporlanmalıdır. Elle hazırlanan raporlar, hem zaman alır hem de güvenilirliği tartışmalıdır.
- **Düzenli gözden geçirin:** Aylık hizmet toplantılarında hedeflerin tutturulup tutturulmadığı, tekrarlayan sorunlar ve iyileştirme önerileri görüşülmelidir.
- **Kullanıcı memnuniyetini ekleyin:** Tüm süreler hedefte olsa bile kullanıcılar memnun olmayabilir. Kapanan taleplerden sonra kısa bir memnuniyet sorusu, bu farkı görünür kılar.

**İç ve dış SLA uyumu.** Şirket içi BT ekibinin kullanıcılara verdiği taahhütler, dış tedarikçilerden alınan hizmet seviyeleriyle uyumlu olmalıdır. Tedarikçi dört saatte çözüm taahhüt ediyorsa, iç ekibin iki saatte çözüm sözü vermesi gerçekçi değildir. ITIL yaklaşımı, bu zinciri hizmet seviyesi yönetimi süreci içinde ele alır.

## Bir örnek

> **Örnek (temsili rakamlar):** Hesaplar `scripts/cards_numbers_ea_b2.py` ile yapılmıştır; 30 günlük ay ve 7/24 hizmet varsayılmıştır.

| Erişilebilirlik | Ayda izin verilen kesinti |
|---|---|
| %99,50 | 216,0 dakika (3,6 saat) |
| %99,90 | 43,2 dakika |
| %99,95 | 21,6 dakika |

Bir bayi, bulut ERP teklifindeki "%99,5 erişilebilirlik" ifadesinin ayda 3,6 saatlik kesintiye izin verdiğini görüyor. Bu sürenin ay sonu fatura kesim gününe denk gelmesi ciddi sorun yaratacağı için tedarikçiden planlı bakımların ay sonu dışında yapılmasını ve P1 olaylarda 30 dakika içinde yanıt verilmesini sözleşmeye ekletiyor.

## Sık yapılan hatalar

- Erişilebilirlik yüzdesini süreye çevirmeden kabul etmek.
- Planlı bakımın erişilebilirlik hesabına dahil olup olmadığını sormamak.
- Yanıt süresini çözüm süresi sanmak; "30 dakikada yanıt" sorunun çözüldüğü anlamına gelmez.
- Tekrar eden olayları her seferinde yeniden çözüp kök nedeni aramamak.
- Canlı sistemde test edilmemiş değişiklik yapmak.

## Pratikte nasıl uygulanır?

- [ ] Kritik sistemlerinizi (ERP, e-belge, saha uygulaması) ve kabul edilebilir kesinti süresini yazın.
- [ ] Öncelik seviyelerini iş etkisiyle tanımlayın; her biri için yanıt ve çözüm süresi koyun.
- [ ] Tedarikçiden aylık SLA raporu isteyin ve kendi kayıtlarınızla karşılaştırın.
- [ ] Ayda bir, tekrar eden olayları gözden geçirip problem kaydı açın.
- [ ] Canlıda değişiklik için basit bir onay ve geri dönüş planı kuralı koyun.

## Daha fazlası

- AXELOS, ITIL 4. https://www.axelos.com/certifications/itil-service-management
