---
id: kb-eco-7-5-auctions-tenders
title: "İhale ve teklif verme: Kazandığınız ihale sizi zarara sokmasın"
summary: "Zincir, kurum ve kamu ihalelerinde teklif fiyatını tam maliyet üzerinden kurmayı, kazananın lanetini ve teklif kurallarının (kapalı zarf, açık eksiltme) stratejiyi nasıl değiştirdiğini anlatır."
course: eco
category: ekonomi-temelleri
tags: [ihale, fiyatlama, kilit-musteri]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [ECO-7.5]
reading_minutes: 3
key_points:
  - "Teklif fiyatının tabanı, ürün maliyeti değil; lojistik, iade, ek iskonto ve finansman dahil tam hizmet maliyetidir."
  - "Çok teklifçili ihalede kazanan, çoğu zaman maliyeti en iyimser tahmin eden firmadır (kazananın laneti)."
  - "Kapalı zarf ihalede teklifinizi kendi değerlemenizin biraz altında, açık eksiltmede ise tam maliyet sınırınızda tutun."
  - "Teklif öncesi bir 'yürüyüp gitme' fiyatı belirleyin ve bunu yazılı hâle getirin."
glossary_terms: [kazananin-laneti, hizmet-maliyeti]
related: [kb-eco-7-1-game-theory-for-managers, kb-fmcg-10-4-negotiating-with-chains, kb-fmcg-6-3-cost-to-serve, kb-ea-17-4-vendor-selection-rfp]
sources:
  - title: "Counterspeculation, Auctions, and Competitive Sealed Tenders"
    authors: "Vickrey, W."
    year: 1961
    type: article
    doi: "10.1111/j.1540-6261.1961.tb02789.x"
    url: "https://doi.org/10.1111/j.1540-6261.1961.tb02789.x"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Finance 16(1)."
  - title: "Principles of Economics 3e, §3.1 Demand, Supply, and Equilibrium in Markets for Goods and Services"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-economics-3e/pages/3-1-demand-supply-and-equilibrium-in-markets-for-goods-and-services"
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

Zincir marketlerin yıllık listeleme ihaleleri, kurumsal yemek şirketlerinin tedarik ihaleleri ya da kamu alımları, distribütör ve üretici için büyük hacim fırsatıdır. Ama ihaleyi kazanmak, kârlı iş kazanmak demek değildir. Bu kart, teklif fiyatınızı nasıl kuracağınızı ve hangi durumda masadan kalkmanız gerektiğini anlatır.

## Temel fikir

**İhale türleri** stratejiyi değiştirir:

- **Açık eksiltme:** Teklifler görünür, fiyat adım adım düşer. Doğru strateji, tam maliyet sınırınıza kadar kalıp orada durmaktır.
- **Kapalı zarf, en düşük fiyat kazanır:** Herkes tek teklif verir. Burada teklifinizi değerlemenize göre ayarlarsınız; çok agresif teklif kârı sıfırlar, çok yüksek teklif işi kaybettirir.
- **İkinci fiyat kuralı:** Vickrey (1961), kazananın ikinci en iyi teklif üzerinden ödeme aldığı kapalı ihalede herkesin gerçek değerlemesini teklif etmesinin en iyi strateji olduğunu gösterdi. Bu kural pratikte nadirdir ama gerçek değerlemenizi bilmenin önemini vurgular.

**Kazananın laneti** (*winner's curse*): İşin maliyeti herkes için benzer ama belirsizse (iade oranı, zincirin ek talepleri, ödeme gecikmesi), en düşük teklifi veren genellikle maliyeti en düşük tahmin edendir. Kazandığınızda, "neden kazandım?" sorusunu sorun.

Teklif tabanınız **tam hizmet maliyeti** (*cost-to-serve*) olmalıdır: ürün maliyeti, lojistik, beklenen iade ve fire, sözleşmede gizli ek iskontolar (listeleme, ciro primi, raf bedeli) ve uzun vadenin finansman maliyeti.

## Bir örnek

> **Örnek (temsili rakamlar):** Bir zincirin yıllık 50.000 kolilik ihalesine teklif veren distribütörün maliyetleri varsayımsaldır; finansman oranı örnek amaçlıdır. Hesaplar `scripts/cards_numbers_eco_b1.py` ile yapılmıştır.

**Koli başına maliyet katmanları:**

- Ürün 78 TL + lojistik 4 TL = görünen maliyet **82,00 TL**.
- İade ve fire 1,50 TL + sözleşmedeki ek iskontolar 1,50 TL = **85,00 TL**.
- 90 gün vadenin finansman maliyeti (yıllık %45 örnek oranla) 9,43 TL = tam maliyet **94,43 TL**.

**Teklif senaryoları:**

| Teklif (TL/koli) | Koli başı sonuç (TL) | Yıllık sonuç (TL) |
|---|---|---|
| 88 | -6,43 | -321.575 |
| 92 | -2,43 | -121.575 |
| 96 | 1,57 | 78.425 |

Görünen maliyete bakan biri 88 TL'yi kârlı sanar. Tam maliyete bakınca 88 ve 92 TL teklifleri zarar yazar. Rakip 88 TL veriyorsa, ihaleyi kaybetmek doğru karar olabilir.

## Sık yapılan hatalar

- Teklifi ürün maliyeti artı sabit bir marjla kurmak; vade ve gizli iskontoları unutmak.
- İhaleyi kaybetmemek için son dakikada tabanın altına inmek.
- Sözleşme ekindeki ciro primi, listeleme bedeli ve ceza maddelerini teklif hesabına katmamak.
- Yüksek enflasyonda sabit fiyatlı uzun dönem teklif vermek; fiyat güncelleme maddesi istememek.
- Kamu ihalelerinde şartname ve başvuru kurallarını uzmana kontrol ettirmeden teklif vermek.
- İhale şartnamesindeki ceza, teminat ve fiyat farkı maddelerini teklif fiyatına yansıtmamak.

## Pratikte nasıl uygulanır?

- [ ] Her ihale için koli başı tam maliyet tablosunu (ürün, lojistik, iade, ek iskonto, finansman) standart bir şablonla hazırlayın.
- [ ] Teklif öncesi yazılı bir "en düşük kabul edilebilir fiyat" belirleyin ve onay yetkisini tanımlayın.
- [ ] Kazanılan ihalelerin gerçekleşen maliyetini ilk 3 ayda tekrar hesaplayın; tahmin hatalarını sonraki tekliflere yansıtın.
- [ ] Uzun vadeli tekliflerde fiyatı bir maliyet endeksine ya da kura bağlayan güncelleme maddesi önerin.
- [ ] Kaybedilen ihalelerde kazanan fiyatı öğrenebiliyorsanız kayda geçirin; pazarın fiyat tabanını izleyin.
- [ ] Kazanılan ve kaybedilen ihalelerin teklif fiyatlarını kaydedip rakiplerin fiyat davranışını analiz edin.

## Daha fazlası

- Vickrey, W. (1961). *Counterspeculation, Auctions, and Competitive Sealed Tenders*. https://doi.org/10.1111/j.1540-6261.1961.tb02789.x
- OpenStax (2026). *Principles of Economics 3e, §3.1 Demand, Supply, and Equilibrium in Markets for Goods and Services*. https://openstax.org/books/principles-economics-3e/pages/3-1-demand-supply-and-equilibrium-in-markets-for-goods-and-services
