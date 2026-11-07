---
id: kb-eco-5-5-economies-of-scale-sunk-costs
title: "Ölçek ekonomisi ve kapsam ekonomisi: Büyümek ne zaman ucuzlatır?"
summary: "Sabit maliyetin daha fazla hacme yayılmasıyla birim maliyetin nasıl düştüğünü, büyük depo ve ortak dağıtım kararlarında ölçek ve kapsam ekonomisinin nasıl hesaplanacağını anlatır."
course: eco
category: ekonomi-temelleri
tags: [maliyet, lojistik, strateji]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [ECO-5.5]
reading_minutes: 3
key_points:
  - "Sabit maliyeti yüksek işlerde hacim arttıkça birim maliyet düşer."
  - "Büyük kapasite, ancak yeterli hacim geldiğinde ucuzdur; düşük hacimde pahalıdır."
  - "Aynı araç, depo veya ekiple birden fazla ürün grubu taşımak kapsam ekonomisi yaratır."
  - "Kapasite yatırımından sonra o harcama batık maliyete dönüşür; kararı yatırımdan önce hacim senaryolarıyla verin."
glossary_terms: [olcek-ekonomisi, kapsam-ekonomisi, batik-maliyet, sabit-maliyet]
related: [kb-eco-1-1-opportunity-cost-sunk-cost, kb-fmcg-1-2-scale-and-concentration, kb-fmcg-6-3-cost-to-serve, kb-fmcg-11-7-warehouse-transport-network]
sources:
  - title: "Principles of Economics 3e, §3.1 Demand, Supply, and Equilibrium in Markets for Goods and Services"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-economics-3e/pages/3-1-demand-supply-and-equilibrium-in-markets-for-goods-and-services"
    verified: true
    checked_on: 2026-10-28
  - title: "The Economy 2.0"
    authors: "CORE Econ"
    year: 2026
    type: web
    url: "https://www.core-econ.org/the-economy/"
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

Distribütörlükte büyüme baskısı süreklidir: daha büyük depo, daha fazla araç, yeni üretici portföyleri. Bu kart, büyümenin birim maliyeti gerçekten düşürüp düşürmeyeceğini hesaplamanıza ve "büyük olursak ucuzlarız" varsayımını hacim rakamlarıyla sınamanıza yardım eder.

## Temel fikir

Toplam maliyet iki parçadan oluşur: **sabit maliyet** (*fixed cost*: kira, kadrolu personel, sistem lisansı) ve **değişken maliyet** (*variable cost*: elleçleme, yakıt, ambalaj). Birim maliyet = sabit maliyet / hacim + birim değişken maliyet. Hacim arttıkça sabit maliyet daha çok birime yayılır.

- **Ölçek ekonomisi** (*economies of scale*): Hacim arttıkça birim maliyetin düşmesi. Kaynakları: sabit maliyetin yayılması, toplu alım, otomasyonun ancak belli bir hacimde mantıklı hâle gelmesi.
- **Ölçek kayıpları:** Belli bir büyüklükten sonra koordinasyon, uzak rotalar ve yönetim katmanları birim maliyeti yeniden artırabilir.
- **Kapsam ekonomisi** (*economies of scope*): Birden fazla ürün grubunu aynı kaynakla taşımak, ayrı ayrı taşımaktan ucuzsa ortaya çıkar. Örneğin aynı araçla hem içecek hem atıştırmalık dağıtmak.

Yatırım yapıldıktan sonra kapasite harcaması geri alınamaz; yani batık maliyete dönüşür. Bu yüzden ölçek kararı, yatırımdan önce farklı hacim senaryolarıyla verilmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Bir distribütörün depo maliyetleri varsayımsaldır; hesaplar `scripts/cards_numbers_eco_b1.py` ile yapılmıştır.

**Mevcut depo:** Aylık sabit maliyet 1.200.000 TL, koli başı değişken maliyet 12 TL.

| Aylık hacim (koli) | Toplam maliyet (TL) | Koli başı maliyet (TL) |
|---|---|---|
| 50.000 | 1.800.000 | 36,00 |
| 100.000 | 2.400.000 | 24,00 |
| 200.000 | 3.600.000 | 18,00 |

**Büyük ve otomasyonlu depo seçeneği:** Sabit maliyet 1.800.000 TL'ye çıkar, koli başı değişken maliyet 6 TL'ye iner.

- 200.000 koli hacimde koli başı maliyet **15,00 TL** olur; mevcut depodaki 18,00 TL'ye göre koli başı **3,00 TL**, ayda **600.000 TL** tasarruf.
- Hacim 100.000 kolide kalırsa büyük depoda da koli başı maliyet **24,00 TL** olur: tasarruf sıfırlanır, üstelik yatırım geri alınamaz.

**Kapsam ekonomisi:** İki ürün grubu için ayrı araç maliyeti her biri 95.000 TL, toplam 190.000 TL. Ortak araçla ikisini birlikte taşımanın maliyeti 118.750 TL. Tasarruf **71.250 TL**.

## Sık yapılan hatalar

- Büyük depo kararını, bugün olmayan ve garanti edilmemiş hacme göre vermek.
- Ölçek ekonomisini yalnızca depo kirası üzerinden hesaplayıp rota uzunluğundaki artışı unutmak.
- Ortak dağıtımda bir ürün grubunun hizmet seviyesinin (teslim sıklığı, soğuk zincir) diğerini bozabileceğini göz ardı etmek.
- Yatırım yapıldıktan sonra kapasiteyi doldurmak için zararlı hacim almak.
- Ortalama maliyeti, ek siparişin fiyatlamasında taban olarak kullanmak.
- Büyümeyle birlikte artan koordinasyon ve yönetim maliyetlerini (ölçek dezavantajı) göz ardı etmek.

## Pratikte nasıl uygulanır?

- [ ] Depo ve filo maliyetlerinizi sabit ve değişken olarak ayırın; koli başı maliyeti aylık izleyin.
- [ ] Kapasite yatırımlarında düşük, beklenen ve yüksek hacim için koli başı maliyeti hesaplayın.
- [ ] Yeni üretici portföyü değerlendirirken mevcut araç ve depo kapasitesini ne kadar doldurduğunu (kapsam etkisi) ayrıca hesaplayın.
- [ ] Ölçek kaybı işaretlerini (rota süresi, teslim gecikmesi, yönetim katmanı) büyüme sonrası izleyin.
- [ ] Üretici olarak, distribütör bölgelerini belirlerken her bölgenin ölçek ekonomisi için yeterli hacim taşıyıp taşımadığına bakın.
- [ ] Birim maliyetlerinizi hacimle birlikte grafiğe dökün; maliyetin düşmeyi bıraktığı noktayı belirleyin.

## Daha fazlası

- OpenStax (2026). *Principles of Economics 3e, §3.1 Demand, Supply, and Equilibrium in Markets for Goods and Services*. https://openstax.org/books/principles-economics-3e/pages/3-1-demand-supply-and-equilibrium-in-markets-for-goods-and-services
- CORE Econ (2026). *The Economy 2.0*. https://www.core-econ.org/the-economy/
