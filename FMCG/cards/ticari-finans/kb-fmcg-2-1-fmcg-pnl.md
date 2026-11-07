---
id: kb-fmcg-2-1-fmcg-pnl
title: "Hızlı tüketimde gelir tablosu: Brüt satıştan faaliyet kârına"
summary: "Hızlı tüketim gelir tablosunun en büyük kalemlerinden biri ticari indirim ve desteklerdir. Bu kart brüt satıştan net satışa, oradan katkı payına ve faaliyet kârına giden yolu tek bir örnekle gösterir."
course: fmcg
category: ticari-finans
tags: [marj, raporlama, butce, muhasebe]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: temel
source_lessons: [FMCG-2.1]
reading_minutes: 3
key_points:
  - "Brüt satış ile net satış arasındaki fark çoğu zaman ticari indirim ve desteklerdir; bu fark yönetilmeden kârlılık konuşulamaz."
  - "Oranları net satışa göre hesaplayın; brüt satışa göre hesaplanan oranlar şirketler ve yıllar arasında karşılaştırılamaz."
  - "Katkı payı satırı, karar vermek için brüt kârdan daha kullanışlıdır çünkü değişken satış ve dağıtım giderlerini de düşer."
  - "Sabit giderler hacimle değişmediği için faaliyet kârı hacim değişimine katkı payından daha sert tepki verir."
glossary_terms: [net-satis, ticari-harcama, katki-payi, sabit-maliyet]
related: [kb-fmcg-2-2-gross-to-net, kb-fmcg-2-3-contribution-breakeven, kb-eco-33-4-income-statement, kb-fmcg-7-1-distributor-pnl, kb-fmcg-5-5-trade-spend-roi]
sources:
  - title: "Principles of Corporate Finance"
    authors: "Brealey, R. A.; Myers, S. C.; Allen, F."
    year: 2020
    type: book
    verified: false
    note: "Kitap; baskı yılı kontrol edilmedi."
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

Satış ekibi ciroyu, finans ekibi kârı konuşur ve aradaki köprü çoğu zaman kurulmaz. Bu kart, hızlı tüketim şirketinin gelir tablosunu yönetim gözüyle okumayı sağlar: Hangi satır neyi anlatır, hangi oran neye göre hesaplanır. Bütçe toplantısı, marka performans değerlendirmesi ve bayi kârlılık analizinden önce faydalıdır.

## Temel fikir

Yönetim amaçlı bir hızlı tüketim gelir tablosu genellikle şu sırayı izler:

1. **Brüt satış:** Liste fiyatı × satılan adet.
2. **Ticari indirim ve destekler** (*trade spend*): Fatura altı iskontolar, ciro primleri, promosyon destekleri, listeleme bedelleri.
3. **Net satış:** Brüt satış eksi ticari indirimler. Şirketin gerçekten elde ettiği gelir budur.
4. **Satılan malın maliyeti (SMM):** Hammadde, ambalaj, üretim işçiliği ve genel üretim giderleri.
5. **Brüt kâr:** Net satış eksi SMM.
6. **Değişken satış ve dağıtım giderleri:** Nakliye, depo elleçleme, satış primleri gibi hacimle değişen kalemler.
7. **Katkı payı:** Sabit giderleri karşılamaya kalan tutar.
8. **Sabit giderler:** Merkez kadro, kira, reklamın sabit kısmı, sistemler.
9. **Faaliyet kârı (FVÖK).**

**Neden net satış tabanı?** Ticari indirim oranı şirketten şirkete, yıldan yıla değişir. Bir şirket indirimi fatura üzerinde, diğeri yıl sonu primi olarak verir. Oranları brüt satışa göre hesaplarsanız aynı ekonomik durum farklı görünür. Net satış tabanı karşılaştırmayı adil kılar. Hangi kalemin brüt satıştan düşüleceği muhasebe politikasına da bağlıdır; şirketinizin uygulamasını mali müşavirinizle netleştirin.

**Neden katkı payı?** Brüt kâr, üretim maliyetini düşer ama müşteriye ulaştırma maliyetini düşmez. Kaplan ve Cooper'ın faaliyet tabanlı maliyetleme yaklaşımı da aynı noktaya işaret eder: Müşteriye hizmet maliyeti gözden kaçarsa kârlı görünen müşteri zarar ettirebilir. Katkı payı, "bir koli fazla satarsam ne kazanırım?" sorusuna doğrudan cevap verir.

**Tabloyu kim kullanır?** Kâr-zarar tablosu yalnızca finans ekibinin değil, satış ve pazarlama yöneticilerinin de ortak dilidir. Satış müdürü net satış ve ticari harcamadan, pazarlama müdürü reklam ve marka yatırımından, operasyon müdürü üretim maliyetinden sorumludur. Her yöneticinin kendi kararlarının tablonun hangi satırını etkilediğini bilmesi, kârlılık konuşmasını somutlaştırır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek bir şirkete ait değildir; hesaplar `scripts/cards_numbers_fmcg_b1.py` ile yapılmıştır.

| Satır | Tutar (TL) | Net satışa oranı |
|---|---|---|
| Brüt satış | 100.000.000 | |
| Ticari indirim ve destekler | 18.000.000 | %22,0 |
| **Net satış** | **82.000.000** | %100,0 |
| SMM | 47.560.000 | %58,0 |
| **Brüt kâr** | **34.440.000** | %42,0 |
| Değişken satış ve dağıtım | 7.380.000 | %9,0 |
| **Katkı payı** | **27.060.000** | %33,0 |
| Sabit giderler | 14.000.000 | %17,1 |
| **Faaliyet kârı** | **13.060.000** | %15,9 |

Dikkat edin: Ticari indirim brüt satışın %18'i, ama net satışa oranla %22,0. Toplantıda hangi oranı kullandığınızı açıkça söylemezseniz yanlış karşılaştırma yapılır. Ayrıca ticari indirimler SMM'den sonra en büyük ikinci kalemdir; reklam bütçesinden çoğu zaman büyüktür.

## Sık yapılan hatalar

- Ciro hedefini brüt satış üzerinden koyup ticari indirim artışını görmemek.
- Oranları bazen brüt, bazen net satışa göre hesaplamak.
- Ticari destekleri pazarlama gideri satırına gömüp net fiyat erozyonunu gizlemek.
- Brüt kârı karar ölçüsü olarak kullanıp nakliye ve depo maliyetlerini unutmak.
- Sabit giderleri adet başına dağıtıp "her ürün şu kadar sabit gider taşıyor" diyerek ürün çıkarma kararı vermek.

## Pratikte nasıl uygulanır?

- [ ] Yönetim raporunuzu yukarıdaki sırayla yeniden düzenleyin; ticari indirimleri ayrı satırda gösterin.
- [ ] Tüm oranları net satışa göre hesaplayın ve raporda bunu yazın.
- [ ] Değişken satış ve dağıtım giderlerini sabitlerden ayırmak için finans ekibiyle bir kez çalışın.
- [ ] Marka, kanal ve büyük müşteri bazında katkı payını ayrı ayrı görün.
- [ ] Satış müdürleri ve bölge müdürleri için tek sayfalık bir gelir tablosu özeti hazırlayın.

## Daha fazlası

- Brealey, R. A.; Myers, S. C.; Allen, F. (2020). *Principles of Corporate Finance.* (kaynak doğrulanmadı)
- Kaplan, R. S.; Cooper, R. (1998). *Cost & Effect: Using Integrated Cost Systems to Drive Profitability and Performance.* (kaynak doğrulanmadı)
