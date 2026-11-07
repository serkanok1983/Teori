---
id: kb-ea-20-1-what-erp-does
title: "ERP ne yapar? Tek veritabanı, entegre modüller ve organizasyon yapısı"
summary: "ERP sistemlerinin ortak veritabanı üzerinde satış, satın alma, stok, üretim ve finans modüllerini nasıl birleştirdiğini; şirket, tesis, depo ve satış organizasyonu gibi organizasyon yapılarını ve yapılandırma ile kod yazma arasındaki farkı anlatır."
course: ea
category: erp
tags: [erp, entegrasyon, organizasyon-yapisi, temel]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru, it-yoneticisi]
level: temel
source_lessons: [EA-20.1]
reading_minutes: 3
key_points:
  - "ERP, firmanın ana süreçlerini ortak bir veritabanı üzerinde birleştiren paket yazılımdır."
  - "Bir işlem bir kez girilir; satış, depo ve muhasebe aynı kaydı görür."
  - "Organizasyon yapısı (şirket, tesis, depo, satış organizasyonu) kurulumun en kritik kararıdır."
  - "Çoğu uyarlama kodla değil, parametrelerle yapılır."
  - "ERP'nin değeri, üzerindeki süreçlerin ve verinin kalitesine bağlıdır."
glossary_terms: [erp, organizasyon-yapisi]
related: [kb-ea-1-1-what-is-an-enterprise-system, kb-ea-20-2-order-to-cash, kb-ea-20-3-procure-to-pay, kb-ea-5-5-erp-core-vs-best-of-breed]
sources:
  - title: "Enterprise resource planning: introduction"
    authors: "Kumar, K.; van Hillegersberg, J."
    year: 2000
    type: article
    doi: "10.1145/332051.332063"
    url: "https://doi.org/10.1145/332051.332063"
    verified: true
    checked_on: 2026-10-28
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

ERP kelimesi her toplantıda geçer ama ne yaptığı çoğu zaman "muhasebe programının büyüğü" olarak anlaşılır. Bu kart, ERP'nin temel mantığını ve kurulumda verilen en önemli kararları anlatır.

## Temel fikir

Kumar ve van Hillegersberg (2000), ERP'yi firmanın iş süreçlerini tek bir bütünleşik sistemde toplayan, hazır süreç modelleri içeren paket yazılım olarak tanımlar. Üç ana fikir vardır:

1. **Ortak veritabanı:** Müşteri, ürün ve tedarikçi bir kez tanımlanır; tüm modüller aynı kaydı kullanır.
2. **Entegre modüller:** Satış, satın alma, stok, üretim ve finans birbirine bağlıdır. Sevkiyat onaylandığında stok düşer, muhasebe kaydı otomatik oluşur, fatura hazırlanır.
3. **Hazır süreçler ve yapılandırma:** Paket, belirli süreç varsayımlarıyla gelir. Uyarlama çoğunlukla kod yazarak değil, parametrelerle (belge tipleri, onay kuralları, hesap eşleştirmeleri) yapılır.

**Organizasyon yapısı**, kurulumun en kritik ve sonradan en zor değişen kararıdır. Magal ve Word'ün anlattığı tipik birimler:

- **Şirket:** Ayrı mali tablo hazırlayan tüzel kişilik.
- **Tesis / şube:** Üretim veya dağıtım yeri.
- **Depo / stok yeri:** Stokun fiziksel olarak tutulduğu yer.
- **Satış organizasyonu ve dağıtım kanalı:** Satıştan sorumlu birim ve satışın yapıldığı kanal (ör. geleneksel kanal, zincir market).

Bu yapılar raporlamayı, yetkileri ve fiyatlandırmayı belirler. Örneğin kanallar ayrı tanımlanmazsa kanal bazlı kârlılık raporu alınamaz.

### ERP'den beklenenler ve sınırları

ERP'nin sağladığı entegrasyon güçlü bir avantajdır; ancak her şeyi ERP'den beklemek de hatalı kararlara yol açabilir. Kumar ve van Hillegersberg'in vurguladığı gibi, ERP süreçleri belirli bir iş modeline göre tasarlar ve bu modelin şirkete uyumu değerlendirilmelidir.

- **ERP'nin güçlü olduğu alanlar:** Muhasebe, satın alma, stok, satış siparişi ve faturalama gibi işlem yoğun ve standart süreçler. Bu alanlarda tek veritabanı, verinin bir kez girilmesini ve tüm birimlerde aynı biçimde görülmesini sağlar.
- **Uzman ürünlerin gerekebileceği alanlar:** Saha satışı, gelişmiş depo yönetimi, rota planlama ve gelişmiş analitik gibi alanlarda ERP modülleri sınırlı kalabilir.
- **Organizasyon yapısının önemi:** Şirket, şube, depo ve satış organizasyonu tanımları, ERP kurulumunun en başında yapılır ve sonradan değiştirilmesi zordur. Bu yapı, raporlama ve yetkilendirmeyi de belirler. Bu nedenle gelecekteki büyüme ve yapı değişiklikleri de düşünülerek tasarlanmalıdır.
- **Süreç disiplini:** ERP, verinin doğru ve zamanında girilmesine bağlıdır. Bir birimdeki gecikme veya hata, diğer birimleri de etkiler. Bu nedenle ERP, şirket içinde daha fazla süreç disiplini gerektirir.

**Gerçek zamanlı bilgi.** Entegre bir ERP'de satış siparişi girildiği anda stok, kredi limiti ve muhasebe etkileri görülebilir. Bu, yönetimin güncel bilgiyle karar vermesini sağlar; ancak verinin kalitesi, bu bilginin güvenilirliğini belirler.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b4.py` ile yapılmıştır.

Bir bayide sipariş önce satış programına, sonra depo Excel'ine, en son muhasebe programına giriliyor. Günde 400 siparişle toplam **1.200** giriş yapılıyor. ERP'ye geçildiğinde sipariş bir kez girilir; depo ve muhasebe aynı kaydı kullanır. Giriş sayısı **400**'e iner; yani **%66,7** azalır. Daha önemlisi, üç sistem arasındaki tutarsızlıklar ortadan kalkar.

Kurulumda bayi, geleneksel kanal ve zincir market satışlarını iki ayrı dağıtım kanalı olarak tanımlıyor; böylece kanal bazlı marj raporu ilk günden alınabiliyor.

## Sık yapılan hatalar

- Organizasyon yapısını danışmana bırakıp raporlama ihtiyacıyla birlikte düşünmemek.
- ERP'yi eski programın ekranlarını kopyalayacak şekilde özelleştirmek.
- Ana veriyi temizlemeden ERP'ye taşımak.
- ERP'nin her şeyi çözeceğini varsayıp süreçleri değiştirmemek.

## Pratikte nasıl uygulanır?

- [ ] Hangi raporları şirket, şube, depo ve kanal bazında görmek istediğinizi yazın.
- [ ] Organizasyon yapısını bu raporlara göre tasarlayın.
- [ ] Uyarlama isteklerini "parametre" ve "kod" olarak ayırın.
- [ ] Çift giriş yapılan her yeri listeleyip ERP kapsamına alın.

## Daha fazlası

- Kumar ve van Hillegersberg (2000), *Communications of the ACM*. https://doi.org/10.1145/332051.332063
- Magal ve Word, *Integrated Business Processes with ERP Systems* (kitap; doğrulanmadı).
