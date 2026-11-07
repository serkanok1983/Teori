---
id: kb-eco-32-4-finance-in-high-inflation
title: "Yüksek enflasyonda finans yönetimi: Vade, fiyat ve yerine koyma maliyeti"
summary: "Yüksek enflasyonda vadeli satışın tahsilatın reel değerini nasıl erittiğini, tarihi maliyet üzerinden fiyatlamanın kârı neden olduğundan yüksek gösterdiğini ve yerine koyma maliyetiyle fiyatlama ve vade yönetimini anlatır."
course: eco
category: kurumsal-finans
tags: [enflasyon, fiyatlama, nakit-yonetimi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [ECO-32.4]
reading_minutes: 3
key_points:
  - "Yüksek enflasyonda vade, müşteriye verilen örtük bir indirimdir."
  - "Tarihi maliyete kâr marjı ekleyerek fiyatlamak, stoğu yenilediğinizde marjınızın eridiğini gizler."
  - "Fiyatlamada yerine koyma maliyetini esas alın."
  - "Tüm nakit kararlarında (vade, stok, borç) aylık enflasyon oranını bir maliyet olarak düşünün."
glossary_terms: [yerine-koyma-maliyeti, reel-faiz, vade]
related: [kb-eco-21-1-monetary-policy-tcmb, kb-eco-35-2-inflation-accounting, kb-eco-38-2-cash-conversion-cycle, kb-fmcg-5-6-pricing-in-high-inflation]
sources:
  - title: "Enflasyon Verileri — Tüketici Fiyatları"
    authors: "TCMB"
    year: 2026
    type: web
    url: "https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Istatistikler/Enflasyon+Verileri"
    verified: true
    checked_on: 2026-10-28
  - title: "IAS 29 Financial Reporting in Hyperinflationary Economies"
    authors: "IFRS Foundation"
    year: 2026
    type: standard
    url: "https://www.ifrs.org/issued-standards/list-of-standards/ias-29-financial-reporting-in-hyperinflationary-economies/"
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

Yüksek enflasyon dönemlerinde muhasebe kârı ile gerçek ekonomik durum birbirinden uzaklaşır. Bir distribütör kâr ettiğini düşünürken stok ve alacaklarının reel değeri eriyebilir. Bu kart, üç temel kararda, yani vade, fiyatlama ve stok yenilemede enflasyonun etkisini hesaba katmanızı sağlar.

## Temel fikir

**1. Vade örtük bir indirimdir.** Bugün 100 TL'ye satıp 60 gün sonra tahsil ederseniz, aylık enflasyon %3 iken tahsil ettiğiniz 100 TL'nin bugünkü değeri yaklaşık 94 TL'dir. Uzun vade veren bir rakip aslında fiyat indirimi yapıyordur.

**2. Tarihi maliyet tuzağı.** Muhasebe, satılan malın maliyetini satın alındığı fiyattan kaydeder. Stoğu 2 ay önce aldıysanız ve fiyatlar o süre içinde arttıysa, maliyetinizi düşük, kârınızı yüksek görürsünüz. Ama sattığınız malı yerine koymak için daha fazla ödeyeceksiniz.

**3. Yerine koyma maliyetiyle fiyatlama.** Fiyatı, sattığınız ürünü bugün yeniden almanın maliyetine göre belirleyin. Aksi hâlde her stok döngüsünde işletme sermayeniz reel olarak küçülür.

Finansal raporlamada yüksek enflasyonun etkisini gidermek için enflasyon muhasebesi (TMS 29) uygulanabilir; ama yönetim kararları için aylık bazda basit hesaplar yeterlidir.

### Yüksek enflasyonda işletme sermayesi

- **Alacaklar:** Vadeyi kısaltmak, erken ödeme iskontosu sunmak veya vade farkını enflasyon beklentisine göre güncellemek. Vade farkının, beklenen enflasyonun ve finansman maliyetinin altında kalması, müşteriye reel bir indirim yapmak demektir.
- **Stok:** Fiyat artışı beklentisiyle stok biriktirmek kazanç sağlayabilir, ama finansman maliyeti, depolama ve talep düşüşü riskini de artırır. Stok kararlarını beklenen fiyat artışıyla finansman maliyetini karşılaştırarak verin.
- **Tedarikçiler:** Uzun vadeli tedarikçi borcu enflasyonda değerlidir, ama tedarikçiler bunu fiyatlarına yansıtır. Vade ve fiyatı birlikte müzakere edin.

### Raporlamada

Yönetim raporlarında nominal büyümeyi enflasyonla, kârlılığı ise reel getiri ile karşılaştırın. Satış miktarını (koli, ton, adet) tutar bazlı raporların yanında mutlaka gösterin; nominal satış artarken miktarın düşmesi, pazar payı kaybının ilk işaretidir.

### Fiyat listeleri

Fiyat güncellemelerini düzensiz ve büyük adımlarla yapmak yerine daha sık ve küçük adımlarla yapmak, müşteri tepkisini azaltır ve marj erimesini önler. Fiyat listelerine geçerlilik süresi koyun.

## Bir örnek

> **Örnek (temsili rakamlar):** Aylık enflasyon oranı ve fiyatlar varsayımsaldır; güncel enflasyon verisi değildir. Hesaplar `scripts/cards_numbers_eco_b4.py` ile yapılmıştır.

Aylık enflasyon %3.

**Vadenin maliyeti:** 100 TL'lik satışın 60 gün sonra tahsil edilen değeri bugünün parasıyla 94,26 TL (**%5,74** reel kayıp). 90 gün vadede 91,51 TL (%8,49).

**Tarihi maliyet tuzağı:** Ürünü 2 ay önce 80 TL'ye aldınız ve %20 kâr ekleyerek 96,00 TL'ye satıyorsunuz.

- Muhasebeye göre brüt kâr 16,00 TL (%16,7).
- Ürünü bugün yeniden almanın maliyeti 84,87 TL. Gerçek kâr 11,13 TL (%11,6).
- Yerine koyma maliyetine aynı kâr oranını ekleseydiniz fiyat 101,85 TL olurdu.

## Sık yapılan hatalar

- Vadeyi bir fiyat unsuru olarak değil, ticari bir alışkanlık olarak görmek.
- Fiyat listesini tarihi maliyete göre ve seyrek güncellemek.
- Muhasebe kârına bakıp kâr dağıtmak; işletme sermayesinin reel olarak küçüldüğünü fark etmemek.
- Enflasyonu yıllık rakamlarla izleyip aylık etkiyi göz ardı etmek.
- Erken ödeme iskontosunu enflasyonla karşılaştırmadan belirlemek.

## Pratikte nasıl uygulanır?

- [ ] Vade farkı ve erken ödeme iskontosunu aylık enflasyon ve finansman maliyetiyle hesaplayın.
- [ ] Fiyat listesini yerine koyma maliyetine göre güncelleyin; güncelleme sıklığını enflasyona göre belirleyin.
- [ ] Yönetim raporlarında brüt kârı yerine koyma maliyetiyle de hesaplayın.
- [ ] Kâr dağıtımı kararlarında işletme sermayesinin reel değerini koruyup korumadığınızı kontrol edin.
- [ ] Enflasyon muhasebesinin raporlamanıza etkisini mali müşavirinizle değerlendirin.

## Daha fazlası

- TCMB (2026). *Enflasyon Verileri — Tüketici Fiyatları*. https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Istatistikler/Enflasyon+Verileri
- IFRS Foundation (2026). *IAS 29 Financial Reporting in Hyperinflationary Economies*. https://www.ifrs.org/issued-standards/list-of-standards/ias-29-financial-reporting-in-hyperinflationary-economies/
- CORE Econ (2026). *The Economy 2.0*. https://www.core-econ.org/the-economy/
