---
id: kb-ea-26-6-dms-secondary-sales
title: "Distribütör yönetim sistemi (DMS): İkincil satış verisi ve talep yönetimi"
summary: "Üretici ile distribütör arasında veri paylaşımını sağlayan distribütör yönetim sistemlerini; ikincil satış (sell-out) görünürlüğünü, distribütör stoğunun izlenmesini ve promosyon ile iskonto taleplerinin doğrulanmasını anlatır."
course: ea
category: saha-satis-ve-dms
tags: [dms, distributor, ikincil-satis, talep, veri-paylasimi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, it-yoneticisi]
level: orta
source_lessons: [EA-26.6]
reading_minutes: 3
key_points:
  - "Birincil satış üreticiden distribütöre, ikincil satış distribütörden noktalara yapılan satıştır."
  - "DMS, distribütörün satış, stok ve müşteri verisini üreticiyle standart biçimde paylaşır."
  - "İkincil satış verisi gerçek talebi, birincil satış ise kanala yüklemeyi gösterir."
  - "Promosyon talepleri ikincil satış verisiyle doğrulanabilir."
  - "Veri paylaşımı için ortak ürün ve nokta kodları şarttır."
glossary_terms: [dms, ikincil-satis, birincil-satis]
related: [kb-fmcg-7-4-distributor-selection-kpis, kb-fmcg-7-1-distributor-pnl, kb-ea-26-5-van-sales-presales, kb-ea-27-2-tpm-promotion-settlement, kb-ea-29-2-demand-planning-systems]
sources:
  - title: "Information Distortion in a Supply Chain: The Bullwhip Effect"
    authors: "Lee, H.; Padmanabhan, V.; Whang, S."
    year: 1997
    type: article
    doi: "10.1287/mnsc.43.4.546"
    url: "https://doi.org/10.1287/mnsc.43.4.546"
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

Üretici, distribütöre ne sattığını bilir; ama ürünün noktalara ne kadar, hangi fiyatla ve ne zaman satıldığını çoğu zaman bilmez. Bu kart, **distribütör yönetim sistemlerinin** (DMS) bu boşluğu nasıl kapattığını anlatır.

## Temel fikir

**Birincil ve ikincil satış.**

- **Birincil satış (sell-in):** Üreticiden distribütöre satış.
- **İkincil satış (sell-out):** Distribütörden bakkal, market ve diğer noktalara satış.

Birincil satış dönem sonu hedef baskısıyla şişebilir; ikincil satış gerçek tüketici talebine daha yakındır. Lee, Padmanabhan ve Whang (1997), tedarik zincirinde talep bilgisinin paylaşılmamasının sipariş dalgalanmalarını büyüttüğünü (kamçı etkisi) gösterir. İkincil satış verisinin paylaşımı bu etkiyi azaltmanın bir yoludur.

**DMS ne yapar?** Distribütörün satış, stok, nokta ve tahsilat işlerini yürüten bir sistemdir. Üretici tarafından sağlandığında veya üreticiye standart veri aktardığında:

- Nokta bazında ikincil satış,
- Distribütör stoğu ve stok gün sayısı,
- Kampanya uygulama ve iskonto verisi,
- Nokta sayısı ve aktif nokta oranı üretici tarafından görülebilir.

**Talep (claim) yönetimi.** Distribütörler üreticiden promosyon, fiyat farkı ve iskonto bedeli talep eder. DMS'teki ikincil satış verisi, talebin gerçekten kampanya kapsamındaki satışlara dayanıp dayanmadığını doğrulamayı sağlar.

**Ön koşul:** Ortak ürün kodları (ör. barkod), ortak nokta kodları ve düzenli veri aktarım takvimi.

### DMS projesinde dikkat edilecek noktalar

DMS, üretici ile distribütörler arasında veri paylaşımına dayanır. Bu ilişki ticari ve teknik boyutlarıyla birlikte yönetilmelidir:

- **Veri paylaşım sözleşmesi:** Distribütörün hangi verileri, hangi sıklıkta ve hangi ayrıntı düzeyinde paylaşacağı sözleşmede yer almalıdır. Distribütörün kendi müşteri verilerinin üretici tarafından nasıl kullanılacağı da açıkça tanımlanmalıdır.
- **Ana veri eşleştirmesi:** Distribütörlerin ürün kodları ve müşteri kodları, üreticinin kodlarıyla eşleştirilmelidir. Bu eşleştirme yapılmadan ikincil satış verisi analiz edilemez.
- **Veri kalitesi kontrolleri:** Gelen veride eksik dönemler, olağan dışı miktarlar ve tanımsız kodlar otomatik olarak işaretlenmelidir. Birincil ve ikincil satışlar ile distribütör stoku arasındaki tutarlılık kontrol edilmelidir.
- **Distribütöre fayda:** Distribütörün sisteme veri girişi, kendisi için de değer üretmelidir: stok yönetimi, sipariş önerileri, promosyon mahsuplaşmasının hızlanması gibi.

**Kamçı etkisi ile ilişkisi.** Lee, Padmanabhan ve Whang'ın tarif ettiği kamçı etkisi, tedarik zincirinin üst halkalarında talep dalgalanmasının büyümesidir. İkincil satış verisi, üreticinin gerçek tüketici talebini doğrudan görmesini sağlayarak bu etkiyi azaltmaya yardımcı olur. Bunun için ikincil satış verisinin talep planlamasına girdi olarak kullanılması gerekir.

**Promosyon talepleri.** Distribütörlerin promosyon talepleri, ikincil satış verisiyle doğrulanabildiğinde mahsuplaşma hızlanır ve itirazlar azalır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b6.py` ile yapılmıştır.

Bir üretici, bir çeyrekte distribütörüne 120.000 koli satıyor. DMS verisine göre distribütörün noktalara satışı 108.000 koli. Fark **12.000** koli, birincil satışın **%10,0**'ı; kanal stoğu birikiyor. Aynı dönemde distribütörün 450.000 TL'lik promosyon talebinin 405.000 TL'si ikincil satış verisiyle doğrulanıyor; **45.000,00 TL** (**%10,0**) kampanya dışı satışlara ait olduğu için reddediliyor.

## Sık yapılan hatalar

- Hedefleri yalnızca birincil satışa göre koymak.
- Distribütörlerden farklı biçimlerde Excel toplamak.
- Ürün ve nokta kodlarını eşlemeden veriyi birleştirmeye çalışmak.
- Promosyon taleplerini veri olmadan ödemek.

## Pratikte nasıl uygulanır?

- [ ] Distribütörlerle veri paylaşımı kapsamını ve sıklığını sözleşmeye yazın.
- [ ] Ortak ürün ve nokta kodlama standardı belirleyin.
- [ ] Birincil ve ikincil satışı aynı raporda izleyin.
- [ ] Talep doğrulamayı ikincil satış verisine bağlayın.

## Daha fazlası

- Lee, Padmanabhan ve Whang (1997), *Management Science*. https://doi.org/10.1287/mnsc.43.4.546
