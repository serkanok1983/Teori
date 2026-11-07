---
id: kb-eco-33-4-income-statement
title: "Gelir tablosu: Brüt satıştan net kâra adım adım"
summary: "Gelir tablosunun yapısını, brüt satıştan indirimlere, satılan malın maliyetine, faaliyet giderlerine, finansman giderine ve vergiye kadar her satırın ne anlattığını ve bir distribütörün marjlarını nasıl okuyacağınızı anlatır."
course: eco
category: finansal-tablolar
tags: [finansal-tablolar, karlilik, raporlama]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: temel
source_lessons: [ECO-33.4]
reading_minutes: 3
key_points:
  - "Gelir tablosu bir dönemin performansını gösterir; brüt satıştan başlayıp net kâra ulaşır."
  - "Distribütörlerde brüt marj düşük, faaliyet giderleri kritik; küçük bir gider artışı faaliyet kârını büyük ölçüde etkiler."
  - "Finansman giderleri, faaliyet kârı güçlü görünen bir şirketi zarara sokabilir."
  - "FAVÖK, faaliyet kârına amortismanın eklenmesiyle bulunur ama nakit akışı değildir."
glossary_terms: [gelir-tablosu, brut-kar, faaliyet-kari, favok, net-satis]
related: [kb-eco-33-5-balance-sheet, kb-eco-33-6-cash-flow-statement, kb-eco-36-4-ratios-profitability-leverage, kb-eco-38-1-distributor-financial-statements]
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

Gelir tablosu, şirketinizin bir dönemde ne kadar kazandığını ve bu kazancın nerede eridiğini gösterir. Bu kart, tablonun her satırını bir distribütör gözüyle okumanızı ve hangi satırın hangi karara işaret ettiğini görmenizi sağlar.

## Temel fikir

Tipik gelir tablosu yapısı:

1. **Brüt satışlar:** Fatura tutarları (KDV hariç).
2. **Satış indirimleri:** İadeler, iskontolar, ciro primleri. Brüt satıştan düşülünce **net satışlar** bulunur.
3. **Satışların maliyeti:** Satılan malın stok maliyeti. Net satışlardan düşülünce **brüt kâr** bulunur.
4. **Faaliyet giderleri:** Pazarlama ve satış, genel yönetim giderleri (personel, depo, araç, kira). Brüt kârdan düşülünce **esas faaliyet kârı** bulunur.
5. **Finansman giderleri ve diğer gelir/giderler:** Faiz, kur farkı, vade farkları.
6. **Vergi öncesi kâr**, vergi gideri ve **net kâr**.

Satır yerleşimi raporlama çerçevesine göre farklılık gösterebilir; ama okuma mantığı aynıdır. Distribütörlerde kâr, büyük bir cironun üzerindeki ince bir katmandır. Brüt marjda bir puanlık kayıp faaliyet kârının önemli bir kısmını götürebilir.

### Gelir tablosunu analiz etmenin iki yolu

**Dikey analiz:** Her satırı net satışların yüzdesi olarak ifade edin. Böylece farklı büyüklükteki dönemleri ve şirketleri karşılaştırabilirsiniz. Distribütörde en kritik oranlar brüt marj, faaliyet gideri oranı ve finansman gideri oranıdır.

**Yatay analiz:** Aynı satırın dönemler arası değişimine bakın. Satışlar artarken faaliyet giderleri daha hızlı artıyorsa ölçek avantajı kaybediliyor demektir. Yüksek enflasyonda bu karşılaştırmayı reel değerlerle yapmayı unutmayın.

### Dikkat edilmesi gereken satırlar

- **Kur farkı ve vade farkı:** Esas faaliyet dışı gibi görünse de distribütörlerde işin doğal bir parçası olabilir. Vade farkı gelirini satış fiyatından ayrı izlemek, gerçek ticari marjı görmeyi sağlar.
- **Tek seferlik kalemler:** Varlık satış kârı veya olağandışı giderler, sürdürülebilir kârı olduğundan farklı gösterir. Bunları ayrıştırarak düzeltilmiş kârı hesaplayın.
- **Karşılık giderleri:** Şüpheli alacak ve stok değer düşüklüğü karşılıkları, yönetimin tahminine dayanır; ani azalış veya artışlar sorgulanmalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Tutarlar varsayımsaldır; vergi oranı örnek orandır. Hesaplar `scripts/cards_numbers_eco_b4.py` ile yapılmıştır.

| Satır | Tutar (TL) | Net satışa oran |
|---|---|---|
| Brüt satışlar | 220.000.000 | |
| Satış indirimleri | (20.000.000) | |
| **Net satışlar** | **200.000.000** | |
| Satışların maliyeti | (164.000.000) | |
| **Brüt kâr** | **36.000.000** | %18 |
| Faaliyet giderleri | (26.000.000) | |
| **Faaliyet kârı** | **10.000.000** | %5 |
| Finansman giderleri | (6.000.000) | |
| Vergi öncesi kâr | 4.000.000 | |
| Vergi (örnek oran %25) | (1.000.000) | |
| **Net kâr** | **3.000.000** | %1,5 |

Faaliyet giderleri içinde 2.000.000 TL amortisman var; FAVÖK 12.000.000 TL. Finansman giderleri faaliyet kârının yarısından fazlasını alıyor; bu şirketin önceliği, işletme sermayesini ve borcu azaltmak olmalı.

## Sık yapılan hatalar

- Brüt satışı ciro olarak raporlayıp indirimleri göz ardı etmek.
- Ciro primlerini faaliyet gideri olarak sınıflandırıp brüt marjı yüksek göstermek.
- Kur farklarını ve vade farklarını faaliyet kârı içinde göstermek ya da hiç ayırmamak.
- FAVÖK'ü nakit üretimi sanmak.
- Tek bir dönemin tablosuna bakıp eğilimleri incelememek.
- Brüt marjı aylık değil yalnızca yıllık izlemek; prim ve iskonto tahakkukları eksikse aylık marj yanıltıcı olur.

## Pratikte nasıl uygulanır?

- [ ] Aylık yönetim raporunuzu yukarıdaki yapıya göre düzenleyin ve her satırı net satışa oranlayın.
- [ ] Satış indirimlerini (iade, iskonto, prim) ayrı satırlarda izleyin.
- [ ] Finansman giderlerini faiz, kur farkı ve vade farkı olarak ayırın.
- [ ] Son 12 ayın eğilimini ve bütçeyle karşılaştırmasını raporlayın.
- [ ] Yasal tablolar ile yönetim raporu arasındaki farkları mali müşavirinizle mutabık kılın.
- [ ] Gelir tablosunu ürün grubu ve kanal bazında da hazırlayın.

## Daha fazlası

- OpenStax (2026). *Principles of Accounting, Volume 1: Financial Accounting*. https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters
- KGK (2026). *Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu (resmî site)*. https://www.kgk.gov.tr
- Koller, T.; Goedhart, M.; Wessels, D. (McKinsey & Company) (2020). *Valuation: Measuring and Managing the Value of Companies*.
