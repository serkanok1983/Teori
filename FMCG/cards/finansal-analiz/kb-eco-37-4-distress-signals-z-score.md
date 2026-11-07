---
id: kb-eco-37-4-distress-signals-z-score
title: "Finansal sıkıntı işaretleri ve Z-skoru: Müşteri ya da tedarikçi batmadan önce"
summary: "Finansal sıkıntının erken işaretlerini, Altman'ın Z-skoru yaklaşımını ve halka açık olmayan ve imalat dışı şirketler için uyarlanmış versiyonunu, hesaplamanın sınırlarını ve skorun kredi limiti ve tedarikçi bağımlılığı kararlarında nasıl kullanılacağını anlatır."
course: eco
category: finansal-analiz
tags: [kredi-riski, finansal-analiz, risk]
roles: [finans-muduru]
level: ileri
source_lessons: [ECO-37.4, ECO-37.5]
reading_minutes: 3
key_points:
  - "Finansal sıkıntı genellikle önce ödeme davranışında, sonra tablolarda görünür."
  - "Z-skoru, birkaç finansal oranı tek bir skorda birleştirerek iflas riskini sınıflandırır."
  - "Skor, geliştirildiği ülke ve dönemin verilerine dayanır; Türkiye'de bir ön tarama aracı olarak kullanılmalıdır."
  - "Düşük skor bir karar değil, ayrıntılı inceleme için bir tetikleyicidir."
glossary_terms: [z-skoru, finansal-sikinti]
related: [kb-eco-37-3-customer-credit-analysis, kb-eco-36-4-ratios-profitability-leverage, kb-eco-36-7-earnings-quality-red-flags, kb-eco-38-3-distributor-credit-risk-dbs]
sources:
  - title: "Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy"
    authors: "Altman, E. I."
    year: 1968
    type: article
    doi: "10.1111/j.1540-6261.1968.tb00843.x"
    url: "https://doi.org/10.1111/j.1540-6261.1968.tb00843.x"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Finance 23(4). Z-skorunun özgün çalışması."
  - title: "Financial Ratios As Predictors of Failure"
    authors: "Beaver, W. H."
    year: 1966
    type: article
    doi: "10.2307/2490171"
    url: "https://doi.org/10.2307/2490171"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Accounting Research 4."
  - title: "Financial Ratios and the Probabilistic Prediction of Bankruptcy"
    authors: "Ohlson, J. A."
    year: 1980
    type: article
    doi: "10.2307/2490395"
    url: "https://doi.org/10.2307/2490395"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Accounting Research 18(1)."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Bir müşterinin ya da kritik bir tedarikçinin batması, bir distribütör için ciddi kayıp ve operasyonel kesinti demektir. Bu kart, finansal sıkıntıyı erken fark etmek için hem gözlemsel işaretleri hem de basit bir sayısal skoru kullanmanızı sağlar.

## Temel fikir

**Gözlemsel işaretler:**

- Ödemelerde düzenli gecikme, vade uzatma talepleri, çek ve senetlerde ertelemeler.
- Sipariş yapısında değişiklik: daha küçük ve sık siparişler, nakit ihtiyacıyla yapılan indirimli satışlar.
- Yönetim ve ortaklık değişiklikleri, kilit çalışanların ayrılması.
- Diğer tedarikçilerin sevkiyatı durdurduğuna dair sektör bilgisi.

**Z-skoru:** Altman (1968), halka açık imalat şirketleri için birkaç finansal oranı ağırlıklandırarak iflası öngören bir skor geliştirdi. Beaver (1966) ve Ohlson (1980) da oranlara dayalı benzer modeller önerdi. Halka açık olmayan ve imalat dışı şirketler için Altman'ın sonradan geliştirdiği dört değişkenli versiyon yaygın olarak kullanılır:

**Z'' = 6,56 × X1 + 3,26 × X2 + 6,72 × X3 + 1,05 × X4**

- X1 = Net işletme sermayesi / Toplam varlıklar
- X2 = Geçmiş yıl kârları / Toplam varlıklar
- X3 = Faaliyet kârı / Toplam varlıklar
- X4 = Özkaynak (defter değeri) / Toplam borçlar

Bu versiyonda yaygın olarak kullanılan eşikler: 2,60'ın üzeri güvenli bölge, 1,10–2,60 gri bölge, 1,10'un altı sıkıntı bölgesi.

**Sınırlar:** Katsayılar başka bir ülkenin ve dönemin verileriyle tahmin edilmiştir. Yüksek enflasyon, enflasyon düzeltmesi ve farklı muhasebe uygulamaları oranları etkiler. Skoru bir ön tarama aracı olarak kullanın.

### İşaretleri bir sisteme bağlamak

Gözlemsel işaretler en erken uyarıdır, ama dağınık kalırsa işe yaramaz. Basit bir izleme sistemi kurun:

- Satış temsilcisi, müşteride gözlediği değişiklikleri (ortak değişikliği, personel azalması, boş raflar) bir forma girer.
- Muhasebe, ödeme gecikmelerini ve iade edilen çek ve senetleri haftalık olarak raporlar.
- Kredi sorumlusu bu bilgileri birleştirip müşteriyi bir izleme listesine alır.

İzleme listesindeki müşterilerde yeni sevkiyat, limit ve teminat kararları yeniden değerlendirilir.

### Z-skorunu doğru kullanmak

- Skoru tek bir yıla değil, birkaç yılın eğilimine göre değerlendirin. Düşüş eğilimi, eşiklerden daha anlamlı bir uyarıdır.
- Müşterinizin finansal tablolarının güncel ve güvenilir olduğundan emin olun. Bir yıl önceki tablolara dayanan skor, hızla değişen bir durumda geç kalabilir.
- Skoru kendi ödeme deneyiminizle karşılaştırın. Geçmişte temerrüde düşen müşterilerinizin skorlarına geriye dönük bakmak, eşiklerin sizin müşteri tabanınızda ne kadar işe yaradığını gösterir.
- Küçük müşterilerde mali tablo bulunmayabilir; bu durumda ödeme davranışı ve dış kayıtlar daha önemlidir.

## Bir örnek

> **Örnek (temsili rakamlar):** İki şirketin bilanço oranları varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b5.py` ile yapılmıştır.

| | Müşteri A | Müşteri B |
|---|---|---|
| X1 | 0,222 | 0,056 |
| X2 | 0,167 | 0,056 |
| X3 | 0,111 | 0,022 |
| X4 | 0,500 | 0,200 |
| **Z''** | **3,27** | **0,90** |

A güvenli bölgede. B sıkıntı bölgesinde: işletme sermayesi ince, birikmiş kârı az ve borçları özkaynağının beş katı. B için limit artışı yerine teminat istemek ve vadeyi kısaltmak değerlendirilmelidir.

## Sık yapılan hatalar

- Skoru kesin bir yargı olarak kullanmak.
- Halka açık imalat şirketleri için geliştirilen orijinal katsayıları her şirkete uygulamak.
- Yalnızca yıllık tablolara bakıp ödeme davranışındaki erken işaretleri kaçırmak.
- Kritik tedarikçilerin finansal durumunu hiç izlememek.
- Skoru bir kez hesaplayıp güncellememek.

## Pratikte nasıl uygulanır?

- [ ] En büyük müşterileriniz ve kritik tedarikçileriniz için yıllık Z'' skoru hesaplayın.
- [ ] Gri ve sıkıntı bölgesindeki şirketler için ayrıntılı inceleme yapın.
- [ ] Ödeme davranışı işaretlerini haftalık izleyin; skordan önce bunlara tepki verin.
- [ ] Kritik tedarikçiler için alternatif tedarik planı hazırlayın.
- [ ] Skoru, kredi limiti ve teminat kurallarınıza bir girdi olarak bağlayın.

## Daha fazlası

- Altman, E. I. (1968). *Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy*. https://doi.org/10.1111/j.1540-6261.1968.tb00843.x
- Beaver, W. H. (1966). *Financial Ratios As Predictors of Failure*. https://doi.org/10.2307/2490171
- Ohlson, J. A. (1980). *Financial Ratios and the Probabilistic Prediction of Bankruptcy*. https://doi.org/10.2307/2490395
