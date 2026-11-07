---
id: kb-eco-33-3-accruals-period-close
title: "Tahakkuk esası ve dönem sonu kapanışı: Aylık kâr neden dalgalanır?"
summary: "Gelir ve giderlerin nakit ödendiği tarihe değil ait oldukları döneme kaydedilmesi gerektiğini, peşin ödenen giderleri, gider tahakkuklarını ve tedarikçi primlerini aylık kâra doğru yansıtmayı ve düzenli bir dönem sonu kapanış listesini anlatır."
course: eco
category: finansal-tablolar
tags: [muhasebe, raporlama, kapanis]
roles: [finans-muduru]
level: temel
source_lessons: [ECO-33.3]
reading_minutes: 3
key_points:
  - "Tahakkuk esasında gelir ve gider, nakit hareketinin tarihine değil ait olduğu döneme kaydedilir."
  - "Peşin ödenen yıllık giderler aylara dağıtılmazsa, ödeme ayında kâr düşük, diğer aylarda yüksek görünür."
  - "Yıl sonu primi gibi giderler her ay tahakkuk ettirilmezse, son ayda büyük bir sürpriz yaşanır."
  - "Kazanılmış ama faturası henüz gelmemiş tedarikçi primleri de kendi dönemine kaydedilmelidir."
glossary_terms: [tahakkuk-esasi, gider-tahakkuku]
related: [kb-eco-33-2-double-entry-basics, kb-eco-33-4-income-statement, kb-ea-20-4-record-to-report-close, kb-eco-36-7-earnings-quality-red-flags]
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
  - title: "213 sayılı Vergi Usul Kanunu"
    authors: "T.C. Resmî Gazete / Mevzuat Bilgi Sistemi"
    year: 1961
    type: law
    url: "https://www.mevzuat.gov.tr/MevzuatMetin/1.4.213.pdf"
    verified: true
    checked_on: 2026-10-28
    note: "Mevzuat Bilgi Sistemi resmî PDF metni açıldı, kanun adı ve numarası eşleşti (2026-10-28)."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28

---

## Ne işe yarar?

Aylık yönetim raporunda kâr bir ay çok yüksek, ertesi ay çok düşük çıkıyorsa, sorun çoğu zaman işin kendisinde değil, kayıt zamanlamasındadır. Bu kart, tahakkuk esasının mantığını ve aylık kapanışta nelere dikkat etmeniz gerektiğini anlatır.

## Temel fikir

**Nakit esası** ile işlem para girdiğinde ya da çıktığında kaydedilir. **Tahakkuk esası** ile ise gelir kazanıldığı dönemde, gider katlanıldığı dönemde kaydedilir. Finansal raporlama tahakkuk esasına dayanır.

Distribütörlerde sık görülen dört durum:

1. **Peşin ödenen giderler:** Yıllık depo kirası, sigorta, yazılım lisansı. Ödeme anında gelecek aylar giderleri olarak kaydedilir, her ay ilgili kısmı gidere aktarılır.
2. **Gider tahakkukları:** Yıl sonunda ödenecek satış primi, faturası gelmemiş enerji ve nakliye giderleri. Her ay tahmini tutarı gider ve borç olarak kaydedilir.
3. **Tedarikçi primleri ve ciro primleri:** Hedef bazlı primler yıl içinde kazanılır, ama fatura çoğu zaman dönem sonunda gelir. Kazanılan kısmın tahmini olarak her ay kaydedilmesi, maliyeti doğru gösterir.
4. **Kesilmemiş faturalar:** Teslim edilmiş ama faturası kesilmemiş satışlar, kendi döneminin hasılatıdır.

Vergi kuralları, bazı kalemlerin hangi döneme ait sayılacağı konusunda finansal raporlamadan farklı olabilir; yönetim raporlaması ile yasal kayıtlar arasındaki farkları mali müşavirinizle netleştirin.

### Ay sonu kapanış süreci

Tahakkuk esası, düzenli bir kapanış süreci gerektirir. Basit bir kontrol listesi:

1. Bütün satış ve alış faturalarının dönemine kaydedildiğini kontrol edin; sevk edilmiş ama faturalanmamış teslimatları belirleyin.
2. Banka hesaplarını ekstrelerle mutabık hâle getirin.
3. Büyük müşteri ve tedarikçilerle cari mutabakat yapın.
4. Tedarikçi primleri, satış primleri, enerji ve nakliye gibi faturası gelmemiş kalemleri tahakkuk ettirin.
5. Peşin ödenmiş giderlerin dönem payını gidere aktarın.
6. Amortisman, kıdem ve izin karşılıklarını hesaplayın.
7. Stok sayım veya kayıt farklarını inceleyin.

### Ne kadar hızlı?

Yönetim raporlarının ayın ilk haftası veya ilk on günü içinde hazır olması, kararların geç kalmamasını sağlar. Hızlı kapanış için bazı tahminler kullanmak kabul edilebilir; önemli olan, tahminlerin bir sonraki ay gerçekleşmeyle karşılaştırılıp düzeltilmesidir.

### Tahminlerin kalitesi

Tahakkuklar tahmine dayanır ve kârı yönlendirmek için kötüye kullanılabilir. Tahminlerin yöntemini yazılı hâle getirin ve her ay aynı yöntemi uygulayın.

## Bir örnek

> **Örnek (temsili rakamlar):** Tutarlar varsayımsaldır. Diğer tüm kalemler sonrası aylık kârın 2.000.000 TL olduğu varsayılmıştır. Hesaplar `scripts/cards_numbers_eco_b4.py` ile yapılmıştır.

Bir distribütör ocakta 1.200.000 TL yıllık depo kirasını peşin ödüyor. Yıl sonunda satış ekibine 600.000 TL prim ödenecek. Aralıkta 300.000 TL tedarikçi primi kazanılıyor, faturası şubatta gelecek.

| Ay | Nakit bazlı kayıt (TL) | Tahakkuk esasına göre (TL) |
|---|---|---|
| Ocak | 800.000 (kiranın tamamı gider) | 1.850.000 (aylık kira 100.000 + prim payı 50.000) |
| Aralık | 1.400.000 (primin tamamı gider, tedarikçi primi yok) | 2.150.000 (aylık kira ve prim payı, tedarikçi primi dahil) |

Tahakkuk esasında aylık kâr işin gerçek performansını yansıtır; nakit bazlı kayıt ise ocakta işi kötü, aralıkta ise yine yanlış gösterir.

## Sık yapılan hatalar

- Yıllık giderleri ödendikleri ayda gider yazmak.
- Yıl sonu primlerini ve izin karşılıklarını aylık tahakkuk ettirmemek.
- Tedarikçi primlerini yalnızca fatura geldiğinde kaydetmek.
- Ay sonu stok sayımı ve stok farklarını kapanışa yansıtmamak.
- Kapanışı her ay farklı kişiye ve farklı sıraya göre yaptırmak.

## Pratikte nasıl uygulanır?

- [ ] Yazılı bir aylık kapanış listesi hazırlayın: peşin giderler, tahakkuklar, primler, stok, kur değerlemesi.
- [ ] Yıllık ödenen giderleri ve yıl sonu primlerini aylık tahakkuk tablosunda izleyin.
- [ ] Tedarikçi primlerini hedef gerçekleşmesine göre her ay tahmin edip kaydedin.
- [ ] Kapanışı her ay aynı takvimle (ör. ayın 5. iş günü) tamamlayın.
- [ ] Yönetim raporu ile yasal kayıtlar arasındaki farkları mali müşavirinizle aylık olarak mutabık kılın.

## Daha fazlası

- OpenStax (2026). *Principles of Accounting, Volume 1: Financial Accounting*. https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters
- KGK (2026). *Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu (resmî site)*. https://www.kgk.gov.tr
- T.C. Resmî Gazete / Mevzuat Bilgi Sistemi (1961). *213 sayılı Vergi Usul Kanunu*. https://www.mevzuat.gov.tr/MevzuatMetin/1.4.213.pdf
