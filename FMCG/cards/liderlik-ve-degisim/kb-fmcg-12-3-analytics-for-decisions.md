---
id: kb-fmcg-12-3-analytics-for-decisions
title: "Karar için analitik: Doğru soruyu sormak ve etkiyi ölçmek"
summary: "Hızlı tüketimde veri çoktur, ama kararı değiştiren analiz azdır. Bu kart analizi bir karardan başlatmayı, korelasyon ile nedensellik arasındaki farkı, test ve kontrol gruplarıyla etki ölçmeyi ve belirsizliği dürüstçe raporlamayı anlatır."
course: fmcg
category: liderlik-ve-degisim
tags: [analitik, liderlik, olcum]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: orta
source_lessons: [FMCG-12.3]
reading_minutes: 3
key_points:
  - "İyi bir analiz, hangi kararın verileceği sorusuyla başlar."
  - "İki değişkenin birlikte hareket etmesi, birinin diğerine neden olduğunu göstermez."
  - "Bir uygulamanın etkisini ölçmenin en güvenilir yolu, test ve kontrol gruplarıyla yapılan kontrollü deneydir."
  - "Büyük ölçekli reklam deneyleri, gözlemsel analizlerin etkiyi önemli ölçüde abartabildiğini göstermiştir."
  - "Sonuçlar tek bir rakamla değil, güven aralığıyla raporlanmalıdır."
glossary_terms: [kontrollu-deney, artimsal-hacim, orneklem-hatasi, baz-satis]
related: [kb-fmcg-8-13-sales-analytics, kb-fmcg-5-5-trade-spend-roi, kb-fmcg-9-7-retail-media, kb-fmcg-3-8-market-research-toolkit, kb-fmcg-12-2-change-digital-transformation]
sources:
  - title: "Consumer Heterogeneity and Paid Search Effectiveness: A Large-Scale Field Experiment"
    authors: "Blake, T.; Nosko, C.; Tadelis, S."
    year: 2015
    type: article
    doi: "10.3982/ECTA12423"
    url: "https://doi.org/10.3982/ECTA12423"
    verified: true
    checked_on: 2026-10-28
    note: "Econometrica 83(1), 155–174. Crossref ile doğrulandı."
  - title: "The Unfavorable Economics of Measuring the Returns to Advertising"
    authors: "Lewis, R. A.; Rao, J. M."
    year: 2015
    type: article
    doi: "10.1093/qje/qjv023"
    url: "https://doi.org/10.1093/qje/qjv023"
    verified: true
    checked_on: 2026-10-28
    note: "Quarterly Journal of Economics 130(4), 1941–1973. Crossref ile doğrulandı."
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

Yönetim toplantısında bir sunum, mağaza içi teşhir yapılan noktaların satışının diğerlerinden %20 yüksek olduğunu gösterir ve teşhir bütçesinin artırılmasını önerir. Ama teşhir zaten en büyük ve en iyi noktalara yapılmıştır. Fark teşhirden mi, yoksa noktaların kendisinden mi geliyor? Bu kart, analizlerin bu tür tuzaklara düşmesini önlemenizi ve kararları daha sağlam bir temele oturtmanızı sağlar.

## Temel fikir

**Karardan başlamak.** Her analiz, "Bu sonuç hangi kararı değiştirecek?" sorusuyla başlamalıdır. Kararı değiştirmeyecek bir analiz, ne kadar ilginç olursa olsun, önceliksizdir.

**Korelasyon ve nedensellik.** Gözlemsel verilerde iki değişkenin birlikte hareket etmesi çoğu zaman üçüncü bir etkenden kaynaklanır. Hızlı tüketimde sık görülen örnekler:

- Teşhir ya da promosyon yapılan noktalar zaten daha büyüktür.
- Reklamı gören tüketiciler zaten ürünü almaya daha yatkındır.
- Yeni ürün lansmanı, mevsimsel bir dönemle çakışır.

**Kontrollü deney.** Bir uygulamanın etkisini ölçmenin en güvenilir yolu, benzer noktaları ya da tüketicileri rastgele test ve kontrol gruplarına ayırmak ve aradaki farkı ölçmektir (*controlled experiment*). Blake, Nosko ve Tadelis, büyük bir çevrim içi pazaryerinde yaptıkları saha deneyinde, gözlemsel analizlerin arama reklamlarının etkisini önemli ölçüde abarttığını gösterdi. Lewis ve Rao ise reklam etkisinin, satışlardaki doğal dalgalanmaya göre küçük olduğu için, çok büyük örneklemlerle bile kesin olarak ölçülmesinin zor olduğunu ortaya koydu.

**Belirsizliği raporlamak.** Bir test sonucu tek bir rakam olarak değil, güven aralığıyla raporlanmalıdır. Güven aralığı sıfırı içeriyorsa, etkinin olmadığı ihtimali dışlanamaz.

**Veri kaynakları.** NielsenIQ gibi perakende paneli sağlayıcıları, mağaza ve kategori düzeyinde satış verisi sunar. İç satış verisi ile panel verisinin birlikte kullanılması, hem kendi performansınızı hem de pazardaki değişimi görmenizi sağlar.

## Bir örnek

> **Örnek (temsili rakamlar):** Artış ve standart hata varsayımdır; güven aralığı normal yaklaşımla hesaplanmıştır; hesaplar `scripts/cards_numbers_fmcg_b7.py` ile yapılmıştır.

Bir üretici, yeni bir teşhir standının etkisini ölçmek için **200** test ve **200** kontrol mağazası seçiyor. Mağazalar rastgele atanıyor. Sekiz hafta sonra test mağazalarında satış, kontrol mağazalarına göre **%3,2** daha fazla artıyor; standart hata **1,5** puan.

- %95 güven aralığı: yaklaşık **%0,26** ile **%6,14** arası.
- Aralık sıfırı içermiyor; etkinin pozitif olduğu söylenebilir, ama büyüklüğü belirsiz.

Aynı test daha az mağazayla yapılsaydı ve standart hata **2,0** puan olsaydı, aralık **−%0,72** ile **%7,12** arasında olurdu. Bu durumda etkinin sıfır olma ihtimali dışlanamazdı. Bu nedenle test tasarlanırken yeterli sayıda mağaza seçilmesi gerekir.

Karar için bir sonraki soru, %0,26 ile %6,14 arasındaki bir artışın stand maliyetini karşılayıp karşılamadığıdır. Alt sınırda bile kârlıysa yaygınlaştırma kolay bir karardır; değilse daha büyük bir test gerekebilir.

## Sık yapılan hatalar

- **Analize veriyle başlamak.** Önce karar ve soru belirlenmelidir.
- **Seçilmiş noktaları ortalamayla karşılaştırmak.** Bu, etkiyi abartır.
- **Kontrol grubu olmadan "önce-sonra" karşılaştırması yapmak.** Mevsim ve pazar etkileri karışır.
- **Tek bir rakam raporlamak.** Belirsizlik gizlenir.
- **Küçük örneklemle kesin sonuç çıkarmak.** Gürültü, etki gibi görünebilir.

## Pratikte nasıl uygulanır?

- [ ] Her analiz talebinde önce "hangi karar?" sorusunu yazılı olarak yanıtlayın.
- [ ] Önemli bütçe kararları için test ve kontrol gruplarıyla pilot uygulama yapın.
- [ ] Mağazaları test ve kontrol gruplarına rastgele ya da eşleştirerek atayın.
- [ ] Sonuçları güven aralığıyla raporlayın ve kararı alt sınıra göre de değerlendirin.
- [ ] Test sonuçlarını bir arşivde toplayın; benzer kararlar için referans olarak kullanın.

## Daha fazlası

- Blake, T.; Nosko, C.; Tadelis, S. (2015). *Consumer Heterogeneity and Paid Search Effectiveness: A Large-Scale Field Experiment.* Econometrica 83(1), 155–174. Crossref ile doğrulandı. https://doi.org/10.3982/ECTA12423
- Lewis, R. A.; Rao, J. M. (2015). *The Unfavorable Economics of Measuring the Returns to Advertising.* Quarterly Journal of Economics 130(4), 1941–1973. Crossref ile doğrulandı. https://doi.org/10.1093/qje/qjv023
- NielsenIQ (2026). *NielsenIQ.* https://www.nielseniq.com/
