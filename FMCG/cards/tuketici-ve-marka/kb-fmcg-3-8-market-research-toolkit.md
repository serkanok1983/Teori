---
id: kb-fmcg-3-8-market-research-toolkit
title: "Pazar araştırması araç kutusu: Panel, perakende denetimi, anket ve saha verisi"
summary: "Hızlı tüketimde kararlar birkaç temel veri kaynağına dayanır: hane paneli, perakende ölçümü, anket ve kendi satış verileriniz. Bu kart her kaynağın neyi söyleyip neyi söylemediğini ve örneklem büyüklüğünün neden önemli olduğunu anlatır."
course: fmcg
category: tuketici-ve-marka
tags: [tuketici, analitik, pazar-payi]
roles: [uretici-sahibi, uretici-yonetici]
level: orta
source_lessons: [FMCG-3.8]
reading_minutes: 3
key_points:
  - "Hane paneli kimin, ne sıklıkla, ne aldığını; perakende ölçümü nerede, ne kadar satıldığını gösterir."
  - "Kendi sell-in verileriniz rafta ne olduğunu değil, kanala ne gönderdiğinizi gösterir."
  - "Anket sonuçlarının bir hata payı vardır; küçük örneklemde küçük farklar anlamlı olmayabilir."
  - "Hiçbir kaynak tek başına yeterli değildir; kararı birkaç kaynağı birlikte okuyarak verin."
glossary_terms: [orneklem-hatasi, penetrasyon]
related: [kb-fmcg-3-2-repeat-buying-patterns, kb-fmcg-3-7-shopper-path-to-purchase, kb-fmcg-12-3-analytics-for-decisions, kb-fmcg-8-13-sales-analytics, kb-fmcg-4-7-launch-forecasting]
sources:
  - title: "Kantar"
    authors: "Kantar"
    year: 2026
    type: web
    url: "https://www.kantar.com/"
    verified: true
    checked_on: 2026-10-28
  - title: "NielsenIQ"
    authors: "NielsenIQ"
    year: 2026
    type: web
    url: "https://www.nielseniq.com/"
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

"Payımız düştü" cümlesi, hangi veriye baktığınıza göre farklı anlamlar taşır. Bu kart, hızlı tüketimde kullanılan temel veri kaynaklarını, her birinin güçlü ve zayıf yanlarını ve bir anket sonucunu yorumlarken hata payını nasıl hesaba katacağınızı anlatır.

## Temel fikir

**1. Hane paneli** (*household panel*). Kantar gibi sağlayıcılar, temsilî bir hane örneğinin satın aldığı ürünleri düzenli olarak kaydeder. Panel şunları gösterir: penetrasyon, alım sıklığı, alım başına miktar, hangi kanaldan alındığı, rakipten geçişler. "Kim alıyor ve neden az alıyor?" sorusunun cevabı burada aranır.

**2. Perakende ölçümü** (*retail measurement*). NielsenIQ gibi sağlayıcılar, mağaza örnekleminden satış, fiyat ve dağıtım verisi toplar. Pazar payı, sayısal ve ağırlıklı dağıtım, ortalama raf fiyatı buradan izlenir. "Nerede ve ne kadar satılıyor?" sorusunun cevabıdır. Kapsamın hangi kanalları içerdiğini her zaman kontrol edin; bazı formatlar ölçüm dışında kalabilir.

**3. Anket ve nitel araştırma.** Bilinirlik, marka algısı, konsept testi gibi konularda kullanılır. Davranış değil beyan ölçer. İnsanlar ne yapacaklarını söylediklerinden farklı davranabilir.

**4. Kendi verileriniz.** Sell-in (dağıtıcıya ya da zincire satışınız), varsa sell-out (rafta tüketiciye satış) ve saha ziyaret kayıtları. Sell-in hızlı ve ucuzdur ama stok hareketlerini de içerir. Promosyon öncesi yükleme, sell-in'i şişirip gerçek tüketimi gizleyebilir.

**Örneklem hatası** (*sampling error*). Örnekleme dayanan her sonuç bir aralıktır. Basit rastgele örneklemde oran için yaklaşık %95 güven aralığının yarı genişliği 1,96 × √(p × (1 − p) / n) formülüyle hesaplanır. Gerçek araştırmaların tasarımı daha karmaşık olabilir; bu formül ilk kontrol içindir.

## Bir örnek

> **Örnek (temsili rakamlar):** Oranlar ve örneklem büyüklükleri varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b2.py` ile yapılmıştır.

Bir bilinirlik anketinde 400 kişiden %30'u markanızı biliyor.

- Hata payı: 1,96 × √(0,30 × 0,70 / 400) ≈ **±%4,49**

Yani gerçek oran kabaca %25,5 ile %34,5 arasındadır. Bir önceki dalgada %28 çıktıysa, "bilinirlik arttı" demek için yeterli kanıt yoktur.

Planlama tarafında, en kötü durum olan p = 0,5 için:

- ±%5 hata payı için gereken örneklem: **385 kişi**
- ±%3 hata payı için gereken örneklem: **1.068 kişi**

Hata payını daraltmak örneklemi hızla büyütür, maliyeti de artırır.

## Sık yapılan hatalar

- **Sell-in'i tüketim sanmak.** Yükleme dönemlerinde sell-in artarken raf satışı düşüyor olabilir.
- **Farklı kaynakların paylarını karşılaştırmak.** Panel payı ile perakende ölçüm payı farklı tanım ve kapsamlarla hesaplanır.
- **Küçük farkları yorumlamak.** Hata payının içinde kalan değişim, gerçek bir değişim olmayabilir.
- **Beyanı davranış sanmak.** "Alırım" diyenlerin tamamı almaz.

## Pratikte nasıl uygulanır?

- [ ] Her ana soru için hangi kaynağı kullanacağınızı yazın: kim alıyor (panel), nerede satılıyor (perakende ölçümü), ne düşünüyor (anket).
- [ ] Sell-in ile sell-out'u aynı grafikte izleyin ve aradaki farkı stok değişimi olarak yorumlayın.
- [ ] Anket sonuçlarını her zaman hata payıyla birlikte raporlayın.
- [ ] Ölçüm kapsamının dışında kalan kanallar için kendi saha verinizi tamamlayıcı olarak kullanın.

## Daha fazlası

- Kantar (2026). *Kantar.* https://www.kantar.com/
- NielsenIQ (2026). *NielsenIQ.* https://www.nielseniq.com/
