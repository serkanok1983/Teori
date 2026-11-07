---
id: kb-fmcg-2-4-roi-roce-npv
title: "ROI, ROCE ve net bugünkü değer: Bir soğutucu yatırımı kendini öder mi?"
summary: "Soğutucu, teşhir ünitesi ya da yeni bir araç gibi yatırımlar bugün nakit çıkışı, yarın nakit girişi demektir. Bu kart basit ROI, geri ödeme süresi, net bugünkü değer ve ROCE'yi tek bir saha örneğiyle karşılaştırır."
course: fmcg
category: ticari-finans
tags: [nakit, butce, isletme-sermayesi, enflasyon]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [FMCG-2.4]
reading_minutes: 3
key_points:
  - "Basit ROI ve geri ödeme süresi hızlı fikir verir ama paranın zaman değerini hesaba katmaz."
  - "Net bugünkü değer, gelecekteki nakit akışlarını sermaye maliyetiyle bugüne indirger; sıfırın üzerindeyse yatırım değer yaratır."
  - "Yüksek enflasyon döneminde iskonto oranı ve nakit akışları aynı bazda (ikisi de nominal ya da ikisi de reel) olmalıdır."
  - "ROCE, işletmenin bağladığı tüm sermayenin ne kadar faaliyet kârı ürettiğini gösterir; bayi kârlılığını karşılaştırmanın temel ölçüsüdür."
glossary_terms: [net-bugunku-deger, geri-odeme-suresi, roce, yatirimin-getirisi, isletme-sermayesi]
related: [kb-eco-25-1-time-value-npv-irr, kb-eco-31-1-capital-budgeting, kb-fmcg-7-2-distributor-roi, kb-fmcg-2-3-contribution-breakeven, kb-eco-32-4-finance-in-high-inflation]
sources:
  - title: "Principles of Corporate Finance"
    authors: "Brealey, R. A.; Myers, S. C.; Allen, F."
    year: 2020
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

Saha ekibi "bu markete soğutucu koyalım, satış artar" der; finans ekibi "kaç ayda geri döner?" diye sorar. İki taraf da haklıdır ama doğru cevap için ortak bir hesap gerekir. Bu kart, satış noktası ekipmanı, araç, depo ya da bayi yatırımı gibi kararlarda kullanılan dört ölçüyü verir ve hangisinin ne zaman yanıltıcı olduğunu gösterir.

## Temel fikir

**Basit ROI** (*return on investment*): Yatırımın ömrü boyunca elde edilen toplam net kazancın yatırıma oranı. Kolay anlaşılır ama paranın zaman değerini yok sayar. Bugünkü 1 TL ile beş yıl sonraki 1 TL'yi eşit sayar.

**Geri ödeme süresi:** Yatırımın kendi nakit akışıyla kaç yılda (ayda) geri döndüğü. Risk ve nakit sıkışıklığı için iyi bir ilk göstergedir, ama geri ödemeden sonraki kazancı görmez.

**Net bugünkü değer (NBD)** (*net present value*): Gelecek yıllarda beklenen nakit akışlarının, şirketin sermaye maliyetiyle bugüne indirgenmiş toplamından yatırım tutarının çıkarılmasıdır. Brealey, Myers ve Allen'ın kurumsal finans kitabı başta olmak üzere finans literatürünün temel karar kuralıdır: NBD sıfırdan büyükse yatırım değer yaratır.

NBD = −Yatırım + Σ (Yıl t nakit akışı ÷ (1 + r)^t)

**Enflasyon notu.** Yüksek enflasyon ortamında iskonto oranı yüksek olur ve uzak yılların nakit akışı bugün çok az değer taşır. Kural basittir: Nakit akışlarını nominal (enflasyonlu) tahmin ettiyseniz nominal iskonto oranı kullanın; reel tahmin ettiyseniz reel oran kullanın. İkisini karıştırmak en sık yapılan hatadır.

**ROCE** (*return on capital employed*): Faaliyet kârının işletmede kullanılan toplam sermayeye (duran varlıklar artı işletme sermayesi) oranı. Tek bir yatırımı değil, bütün işletmeyi değerlendirir. Bayi için stok ve alacakla bağlanan para çoğu zaman araç ve depodan büyüktür; bu yüzden ROCE'yi düşüren en büyük kalem işletme sermayesidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek bir yatırıma ait değildir; hesaplar `scripts/cards_numbers_fmcg_b1.py` ile yapılmıştır.

Bir markete 25.000 TL'lik soğutucu konuyor. Beklenti: ayda 20 koli ek satış, koli başı katkı payı 60 TL, aylık bakım 150 TL. Ömür 5 yıl, yıllık iskonto oranı %35 (nominal).

- Yıllık net nakit: (20 × 60 − 150) × 12 = **12.600 TL**
- Geri ödeme süresi: 25.000 ÷ 12.600 = **1,98 yıl**
- Basit ROI (5 yıl): (12.600 × 5 − 25.000) ÷ 25.000 = **%152,00**
- NBD (%35): **2.972 TL**

Basit ROI çok parlak görünüyor, NBD ise yatırımın ancak az farkla değer yarattığını söylüyor. Şimdi ek satışın 20 değil 10 koli olduğunu varsayın:

- Yıllık net nakit **5.400 TL**, geri ödeme **4,63 yıl**, NBD **−13.012 TL**.

Yatırımın kaderi, ek satış tahmininin doğruluğuna bağlıdır. Soğutucuyu koymadan önce benzer noktalarda gerçekleşen artışı ölçmek gerekir.

Aynı mantık bayi düzeyinde: Yıllık faaliyet kârı 3.600.000 TL, kullanılan sermaye 18.000.000 TL olan bir bayinin ROCE'si **%20,00**'dır. Bu oranın sermaye maliyetinin altında kalması, işletmenin büyüdükçe değer kaybettiği anlamına gelir.

## Sık yapılan hatalar

- Yalnızca basit ROI'ye bakıp zaman değerini yok saymak.
- Nominal nakit akışını reel iskonto oranıyla (ya da tersini) indirgemek.
- Ek satışı, ekipman olmadan da gerçekleşecek satışla karıştırmak.
- Bakım, sigorta, enerji ve geri toplama maliyetlerini unutmak.
- Bayi kârlılığını cironun yüzdesi olarak konuşup bağlanan sermayeyi görmemek.

## Pratikte nasıl uygulanır?

- [ ] Ekipman yatırımı talepleri için tek tip bir form kullanın: yatırım, aylık ek koli, katkı payı, işletme gideri, ömür.
- [ ] Finans ekibinden şirketin kullandığı iskonto oranını ve bunun nominal mi reel mi olduğunu öğrenin.
- [ ] Her talep için hem NBD'yi hem de geri ödeme süresini raporlayın; düşük ve yüksek satış senaryosu ekleyin.
- [ ] Yerleştirilen ekipmanlarda gerçekleşen ek satışı 6 ay sonra ölçün ve tahmin yöntemini düzeltin.
- [ ] Bayi olarak yıllık ROCE hesaplayın; stok gün sayısı ve alacak tahsil süresinin ROCE'ye etkisini görün.

## Daha fazlası

- Brealey, R. A.; Myers, S. C.; Allen, F. (2020). *Principles of Corporate Finance.* (kaynak doğrulanmadı)
