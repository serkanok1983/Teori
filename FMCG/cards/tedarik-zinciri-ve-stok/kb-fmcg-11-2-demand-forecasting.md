---
id: kb-fmcg-11-2-demand-forecasting
title: "Talep tahmini: Yöntem, hata ölçümü ve sapma"
summary: "İyi bir talep tahmini, stok, üretim ve satış planlarının temelidir. Bu kart temel tahmin yöntemlerini, tahmin hatasını ölçmenin yollarını, sistematik sapmanın neden tehlikeli olduğunu ve tahmine satış bilgisinin nasıl ekleneceğini anlatır."
course: fmcg
category: tedarik-zinciri-ve-stok
tags: [tedarik-zinciri, planlama, analitik]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, depo-lojistik-muduru]
level: orta
source_lessons: [FMCG-11.2]
reading_minutes: 3
key_points:
  - "Tahmin her zaman hatalıdır; amaç hatayı ölçmek, azaltmak ve plana dahil etmektir."
  - "Ortalama mutlak yüzde hata, hatanın büyüklüğünü; sapma ise tahminin sistematik olarak yüksek ya da düşük olup olmadığını gösterir."
  - "Her tahmin yöntemi, en basit naif tahminle karşılaştırılmalıdır."
  - "Satış ekibinin promosyon ve listeleme bilgisi tahmine değer katabilir, ama sistematik iyimserlik de getirebilir."
  - "Tahmin, ürün-müşteri-hafta gibi uygun bir ayrıntı düzeyinde yapılmalı ve toplanarak kontrol edilmelidir."
glossary_terms: [tahmin-hatasi, guvenlik-stoku, baz-satis, satis-ve-operasyon-planlamasi]
related: [kb-fmcg-11-4-safety-stock, kb-fmcg-11-6-sop-ibp, kb-fmcg-13-16-sales-forecasting, kb-fmcg-11-5-bullwhip-effect, kb-fmcg-4-7-launch-forecasting]
sources:
  - title: "Forecasting: Principles and Practice (3rd ed.)"
    authors: "Hyndman, R. J.; Athanasopoulos, G."
    year: 2021
    type: book
    url: "https://otexts.com/fpp3/"
    verified: true
    checked_on: 2026-10-28
    note: "URL HTTP 200 ile açıldı, başlık/kurum eşleşti (2026-10-28)."
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

Fazla tahmin, depoda bekleyen stok ve son kullanma tarihi yaklaşan ürünler demektir. Eksik tahmin ise stoksuzluk ve kayıp satış. Bu kart, tahmin yapmanın temel mantığını, tahminin ne kadar iyi olduğunu ölçmeyi ve satış ekibinin bilgisini tahmine nasıl ekleyeceğinizi anlatır.

## Temel fikir

**Temel yöntemler.** Hyndman ve Athanasopoulos'un ücretsiz çevrim içi kitabı, tahmin yöntemlerini ayrıntılı biçimde anlatır. Hızlı tüketimde sık kullanılanlar:

- **Naif tahmin:** Gelecek hafta, bu haftanın aynısı olacak. Basittir, ama her yöntemin geçmesi gereken bir ölçüttür.
- **Hareketli ortalama:** Son birkaç dönemin ortalaması. Dalgalanmayı yumuşatır.
- **Üstel düzeltme:** Yakın dönemlere daha fazla ağırlık verir; eğilim ve mevsimsellik eklenebilir.
- **Nedensel modeller:** Fiyat, promosyon, hava durumu, bayram gibi etkenleri hesaba katar.

**Baz ve artış.** Promosyon yoğun kategorilerde tahmin genellikle iki parçaya ayrılır: baz satış (promosyon olmadan beklenen satış) ve promosyon artışı. Baz istatistiksel yöntemlerle, artış ise geçmiş promosyonların sonuçları ve satış ekibinin bilgisiyle tahmin edilir.

**Hatayı ölçmek.**

- **Ortalama mutlak yüzde hata** (*mean absolute percentage error*, MAPE): Her dönemdeki hatanın gerçekleşmeye oranının ortalaması. Hatanın büyüklüğünü gösterir.
- **Ağırlıklı mutlak yüzde hata** (WAPE): Toplam mutlak hatanın toplam gerçekleşmeye oranı. Düşük hacimli dönemlerin etkisini azaltır.
- **Sapma** (*bias*): Tahmin ile gerçekleşme arasındaki farkların işaretli toplamı. Sürekli pozitifse tahmin sistematik olarak yüksek, sürekli negatifse düşüktür.

Sapma, büyüklükten daha tehlikelidir. Rastgele hatalar güvenlik stokuyla karşılanabilir; sistematik sapma ise sürekli fazla ya da eksik stok yaratır.

**Satış bilgisi.** Satış ekibi, yaklaşan listeleme, promosyon ya da rakip hareketlerini bilir. Bu bilgi tahmine eklenmelidir. Ancak satış ekibi hedef baskısıyla tahmini yükseltebilir ya da prim hedefini düşük tutmak için düşürebilir. Bu nedenle her düzeltmenin tahmini iyileştirip iyileştirmediği ayrıca ölçülmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Haftalık satış ve tahminler varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b6.py` ile yapılmıştır.

Bir ürünün altı haftalık satışı ve tahmini:

| Hafta | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Gerçekleşen | 100 | 120 | 90 | 110 | 130 | 105 |
| Tahmin | 110 | 110 | 100 | 100 | 120 | 115 |

- MAPE: **%9,3**
- WAPE: **%9,2**
- Sapma: **0** (yüksek ve düşük tahminler birbirini dengeliyor)

Aynı dönemde naif tahmin ("geçen haftanın aynısı") 2–6. haftalar için **%21,5** MAPE veriyor; tahmin yöntemi aynı haftalarda **%9,2** ile çok daha iyi. Sapmanın sıfır olması, tahminin sistematik bir yönde kaymadığını gösteriyor. Ama tek bir ürün ve altı hafta, genel bir sonuç için yeterli değildir; ölçüm ürün grupları ve daha uzun dönemler için tekrarlanmalıdır.

## Sık yapılan hatalar

- **Tahmin hatasını ölçmemek.** Ölçülmeyen tahmin iyileştirilemez.
- **Yalnızca MAPE'ye bakmak.** Sapma, sistematik fazla ya da eksik stokun nedenidir.
- **Naif tahminle karşılaştırmamak.** Karmaşık bir yöntem, en basit yöntemden kötü olabilir.
- **Satış hedefini tahmin olarak kullanmak.** Hedef bir istektir; tahmin bir beklentidir.
- **Promosyonları baz satışa karıştırmak.** Geçmiş promosyonlar baz tahmini şişirir.

## Pratikte nasıl uygulanır?

- [ ] Ana ürünleriniz için haftalık tahmin hatasını (MAPE ve sapma) ölçmeye başlayın.
- [ ] Her tahmin yöntemini naif tahminle karşılaştırın.
- [ ] Promosyon dönemlerini ayırarak baz satış tahmini yapın.
- [ ] Satış ekibinin düzeltmelerini kaydedin ve tahmini iyileştirip iyileştirmediğini ölçün.
- [ ] Tahmin hatasını güvenlik stoku hesabına girdi olarak kullanın.

## Daha fazlası

- Hyndman, R. J.; Athanasopoulos, G. (2021). *Forecasting: Principles and Practice (3rd ed.).* https://otexts.com/fpp3/
- Chopra, S.; Meindl, P. (2016). *Supply Chain Management: Strategy, Planning, and Operation.* (kaynak doğrulanmadı)
