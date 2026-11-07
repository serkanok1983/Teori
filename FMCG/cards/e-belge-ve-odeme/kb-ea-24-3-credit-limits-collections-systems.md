---
id: kb-ea-24-3-credit-limits-collections-systems
title: "Kredi limiti ve tahsilat sistemleri: Limit kontrolü, hatırlatma ve DBS"
summary: "Müşteri kredi limitlerinin belirlenmesini, ERP'de sipariş anında risk kontrolünü, vadesi geçen alacaklar için kademeli hatırlatma sürecini ve doğrudan borçlandırma sistemi (DBS) ile tahsilatın güvence altına alınmasını anlatır."
course: ea
category: e-belge-ve-odeme
tags: [kredi-limiti, tahsilat, dbs, risk]
roles: [bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: orta
source_lessons: [EA-24.3]
reading_minutes: 3
key_points:
  - "Kredi riski; açık alacak, açık siparişler ve yeni siparişin toplamıdır."
  - "ERP limit aşan siparişi otomatik olarak bloke edip onaya gönderebilir."
  - "Kademeli hatırlatma süreci vadesi geçen alacakları sistematik takip eder."
  - "DBS, bayinin bankası üzerinden tanımlı limit dahilinde ödemeyi güvenceye alır."
  - "Limitler müşteri ödeme davranışına göre düzenli güncellenmelidir."
glossary_terms: [kredi-limiti, dbs, kademeli-hatirlatma]
related: [kb-fmcg-7-3-credit-collections-dso, kb-eco-38-3-distributor-credit-risk-dbs, kb-ea-20-2-order-to-cash, kb-ea-38-3-findeks-credit-bureau]
sources:
  - title: "Integrated Business Processes with ERP Systems"
    authors: "Magal, S. R.; Word, J."
    year: 2011
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

Satış ekibi hacim büyütmek ister, finans ekibi tahsil edilemeyecek alacaktan korkar. Bu kart, kredi riskini sistemle yönetmenin temel yapısını anlatır ve iki ekibin aynı kuralla çalışmasını sağlar.

## Temel fikir

**Kredi limiti.** Her müşteriye ödeme geçmişi, teminatı ve hacmine göre bir limit verilir. Limit belirlemede şirket içi ödeme geçmişi ve kredi bürosu bilgileri kullanılabilir.

**Risk hesabı.** ERP'de sipariş anında şu toplam kontrol edilir:

- Açık alacak (faturalanmış ama ödenmemiş),
- Açık siparişler (onaylanmış ama faturalanmamış),
- Yeni siparişin tutarı.

Toplam limiti aşarsa sipariş **bloke** edilir ve yetkili kişinin onayına düşer. Vadesi belirli bir günü geçen alacak varsa sipariş limitten bağımsız olarak da bloke edilebilir.

**Kademeli hatırlatma.** Vadesi geçen alacaklar için sistem adım adım hatırlatma yapar: Vade günü bilgilendirme, birkaç gün sonra e-posta veya SMS, ardından satış temsilcisinin ziyareti, en son sevkiyat durdurma. Her adım ERP'de kayıt altına alınır.

**DBS (doğrudan borçlandırma sistemi).** Bayinin bankası, bayiye tanımladığı limit dahilinde tedarikçiye vadesinde ödeme yapmayı taahhüt eder. Tedarikçi faturayı bankaya iletir; vade günü ödeme otomatik yapılır. DBS limiti ERP'de müşteri kartında ayrıca izlenmelidir.

### Kredi ve tahsilat politikasını sisteme aktarmak

Kredi limiti kontrolü, ancak yazılı bir politikaya dayandığında tutarlı çalışır. Politikanın sistemde karşılık bulması gereken başlıca unsurlar şunlardır:

- **Limit belirleme kuralları:** Yeni müşteri için başlangıç limiti, limit artışı için gereken belgeler ve onay seviyeleri tanımlanmalıdır.
- **Blokaj davranışı:** Limit aşıldığında sipariş tamamen mi durdurulacak, onaya mı gönderilecek, yoksa yalnızca uyarı mı verilecek? Vadesi geçmiş borç olduğunda limit içinde kalınsa bile blokaj uygulanacak mı?
- **Geçici limit:** Kampanya veya mevsimsel yoğunluk dönemlerinde verilen geçici artışların bitiş tarihi sistemde tanımlanmalıdır.
- **Teminatlar:** Teminat mektubu, ipotek veya DBS limiti gibi güvencelerin tutarı ve vade tarihi kayıt altında olmalı; süresi dolmak üzere olan teminatlar için uyarı üretilmelidir.

**Tahsilat ekibinin iş listesi.** Sistem, tahsilat ekibine her gün öncelikli bir liste sunmalıdır: vadesi yaklaşan büyük bakiyeler, vadesi geçmiş borçlar, söz verilip ödenmeyen tutarlar ve itiraz edilen faturalar. Her görüşmenin sonucu ve verilen ödeme sözü kayda geçirilmelidir.

**Satış ekibinin rolü.** Saha temsilcileri, müşterinin bakiyesini ve vadesi geçmiş borçlarını ziyaret sırasında görebilmelidir. Tahsilatın bir kısmının temsilci hedeflerine dahil edilmesi, satış ile tahsilat arasındaki dengeyi korur.

**İtirazların yönetimi.** Ödenmeyen faturaların önemli bir kısmı, fiyat farkı, eksik teslimat veya promosyon mahsuplaşması gibi itirazlardan kaynaklanır. İtirazlar ayrı bir kayıt olarak izlenmeli ve sorumlu birime yönlendirilmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b5.py` ile yapılmıştır.

Bir bayinin kredi limiti 500.000 TL. Açık alacağı 420.000 TL, onaylı ama faturalanmamış siparişleri 60.000 TL. Satış temsilcisi 50.000 TL'lik yeni sipariş giriyor.

- Toplam risk: **530.000,00 TL**
- Limit aşımı: **30.000,00 TL**
- Yeni sipariş için kullanılabilir limit: **20.000,00 TL**

ERP siparişi bloke ediyor. Finans müdürü, bayinin vadesi gelmiş bir ödemesini bu hafta yapacağını teyit edip siparişi onaylıyor; onay gerekçesi sisteme not olarak düşülüyor.

## Sık yapılan hatalar

- Açık siparişleri risk hesabına katmamak.
- Bloke edilen siparişleri gerekçesiz toplu onaylamak.
- Limitleri yıllarca güncellememek.
- DBS limitini ERP'de izlememek.

## Pratikte nasıl uygulanır?

- [ ] Limit belirleme kurallarını yazılı hale getirin.
- [ ] ERP'de risk hesabına açık siparişleri ekleyin.
- [ ] Kademeli hatırlatma adımlarını ve sorumlularını tanımlayın.
- [ ] Limit aşım onaylarını aylık olarak raporlayın.

## Daha fazlası

- Magal ve Word, *Integrated Business Processes with ERP Systems* (kitap; doğrulanmadı).
