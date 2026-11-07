---
id: kb-fmcg-11-5-bullwhip-effect
title: "Kamçı etkisi: Talep dalgalanması zincir boyunca neden büyür?"
summary: "Tüketici talebi görece istikrarlıyken, perakendeci, dağıtıcı ve üretici siparişleri zincirin yukarısına doğru giderek daha fazla dalgalanır. Bu kart kamçı etkisinin nedenlerini, örnek bir simülasyonla büyüklüğünü ve azaltma yollarını anlatır."
course: fmcg
category: tedarik-zinciri-ve-stok
tags: [tedarik-zinciri, planlama, bayi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, depo-lojistik-muduru]
level: temel
source_lessons: [FMCG-11.5]
reading_minutes: 3
key_points:
  - "Kamçı etkisi, sipariş dalgalanmasının zincirin yukarısına doğru büyümesidir."
  - "Lee, Padmanabhan ve Whang dört ana neden tanımlar: tahminin siparişlere göre güncellenmesi, toplu sipariş, fiyat dalgalanmaları ve kıtlık oyunu."
  - "Her halka yalnızca bir alttaki halkanın siparişini görürse, dalgalanma her adımda büyür."
  - "Satış verisinin paylaşılması, sipariş sıklığının artırılması ve sürekli düşük fiyat etkiyi azaltır."
  - "Yüklemeye dayalı satış ve dönem sonu baskısı, kamçı etkisini satış ekibinin kendi eliyle yaratmasına yol açabilir."
glossary_terms: [kamci-etkisi, tahmin-hatasi, guvenlik-stoku]
related: [kb-fmcg-11-2-demand-forecasting, kb-fmcg-11-9-vmi-cpfr, kb-fmcg-11-6-sop-ibp, kb-fmcg-7-4-distributor-selection-kpis, kb-fmcg-5-4-promotion-economics]
sources:
  - title: "Information Distortion in a Supply Chain: The Bullwhip Effect"
    authors: "Lee, H. L.; Padmanabhan, V.; Whang, S."
    year: 1997
    type: article
    doi: "10.1287/mnsc.43.4.546"
    url: "https://doi.org/10.1287/mnsc.43.4.546"
    verified: true
    checked_on: 2026-10-28
    note: "Management Science 43(4), 546–558."
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

Fabrikadaki üretim planlayıcı, bir ay çok büyük siparişler, ertesi ay neredeyse hiç sipariş görür. Oysa mağazalarda tüketici aynı ürünü her hafta benzer miktarda alır. Bu kart, bu farkın nedenini, yani kamçı etkisini (*bullwhip effect*), ve satış ekibinin bu etkiyi azaltmadaki rolünü anlatır.

## Temel fikir

**Tanım.** Lee, Padmanabhan ve Whang'ın 1997 tarihli makalesi, tüketici talebindeki küçük dalgalanmaların perakendeci, dağıtıcı ve üretici siparişlerinde giderek büyüyen dalgalanmalara dönüştüğünü anlatır ve bu olguyu kamçı etkisi olarak adlandırır.

**Dört ana neden.** Makale dört temel neden tanımlar:

- **Talep sinyalinin işlenmesi:** Her halka, alttaki halkanın siparişini talep sinyali olarak kullanır ve tahminini buna göre günceller. Güvenlik stoku da eklenince sipariş dalgalanması büyür.
- **Toplu sipariş:** Taşıma ve sipariş maliyetleri nedeniyle siparişler seyrek ve büyük verilir.
- **Fiyat dalgalanmaları:** Promosyonlar ve fiyat artışı duyuruları, alıcıları ileri alıma (*forward buying*) yöneltir; ardından siparişler düşer.
- **Kıtlık oyunu:** Ürün kıt olduğunda alıcılar gerçek ihtiyaçlarından fazlasını sipariş eder, kıtlık bitince siparişleri iptal eder.

**Satış ekibinin rolü.** Hızlı tüketimde dönem sonu hedefleri, dağıtıcıya ve zincire yükleme yapılmasına yol açabilir. Bu yükleme, sonraki dönemde siparişlerin düşmesiyle sonuçlanır ve dalgalanmayı satış ekibinin kendisi yaratır. Sell-in ile sell-out arasındaki fark, bu etkinin en açık göstergesidir.

**Azaltma yolları.** Makalede ve sonraki literatürde önerilen yollar şunlardır:

- Satış verisinin (sell-out) zincir boyunca paylaşılması
- Sipariş sıklığının artırılması, karma araç yüklemesi
- Sürekli düşük fiyat ya da promosyonların daha düzgün dağıtılması
- Kıtlık dönemlerinde geçmiş satışa göre dağıtım (sipariş miktarına göre değil)
- Tedarikçi yönetimli stok ve ortak planlama

## Bir örnek

> **Örnek (temsili rakamlar):** Simülasyon varsayımdır: tüketici talebi rastgele üretilmiş (tohum 7), her halka son dört dönemin ortalamasıyla tahmin yapıp hedef stok seviyesine göre sipariş veriyor, tedarik süresi 2 dönem; hesaplar `scripts/cards_numbers_fmcg_b6.py` ile yapılmıştır.

| Halka | Siparişin standart sapması | Tüketici talebine oran |
|---|---|---|
| Tüketici talebi | 10,1 | 1,0 |
| Perakendeci siparişi | 19,2 | 1,9 |
| Dağıtıcı siparişi | 41,1 | 4,1 |
| Fabrika siparişi | 83,2 | 8,2 |

Her halka ortalama aynı miktarda ürün sipariş ediyor (fabrika düzeyinde ortalama **105,4**), ama dalgalanma her adımda yaklaşık iki katına çıkıyor. Fabrikanın gördüğü sipariş dalgalanması, tüketici talebindekinin **8,2** katı. Bu dalgalanmaya göre kapasite ve stok planlayan fabrika, gereğinden çok fazla kapasite ve stok tutmak zorunda kalır.

Bu sonuç basit bir varsayıma dayanıyor; gerçek zincirlerde oranlar farklı olacaktır. Ama mekanizma aynıdır: Her halka yalnızca alttakinin siparişini gördüğünde, dalgalanma büyür.

## Sık yapılan hatalar

- **Fabrika siparişini talep olarak görmek.** Talep, tüketicinin raftan aldığı miktardır.
- **Dönem sonunda yükleme yapmak.** Bu, sonraki dönemin siparişlerini düşürür ve dalgalanmayı artırır.
- **Sık ve büyük promosyonlar.** İleri alım, siparişleri dalgalandırır.
- **Kıtlıkta sipariş miktarına göre dağıtım yapmak.** Alıcıları fazla sipariş vermeye teşvik eder.
- **Satış verisini paylaşmamak.** Her halka yalnızca kendi siparişlerini görür.

## Pratikte nasıl uygulanır?

- [ ] Sell-in ve sell-out verilerinizi aynı grafikte haftalık olarak karşılaştırın.
- [ ] Dağıtıcı ve zincirlerle satış ve stok verisi paylaşımı için anlaşma yapın.
- [ ] Satış ekibinin hedeflerinde sell-out ve dağıtıcı stok gününü de izleyin.
- [ ] Promosyon takvimini dağıtın; büyük ileri alıma yol açan fiyat duyurularını planlı yapın.
- [ ] Kıtlık dönemlerinde geçmiş satışa göre dağıtım kuralı belirleyin.

## Daha fazlası

- Lee, H. L.; Padmanabhan, V.; Whang, S. (1997). *Information Distortion in a Supply Chain: The Bullwhip Effect.* Management Science 43(4), 546–558. https://doi.org/10.1287/mnsc.43.4.546
- Chopra, S.; Meindl, P. (2016). *Supply Chain Management: Strategy, Planning, and Operation.* (kaynak doğrulanmadı)
