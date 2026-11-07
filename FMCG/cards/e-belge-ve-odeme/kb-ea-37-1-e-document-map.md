---
id: kb-ea-37-1-e-document-map
title: "Türkiye'de e-belge haritası: Hangi belge ne işe yarar?"
summary: "e-Fatura, e-Arşiv Fatura, e-İrsaliye, e-Defter, e-Serbest Meslek Makbuzu, e-Müstahsil Makbuzu ve e-Adisyon belgelerini iş akışındaki yerleriyle tanıtır; arka plandaki UBL-TR belge yapısını ve zorunluluk koşullarının nereden kontrol edileceğini anlatır."
course: ea
category: e-belge-ve-odeme
tags: [e-belge, e-fatura, e-arsiv, e-irsaliye, mevzuat, ubl]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru, it-yoneticisi]
level: temel
source_lessons: [EA-11.5, EA-37.1]
reading_minutes: 3
key_points:
  - "e-Fatura, sisteme kayıtlı iki mükellef arasında; e-Arşiv Fatura, kayıtlı olmayan alıcıya düzenlenir."
  - "e-İrsaliye malın taşınmasını, e-Defter yasal defterleri elektronik ortamda belgeler."
  - "Belgelerin arka planında UBL tabanlı ortak bir XML yapısı (UBL-TR) vardır."
  - "Kimin hangi belgeye geçmek zorunda olduğu ciro ve sektör koşullarına bağlıdır; bu koşullar değişir."
  - "Zorunluluk ve tarihleri her zaman güncel GİB duyurusundan ve mali müşavirinizden teyit edin."
glossary_terms: [e-fatura, e-irsaliye, e-arsiv-fatura, e-defter]
related: [kb-ea-37-2-e-fatura-scenarios, kb-ea-37-2-e-irsaliye-practice, kb-ea-37-3-e-document-integration-routes, kb-ea-37-4-e-defter-e-arsiv, kb-ea-20-2-order-to-cash]
sources:
  - title: "GİB e-Belge portalı"
    authors: "Gelir İdaresi Başkanlığı"
    year: 2026
    type: web
    url: "https://ebelge.gib.gov.tr/"
    verified: false
    note: "Kutudan erişilemedi (2026-10-28)."
  - title: "213 sayılı Vergi Usul Kanunu (mevzuat.gov.tr)"
    authors: "T.C. Cumhurbaşkanlığı Mevzuat Bilgi Sistemi"
    year: 2026
    type: law
    url: "https://www.mevzuat.gov.tr/"
    verified: true
    checked_on: 2026-10-28
    note: "Site erişimi doğrulandı; ilgili madde ve tebliğ metinleri ayrıca kontrol edilmeli."
  - title: "Universal Business Language Version 2.1"
    authors: "OASIS"
    year: 2013
    type: standard
    url: "https://docs.oasis-open.org/ubl/UBL-2.1.html"
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

Bir bayi gün içinde onlarca belge üretir: fatura, irsaliye, iade faturası, makbuz. Bunların büyük kısmı artık elektronik ve her birinin kuralı farklıdır. Bu kart, e-belge türlerini iş akışındaki yerleriyle tanıtır; ayrıntı için ilgili kartlara yönlendirir.

## Temel fikir

| Belge | Ne zaman kullanılır |
|---|---|
| **e-Fatura** | Satıcı ve alıcı, GİB e-Fatura sistemine kayıtlı mükellefse |
| **e-Arşiv Fatura** | Alıcı e-Fatura sistemine kayıtlı değilse (nihai tüketici veya kayıtsız firma) |
| **e-İrsaliye** | Malın taşınması sırasında kâğıt sevk irsaliyesi yerine |
| **e-Defter** | Yevmiye ve büyük defterin elektronik tutulması ve beratlarının alınması |
| **e-Serbest Meslek Makbuzu** | Serbest meslek erbabının düzenlediği makbuz |
| **e-Müstahsil Makbuzu** | Çiftçiden yapılan alımlarda |
| **e-Adisyon** | Yeme–içme işletmelerinde adisyon yerine |

Satış yaparken hangi faturanın kesileceği alıcıya bağlıdır: ERP, faturayı oluştururken alıcının e-Fatura sistemine kayıtlı olup olmadığını kontrol eder (kayıtlı kullanıcı listesi) ve buna göre e-Fatura ya da e-Arşiv Fatura üretir.

Belgelerin arka planında OASIS'in **UBL 2.1** standardından uyarlanan **UBL-TR** yapısı vardır. Bu, belgenin XML olarak hangi alanlardan oluşacağını tanımlar. Yönetici için önemli sonuç şudur: ERP'nizdeki müşteri, ürün, vergi ve birim verisi bu yapıya doğru eşlenmezse belge reddedilir.

Kimin hangi belgeye geçmek zorunda olduğu; ciro eşikleri, sektör ve faaliyet türüne göre Vergi Usul Kanunu'na dayanan tebliğlerle belirlenir ve sık güncellenir. Bu kart eşik ve tarih vermez; güncel koşullar GİB duyurularından teyit edilmelidir.

### Haritayı kendi şirketinize uyarlamak

Her şirket tüm e-belge türlerini kullanmaz. Hangi belgelerin sizin için geçerli olduğunu belirlemek için faaliyet türünüzü, ciro büyüklüğünüzü, müşteri profilinizi ve satış kanallarınızı mali müşavirinizle birlikte değerlendirin. Ardından her belge türü için ERP'deki karşılığını, kullanılan entegratörü, sorumlu birimi ve kontrol raporunu bir tabloda toplayın. Bu tablo, yeni bir süreç veya kanal açıldığında hangi belge yükümlülüğünün doğacağını görmeyi kolaylaştırır. Yükümlülük kapsamı ve geçiş tarihleri değişebildiği için tablonun düzenli aralıklarla resmî duyurulara göre güncellenmesi gerekir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b3.py` ile yapılmıştır.

Bir bayi ayda 1.800 satış faturası kesiyor. Bunların 1.250'si e-Fatura sistemine kayıtlı müşterilere (**%69,4**), 550'si kayıtlı olmayan bakkal ve büfelere (**%30,6**) gidiyor; bu 550 belge e-Arşiv Fatura olarak düzenleniyor. Her sevkiyata e-İrsaliye eşlik ediyor ve ay sonunda yasal defterler e-Defter olarak oluşturuluyor.

Bayi, bir müşterinin ay ortasında e-Fatura sistemine kaydolması durumunda ERP'nin kayıtlı kullanıcı listesini her fatura öncesinde kontrol etmesini sağlıyor; böylece yanlış belge türü düzenlenmiyor.

## Sık yapılan hatalar

- Alıcının kayıt durumunu bir kez kontrol edip güncellememek.
- e-Belgeyi yalnızca muhasebenin işi saymak; sevkiyat ve satış da belge üretir.
- Zorunluluk eşiklerini eski bir sunumdan ya da forumdan öğrenmek.
- Belge reddedildiğinde nedenini kaydetmeyip elle tekrar göndermek.

## Pratikte nasıl uygulanır?

- [ ] Firmanızın düzenlediği ve aldığı tüm belge türlerini listeleyin.
- [ ] Her belge için hangi sistemin ürettiğini ve kimin sorumlu olduğunu yazın.
- [ ] Mali müşavirinizle yükümlülüklerinizi ve geçiş tarihlerinizi yılda bir gözden geçirin.
- [ ] Reddedilen belgeleri nedenleriyle raporlayın.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın. GİB e-belge sayfalarına bu tarihte erişilemediği için belge türleri genel bilgi olarak verilmiştir; mali müşavir kontrolü gereklidir.

## Daha fazlası

- GİB e-Belge portalı: https://ebelge.gib.gov.tr/ (erişilemedi; doğrulanmadı).
- Mevzuat Bilgi Sistemi, 213 sayılı VUK: https://www.mevzuat.gov.tr/
- OASIS UBL 2.1: https://docs.oasis-open.org/ubl/UBL-2.1.html
