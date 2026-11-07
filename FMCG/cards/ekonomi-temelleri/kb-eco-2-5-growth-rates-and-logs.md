---
id: kb-eco-2-5-growth-rates-and-logs
title: "Büyüme oranlarını doğru okumak: reel büyüme, bileşik oran ve logaritma"
summary: "Yüksek enflasyonda nominal büyümeden reel büyümeyi doğru hesaplamayı, aylık oranları yıllığa çevirmeyi, yıllık ortalama bileşik büyümeyi ve logaritmik değişimin pratik kullanımını anlatır."
course: eco
category: ekonomi-temelleri
tags: [analiz, enflasyon, raporlama]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [ECO-2.5]
reading_minutes: 2
key_points:
  - "Reel büyüme, nominal büyümeden enflasyonun çıkarılmasıyla değil, bölünmesiyle bulunur."
  - "Aylık oranlar yıllığa çevrilirken çarpılmaz, bileşik olarak hesaplanır."
  - "Çok yıllık büyümeyi yıllık ortalama bileşik büyüme oranıyla (CAGR) özetleyin."
  - "%50 artış ve ardından %50 düşüş başlangıç noktasına değil, daha aşağıya götürür."
  - "Logaritmik değişimler toplanabilir; bu yüzden büyümeyi bileşenlerine ayırmak kolaylaşır."
glossary_terms: [reel-buyume, cagr]
related: [kb-eco-14-1-gdp-real-nominal, kb-eco-14-2-inflation-measurement-tufe-ufe, kb-eco-32-4-finance-in-high-inflation, kb-eco-49-1-time-series-seasonality]
sources:
  - title: "The Economy 2.0"
    authors: "CORE Econ"
    year: 2026
    type: web
    url: "https://www.core-econ.org/the-economy/"
    verified: true
    checked_on: 2026-10-28
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

Enflasyonun yüksek olduğu bir ortamda "satışlarımız %65 büyüdü" cümlesi tek başına bir şey söylemez. Bu kart, satış ve maliyet raporlarındaki büyüme oranlarını doğru okumanızı, bölgeleri ve yılları adil karşılaştırmanızı ve hedef belirlerken sık yapılan hesap hatalarından kaçınmanızı sağlar.

## Temel fikir

Dört kural çoğu hatayı önler:

1. **Reel büyüme** (*real growth*) için bölün: (1 + nominal büyüme) / (1 + enflasyon) − 1. Nominal büyümeden enflasyonu çıkarmak, oranlar yüksekken ciddi hata yaratır.
2. **Aylık oranı yıllığa bileşik çevirin:** (1 + aylık oran)^12 − 1. Aylık oranı 12 ile çarpmak, yıllık artışı olduğundan düşük gösterir.
3. **Çok yıllık büyümeyi CAGR ile özetleyin:** (son değer / ilk değer)^(1/yıl sayısı) − 1. Toplam büyümeyi yıl sayısına bölmek ortalamayı şişirir.
4. **Logaritma kullanın:** Doğal logaritma farkı, ln(son/ilk), sürekli bileşik büyümeyi verir. Logaritmik değişimler toplanabilir: Nominal büyümenin logaritması, fiyat etkisinin logaritması ile reel etkinin logaritmasının toplamıdır.

Bir de asimetriye dikkat edin: Bir değer önce yüzde x artıp sonra yüzde x düşerse başlangıç noktasının altına iner.

## Bir örnek

> **Örnek (temsili rakamlar):** Bir bayinin ciro ve enflasyon rakamları varsayımsaldır; gerçek enflasyon verisini temsil etmez. Hesaplar `scripts/cards_numbers_eco_b1.py` ile yapılmıştır.

**Reel büyüme.** Ciro 100.000.000 TL'den 165.000.000 TL'ye çıkmış: nominal büyüme **%65,0**. Aynı dönemde ilgili fiyat artışı %50.

- Doğru reel büyüme: 1,65 / 1,50 − 1 = **%10,0**.
- Yanlış yöntem (çıkarma): %15,0. Fark, hedef primini ve bölge sıralamasını değiştirecek kadar büyüktür.

**Aylıktan yıllığa.** Aylık %3 fiyat artışı, yılda **%42,58** eder; 12 ile çarpmak yalnızca %36 verir.

**CAGR.** Ciro üç yılda 100.000.000 TL'den 300.000.000 TL'ye çıkmış. Yıllık ortalama bileşik büyüme **%44,22**; toplam artışı üçe bölmek yanlış biçimde %66,67 gösterir.

**Logaritma.** İlk örnekte ln(1,65) = 0,5008, ln(1,50) = 0,4055, ln(1,10) = 0,0953. Fiyat ve reel etki toplamı nominal etkiye eşittir; böylece büyümeyi fiyat, hacim ve karma etkilerine ayırabilirsiniz.

**Asimetri.** %50 artıp sonra %50 düşen bir değer, başlangıca göre **−%25** noktasındadır.

**Kural.** Aylık %3 büyüyen bir değer yaklaşık 23,4 ayda ikiye katlanır.

## Sık yapılan hatalar

- Bölgeleri nominal büyümeye göre sıralamak; farklı ürün karmasının farklı fiyat artışı taşıdığını gözden kaçırmak.
- Genel enflasyonu kullanıp kendi ürün grubunuzun fiyat artışını hesaba katmamak.
- Aylık hedefleri yıllık hedefin on ikide biri olarak dağıtmak.
- Düşük bir tabandan gelen yüksek yüzde artışları başarı göstergesi saymak.
- Yüzde ile yüzde puanı karıştırmak (marj %12'den %15'e çıktıysa artış 3 puandır, %25 değildir).

## Pratikte nasıl uygulanır?

- [ ] Satış raporlarına nominal büyümenin yanında kendi fiyat artışınızla düzeltilmiş hacim büyümesini koyun.
- [ ] Hedef ve prim hesaplarında reel büyümeyi bölme yöntemiyle hesaplayın.
- [ ] Yıllık planları aya bölerken bileşik oran ve mevsimsellik katsayısı kullanın.
- [ ] Çok yıllık karşılaştırmalarda CAGR verin; toplam yüzde artışı tek başına göstermeyin.
- [ ] Ciro değişimini fiyat, hacim ve karma etkisine ayıran bir tabloyu her çeyrek güncelleyin.

## Daha fazlası

- CORE Econ (2026). *The Economy 2.0*. https://www.core-econ.org/the-economy/
- OpenStax (2026). *Introductory Statistics 2e*. https://openstax.org/books/introductory-statistics-2e/pages/1-introduction
