---
id: kb-eco-47-5-correlation-regression-basics
title: "Korelasyon ve regresyon: İki değişken arasındaki ilişkiyi ölçmek"
summary: "Promosyon harcaması ile satış gibi iki değişken arasındaki ilişkinin korelasyon katsayısı ve basit doğrusal regresyonla nasıl ölçüleceğini, eğimin ve R²'nin nasıl yorumlanacağını ve korelasyonun nedensellik olmadığını anlatır."
course: eco
category: veri-ve-istatistik
tags: [istatistik, regresyon, analiz]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: orta
source_lessons: [ECO-47.5]
reading_minutes: 2
key_points:
  - "Korelasyon katsayısı −1 ile +1 arasında, iki değişkenin birlikte hareketinin yönünü ve gücünü gösterir."
  - "Regresyon eğimi, bağımsız değişkendeki bir birimlik artışın bağımlı değişkende ne kadar değişimle ilişkili olduğunu gösterir."
  - "R², bağımlı değişkendeki değişimin ne kadarının modelle açıklandığını gösterir."
  - "Korelasyon nedensellik değildir; ortak bir etken iki değişkeni birlikte hareket ettirebilir."
glossary_terms: [korelasyon, regresyon, belirlilik-katsayisi]
related: [kb-eco-47-1-descriptive-statistics, kb-eco-48-7-test-vs-control-did, kb-eco-49-1-time-series-seasonality, kb-eco-47-4-ab-testing-significance]
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

"Promosyona daha fazla harcarsak satış ne kadar artar?", "Fiyat artışı satış adedini ne kadar düşürür?" gibi sorular iki değişken arasındaki ilişkiyi ölçmeyi gerektirir. Bu kart, bu ilişkiyi basit araçlarla ölçmenizi ve sonuçları aşırı yorumlamaktan kaçınmanızı sağlar.

## Temel fikir

**Korelasyon katsayısı (r):** −1 ile +1 arasında değer alır. +1'e yakınsa iki değişken birlikte artar, −1'e yakınsa biri artarken diğeri azalır, 0'a yakınsa doğrusal bir ilişki yoktur.

**Basit doğrusal regresyon:** Y = a + b × X

- **b (eğim):** X'teki bir birimlik artışla Y'de beklenen değişim.
- **a (sabit):** X sıfırken Y'nin tahmini değeri.
- **R² (belirlilik katsayısı):** Y'deki değişimin modelle açıklanan payı.

**Nedensellik uyarısı:** Promosyon bütçesi genellikle satışın yüksek olacağı dönemlerde artırılır. Bu durumda yüksek korelasyonun bir kısmı mevsimsellikten kaynaklanır. Nedensellik için kontrollü deney veya fark-içinde-fark gibi yöntemler gerekir.

### Regresyonu iş kararlarında kullanmak

- **Fiyat esnekliği:** Satış miktarının logaritmasını fiyatın logaritmasına göre regresyonla tahmin ederseniz, eğim yaklaşık fiyat esnekliğini verir. Ancak fiyatın yalnızca talep düşükken indirildiği durumlarda tahmin yanlı olur.
- **Maliyet davranışı:** Depo giderlerini sipariş satırı sayısına göre regresyonla inceleyerek sabit ve değişken maliyet bileşenlerini kabaca ayırabilirsiniz.
- **Birden fazla değişken:** Çoklu regresyon, mevsim, fiyat ve promosyon gibi birden fazla etkeni aynı anda dikkate alır. Ancak birbirine çok bağlı değişkenler aynı modele girdiğinde katsayılar kararsızlaşır.

### Modeli kontrol etmek

- Artıklara, yani gerçek değer ile tahmin arasındaki farklara bakın. Belirli bir örüntü varsa (ör. hep yaz aylarında pozitif), model bir etkeni kaçırıyordur.
- Veri aralığının dışına çıkarak tahmin yapmayın. Geçmişte hiç denenmemiş bir fiyat seviyesi için regresyon tahmini güvenilir değildir.
- Yüksek R² tek başına iyi bir model anlamına gelmez; zaman serilerinde ortak eğilim, ilişkisiz değişkenler arasında bile yüksek R² üretebilir.

## Bir örnek

> **Örnek (temsili rakamlar):** Aylık veriler varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b7.py` ile yapılmıştır.

Bir üreticinin 8 aylık promosyon harcaması (bin TL): 10; 20; 30; 40; 50; 60; 70; 80. Aynı aylardaki satış (bin TL): 210; 240; 245; 280; 300; 295; 330; 350.

- Korelasyon: r = **0,98**
- Regresyon: Satış = 195,5 + 1,90 × Promosyon
- R² = %97

Yorum: Promosyon harcamasındaki her 1.000 TL'lik artış, yaklaşık 1.905 TL ek satışla **ilişkili**. Ama bu, 1.000 TL'lik harcamanın 1.905 TL satış yarattığı anlamına gelmez; yüksek harcamalı aylar zaten güçlü sezon ayları olabilir.

Ayrıca 90 bin TL harcama için model 367 bin TL satış tahmin eder, ancak bu değer gözlenen aralığın dışındadır ve dikkatle kullanılmalıdır.

## Sık yapılan hatalar

- Korelasyonu nedensellik olarak yorumlamak.
- Veri aralığının dışına çıkan tahminlere güvenmek.
- Mevsimsellik ve fiyat gibi diğer etkenleri modele katmamak.
- Az sayıda gözlemle yüksek R²'ye fazla güvenmek.
- Grafik çizmeden yalnızca katsayıya bakmak.

## Pratikte nasıl uygulanır?

- [ ] Analizden önce iki değişkenin dağılım grafiğini çizin.
- [ ] Katsayıları "ilişkili" diliyle raporlayın, "neden olur" demeyin.
- [ ] Mevsimsellik, fiyat ve dağıtım gibi etkenleri ek değişken olarak ekleyin.
- [ ] Nedensel etki önemliyse test-kontrol deneyi tasarlayın.

## Daha fazlası

- OpenStax (2026). *Introductory Statistics 2e*. https://openstax.org/books/introductory-statistics-2e/pages/1-introduction
