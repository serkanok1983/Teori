---
id: kb-fmcg-11-1-supply-chain-basics
title: "Hızlı tüketimde tedarik zinciri: Akışlar, hedefler ve ödünleşimler"
summary: "Tedarik zinciri; ürünün tedarikçiden fabrikaya, depoya, noktaya ve tüketiciye akışını, bu akışa eşlik eden bilgi ve para akışlarıyla birlikte kapsar. Bu kart temel akışları, hizmet, maliyet ve sermaye arasındaki ödünleşimi ve nakit dönüşüm süresini anlatır."
course: fmcg
category: tedarik-zinciri-ve-stok
tags: [tedarik-zinciri, stok, finans]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, depo-lojistik-muduru]
level: temel
source_lessons: [FMCG-11.1]
reading_minutes: 3
key_points:
  - "Tedarik zincirinde üç akış vardır: ürün, bilgi ve para."
  - "Tedarik zinciri yönetimi; hizmet seviyesi, maliyet ve bağlanan sermaye arasında bir denge kurar."
  - "Nakit dönüşüm süresi, stok ve alacak günlerinin toplamından borç günlerinin düşülmesiyle bulunur."
  - "Stok gününü kısaltmak, satış büyüklüğüne göre önemli miktarda sermayeyi serbest bırakabilir."
  - "Satış, pazarlama ve tedarik zinciri kararları birbirini etkiler; ayrı ayrı optimize edilemez."
glossary_terms: [nakit-donusum-suresi, stok-gun-sayisi, alacak-tahsil-suresi, borc-odeme-suresi, siparis-karsilama-orani, isletme-sermayesi]
related: [kb-fmcg-11-2-demand-forecasting, kb-fmcg-11-4-safety-stock, kb-fmcg-11-5-bullwhip-effect, kb-fmcg-11-6-sop-ibp, kb-fmcg-11-7-warehouse-transport-network]
sources:
  - title: "Supply Chain Management: Strategy, Planning, and Operation"
    authors: "Chopra, S.; Meindl, P."
    year: 2016
    type: book
    verified: false
    note: "Kitap; baskı yılı kontrol edilmedi."
  - title: "ASCM CSCP — Certified Supply Chain Professional"
    authors: "ASCM"
    year: 2026
    type: web
    url: "https://www.ascm.org/learning-development/certifications-credentials/cscp/"
    verified: true
    checked_on: 2026-10-28
    note: "HTTP 200; başlık etiketi okunamadı."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Satış ekibi "ürün yok" diye şikâyet ederken, finans "stok çok yüksek" der, depo ise "kapasite doldu" diye uyarır. Bu üç şikâyet aynı sistemin farklı yüzleridir. Bu kart, tedarik zincirinin temel mantığını ve bu çatışan hedefler arasında nasıl karar verileceğini anlatır.

## Temel fikir

**Üç akış.**

- **Ürün akışı:** Hammadde ve ambalaj tedarikçilerinden fabrikaya, fabrikadan merkez depoya, oradan dağıtıcıya ya da doğrudan zincir deposuna ve mağazaya.
- **Bilgi akışı:** Siparişler, tahminler, stok seviyeleri, satış verisi. Bu akış ne kadar hızlı ve doğruysa ürün akışı o kadar verimli olur.
- **Para akışı:** Perakendeciden dağıtıcıya, dağıtıcıdan üreticiye, üreticiden tedarikçilere ödemeler.

**Temel ödünleşim.** Chopra ve Meindl gibi temel kaynaklar, tedarik zinciri kararlarını duyarlılık (hizmet) ile verimlilik (maliyet) arasındaki bir denge olarak anlatır. Hızlı tüketimde bu denge üç boyutta görülür:

- **Hizmet seviyesi:** Sipariş karşılama oranı, zamanında teslimat, raf bulunurluğu.
- **Maliyet:** Üretim, depolama, taşıma, fire.
- **Bağlanan sermaye:** Stok ve alacaklar.

Daha yüksek hizmet seviyesi genellikle daha fazla stok ya da daha sık teslimat, yani daha fazla maliyet ve sermaye gerektirir. Bu dengeyi bilinçli olarak kurmak gerekir; her ürün ve her müşteri için aynı hizmet seviyesi gerekmez.

**Nakit dönüşüm süresi.** Tedarik zincirinin finansal etkisini özetleyen göstergedir:

Nakit dönüşüm süresi = stok gün sayısı + alacak tahsil süresi − borç ödeme süresi

Bu süre ne kadar uzunsa, işletme o kadar uzun süre kendi kaynağıyla ya da borçla finansman sağlar.

**Mesleki çerçeve.** ASCM'nin tedarik zinciri sertifika programları gibi mesleki kaynaklar, planlama, kaynak sağlama, üretim, teslimat ve iadeleri birbirine bağlı süreçler olarak ele alır.

## Bir örnek

> **Örnek (temsili rakamlar):** Satış ve gün sayıları varsayımdır; bağlanan sermaye satış bazlı yaklaşık bir hesaptır; hesaplar `scripts/cards_numbers_fmcg_b6.py` ile yapılmıştır.

Yıllık satışı 120.000.000 TL olan bir dağıtıcı:

- Stok gün sayısı: **45** gün
- Alacak tahsil süresi: **60** gün
- Borç ödeme süresi: **40** gün
- Nakit dönüşüm süresi: 45 + 60 − 40 = **65** gün

Günlük satış yaklaşık **328.767 TL**. Satış bazlı kaba bir hesapla, işletmenin bu döngüyü finanse etmek için yaklaşık **21.369.863 TL** sermaye bağladığı söylenebilir.

Dağıtıcı, sipariş ve tahmin süreçlerini iyileştirerek stok gününü 45'ten 35'e indirirse, yaklaşık **3.287.671 TL** sermaye serbest kalır. Bu tutar, yüksek faiz ortamında önemli bir finansman tasarrufu demektir. Ancak stok azaltılırken sipariş karşılama oranının düşmemesi gerekir; bu nedenle azaltma, önce yavaş dönen ürünlerden başlamalıdır.

## Sık yapılan hatalar

- **Her birimin kendi hedefini ayrı optimize etmesi.** Satış yüksek stok, finans düşük stok, depo az sevkiyat ister; sonuç kimsenin hedefini karşılamaz.
- **Bütün ürünlere aynı hizmet seviyesini uygulamak.** Hızlı dönen ana ürünler ile yavaş dönen ürünler farklı yönetilmelidir.
- **Stoku yalnızca adet olarak izlemek.** Gün ve TL olarak izlenmeyen stok, sermaye etkisini göstermez.
- **Bilgi akışını ihmal etmek.** Gecikmeli ya da hatalı sipariş verisi, fazla stokun en yaygın nedenidir.
- **Alacakları tedarik zincirinden ayrı düşünmek.** Uzun vadeli müşteriler, nakit dönüşüm süresini uzatır.

## Pratikte nasıl uygulanır?

- [ ] Nakit dönüşüm süresini her ay hesaplayın ve bileşenlerini ayrı ayrı izleyin.
- [ ] Ürünlerinizi satış hızına göre gruplayın ve her grup için hizmet seviyesi hedefi belirleyin.
- [ ] Stoku gün ve TL olarak raporlayın; yavaş dönen ürünleri ayrı listeleyin.
- [ ] Satış, finans ve tedarik zinciri yöneticilerini aylık ortak bir toplantıda bir araya getirin.
- [ ] Sipariş verisi ile gerçek stok arasındaki farkları düzenli sayımlarla kontrol edin.

## Daha fazlası

- Chopra, S.; Meindl, P. (2016). *Supply Chain Management: Strategy, Planning, and Operation.* (kaynak doğrulanmadı)
- ASCM (2026). *ASCM CSCP — Certified Supply Chain Professional.* https://www.ascm.org/learning-development/certifications-credentials/cscp/
