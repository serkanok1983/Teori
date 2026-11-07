---
id: kb-eco-38-2-cash-conversion-cycle
title: "Nakit dönüşüm süresi: Paranız kaç gün sahada kalıyor?"
summary: "Alacak, stok ve borç günlerinden nakit dönüşüm süresini hesaplamayı, bunun yüksek faiz ve enflasyon ortamında bayiye ne kadara mal olduğunu ve süreyi kısaltmanın yollarını anlatır."
course: eco
category: finansal-analiz
tags: [nakit, isletme-sermayesi, tahsilat, vade, stok, enflasyon]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: orta
source_lessons: [ECO-38.2, ECO-31.7, ECO-36.3, FMCG-2.5]
reading_minutes: 4
key_points:
  - "Nakit dönüşüm süresi = alacak tahsil süresi + stokta kalma süresi − borç ödeme süresi."
  - "Süre ne kadar uzunsa, satışı finanse etmek için o kadar çok para bağlanır."
  - "Bağlanan paranın bir finansman maliyeti vardır; yüksek faiz döneminde bu maliyet brüt kârın önemli bir kısmını yiyebilir."
  - "Alacak gününü birkaç gün kısaltmak, yeni kredi almadan nakit yaratır."
  - "Enflasyonda vadeli alacak, tahsil edilene kadar değer kaybeder."
glossary_terms: [nakit-donusum-suresi, alacak-tahsil-suresi, stok-gun-sayisi, borc-odeme-suresi, isletme-sermayesi]
related: [kb-fmcg-7-3-credit-collections-dso, kb-fmcg-7-2-distributor-roi, kb-eco-38-3-distributor-credit-risk-dbs, kb-fmcg-1-1-margin-vs-markup, kb-eco-18-3-real-vs-nominal-interest-fisher]
sources:
  - title: "A Cash Conversion Cycle Approach to Liquidity Analysis"
    authors: "Richards, V. D.; Laughlin, E. J."
    year: 1980
    type: article
    doi: "10.2307/3665310"
    url: "https://doi.org/10.2307/3665310"
    verified: true
    checked_on: 2026-10-28
    note: "Financial Management 9(1). Nakit dönüşüm süresi kavramının klasik kaynağı."
  - title: "Does Working Capital Management Affect Profitability of Belgian Firms?"
    authors: "Deloof, M."
    year: 2003
    type: article
    doi: "10.1111/1468-5957.00008"
    url: "https://doi.org/10.1111/1468-5957.00008"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Business Finance & Accounting 30(3–4), 573–588. Alacak ve stok günleri ile kârlılık ilişkisi."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Bir bayi malı alır, depoda bekletir, vadeli satar ve sonra tahsil eder. Bu sırada tedarikçisine de belli bir vadeyle öder. Aradaki fark, işletmenin kendi parasıyla ya da krediyle finanse ettiği süredir. Bu süreye **nakit dönüşüm süresi** (*cash conversion cycle*) denir. Kârlı görünen bir işletmenin neden sürekli nakit sıkıntısı çektiğini anlamanın en kısa yolu bu hesaptır.

## Temel fikir

Üç gün sayısı hesaplanır (yıllık veriyle, 365 gün üzerinden):

- **Alacak tahsil süresi** (*DSO*) = Ticari alacaklar ÷ Yıllık net satış × 365 → Satışın parası ortalama kaç günde geliyor?
- **Stokta kalma süresi** (*DIO*) = Stok ÷ Yıllık satılan malın maliyeti × 365 → Mal depoda ortalama kaç gün bekliyor?
- **Borç ödeme süresi** (*DPO*) = Ticari borçlar ÷ Yıllık satılan malın maliyeti × 365 → Tedarikçiye ortalama kaç günde ödüyorsunuz?

**Nakit dönüşüm süresi = Alacak tahsil süresi + Stokta kalma süresi − Borç ödeme süresi**

Bu sürenin karşılığı olan tutar, **net işletme sermayesidir** (ticari alacak + stok − ticari borç). Bu para işin içinde dönmek zorundadır ve bir maliyeti vardır: ya bankaya faiz ödersiniz ya da paranızı başka bir yerde değerlendirme fırsatını kaçırırsınız.

Yüksek enflasyon döneminde iki etki üst üste biner. Birincisi, finansman maliyeti yükselir. İkincisi, vadeli alacak tahsil edilene kadar satın alma gücünü kaybeder. Bu yüzden vade, fiyat kadar önemli bir ticari koşuldur.

## Bir örnek

> **Örnek (temsili rakamlar):** Aşağıdaki bayi gerçek bir işletme değildir; rakamlar `scripts/pilot_numbers.py` ile hesaplanmıştır. %45 yıllık finansman maliyeti ve aylık %3 enflasyon yalnızca örnek varsayımlardır.

Bir bayinin yıllık rakamları:

| Kalem | Tutar |
|---|---|
| Yıllık net satış | 120.000.000 TL |
| Satılan malın maliyeti | 105.000.000 TL |
| Ticari alacaklar | 14.000.000 TL |
| Stok | 9.000.000 TL |
| Ticari borçlar | 11.000.000 TL |

**Adım 1 — Gün sayıları**

- Alacak tahsil süresi = 14.000.000 ÷ 120.000.000 × 365 = **42,6 gün**
- Stokta kalma süresi = 9.000.000 ÷ 105.000.000 × 365 = **31,3 gün**
- Borç ödeme süresi = 11.000.000 ÷ 105.000.000 × 365 = **38,2 gün**

**Adım 2 — Nakit dönüşüm süresi**

42,6 + 31,3 − 38,2 = **35,7 gün** (yuvarlanmamış değerlerle 35,6 gün; yaklaşık 36 gün). Bayi, sattığı malın parasını tedarikçisine ödedikten yaklaşık 36 gün sonra tahsil ediyor.

**Adım 3 — Bunun maliyeti**

- Net işletme sermayesi = 14.000.000 + 9.000.000 − 11.000.000 = **12.000.000 TL**
- Yıllık %45 finansman maliyetiyle: 12.000.000 × 0,45 = **5.400.000 TL/yıl**
- Bayinin brüt kârı = 120.000.000 − 105.000.000 = 15.000.000 TL. Finansman maliyeti bu brüt kârın **%36,0**'sı ediyor.

**Adım 4 — Alacak gününü 10 gün kısaltmak**

- Günlük ortalama satış = 120.000.000 ÷ 365 = **328.767 TL**
- 10 günlük kısalma, alacaklardan 328.767 × 10 = **3.287.671 TL** nakit serbest bırakır.
- Bu tutar krediyle finanse edilmiyorsa yıllık tasarruf: 3.287.671 × 0,45 = **1.479.452 TL**.

**Adım 5 — Enflasyonun alacağa etkisi**

Aylık %3 enflasyonda, 60 gün vadeli 1.000.000 TL'lik bir alacağın bugünkü satın alma gücüyle değeri: 1.000.000 ÷ 1,03² = **942.596 TL**. Yani tahsilat zamanında yapılsa bile yaklaşık **57.404 TL** reel değer kaybı vardır. Gecikme bu kaybı büyütür.

## Sık yapılan hatalar

- Satış hedefini tutturmak için vadeyi uzatmak ve vadenin maliyetini fiyata yansıtmamak.
- Yalnızca kâr-zarar tablosuna bakıp nakit akışını izlememek: kâr eden işletme de nakitsiz kalabilir.
- Stok gününü ortalama olarak izlemek; yavaş dönen ürünlerin ortalamanın içinde kaybolması.
- Gün hesaplarında alacak için maliyeti, stok için satışı kullanmak (paydaları karıştırmak).
- Borç ödeme süresini tedarikçiyle ilişkiyi bozacak kadar uzatmaya çalışmak; erken ödeme iskontosunu kaçırmak.

## Pratikte nasıl uygulanır?

- [ ] Üç gün sayısını her ay aynı yöntemle hesaplayın ve trendini izleyin.
- [ ] Alacak tahsil süresini müşteri, temsilci ve bölge bazında görün; en uzun vadeli müşterileri ayrı listeleyin.
- [ ] Vade farkını fiyatlamaya dahil edin: peşin ve vadeli fiyat arasındaki farkı finansman maliyetiyle karşılaştırın.
- [ ] Satış ekibinin primine tahsilat ve vade hedefini de ekleyin.
- [ ] Stokta 60 günü aşan ürünleri ayrıca raporlayın.
- [ ] Tedarikçi vadeleri ile müşteri vadelerini yan yana koyup aradaki farkı nasıl finanse ettiğinizi netleştirin.

## Daha fazlası

- Richards, V. D. ve Laughlin, E. J. (1980). *A Cash Conversion Cycle Approach to Liquidity Analysis.* Financial Management, 9(1). https://doi.org/10.2307/3665310
- Deloof, M. (2003). *Does Working Capital Management Affect Profitability of Belgian Firms?* Journal of Business Finance & Accounting, 30(3–4), 573–588. https://doi.org/10.1111/1468-5957.00008
