---
id: kb-eco-26-4-business-valuation-basics
title: "Şirket değerleme temelleri: Çarpanlar ve indirgenmiş nakit akışı"
summary: "Bir dağıtım ya da üretim şirketinin değerini FAVÖK çarpanı ve indirgenmiş nakit akışı yöntemleriyle tahmin etmeyi, firma değeri ile özkaynak değeri arasındaki farkı ve değerlemenin varsayımlara ne kadar duyarlı olduğunu anlatır."
course: eco
category: kurumsal-finans
tags: [degerleme, kurumsal-finans, birlesme-satin-alma]
roles: [uretici-sahibi, bayi-sahibi, finans-muduru]
level: ileri
source_lessons: [ECO-26.4, ECO-26.6]
reading_minutes: 3
key_points:
  - "Firma değeri şirketin tüm faaliyetlerinin değeridir; özkaynak değerine ulaşmak için net borç düşülür."
  - "Çarpan yöntemi hızlıdır ama karşılaştırılabilir şirket seçimine çok bağlıdır."
  - "İndirgenmiş nakit akışı yönteminde değerin büyük kısmı çoğu zaman uç değerden gelir."
  - "Büyüme oranı ve iskonto oranındaki küçük değişiklikler değeri ciddi biçimde değiştirir."
glossary_terms: [firma-degeri, favok, serbest-nakit-akisi]
related: [kb-eco-31-8-mergers-acquisitions, kb-eco-25-1-time-value-npv-irr, kb-eco-31-2-cost-of-capital, kb-eco-31-10-scenario-sensitivity]
sources:
  - title: "Valuation: Measuring and Managing the Value of Companies"
    authors: "Koller, T.; Goedhart, M.; Wessels, D. (McKinsey & Company)"
    year: 2020
    type: book
    verified: true
    checked_on: 2026-10-28
  - title: "Principles of Finance"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-finance/pages/1-why-it-matters"
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
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Bir bölge distribütörünü satın almak, ortaklık payı devretmek, aile içinde hisse paylaşımı yapmak ya da şirketinizi satmayı düşünmek... Bu kart, bir şirketin değerini konuşurken kullanılan iki temel yöntemi ve en sık yapılan hesap hatalarını anlatır.

## Temel fikir

**Firma değeri ve özkaynak değeri:** Firma değeri (*enterprise value*), şirketin faaliyetlerinin tümünün değeridir. Hissedarlara kalan **özkaynak değeri** = firma değeri − net borç (finansal borçlar eksi nakit).

**1. Çarpan yöntemi:** Firma değeri = FAVÖK × çarpan. Çarpan, benzer şirketlerin işlem ya da piyasa değerlerinden çıkarılır. Hızlı ve anlaşılırdır, ama şunlara dikkat edin: Karşılaştırılan şirketler büyüklük, büyüme, müşteri yoğunluğu ve kârlılık açısından benzer mi? FAVÖK tek seferlik kalemlerden arındırılmış mı?

**2. İndirgenmiş nakit akışı (İNA):** Gelecekteki serbest nakit akışları sermaye maliyetiyle bugüne iskonto edilir. Tahmin döneminin sonrası için **uç değer** hesaplanır; sabit büyüme varsayımıyla:

Uç değer = gelecek yılın serbest nakit akışı / (iskonto oranı − büyüme oranı)

Koller ve diğerlerinin değerleme kitabında da vurgulandığı gibi, değeri sonuçta büyüme, kârlılık ve sermaye getirisi belirler; yöntem yalnızca bu varsayımları sayıya çevirir. Yüksek enflasyonda nominal büyüme ve nominal iskonto oranının tutarlı olması kritik önemdedir.

### Firma değerinden özkaynak değerine

Bir şirketi satın alırken ödenen fiyat genellikle özkaynak değeridir. Firma değerinden özkaynak değerine geçerken:

- **Net borç düşülür:** Finansal borçlar eksi nakit.
- **Borç benzeri kalemler düşülür:** Kıdem tazminatı yükümlülüğü, vadesi geçmiş vergi ve SGK borçları, ödenmemiş kâr payları.
- **İşletme sermayesi ayarlaması yapılır:** Satıcı, satıştan önce alacakları tahsil edip stoğu azaltarak ve tedarikçi ödemelerini erteleyerek nakit çekebilir. Bu yüzden sözleşmelerde "normal" işletme sermayesi seviyesi belirlenir ve kapanışta fark fiyata yansıtılır.

### Distribütör değerlemesinde özel noktalar

- **Tedarikçi sözleşmeleri:** Distribütörün değeri büyük ölçüde temsil ettiği markalara bağlıdır. Sözleşmelerin süresi, fesih koşulları ve münhasırlık hakları değeri doğrudan etkiler.
- **Müşteri yoğunlaşması:** Birkaç büyük müşteriye bağımlılık, daha düşük çarpan anlamına gelir.
- **Normalleştirilmiş kâr:** Ortaklara ödenen piyasa dışı ücretler, ilişkili taraf kiraları ve tek seferlik kalemler düzeltilir.

### Değer ile fiyat farklıdır

Değerleme bir aralık verir; fiyat ise müzakereyle belirlenir. Alıcının sinerjileri, satıcının alternatifleri ve ödeme koşulları (peşin, taksitli, performansa bağlı ek ödeme) nihai fiyatı belirler.

## Bir örnek

> **Örnek (temsili rakamlar):** FAVÖK, çarpan, borç ve oranlar varsayımsaldır; gerçek bir işlem ya da sektör çarpanı değildir. Hesaplar `scripts/cards_numbers_eco_b3.py` ile yapılmıştır.

**Çarpan yöntemi:** FAVÖK 40.000.000 TL, çarpan 5. Firma değeri 200.000.000 TL; net borç 60.000.000 TL; özkaynak değeri **140.000.000 TL**.

Çarpan 4 olursa özkaynak 100.000.000 TL (−%29), 6 olursa 180.000.000 TL (%29). Çarpandaki bir birimlik fark, özkaynak değerini yaklaşık %30 oranında değiştiriyor; çünkü borç sabit kalıyor.

**Uç değer duyarlılığı:** Gelecek yılın serbest nakit akışı 25.000.000 TL, iskonto oranı %30, büyüme %20. Uç değer **250.000.000 TL**. Büyüme varsayımı %18 olursa uç değer 208.333.333 TL'ye iner (−%16,7).

## Sık yapılan hatalar

- Firma değerini özkaynak değeri sanmak; net borcu düşmemek.
- Tek seferlik gelirlerle şişmiş FAVÖK'ü çarpanla çarpmak.
- Büyük, borsada işlem gören şirketlerin çarpanını küçük bir aile şirketine doğrudan uygulamak.
- Büyüme oranını iskonto oranına çok yakın seçip uç değeri şişirmek.
- İşletme sermayesi ihtiyacını serbest nakit akışından düşmemek.

## Pratikte nasıl uygulanır?

- [ ] Değerlemeye son 3 yılın düzeltilmiş FAVÖK'ü ve serbest nakit akışıyla başlayın.
- [ ] Net borcu kapanış tarihindeki bilançodan, kiralama ve kıdem yükümlülükleri dahil açıkça hesaplayın.
- [ ] En az iki yöntem kullanın ve sonuçları bir aralık olarak sunun.
- [ ] Büyüme ve iskonto oranları için duyarlılık tablosu ekleyin.
- [ ] Önemli bir işlemde bağımsız değerleme uzmanı ve hukuk danışmanıyla çalışın.

## Daha fazlası

- Koller, T.; Goedhart, M.; Wessels, D. (McKinsey & Company) (2020). *Valuation: Measuring and Managing the Value of Companies*.
- OpenStax (2026). *Principles of Finance*. https://openstax.org/books/principles-finance/pages/1-why-it-matters
- KGK (2026). *Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu (resmî site)*. https://www.kgk.gov.tr
