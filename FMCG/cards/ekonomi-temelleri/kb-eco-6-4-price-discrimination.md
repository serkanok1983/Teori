---
id: kb-eco-6-4-price-discrimination
title: "Fiyat farklılaştırma ve hacim iskontosu: Kimden ne kadar istemeli?"
summary: "Farklı müşteri gruplarına farklı fiyat uygulamanın mantığını, hacim iskontolarının kârı nasıl artırıp nasıl eritebileceğini ve bir iskonto basamağını tasarlamadan önce hangi hesabın yapılması gerektiğini anlatır."
course: eco
category: ekonomi-temelleri
tags: [fiyatlama, iskonto, kanal]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: orta
source_lessons: [ECO-6.4]
reading_minutes: 3
key_points:
  - "Fiyat farklılaştırma, aynı ürünü farklı ödeme isteği olan müşterilere farklı fiyattan satmaktır."
  - "İskonto basamağı yalnızca davranışı değişen müşteriden ek kâr getirir; zaten o hacmi alanlara verilen iskonto kayıptır."
  - "Bir iskonto kampanyası hacmi artırırken toplam kârı düşürebilir."
  - "Farklılaştırma için müşteri gruplarını ayırabilmeli ve aralarındaki yeniden satışı sınırlayabilmelisiniz."
  - "Fiyat farklılaştırmasının rekabet hukuku açısından sınırları olabilir; hâkim durumdaysanız hukuk görüşü alın."
glossary_terms: [fiyat-farklilastirma, marj]
related: [kb-fmcg-10-2-trade-terms, kb-fmcg-5-4-promotion-economics, kb-ea-27-1-pricing-engine-conditions, kb-eco-1-3-supply-demand]
sources:
  - title: "Principles of Economics 3e, §3.1 Demand, Supply, and Equilibrium in Markets for Goods and Services"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-economics-3e/pages/3-1-demand-supply-and-equilibrium-in-markets-for-goods-and-services"
    verified: true
    checked_on: 2026-10-28
  - title: "The Economy 2.0"
    authors: "CORE Econ"
    year: 2026
    type: web
    url: "https://www.core-econ.org/the-economy/"
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

Distribütörler ve üreticiler her gün farklı fiyat uygular: kanal iskontosu, hacim basamağı, peşin ödeme indirimi, zincir anlaşması. Bu kart, bu farklılaştırmanın ne zaman kârı artırdığını, ne zaman yalnızca para dağıttığını hesaplamanıza yardım eder.

## Temel fikir

**Fiyat farklılaştırma** (*price discrimination*), aynı ürünü farklı müşterilere, maliyet farkıyla açıklanamayan farklı fiyatlardan satmaktır. Üç tür yaygındır:

- **Birinci derece:** Her müşteriye ödemeye razı olduğu en yüksek fiyat. Pratikte yalnızca pazarlıklı büyük satışlarda yaklaşılır.
- **İkinci derece:** Müşteri kendi seçer: hacim basamakları, büyük ambalaj, paket teklifleri.
- **Üçüncü derece:** Gözlenebilir gruplara farklı fiyat: kanal (bakkal, market, HORECA), bölge, öğrenci ya da kurum.

Farklılaştırmanın çalışması için üç koşul gerekir: Gruplar arasında ödeme isteği farkı olmalı, grupları ayırabilmelisiniz ve ucuz alan grubun pahalı gruba yeniden satışı (arbitraj) sınırlı olmalı.

Hacim iskontosunun ana tuzağı şudur: İskonto, basamağa ulaşmak için davranışını değiştiren müşteriye ek hacim getirir, ama basamağın zaten üstünde alan müşteriye bedavaya marj verir. Kararı bu iki etkiyi karşılaştırarak verin.

## Bir örnek

> **Örnek (temsili rakamlar):** Bir distribütörün bakkal kanalındaki müşteri grupları varsayımsaldır; hesaplar `scripts/cards_numbers_eco_b1.py` ile yapılmıştır.

Liste fiyatı koli başı 100 TL, maliyet 80 TL. Öneri: 10 koli ve üzeri siparişte koli fiyatı 96 TL.

- **A grubu (40 müşteri):** Ayda 8 koli alıyor, iskonto için 10 koliye çıkıyor. Müşteri başı kâr 160 TL'den 160 TL'ye: değişmiyor. Hacim artıyor ama kâr artmıyor.
- **B grubu (25 müşteri):** Zaten ayda 15 koli alıyor. Müşteri başı kâr 300 TL'den 240 TL'ye düşüyor: müşteri başı **60 TL** kayıp.
- **C grubu (60 müşteri):** Ayda 4 koli alıyor, basamağa ulaşmıyor; değişiklik yok.

**Sonuç:** Toplam hacim 935 koliden 1.015 koliye çıkıyor, ama aylık brüt kâr 18.700 TL'den 17.200 TL'ye iniyor: **−1.500 TL**. Satış raporu başarı gösterir, kâr raporu tersini.

Basamağı B grubunun mevcut hacminin üstüne (ör. 20 koli) koymak ya da iskontoyu yalnızca artan hacme uygulamak bu kaybı azaltır.

## Sık yapılan hatalar

- İskonto kampanyasını yalnızca hacim artışıyla değerlendirmek.
- Basamağı müşterilerin mevcut sipariş dağılımına bakmadan belirlemek.
- Kanal fiyatları arasındaki farkı, kanallar arası mal kaçışını (ör. market fiyatından bakkala) engelleyemeyecek kadar açmak.
- Peşin iskontoyu, finansman maliyetinin çok üstünde vermek.
- Hâkim durumdaki bir üretici olarak benzer müşterilere gerekçesiz farklı koşul uygulamak; rekabet hukuku riski doğurabilir.
- Kanal bazlı fiyat farklarını ürünün bir kanaldan diğerine aktarılmasını (paralel satış) önleyecek önlemler olmadan uygulamak.

## Pratikte nasıl uygulanır?

- [ ] Her iskonto basamağı için müşterilerinizin son 6 aylık sipariş büyüklüğü dağılımını çıkarın.
- [ ] İskontonun "zaten basamağı geçen" müşterilere maliyetini ayrıca hesaplayın.
- [ ] Mümkünse iskontoyu toplam hacme değil, geçen döneme göre artan hacme bağlayın.
- [ ] Kampanya sonrası hacim ve brüt kâr etkisini müşteri grubu bazında raporlayın.
- [ ] Kanal ve bölge fiyat farklarını, mal kaçışını izleyen bir kontrol raporuyla birlikte yönetin.
- [ ] Her fiyat ve iskonto kademesi için gerekçeyi ve uygulanma koşullarını yazılı hâle getirin; rekabet hukuku açısından hukuk danışmanınızla gözden geçirin.

## Daha fazlası

- OpenStax (2026). *Principles of Economics 3e, §3.1 Demand, Supply, and Equilibrium in Markets for Goods and Services*. https://openstax.org/books/principles-economics-3e/pages/3-1-demand-supply-and-equilibrium-in-markets-for-goods-and-services
- CORE Econ (2026). *The Economy 2.0*. https://www.core-econ.org/the-economy/
