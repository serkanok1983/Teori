---
id: kb-fmcg-2-3-contribution-breakeven
title: "Katkı payı, başabaş ve faaliyet kaldıracı: İndirim kaç adet daha satmayı gerektirir?"
summary: "Katkı payı, bir birim fazla satışın kâra ne eklediğini gösterir. Bu kart başabaş noktasını, faaliyet kaldıracını ve fiyat indiriminin aynı kârı korumak için gerektirdiği ek hacmi hesaplamayı gösterir."
course: fmcg
category: ticari-finans
tags: [marj, fiyatlama, promosyon, butce]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: temel
source_lessons: [FMCG-2.3, ECO-39.1]
reading_minutes: 3
key_points:
  - "Birim katkı payı = fiyat − birim değişken maliyet; başabaş adedi = sabit giderler ÷ birim katkı payı."
  - "Sabit giderler yüksekken hacimdeki küçük bir değişim kârda büyük değişime yol açar; buna faaliyet kaldıracı denir."
  - "Fiyat indirimi katkı payını yüzde olarak indirimden çok daha fazla düşürür; aynı kârı korumak için gereken ek hacim büyüktür."
  - "Karar verirken yalnızca o karardan etkilenen gelir ve maliyetlere bakın; dağıtılmış sabit giderler yanıltır."
glossary_terms: [katki-payi, basabas-noktasi, faaliyet-kaldiraci, sabit-maliyet, degisken-maliyet]
related: [kb-fmcg-2-1-fmcg-pnl, kb-fmcg-5-4-promotion-economics, kb-eco-39-5-relevant-costs-decisions, kb-fmcg-1-2-scale-and-concentration, kb-fmcg-2-4-roi-roce-npv]
sources:
  - title: "Principles of Corporate Finance"
    authors: "Brealey, R. A.; Myers, S. C.; Allen, F."
    year: 2020
    type: book
    verified: false
    note: "Kitap; baskı yılı kontrol edilmedi."
  - title: "Cost & Effect: Using Integrated Cost Systems to Drive Profitability and Performance"
    authors: "Kaplan, R. S.; Cooper, R."
    year: 1998
    type: book
    verified: false
    note: "Kitap; faaliyet tabanlı maliyetleme. Künye kontrol edilmedi."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

"%5 indirim verirsek satış artar, kâr da artar" cümlesi ancak hesapla doğrulanabilir. Bu kart, fiyat ve hacim kararlarında en çok kullanılan üç aracı verir: katkı payı, başabaş noktası ve faaliyet kaldıracı. Promosyon onayı, büyük sipariş indirimi ve yeni ürün kararlarında işinize yarar.

## Temel fikir

**Katkı payı.** Bir ürünü sattığınızda fiyattan yalnızca o birim için ortaya çıkan maliyetleri (hammadde, ambalaj, adet başı nakliye, satış primi) düşersiniz. Kalan tutar sabit giderleri karşılamaya ve kâra katkı yapar.

- Birim katkı payı = Fiyat − Birim değişken maliyet
- Katkı payı oranı = Birim katkı payı ÷ Fiyat

**Başabaş noktası.** Sabit giderlerin tamamen karşılandığı ve kârın sıfır olduğu hacimdir.

- Başabaş adedi = Sabit giderler ÷ Birim katkı payı

**Faaliyet kaldıracı.** Sabit giderler değişmezken hacim artınca kâr, hacimden daha hızlı artar. Belirli bir hacimde kaldıraç derecesi şöyle hesaplanır:

- Faaliyet kaldıracı derecesi = Toplam katkı payı ÷ Faaliyet kârı

Derece 6 ise hacimdeki %1'lik değişim kârı yaklaşık %6 değiştirir. Bu iki yönlü çalışır: Hacim düşünce kâr da aynı hızla erir.

**İndirim ve gereken hacim.** Fiyat indirimi doğrudan katkı payından düşer. Katkı payı oranı %30 olan bir üründe %5 fiyat indirimi, birim katkıyı %5 değil yaklaşık %17 azaltır. Aynı toplam katkıyı korumak için gereken hacim formülü:

- Gereken hacim = Eski toplam katkı ÷ Yeni birim katkı

**İlgili maliyet ilkesi.** Bir karar verirken yalnızca o karar yüzünden değişecek gelir ve giderlere bakın. Zaten var olan ve karardan etkilenmeyen sabit giderleri birim başına dağıtıp karara katmak, kârlı bir siparişi reddetmenize yol açabilir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek bir ürüne ait değildir; hesaplar `scripts/cards_numbers_fmcg_b1.py` ile yapılmıştır.

Bir ürün: fiyat 30,00 TL, değişken maliyet 21,00 TL, aylık sabit gider 450.000 TL.

- Birim katkı payı: 30,00 − 21,00 = **9,00 TL**; katkı payı oranı **%30,00**
- Başabaş: 450.000 ÷ 9 = **50.000 adet**, yani **1.500.000 TL** ciro
- 60.000 adette kâr: 9 × 60.000 − 450.000 = **90.000 TL**
- Faaliyet kaldıracı derecesi: 540.000 ÷ 90.000 = **6,00**
- Hacim %10 artarsa (66.000 adet): kâr **144.000 TL**, yani **%60,00** artış

Şimdi %5 indirim önerisi geliyor. Yeni fiyat 28,50 TL, birim katkı payı **7,50 TL**. Mevcut 540.000 TL'lik toplam katkıyı korumak için 540.000 ÷ 7,50 = **72.000 adet** satmak gerekir; bu **%20,00** hacim artışı demektir. Promosyonun bu artışı getireceğine dair bir veriniz yoksa indirim kârı düşürür.

## Sık yapılan hatalar

- Katkı payı oranı ile brüt kâr oranını karıştırmak; nakliye ve satış primlerini unutmak.
- İndirimin katkıya etkisini fiyat yüzdesiyle aynı sanmak.
- Yüksek kaldıraçlı bir işte hacim düşüşünün kârı ne kadar hızlı eriteceğini planlamamak.
- Sabit giderleri birime dağıtıp "bu ürün zarar ediyor" diyerek katkı yaratan ürünü çıkarmak.
- Promosyondaki ek hacmin bir kısmının sonraki haftalardan çalındığını hesaba katmamak.

## Pratikte nasıl uygulanır?

- [ ] Ana ürünleriniz için birim değişken maliyeti finansla birlikte netleştirin ve birim katkı payını listeleyin.
- [ ] Her indirim talebinde "aynı katkı için gereken hacim artışı" rakamını hesaplayıp onay formuna yazın.
- [ ] Aylık başabaş hacminizi bilin ve satış ekibiyle paylaşın.
- [ ] Bütçede faaliyet kaldıracı derecesini hesaplayın; hacim %5 ve %10 düşerse kârın ne olacağını görün.
- [ ] Ürün çıkarma kararlarında yalnızca gerçekten ortadan kalkacak maliyetleri hesaba katın.

## Daha fazlası

- Brealey, R. A.; Myers, S. C.; Allen, F. (2020). *Principles of Corporate Finance.* (kaynak doğrulanmadı)
- Kaplan, R. S.; Cooper, R. (1998). *Cost & Effect: Using Integrated Cost Systems to Drive Profitability and Performance.* (kaynak doğrulanmadı)
