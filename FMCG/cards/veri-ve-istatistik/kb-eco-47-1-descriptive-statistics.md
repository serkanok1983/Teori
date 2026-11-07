---
id: kb-eco-47-1-descriptive-statistics
title: "Tanımlayıcı istatistik: Ortalama, medyan ve dağılım"
summary: "Satış, sipariş ve tahsilat verilerini özetlerken ortalama, medyan, standart sapma ve uç değerlerin nasıl yorumlanacağını, tek bir uç değerin ortalamayı nasıl yanıltabileceğini anlatır."
course: eco
category: veri-ve-istatistik
tags: [istatistik, veri, raporlama]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: temel
source_lessons: [ECO-47.1]
reading_minutes: 2
key_points:
  - "Ortalama uç değerlere duyarlıdır; medyan değildir."
  - "Standart sapma, değerlerin ortalama etrafında ne kadar dağıldığını gösterir."
  - "Bir veri setini özetlerken merkez ve dağılım birlikte raporlanmalıdır."
  - "Uç değeri silmeden önce nedenini anlayın; bazen en önemli bilgi odur."
glossary_terms: [ortalama, medyan, standart-sapma, uc-deger]
related: [kb-eco-47-3-sampling-confidence, kb-eco-47-5-correlation-regression-basics, kb-eco-49-1-time-series-seasonality, kb-eco-2-5-growth-rates-and-logs]
sources:
  - title: "Introductory Statistics 2e"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/introductory-statistics-2e/pages/1-introduction"
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

Yönetim raporları "ortalama sipariş tutarı", "ortalama tahsilat süresi" gibi ölçülerle doludur. Ancak ortalama, verinin dağılımını gizleyebilir. Bu kart, birkaç temel ölçüyü birlikte kullanarak veriyi doğru özetlemenizi sağlar.

## Temel fikir

**Merkez ölçüleri:**

- **Ortalama:** Değerlerin toplamı ÷ değer sayısı.
- **Medyan:** Değerler sıralandığında ortadaki değer. Uç değerlerden etkilenmez.

**Dağılım ölçüleri:**

- **Standart sapma:** Değerlerin ortalamadan tipik uzaklığı. Büyükse veri dağınıktır.
- **Çeyrekler ve aralık:** En küçük, en büyük ve %25–%75 aralığındaki değerler.

**Uç değer:** Diğerlerinden belirgin biçimde farklı değer. Veri hatası, tek seferlik bir olay ya da ayrı bir müşteri tipi olabilir.

Ortalama ile medyan arasındaki büyük fark, verinin çarpık olduğunun veya uç değer bulunduğunun işaretidir.

### Hangi ölçüyü ne zaman kullanırsınız?

- **Sipariş tutarı, müşteri cirosu, tahsilat süresi** gibi verilerde birkaç büyük müşteri ortalamayı yukarı çeker. Tipik müşteriyi anlatmak için medyanı, toplam tutarla ilgili planlama için ortalamayı kullanın.
- **Talep planlamada** standart sapma, güvenlik stoku hesabının temel girdisidir. Ortalaması aynı olan iki üründen dalgalanması yüksek olan daha fazla güvenlik stoku gerektirir.
- **Değişim katsayısı** (standart sapma ÷ ortalama), büyüklükleri farklı ürünlerin dalgalanmasını karşılaştırmayı sağlar.

### Raporlarda dikkat

Bir yönetim raporunda yalnızca ortalamayı vermek, çoğu zaman eksik bilgi verir. Ortalamanın yanına medyanı, değer sayısını ve en küçük ile en büyük değeri ekleyin. Uç değerleri silmeden önce nedenini araştırın: Hatalı fatura girişi düzeltilmeli, ama yılda bir gelen büyük ihale siparişi gerçek bir iş olayıdır ve ayrı raporlanmalıdır. Bir histogram veya kutu grafiği, tablolardan çok daha hızlı bir biçimde çarpıklığı ve uç değerleri gösterir.

## Bir örnek

> **Örnek (temsili rakamlar):** Mağaza verileri varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b7.py` ile yapılmıştır.

Bir distribütörün bir bölgedeki 10 mağazaya haftalık satışı (bin TL): 12; 14; 15; 15; 16; 17; 18; 19; 20; 74.

- Ortalama: **22,0**
- Medyan: **16,5**
- Standart sapma: 18,4

Ortalama, 10 mağazanın 9'unun satışından yüksek. Nedeni, 74 bin TL satış yapan tek bir mağaza. Bu mağaza çıkarıldığında ortalama 16,2, standart sapma 2,5 oluyor.

Doğru yorum: "Tipik mağaza haftada yaklaşık 16,5 bin TL satıyor; bir mağaza ise ayrı bir segment gibi davranıyor." Bölge hedefi ortalamaya göre konursa mağazaların çoğu hedefin altında kalır.

## Sık yapılan hatalar

- Yalnızca ortalamayı raporlamak.
- Uç değeri nedenini araştırmadan silmek ya da hiç fark etmemek.
- Farklı büyüklükteki müşterileri tek bir ortalamada birleştirmek.
- Hedefleri çarpık dağılımlı veride ortalamaya göre belirlemek.
- Farklı sayıda gözleme dayanan ortalamaları (ör. üç siparişlik ve üç yüz siparişlik müşteri) aynı güvenle karşılaştırmak.
- Yüzde değişimlerin ortalamasını alırken bileşik etkiyi göz ardı etmek.

## Pratikte nasıl uygulanır?

- [ ] Raporlarınızda ortalamanın yanına medyanı ve standart sapmayı ekleyin.
- [ ] Ortalama ile medyan arasındaki fark büyükse veriyi grafikle inceleyin.
- [ ] Uç değerleri ayrı listeleyin ve nedenini not edin.
- [ ] Hedef ve performans karşılaştırmalarını benzer büyüklükteki gruplar içinde yapın.
- [ ] Raporlarınızda her ortalamanın yanına gözlem sayısını yazın.
- [ ] Aykırı değerleri silmek yerine bir "uç değer listesi" hâlinde ayrıca raporlayın.

## Daha fazlası

- OpenStax (2026). *Introductory Statistics 2e*. https://openstax.org/books/introductory-statistics-2e/pages/1-introduction
