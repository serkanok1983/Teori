---
id: kb-eco-1-1-opportunity-cost-sunk-cost
title: "Fırsat maliyeti ve batık maliyet: Kararı neye göre vermeli?"
summary: "Bir kararın gerçek maliyetinin, vazgeçilen en iyi seçenek olduğunu ve geri dönmeyecek harcamaların bugünkü kararı etkilememesi gerektiğini bayi ve üretici örnekleriyle anlatır."
course: eco
category: ekonomi-temelleri
tags: [karar-verme, maliyet, yatirim]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru]
level: temel
source_lessons: [ECO-1.1]
reading_minutes: 3
key_points:
  - "Bir seçeneğin gerçek maliyeti, onun için vazgeçtiğiniz en iyi alternatifin getirisidir."
  - "Ekonomik maliyet, ödenen paraya ek olarak kendi deponuzun, sermayenizin ve emeğinizin alternatif getirisini de içerir."
  - "Geri alınamayan geçmiş harcama (batık maliyet) bugünkü seçenekler arasında fark yaratmaz; karara girmez."
  - "Kararı yalnızca bundan sonraki ek gelir ve ek maliyetlere bakarak verin."
glossary_terms: [firsat-maliyeti, batik-maliyet]
related: [kb-eco-5-5-economies-of-scale-sunk-costs, kb-eco-39-5-relevant-costs-decisions, kb-eco-13-1-heuristics-biases, kb-eco-31-1-capital-budgeting]
sources:
  - title: "An Essay on the Nature and Significance of Economic Science"
    authors: "Robbins, L."
    year: 1932
    type: book
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
  - title: "Principles of Economics 3e, §1.1 What Is Economics, and Why Is It Important?"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-economics-3e/pages/1-1-what-is-economics-and-why-is-it-important"
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

Yeni bir bölgeye girmek, bir ürün grubunu bırakmak ya da deponuzu kiraya vermek gibi kararların hepsinde aynı soru vardır: Bunu yaparsam neyden vazgeçiyorum? Bu kart, muhasebe kârı yüksek görünen bir işin aslında para kaybettirebileceğini ve "bu kadar para harcadık, bırakamayız" düşüncesinin neden yanlış kararlara götürdüğünü gösterir.

## Temel fikir

**Fırsat maliyeti** (*opportunity cost*), bir seçeneği seçtiğinizde vazgeçtiğiniz en iyi alternatifin değeridir. Kaynaklar kıttır: Aynı depo, aynı araç ya da aynı sermaye aynı anda iki işte kullanılamaz. Bu yüzden her kararın görünmeyen bir bedeli vardır.

Bu fikirden iki pratik sonuç çıkar:

- **Ekonomik maliyet = açık maliyet + örtük maliyet.** Açık maliyet, kasadan çıkan paradır (kira, maaş, yakıt). Örtük maliyet ise sahip olduğunuz kaynağın başka bir işte getirebileceği tutardır: kendi deponuzun kira geliri, işe koyduğunuz sermayenin faiz getirisi, patronun başka bir işte kazanabileceği ücret. Muhasebe kayıtları örtük maliyeti göstermez.
- **Batık maliyet** (*sunk cost*) karara girmez. Geçmişte yapılmış ve hangi yolu seçerseniz seçin geri gelmeyecek harcama, bugünkü seçenekler arasında fark yaratmaz. Karşılaştırmada yalnızca bundan sonra oluşacak gelir ve maliyetler yer alır.

Robbins (1932) ekonomiyi, alternatif kullanımları olan kıt kaynaklarla amaçlar arasındaki ilişki olarak tanımlar. Yönetici için bunun anlamı basittir: Her kararda masaya en az iki seçenek koyun ve bunları aynı ölçüyle karşılaştırın.

## Bir örnek

> **Örnek (temsili rakamlar):** Aşağıdaki bayi gerçek bir işletme değildir; rakamlar `scripts/cards_numbers_eco_b1.py` ile hesaplanmıştır.

**Durum 1 — Kâr gerçekten kâr mı?** Bir bayi sahibi kendi mülkü olan depoda çalışıyor ve kendine maaş yazmıyor. Muhasebe kârı yıllık **4.000.000 TL**.

- Depo dışarıya kiraya verilse ayda 150.000 TL getirecek: yıllık **1.800.000 TL** örtük maliyet.
- Patron aynı emekle başka bir firmada ayda 90.000 TL kazanabilir: yıllık **1.080.000 TL** örtük maliyet.
- Ekonomik kâr = 4.000.000 − 1.800.000 − 1.080.000 = **1.120.000 TL**.

İş hâlâ kârlı, ama tablodaki rakamın üçte birinden azı kadar. Bayilik koşulları kötüleşirse bu tampon hızla erir.

**Durum 2 — Batık maliyet tuzağı.** Bayi yeni bir ilçeye girmek için şimdiye kadar **2.000.000 TL** harcamış (araç giydirme, açılış promosyonları, ilk ekip). Sonuçlar zayıf. Devam etmek için **1.500.000 TL** daha gerekiyor ve önümüzdeki dönemde beklenen ek brüt katkı **1.200.000 TL**.

- Devam etmenin net etkisi: 1.200.000 − 1.500.000 = **−300.000 TL**.
- Aynı 1.500.000 TL mevcut bölgede rota yoğunlaştırmaya harcanırsa beklenen ek katkı 1.800.000 TL: net **300.000 TL**.
- İki seçenek arasındaki fark **600.000 TL**'dir. Daha önce harcanan 2.000.000 TL iki seçenekte de aynıdır; bu yüzden hesaba hiç girmez.

## Sık yapılan hatalar

- "Şu ana kadar bu kadar yatırım yaptık" diyerek kötü giden bir projeye para eklemeye devam etmek.
- Kendi mülkünüzdeki depoyu ya da kendi sermayenizi "bedava" saymak.
- Yalnızca tek bir seçeneği değerlendirmek; "yapmazsak ne olur?" sorusunu sormamak.
- Ortalama maliyete bakıp karar vermek; oysa karar, ek (marjinal) maliyet ve ek gelirle verilir.
- Batık maliyeti gizlemek için performans raporlarını yumuşatmak; bu, sorunu yalnızca erteler.

## Pratikte nasıl uygulanır?

- [ ] Her yatırım ya da genişleme kararında en az iki somut alternatifi yazılı olarak karşılaştırın.
- [ ] Bayi sahibi olarak kendi deponuzun piyasa kirasını ve kendi emeğinizin karşılığını yıllık kâr hesabınızdan düşerek bakın.
- [ ] Devam/vazgeç kararlarında tabloya yalnızca bundan sonraki nakit giriş ve çıkışlarını koyun.
- [ ] Yeni bölge ve ürün projelerine baştan bir "durdurma kriteri" (ör. 6 ayda ulaşılacak ziyaret ve tahsilat düzeyi) koyun.
- [ ] Satış direktörü olarak, ekipten gelen "bıraktığımız yatırım boşa gider" itirazını, ek getiri ve ek maliyet sorusuna çevirin.

## Daha fazlası

- Robbins, L. (1932). *An Essay on the Nature and Significance of Economic Science*.
- Arkes, H. R.; Blumer, C. (1985). *The psychology of sunk cost*. https://doi.org/10.1016/0749-5978(85)90049-4
- OpenStax (2026). *Principles of Economics 3e, §1.1 What Is Economics, and Why Is It Important?*. https://openstax.org/books/principles-economics-3e/pages/1-1-what-is-economics-and-why-is-it-important
