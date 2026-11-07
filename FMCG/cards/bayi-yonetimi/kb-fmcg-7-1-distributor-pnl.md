---
id: kb-fmcg-7-1-distributor-pnl
title: "Dağıtıcının kâr-zarar tablosu: %9 marjla nasıl para kazanılır?"
summary: "Dağıtıcının brüt marjı birkaç yüzde puandır ve giderlerin çoğu bu marjdan karşılanır. Bu kart tipik bir dağıtıcı kâr-zarar tablosunu, gider kalemlerini ve üreticinin dağıtıcı kârlılığını neden izlemesi gerektiğini anlatır."
course: fmcg
category: bayi-yonetimi
tags: [dagitim, finans, maliyet]
roles: [bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: temel
source_lessons: [FMCG-7.1]
reading_minutes: 3
key_points:
  - "Dağıtıcının geliri, alış ve satış fiyatı arasındaki marj ile üreticiden aldığı destek ve primlerden oluşur."
  - "Personel, araç, depo ve şüpheli alacaklar marjın büyük kısmını tüketir; faaliyet kârı çoğu zaman satışın birkaç yüzdesidir."
  - "Küçük bir gider artışı ya da marj kaybı, dağıtıcının kârını hızla sıfıra yaklaştırabilir."
  - "Kârsız dağıtıcı yatırım yapmaz, nokta atlar ve sonunda işi bırakır; bu üreticinin de sorunudur."
glossary_terms: [bayi, katki-payi, hizmet-maliyeti]
related: [kb-fmcg-7-2-distributor-roi, kb-fmcg-7-3-credit-collections-dso, kb-fmcg-6-4-direct-vs-indirect, kb-fmcg-1-1-margin-stack, kb-fmcg-7-5-distributor-development]
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

Üretici dağıtıcıdan daha fazla nokta, daha sık ziyaret ve daha uzun vade ister. Bu taleplerin her biri dağıtıcının kâr-zarar tablosunda bir gider satırıdır. Bu kart, dağıtıcının nasıl para kazandığını görmenizi ve taleplerinizi gerçekçi kurmanızı sağlar.

## Temel fikir

**Gelir tarafı.**

- **Brüt marj:** Dağıtıcının üreticiden alış fiyatı ile perakendeciye satış fiyatı arasındaki fark.
- **Üretici destekleri:** Hedef primleri, lojistik ya da kapsama destekleri, promosyon katkıları.

**Gider tarafı.**

- **Personel:** Satış temsilcileri, sürücüler, depo çalışanları, tahsilat ve yönetim.
- **Araç ve yakıt:** Kira ya da amortisman, bakım, yakıt, sigorta.
- **Depo:** Kira, enerji, ekipman.
- **Şüpheli alacaklar:** Tahsil edilemeyen alacaklar.
- **Diğer:** Bilgi sistemi, ofis, muhasebe.

Coughlan ve arkadaşlarının kanal yaklaşımına göre dağıtıcı, üstlendiği işlevler karşılığında marj kazanır. Bu işlevlerin maliyeti marjı aşarsa dağıtıcı ya işlevleri azaltır ya da kanaldan çıkar.

**Kâr ve finansman.** Faaliyet kârı, finansman giderlerinden önce hesaplanır. Dağıtıcı alacak ve stok için genellikle borçlanır. Yüksek faiz ortamında finansman gideri faaliyet kârının önemli bir kısmını yiyebilir.

**Kâr-zarar tablosunu okumak.** Dağıtıcının tablosunu değerlendirirken üç soruyu sorun. Birincisi, brüt marjın ne kadarı üreticiden gelen primlere ve hedef bağlantılı ödemelere bağlı? Bu kısım hedefler tutmazsa kaybolur ve dağıtıcının kârını oynak hâle getirir. İkincisi, en büyük gider kalemleri (personel, araç ve yakıt, depo) satışla birlikte mi artıyor, yoksa sabit mi? Sabit giderlerin payı yüksekse hacim düşüşü kârı hızla eritir. Üçüncüsü, finansman gideri ve şüpheli alacak karşılıkları tabloda açıkça yer alıyor mu? Yüksek faiz dönemlerinde bu kalemler faaliyet kârının önemli bir kısmını tüketebilir. Bu soruların yanıtları, üreticinin destek paketini nereye yönlendirmesi gerektiğini gösterir.

Dağıtıcıyla bu tabloyu birlikte incelemek, üreticinin dağıtıcıdan beklentilerini gerçekçi kılar: Kapsama ya da ziyaret sıklığı artışı isteniyorsa, bunun gider tarafındaki karşılığı da konuşulmalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Satış, marj ve giderler varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b4.py` ile yapılmıştır.

Yıllık satışı 60.000.000 TL olan bir dağıtıcı:

| Kalem | Tutar |
|---|---|
| Brüt marj (%9) | 5.400.000 TL |
| Üretici destekleri (%1,2) | 720.000 TL |
| Personel | −2.400.000 TL |
| Araç ve yakıt | −1.100.000 TL |
| Depo | −600.000 TL |
| Şüpheli alacak | −300.000 TL |
| Diğer | −400.000 TL |
| **Faaliyet kârı** | **1.320.000 TL (%2,20)** |

Satışın yalnızca %2,20'si faaliyet kârı. Üretici marjı bir puan düşürürse (600.000 TL) ya da dağıtıcıdan iki temsilci daha isterse, kârın yarısı gider. Üstelik bu kâr, alacak ve stok için kullanılan borcun faizinden önce hesaplanmıştır.

## Sık yapılan hatalar

- **Dağıtıcı marjını yüksek sanmak.** %9 brüt marj, giderlerden sonra çok küçük bir kâra dönüşebilir.
- **Ek talepleri ücretsiz saymak.** Her ek nokta, ziyaret ve vade gününün bir maliyeti vardır.
- **Destekleri tek seferlik vermek.** Kalıcı bir hizmet bekliyorsanız kalıcı bir destek modeli kurun.
- **Dağıtıcının tablosunu hiç görmemek.** Kârsızlık, ancak dağıtıcı işi bırakmaya karar verdiğinde fark edilir.

## Pratikte nasıl uygulanır?

- [ ] Dağıtıcılarınızla yıllık olarak, mümkünse özet bir kâr-zarar tablosu üzerinden konuşun.
- [ ] Her yeni talebin (nokta, ziyaret, vade, ekip) dağıtıcıya maliyetini hesaplayın.
- [ ] Desteklerinizi ölçülebilir hizmet hedeflerine bağlayın.
- [ ] Dağıtıcı kârlılığını, satış büyümesi ve kapsama ile birlikte izleyin.

## Daha fazlası

- Coughlan, A. T.; Anderson, E.; Stern, L. W.; El-Ansary, A. I. (2006). *Marketing Channels.* (kaynak doğrulanmadı)
