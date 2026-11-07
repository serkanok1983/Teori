---
id: kb-ea-11-6-apis-for-managers
title: "Yöneticiler için API: Uç noktalar, sınırlar ve sözleşme"
summary: "Bir uygulama programlama arayüzünün (API) nasıl çalıştığını; kimlik doğrulama, istek sınırı, sayfalama, sürümleme ve olay bildirimi (webhook) kavramlarını ve bir tedarikçinin API'sini değerlendirirken sorulacak soruları anlatır."
course: ea
category: entegrasyon
tags: [entegrasyon, api, webhook, mimari]
roles: [it-yoneticisi]
level: ileri
source_lessons: [EA-11.6]
reading_minutes: 3
key_points:
  - "API, bir sistemin başka sistemlere hangi veriyi hangi kurallarla verdiğini tanımlayan sözleşmedir."
  - "İstek sınırı (rate limit) ve sayfalama, toplu veri aktarımının ne kadar süreceğini belirler."
  - "Sürümleme, tedarikçi API'yi değiştirdiğinde entegrasyonunuzun kırılmamasını sağlar."
  - "Webhook, sizin sürekli sormanız yerine karşı sistemin olay olduğunda haber vermesidir."
  - "API dokümantasyonu, test ortamı ve değişiklik bildirimi sözleşmeye yazılmalıdır."
glossary_terms: [api, webhook, entegrasyon]
related: [kb-ea-10-1-why-integration-is-hard, kb-ea-40-4-integrating-sfa-with-erp, kb-ea-6-2-it-service-sla, kb-ea-15-2-user-roles-permissions]
sources:
  - title: "Architectural Styles and the Design of Network-based Software Architectures (doktora tezi)"
    authors: "Fielding, R. T."
    year: 2000
    type: web
    url: "https://ics.uci.edu/~fielding/pubs/dissertation/top.htm"
    verified: true
    checked_on: 2026-10-28
    note: "URL HTTP 200 ile açıldı, başlık/kurum eşleşti (2026-10-28)."
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

"Sistemimizin API'si var" cümlesi entegrasyonun kolay olacağı anlamına gelmez. Bu kart, bir **API**'yi teknik ekip gibi değil, iş ve sözleşme açısından değerlendirmenize yardım eder.

## Temel fikir

API (*application programming interface*), bir sistemin dışarıya açtığı kapılar listesidir. Her kapı (**uç nokta**, *endpoint*) bir işi yapar: "ürünleri listele", "sipariş oluştur", "stok getir". Günümüzde çoğu iş uygulaması, Fielding'in tanımladığı REST yaklaşımına uygun, internet üzerinden JSON veri alıp veren API'ler sunar.

Değerlendirmede bakılacak kavramlar:

- **Kimlik doğrulama:** Kim, hangi anahtarla bağlanıyor? Anahtar kişiye değil entegrasyon kullanıcısına ait olmalı ve yetkisi sınırlı tutulmalıdır.
- **İstek sınırı** (*rate limit*): Dakikada kaç çağrıya izin var? Toplu aktarım süresini bu belirler.
- **Sayfalama:** Büyük listeler parça parça gelir; sayfa boyutu çağrı sayısını belirler.
- **Toplu işlem:** Tek çağrıda çok kayıt gönderilebiliyor mu?
- **Webhook:** Karşı sistem, bir olay olduğunda (yeni sipariş, durum değişikliği) size kendisi haber verebiliyor mu? Yoksa sürekli sormanız mı gerekiyor?
- **Sürümleme:** Tedarikçi API'yi değiştirdiğinde eski sürüm ne kadar süre çalışmaya devam ediyor?
- **Hata kodları ve tekrar deneme:** Başarısız çağrıda ne dönüyor, tekrar göndermek kopya kayıt yaratır mı?

### API projelerinde yöneticinin soracağı sorular

Bir entegrasyon projesi değerlendirilirken, yöneticinin teknik ayrıntılara girmeden sorabileceği temel sorular şunlardır:

- **Hangi iş olayları aktarılıyor?** Sipariş, fatura, stok, fiyat veya müşteri değişikliği gibi hangi bilgilerin hangi yönde ve hangi sıklıkta aktarılacağı bir listede yer almalıdır.
- **Gecikme ne kadar kabul edilebilir?** Bazı bilgilerin anlık aktarılması gerekirken, bazıları için günlük aktarım yeterlidir. Bu karar, mimari seçimi ve maliyeti doğrudan etkiler.
- **Hata olursa ne olur?** Aktarım başarısız olduğunda kim haberdar olur, kayıt kaybolur mu, otomatik yeniden deneme var mı? Hata yönetimi tasarlanmamış bir entegrasyon, sessizce veri kaybına yol açabilir.
- **Kim sahibi?** API'nin ve entegrasyonun bakımından, belgelerinden ve değişikliklerinden kim sorumlu? Dış tedarikçinin API'si değiştiğinde kim haberdar edilir?
- **Güvenlik nasıl sağlanıyor?** Erişim anahtarları nerede saklanıyor, kimlerin erişimi var, düzenli olarak yenileniyor mu?
- **Maliyet modeli nedir?** Bazı hizmetler API çağrısı başına ücret alır; hacim arttıkça maliyet beklenmedik biçimde yükselebilir.

**Sözleşme ve belgeler.** Dış tedarikçilerle API üzerinden çalışılırken, hizmet seviyesi, istek sınırları, sürüm değişikliklerinin bildirim süresi ve destek kanalları sözleşmede yer almalıdır. İyi belgelenmiş bir API, entegrasyon süresini ve maliyetini belirgin biçimde azaltır. Hohpe ve Woolf'un desenleri, bu tartışmalarda ortak bir dil sağlar.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b3.py` ile yapılmıştır.

Bir e-ticaret platformu dakikada 600 çağrıya izin veriyor. 12.000 ürünün fiyatı güncellenecek:

| Yöntem | Çağrı sayısı | Süre |
|---|---|---|
| Ürün başına bir çağrı | 12.000 | 20,0 dakika |
| Sayfa başına 100 ürün | 120 | 0,20 dakika |

Aynı iş, toplu işlem desteğiyle saniyeler içinde bitiyor. Ürün başına çağrı ise 20 dakika boyunca istek sınırını dolduruyor; bu sürede sipariş çekme çağrıları da bekliyor. Bu yüzden teklif aşamasında toplu işlem ve sayfa boyutu sorulmalıdır.

## Sık yapılan hatalar

- API'nin varlığını yeterli sayıp istek sınırı ve toplu işlem desteğini sormamak.
- Entegrasyonu bir çalışanın kişisel API anahtarıyla kurmak.
- Webhook varken her dakika tüm listeyi yeniden çekmek.
- Sürüm değişikliği bildirim süresini sözleşmeye yazmamak.

## Pratikte nasıl uygulanır?

- [ ] Tedarikçiden API dokümantasyonu ve test ortamı isteyin.
- [ ] İstek sınırı, sayfa boyutu, toplu işlem ve webhook desteğini yazılı alın.
- [ ] Sürüm değişikliklerinin kaç ay önce bildirileceğini sözleşmeye koyun.
- [ ] Entegrasyon için ayrı ve yetkisi sınırlı bir kullanıcı açın.
- [ ] Hatalı çağrıları izleyen bir rapor ve alarm tanımlayın.

## Daha fazlası

- Fielding (2000), REST'i tanımlayan doktora tezi.
- Hohpe ve Woolf, *Enterprise Integration Patterns* (kitap; doğrulanmadı).
