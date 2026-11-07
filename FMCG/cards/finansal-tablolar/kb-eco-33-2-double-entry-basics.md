---
id: kb-eco-33-2-double-entry-basics
title: "Çift taraflı kayıt: Bir satış muhasebeye nasıl yansır?"
summary: "Her işlemin en az iki hesabı etkilediği çift taraflı kayıt mantığını, borç ve alacak kavramlarını ve bir distribütörün vadeli satışının, satılan malın maliyetinin ve tahsilatın kayıtlara nasıl yansıdığını anlatır."
course: eco
category: finansal-tablolar
tags: [muhasebe, temel-kavramlar]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: temel
source_lessons: [ECO-33.2]
reading_minutes: 3
key_points:
  - "Her işlem en az iki hesabı eşit tutarda etkiler; toplam borçlar toplam alacaklara eşittir."
  - "Varlık ve gider hesapları borç tarafında artar; kaynak ve gelir hesapları alacak tarafında artar."
  - "Satış anında hasılat, KDV ve alacak; aynı anda satılan malın maliyeti ve stok azalışı kaydedilir."
  - "Tahsilat kâr yaratmaz; yalnızca alacağı nakde çevirir."
glossary_terms: [cift-tarafli-kayit, hasilat, kdv]
related: [kb-eco-33-3-accruals-period-close, kb-eco-33-4-income-statement, kb-eco-33-5-balance-sheet, kb-eco-43-4-kdv-vat]
sources:
  - title: "Principles of Accounting, Volume 1: Financial Accounting"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters"
    verified: true
    checked_on: 2026-10-28
  - title: "213 sayılı Vergi Usul Kanunu"
    authors: "T.C. Resmî Gazete / Mevzuat Bilgi Sistemi"
    year: 1961
    type: law
    url: "https://www.mevzuat.gov.tr/MevzuatMetin/1.4.213.pdf"
    verified: true
    checked_on: 2026-10-28
    note: "Mevzuat Bilgi Sistemi resmî PDF metni açıldı, kanun adı ve numarası eşleşti (2026-10-28)."
  - title: "Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu (resmî site)"
    authors: "KGK"
    year: 2026
    type: web
    url: "https://www.kgk.gov.tr"
    verified: true
    checked_on: 2026-10-28
    note: "TFRS/TMS ve BOBİ FRS metinlerinin Türkiye'deki yayımcısı."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Muhasebeci olmanız gerekmez, ama mizan, bilanço ve gelir tablosunu doğru okuyabilmek için kayıt mantığını bilmeniz gerekir. Bu kart, bir distribütörün en sık yaptığı işlemin, yani vadeli satışın kayıtlara nasıl yansıdığını gösterir.

## Temel fikir

**Temel denklik:** Varlıklar = Yabancı kaynaklar + Özkaynaklar.

Her işlem bu denkliği korur; bu yüzden her işlem en az iki hesabı etkiler. Bir hesaba **borç**, diğerine **alacak** kaydı yapılır ve tutarları eşittir. Buradaki "borç" ve "alacak" günlük dildeki anlamlarıyla değil, hesabın sol ve sağ tarafı olarak kullanılır.

| Hesap türü | Artış | Azalış |
|---|---|---|
| Varlık (kasa, banka, alacak, stok) | Borç | Alacak |
| Gider ve maliyet | Borç | Alacak |
| Yabancı kaynak (borçlar, ödenecek KDV) | Alacak | Borç |
| Özkaynak | Alacak | Borç |
| Gelir (hasılat) | Alacak | Borç |

Türkiye'de şirketler Tekdüzen Hesap Planı'nı kullanır; hesaplar numaralandırılmıştır (ör. alıcılar, ticari mallar, yurt içi satışlar). Kayıt düzeni Vergi Usul Kanunu ve ilgili tebliğlerle belirlenir.

### Neden yönetici için önemlidir?

Çift taraflı kayıt yalnızca muhasebecinin işi değildir. Bir işlemin hangi hesaplara gideceğini anlamak, raporları okumanızı ve hataları erken fark etmenizi sağlar:

- **Mizan:** Bütün hesapların borç ve alacak toplamlarını ve bakiyelerini gösterir. Borç toplamı her zaman alacak toplamına eşittir. Eşit değilse kayıt hatası vardır; eşit olması ise kayıtların doğru olduğunu garanti etmez (yanlış hesaba yapılan kayıt dengeyi bozmaz).
- **Muavin defter:** Bir hesabın, örneğin tek bir müşterinin cari hesabının, bütün hareketlerini gösterir. Cari mutabakat bu kayıtlar üzerinden yapılır.
- **Yevmiye defteri:** Bütün kayıtların tarih sırasıyla tutulduğu defterdir. Defter tutma ve onay kuralları Vergi Usul Kanunu ile belirlenir; e-defter kapsamındaki şirketler bunu elektronik ortamda tutar.

### Sık karşılaşılan durumlar

Tahsilat, satış değil bir varlığın başka bir varlığa dönüşmesidir: alacak azalır, banka artar. Kredi kullanımı gelir değildir: banka artar, borç artar. Stok alımı gider değildir: satılana kadar varlıktır. Bu üç ayrımı bilmek, kâr ile nakit arasındaki farkı anlamanın temelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Tutarlar varsayımsaldır; KDV oranı örnek orandır ve ürüne göre değişir. Hesaplar `scripts/cards_numbers_eco_b4.py` ile yapılmıştır.

Bir distribütör bir markete KDV hariç 100.000 TL'lik ürünü vadeli satıyor. Örnek KDV oranı %20. Ürünlerin stok maliyeti 70.000 TL.

**1. Satış kaydı:**

| Hesap | Borç (TL) | Alacak (TL) |
|---|---|---|
| Alıcılar (müşteri alacağı) | 120.000 | |
| Yurt içi satışlar (hasılat) | | 100.000 |
| Hesaplanan KDV | | 20.000 |

**2. Satılan malın maliyeti:**

| Hesap | Borç (TL) | Alacak (TL) |
|---|---|---|
| Satılan ticari mallar maliyeti | 70.000 | |
| Ticari mallar (stok) | | 70.000 |

Bu iki kayıtla brüt kâr 30.000 TL olur. KDV şirketin geliri değildir; devlete ödenecek bir yükümlülüktür.

**3. Tahsilat (60 gün sonra):** Banka hesabına borç 120.000 TL, alıcılar hesabına alacak 120.000 TL. Tahsilat kârı değiştirmez; alacağı nakde çevirir.

## Sık yapılan hatalar

- KDV dahil tutarı hasılat sanmak.
- Satış kaydını yapıp satılan malın maliyetini dönem sonuna bırakmak; aylık kârı yanlış görmek.
- Tahsilatı gelir sanmak.
- İade ve iskontoları ayrı hesaplarda izlememek.
- Borç ve alacak kavramlarını günlük anlamıyla yorumlamak.
- Mizandaki ters bakiyeli hesapları (ör. alacak bakiyesi veren kasa hesabı) incelememek.

## Pratikte nasıl uygulanır?

- [ ] Aylık mizanı mali müşavirinizden isteyin ve ana hesapların (alıcılar, stok, satıcılar, banka) bakiyelerini kendi kayıtlarınızla karşılaştırın.
- [ ] Satış, iade ve iskonto hesaplarını ayrı izleyin.
- [ ] Satılan malın maliyetinin aylık olarak kaydedildiğinden emin olun.
- [ ] ERP'nizdeki satış ve tahsilat işlemlerinin hangi hesaplara kayıt ürettiğini bir kez mali müşavirinizle birlikte gözden geçirin.
- [ ] Muhasebe uygulamalarında mevzuata uygunluğu mali müşavirinizle teyit edin.
- [ ] Aylık mizanı gözden geçirip olağandışı bakiyeleri muhasebeye sorun.

## Daha fazlası

- OpenStax (2026). *Principles of Accounting, Volume 1: Financial Accounting*. https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters
- T.C. Resmî Gazete / Mevzuat Bilgi Sistemi (1961). *213 sayılı Vergi Usul Kanunu*. https://www.mevzuat.gov.tr/MevzuatMetin/1.4.213.pdf
- KGK (2026). *Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu (resmî site)*. https://www.kgk.gov.tr
