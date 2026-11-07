---
id: kb-eco-22-1-exchange-rates-real-nominal
title: "Nominal ve reel kur: İthal ürün gerçekten pahalandı mı?"
summary: "Nominal kur ile reel kur arasındaki farkı, kur artışının ithal maliyetlere ve yerli rakiplere göre fiyat rekabetine etkisini ve kur değişimini planlamaya nasıl yansıtacağınızı anlatır."
course: eco
category: makroekonomi-ve-enflasyon
tags: [kur, ithalat, fiyatlama, makroekonomi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [ECO-22.1, ECO-22.4]
reading_minutes: 3
key_points:
  - "Nominal kur, bir dövizin TL karşılığıdır; reel kur bunu iki ülkenin fiyat artışlarıyla düzeltir."
  - "Kur artışı yurt içi enflasyondan düşükse, ithal ürün yerli ürüne göre aslında ucuzlamış olabilir."
  - "Kur artışının maliyete etkisi, ürün maliyetindeki döviz payına bağlıdır."
  - "Kısa vadede kur, faiz farkı ve beklentilerle sert hareket edebilir; plan tek bir kur varsayımına dayanmamalıdır."
glossary_terms: [reel-kur, nominal-kur]
related: [kb-eco-23-2-currency-crises-business, kb-eco-30-1-forwards-fx-hedging, kb-eco-34-8-fx-transactions, kb-eco-19-3-supply-shocks-cost-inflation]
sources:
  - title: "Türkiye Cumhuriyet Merkez Bankası (resmî site)"
    authors: "TCMB"
    year: 2026
    type: web
    url: "https://www.tcmb.gov.tr"
    verified: true
    checked_on: 2026-10-28
  - title: "Expectations and Exchange Rate Dynamics"
    authors: "Dornbusch, R."
    year: 1976
    type: article
    doi: "10.1086/260506"
    url: "https://doi.org/10.1086/260506"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Political Economy 84(6)."
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

İthal ürün satan bir distribütör ya da ithal hammadde kullanan bir üretici için kur, maliyetin en oynak kalemidir. Ama kurun %20 artması, rekabet gücünüzün %20 düştüğü anlamına gelmez. Bu kart, kur hareketini yurt içi fiyatlarla birlikte okumanızı sağlar.

## Temel fikir

- **Nominal kur** (*nominal exchange rate*): 1 dolar veya 1 avronun kaç TL ettiği.
- **Reel kur** (*real exchange rate*): Nominal kurun iki ülkenin fiyat düzeyleriyle düzeltilmiş hâli. Reel kurdaki değişim = (1 + nominal kur değişimi) × (1 + yabancı enflasyon) / (1 + yurt içi enflasyon) − 1.

Reel kur yükseliyorsa yabancı mallar yerli mallara göre pahalanıyor, yani TL reel olarak değer kaybediyor demektir. Reel kur düşüyorsa, nominal kur artsa bile TL reel olarak değer kazanıyor ve ithal ürünler yerli ürünlere göre ucuzluyordur.

**Kısa vadeli dalgalanma:** Dornbusch (1976), fiyatlar yavaş, finansal piyasalar hızlı uyum sağladığında kurun para politikası şoklarına uzun vadeli dengesini aşan sert tepkiler verebileceğini gösterdi (aşırı tepki, *overshooting*). Bu, kısa vadeli kur tahminlerinin güvenilmez olduğunu hatırlatır.

**Maliyete etkisi:** Ürünün tamamı ithalse kur artışı maliyete neredeyse doğrudan geçer. Yerli üretimde etkisi, ithal hammadde, ambalaj ve enerji payı kadardır.

## Bir örnek

> **Örnek (temsili rakamlar):** Kur ve enflasyon oranları varsayımsaldır; gerçek kur veya enflasyon verisi değildir. Hesaplar `scripts/cards_numbers_eco_b2.py` ile yapılmıştır.

Bir distribütör yılda 100.000 dolarlık ürün ithal ediyor. Kur 34 TL'den 35 TL'ye çıkıyor: nominal artış **%20**. İthal maliyet 30.000.000 TL'den 36.000.000 TL'ye yükseliyor.

Aynı dönemde yurt içi enflasyon %25, ABD enflasyonu %3.

- Reel kur değişimi = 1,20 × 1,03 / 1,25 − 1 = **−%1,12**: TL reel olarak hafif değer kazanmış.
- Başlangıçta aynı maliyetli bir yerli rakibin maliyeti yurt içi enflasyonla artarsa 37.500.000 TL olur. İthal ürün, yerli rakibe göre **−%4,0** daha ucuz konuma gelir.

Kur arttığı hâlde ithal ürünün rekabet gücü kötüleşmemiş, hafif iyileşmiştir.

## Sık yapılan hatalar

- Kur artışını tek başına "ithal ürün pahalandı" diye yorumlamak.
- Kuru bütçede tek bir rakam olarak sabitlemek.
- Ürün maliyetindeki döviz payını bilmeden fiyat güncellemek.
- Avro ve dolar maliyetlerini ayrı izlememek; çapraz kur hareketini kaçırmak.
- Kur düştüğünde fiyat indirmeyip yükseldiğinde hemen artırmak; müşteri güvenini zedelemek.
- Kurdaki yükselişi otomatik olarak rekabet avantajı saymak; yurt içi maliyetler daha hızlı artıyorsa reel kur avantajı kısa sürede kaybolur.
- Tek bir dövize bakmak; ihracat ve ithalatın para birimi dağılımına göre sepet kuru izlenmelidir.

## Pratikte nasıl uygulanır?

- [ ] Ürün gruplarınızın maliyetindeki döviz payını (dolar, avro) çıkarın.
- [ ] Bütçede en az üç kur senaryosu kullanın ve her birinde maliyet ve fiyat etkisini hesaplayın.
- [ ] Reel kuru (ör. TCMB'nin yayımladığı reel efektif kur endeksi) çeyrek bazında izleyin.
- [ ] Döviz bazlı alımlarda fiyat güncelleme kuralını (hangi kur, hangi tarih) müşterilerle önceden netleştirin.
- [ ] Yüksek döviz payı olan alımlar için korunma seçeneklerini değerlendirin.
- [ ] İhracat fiyatlarınızı ve yurt içi birim maliyetlerinizi aynı tabloda çeyreklik izleyin.
- [ ] TCMB'nin yayımladığı reel efektif döviz kuru endeksini rakiplerinizin ülke kurlarıyla birlikte takip edin.

## Daha fazlası

- TCMB (2026). *Türkiye Cumhuriyet Merkez Bankası (resmî site)*. https://www.tcmb.gov.tr
- Dornbusch, R. (1976). *Expectations and Exchange Rate Dynamics*. https://doi.org/10.1086/260506
- CORE Econ (2026). *The Economy 2.0*. https://www.core-econ.org/the-economy/
