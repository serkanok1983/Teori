---
id: kb-fmcg-6-8-rtm-design-case
title: "Vaka: Bir bölge için pazara giriş modeli tasarlamak"
summary: "Bu vaka, bir üreticinin bir bölgede dağıtıcıyla devam mı edeceğini, yoksa doğrudan dağıtıma mı geçeceğini adım adım değerlendirir. Nokta evreni, hizmet maliyeti ve başabaş hesabı tek bir kararda birleşir."
course: fmcg
category: dagitim-modeli
tags: [dagitim, strateji, vaka, maliyet]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru]
level: ileri
source_lessons: [FMCG-6.8]
reading_minutes: 3
key_points:
  - "Pazara giriş modeli kararı, maliyet karşılaştırmasıyla birlikte satış etkisini, işletme sermayesini ve riski kapsamalıdır."
  - "Doğrudan modelin daha pahalı olması, ek satışın katkısı bu farkı kapatıyorsa geçişi engellemez."
  - "Varsayımları senaryolarla sınamak, kararın hangi rakama en duyarlı olduğunu gösterir."
  - "Karar ya hep ya hiç değildir; dağıtıcıyı iyileştirmek ya da karma bir model kurmak da seçenektir."
glossary_terms: [pazara-giris-modeli, dogrudan-dagitim, hizmet-maliyeti]
related: [kb-fmcg-6-4-direct-vs-indirect, kb-fmcg-6-2-outlet-universe-segmentation, kb-fmcg-6-3-cost-to-serve, kb-fmcg-7-1-distributor-pnl, kb-fmcg-7-5-distributor-development]
sources:
  - title: "Marketing Channels"
    authors: "Coughlan, A. T.; Anderson, E.; Stern, L. W.; El-Ansary, A. I."
    year: 2006
    type: book
    verified: false
    note: "Kitap; baskı yılı kontrol edilmedi."
  - title: "The Economic Institutions of Capitalism"
    authors: "Williamson, O. E."
    year: 1985
    type: book
    verified: false
    note: "Kitap; künye kontrol edilmedi."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Önceki kartlarda ayrı ayrı anlatılan araçlar, gerçek bir kararda birlikte kullanılır. Bu vaka, kendi bölgeniz için benzer bir değerlendirmeyi yapmanızda bir şablon sunar. Vakadaki firma ve rakamlar kurgusaldır.

## Temel fikir

**Durum.** Bir gıda üreticisi, yıllık 60 milyon TL satış yaptığı bir bölgede bir dağıtıcıyla çalışıyor. Dağıtıcı satış üzerinden %9 marj alıyor. Üretici, bölgede dağıtıcıyı denetleyen iki kişilik bir ekip için ayrıca yıllık 1,2 milyon TL harcıyor. Satış müdürü, dağıtıcının küçük noktaları ihmal ettiğini ve doğrudan dağıtımla satışın %10 artacağını düşünüyor.

**Değerlendirme adımları.**

1. **Nokta evreni:** Dağıtıcının gerçekten hangi noktalara gittiğini ve hangilerini atladığını görmek için nokta evrenini çıkarın.
2. **Doğrudan modelin maliyeti:** Satış temsilcileri, araçlar, depo ve tahsilat riski.
3. **Satış etkisi:** Ek satış iddiasını hangi verilere dayandırıyorsunuz? Atlanan noktaların potansiyeli ne?
4. **İşletme sermayesi:** Doğrudan modelde alacak ve stok bilançonuza gelir.
5. **Risk ve geçiş:** Dağıtıcıyla sözleşmenin sona ermesi, müşteri ilişkilerinin devri, ilk aylardaki aksaklıklar.

Williamson'ın (1985) işlem maliyetleri yaklaşımı burada da yol gösterir: Bir işi içeri almak, fırsatçılık ve belirsizlik riskini azaltabilir, ama yönetim yükünü artırır.

## Bir örnek

> **Örnek (temsili rakamlar):** Bütün rakamlar kurgusaldır; hesaplar `scripts/cards_numbers_fmcg_b3.py` ile yapılmıştır.

**Bugünkü model (dağıtıcı):** 60.000.000 × %9 + 1.200.000 = **6.600.000 TL** (satışın **%11,00**'i).

**Doğrudan model:** 10 temsilci × 540.000 TL, 6 araç × 360.000 TL, depo 1.200.000 TL, tahsilat kaybı satışın %0,5'i. Aynı satışta toplam **9.060.000 TL** (satışın **%15,10**'u).

Satış %10 artıp 66 milyon TL olursa doğrudan maliyet **9.090.000 TL** olur. Ek 6 milyon TL satışın katkısı (%30 katkı oranıyla) **1.800.000 TL**.

- Doğrudan modelin ek maliyeti: 9.090.000 − 6.600.000 = 2.490.000 TL
- Ek katkı: 1.800.000 TL
- Net etki: **−690.000 TL**

Üstelik doğrudan model yaklaşık **4.000.000 TL** ek işletme sermayesi gerektiriyor. Satış artışı %10'da kalırsa geçiş kârlı değil.

**Seçenekler.** Ekip, doğrudan geçiş yerine dağıtıcıyla atlanan noktalar için bir kapsama hedefi ve buna bağlı bir prim konuşmaya karar verir. Hedef tutmazsa bir yıl sonra büyük şehir merkezinde karma bir model (merkezde doğrudan, çevrede dağıtıcı) değerlendirilecektir.

## Sık yapılan hatalar

- **Satış artışını kanıtsız varsaymak.** Kararın en duyarlı rakamı genellikle budur.
- **İşletme sermayesini dışarıda bırakmak.** Kâr tablosunda görünmez, ama nakdi bağlar.
- **Yalnızca iki seçenek düşünmek.** Dağıtıcıyı geliştirmek ya da karma model çoğu zaman daha az risklidir.

## Pratikte nasıl uygulanır?

- [ ] Bölgenizin rakamlarıyla aynı tabloyu kurun.
- [ ] Satış artışı, temsilci maliyeti ve tahsilat kaybı için en az üç senaryo hazırlayın.
- [ ] Kararı değiştiren eşik değeri bulun: Satış artışı yüzde kaç olursa doğrudan model kârlı hâle geliyor?
- [ ] Kararı, eşiği test edecek bir pilot uygulamayla destekleyin.

## Daha fazlası

- Coughlan, A. T.; Anderson, E.; Stern, L. W.; El-Ansary, A. I. (2006). *Marketing Channels.* (kaynak doğrulanmadı)
- Williamson, O. E. (1985). *The Economic Institutions of Capitalism.* (kaynak doğrulanmadı)
