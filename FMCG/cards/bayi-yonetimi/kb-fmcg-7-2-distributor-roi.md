---
id: kb-fmcg-7-2-distributor-roi
title: "Dağıtıcının sermaye getirisi: Kâr, bağlanan sermayeye değiyor mu?"
summary: "Dağıtıcı için asıl soru kâr değil, işe bağladığı sermayenin getirisidir. Bu kart dağıtıcının sermayesini alacak, stok, borç ve duran varlıklarla hesaplamayı, sermaye getirisini sermaye maliyetiyle karşılaştırmayı ve vadenin getiriyi nasıl değiştirdiğini anlatır."
course: fmcg
category: bayi-yonetimi
tags: [dagitim, finans]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, finans-muduru]
level: orta
source_lessons: [FMCG-7.2]
reading_minutes: 3
key_points:
  - "Dağıtıcının kullandığı sermaye büyük ölçüde alacak ve stoktan, eksi tedarikçi borçlarından oluşur."
  - "Kullanılan sermaye getirisi, faaliyet kârının kullanılan sermayeye oranıdır."
  - "Getiri sermaye maliyetinin altındaysa dağıtıcı kâr ediyor görünse de değer kaybediyordur."
  - "Müşteri vadesini kısaltmak ya da üretici vadesini uzatmak, kârı değiştirmeden getiriyi artırabilir."
glossary_terms: [roce, isletme-sermayesi, vade]
related: [kb-fmcg-7-1-distributor-pnl, kb-fmcg-7-3-credit-collections-dso, kb-fmcg-2-4-roi-roce-npv, kb-fmcg-7-4-distributor-selection-kpis, kb-fmcg-12-7-case-distributor-turnaround]
sources:
  - title: "Principles of Corporate Finance"
    authors: "Brealey, R. A.; Myers, S. C.; Allen, F."
    year: 2020
    type: book
    verified: false
    note: "Kitap; baskı yılı kontrol edilmedi."
  - title: "Marketing Channels"
    authors: "Coughlan, A. T.; Anderson, E.; Stern, L. W.; El-Ansary, A. I."
    year: 2006
    type: book
    verified: false
    note: "Kitap; baskı yılı kontrol edilmedi."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Bir dağıtıcı yılda 1,3 milyon TL kâr ediyor olabilir. Ama bu kâr için 8 milyon TL'lik sermaye bağlıyorsa ve aynı parayı başka bir yerde daha yüksek getiriyle değerlendirebiliyorsa, işi sürdürmek için güçlü bir nedeni yoktur. Bu kart, dağıtıcının ekonomisini sermaye açısından okumanızı sağlar.

## Temel fikir

**Kullanılan sermaye.** Dağıtıcının işe bağladığı para kabaca şöyle hesaplanır:

- **Alacaklar:** Perakendecilerin henüz ödemediği satışlar.
- **Stok:** Depodaki ve araçtaki ürünler.
- **Eksi tedarikçi borçları:** Üreticiye henüz ödenmemiş alışlar.
- **Artı duran varlıklar:** Araçlar, depo ekipmanı.

İlk üç kalem, işletme sermayesidir.

**Kullanılan sermaye getirisi** (ROCE) = faaliyet kârı / kullanılan sermaye. Brealey, Myers ve Allen'ın kurumsal finans yaklaşımına göre bir yatırımın değer yaratması için getirisinin sermaye maliyetinin üstünde olması gerekir. Sermaye maliyeti, dağıtıcının borçlanma faizi ve ortakların beklediği getiriyle belirlenir. Yüksek faiz ortamında bu eşik yükselir.

**Ekonomik kâr.** Faaliyet kârı − (kullanılan sermaye × sermaye maliyeti). Negatifse dağıtıcı muhasebede kâr etse bile değer kaybediyordur.

**Vadenin etkisi.** Perakendeciye verilen vade uzadıkça alacak büyür, sermaye artar, getiri düşer. Üreticinin dağıtıcıya verdiği vade uzadıkça borç büyür, sermaye azalır, getiri artar.

**Sermayeyi azaltmanın yolları.** Dağıtıcının sermaye getirisi yalnızca kâr artırılarak değil, bağlanan sermaye azaltılarak da iyileşir. Stok gün sayısını düşürmek için üreticiyle daha sık ve daha küçük teslimat, yavaş dönen ürünlerin listeden çıkarılması ve talep tahmininin paylaşılması değerlendirilebilir. Alacak gün sayısını düşürmek için kredi limitleri, erken ödeme iskontosu ve düzenli tahsilat takibi kullanılır. Üreticiye olan borcun vadesi de önemlidir; ancak üreticinin vadeyi uzatması, sermayeyi üreticiye kaydırır. Bu nedenle sermaye getirisi konuşması, üretici ile dağıtıcının birlikte bakması gereken bir konudur; ortak iş planında yer almalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Satış, vade, stok ve sermaye maliyeti varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b4.py` ile yapılmıştır.

Bir önceki karttaki dağıtıcı: satış 60.000.000 TL, faaliyet kârı 1.320.000 TL, satılan malın maliyeti 54.600.000 TL.

| Kalem | Varsayım | Tutar |
|---|---|---|
| Alacak | 45 gün satış | 7.397.260 TL |
| Stok | 20 gün maliyet | 2.991.781 TL |
| Tedarikçi borcu | 30 gün maliyet | −4.487.671 TL |
| Duran varlık | | 2.000.000 TL |
| **Kullanılan sermaye** | | **7.901.370 TL** |

- ROCE: 1.320.000 / 7.901.370 = **%16,7**
- Sermaye maliyeti %35 ise: 7.901.370 × 0,35 = 2.765.479 TL
- Ekonomik kâr: **−1.445.479 TL**

Perakendeci vadesi 30 güne inerse sermaye **5.435.616 TL**'ye, ROCE **%24,3**'e çıkar. Yine de sermaye maliyetinin altında. Bu dağıtıcının sürdürülebilir olması için marj, gider ve vade birlikte ele alınmalıdır.

## Sık yapılan hatalar

- **Yalnızca kâra bakmak.** Kârın kaç liralık sermayeyle üretildiği görülmezse dağıtıcının durumu anlaşılmaz.
- **Vadeyi bedava saymak.** Perakendeciye verilen her ek vade günü dağıtıcının sermayesini artırır.
- **Sermaye maliyetini düşük faiz döneminden kalma bir rakamla almak.** Faizler değiştiğinde eşik de değişir.

## Pratikte nasıl uygulanır?

- [ ] Dağıtıcılarınızın alacak, stok ve borç günlerini düzenli olarak öğrenin.
- [ ] Her dağıtıcı için kullanılan sermayeyi ve ROCE'yi kabaca hesaplayın.
- [ ] Vade ve stok günlerinde iyileştirme hedefleri koyun; üretici olarak siz de ödeme koşullarınızı bu hesapla değerlendirin.
- [ ] Ekonomik kârı negatif olan dağıtıcılar için bir iyileştirme planı hazırlayın.

## Daha fazlası

- Brealey, R. A.; Myers, S. C.; Allen, F. (2020). *Principles of Corporate Finance.* (kaynak doğrulanmadı)
- Coughlan, A. T.; Anderson, E.; Stern, L. W.; El-Ansary, A. I. (2006). *Marketing Channels.* (kaynak doğrulanmadı)
