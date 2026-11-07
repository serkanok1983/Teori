---
id: kb-eco-33-5-balance-sheet
title: "Bilanço: Varlıklar, borçlar ve özkaynak bir distribütörde nasıl okunur?"
summary: "Bilançonun yapısını, dönen ve duran varlıkları, kısa ve uzun vadeli borçları, özkaynağı ve bir distribütörün bilançosunda işletme sermayesi, cari oran, likidite oranı ve net borcun nasıl hesaplanıp yorumlanacağını anlatır."
course: eco
category: finansal-tablolar
tags: [finansal-tablolar, likidite, isletme-sermayesi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: temel
source_lessons: [ECO-33.5]
reading_minutes: 3
key_points:
  - "Bilanço belirli bir tarihteki durumu gösterir: Varlıklar = Borçlar + Özkaynak."
  - "Distribütörlerde bilançonun büyük kısmı alacak ve stoktan oluşur; bunların kalitesi kritik önemdedir."
  - "Cari oran ve likidite oranı kısa vadeli ödeme gücünü gösterir ama alacak ve stok kalitesine göre yorumlanmalıdır."
  - "Net borç, finansal borçlardan nakdin düşülmesiyle bulunur ve bankaların en çok baktığı göstergelerdendir."
glossary_terms: [bilanco, isletme-sermayesi, cari-oran, net-borc]
related: [kb-eco-33-4-income-statement, kb-eco-33-6-cash-flow-statement, kb-eco-38-1-distributor-financial-statements, kb-eco-38-2-cash-conversion-cycle]
sources:
  - title: "Principles of Accounting, Volume 1: Financial Accounting"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters"
    verified: true
    checked_on: 2026-10-28
  - title: "Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu (resmî site)"
    authors: "KGK"
    year: 2026
    type: web
    url: "https://www.kgk.gov.tr"
    verified: true
    checked_on: 2026-10-28
    note: "TFRS/TMS ve BOBİ FRS metinlerinin Türkiye'deki yayımcısı."
  - title: "Valuation: Measuring and Managing the Value of Companies"
    authors: "Koller, T.; Goedhart, M.; Wessels, D. (McKinsey & Company)"
    year: 2020
    type: book
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

Gelir tablosu bir dönemin filmini, bilanço ise belirli bir günün fotoğrafını verir. Bankalar, tedarikçiler ve yatırımcılar şirketinizi büyük ölçüde bilançoya bakarak değerlendirir. Bu kart, bir distribütörün bilançosunu okumanızı ve temel oranları hesaplamanızı sağlar.

## Temel fikir

**Varlıklar:**

- **Dönen varlıklar:** Nakit, ticari alacaklar, stok, diğer kısa vadeli varlıklar.
- **Duran varlıklar:** Depo, araç, raf sistemleri, yazılım gibi uzun ömürlü varlıklar.

**Kaynaklar:**

- **Kısa vadeli yabancı kaynaklar:** Tedarikçi borçları, kısa vadeli banka kredileri, vergi ve SGK borçları.
- **Uzun vadeli yabancı kaynaklar:** Vadesi bir yıldan uzun krediler, kıdem tazminatı karşılığı.
- **Özkaynaklar:** Sermaye ve geçmiş yıl kârları.

**Temel oranlar:**

- **Net işletme sermayesi** = Dönen varlıklar − Kısa vadeli yabancı kaynaklar.
- **Cari oran** = Dönen varlıklar / Kısa vadeli yabancı kaynaklar.
- **Likidite (asit-test) oranı** = (Dönen varlıklar − Stok) / Kısa vadeli yabancı kaynaklar.
- **Net borç** = Finansal borçlar − Nakit.
- **Borç/özkaynak** = Finansal borçlar / Özkaynak.

### Bilançoyu okumak

**Vade uyumu:** Uzun vadeli varlıkları (depo, araç) kısa vadeli kredilerle finanse etmek, her vade sonunda yeniden finansman riskini doğurur. Kalıcı işletme sermayesi ihtiyacının da en azından bir kısmının uzun vadeli kaynaklarla karşılanması daha sağlamdır.

**Kalitesine bakın:** Bilançodaki rakamlar aynı kalitede değildir.

- **Alacaklar:** Vadesi geçmiş veya ilişkili taraflardan olan alacakların payı nedir?
- **Stok:** Yavaş dönen, son kullanma tarihi yaklaşan veya modası geçmiş ürünler var mı?
- **Ortaklardan alacaklar:** Ortaklara verilen borçlar, özkaynağın fiilen azaldığı anlamına gelebilir ve vergi açısından da risk taşır.

**Bilanço dışı yükümlülükler:** Verilen teminat mektupları, kefaletler ve bazı sözleşme taahhütleri bilançoda görünmez ama dipnotlarda açıklanır.

### Tarih etkisi

Bilanço tek bir günün fotoğrafıdır. Dönem sonundan hemen önce yapılan tahsilat kampanyası veya tedarikçi ödemelerinin ertelenmesi, oranları geçici olarak iyi gösterebilir. Bu yüzden yıl içindeki aylık bakiyelere ve ortalamalara da bakın. Yüksek enflasyonda tarihî maliyetle gösterilen duran varlıklar ve özkaynak, enflasyon düzeltmesi yapılmazsa olduğundan düşük görünür.

## Bir örnek

> **Örnek (temsili rakamlar):** Tutarlar varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b4.py` ile yapılmıştır.

| Varlıklar | TL | Kaynaklar | TL |
|---|---|---|---|
| Nakit | 5.000.000 | Tedarikçi borçları | 30.000.000 |
| Ticari alacaklar | 40.000.000 | Kısa vadeli krediler | 20.000.000 |
| Stok | 25.000.000 | Uzun vadeli krediler | 10.000.000 |
| Duran varlıklar | 20.000.000 | Özkaynak | 30.000.000 |
| **Toplam** | **90.000.000** | **Toplam** | **90.000.000** |

- Dönen varlıklar 70.000.000 TL, kısa vadeli yabancı kaynaklar 50.000.000 TL; net işletme sermayesi 35.000.000 TL.
- Cari oran 1,40, likidite oranı 0,90.
- Net borç 25.000.000 TL, borç/özkaynak 1,00.

Cari oran ilk bakışta rahat görünüyor; ama stok çıkarıldığında oran 1'in altına düşüyor. Yani kısa vadeli borçların ödenmesi stok satışına ve alacak tahsilatına bağlı. Alacakların içinde vadesi geçmiş ya da şüpheli tutarlar varsa tablo daha da zayıflar.

## Sık yapılan hatalar

- Cari oranı yüksek diye likiditeyi güçlü sanmak; alacak ve stok kalitesine bakmamak.
- Yıl sonu bilançosunu "güzelleştirmek" için dönem sonu tahsilat ve ödemeleri kaydırmak; bankalar bu oyunları fark eder.
- Kıdem tazminatı karşılığı gibi gizli yükümlülükleri ihmal etmek.
- Ortaklara olan borç ve alacakları ayrı izlememek.
- Bilançoyu yalnızca yıl sonunda incelemek.

## Pratikte nasıl uygulanır?

- [ ] Aylık bilanço hazırlatın ve yukarıdaki oranları bir tabloda izleyin.
- [ ] Alacakları yaşlandırma tablosuyla, stoğu yaşına göre ayrıştırın.
- [ ] Net borç ve borç/özkaynak için ana bankalarınızın beklentilerini öğrenip iç sınırlar belirleyin.
- [ ] Bilanço dışı yükümlülükleri (teminat mektupları, kefaletler) ayrıca listeleyin.
- [ ] Yıllık bilançoyu bankalara sunmadan önce mali müşavirinizle oranların tutarlılığını gözden geçirin.

## Daha fazlası

- OpenStax (2026). *Principles of Accounting, Volume 1: Financial Accounting*. https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters
- KGK (2026). *Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu (resmî site)*. https://www.kgk.gov.tr
- Koller, T.; Goedhart, M.; Wessels, D. (McKinsey & Company) (2020). *Valuation: Measuring and Managing the Value of Companies*.
