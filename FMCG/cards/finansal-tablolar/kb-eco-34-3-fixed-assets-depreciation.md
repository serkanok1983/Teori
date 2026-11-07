---
id: kb-eco-34-3-fixed-assets-depreciation
title: "Maddi duran varlıklar ve amortisman: Araç ve depo yatırımlarını doğru okumak"
summary: "Maddi duran varlıkların maliyetle kaydedilip faydalı ömrü boyunca amortismana tabi tutulmasını, normal ve azalan bakiyeler yöntemlerini, amortismanın nakit çıkışı olmadığını ve enflasyonda tarihi maliyetle ayrılan amortismanın yenileme ihtiyacını neden karşılamadığını anlatır."
course: eco
category: finansal-tablolar
tags: [muhasebe, yatirim, duran-varliklar]
roles: [finans-muduru]
level: orta
source_lessons: [ECO-34.3]
reading_minutes: 3
key_points:
  - "Amortisman, varlığın maliyetini kullanıldığı yıllara dağıtır; nakit çıkışı değildir."
  - "Azalan bakiyeler yöntemi ilk yıllarda daha fazla gider yazar; toplam amortisman değişmez."
  - "Yüksek enflasyonda tarihi maliyetle hesaplanan amortisman, varlığı yenilemek için gereken tutarın çok altında kalır."
  - "Vergi açısından faydalı ömür ve yöntemler mevzuatla belirlenir; mali müşavirinizle teyit edin."
glossary_terms: [amortisman, faydali-omur, yerine-koyma-maliyeti]
related: [kb-eco-33-4-income-statement, kb-eco-35-2-inflation-accounting, kb-eco-34-5-leases-ifrs16, kb-eco-32-4-finance-in-high-inflation]
sources:
  - title: "IAS 16 Property, Plant and Equipment"
    authors: "IFRS Foundation"
    year: 2026
    type: standard
    url: "https://www.ifrs.org/issued-standards/list-of-standards/ias-16-property-plant-and-equipment/"
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
  - title: "Principles of Accounting, Volume 1: Financial Accounting"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters"
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

Kamyonlar, forkliftler, raf sistemleri ve depo binası, bir distribütörün işini yapması için gereken varlıklardır. Bu kart, bu varlıkların muhasebeye nasıl yansıdığını ve özellikle yenileme bütçesinin neden amortismandan bağımsız planlanması gerektiğini anlatır.

## Temel fikir

**Kayıt:** Maddi duran varlıklar (TMS 16) alış maliyeti ve kullanıma hazır hâle getirme masraflarıyla kaydedilir. Maliyet, faydalı ömür boyunca amortisman yoluyla gidere dönüşür.

**Yöntemler:**

- **Normal (doğrusal) amortisman:** Maliyet / faydalı ömür; her yıl aynı tutar.
- **Azalan bakiyeler:** Kalan net değere sabit bir oran uygulanır; ilk yıllarda gider daha yüksektir.

Vergi açısından faydalı ömürler Gelir İdaresi'nin yayımladığı listelerle belirlenir ve yöntem seçimi mevzuattaki koşullara bağlıdır. Finansal raporlamada ise ömür, varlığın beklenen kullanımına göre tahmin edilir.

**Amortisman nakit değildir:** Gelir tablosunda gider olarak görünür, ama nakit çıkışı varlık satın alındığında gerçekleşmiştir. Bu yüzden nakit akış tablosunda net kâra geri eklenir.

**Enflasyon etkisi:** Amortisman tarihi maliyetle hesaplanır. Fiyatlar hızla arttığında, ömrü dolan varlığın yerine yenisini almak için gereken tutar, ayrılan toplam amortismanın çok üzerindedir.

### Duran varlık yönetimi

- **Demirbaş listesi:** Her varlığın etiket numarası, yeri, alış tarihi, maliyeti ve birikmiş amortismanı kayıtlı olmalıdır. Dönemsel sayımla kayıttaki varlıkların fiilen var olduğunu doğrulayın.
- **Gider mi, varlık mı?** Bir harcamanın varlığın ömrünü veya kapasitesini artırıp artırmadığına göre aktifleştirilip aktifleştirilmeyeceği belirlenir. Olağan bakım ve onarım gider yazılır. Vergi mevzuatında doğrudan gider yazılabilecek düşük tutarlı demirbaşlar için bir sınır da bulunur ve bu sınır dönemsel olarak güncellenir.
- **Satış ve hurdaya ayırma:** Satılan varlığın satış bedeli ile net defter değeri arasındaki fark kâr veya zarar olarak kaydedilir. Hurdaya ayrılan varlıklar kayıtlardan çıkarılmalıdır.

### Yatırım kararlarıyla bağlantı

Amortisman bir muhasebe dağıtımıdır; yatırım kararı ise nakit akışlarına göre verilir. Ancak amortismanın vergi matrahını düşürmesi bir nakit avantajı yaratır ve yatırım analizine dahil edilmelidir.

Araç filosu gibi varlıklarda yenileme zamanını belirlerken yalnızca amortismanın bitmesine değil, artan bakım ve yakıt maliyetlerine ve ikinci el değerine bakın.

## Bir örnek

> **Örnek (temsili rakamlar):** Tutarlar, ömür ve enflasyon oranı varsayımsaldır; vergi açısından geçerli ömür ve oranlar değildir. Hesaplar `scripts/cards_numbers_eco_b4.py` ile yapılmıştır.

Bir distribütör 3.000.000 TL'ye bir dağıtım kamyonu alıyor. Faydalı ömür 5 yıl.

- **Normal yöntem:** Her yıl 600.000 TL amortisman.
- **Azalan bakiyeler (oran %40):** 1. yıl 1.200.000 TL, 2. yıl 720.000 TL, 3. yıl 432.000 TL.

Yıllık enflasyon %30 olursa, beş yıl sonra aynı kamyonun fiyatı yaklaşık 11.138.790 TL olur. Toplam amortisman yalnızca 3.000.000 TL; aradaki 8.138.790 TL'lik fark, kârdan ayrılmamışsa yeni borçla finanse edilmek zorunda kalır.

## Sık yapılan hatalar

- Amortismanı nakit çıkışı sanmak ya da tam tersine, yenileme ihtiyacını unutmak.
- Muhasebe kârının tamamını dağıtıp araç filosunu yenileyecek kaynak bırakmamak.
- Bakım ve onarım harcamalarıyla varlık değerini artıran harcamaları ayırt etmemek.
- Kullanılmayan ya da satılan varlıkları kayıtlardan çıkarmamak.
- Araç alım-kiralama kararını yalnızca muhasebe giderine bakarak vermek.

## Pratikte nasıl uygulanır?

- [ ] Duran varlık listenizi (araç, ekipman, bina) yıllık sayımla kayıtlarla eşleştirin.
- [ ] Varlık yenileme planı hazırlayın ve bütçeyi yerine koyma maliyetiyle hesaplayın.
- [ ] Kâr dağıtımı kararlarında yenileme ihtiyacını dikkate alın.
- [ ] Faydalı ömür ve amortisman yöntemlerini mali müşavirinizle teyit edin.
- [ ] Alım ve kiralama seçeneklerini toplam sahip olma maliyetiyle karşılaştırın.

## Daha fazlası

- IFRS Foundation (2026). *IAS 16 Property, Plant and Equipment*. https://www.ifrs.org/issued-standards/list-of-standards/ias-16-property-plant-and-equipment/
- T.C. Resmî Gazete / Mevzuat Bilgi Sistemi (1961). *213 sayılı Vergi Usul Kanunu*. https://www.mevzuat.gov.tr/MevzuatMetin/1.4.213.pdf
- OpenStax (2026). *Principles of Accounting, Volume 1: Financial Accounting*. https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters
