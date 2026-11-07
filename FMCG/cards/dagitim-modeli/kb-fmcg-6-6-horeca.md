---
id: kb-fmcg-6-6-horeca
title: "Horeca kanalı: Otel, restoran ve kafelere satış"
summary: "Horeca, ürünün evde değil dışarıda tüketildiği kanaldır ve kendine özgü bir satın alma, hizmet ve yatırım mantığı vardır. Bu kart kanalın özelliklerini, ekipman yatırımlarının hesabını ve sözleşmeli hacim taahhütlerini anlatır."
course: fmcg
category: dagitim-modeli
tags: [dagitim, horeca, saha-satis, finans]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: temel
source_lessons: [FMCG-6.6]
reading_minutes: 3
key_points:
  - "Horeca'da müşteri işletmedir, ama son kararı çoğu zaman tüketici menüde ya da tezgâhta verir."
  - "Kanal, ambalaj, hizmet sıklığı ve ödeme koşulları açısından perakendeden farklıdır."
  - "Ekipman ve görünürlük yatırımları yaygındır; geri dönüşleri sözleşmeli hacim taahhüdüne bağlanmalıdır."
  - "Bir işletmeye yatırım kararını, beklenen hacmin katkısı ve geri ödeme süresiyle verin."
glossary_terms: [horeca, geri-odeme-suresi, katki-payi]
related: [kb-fmcg-6-1-rtm-channels-formats, kb-fmcg-6-5-wholesale-cash-carry, kb-fmcg-2-4-roi-roce-npv, kb-fmcg-6-3-cost-to-serve, kb-fmcg-7-3-credit-collections-dso]
sources:
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

Kahve, içecek, dondurma, yağ ve un gibi kategorilerde horeca satışın önemli bir kısmını oluşturabilir. Bu kanalda işletmeye ekipman vermek, menüde yer almak ve sürekli tedarik sağlamak, perakendeden farklı becerilere dayanır. Bu kart, horeca satışının temel mantığını ve yatırım kararlarının hesabını anlatır.

## Temel fikir

**Horeca** (*hotel, restaurant, café*). Otel, restoran, kafe, kantin ve yemek şirketleri gibi ürünün dışarıda tüketildiği noktalardır.

**Farklar.**

- **Karar verici:** İşletme sahibi, şef ya da satın alma sorumlusu ürünü seçer; tüketici menüden ya da tezgâhtan seçer. İki tarafı da ikna etmek gerekir.
- **Ambalaj:** Büyük ambalajlar, profesyonel ürünler ve bazen işletmeye özel formatlar.
- **Hizmet:** Sık ve küçük teslimat, bazen acil sipariş, ekipman bakımı ve personel eğitimi.
- **Satın alma kanalı:** Doğrudan, dağıtıcı üzerinden, toptancıdan ya da nakit-ve-taşı mağazasından.
- **Ödeme:** Tahsilat riski işletmeye göre çok değişir; küçük işletmelerde risk yüksek olabilir.

**Yatırım.** Kahve makinesi, içecek soğutucusu, dondurma dolabı, şemsiye, menü desteği gibi yatırımlar yaygındır. Coughlan ve arkadaşlarının kanal yaklaşımında olduğu gibi, bu yatırımlar kanal üyesine bir işlevi daha iyi yapması için verilen kaynaklardır. Karşılığında işletmeden bir hacim ya da münhasırlık taahhüdü alınır. Münhasırlık şartları rekabet hukuku açısından sınırlara tabi olabilir; büyük pazar payınız varsa hukukçunuza danışın.

**Geri ödeme süresi.** Bir ekipman yatırımının değerlendirilmesinde en basit gösterge, yatırımın aylık katkıyla kaç ayda geri döneceğidir.

**Horeca'da satış ve hizmet.** Horeca müşterileri çoğu zaman ürünle birlikte hizmet bekler: düzenli ve zamanında teslimat, ekipmanın bakımı, personel eğitimi, menüde görünürlük. Bu nedenle horeca satışında temsilcinin rolü, ürün siparişi almanın ötesindedir. Zincir oteller ve restoranlar merkezi satın alma ile çalışabilir; bağımsız işletmelerde ise karar genellikle işletme sahibi ya da şefindir. Horeca müşterileri sezonsallıktan güçlü etkilenir; turistik bölgelerde talep yaz aylarında yoğunlaşır. Ekipman sözleşmelerinde mülkiyet, bakım sorumluluğu ve münhasırlık koşulları hukuk danışmanıyla kontrol edilmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Ekipman maliyeti, hacim ve katkı varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b3.py` ile yapılmıştır.

Bir kafeye 60.000 TL değerinde bir kahve makinesi veriyorsunuz. Kafe ayda 20 kg kahve alacağını taahhüt ediyor. Kilogram başına katkınız 150 TL.

- Aylık katkı: 20 × 150 = **3.000 TL**
- Geri ödeme süresi: 60.000 / 3.000 = **20,0 ay**

Kafe ayda yalnızca 12 kg alırsa geri ödeme **33,3 aya** uzar. Makinenin ömrü ve bakım maliyeti düşünüldüğünde bu, yatırımı zarara çevirebilir. Bu yüzden sözleşmede asgari hacmi, taahhüt tutmazsa ekipmanın geri alınmasını ve bakım sorumluluğunu açıkça yazın.

## Sık yapılan hatalar

- **Taahhütsüz ekipman vermek.** Ekipman işletmede kalır, ürün rakipten alınır.
- **Hacim taahhüdünü izlememek.** Sözleşme yazılır, ama aylık alımlar kontrol edilmez.
- **Tahsilat riskini küçümsemek.** Horeca'da işletme kapanmaları ve el değiştirmeler sık olabilir.
- **Personeli unutmak.** Ürünü doğru hazırlamayan personel, tüketici deneyimini ve tekrar siparişi bozar.

## Pratikte nasıl uygulanır?

- [ ] Horeca noktalarını potansiyel ve işletme tipine göre gruplayın.
- [ ] Her yatırım için beklenen hacmi, katkıyı ve geri ödeme süresini hesaplayın; bir azami geri ödeme süresi belirleyin.
- [ ] Sözleşmelerde hacim, süre, ekipman iadesi ve bakım koşullarını yazılı tanımlayın.
- [ ] Aylık alımları taahhütle karşılaştıran bir rapor kurun.
- [ ] Kritik noktalarda personel eğitimi ve hizmet ziyaretleri planlayın.

## Daha fazlası

- Coughlan, A. T.; Anderson, E.; Stern, L. W.; El-Ansary, A. I. (2006). *Marketing Channels.* (kaynak doğrulanmadı)
