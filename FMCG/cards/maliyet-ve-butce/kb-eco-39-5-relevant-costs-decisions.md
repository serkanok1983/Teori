---
id: kb-eco-39-5-relevant-costs-decisions
title: "İlgili maliyetler: Özel sipariş, yap-ya da-al ve ürün bırakma kararları"
summary: "Kısa vadeli kararlarda yalnızca karardan etkilenen gelir ve maliyetlerin dikkate alınması gerektiğini, özel sipariş örneğiyle kapasite boşken ve doluyken farklı sonuçlar çıktığını anlatır."
course: eco
category: maliyet-ve-butce
tags: [maliyet, karar, fiyatlama]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: ileri
source_lessons: [ECO-39.5]
reading_minutes: 3
key_points:
  - "İlgili maliyet, kararla birlikte değişen gelecekteki maliyettir."
  - "Dağıtılmış sabit giderler ve batık maliyetler çoğu kısa vadeli kararda ilgisizdir."
  - "Boş kapasitede tam maliyetin altındaki bir sipariş kârlı olabilir."
  - "Kapasite doluysa vazgeçilen katkı payı (fırsat maliyeti) hesaba katılmalıdır."
glossary_terms: [ilgili-maliyet, katki-payi, firsat-maliyeti, batik-maliyet]
related: [kb-eco-1-1-opportunity-cost-sunk-cost, kb-eco-39-2-product-costing, kb-eco-6-4-price-discrimination, kb-eco-5-5-economies-of-scale-sunk-costs]
sources:
  - title: "Principles of Accounting, Volume 2: Managerial Accounting"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-managerial-accounting/pages/1-why-it-matters"
    verified: true
    checked_on: 2026-10-28
  - title: "The psychology of sunk cost"
    authors: "Arkes, H. R.; Blumer, C."
    year: 1985
    type: article
    doi: "10.1016/0749-5978(85)90049-4"
    url: "https://doi.org/10.1016/0749-5978(85)90049-4"
    verified: true
    checked_on: 2026-10-28
    note: "Organizational Behavior and Human Decision Processes 35(1)."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

"Bu fiyat maliyetimizin altında" cümlesi, kârlı siparişlerin reddedilmesine ya da zararlı siparişlerin kabul edilmesine yol açabilir. Bu kart, özel sipariş, yap-ya da-al ve ürün bırakma gibi kararlarda hangi maliyetlere bakmanız gerektiğini gösterir.

## Temel fikir

**İlgili maliyet:** Kararın sonucunda değişecek, gelecekteki maliyet ve gelirlerdir.

- **İlgili:** Hammadde, değişken işçilik, ek nakliye, kaybedilen satışların katkı payı.
- **İlgisiz:** Geçmişte yapılmış harcamalar (batık maliyet) ve karardan bağımsız olarak süren sabit giderler (kira, yönetim maaşları).

**Katkı payı** = Fiyat − Değişken maliyet. Sabit giderler zaten ödenecekse, pozitif katkı payı şirketin toplam kârını artırır.

**Kapasite önemlidir:** Boş kapasite varsa fırsat maliyeti sıfıra yakındır. Kapasite doluysa yeni sipariş, mevcut bir satışın yerini alır ve o satışın katkı payı kaybedilir.

### Tipik kararlar

- **Özel sipariş:** Boş kapasite varken normal fiyatın altındaki bir sipariş, değişken maliyetleri karşılıyorsa kârı artırır. Ancak diğer müşterilerin aynı fiyatı talep etme riski de bir ilgili maliyettir.
- **Yap ya da al:** Bir parçayı veya hizmeti (ör. nakliye) dışarıdan almanın maliyeti, içeride üretmenin kaçınılabilir maliyetleriyle karşılaştırılır. Kullanılmayan kapasitenin başka bir işte kullanılıp kullanılamayacağı da hesaba katılır.
- **Ürün veya şube kapatma:** Kapatılınca ortadan kalkacak gelir ve giderlere bakılır. Ortak giderlerin payı genellikle kalkmaz ve diğer ürünlere kalır.
- **Kısıtlı kaynak:** Depo alanı veya üretim kapasitesi kısıtlıysa, ürünleri birim başına değil kısıtlı kaynak birimi başına katkı payına göre sıralayın.

### Nitel unsurlar

Her kararın sayılara yansımayan yönleri vardır: müşteri ilişkisi, tedarikçi bağımlılığı, kalite kontrolü, çalışanlar üzerindeki etkisi. Rakamlar karar için zemin hazırlar ama nitel unsurları da açıkça yazın. Ayrıca kararın geri dönüşü olup olmadığını düşünün; kapatılan bir şubeyi veya kaybedilen bir müşteriyi geri kazanmak çoğu zaman pahalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Fiyatlar, maliyetler ve adetler varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b6.py` ile yapılmıştır.

Bir zincir, 20.000 adetlik özel markalı ürün için birim 70 TL teklif ediyor. Muhasebedeki tam birim maliyet 80 TL (60 TL değişken + 20 TL dağıtılmış sabit gider). Tam maliyetle bakıldığında sipariş 200.000 TL zarar gibi görünüyor.

**Boş kapasite varsa:** Katkı payı 20.000 × (70 − 60) = 200.000 TL. Ek etiket ve nakliye maliyeti 50.000 TL. Net etki **+150.000 TL.** Sipariş kabul edilmeli.

**Kapasite doluysa:** Sipariş, birim 90 TL'ye satılan normal ürünün yerini alıyor. Vazgeçilen katkı payı 600.000 TL. Net etki **450.000 TL zarar.** Sipariş reddedilmeli ya da fiyat yükseltilmeli.

## Sık yapılan hatalar

- Dağıtılmış sabit gideri değişken maliyet gibi kullanmak.
- Batık maliyetleri ("bu makineye çok para verdik") karara katmak.
- Kapasite kısıtını ve fırsat maliyetini unutmak.
- Düşük fiyatlı özel siparişin diğer müşterilerin fiyat beklentisini etkileme riskini göz ardı etmek.
- Kısa vadeli katkı payı mantığını kalıcı fiyatlama politikasına dönüştürmek; uzun vadede sabit giderlerin de karşılanması gerekir.

## Pratikte nasıl uygulanır?

- [ ] Maliyet raporlarınızda değişken ve sabit maliyetleri ayrı gösterin.
- [ ] Her özel sipariş için ilgili gelir ve maliyetleri listeleyen bir şablon kullanın.
- [ ] Teklif öncesinde kapasite kullanım oranını kontrol edin.
- [ ] Özel siparişlerin mevcut müşteri fiyatlarına etkisini değerlendirin.
- [ ] Kararı ve varsayımları kayda geçirin, sonrasında gerçekleşenle karşılaştırın.

## Daha fazlası

- OpenStax (2026). *Principles of Accounting, Volume 2: Managerial Accounting*. https://openstax.org/books/principles-managerial-accounting/pages/1-why-it-matters
- Arkes, H. R.; Blumer, C. (1985). *The psychology of sunk cost*. https://doi.org/10.1016/0749-5978(85)90049-4
