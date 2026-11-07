---
id: kb-fmcg-1-1-margin-vs-markup
title: "Marj mı, maliyet üzerine ekleme mi? Fiyatı doğru kurmak"
summary: "Marj satış fiyatı üzerinden, maliyet üzerine ekleme oranı (markup) ise maliyet üzerinden hesaplanır. İkisini karıştırmak fiyatı ve kârı sessizce düşürür; bu kart dönüşümü ve üretici–bayi–market fiyat zincirini adım adım gösterir."
course: fmcg
category: sektor-ve-kanal
tags: [marj, kar-orani, fiyatlama, kdv, bayi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: temel
source_lessons: [FMCG-1.1]
reading_minutes: 6
key_points:
  - "Marj = (Satış fiyatı − Maliyet) ÷ Satış fiyatı; maliyet üzerine ekleme oranı = (Satış fiyatı − Maliyet) ÷ Maliyet."
  - "Hedef marjla fiyat bulmak için maliyet (1 − marj) sayısına bölünür; (1 + marj) ile çarpılmaz."
  - "Kanaldaki her aşamanın marjı farklı bir tabana göre alınır, bu yüzden yüzdeler toplanamaz."
  - "Marjlar KDV hariç fiyatlar üzerinden hesaplanır; KDV en son eklenir."
  - "Brüt marj kâr değildir; teslimat, vade ve tahsilat maliyetleri ayrıca düşülmelidir."
glossary_terms: [marj, maliyet-uzerine-ekleme-orani, kdv, cift-marjinallesme]
related: [kb-fmcg-1-1-margin-stack, kb-fmcg-2-2-gross-to-net, kb-fmcg-6-3-cost-to-serve, kb-fmcg-1-3-channel-actors, kb-eco-43-4-kdv-vat]
sources:
  - title: "Vertical Integration and Antitrust Policy"
    authors: "Spengler, J. J."
    year: 1950
    type: article
    doi: "10.1086/256964"
    url: "https://doi.org/10.1086/256964"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Political Economy 58(4), 347–352. Çift marjinalleşme."
  - title: "Competitive Advantage: Creating and Sustaining Superior Performance"
    authors: "Porter, M. E."
    year: 1985
    type: book
    verified: false
    note: "Kitap; DOI yok. Değer zinciri kavramı. Künyeyi yayımlamadan önce kontrol edin."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Bir ürünün fiyatını kurarken ya da bir tedarikçinin "size %25 bırakıyoruz" teklifini değerlendirirken iki farklı oranla karşılaşırsınız: **marj** ve **maliyet üzerine ekleme oranı** (İngilizcesi *markup*). İkisi aynı şey değildir. Karıştırıldığında fiyat olması gerekenden düşük kurulur ve kâr, kimse fark etmeden erir. Bu kart iki oran arasındaki dönüşümü ve üreticiden rafa kadar fiyatın nasıl oluştuğunu gösterir.

## Temel fikir

Bir ürünü **M** maliyetle alıp **F** fiyatla satan biri için:

- **Marj** = (F − M) ÷ F → kârın *satış fiyatına* oranı
- **Maliyet üzerine ekleme oranı** = (F − M) ÷ M → kârın *maliyete* oranı

Ticarette, özellikle bayi ve market tarafında, oranlar genellikle **satış fiyatı üzerinden marj** olarak konuşulur. Bu yüzden şu kural önemlidir:

> **İpucu:** Hedef marjla satış fiyatı bulmak için maliyeti **(1 − marj)** sayısına bölün. Maliyeti (1 + marj) ile çarparsanız istediğiniz marjı tutturamazsınız.

İki oran birbirine şöyle çevrilir:

- Ekleme oranı = Marj ÷ (1 − Marj)
- Marj = Ekleme oranı ÷ (1 + Ekleme oranı)

**Fiyat zinciri.** Ürün üreticiden bayiye, bayiden markete, marketten tüketiciye geçerken her aşama kendi marjını ekler. Raf fiyatı şöyle oluşur:

Raf fiyatı = Üretici satış fiyatı ÷ (1 − bayi marjı) ÷ (1 − market marjı) × (1 + KDV oranı)

KDV en sona eklenir, çünkü tüketicinin ödediği fiyat üzerinden alınan bir vergidir; marjlar hep KDV hariç fiyatlarla hesaplanır. Bu basit formül, liste fiyatı dışındaki iskontoları, ciro primlerini ve sabit ödemeleri içermez; onlar için brütten nete kartına bakın.

Aşamalar birbirinden bağımsız kendi marjını eklediğinde raf fiyatı yükselir ve kanalın toplam kârı, tek elden yönetilen bir kanala göre düşebilir. İktisatta buna **çift marjinalleşme** (*double marginalisation*) denir (Spengler, 1950). Ticari şartların ve ortak iş planlarının varlık nedeni büyük ölçüde budur.

## Bir örnek

> **Örnek (temsili rakamlar):** Aşağıdaki fiyatlar ve oranlar gerçek bir ürüne ait değildir; tüm hesaplar `scripts/pilot_numbers.py` ile yapılmıştır. KDV oranı yalnızca örnek içindir; ürününüzün güncel oranını kontrol edin.

**1. Marj ile ekleme oranı arasındaki fark**

- %25 marj = 0,25 ÷ 0,75 = **%33,33** ekleme oranı.
- %12 marj = 0,12 ÷ 0,88 = **%13,64** ekleme oranı.
- Tersten: %25 ekleme oranı = 0,25 ÷ 1,25 = **%20,00** marj.

Maliyeti 100,00 TL olan bir ürüne "%25 marj" koymak isteyen biri fiyatı 100,00 × 1,25 = 125,00 TL yaparsa, gerçek marjı (125,00 − 100,00) ÷ 125,00 = **%20,00** olur. Doğru fiyat 100,00 ÷ 0,75 = **133,33 TL**'dir. Aradaki 8,33 TL, her adette kaybedilen kârdır.

**2. Üreticiden rafa fiyat zinciri**

Varsayımlar: üretim maliyeti 20,00 TL/adet, üreticinin bayiye net satış fiyatı 30,00 TL, bayi marjı %12, market marjı %25, KDV %20 (örnek oran).

| Adım | Hesap | Sonuç |
|---|---|---|
| Bayinin markete satış fiyatı | 30,00 ÷ (1 − 0,12) | 34,09 TL (bayinin brüt kârı 4,09 TL) |
| Marketin KDV hariç satış fiyatı | 34,09 ÷ (1 − 0,25) | 45,45 TL (marketin brüt kârı 11,36 TL) |
| Raf fiyatı (KDV dahil) | 45,45 × 1,20 | 54,55 TL (içindeki KDV 9,09 TL) |
| Üreticinin brüt marjı | (30,00 − 20,00) ÷ 30,00 | %33,33 |

**3. KDV hariç 45,45 TL'lik raf fiyatını kim alıyor?**

| Pay | TL/adet | Oran |
|---|---|---|
| Üretim maliyeti | 20,00 | %44,0 |
| Üreticinin brüt kârı | 10,00 | %22,0 |
| Bayinin brüt kârı | 4,09 | %9,0 |
| Marketin brüt kârı | 11,36 | %25,0 |
| **Toplam** | **45,45** | **%100** |

Sağlama: 20,00 + 10,00 + 4,09 + 11,36 = 45,45 TL. Bu örnekte tüketicinin ödediği tutarın (KDV hariç) yarısından fazlası ürünü üretmeye değil, ürünü rafa getirmeye ve satmaya gidiyor. Dağıtım modelinin ticari önemi buradan gelir.

Dikkat: bayi marjı %12 ve market marjı %25 olduğu hâlde, toplam "kanal marjı" %37 değildir. İki oran farklı fiyatlar üzerinden alınmıştır, toplanamaz.

## Sık yapılan hatalar

- Marjı ekleme oranı gibi kullanmak: maliyeti 1,25 ile çarpıp "%25 marj koydum" sanmak.
- Farklı aşamaların marj yüzdelerini toplamak ya da ortalamasını almak.
- Marjı KDV dahil fiyat üzerinden hesaplamak.
- Liste fiyatını net fiyat sanmak; iskonto, ciro primi ve promosyon desteklerini hesaba katmamak.
- Brüt marjı kâr saymak: küçük siparişlerin teslimat maliyetini ve uzun vadenin finansman maliyetini unutmak. Yüksek enflasyonda vadeli satışın maliyeti özellikle yüksektir.

## Pratikte nasıl uygulanır?

- [ ] Fiyat listelerinizde ve tekliflerinizde oranın "marj" mı, "ekleme oranı" mı olduğunu açıkça yazın.
- [ ] Hedef marjdan fiyat hesaplayan tüm tablolarda formülün `maliyet ÷ (1 − marj)` olduğunu kontrol edin.
- [ ] Marj raporlarını KDV hariç net fiyatlarla hazırlayın.
- [ ] Ana ürünleriniz için üreticiden rafa fiyat zincirini bir kez çıkarın; zincirdeki her aşamanın TL olarak ne kazandığını görün.
- [ ] Satış ekibine (şef ve temsilciler) %20 marj ile %25 ekleme oranının aynı şey olduğunu bir örnekle anlatın.
- [ ] Bayi ve market marjlarını tartışırken yüzde yerine adet başına TL'yi de konuşun.

## Daha fazlası

- Spengler, J. J. (1950). *Vertical Integration and Antitrust Policy.* Journal of Political Economy, 58(4), 347–352. https://doi.org/10.1086/256964 — çift marjinalleşmenin ilk açıklaması.
- Porter, M. E. (1985). *Competitive Advantage.* Free Press — değer zinciri kavramı.
