---
id: kb-fmcg-6-1-rtm-channels-formats
title: "Pazara giriş modeli: Kanallar, formatlar ve her birinin ekonomisi"
summary: "Ürünlerinizin tüketiciye hangi kanallardan ve kim aracılığıyla ulaştığı, hem satışınızı hem marjınızı belirler. Bu kart başlıca kanal ve formatları, her birinin farklı ihtiyaçlarını ve kanal karmasının toplam marja etkisini anlatır."
course: fmcg
category: dagitim-modeli
tags: [dagitim, perakende, strateji]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: temel
source_lessons: [FMCG-6.1]
reading_minutes: 3
key_points:
  - "Pazara giriş modeli, ürünün tüketiciye hangi kanallardan, hangi aracılarla ve hangi hizmet düzeyiyle ulaştığını tanımlar."
  - "Her kanalın sipariş büyüklüğü, ziyaret ihtiyacı, ödeme davranışı ve marj yapısı farklıdır."
  - "Kanal karması değiştiğinde toplam marj da değişir; büyüyen kanalın marjı düşükse büyüme kârı azaltabilir."
  - "Her kanala aynı ürün, fiyat ve hizmeti vermek yerine kanala göre tasarım yapın."
glossary_terms: [pazara-giris-modeli, kanal-islevleri, zincir-magaza]
related: [kb-fmcg-6-2-outlet-universe-segmentation, kb-fmcg-6-3-cost-to-serve, kb-fmcg-6-4-direct-vs-indirect, kb-fmcg-1-3-channel-actors, kb-fmcg-6-8-rtm-design-case]
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

Bir üreticinin satışı ulusal zincirlerden, yerel zincirlerden, bakkal ve büfelerden, indirim marketlerinden, toptancılardan ve çevrim içi kanallardan gelir. Bu kanalların her biri farklı bir ekonomiyle çalışır. Bu kart, pazara giriş modelinizi kanal bazında okumanızı sağlar.

## Temel fikir

**Pazara giriş modeli** (*route to market*, RTM), ürünün fabrikadan tüketiciye nasıl ulaştığının tasarımıdır: hangi kanallar, hangi aracılar (dağıtıcı, toptancı, lojistik firması), hangi ziyaret ve teslimat sıklığı, hangi ödeme koşulları.

Coughlan ve arkadaşlarının pazarlama kanalları kitabı, kanalı bir dizi işlevin (stok tutma, teslimat, kredi, sipariş alma, bilgi toplama) üstlenilmesi olarak ele alır. Bu işlevler ortadan kalkmaz; yalnızca kimin üstlendiği değişir. Kanal tasarımı, bu işlevleri en düşük toplam maliyetle ve hedef hizmet düzeyinde dağıtmaktır.

**Başlıca kanallar ve farkları:**

- **Ulusal zincirler:** Büyük siparişler, merkezi pazarlık, yüksek ticari koşullar, uzun vade.
- **Yerel zincirler:** Orta büyüklükte siparişler, bölgesel pazarlık, daha esnek ama ölçek olarak küçük.
- **Geleneksel kanal (bakkal, büfe, şarküteri):** Çok sayıda küçük nokta, sık ziyaret ihtiyacı, küçük paket talebi, genellikle dağıtıcı ya da toptancı üzerinden.
- **İndirim marketleri:** Dar ürün yelpazesi, sert fiyat pazarlığı, yüksek hacim.
- **Toptancı ve nakit-ve-taşı:** Küçük perakendeci ve horeca için ara toplayıcı.
- **E-ticaret ve hızlı teslimat:** Hızla büyüyen, kendine özgü ambalaj ve içerik ihtiyacı olan kanal.

**Kanal karması ve marj.** Her kanalın brüt marjı ve hizmet maliyeti farklıdır. Satışın kanallara dağılımı değiştiğinde toplam marj da değişir.

**Modeli seçerken sorulacak sorular.** Pazara giriş modeli tasarlanırken şu sorular yol gösterir: Hedef noktalar nerede ve ne büyüklükte? Ürün soğuk zincir, kısa raf ömrü ya da sık teslimat gerektiriyor mu? Noktaların sipariş büyüklüğü, doğrudan teslimatın maliyetini karşılıyor mu? Hangi işlevleri (satış, teslimat, kredi, tahsilat, raf düzeni) kendiniz yapmak, hangilerini aracılara bırakmak istiyorsunuz? Rakipler hangi modeli kullanıyor ve noktalar neye alışkın? Bu soruların yanıtı genellikle tek bir model değil, kanal ve bölgeye göre farklılaşan bir karmadır. Model, şirket büyüdükçe ve kanal yapısı değiştikçe yeniden değerlendirilmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Kanal payları ve marjlar varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b3.py` ile yapılmıştır.

| Kanal | Satış payı | Brüt marj | Toplam marja katkı (puan) |
|---|---|---|---|
| Ulusal zincir | %35 | %22 | 7,70 |
| Yerel zincir | %20 | %27 | 5,40 |
| Geleneksel kanal | %30 | %31 | 9,30 |
| İndirim marketi | %10 | %18 | 1,80 |
| E-ticaret | %5 | %24 | 1,20 |

Ağırlıklı brüt marj **%25,4**. Geleneksel kanal satışın %30'unu, ama marjın en büyük kısmını getiriyor. Gelecek yıl indirim marketlerinin payı artarken geleneksel kanalın payı düşerse, toplam satış artsa bile toplam marj düşebilir. Brüt marjın yanında her kanalın hizmet maliyetini de hesaba katmak gerekir.

## Sık yapılan hatalar

- **Kanalları yalnızca ciroya göre değerlendirmek.** Marj ve hizmet maliyeti dahil edilmeden kanal önceliği belirlenemez.
- **Her kanala aynı ürün ve fiyatı vermek.** Kanal çatışmasını artırır ve kanalın ihtiyacına uymaz.
- **Büyüyen kanallara geç kalmak.** Yeni bir kanalda erken öğrenmek, sonradan büyük yatırımla telafi etmekten ucuzdur.

## Pratikte nasıl uygulanır?

- [ ] Satışınızı kanal bazında ayırın ve her kanalın brüt marjını hesaplayın.
- [ ] Her kanal için kim hangi işlevi üstleniyor, tablo hâlinde yazın.
- [ ] Kanal karmasının önümüzdeki üç yılda nasıl değişeceğini tahmin edip marja etkisini hesaplayın.
- [ ] Kanal başına ürün, paket, fiyat ve hizmet düzeyini ayrı tanımlayın.

## Daha fazlası

- Coughlan, A. T.; Anderson, E.; Stern, L. W.; El-Ansary, A. I. (2006). *Marketing Channels.* (kaynak doğrulanmadı)
