---
id: kb-ea-3-6-it-business-case
title: "Yazılım yatırımının iş gerekçesi: NBD, geri dönüş ve fayda takibi"
summary: "Bir sistem yatırımının iş gerekçesini net bugünkü değer, geri dönüş süresi ve basit getiriyle kurmayı; yüksek enflasyon ortamında basit getirinin neden yanıltabileceğini ve faydanın nasıl izleneceğini anlatır."
course: ea
category: yazilim-secimi-ve-proje
tags: [yatirim, butce, yazilim-secimi, kpi, enflasyon]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-3.6]
reading_minutes: 3
key_points:
  - "İş gerekçesi; yatırım, işletme maliyeti ve ölçülebilir faydaları yıllara yayarak gösterir."
  - "Net bugünkü değer (NBD), paranın zaman değerini hesaba katar; basit getiri katmaz."
  - "Yüksek iskonto oranında, kâğıt üstünde kârlı görünen bir yatırımın NBD'si negatif çıkabilir."
  - "Faydalar ilk yıl tam gelmez; kademeli artışı ve kötü senaryoyu ayrıca hesaplayın."
  - "Her fayda kalemi için bir sahip ve ölçüm yöntemi belirlenmedikçe gerekçe kâğıtta kalır."
glossary_terms: [net-bugunku-deger, toplam-sahip-olma-maliyeti]
related: [kb-ea-17-2-total-cost-of-ownership, kb-ea-3-2-it-plus-process-complementarity, kb-ea-17-1-build-buy-configure, kb-ea-18-4-post-go-live-dip]
sources:
  - title: "Beyond Computation: Information Technology, Organizational Transformation and Business Performance"
    authors: "Brynjolfsson, E.; Hitt, L. M."
    year: 2000
    type: article
    doi: "10.1257/jep.14.4.23"
    url: "https://doi.org/10.1257/jep.14.4.23"
    verified: true
    checked_on: 2026-10-28
    note: "Fayda ve tamamlayıcı yatırımlar."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

"Bu sistem kendini iki yılda öder" cümlesi, yönetim kurulunda sıkça duyulur ve nadiren kontrol edilir. Bu kart, bir yazılım yatırımının iş gerekçesini (*business case*) birkaç yıllık nakit akışıyla kurmanızı, sonucu **net bugünkü değer** (NBD, *net present value*) ile sınamanızı ve yatırım sonrası faydayı takip etmenizi sağlar. Finans müdürü ile genel müdürün aynı rakama bakmasını kolaylaştırır.

## Temel fikir

İyi bir iş gerekçesi dört bölümden oluşur:

1. **Yatırım:** Lisans ya da ilk abonelik dönemi, uygulama hizmeti, donanım, veri taşıma, eğitim.
2. **İşletme maliyeti:** Yıllık bakım veya abonelik, destek, BT personeli zamanı. (Ayrıntı için toplam sahip olma maliyeti kartına bakın.)
3. **Fayda:** Ölçülebilir kalemler; örneğin azalan hatalı sipariş, kısalan tahsil süresi, daha az fazla mesai, kayıp satışın azalması.
4. **Risk ve senaryo:** Faydanın geç gelmesi veya beklenenden az olması.

Üç ölçü birlikte kullanılır:

- **Basit getiri:** (Toplam net fayda − yatırım) ÷ yatırım. Anlaşılması kolaydır ama paranın zaman değerini dikkate almaz.
- **Geri dönüş süresi:** Kümülatif net akışın sıfırı geçtiği an.
- **NBD:** Her yılın net akışı (1 + r)^t ile iskonto edilip toplanır, yatırım düşülür. r, firmanın sermaye maliyeti ya da beklediği getiri oranıdır. Yüksek enflasyon ortamında nominal r yüksek olduğu için geç gelen faydanın bugünkü değeri çok azalır.

## Bir örnek

> **Örnek (temsili rakamlar):** Tutarlar ve oran gerçek değildir; hesaplar `scripts/cards_numbers_ea_b1.py` ile yapılmıştır.

Bir bayi saha satış ve ERP entegrasyonu için 1.800.000 TL yatırım yapıyor. Yıllık işletme maliyeti 250.000 TL. Brüt faydanın kademeli gelmesi bekleniyor: 1. yıl 500.000 TL, 2. yıl 900.000 TL, 3–5. yıllar 1.100.000 TL. İskonto oranı (nominal) %35.

| Yıl | Net akış | Bugünkü değer | Kümülatif net akış |
|---|---|---|---|
| 1 | 250.000 | 185.185 | −1.550.000 |
| 2 | 650.000 | 356.653 | −900.000 |
| 3 | 850.000 | 345.476 | −50.000 |
| 4 | 850.000 | 255.908 | 800.000 |
| 5 | 850.000 | 189.561 | 1.650.000 |

- Basit getiri: 5 yılın net faydası 3.450.000 TL → (3.450.000 − 1.800.000) ÷ 1.800.000 = **%91,7**.
- Geri dönüş süresi: yaklaşık **3,1 yıl**.
- NBD: bugünkü değerlerin toplamı − 1.800.000 = **−467.217 TL**.

Basit getiri "neredeyse iki kat" derken, %35 iskonto oranında yatırım değer yaratmıyor. Faydalar %30 düşük gelirse NBD **−1.033.549 TL**'ye iner. Bu sonuç "yatırım yapmayın" demek değildir; faydayı öne çekmenin (ör. önce en hızlı getiri sağlayacak modülü açmak) ya da yatırımı küçültmenin yollarını aramanız gerektiğini gösterir.

## Sık yapılan hatalar

- Faydayı ilk yıldan itibaren tam saymak.
- Yüksek enflasyonda yalnızca basit getiri ve geri dönüş süresine bakmak.
- Aynı faydayı iki kez saymak (ör. hem "daha az hata" hem "daha az iade" olarak).
- İç personel zamanını ve eğitim süresini maliyete koymamak.
- Yatırım onaylandıktan sonra faydayı hiç ölçmemek.

## Pratikte nasıl uygulanır?

- [ ] Fayda kalemlerini ölçülebilir hale getirin: bugünkü değer, hedef değer, ölçüm kaynağı.
- [ ] Her fayda kalemine bir sahip atayın (ör. hatalı sipariş için depo müdürü).
- [ ] İskonto oranını finans ile birlikte belirleyin ve tüm projelerde aynı oranı kullanın.
- [ ] En az iki senaryo hesaplayın: beklenen ve faydanın %30 düşük geldiği durum.
- [ ] Canlıya geçişten 6 ve 12 ay sonra fayda gerçekleşmesini raporlayın.

## Daha fazlası

- Brynjolfsson ve Hitt (2000), *Journal of Economic Perspectives* — BT yatırımlarının getirisi ve tamamlayıcı değişiklikler. https://doi.org/10.1257/jep.14.4.23
- İlgili kartlar: toplam sahip olma maliyeti, tamamlayıcılık.
