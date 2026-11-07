---
id: kb-fmcg-8-1-selling-formats
title: "Satış biçimleri: Ön satış, araçtan satış, telefonla ve dijital satış"
summary: "Bir noktaya her ay aynı biçimde gitmek zorunda değilsiniz. Bu kart saha satışının temel biçimlerini, her birinin sipariş başı maliyetini ve hangi nokta için hangisinin uygun olduğunu karşılaştırır."
course: fmcg
category: saha-satis-ekibi
tags: [saha-satis, pazara-giris, maliyet]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, saha-satis-temsilcisi]
level: temel
source_lessons: [FMCG-8.1]
reading_minutes: 3
key_points:
  - "Ön satışta temsilci siparişi alır, teslimatı ayrı bir araç yapar; araçtan satışta satış ve teslimat aynı ziyarette olur."
  - "Telefonla ve dijital satış, ziyaret başı maliyeti düşürür ama rafta yapılan işi yerine getirmez."
  - "Doğru ölçü ziyaret başı değil, sipariş başı ve satışa oranla maliyettir."
  - "Çoğu şirket nokta değerine göre biçimleri karıştıran hibrit bir model kullanır."
glossary_terms: [on-satis, aractan-satis, ziyaret-sikligi, pazara-giris-modeli]
related: [kb-fmcg-6-1-rtm-channels-formats, kb-fmcg-6-2-outlet-universe-segmentation, kb-fmcg-8-2-structured-sales-call, kb-fmcg-8-4-sales-force-sizing, kb-fmcg-6-7-e-grocery-quick-commerce]
sources:
  - title: "Building a Winning Sales Force"
    authors: "Zoltners, A. A.; Sinha, P.; Lorimer, S. E."
    year: 2009
    type: book
    verified: false
    note: "Kitap; künye kontrol edilmedi."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Saha satışı, bir hızlı tüketim şirketinin en büyük gider kalemlerinden biridir. Her noktaya aynı biçimde hizmet vermek, küçük noktalarda parayı boşa harcamak, büyük noktalarda ise fırsatı kaçırmak demektir. Bu kart, biçimleri maliyet ve etki açısından karşılaştırmanızı sağlar.

## Temel fikir

**Ön satış** (*pre-selling*). Temsilci noktayı ziyaret eder, siparişi alır, rafı düzenler. Teslimat bir sonraki gün ayrı bir araçla yapılır. Temsilci daha çok nokta gezebilir; teslimat aracı tam yüklenir.

**Araçtan satış** (*van selling*). Temsilci ürünle gelir, satışı ve teslimatı aynı anda yapar, çoğu zaman tahsilatı da alır. Küçük ve sık sipariş veren noktalarda, özellikle nakit çalışan geleneksel kanalda yaygındır. Ziyaret uzun sürer, araç kapasitesi sınırlıdır.

**Telefonla satış** (*telesales*). Sipariş telefonla alınır. Ziyaret başı maliyeti çok düşüktür ama raf, teşhir ve fiyat etiketi gibi mağaza içi işleri yapamaz.

**Dijital satış.** Noktanın sipariş uygulaması ya da bir B2B pazaryeri üzerinden sipariş vermesi. Sipariş maliyeti en düşüktür, ama noktanın alışkanlık kazanması zaman alır.

**Hibrit model.** Zoltners, Sinha ve Lorimer, satış ekibinin tasarımında farklı müşteri gruplarına farklı satış kanalları atamanın verimliliği artırdığını anlatır. Tipik bir hibrit model: büyük noktalara sık ön satış ziyareti, orta noktalara seyrek ziyaret ve arada telefon, küçük noktalara telefon ya da dijital sipariş.

**Biçimi değiştirirken dikkat edilecekler.** Bir noktayı ön satıştan telefonla ya da dijital siparişe geçirmek maliyeti düşürür, ama nokta sahibiyle yüz yüze ilişkiyi ve raftaki gözlemi azaltır. Bu nedenle geçişi aşamalı yapın: Önce düzenli ve öngörülebilir sipariş veren noktaları seçin, ilk aylarda yüz yüze ziyareti seyrekleştirerek sürdürün, sipariş tutarını ve raf bulunurluğunu karşılaştırın. Araçtan satışta nakit ve stok kontrolü ayrıca önemlidir; günlük kasa ve araç stok mutabakatı yapılmalıdır. Karma modeller yaygındır: Aynı nokta ayda bir yüz yüze, arada telefonla ya da uygulama üzerinden sipariş verebilir. Doğru karma, noktanın potansiyeline ve sipariş düzenine göre belirlenir.

## Bir örnek

> **Örnek (temsili rakamlar):** Maliyetler, ziyaret sayıları, sipariş oranları ve tutarlar varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b4.py` ile yapılmıştır.

| | Ön satış | Telefonla satış |
|---|---|---|
| Aylık çalışan maliyeti | 45.000 TL | 30.000 TL |
| Aylık temas | 176 ziyaret | 600 arama |
| Temas başı maliyet | 255,68 TL | 50,00 TL |
| Siparişle sonuçlanma | %70 | %35 |
| Sipariş sayısı | yaklaşık 123 | 210 |
| Sipariş başı maliyet | 365,26 TL | 142,86 TL |
| Ortalama sipariş | 2.500 TL | 1.200 TL |
| Maliyet / satış | %14,61 | %11,90 |

Temas başı bakınca telefonla satış beş kat ucuz görünüyor. Sipariş başı ve satışa oranla bakınca fark daralıyor. Ayrıca telefonla satış raf ve teşhir işini yapmıyor. Sonuç: Küçük noktalarda telefon mantıklı, büyük noktalarda ziyaret gerekli.

## Sık yapılan hatalar

- **Temas başı maliyetle karar vermek.** Sipariş oranı ve sipariş tutarı hesaba katılmalı.
- **Mağaza içi işi unutmak.** Telefon, raf ve teşhir kaybını görmez.
- **Dijital siparişi kendiliğinden yerleşecek sanmak.** Nokta sahibine teşvik ve eğitim gerekir.
- **Tek biçimde ısrar etmek.** Farklı nokta segmentleri farklı biçim gerektirir.

## Pratikte nasıl uygulanır?

- [ ] Noktalarınızı değerine ve ihtiyacına göre segmentlere ayırın.
- [ ] Her segment için biçimlerin sipariş başı maliyetini ve satışa oranını hesaplayın.
- [ ] Bir bölgede hibrit modeli pilot olarak deneyin ve satış, bulunurluk ve maliyeti karşılaştırın.
- [ ] Telefon ya da dijitale geçen noktalarda raf durumunu belirli aralıklarla kontrol edin.

## Daha fazlası

- Zoltners, A. A.; Sinha, P.; Lorimer, S. E. (2009). *Building a Winning Sales Force.* (kaynak doğrulanmadı)
