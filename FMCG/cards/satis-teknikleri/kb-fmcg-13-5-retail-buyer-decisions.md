---
id: kb-fmcg-13-5-retail-buyer-decisions
title: "Perakende alıcısı yeni ürünü neye göre listeler?"
summary: "Zincir perakendecilerin alıcıları her yıl çok sayıda yeni ürün teklifi alır ve sınırlı raf alanını en verimli ürünlere ayırmaya çalışır. Bu kart, alıcının listeleme kararında baktığı ölçütleri ve teklifinizi bu ölçütlere göre nasıl hazırlayacağınızı anlatır."
course: fmcg
category: satis-teknikleri
tags: [satis-teknikleri, perakende, listeleme]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, saha-satis-temsilcisi]
level: temel
source_lessons: [FMCG-13.5]
reading_minutes: 3
key_points:
  - "Alıcı, yeni ürünü raf alanının fırsat maliyetine göre değerlendirir."
  - "Montgomery'nin 1975 çalışması, süpermarket alıcılarının yeni ürün kararlarını etkileyen etkenleri inceleyen erken ve önemli bir çalışmadır."
  - "Alıcı için önemli ölçütler; kategori büyümesi, marj, metre başına satış, pazarlama desteği, tedarikçi güvenilirliği ve ürünün yeniliğidir."
  - "Teklif, ürünün kategoriye ne kattığını göstermelidir; yalnızca kendi satışını değil."
  - "Listeleme kararı, ürünün raftan neyi çıkaracağı sorusunu da içerir."
glossary_terms: [kategori-yonetimi, raf-payi, talep-transferi, katki-payi, artimsal-hacim]
related: [kb-fmcg-13-4-b2b-buying-behaviour, kb-fmcg-13-2-strategic-selling, kb-fmcg-9-1-retailer-economics, kb-fmcg-9-3-shelf-space-planogram, kb-fmcg-10-1-key-account-management]
sources:
  - title: "New Product Distribution: An Analysis of Supermarket Buyer Decisions"
    authors: "Montgomery, D. B."
    year: 1975
    type: article
    doi: "10.1177/002224377501200301"
    url: "https://doi.org/10.1177/002224377501200301"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Marketing Research 12(3), 255–264."
  - title: "A General Model for Understanding Organizational Buying Behavior"
    authors: "Webster, F. E.; Wind, Y."
    year: 1972
    type: article
    doi: "10.1177/002224297203600204"
    url: "https://doi.org/10.1177/002224297203600204"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Marketing 36(2), 12–19."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Bir zincir alıcısı, aynı hafta içinde birçok tedarikçiden yeni ürün teklifi alır. Rafta yer sınırlıdır; yeni bir ürünün girmesi, çoğu zaman başka bir ürünün çıkması demektir. Bu kart, alıcının bakış açısını anlamanızı ve teklifinizi "neden bu ürün, neden şimdi, neyin yerine?" sorularına yanıt verecek şekilde hazırlamanızı sağlar.

## Temel fikir

**Alıcının sorusu.** Perakende alıcısı için temel soru şudur: Bu ürün, rafta yerini alacağı üründen daha fazla değer yaratacak mı? Değer genellikle metre başına satış, marj, kategori büyümesi ve müşteri trafiği üzerinden ölçülür.

**Araştırmadan bir bakış.** Montgomery'nin 1975'te *Journal of Marketing Research*'te yayımlanan çalışması, süpermarket alıcılarının yeni ürün kabul kararlarını etkileyen etkenleri inceleyen erken ve sık atıf yapılan bir çalışmadır. Çalışma, ürünün yeniliği, tedarikçi firmanın itibarı, reklam ve promosyon desteği ile satış sunumunun niteliği gibi etkenleri ele almıştır. Bu çalışma eski olsa da, alıcının ürünü yalnızca kendi başına değil, tedarikçinin desteği ve kategoriye katkısıyla birlikte değerlendirdiği fikri bugün de geçerlidir.

**Alıcının tipik ölçütleri.**

- **Kategori büyümesi:** Ürün yeni alışveriş yapan kitle getiriyor mu, yoksa yalnızca mevcut ürünlerden satış mı çalıyor?
- **Marj ve ticari koşullar:** Perakendecinin kazancı, primler ve ödeme koşulları
- **Metre başına satış:** Raf alanının verimliliği
- **Pazarlama desteği:** Medya, örnekleme, mağaza içi aktivite
- **Tedarikçi güvenilirliği:** Teslimat performansı, raf bulunurluğu, geçmiş lansmanların başarısı
- **Yenilik:** Ürün kategoride gerçekten farklı bir ihtiyaca mı hitap ediyor?

**Talep transferi.** Alıcı, yeni ürünün satışlarının ne kadarının kategoriye ek, ne kadarının diğer ürünlerden kayma olduğunu bilmek ister. Bu nedenle teklifin artımsal hacim tahmini içermesi önemlidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Satış, marj ve raf alanı değerleri varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b8.py` ile yapılmıştır.

Bir tedarikçi, yeni ürünü için **1,5** metre raf alanı istiyor. Ürünün haftalık **8.000 TL** satış yapması ve perakendeciye **%25** marj bırakması bekleniyor.

Metre başına haftalık perakendeci kazancı: 8.000 × %25 ÷ 1,5 = yaklaşık **1.333 TL**.

Yerini alacağı mevcut ürünün aynı alanda metre başına haftalık kazancı **1.000 TL**. Fark metre başına haftada yaklaşık **333 TL**.

Tedarikçi teklifini bu karşılaştırmayla sunuyor, satış tahmininin dayandığı test pazarı verilerini ve lansman destek planını ekliyor. Alıcı tahmini iyimser bulursa, ilk üç ay sonunda gerçekleşmeye göre değerlendirme yapılmasını öneriyor.

## Sık yapılan hatalar

- **Yalnızca ürünü anlatmak.** Alıcı kategoriye etkisini görmek ister.
- **Talep transferini yok saymak.** Yamyamlaşma hesaba katılmazsa tahmin abartılı görünür.
- **Destek planını belirsiz bırakmak.** "Reklam yapacağız" yeterli değildir; takvim ve bütçe verin.
- **Geçmiş lansmanların sonuçlarını gizlemek.** Alıcı bunları zaten bilir.
- **Hangi ürünün çıkacağını düşünmemek.** Önerinizi alıcının yerine siz hazırlayın.

## Pratikte nasıl uygulanır?

- [ ] Teklifi alıcının ölçütlerine göre yapılandırın.
- [ ] Metre başına kazanç karşılaştırmasını hazırlayın.
- [ ] Artımsal hacim ve talep transferi tahminini açıkça belirtin.
- [ ] Destek planını takvim ve bütçeyle verin.
- [ ] Lansman sonrası değerlendirme noktalarını baştan önerin.

## Daha fazlası

- Montgomery, D. B. (1975). *New Product Distribution: An Analysis of Supermarket Buyer Decisions.* Journal of Marketing Research 12(3), 255–264. https://doi.org/10.1177/002224377501200301
- Webster, F. E.; Wind, Y. (1972). *A General Model for Understanding Organizational Buying Behavior.* Journal of Marketing 36(2), 12–19. https://doi.org/10.1177/002224297203600204
