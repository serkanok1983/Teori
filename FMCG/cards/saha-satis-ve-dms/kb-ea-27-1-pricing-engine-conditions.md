---
id: kb-ea-27-1-pricing-engine-conditions
title: "Fiyatlandırma motoru: Koşul tekniği ve fiyat şelalesi"
summary: "ERP ve saha sistemlerinde fiyatın liste fiyatı, iskonto, kademe ve erişim sırası gibi koşullarla nasıl hesaplandığını ve liste fiyatından cep fiyatına kadar olan fiyat şelalesinin nasıl görünür kılınacağını anlatır."
course: ea
category: saha-satis-ve-dms
tags: [fiyatlandirma, kosul-teknigi, iskonto, fiyat-selalesi]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-27.1]
reading_minutes: 3
key_points:
  - "Fiyat motoru, liste fiyatı ve iskontoları koşul kayıtları olarak tutar ve sırayla uygular."
  - "Erişim sırası, hangi koşul kaydının önce aranacağını belirler (ör. müşteri, sonra müşteri grubu, sonra genel)."
  - "Kademeli iskonto miktara veya tutara göre değişen iskontodur."
  - "Fiyat şelalesi, fatura dışı primler dahil tüm indirimleri göstererek cep fiyatını ortaya çıkarır."
  - "Fatura dışı indirimler sistemde izlenmezse gerçek kârlılık görünmez."
glossary_terms: [kosul-teknigi, erisim-sirasi, fiyat-selalesi, cep-fiyati]
related: [kb-fmcg-5-1-price-elasticity, kb-fmcg-5-6-pricing-in-high-inflation, kb-ea-27-2-tpm-promotion-settlement, kb-ea-20-2-order-to-cash]
sources:
  - title: "The Strategy and Tactics of Pricing"
    authors: "Nagle, T. T.; Müller, G."
    year: 2018
    type: book
    doi: "10.4324/9781315266220"
    verified: true
    checked_on: 2026-10-28
    note: "DOI Crossref kaydında başlık ve yazar eşleşti; baskı yılı karttakinden farklı olabilir."
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

Bir bayiye uygulanan fiyat; liste fiyatı, kanal iskontosu, miktar kademesi, kampanya ve yıl sonu primiyle oluşur. Bunlar farklı Excel dosyalarında tutulduğunda kimse gerçek fiyatı bilemez. Bu kart, fiyatlandırma motorunun mantığını ve **fiyat şelalesini** anlatır.

## Temel fikir

**Koşul tekniği.** ERP'lerde yaygın kullanılan yaklaşımda fiyatın her parçası bir **koşul** olarak tanımlanır:

- Liste fiyatı (ürün bazında)
- Kanal iskontosu (müşteri grubu bazında)
- Müşteriye özel iskonto
- Kademeli iskonto (ör. 100 koli üzeri ek %3)
- Kampanya iskontosu (tarih aralığına bağlı)

Her koşulun bir **erişim sırası** vardır: Sistem önce müşteriye özel kaydı arar, bulamazsa müşteri grubuna, o da yoksa genel kayda bakar. Koşullar bir **fiyatlandırma şemasında** sırayla uygulanır; her adım bir önceki tutar üzerinden hesaplanır.

**Fiyat şelalesi.** Nagle ve Müller, liste fiyatından başlayıp tüm indirimleri sırayla düşerek **cep fiyatına** ulaşan bir şema önerir. Fatura üzerindeki iskontoların yanında fatura dışı kalemler de gösterilir:

- Yıl sonu ciro primleri,
- Ödeme vadesi maliyeti,
- Promosyon ve raf katkı payları,
- Ücretsiz mal fazlası.

Fatura dışı kalemler genellikle ayrı tablolarda izlendiği için en çok bunlar gözden kaçar.

### Fiyat yönetişimi

Fiyatlandırma motoru güçlü bir araçtır; ancak kuralların kontrolsüz çoğalması, fiyatı anlaşılmaz ve yönetilemez hâle getirir. Sağlıklı bir fiyat yönetimi için şu ilkeler önerilir:

- **Koşul türlerini sınırlayın:** Her yeni ticari talep için yeni bir koşul türü açmak yerine, mevcut türlerin kullanılması tercih edilmelidir. Az sayıda ve iyi tanımlanmış koşul türü, hem bakımı hem de analizi kolaylaştırır.
- **Onay akışları:** Fiyat listesi değişiklikleri ve müşteriye özel iskontolar, tutara ve iskonto oranına göre farklı onay seviyelerinden geçmelidir.
- **Geçerlilik tarihleri:** Her koşulun başlangıç ve bitiş tarihi olmalıdır. Süresiz koşullar, zamanla unutulan ve gereksiz yere uygulanan iskontolara dönüşür.
- **Çakışma kuralları:** Aynı siparişe birden fazla iskonto uygulanabiliyorsa, hangisinin öncelikli olduğu veya iskontoların birleşip birleşmeyeceği açıkça tanımlanmalıdır.
- **Düzenli temizlik:** Süresi dolmuş veya kullanılmayan koşullar periyodik olarak gözden geçirilmeli ve pasife alınmalıdır.

**Fiyat şelalesi analizi.** Nagle ve Müller'in vurguladığı gibi, liste fiyatı ile cebe giren net fiyat arasındaki fark çoğu zaman sanıldığından büyüktür. Fatura üzerindeki iskontoların yanı sıra, fatura dışı primler, ödeme iskontoları ve lojistik destekleri de şelaleye dahil edilmelidir. Müşteri bazında şelale analizi, hangi müşterilerin kârlılığı aşındırdığını gösterir.

**Satış ekibinin yetkisi.** Temsilcilerin sahada verebileceği iskonto aralıkları sistemde tanımlanmalı ve aşımlar onaya düşmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b6.py` ile yapılmıştır.

Bir ürünün liste fiyatı koli başı 300 TL.

- Kanal iskontosu %10: **270,00 TL**
- Kademe iskontosu %3: **261,90 TL** (fatura fiyatı)
- Yıl sonu primi %2: **5,24 TL**
- Promosyon katkısı: 6,00 TL
- Cep fiyatı: **250,66 TL**; liste fiyatının **%83,6**'sı

Satış ekibi fatura fiyatına bakarak kârlılığı değerlendiriyordu. Şelale, fatura dışı kalemlerin de hesaba katılması gerektiğini gösteriyor.

## Sık yapılan hatalar

- Müşteriye özel fiyatları sistem dışında, Excel'de tutmak.
- Koşulları üst üste bindirip hangi iskontonun geçerli olduğunu bilmemek.
- Fatura dışı primleri müşteri kârlılığına yansıtmamak.
- Koşul kayıtlarının geçerlilik tarihlerini kontrol etmemek.

## Pratikte nasıl uygulanır?

- [ ] Kullandığınız tüm fiyat ve iskonto türlerini listeleyin.
- [ ] Her biri için erişim sırasını ve uygulama sırasını belirleyin.
- [ ] Fatura dışı kalemleri müşteri bazında ERP'de izleyin.
- [ ] Ana müşteriler için üç ayda bir fiyat şelalesi raporu hazırlayın.

## Daha fazlası

- Nagle ve Müller, *The Strategy and Tactics of Pricing*.
- Magal ve Word, *Integrated Business Processes with ERP Systems* (kitap; doğrulanmadı).
