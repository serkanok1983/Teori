---
id: kb-fmcg-11-3-eoq-reorder-point
title: "Ne kadar ve ne zaman sipariş vermeli: Ekonomik sipariş miktarı ve yeniden sipariş noktası"
summary: "Her sipariş bir maliyet yaratır, her stok da bir tutma maliyeti. Bu kart sipariş ve stok tutma maliyetleri arasındaki dengeyi kuran ekonomik sipariş miktarını, yeniden sipariş noktasını ve bu formüllerin hızlı tüketimde nasıl uyarlanacağını anlatır."
course: fmcg
category: tedarik-zinciri-ve-stok
tags: [tedarik-zinciri, stok, bayi]
roles: [bayi-sahibi, bayi-yonetici, depo-lojistik-muduru]
level: orta
source_lessons: [FMCG-11.3]
reading_minutes: 3
key_points:
  - "Sık ve küçük siparişler sipariş maliyetini, seyrek ve büyük siparişler stok tutma maliyetini artırır."
  - "Ekonomik sipariş miktarı, iki maliyetin toplamını en aza indiren sipariş büyüklüğüdür."
  - "Toplam maliyet eğrisi en düşük noktanın çevresinde düzdür; formülden biraz sapmak maliyeti çok az artırır."
  - "Yeniden sipariş noktası, tedarik süresi boyunca beklenen talep ile güvenlik stokunun toplamıdır."
  - "Asgari sipariş miktarları, palet ve araç kapasitesi ile indirimler, formülün sonucunu pratikte değiştirir."
glossary_terms: [ekonomik-siparis-miktari, yeniden-siparis-noktasi, guvenlik-stoku, minimum-siparis-buyuklugu, stok-gun-sayisi]
related: [kb-fmcg-11-4-safety-stock, kb-fmcg-11-2-demand-forecasting, kb-fmcg-11-1-supply-chain-basics, kb-fmcg-7-1-distributor-pnl, kb-fmcg-11-7-warehouse-transport-network]
sources:
  - title: "Inventory and Production Management in Supply Chains"
    authors: "Silver, E. A.; Pyke, D. F.; Thomas, D. J."
    year: 2017
    type: book
    doi: "10.1201/9781315374406"
    verified: true
    checked_on: 2026-10-28
    note: "DOI Crossref kaydında başlık ve yazar eşleşti; baskı yılı karttakinden farklı olabilir."
  - title: "Supply Chain Management: Strategy, Planning, and Operation"
    authors: "Chopra, S.; Meindl, P."
    year: 2016
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

Bir dağıtıcı her hafta üreticiden sipariş verebilir ya da ayda bir büyük sipariş verebilir. İlki daha fazla sipariş işi, daha fazla teslimat ve daha az stok demektir. İkincisi daha az iş, ama depoda daha fazla stok ve bağlanan sermaye. Bu kart, bu iki maliyet arasındaki dengeyi kurmanızı ve ne zaman sipariş vereceğinize karar vermenizi sağlar.

## Temel fikir

**İki maliyet.**

- **Sipariş maliyeti:** Her sipariş için yapılan sabit iş: sipariş hazırlama, mal kabul, taşıma, fatura kontrolü. Yıllık sipariş maliyeti = (yıllık talep / sipariş miktarı) × sipariş başına maliyet.
- **Stok tutma maliyeti:** Stoktaki ürünün finansman, depo, sigorta ve fire maliyeti. Genellikle birim maliyetin yıllık bir yüzdesi olarak ifade edilir. Yıllık tutma maliyeti = (sipariş miktarı / 2) × birim başına yıllık tutma maliyeti.

**Ekonomik sipariş miktarı** (*economic order quantity*, EOQ). Silver, Pyke ve Thomas gibi stok yönetimi kaynaklarında anlatılan klasik formül, iki maliyetin toplamını en aza indiren miktarı verir:

EOQ = √(2 × yıllık talep × sipariş başına maliyet / birim başına yıllık tutma maliyeti)

Formülün önemli bir özelliği vardır: Toplam maliyet eğrisi en düşük noktanın çevresinde oldukça düzdür. Bu nedenle palet ya da araç kapasitesine uymak için miktarı biraz değiştirmek maliyeti çok az artırır.

**Yeniden sipariş noktası** (*reorder point*). Stok belirli bir seviyeye düştüğünde sipariş verilir:

Yeniden sipariş noktası = günlük talep × tedarik süresi (gün) + güvenlik stoku

Tedarik süresi, siparişin verilmesinden ürünün satışa hazır hâle gelmesine kadar geçen süredir.

**Hızlı tüketimde uyarlamalar.**

- **Asgari sipariş ve palet:** Üretici asgari sipariş miktarı ya da tam palet şartı koyabilir.
- **Araç doluluğu:** Taşıma maliyeti, aracın doluluğuna göre değişir; birden fazla ürün birlikte sipariş edilir.
- **Miktar indirimleri:** Büyük siparişe verilen indirim, tutma maliyetini dengeleyebilir.
- **Son kullanma tarihi:** Kısa raf ömrü, sipariş miktarına üst sınır koyar.
- **Enflasyon:** Fiyat artışı beklentisi, öne çekilmiş alımları cazip kılabilir; ama bu karar ayrıca ve bilinçli verilmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Talep, maliyetler ve tedarik süresi varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b6.py` ile yapılmıştır.

Bir dağıtıcı bir üründen yılda **12.000** koli satıyor. Sipariş başına maliyet **600 TL**, birim maliyet **200 TL**, yıllık tutma maliyeti birim maliyetin **%25**'i, yani **50 TL**.

EOQ = √(2 × 12.000 × 600 / 50) ≈ **536,7** koli.

| Sipariş miktarı | Sipariş maliyeti | Tutma maliyeti | Toplam (TL/yıl) |
|---|---|---|---|
| 200 | 36.000 | 5.000 | 41.000 |
| 537 | 13.408 | 13.425 | 26.833 |
| 1.000 | 7.200 | 25.000 | 32.200 |
| 2.000 | 3.600 | 50.000 | 53.600 |

En düşük maliyet EOQ civarında, ama 1.000 koli de en düşük maliyetin yalnızca yaklaşık %20 üzerinde. Çok küçük ya da çok büyük siparişler ise belirgin biçimde pahalı.

Yılda 300 iş günüyle günlük talep **40** koli, tedarik süresi **5** gün. Güvenlik stoku olmadan yeniden sipariş noktası **200** koli; **44** kolilik güvenlik stokuyla **244** koli. Stok 244 koliye düştüğünde dağıtıcı yaklaşık 537 koli sipariş verir.

## Sık yapılan hatalar

- **Sipariş maliyetini sıfır saymak.** Her siparişin iş, taşıma ve kontrol maliyeti vardır.
- **Tutma maliyetini yalnızca faiz olarak görmek.** Depo, fire ve son kullanma tarihi kayıpları da eklenmelidir.
- **Formülü mekanik uygulamak.** Asgari sipariş, palet ve raf ömrü kısıtlarını hesaba katın.
- **Tedarik süresini sabit varsaymak.** Değişken tedarik süresi, daha fazla güvenlik stoku gerektirir.
- **Parametreleri güncellememek.** Talep ve maliyetler değiştikçe sipariş miktarı da değişmelidir.

## Pratikte nasıl uygulanır?

- [ ] Sipariş başına maliyetinizi ve yıllık tutma maliyeti oranınızı bir kez hesaplayın.
- [ ] Hızlı dönen ana ürünler için EOQ ve yeniden sipariş noktası hesaplayın.
- [ ] Sonucu palet, araç ve asgari sipariş kısıtlarına göre yuvarlayın.
- [ ] Yeniden sipariş noktalarını stok yönetim sisteminize tanımlayın.
- [ ] Parametreleri üç ayda bir, enflasyon ve faiz yüksekse daha sık güncelleyin.

## Daha fazlası

- Silver, E. A.; Pyke, D. F.; Thomas, D. J. (2017). *Inventory and Production Management in Supply Chains.*
- Chopra, S.; Meindl, P. (2016). *Supply Chain Management: Strategy, Planning, and Operation.* (kaynak doğrulanmadı)
