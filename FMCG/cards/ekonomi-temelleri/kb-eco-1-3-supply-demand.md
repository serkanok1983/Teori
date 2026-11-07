---
id: kb-eco-1-3-supply-demand
title: "Arz ve talep: Fiyat neden ve ne kadar değişir?"
summary: "Talep ve arzın fiyatı nasıl belirlediğini, talep artışı ile maliyet artışının fiyat ve hacme farklı etkilerini ve maliyet artışının ne kadarının fiyata yansıyabileceğini sade bir örnekle anlatır."
course: eco
category: ekonomi-temelleri
tags: [fiyatlama, talep, maliyet]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: temel
source_lessons: [ECO-1.3]
reading_minutes: 3
key_points:
  - "Piyasa fiyatı, alıcıların almak istediği miktar ile satıcıların satmak istediği miktarın eşitlendiği noktada oluşur."
  - "Talep artışı hem fiyatı hem satılan miktarı artırır; maliyet artışı fiyatı artırırken miktarı düşürür."
  - "Maliyet artışının fiyata ne kadar yansıyacağı, alıcıların ve satıcıların fiyata ne kadar duyarlı olduğuna bağlıdır."
  - "Fiyat hareketini yorumlamadan önce, değişimin talep tarafından mı yoksa arz tarafından mı geldiğini ayırın."
glossary_terms: [talep-esnekligi, piyasa-dengesi]
related: [kb-eco-1-5-price-controls-tax-incidence, kb-fmcg-5-1-price-elasticity, kb-eco-19-3-supply-shocks-cost-inflation, kb-fmcg-5-6-pricing-in-high-inflation]
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

Hammadde zammı geldiğinde "fiyatı ne kadar artırabilirim, hacim ne kadar düşer?" sorusunu sorarsınız. Bayram öncesi talep patladığında ise tersini yaşarsınız: Mal azalır, fiyat yükselir. Bu kart, bu iki durumu birbirinden ayırmanızı ve maliyet artışının fiyata ne ölçüde aktarılabileceğini kabaca tahmin etmenizi sağlar.

## Temel fikir

**Talep**, belli bir fiyatta alıcıların almak istediği miktardır; fiyat yükseldikçe istenen miktar düşer. **Arz**, belli bir fiyatta satıcıların satmak istediği miktardır; fiyat yükseldikçe sunulan miktar artar. İki eğrinin kesiştiği yer **piyasa dengesidir** (*market equilibrium*): Bu fiyatta ne kıtlık ne de fazla mal kalır.

Fiyatı hareket ettiren iki farklı şok vardır:

- **Talep şoku:** Mevsim, nüfus, gelir artışı ya da bir kampanya nedeniyle aynı fiyattan daha çok alıcı çıkar. Fiyat da miktar da artar.
- **Arz (maliyet) şoku:** Hammadde, enerji, kur ya da ücret artışı nedeniyle satıcılar aynı miktarı ancak daha yüksek fiyattan sunar. Fiyat artar, miktar düşer.

Maliyet artışının fiyata **yansıma oranı** (*pass-through*), iki tarafın fiyat duyarlılığına bağlıdır. Alıcılar fiyata çok duyarlıysa (rakip ürün, özel marka bolsa) artışın büyük kısmını satıcı üstlenir. Alıcılar az duyarlıysa (vazgeçilmez ürün, güçlü marka) artışın büyük kısmı rafa yansır. Bu duyarlılığın ölçüsüne **talep esnekliği** (*price elasticity of demand*) denir.

## Bir örnek

> **Örnek (temsili rakamlar):** Bir bölgedeki bir ürün için doğrusal talep ve arz varsayılmıştır; rakamlar `scripts/cards_numbers_eco_b1.py` ile hesaplanmıştır.

Aylık talep: Miktar = 10.000 − 40 × Fiyat. Aylık arz: Miktar = −2.000 + 60 × Fiyat.

**Adım 1 — Başlangıç dengesi.** İki denklemi eşitleyince fiyat **120 TL**, miktar **5.200 koli** olur. Ciro 624.000 TL.

**Adım 2 — Talep artışı.** Bayram etkisiyle her fiyatta 1.000 koli daha fazla talep oluşursa (10.000 yerine 11.000), yeni denge **130 TL** ve **5.800 koli** olur. Fiyat ve miktar birlikte artar.

**Adım 3 — Maliyet artışı.** Talep eski hâlindeyken satıcıların koli başı maliyeti 10 TL artarsa, arz eğrisi 10 TL yukarı kayar. Yeni denge **126 TL** ve **4.960 koli** olur.

- 10 TL'lik maliyet artışının **6 TL**'si fiyata yansır: yansıma oranı **%60**.
- Kalan kısım satıcının marjından çıkar.
- Ciro 624.960 TL ile neredeyse aynı kalır; ama satılan koli sayısı düşer ve birim marj daralır.

Bu örnekte yansıma oranı, arz eğiminin (60) toplam eğime (40 + 60) oranına eşittir. Gerçekte bu eğimleri bilmezsiniz; geçmiş fiyat değişikliklerine verilen hacim tepkisinden kabaca tahmin edersiniz.

## Sık yapılan hatalar

- Fiyat ve hacmin birlikte arttığı bir dönemi "fiyat artırınca satış artıyor" diye yorumlamak; oysa artış talepten gelir.
- Maliyet artışının tamamının fiyata aktarılabileceğini varsaymak.
- Yalnızca ciroya bakmak; ciro sabit kalırken hacim ve marj düşebilir.
- Rakiplerin aynı maliyet artışını yaşadığını unutup fiyat kararını tek başına vermek.
- Talep artışını kalıcı sanıp stok ve kapasiteyi buna göre büyütmek.

## Pratikte nasıl uygulanır?

- [ ] Her fiyat değişikliğinden önce ve sonra 8–12 haftalık hacim verisini kanal ve ürün bazında karşılaştırın.
- [ ] Hacimdeki değişimin kaynağını (mevsim, kampanya, rakip, fiyat) ayrı ayrı not edin.
- [ ] Maliyet artışında önce rakip ve özel marka fiyatlarını kontrol edin; yansıma oranını buna göre tahmin edin.
- [ ] Bayi yöneticisi olarak, üretici zammını hangi müşteri grubuna ne ölçüde yansıtabileceğinizi segment bazında planlayın.
- [ ] Talep zirvelerini (bayram, okul açılışı) geçici kabul edin; kapasite kararını ortalama talebe göre verin.

## Daha fazlası

- OpenStax (2026). *Principles of Economics 3e, §3.1 Demand, Supply, and Equilibrium in Markets for Goods and Services*. https://openstax.org/books/principles-economics-3e/pages/3-1-demand-supply-and-equilibrium-in-markets-for-goods-and-services
- CORE Econ (2026). *The Economy 2.0*. https://www.core-econ.org/the-economy/
