---
id: kb-fmcg-6-3-cost-to-serve
title: "Hizmet maliyeti: Her müşteriye hizmet vermek ne kadara mal oluyor?"
summary: "İki müşteri aynı ciroyu getirse de birine hizmet vermek diğerinden çok daha pahalı olabilir. Bu kart teslimat, ziyaret, sipariş büyüklüğü ve vadenin hizmet maliyetini nasıl belirlediğini ve kârlı olmayan müşterileri nasıl kârlı hâle getireceğinizi anlatır."
course: fmcg
category: dagitim-modeli
tags: [dagitim, maliyet, saha-satis, lojistik]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru, depo-lojistik-muduru]
level: orta
source_lessons: [FMCG-6.3]
reading_minutes: 3
key_points:
  - "Hizmet maliyeti, bir müşteriye satış yapmak, teslimat yapmak ve tahsilat yapmak için harcanan toplam maliyettir."
  - "Teslimat başına maliyet büyük ölçüde sabittir; sipariş küçüldükçe satışa oranı hızla artar."
  - "Müşteri kârlılığı, brüt marjdan hizmet maliyeti çıkarılarak bulunur."
  - "Minimum sipariş tutarı, teslimat sıklığı ve hizmet modelini müşteri grubuna göre ayarlamak kârlılığı artırır."
glossary_terms: [hizmet-maliyeti, minimum-siparis-buyuklugu]
related: [kb-fmcg-6-2-outlet-universe-segmentation, kb-fmcg-6-4-direct-vs-indirect, kb-fmcg-1-1-margin-stack, kb-fmcg-7-1-distributor-pnl, kb-fmcg-11-7-warehouse-transport-network]
sources:
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

Ciroya göre sıralanmış müşteri listesi, hangi müşterinin para kazandırdığını göstermez. Hizmet maliyeti (*cost to serve*) analizi, her müşterinin gerçekten ne kadar kâr bıraktığını ortaya koyar ve hizmet modelinizi müşteriye göre ayarlamanızı sağlar.

## Temel fikir

**Maliyet kalemleri.** Bir müşteriye hizmet vermenin maliyeti genellikle şu kalemlerden oluşur:

- **Satış:** Temsilcinin ziyaret süresi, yol, sipariş alma.
- **Teslimat:** Araç, sürücü, yakıt, yükleme ve boşaltma süresi.
- **Depo:** Toplama, paketleme, sipariş satırı sayısı.
- **Finansman:** Vade süresince bağlanan sermaye ve tahsilat riski.
- **Ticari koşullar:** İskontolar, primler, iadeler.

Kaplan ve Cooper, faaliyet tabanlı maliyetleme yaklaşımıyla maliyetlerin, onları gerçekten tüketen faaliyetlere göre dağıtılmasını önerir. Böylece maliyetin genel bir ortalama ile değil, her müşterinin gerçek kullanımıyla hesaplanması mümkün olur.

**Sipariş büyüklüğünün etkisi.** Teslimat başına maliyetin büyük kısmı sabittir: Araç oraya gider, sürücü durur, ürün indirilir. 1.500 TL'lik bir sipariş ile 6.000 TL'lik bir sipariş, teslimat maliyetinde çok farklı oranlar yaratır.

**Müşteri kârlılığı.** Brüt marj − hizmet maliyeti = müşterinin katkısı. Bu hesap, ciro sıralamasında üstte olan bazı müşterilerin aslında az kâr bıraktığını, küçük ama verimli müşterilerin ise iyi kâr getirdiğini gösterebilir.

**Hizmet maliyetini hesaplamak için veri.** Hizmet maliyeti hesabı için çoğu şirkette veri zaten vardır, ama farklı sistemlere dağılmıştır. Teslimat sayısı ve araç maliyetleri lojistik ekibinden, ziyaret sayısı ve süresi SFA'dan, sipariş satırları ve iadeler ERP'den, vade ve tahsilat süresi finans ekibinden gelir. İlk hesabı mükemmel yapmaya çalışmayın; birkaç ana etkinlik ve makul dağıtım anahtarlarıyla başlamak, müşteriler arasındaki büyük farkları göstermeye yeter. Sonuçlar, müşteriyi bırakmak için değil, hizmet modelini değiştirmek için kullanılmalıdır: Asgari sipariş tutarı, teslimat sıklığı, telefonla sipariş ya da toptancıya devretmek gibi seçenekler değerlendirilebilir.

## Bir örnek

> **Örnek (temsili rakamlar):** Teslimat maliyeti, sipariş tutarları ve marj varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b3.py` ile yapılmıştır.

Teslimat başına maliyet 120 TL. Brüt marj %20.

| Müşteri | Ortalama sipariş | Teslimat maliyet oranı | Kalan marj |
|---|---|---|---|
| Küçük bakkal | 1.500 TL | %8,00 | %12,00 |
| Büyük market | 6.000 TL | %2,00 | %18,00 |

Bakkalın siparişi küçük olduğu için marjın yarıya yakını teslimata gidiyor. Teslimat maliyetinin satışın %4'ünü geçmemesini istiyorsanız minimum sipariş tutarı 120 / 0,04 = **3.000 TL** olmalıdır. Bunu sağlamanın yolları: teslimat sıklığını azaltmak, siparişleri birleştirmek ya da küçük noktaları toptancı üzerinden hizmetlendirmek.

## Sık yapılan hatalar

- **Ortalama maliyetle hesaplamak.** Bütün müşterilere aynı oranı dağıtmak, gerçek farkları gizler.
- **Vadeyi hesaba katmamak.** 90 günlük vadeyle çalışan müşterinin finansman maliyeti, 15 günlük vadeyle çalışandan çok yüksektir.
- **Kârsız müşteriyi hemen bırakmak.** Önce hizmet modelini değiştirmeyi deneyin: daha seyrek teslimat, minimum sipariş, farklı kanal.
- **Satış ekibine yalnızca ciro hedefi vermek.** Küçük ve sık siparişi teşvik eder.

## Pratikte nasıl uygulanır?

- [ ] Teslimat, ziyaret, depo ve finansman maliyetlerini faaliyet başına hesaplayın.
- [ ] Her müşteri için yıllık teslimat sayısını, ortalama sipariş tutarını ve vadesini çıkarın.
- [ ] Müşteri bazında katkıyı hesaplayın ve müşterileri katkıya göre sıralayın.
- [ ] Düşük katkılı müşteriler için hizmet modelini değiştirin: minimum sipariş, teslimat günü, telefonla sipariş, toptancı.
- [ ] Satış ekibinin hedeflerine sipariş büyüklüğü ya da müşteri katkısı ekleyin.

## Daha fazlası

- Kaplan, R. S.; Cooper, R. (1998). *Cost & Effect: Using Integrated Cost Systems to Drive Profitability and Performance.* (kaynak doğrulanmadı)
