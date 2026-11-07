---
id: kb-ea-10-1-why-integration-is-hard
title: "Entegrasyon neden zordur? Dört entegrasyon yolu ve ortak veri dili"
summary: "Sistemleri birbirine bağlamanın neden teknik değil çoğunlukla anlam sorunu olduğunu; dosya aktarımı, ortak veritabanı, doğrudan çağrı ve mesajlaşma yollarını ve ortak veri modeliyle eşleme tablolarının rolünü anlatır."
course: ea
category: entegrasyon
tags: [entegrasyon, ana-veri, mimari, erp]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, it-yoneticisi]
level: orta
source_lessons: [EA-10.1, EA-10.5]
reading_minutes: 3
key_points:
  - "Entegrasyonun asıl zorluğu anlamdır: Aynı kelime iki sistemde farklı şey ifade edebilir."
  - "Dört temel yol vardır: dosya aktarımı, ortak veritabanı, doğrudan çağrı (API) ve mesajlaşma."
  - "Ortak veri modeli, her sistemin kendi koduyla değil ortak bir tanımla konuşmasını sağlar."
  - "Ürün, müşteri ve birim eşleme tabloları entegrasyonun en kritik ana verisidir."
  - "Her arayüz için sahip, hata bildirimi ve tekrar deneme kuralı tanımlanmalıdır."
glossary_terms: [entegrasyon, ana-veri]
related: [kb-ea-5-5-erp-core-vs-best-of-breed, kb-ea-11-6-apis-for-managers, kb-ea-40-4-integrating-sfa-with-erp, kb-ea-8-3-mdm-matching-duplicates]
sources:
  - title: "Federated database systems for managing distributed, heterogeneous, and autonomous databases"
    authors: "Sheth, A. P.; Larson, J. A."
    year: 1990
    type: article
    doi: "10.1145/96602.96604"
    url: "https://doi.org/10.1145/96602.96604"
    verified: true
    checked_on: 2026-10-28
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

"İki sistemi entegre edin, bir haftalık iş" denilen projeler çoğu zaman aylar sürer. Bu kart, **entegrasyonun** neden zor olduğunu ve teklif değerlendirirken ya da bir arayüz sorunu çözerken hangi soruları sormanız gerektiğini anlatır.

## Temel fikir

Sheth ve Larson (1990), birbirinden bağımsız geliştirilmiş veritabanlarını birlikte kullanmanın üç zorluğunu tanımlar: farklı yapı, farklı anlam ve her sistemin kendi kararını vermesi. Bugün de en zor kısım **anlamdır**:

- Saha uygulamasında "miktar" koli, ERP'de adet olabilir.
- "Müşteri" bir sistemde vergi mükellefi, diğerinde teslimat noktasıdır.
- "Ciro" birinde iskonto öncesi, diğerinde sonrasıdır.

Hohpe ve Woolf dört temel entegrasyon yolunu ayırır:

| Yol | Nasıl çalışır | Ne zaman uygun |
|---|---|---|
| Dosya aktarımı | Bir sistem dosya yazar, diğeri okur | Günlük toplu aktarım, basit ortam |
| Ortak veritabanı | İki uygulama aynı tabloları kullanır | Aynı tedarikçinin modülleri |
| Doğrudan çağrı (API) | Bir sistem diğerinden anında veri ister veya gönderir | Anlık stok, fiyat, sipariş |
| Mesajlaşma | Olaylar bir kuyruğa yazılır, alıcılar sırayla işler | Çok sistem, kesintiye dayanıklılık |

Çok sayıda sistem varsa **ortak veri modeli** (*canonical data model*) kullanılır: Her sistem kendi verisini ortak tanıma çevirir. Böylece her yeni sistem için yalnızca bir eşleme yazılır. Pratikte bunun kalbi **eşleme tablolarıdır**: ürün kodu, müşteri kodu, birim ve vergi kodu karşılıkları.

### Entegrasyon zorluğunu azaltmanın yolları

Entegrasyonun zorluğu büyük ölçüde teknik değil, anlam ve sorumluluk meselesidir. Sheth ve Larson'ın vurguladığı gibi, farklı sistemler aynı kavramı farklı biçimde tanımlar. Zorluğu azaltmak için şu yaklaşımlar yardımcı olur:

- **Ortak kavram sözlüğü:** Müşteri, nokta, sipariş, iade ve teslimat gibi kavramların ne anlama geldiği ve hangi alanlarla tanımlandığı yazılı olmalıdır. Örneğin bir sistemde "müşteri" fatura adresi, diğerinde teslimat noktası olabilir.
- **Ana verinin tek kaynağı:** Her veri türü için hangi sistemin kaynak olduğu belirlenmelidir. İki sistemin aynı veriyi değiştirebildiği durumlar, çakışmaların ve tutarsızlıkların başlıca nedenidir.
- **Entegrasyon envanteri:** Hangi sistemlerin birbirine hangi yolla, hangi sıklıkta bağlı olduğu bir listede tutulmalıdır. Bu liste, bir sistem değiştiğinde etkilenecek bağlantıları görmeyi sağlar.
- **İzleme:** Her entegrasyonun başarılı ve başarısız işlem sayıları düzenli olarak izlenmelidir. Sessizce duran bir entegrasyon, günler sonra fark edildiğinde büyük düzeltme yükü yaratır.
- **Sahiplik:** Her entegrasyonun bir iş sahibi ve bir teknik sahibi olmalıdır.

**Yol seçimi.** Hohpe ve Woolf'un tarif ettiği dört yol arasında tek bir doğru yoktur. Toplu ve az değişen veriler için dosya aktarımı, anlık sorgular için API, birden fazla sistemin aynı olaydan haberdar olması gereken durumlar için mesajlaşma uygundur. Ortak veritabanı ise hızlı görünse de sistemleri birbirine sıkı biçimde bağladığı için genellikle kaçınılması önerilen bir yoldur.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b3.py` ile yapılmıştır.

Saha uygulaması siparişi koli olarak gönderiyor, ERP ise adet bekliyor. Koli içi adet 24 olan bir üründen 10 kolilik sipariş ERP'ye 10 adet olarak düşüyor. Doğru miktar 240 adet; fark **24 kat**. Adet fiyatı 18,50 TL ile doğru tutar **4.440,00 TL** iken fatura **185,00 TL** çıkıyor.

Hata, entegrasyon spesifikasyonunda birimin yazılmamasından kaynaklanıyor. Çözüm: Arayüz dokümanına her alanın birimi ve anlamı ekleniyor; ERP tarafında koli içi adetten dönüşüm yapılıyor ve sipariş tutarı iki sistemde farklıysa kayıt hata kuyruğuna düşüyor.

## Sık yapılan hatalar

- Arayüzü yalnızca alan adlarıyla tanımlayıp anlamı ve birimi yazmamak.
- Hata olduğunda kaydın sessizce kaybolması; kimsenin haberdar olmaması.
- Eşleme tablolarını bir kişinin Excel'inde tutmak.
- Her sistem çiftine ayrı arayüz yazıp sayısının artmasına izin vermek.

## Pratikte nasıl uygulanır?

- [ ] Her arayüz için bir sayfalık doküman isteyin: alanlar, anlamları, birimleri, yönü, sıklığı.
- [ ] Ürün, müşteri, birim ve vergi kodu eşleme tablolarının sahibini belirleyin.
- [ ] Hatalı kayıtlar için bir kuyruk, bildirim ve tekrar deneme kuralı tanımlayın.
- [ ] İki sistem arasında günlük mutabakat raporu (kayıt sayısı ve tutar) çalıştırın.

## Daha fazlası

- Sheth ve Larson (1990), *ACM Computing Surveys*. https://doi.org/10.1145/96602.96604
- Hohpe ve Woolf, *Enterprise Integration Patterns* (kitap; doğrulanmadı).
