---
id: kb-eco-31-9-three-statement-model
title: "Üç tablo modeli: Kâr eden şirketin nakdi neden azalır?"
summary: "Gelir tablosu, bilanço ve nakit akış tablosunun birbirine nasıl bağlandığını, büyüyen bir distribütörde kârın alacak ve stok artışıyla nasıl nakit açığına dönüştüğünü ve basit bir üç tablo modelinin nasıl kurulacağını anlatır."
course: eco
category: kurumsal-finans
tags: [finansal-modelleme, nakit-akisi, planlama]
roles: [finans-muduru]
level: orta
source_lessons: [ECO-31.9, ECO-37.1]
reading_minutes: 3
key_points:
  - "Net kâr bilançoda özkaynağa, nakit akış tablosunda faaliyet nakdinin başlangıcına gider."
  - "Alacak ve stok artışı nakdi tüketir; tedarikçi borcu artışı nakit sağlar."
  - "Hızlı büyüyen bir distribütör kâr ederken nakit açığı verebilir."
  - "Model doğru kurulduysa bilanço her dönem denkleşir; denkleşmiyorsa bir bağlantı eksiktir."
glossary_terms: [serbest-nakit-akisi, isletme-sermayesi]
related: [kb-eco-33-6-cash-flow-statement, kb-eco-36-6-cash-flow-vs-profit, kb-eco-38-2-cash-conversion-cycle, kb-eco-31-10-scenario-sensitivity]
sources:
  - title: "Principles of Accounting, Volume 1: Financial Accounting"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters"
    verified: true
    checked_on: 2026-10-28
  - title: "IAS 7 Statement of Cash Flows"
    authors: "IFRS Foundation"
    year: 2026
    type: standard
    url: "https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/"
    verified: true
    checked_on: 2026-10-28
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

Bütçe yalnızca gelir tablosu olarak hazırlanırsa, yılın ortasında "kâr ediyoruz ama kasada para yok" sürprizi yaşanır. Üç tablo modeli, satış, kâr, işletme sermayesi ve finansman ihtiyacını birlikte görmenizi sağlar.

## Temel fikir

Üç tablo birbirine şu şekilde bağlanır:

1. **Gelir tablosu:** Satış − maliyetler = net kâr.
2. **Bilanço:** Net kâr (dağıtılmayan kısmı) özkaynağa eklenir. Alacak, stok, tedarikçi borcu, duran varlık ve kredi bakiyeleri dönem sonu itibarıyla gösterilir.
3. **Nakit akış tablosu:** Net kârdan başlar, amortisman gibi nakit dışı giderleri ekler, işletme sermayesi değişimlerini yansıtır, yatırım ve finansman nakitlerini ekler. Sonuç, bilançodaki nakit değişimine eşit olmalıdır.

**İşletme sermayesi etkisi:**

- Alacak artışı → nakit azalır (satış yaptınız ama tahsil etmediniz).
- Stok artışı → nakit azalır.
- Tedarikçi borcu artışı → nakit artar (ödemeyi ertelediniz).

Distribütörlerde alacak ve stok, ciroya oranla büyüktür. Ciro hızla büyürken bu kalemler de büyür ve nakdi tüketir.

**Modelin itici güçleri:** Satış büyümesi, brüt marj, faaliyet giderleri, alacak, stok ve borç gün sayıları, yatırım planı ve kredi koşulları. Bu varsayımları ayrı bir sayfada tutun.

### Modeli nasıl kontrol edersiniz?

- **Bilanço dengesi:** Her dönemde varlıklar, kaynaklar toplamına eşit olmalıdır. Fark varsa model hatalıdır.
- **Nakit mutabakatı:** Nakit akış tablosunun sonucu bilançodaki nakit değişimine eşit olmalıdır.
- **Makullük kontrolü:** Marjlar, gün sayıları ve büyüme oranları geçmiş verilerle ve sektörle tutarlı mı?

### Kredi ihtiyacını modellemek

Pratikte nakit, kredi ile dengelenir: Nakit asgari seviyenin altına düşerse model otomatik olarak kredi kullanır, fazla nakit varsa kredi geri ödenir. Bu yapı, faiz giderinin kredi bakiyesine bağlı olması nedeniyle döngüsel bir hesap doğurur. Faizi dönem başı bakiyesi üzerinden hesaplamak bu döngüyü önlemenin basit bir yoludur.

### Kullanım alanları

Üç tablolu model; bütçe, banka kredi başvurusu, yatırım kararı ve senaryo analizinin ortak temelidir. Bankalar çoğu zaman projeksiyonlarınızın gün sayıları ve geçmiş performansla tutarlı olup olmadığına bakar. Modeli şirket içinde tek bir sorumlunun yönetmesi ve varsayımların bir kayıt sayfasında tarihleriyle tutulması, farklı sürümlerin karışmasını önler.

## Bir örnek

> **Örnek (temsili rakamlar):** Kâr, işletme sermayesi ve yatırım tutarları varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b3.py` ile yapılmıştır.

Bir distribütörün cirosu bir yılda 100.000.000 TL'den 125.000.000 TL'ye çıkıyor (%25 büyüme). Net kâr 8.000.000 TL.

| Kalem | Tutar (TL) |
|---|---|
| Net kâr | 8.000.000 |
| + Amortisman | 2.000.000 |
| − Alacak artışı | 10.000.000 |
| − Stok artışı | 5.000.000 |
| + Tedarikçi borcu artışı | 3.000.000 |
| **= Faaliyetlerden nakit** | **-2.000.000** |
| − Yatırım harcaması | 4.000.000 |
| **= Serbest nakit akışı** | **-6.000.000** |

Şirket 8.000.000 TL kâr ederken 6.000.000 TL nakit açığı veriyor. Bu açık kredi, ortak sermayesi ya da işletme sermayesi iyileştirmesiyle kapatılmak zorunda.

## Sık yapılan hatalar

- Bütçeyi yalnızca gelir tablosu olarak hazırlamak.
- Büyüme planında alacak ve stok artışını hesaba katmamak.
- Kredi faizini, kredi bakiyesine bağlamadan sabit bir tutar olarak yazmak.
- Bilanço denkleşmediğinde "fark" satırıyla kapatmak.
- Varsayımları formüllerin içine gömmek.

## Pratikte nasıl uygulanır?

- [ ] Bütçeyi gelir tablosu, bilanço ve nakit akışı olarak üç tablo hâlinde hazırlayın.
- [ ] Alacak, stok ve borç gün sayılarını ayrı varsayımlar olarak modele girin.
- [ ] Her ay bilançonun denkleştiğini kontrol eden bir satır ekleyin.
- [ ] Büyüme hedefinin gerektirdiği ek finansmanı modelden çıkarıp bankanızla önceden görüşün.
- [ ] Modeli gerçekleşen rakamlarla aylık karşılaştırın.

## Daha fazlası

- OpenStax (2026). *Principles of Accounting, Volume 1: Financial Accounting*. https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters
- IFRS Foundation (2026). *IAS 7 Statement of Cash Flows*. https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/
- Koller, T.; Goedhart, M.; Wessels, D. (McKinsey & Company) (2020). *Valuation: Measuring and Managing the Value of Companies*.
