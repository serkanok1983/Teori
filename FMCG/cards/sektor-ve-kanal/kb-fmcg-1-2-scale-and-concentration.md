---
id: kb-fmcg-1-2-scale-and-concentration
title: "Ölçek ve yoğunlaşma: Sabit maliyet, pazar payı ve HHI"
summary: "Hızlı tüketimde sabit maliyetlerin hacme yayılması büyük oyunculara avantaj sağlar. Bu kart birim maliyetin hacimle nasıl düştüğünü ve pazar yoğunlaşmasının CR4 ve HHI ile nasıl ölçüldüğünü gösterir."
course: fmcg
category: sektor-ve-kanal
tags: [maliyet, rekabet, pazar-payi, mevzuat]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [FMCG-1.2, ECO-8.1]
reading_minutes: 4
key_points:
  - "Sabit maliyet hacme bölündükçe birim maliyet düşer; reklam, dağıtım ve üretimdeki ölçek ekonomisi büyük markaları korur."
  - "CR4, en büyük dört firmanın pazar payları toplamıdır; HHI ise tüm firmaların paylarının karelerinin toplamıdır."
  - "HHI büyük oyunculara daha fazla ağırlık verir ve birleşmelerin yoğunlaşmayı ne kadar artırdığını gösterir."
  - "Rekabet Kurumu birleşme ve hâkim durum incelemelerinde pazar tanımı ve yoğunlaşmaya bakar; eşik ve kurallar için güncel mevzuata başvurun."
glossary_terms: [sabit-maliyet, degisken-maliyet, olcek-ekonomisi, hhi, cr4]
related: [kb-eco-5-5-economies-of-scale-sunk-costs, kb-eco-7-7-oligopoly-collusion, kb-fmcg-1-4-channel-power-conflict, kb-fmcg-2-3-contribution-breakeven, kb-fmcg-12-5-ethics-compliance-trade]
sources:
  - title: "Sunk Costs and Market Structure"
    authors: "Sutton, J."
    year: 1991
    type: book
    verified: false
    note: "Kitap; künye kontrol edilmedi."
  - title: "Rekabet Kurumu"
    authors: "Rekabet Kurumu"
    year: 2026
    type: web
    url: "https://www.rekabet.gov.tr/"
    verified: true
    checked_on: 2026-10-28
  - title: "4054 sayılı Rekabetin Korunması Hakkında Kanun"
    authors: "T.C. Mevzuat Bilgi Sistemi"
    year: 1994
    type: law
    url: "https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=4054&MevzuatTur=1&MevzuatTertip=5"
    verified: true
    checked_on: 2026-10-28
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Bir kategoride kaç güçlü oyuncu olduğunu ve neden küçük markaların zorlandığını anlamak; fiyat, yatırım ve ortaklık kararlarınızı etkiler. Üretici için ölçek, birim maliyeti ve reklam gücünü belirler. Bayi için ise hangi markaların kategoride kalıcı olacağını gösterir. Bu kart iki aracı verir: birim maliyetin hacimle değişimi ve yoğunlaşma ölçüleri.

## Temel fikir

**Sabit ve değişken maliyet.** Fabrika kirası, makine, reklam kampanyası ve merkez kadro gibi giderler üretim miktarından bağımsızdır; bunlar **sabit maliyettir**. Hammadde, ambalaj ve adet başı nakliye ise hacimle birlikte artar; bunlar **değişken maliyettir**. Birim maliyet şöyle hesaplanır:

Birim maliyet = Değişken maliyet + Sabit maliyet ÷ Hacim

Hacim büyüdükçe sabit maliyetin adet başına düşen payı küçülür. Buna **ölçek ekonomisi** denir. Hızlı tüketimde ölçek üç yerde birden çalışır: üretimde, reklamda (ulusal kampanyanın maliyeti satış adedine bölünür) ve dağıtımda (dolu kamyon, yoğun rota).

Sutton (1991), reklam ve ar-ge gibi geri dönüşü olmayan harcamaların bazı gıda kategorilerinde pazar büyüse bile yoğunlaşmayı yüksek tuttuğunu gösterir. Pratik sonucu şudur: Bazı kategorilerde birkaç büyük marka kalıcıdır. Küçük oyuncu ancak niş, bölgesel ya da fiyat odaklı bir konumla yaşar.

**Yoğunlaşma ölçüleri.**

- **CR4:** En büyük dört firmanın pazar payları toplamı.
- **HHI** (*Herfindahl-Hirschman Index*): Tüm firmaların yüzde olarak pazar paylarının karelerinin toplamı. Tek firmalı pazarda 10.000'dir; çok parçalı pazarda sıfıra yaklaşır.

HHI büyük paylara daha fazla ağırlık verir. Bu nedenle iki firmanın birleşmesinin yoğunlaşmayı ne kadar artırdığını göstermekte CR4'ten daha duyarlıdır.

> **Dikkat:** Rekabet Kurumu, 4054 sayılı Kanun kapsamında birleşme ve devralmaları ve hâkim durumun kötüye kullanılmasını inceler. Pazar tanımı ve hangi eşiğin sorun sayılacağı vakaya göre değişir. Bu kart yalnızca hesap mantığını anlatır; hukuki değerlendirme yerine geçmez.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek bir kategoriye ait değildir; hesaplar `scripts/cards_numbers_fmcg_b1.py` ile yapılmıştır.

**1. Hacim ve birim maliyet**

Yıllık sabit maliyet 12.000.000 TL, değişken maliyet 18 TL/adet.

| Yıllık hacim | Birim maliyet |
|---|---|
| 1.000.000 adet | 30,00 TL |
| 2.000.000 adet | 24,00 TL |
| 4.000.000 adet | 21,00 TL |

Hacmi dört katına çıkaran üretici, birim maliyette 9 TL avantaj kazanıyor. Yarısı kadar hacimle aynı rafta yarışan küçük rakip bu farkı ya marjından ya da reklamından kısmak zorunda kalır.

**2. CR4 ve HHI**

Bir kategoride pazar payları: %30, %20, %15, %10, %8, %7, %5, %5.

- CR4 = 30 + 20 + 15 + 10 = **%75**
- HHI = 30² + 20² + 15² + 10² + 8² + 7² + 5² + 5² = **1.788**

Birinci ve üçüncü firma birleşirse yeni paylar %45, %20, %10, %8, %7, %5, %5 olur. HHI **2.688**'e çıkar; artış **900** puandır. CR4 ise yalnızca %75'ten %90'a çıkıyor gibi görünür, ama birleşen firmanın tek başına kategorinin neredeyse yarısını tuttuğunu HHI çok daha net gösterir.

## Sık yapılan hatalar

- Birim maliyeti tek bir hacim için hesaplayıp hacim düşünce maliyetin de değişeceğini unutmak.
- Reklam ve dağıtım harcamalarını ölçek hesabının dışında tutmak.
- Pazar payını yanlış tabanda ölçmek: kategori, kanal ve bölge tanımı değişince paylar da değişir.
- HHI'yi oranlarla (0,30) hesaplayıp yüzde tabanlı sonuçla (30) karıştırmak.
- Yoğunlaşma hesabını hukuki sonuç gibi yorumlamak; rekabet hukuku değerlendirmesi uzman işidir.

## Pratikte nasıl uygulanır?

- [ ] Üretici olarak ana ürünleriniz için sabit ve değişken maliyeti ayırın; üç farklı hacimde birim maliyeti çıkarın.
- [ ] Kategoriniz için güncel pazar payı verisini (panel ya da perakende ölçüm) kullanarak CR4 ve HHI hesaplayın.
- [ ] Bayi olarak portföyünüzdeki markaların kategori içindeki yerini görün; ölçek avantajı zayıf markalara yatırım yaparken temkinli olun.
- [ ] Bir birleşme, devralma ya da özel dağıtım anlaşması gündemdeyse rekabet hukuku danışmanından görüş alın.
- [ ] Ölçek avantajınızı nerede kullandığınızı (fiyat mı, reklam mı, dağıtım mı) yönetim ekibiyle açıkça konuşun.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın.

## Daha fazlası

- Sutton, J. (1991). *Sunk Costs and Market Structure.* (kaynak doğrulanmadı)
- Rekabet Kurumu (2026). *Rekabet Kurumu.* https://www.rekabet.gov.tr/
- T.C. Mevzuat Bilgi Sistemi (1994). *4054 sayılı Rekabetin Korunması Hakkında Kanun.* https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4054.pdf
