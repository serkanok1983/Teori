---
id: kb-ea-25-2-customer-lifetime-value
title: "Müşteri yaşam boyu değeri (CLV): Elde tutma oranı ve değer hesabı"
summary: "Müşteri yaşam boyu değerinin elde tutma oranı, müşteri başı marj ve iskonto oranından nasıl hesaplandığını, göç ve olasılık tabanlı modellerin ne zaman gerektiğini ve CLV'nin bayi ve nokta yatırımlarında nasıl kullanılabileceğini anlatır."
course: ea
category: saha-satis-ve-dms
tags: [clv, musteri-degeri, elde-tutma, analitik]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: ileri
source_lessons: [EA-25.2]
reading_minutes: 3
key_points:
  - "CLV, bir müşterinin gelecekte getireceği marjların bugünkü değeridir."
  - "Basit modelde CLV = marj × elde tutma / (1 + iskonto − elde tutma)."
  - "Elde tutma oranındaki küçük bir artış CLV'yi belirgin artırır."
  - "Müşteriler sözleşmesiz ve düzensiz alım yapıyorsa olasılık tabanlı modeller daha uygundur."
  - "Yüksek enflasyonda marj ve iskonto oranı tutarlı biçimde (nominal veya reel) seçilmelidir."
glossary_terms: [musteri-yasam-boyu-degeri, elde-tutma-orani]
related: [kb-ea-25-1-crm-basics, kb-eco-31-1-capital-budgeting, kb-ea-26-1-retail-execution-sfa]
sources:
  - title: "Modeling Customer Lifetime Value"
    authors: "Gupta, S.; Hanssens, D.; Hardie, B.; Kahn, W.; Kumar, V.; Lin, N.; Ravishanker, N.; Sriram, S."
    year: 2006
    type: article
    doi: "10.1177/1094670506293810"
    url: "https://doi.org/10.1177/1094670506293810"
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

Hangi bayiye daha fazla iskonto verilmeli, hangi noktaya soğutucu yerleştirilmeli? Bu sorular, müşterinin bugünkü cirosundan çok gelecekte getireceği değerle ilgilidir. Bu kart, **müşteri yaşam boyu değerinin** (CLV) temel mantığını anlatır.

## Temel fikir

Gupta ve arkadaşları (2006), CLV'yi bir müşterinin gelecekteki marjlarının bugünkü değeri olarak tanımlar ve farklı model ailelerini karşılaştırır.

**Basit elde tutma modeli.** Her yıl sabit bir marj (m) ve sabit bir elde tutma oranı (r) varsayılır; iskonto oranı i'dir. Marjın dönem sonunda elde edildiği varsayımıyla:

CLV = m × r / (1 + i − r)

Bu formül, sonsuza kadar süren ama her yıl r olasılıkla devam eden bir ilişkinin değerini verir.

**Göç modelleri.** Müşterinin bir dönem alım yapmayıp sonra geri dönebildiği durumlar için kullanılır. Bakkal ve market gibi düzensiz sipariş veren noktalar için daha gerçekçidir.

**Olasılık tabanlı modeller.** Sözleşmesiz ilişkilerde, müşterinin hâlâ "aktif" olup olmadığını geçmiş alım sıklığı ve son alım tarihinden tahmin eder.

**Yüksek enflasyon notu.** Marjı nominal TL ile alıyorsanız iskonto oranı da nominal olmalıdır; reel marj kullanıyorsanız reel oran seçin. İkisini karıştırmak sonucu ciddi biçimde bozar.

### CLV'yi kararlarda kullanmak

Müşteri yaşam boyu değeri, tek başına bir rapor rakamı olarak kaldığında sınırlı fayda sağlar. Değeri, kararlara girdi olarak kullanıldığında ortaya çıkar:

- **Müşteri edinme bütçesi:** Yeni bir müşteri kazanmak için harcanabilecek tutarın üst sınırı, o müşteri segmentinin beklenen değerine göre belirlenebilir. Değeri düşük segmentlerde pahalı edinme kampanyaları kârsız olabilir.
- **Hizmet seviyesi farklılaştırma:** Yüksek değerli müşterilere daha sık ziyaret, öncelikli teslimat veya özel destek sunmak, elde tutma oranını artırabilir.
- **Elde tutma girişimleri:** Kayıp riski yüksek ve değeri büyük müşteriler, erken uyarı listeleriyle belirlenebilir. Sipariş sıklığının düşmesi veya ürün çeşitliliğinin azalması, kayıp riskinin işaretleri olabilir.
- **Kredi kararları:** Müşterinin uzun vadeli değeri, kredi limiti ve vade kararlarında risk ile birlikte değerlendirilebilir.

**Hesaplamada dikkat edilecekler.** CLV hesabı, ciro yerine katkı payına dayanmalıdır: iskontolar, promosyonlar, lojistik maliyeti ve hizmet maliyeti düşülmelidir. Aksi hâlde yüksek ciro getiren ancak kârsız müşteriler değerli görünebilir.

**Varsayımların gözden geçirilmesi.** Elde tutma oranı ve iskonto oranı gibi varsayımlar, sonucu büyük ölçüde etkiler. Bu varsayımlar düzenli olarak gerçekleşen verilerle güncellenmeli ve rakamlar kesin değerler olarak değil, karşılaştırma aracı olarak sunulmalıdır. Gupta ve arkadaşları, farklı modelleme yaklaşımlarının güçlü ve zayıf yönlerini ayrıntılı olarak tartışır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b5.py` ile yapılmıştır.

Bir üretici, bir market noktasından yılda 1.000 TL marj elde ediyor. Nominal iskonto oranı %30.

- Elde tutma oranı %80 iken CLV: **1.600,00 TL**
- Elde tutma oranı %85'e çıkarsa CLV: **1.888,89 TL**

Elde tutmadaki 5 puanlık iyileşme CLV'yi **%18,1** artırıyor. Firma, noktaların bir sonraki yıl kaybedilmemesi için düzenli ziyaret ve raf düzenlemesine harcayacağı tutarı bu farkla karşılaştırıyor.

## Sık yapılan hatalar

- CLV'yi ciro üzerinden hesaplamak; marj yerine.
- Tüm müşterilere tek bir elde tutma oranı uygulamak.
- Nominal marjı reel iskonto oranıyla iskonto etmek.
- CLV'yi kesin bir rakam gibi sunmak; varsayımları göstermemek.

## Pratikte nasıl uygulanır?

- [ ] Müşteri başı yıllık marjı segment bazında hesaplayın.
- [ ] Geçen yılın müşterilerinden kaçının bu yıl alım yaptığını ölçün.
- [ ] Basit formülle segment bazında CLV hesaplayın.
- [ ] Yatırım ve iskonto kararlarında CLV'yi destekleyici bir gösterge olarak kullanın.

## Daha fazlası

- Gupta ve ark. (2006), *Journal of Service Research*. https://doi.org/10.1177/1094670506293810
