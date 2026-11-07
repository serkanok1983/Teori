---
id: kb-fmcg-9-5-perfect-store
title: "Mükemmel mağaza: Mağaza içi uygulamayı tek puanla yönetmek"
summary: "Mükemmel mağaza, bir üreticinin mağaza içinde görmek istediği uygulama standartlarının tanımlanması ve puanlanmasıdır. Bu kart standartların seçimini, ağırlıklandırmayı, puan hesabını ve puanın saha yönetiminde nasıl kullanılacağını anlatır."
course: fmcg
category: perakende-uygulama
tags: [perakende, saha-satis, uygulama]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, saha-satis-temsilcisi]
level: temel
source_lessons: [FMCG-9.5]
reading_minutes: 3
key_points:
  - "Mükemmel mağaza; bulunurluk, raf payı, fiyat, teşhir ve planogram gibi standartların birlikte tanımlanmasıdır."
  - "Her standart, satışa etkisine göre ağırlıklandırılır ve ağırlıklı ortalama tek bir puan verir."
  - "Standartlar format ve nokta tipine göre farklı olmalıdır; bakkal ile hipermarket aynı ölçütlerle değerlendirilmez."
  - "Puan, ancak satışla ilişkisi gösterilebildiğinde ve temsilcinin aksiyon alabildiği bir araç olduğunda değerlidir."
glossary_terms: [mukemmel-magaza, zorunlu-urun-listesi, raf-payi, planogram, raf-bulunurlugu]
related: [kb-fmcg-9-3-shelf-space-planogram, kb-fmcg-9-4-osa-out-of-stock, kb-fmcg-8-10-sfa-data-driven-selling, kb-fmcg-8-7-sales-kpi-design, kb-fmcg-9-6-trade-marketing]
sources:
  - title: "Desperately Seeking Shelf Availability: An Examination of the Extent, the Causes, and the Efforts to Address Retail Out-of-Stocks"
    authors: "Corsten, D.; Gruen, T."
    year: 2003
    type: article
    doi: "10.1108/09590550310507731"
    url: "https://doi.org/10.1108/09590550310507731"
    verified: true
    checked_on: 2026-10-28
    note: "International Journal of Retail & Distribution Management 31(12), 605–617."
  - title: "NielsenIQ"
    authors: "NielsenIQ"
    year: 2026
    type: web
    url: "https://www.nielseniq.com/"
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

Temsilci bir mağazadan çıktığında "ziyaret iyi geçti" demek yeterli değildir. Ürünler rafta mı, doğru yerde mi, fiyat etiketi doğru mu, teşhir kuruldu mu? Mükemmel mağaza (*perfect store*) yaklaşımı, bu soruları tek bir ölçülebilir standarda dönüştürür. Bu kart, kendi mükemmel mağaza puanınızı kurmanızı ve kullanmanızı sağlar. Bu yaklaşım, büyük hızlı tüketim şirketlerinde yaygın bir uygulamadır; burada anlatılan yöntem genel bir çerçevedir, belirli bir şirketin modeli değildir.

## Temel fikir

**1. Standartları seçmek.** Tipik standartlar şunlardır:

- **Bulunurluk:** Zorunlu ürün listesindeki ürünlerin rafta olması.
- **Raf payı:** Markanın raftaki payının hedefe ulaşması.
- **Fiyat etiketi:** Rafta doğru fiyat etiketinin bulunması.
- **Teşhir:** Anlaşılan ek teşhirin kurulmuş olması.
- **Planogram:** Ürünlerin plana uygun yerleştirilmesi.

Standart sayısı az tutulmalıdır. Beş-altı standart, temsilcinin her ziyarette kontrol edebileceği bir sayıdır.

**2. Ağırlık vermek.** Her standart satışa aynı ölçüde etki etmez. Genellikle bulunurluk en büyük ağırlığı alır, çünkü ürün rafta yoksa diğer standartların anlamı kalmaz. Corsten ve Gruen (2003), stoksuzluğun hem üreticiye hem perakendeciye önemli satış kaybı yaşattığını ve nedenlerin büyük kısmının mağaza süreçlerinde olduğunu özetler; bu da bulunurluğu saha ekibinin doğrudan etkileyebildiği bir standart yapar. Raf payı ve fiyat gibi standartların hedefleri ise NielsenIQ gibi perakende paneli sağlayıcılarının satış payı verileriyle karşılaştırılarak belirlenebilir. Ağırlıklar başlangıçta deneyime dayanabilir, ama zamanla puan ile satış arasındaki ilişkiye bakılarak güncellenmelidir.

**3. Puanı hesaplamak.** Her standart için gerçekleşme oranı (0 ile 1 arası) ölçülür. Puan = Σ (ağırlık × gerçekleşme) × 100.

**4. Nokta tipine göre ayarlamak.** Bir hipermarket için teşhir ve planogram önemliyken bir bakkalda soğutucu ve küçük paket bulunurluğu öne çıkar. Her nokta tipi için ayrı standart seti ve ağırlık tanımlayın.

**5. Puanı kullanmak.** Puan; temsilcinin ziyaret sonunda neyin eksik kaldığını görmesi, şefin koçluk yapacağı konuları belirlemesi ve yönetimin bölgeleri karşılaştırması için kullanılır. Prim sistemine bağlanacaksa ölçümün güvenilir olması şarttır.

## Bir örnek

> **Örnek (temsili rakamlar):** Ağırlıklar ve gerçekleşme oranları varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b5.py` ile yapılmıştır.

Bir süpermarket ziyaretinin sonuçları:

| Standart | Ağırlık | Gerçekleşme | Katkı |
|---|---|---|---|
| Bulunurluk | 0,35 | %87,5 (8 üründen 7'si) | 30,6 |
| Raf payı | 0,25 | %70 (hedefin oranı) | 17,5 |
| Fiyat etiketi | 0,15 | %100 | 15,0 |
| Teşhir | 0,15 | %50 | 7,5 |
| Planogram | 0,10 | %80 | 8,0 |
| **Toplam puan** | | | **78,6** |

Puan, temsilciye en çok neyi kazanabileceğini gösterir. Teşhiri tamamlamak 7,5 puan, raf payını hedefe çıkarmak 7,5 puan, eksik ürünü rafa koymak yaklaşık 4,4 puan kazandırır. Temsilci bir sonraki ziyarette teşhir anlaşmasını mağaza müdürüyle yeniden konuşmayı ve eksik ürünü getirmeyi planlar.

## Sık yapılan hatalar

- **Çok fazla standart.** Yirmi maddelik bir kontrol listesi, ziyareti denetime dönüştürür ve satış zamanını azaltır.
- **Ağırlıkları hiç güncellememek.** Puan ile satış arasında ilişki yoksa ağırlıklar ya da standartlar yanlıştır.
- **Her nokta tipine aynı standardı uygulamak.** Bakkal, hipermarket standardında hep düşük puan alır ve puan anlamını yitirir.
- **Ölçümü doğrulamamak.** Temsilci kendi puanını kaydediyorsa ve puan prime bağlıysa, rastgele denetimler gerekir.
- **Puanı yalnızca rapor için kullanmak.** Asıl değer, temsilcinin ve şefin aksiyonudur.

## Pratikte nasıl uygulanır?

- [ ] Her nokta tipi için en fazla altı standart seçin.
- [ ] Başlangıç ağırlıklarını belirleyin ve SFA'da kontrol listesi olarak tanımlayın.
- [ ] Temsilcinin ziyaret sonunda puanı ve eksik kalan maddeleri görmesini sağlayın.
- [ ] Üç-altı ay sonra, puanı yüksek ve düşük mağazaların satış büyümesini karşılaştırın; ağırlıkları buna göre güncelleyin.
- [ ] Rastgele mağaza denetimleriyle temsilci kayıtlarını doğrulayın.
- [ ] Puanı şef koçluğunun ve bölge toplantılarının düzenli gündemi yapın.

## Daha fazlası

- Corsten, D.; Gruen, T. (2003). *Desperately Seeking Shelf Availability: An Examination of the Extent, the Causes, and the Efforts to Address Retail Out-of-Stocks.* International Journal of Retail & Distribution Management 31(12), 605–617. https://doi.org/10.1108/09590550310507731
- NielsenIQ (2026). *NielsenIQ.* https://www.nielseniq.com/
