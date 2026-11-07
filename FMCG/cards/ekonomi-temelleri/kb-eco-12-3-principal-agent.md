---
id: kb-eco-12-3-principal-agent
title: "Asil–vekil sorunu: Prim sistemi neden yanlış davranışı ödüllendirebilir?"
summary: "İşveren ile çalışan, üretici ile bayi arasındaki çıkar farkını, ölçülen şeyin ödüllendirilen şey olduğunu ve satış primini kâr ve tahsilatla uyumlu hâle getirmeyi anlatır."
course: eco
category: ekonomi-temelleri
tags: [prim, tesvik, yonetisim, satis-yonetimi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: orta
source_lessons: [ECO-12.3]
reading_minutes: 3
key_points:
  - "İşi yapan (vekil) ile işin sahibi (asil) farklı şeyleri önemser; vekilin çabası tam gözlenemez."
  - "Prim sistemi neyi ölçüyorsa çalışan onu artırır; ciro primi kârsız ciroyu da ödüllendirir."
  - "Primi brüt kâr ve tahsilat gibi şirket sonucuna yakın göstergelere bağlamak çıkarları hizalar."
  - "Göstergeler çalışanın kontrolü dışındaki şanstan çok etkileniyorsa, risk primi yükseltir ve motivasyonu düşürür."
glossary_terms: [asil-vekil-sorunu, bilgi-asimetrisi]
related: [kb-fmcg-8-8-incentive-compensation, kb-eco-12-1-adverse-selection-credit, kb-eco-31-5-agency-governance-family-firm, kb-fmcg-8-7-sales-kpi-design]
sources:
  - title: "Theory of the firm: Managerial behavior, agency costs and ownership structure"
    authors: "Jensen, M. C.; Meckling, W. H."
    year: 1976
    type: article
    doi: "10.1016/0304-405X(76)90026-X"
    url: "https://doi.org/10.1016/0304-405X(76)90026-X"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Financial Economics 3(4)."
  - title: "Moral Hazard and Observability"
    authors: "Holmström, B."
    year: 1979
    type: article
    doi: "10.2307/3003320"
    url: "https://doi.org/10.2307/3003320"
    verified: true
    checked_on: 2026-10-28
    note: "Bell Journal of Economics 10(1)."
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

Satış temsilcisi hedefini tutturuyor ama şirketin kârı artmıyor; bayi hacim primini alıyor ama tahsilat günleri uzuyor. Bu kart, bu tür çelişkilerin kaynağını, yani asil–vekil sorununu, ve prim sistemini şirketin çıkarıyla uyumlu hâle getirmenin yollarını anlatır.

## Temel fikir

**Asil–vekil sorunu** (*principal–agent problem*): Bir taraf (asil: işveren, üretici, şirket ortakları) bir işi başka bir tarafa (vekil: çalışan, bayi, profesyonel yönetici) yaptırır. Vekilin çıkarı asilinkinden farklıdır ve vekilin ne kadar çaba gösterdiği tam gözlenemez. Jensen ve Meckling (1976), bu farkın şirketlere getirdiği maliyetleri (izleme, teşvik ve kalan kayıplar) **vekâlet maliyeti** olarak tanımladı.

Yönetici için üç ders:

1. **Ölçtüğünüzü alırsınız.** Ciroya prim veriyorsanız düşük marjlı, yüksek iskontolu ve tahsil edilmesi zor satışlar da ödüllenir.
2. **Sonuca yakın gösterge seçin.** Brüt kâr, tahsil edilmiş satış, aktif müşteri sayısı ve dağıtım (sayısal bulunurluk) gibi göstergeler, ciroya göre şirket sonucuna daha yakındır.
3. **Gürültüyü hesaba katın.** Holmström (1979), vekilin performans ölçüsü şanstan çok etkileniyorsa, primin ağırlığının azaltılması ve çabayla ilgili ek bilgilerin kullanılması gerektiğini gösterdi. Örneğin bölgedeki pazar daralmasını hedeften arındırmak.

## Bir örnek

> **Örnek (temsili rakamlar):** Temsilcinin seçebileceği iki satış fırsatı ve prim oranları varsayımsaldır; hesaplar `scripts/cards_numbers_eco_b2.py` ile yapılmıştır.

Temsilci ay sonunda iki fırsattan yalnızca birine zaman ayırabiliyor:

- **X fırsatı:** ciro 100.000 TL, brüt marj %8: brüt kâr 8.000 TL.
- **Y fırsatı:** ciro 70.000 TL, brüt marj %18: brüt kâr 12.600 TL.

**Ciro primi (%1):** X'ten 1.000 TL, Y'den 700 TL prim. Temsilci X'i seçer; şirket Y'ye göre **4.600 TL** daha az brüt kâr elde eder.

**Brüt kâr primi (%8):** X'ten 640 TL, Y'den 1.008 TL prim. Temsilci Y'yi seçer; şirketin ve temsilcinin çıkarı örtüşür.

Primin bir kısmını tahsilata bağlamak (ör. vadesinde tahsil edilmeyen satışın primini tahsilata kadar bekletmek) ikinci bir sapmayı, riskli müşteriye satışı da sınırlar.

## Sık yapılan hatalar

- Tek bir göstergeye (genellikle ciro veya koli) prim bağlamak.
- Hedefleri geçmiş yılın üstüne sabit bir oran ekleyerek koymak; bölge koşullarını hesaba katmamak.
- Prim sistemini sık değiştirmek; çalışanın güvenini kaybetmek.
- Ay sonu yüklemesini (bayiye fazla mal basma) fark etmemek; bu, bir sonraki ayın satışını çalar.
- Profesyonel yöneticiye yalnızca kısa vadeli kâr primi verip uzun vadeli yatırımları ihmal etmesine yol açmak.
- Prim sistemini bir kez kurup yıllarca güncellememek; satış ekibi zamanla sistemin açıklarını öğrenir.

## Pratikte nasıl uygulanır?

- [ ] Mevcut prim sisteminin hangi davranışları ödüllendirdiğini bir tabloya yazın; istenmeyenleri işaretleyin.
- [ ] Primi en az iki göstergeye bağlayın: biri kâr (brüt kâr veya katkı), biri tahsilat veya müşteri sağlığı.
- [ ] Bölge hedeflerini pazar büyüklüğü ve potansiyeline göre ayarlayın.
- [ ] Ay sonu satış yoğunlaşmasını ve sonraki ayın ilk haftasındaki iadeleri izleyin.
- [ ] Bayi teşviklerinde de aynı ilkeyi uygulayın: hacim yanında sell-out, tahsilat ve dağıtım hedefleri koyun.
- [ ] Prim sistemini yılda bir, istenmeyen davranışlara yol açıp açmadığı açısından gözden geçirin.

## Daha fazlası

- Jensen, M. C.; Meckling, W. H. (1976). *Theory of the firm: Managerial behavior, agency costs and ownership structure*. https://doi.org/10.1016/0304-405X(76)90026-X
- Holmström, B. (1979). *Moral Hazard and Observability*. https://doi.org/10.2307/3003320
- OpenStax (2026). *Principles of Economics 3e, §3.1 Demand, Supply, and Equilibrium in Markets for Goods and Services*. https://openstax.org/books/principles-economics-3e/pages/3-1-demand-supply-and-equilibrium-in-markets-for-goods-and-services
