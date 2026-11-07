---
id: kb-ea-26-1-retail-execution-sfa
title: "Saha satış otomasyonu (SFA): Rut planı, mükemmel mağaza ve sipariş alma"
summary: "Hızlı tüketim ürünlerinde saha satış otomasyonunun ziyaret ve rut planlama, mükemmel mağaza denetimi, sipariş alma ve anket gibi temel işlevlerini ve iş tarafının bir SFA sisteminden gerçekte ne beklemesi gerektiğini anlatır."
course: ea
category: saha-satis-ve-dms
tags: [sfa, saha-satis, rut, mukemmel-magaza, fmcg]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, saha-satis-temsilcisi, it-yoneticisi]
level: temel
source_lessons: [EA-26.1]
reading_minutes: 3
key_points:
  - "SFA, saha ekibinin ziyaret, sipariş, denetim ve tahsilat işlerini mobil cihazda yürütmesini sağlar."
  - "Rut planı hangi noktaya hangi sıklıkla ve hangi sırayla gidileceğini belirler."
  - "Mükemmel mağaza, noktadaki bulunurluk, raf, fiyat ve promosyon uyumunun puanlanmasıdır."
  - "Sistemden önce ziyaretin standart adımlarını tanımlayın."
  - "SFA'nın değeri sahadan gelen veriyle yönetimin karar alabilmesindedir."
glossary_terms: [sfa, rut-plani, mukemmel-magaza]
related: [kb-fmcg-8-10-sfa-data-driven-selling, kb-fmcg-8-2-structured-sales-call, kb-ea-26-2-field-data-outlet-visit, kb-ea-26-3-offline-mode-for-managers, kb-ea-40-4-integrating-sfa-with-erp]
sources:
  - title: "A Strategic Framework for Customer Relationship Management"
    authors: "Payne, A.; Frow, P."
    year: 2005
    type: article
    doi: "10.1509/jmkg.2005.69.4.167"
    url: "https://doi.org/10.1509/jmkg.2005.69.4.167"
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

Bir üretici ya da distribütör, satış temsilcilerinin her gün onlarca noktayı ziyaret ettiğini bilir; ama hangi noktada ne yapıldığını çoğu zaman göremez. **Saha satış otomasyonu** (SFA), bu görünürlüğü sağlar. Bu kart, iş tarafının bir SFA'dan ne beklemesi gerektiğini anlatır.

## Temel fikir

Hızlı tüketim sektöründe SFA'nın temel işlevleri:

- **Rut ve ziyaret planı:** Hangi noktaya hangi gün, hangi sıklıkla gidileceği. Noktalar ciro potansiyeline göre sınıflandırılır (ör. A noktaları haftada iki kez).
- **Ziyaret akışı:** Giriş (konum doğrulama), stok ve raf kontrolü, sipariş, tahsilat, anket ve çıkış.
- **Mükemmel mağaza denetimi:** Noktada olması gereken ürünlerin bulunurluğu, raf düzeni (planogram), fiyat etiketi ve promosyon materyali kontrol edilir ve puanlanır.
- **Sipariş alma:** Önerilen sipariş, fiyat ve iskonto bilgisi, kredi limiti kontrolü.
- **Anket ve fotoğraf:** Rakip faaliyeti, raf fotoğrafı, soğutucu durumu.
- **Raporlama:** Ziyaret uyumu, sipariş başarısı, mükemmel mağaza puanı.

Payne ve Frow'un CRM çerçevesi açısından SFA, operasyonel CRM'in sahadaki yüzüdür ve çok kanallı müşteri bilgisinin önemli bir kaynağıdır.

Başarılı projelerde önce ziyaretin **standart adımları** tanımlanır, sonra sistem bu adımlara göre kurulur. Aksi halde SFA, eski kâğıt formların elektronik kopyasına dönüşür.

### SFA'nın benimsenmesini sağlamak

Saha satış otomasyonunun değeri, temsilcilerin sistemi her ziyarette gerçekten kullanmasına bağlıdır. Benimsemeyi artırmak için şu yaklaşımlar önerilir:

- **Temsilciye fayda sağlayın:** Uygulama, temsilcinin işini kolaylaştırmalıdır: müşterinin son siparişleri, açık bakiyesi, aktif kampanyalar ve önerilen sipariş tek ekranda görünmelidir. Yalnızca yönetime veri toplamak için tasarlanmış bir uygulama, kısa sürede formalite hâline gelir.
- **Ziyaret akışını kısa tutun:** Her ziyarette doldurulması gereken anket ve denetim adımları sınırlı tutulmalıdır. Uzun formlar, ziyaret sayısını düşürür ve rastgele doldurulan cevaplara yol açar.
- **Çevrimdışı çalışma:** Bağlantının zayıf olduğu bölgelerde de sipariş alınabilmeli, veriler bağlantı geldiğinde otomatik gönderilmelidir.
- **Pilot ve geri bildirim:** Uygulama, önce küçük bir ekiple denenmeli ve temsilcilerin geri bildirimleriyle iyileştirilmelidir. Saha ekibinden seçilen öncü kullanıcılar, yaygınlaştırmada diğer temsilcilere destek olabilir.

**Yöneticinin rolü.** Bölge yöneticileri, toplantılarda ve saha ziyaretlerinde uygulamadaki verileri kullanmalıdır. Yöneticiler eski tablolarla çalışmaya devam ederse, temsilciler de uygulamayı ciddiye almaz.

**Veri kullanımı.** Toplanan ziyaret, sipariş ve denetim verileri, temsilcilere geri bildirim olarak dönmelidir: hangi noktalarda dağıtım eksik, hangi ürünlerde fırsat var? Payne ve Frow'un vurguladığı gibi, müşteri bilgisinin değeri, ilişkiyi geliştirmek için kullanıldığında ortaya çıkar.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b6.py` ile yapılmıştır.

Bir distribütör mükemmel mağaza puanını dört kritere göre hesaplıyor:

- Bulunurluk (ağırlık %40): 90 puan
- Raf düzeni (%25): 80 puan
- Fiyat etiketi (%20): 100 puan
- Promosyon materyali (%15): 60 puan

Noktanın toplam puanı **85,0**. Aynı gün temsilci planlanan 22 ziyaretin 19'unu yapmış; ziyaret uyumu **%86,4**. Bölge müdürü, promosyon materyali puanının düşük olduğu noktaları bir sonraki hafta için öncelikli listeye alıyor.

## Sık yapılan hatalar

- SFA'yı yalnızca sipariş alma aracı olarak kullanmak.
- Ziyaret formunu çok uzun tutup temsilcinin zamanını yemek.
- Sahadan gelen veriyi kimsenin analiz etmemesi.
- Rut planını nokta potansiyeline göre değil alışkanlığa göre yapmak.

## Pratikte nasıl uygulanır?

- [ ] Standart ziyaret adımlarını ve süresini belirleyin.
- [ ] Mükemmel mağaza kriterlerini en fazla 4–6 maddeyle sınırlayın.
- [ ] Noktaları potansiyele göre sınıflandırıp ziyaret sıklığını buna bağlayın.
- [ ] Haftalık saha toplantılarında SFA raporlarını kullanın.

## Daha fazlası

- Payne ve Frow (2005), *Journal of Marketing*. https://doi.org/10.1509/jmkg.2005.69.4.167
