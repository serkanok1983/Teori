---
id: kb-ea-40-4-integrating-sfa-with-erp
title: "Satış uygulamasını müşterilerin ERP'sine bağlamak"
summary: "Bir satış ekibi uygulamasının Logo, Mikro veya SAP gibi farklı ERP'lere ve e-belge entegratörlerine bağlanmasında adaptör, alan eşleştirme ve mutabakat yaklaşımını, kurulum kontrol listesiyle anlatır."
course: ea
category: entegrasyon
tags: [entegrasyon, sfa, erp, adaptor, mutabakat]
roles: [it-yoneticisi]
level: ileri
source_lessons: [EA-40.4]
reading_minutes: 2
key_points:
  - "Farklı ERP'lere bağlanmak için ortak bir veri modeli ve ERP'ye özel adaptörler kullanılır."
  - "Müşteri, ürün, fiyat ve stok gibi ana veriler ERP'den, sipariş ve tahsilat ise satış uygulamasından akar."
  - "Alan eşleştirme tablosu her kurulumda yazılı hâle getirilmelidir."
  - "Günlük mutabakat raporu, kaybolan veya mükerrer kayıtları erken yakalar."
  - "E-belge akışında belgenin hangi sistemden üretileceği net olmalıdır."
glossary_terms: [adaptor, alan-eslestirme]
related: [kb-ea-37-3-e-document-integration-routes, kb-ea-21-3-erp-market-turkey, kb-ea-26-1-retail-execution-sfa, kb-ea-11-6-apis-for-managers]
sources:
  - title: "Enterprise Integration Patterns"
    authors: "Hohpe, G.; Woolf, B."
    year: 2003
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

Bir satış uygulaması sağlayıcısı için her yeni müşteri, farklı bir ERP ve farklı bir veri yapısı demektir. Entegrasyon iyi kurulmazsa siparişler kaybolur, fiyatlar tutmaz ve proje uzar. Bu kart, tekrarlanabilir bir entegrasyon yaklaşımı ve kurulum kontrol listesi sunar.

## Temel fikir

**Mimari:** Satış uygulaması tek bir ortak veri modeli kullanır. Her ERP türü için bir **adaptör**, bu ortak modeli ERP'nin yapısına çevirir.

**Veri akışı:**

- **ERP → satış uygulaması:** Müşteri, ürün, fiyat listesi, iskonto, stok, açık bakiye.
- **Satış uygulaması → ERP:** Sipariş, tahsilat, iade talebi, ziyaret bilgisi.

**Alan eşleştirme:** Her kurulumda hangi alanın hangi alana karşılık geldiği, birim dönüşümleri ve kod listeleri bir tabloda belgelenir.

**E-belge:** Fatura ve irsaliyenin genellikle ERP tarafından üretilip entegratöre gönderilmesi tercih edilir; satış uygulaması belge durumunu yalnızca okur. Aksi tasarımda belge mükerrerliği riski doğar.

**Mutabakat:** Her gün iki sistem arasındaki sipariş sayısı ve tutarı karşılaştırılır; fark varsa uyarı üretilir.

### Entegrasyon desenleri ve hata yönetimi

Hohpe ve Woolf'un kurumsal entegrasyon desenleri, bu tür bağlantılar için ortak bir dil sunar. Satış uygulaması ile ERP arasında en sık kullanılan yaklaşımlar şunlardır:

- **Mesaj kuyruğu:** Sipariş, satış uygulamasından bir kuyruğa bırakılır; adaptör kuyruğu okuyarak ERP'ye aktarır. ERP geçici olarak erişilemez olsa bile sipariş kaybolmaz, bağlantı geri geldiğinde işlenir.
- **Toplu aktarım:** Fiyat listesi ve ürün kataloğu gibi sık değişmeyen veriler, belirli aralıklarla toplu olarak aktarılabilir. Bu yöntem basittir ancak verinin ne zaman güncellendiğini kullanıcıya göstermek gerekir.
- **Değişiklik bazlı aktarım:** Yalnızca son aktarımdan sonra değişen kayıtların gönderilmesi, büyük veri setlerinde süreyi kısaltır. Bunun için ERP'de güvenilir bir değişiklik zamanı alanı bulunmalıdır.

**Hata yönetimi.** Her hatalı kayıt için hata nedeni, ham veri ve yeniden deneme durumu saklanmalıdır. Hata türleri sınıflandırılmalıdır: ana veri eksikliği (ör. tanımsız ürün), iş kuralı ihlali (ör. kredi limiti) ve teknik hata (ör. bağlantı kopması). Her sınıf için sorumlu farklıdır; ana veri hatasını müşterinin ana veri ekibi, teknik hatayı entegrasyon ekibi çözer.

**Sürüm yönetimi.** Müşterinin ERP'si güncellendiğinde adaptörün etkilenip etkilenmeyeceği önceden test edilmelidir. Bu nedenle müşteriyle yapılan sözleşmede ERP güncellemelerinin bildirilmesi ve test ortamı sağlanması maddeleri yer almalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b8.py` ile yapılmıştır.

Yeni bir müşteride ilk ayda 5.000 sipariş ERP'ye aktarılıyor; 75'i hata alıyor: **%1,5**. Hataların çoğu, ERP'de pasif yapılmış ama satış uygulamasına iletilmemiş ürün kodlarından kaynaklanıyor. Ekip, ürün durum alanını eşleştirme tablosuna ekliyor ve günlük mutabakat raporunu müşterinin muhasebe ekibiyle paylaşıyor.

## Sık yapılan hatalar

- Her müşteri için sıfırdan özel kod yazmak.
- Alan eşleştirmeyi yazılı hâle getirmemek.
- Ana verinin hangi sistemde ana kaynak olduğunu belirlememek.
- E-belgenin iki sistemden üretilebilmesine izin vermek.
- Mutabakat yapmadan canlıya geçmek.

## Pratikte nasıl uygulanır?

Kurulum kontrol listesi:

- [ ] ERP türü ve sürümü, erişim yöntemi (API, veritabanı, dosya)
- [ ] Ana veri kaynağı kararları
- [ ] Alan eşleştirme tablosu ve birim dönüşümleri
- [ ] Sipariş, tahsilat ve iade akışlarının testi
- [ ] E-belgenin üretileceği sistem ve entegratör bilgisi
- [ ] Hata kuyruğu ve sorumlu kişi
- [ ] Günlük mutabakat raporu

## Daha fazlası

- Hohpe ve Woolf, *Enterprise Integration Patterns* (kitap; doğrulanmadı).
