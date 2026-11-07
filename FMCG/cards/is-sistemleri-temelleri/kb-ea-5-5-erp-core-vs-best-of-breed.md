---
id: kb-ea-5-5-erp-core-vs-best-of-breed
title: "ERP çekirdeği mi, en iyi uzman ürünler mi? Uygulama yerleşimini seçmek"
summary: "Tek bir paketin her işi yapması (suit), ERP çekirdeği etrafında uzman uygulamalar ve her alan için ayrı en iyi ürün yaklaşımlarını karşılaştırır; arayüz sayısı ve 'temiz çekirdek' fikriyle karar ölçütlerini verir."
course: ea
category: is-sistemleri-temelleri
tags: [erp, mimari, entegrasyon, yazilim-secimi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, it-yoneticisi]
level: orta
source_lessons: [EA-5.5]
reading_minutes: 3
key_points:
  - "Üç temel yerleşim vardır: tek paket (suit), ERP çekirdeği + uzman uydular, her alanda ayrı en iyi ürün."
  - "Her yeni uygulama, bakımı gereken yeni arayüzler getirir; noktadan noktaya bağlantı sayısı hızla artar."
  - "'Temiz çekirdek', ERP'nin özelleştirilmeden standart tutulması ve farklılaşan işlerin dışarıda çözülmesidir."
  - "İki katmanlı ERP, merkezde büyük bir sistem, bayi veya şubede daha hafif bir sistem kullanmaktır."
  - "Karar, farklılaştığınız alanlarla teknik ekibinizin entegrasyon taşıma gücüne göre verilir."
glossary_terms: [erp, entegrasyon]
related: [kb-ea-5-4-application-portfolio, kb-ea-10-1-why-integration-is-hard, kb-ea-17-1-build-buy-configure, kb-ea-40-4-integrating-sfa-with-erp]
sources:
  - title: "Enterprise resource planning: Implementation procedures and critical success factors"
    authors: "Umble, E. J.; Haft, R. R.; Umble, M. M."
    year: 2003
    type: article
    doi: "10.1016/S0377-2217(02)00547-7"
    verified: true
    checked_on: 2026-10-28
    note: "DOI Crossref kaydında başlık ve yazar eşleşti; baskı yılı karttakinden farklı olabilir."
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

Yeni bir saha satış, depo ya da raporlama ihtiyacı çıktığında iki seçenek hep masadadır: ERP'nin kendi modülünü kullanmak ya da o alanda daha iyi bir uzman ürün almak. Bu kart, bu tekil kararları bir **uygulama yerleşimi** stratejisine bağlamanızı sağlar.

## Temel fikir

Üç yaygın yaklaşım vardır:

| Yaklaşım | Artı | Eksi |
|---|---|---|
| **Tek paket (suit):** Her şey aynı tedarikçiden | Tek veri modeli, az entegrasyon | Bazı modüller zayıf kalabilir, tedarikçiye bağımlılık |
| **ERP çekirdeği + uzman uydular** | Finans, stok, fatura tek yerde; saha satış veya depo gibi alanlarda daha iyi ürün | Her uydu için arayüz ve sorumluluk |
| **Her alanda en iyi ürün** (*best-of-breed*) | Her alanda en güçlü işlev | Çok sayıda arayüz, veri tutarsızlığı, yüksek BT yükü |

Bu kararda iki kavram işe yarar:

- **Temiz çekirdek** (*clean core*): ERP'nin kaynak kodunu değiştirmeden, standart kullanmak. Firmayı farklılaştıran işler (ör. özel prim modeli, saha uygulaması) ERP'nin dışındaki, standart arayüzlerle bağlanan uygulamalarda çözülür. Böylece ERP sürüm güncellemeleri kolaylaşır.
- **İki katmanlı ERP** (*two-tier ERP*): Üretici merkezde büyük bir ERP kullanırken bayilerin veya küçük şirketlerin daha hafif bir sistem kullanması ve ikisinin belirli verilerle bağlanması.

### Karar için değerlendirme soruları

Uygulama yerleşimine karar verirken, her iş alanı için ayrı ayrı şu sorular sorulabilir:

- **Farklılaştırıcı mı?** Bu süreç şirketinizi rakiplerinden ayıran bir yetkinlik mi, yoksa herkesin benzer biçimde yaptığı bir iş mi? Muhasebe ve bordro gibi standart süreçlerde ERP çekirdeği genellikle yeterlidir. Saha satışı veya depo yönetimi gibi alanlarda ise uzman ürünler belirgin avantaj sağlayabilir.
- **ERP'nin yeteneği yeterli mi?** ERP'nin ilgili modülü ihtiyaçların ne kadarını karşılıyor? Eksikler küçük ayarlarla mı kapanır, yoksa ağır özelleştirme mi gerekir?
- **Entegrasyon maliyeti:** Uzman ürün seçildiğinde, ana veri, işlem verisi ve raporlama için kaç entegrasyon gerekecek? Her entegrasyon, kurulum ve sürekli bakım maliyeti demektir.
- **Kullanıcı deneyimi:** Kullanıcılar farklı sistemler arasında geçiş yapmak zorunda kalacak mı? Saha çalışanları için mobil deneyim ayrıca değerlendirilmelidir.
- **Tedarikçi bağımlılığı:** Tek tedarikçiye bağımlılık, pazarlık gücünü azaltabilir; çok sayıda tedarikçi ise yönetim yükünü artırır.

**Entegrasyon mimarisi.** Uzman ürünler seçildiğinde, noktadan noktaya bağlantılar zamanla karmaşık bir ağa dönüşebilir. Hohpe ve Woolf'un anlattığı mesajlaşma desenleri ve ortak bir entegrasyon katmanı, bu karmaşıklığı sınırlamaya yardımcı olur.

**Ana verinin yeri.** Hangi yaklaşım seçilirse seçilsin, müşteri, ürün ve fiyat verisinin tek bir kaynağı olmalıdır. Bu kaynak çoğu zaman ERP'dir; uzman ürünler bu veriyi ERP'den alır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b2.py` ile yapılmıştır.

Altı uygulamanın her biri diğer beşiyle doğrudan konuşursa n × (n − 1) ÷ 2 formülüyle **15 arayüz** oluşur; sekiz uygulamada bu sayı **28**'e çıkar. Arayüz başına yıllık 40.000 TL bakım varsayıldığında 15 arayüz yılda **600.000 TL** eder.

Aynı firma ERP'yi çekirdek yapar ve saha satış, depo, raporlama uygulamalarını yalnızca ERP'ye bağlarsa **3 arayüz** ve yılda **120.000 TL** bakım kalır. Uydular birbirleriyle değil, ERP üzerinden konuşur.

## Sık yapılan hatalar

- Her departmanın kendi favori ürününü seçmesine izin verip entegrasyonu sonraya bırakmak.
- ERP'yi firmaya uydurmak için kaynak kodunu değiştirmek; her güncellemede maliyet doğurur.
- Uzman ürünü yalnızca demoya göre seçmek; arayüz maliyetini teklif dışı bırakmak.
- "Tek paket" kararının modül kalitesini garanti ettiğini sanmak.

## Pratikte nasıl uygulanır?

- [ ] Firmanızı rakiplerden ayıran 2–3 alanı yazın; uzman ürün öncelikle buralarda düşünülür.
- [ ] Geri kalan alanlarda ERP'nin standart modülünü varsayılan seçim yapın.
- [ ] Her uydu uygulama için hangi verinin hangi yönde aktığını tek bir şemada gösterin.
- [ ] Teklif değerlendirmesine arayüz kurulum ve yıllık bakım maliyetini ekleyin.
- [ ] ERP'de kod değişikliği taleplerini bir kurulda onaya bağlayın.

## Daha fazlası

- Hohpe ve Woolf, *Enterprise Integration Patterns* (kitap; doğrulanmadı).
- Tedarikçilerin "temiz çekirdek" ve iki katmanlı ERP dokümanları, karar anında güncel sürümleriyle okunmalıdır.
