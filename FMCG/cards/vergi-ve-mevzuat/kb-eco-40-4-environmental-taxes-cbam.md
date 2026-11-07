---
id: kb-eco-40-4-environmental-taxes-cbam
title: "Çevre vergileri ve SKDM (CBAM): İhracatçıya karbon maliyeti"
summary: "Karbon fiyatlamasının mantığını, AB'nin Sınırda Karbon Düzenleme Mekanizması'nın (SKDM/CBAM) Türk ihracatçıya olası maliyetini, emisyon yoğunluğunun bu maliyeti nasıl belirlediğini ve hazırlık adımlarını anlatır."
course: eco
category: vergi-ve-mevzuat
tags: [vergi, cevre, ihracat, karbon]
roles: [uretici-sahibi, uretici-yonetici]
level: orta
source_lessons: [ECO-11.1, ECO-40.4]
reading_minutes: 3
key_points:
  - "Karbon fiyatlaması, emisyonun topluma maliyetini üreticiye yükleyerek davranışı değiştirmeyi amaçlar."
  - "SKDM, kapsamdaki ürünlerin AB'ye ithalatında gömülü emisyon için sertifika alınmasını öngörür."
  - "Maliyeti emisyon yoğunluğu, karbon fiyatı ve menşe ülkede ödenmiş karbon bedeli belirler."
  - "Doğrulanmış emisyon verisi olmayan ihracatçı, varsayılan değerlerle daha yüksek maliyete katlanabilir."
glossary_terms: [karbon-fiyatlamasi, skdm, emisyon-yogunlugu, dissallik]
related: [kb-eco-54-3-governance-sustainability-reporting, kb-eco-1-5-price-controls-tax-incidence, kb-eco-22-1-exchange-rates-real-nominal, kb-eco-43-1-turkish-tax-system-overview]
sources:
  - title: "Carbon Border Adjustment Mechanism"
    authors: "European Commission, Taxation and Customs Union"
    year: 2026
    type: web
    url: "https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en"
    verified: true
    checked_on: 2026-10-28
  - title: "İklim Değişikliği Başkanlığı (resmî site)"
    authors: "T.C. Çevre, Şehircilik ve İklim Değişikliği Bakanlığı"
    year: 2026
    type: web
    url: "https://www.iklim.gov.tr"
    verified: true
    checked_on: 2026-10-28
  - title: "The Economics of Welfare"
    authors: "Pigou, A. C."
    year: 1920
    type: book
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

AB, Türkiye'nin en büyük ihracat pazarıdır. Demir-çelik, alüminyum, çimento, gübre gibi sektörlerde AB'ye ihracat yapan üreticiler ile bu üreticilere girdi sağlayan veya onların ürünlerini dağıtan işletmeler, karbon maliyetiyle karşılaşmaya başlamıştır. Bu kart, maliyetin nasıl oluştuğunu ve neye hazırlanmanız gerektiğini anlatır.

## Temel fikir

**Dışsallık ve karbon fiyatı:** Bir üretim faaliyeti, başkalarına yansıyan ama fiyata dahil olmayan bir maliyet (kirlilik) yaratıyorsa buna dışsallık denir. Pigou'nun (1920) önerdiği yaklaşım, bu maliyeti vergi veya fiyat yoluyla üreticiye yüklemektir.

**SKDM (CBAM):** AB, kendi emisyon ticaret sistemindeki üreticiler ile ithal ürünler arasında eşitlik sağlamak için kapsamdaki ürünlerin ithalatında gömülü emisyon için sertifika alınmasını öngörür. Mekanizma geçiş döneminden sonra kademeli olarak uygulanır; kapsam, takvim ve ücretsiz tahsis indirimleri AB mevzuatında belirlenir ve değişebilir.

**Maliyeti belirleyenler:**

- Ton ürün başına gömülü emisyon (emisyon yoğunluğu)
- AB'deki karbon fiyatı
- Menşe ülkede fiilen ödenmiş karbon bedeli (mahsup edilebilir)

Türkiye'de de iklim mevzuatı ve emisyon ticaret sistemi düzenlemeleri gelişmektedir; bu düzenlemeler ileride mahsup açısından önem kazanabilir.

### Hazırlık için atılabilecek adımlar

- **Kapsamı kontrol edin:** SKDM ilk aşamada belirli sektörleri (ör. demir-çelik, alüminyum, çimento, gübre, elektrik ve hidrojen) kapsar. Ürünlerinizin gümrük tarife pozisyonlarının kapsamda olup olmadığını kontrol edin. Kapsam ileride genişleyebilir.
- **Emisyon verisi toplayın:** Üretim süreçlerinizdeki yakıt, elektrik ve hammadde tüketimini düzenli ve belgelenmiş biçimde kaydedin. AB'deki ithalatçınız gömülü emisyon verisini sizden isteyecektir.
- **Doğrulama:** Beyan edilen emisyon verilerinin doğrulanması gerekebilir. Doğrulama süreçlerini ve maliyetini önceden araştırın.
- **Müşterilerle konuşun:** AB'deki müşterileriniz SKDM maliyetini fiyat müzakerelerine yansıtacaktır. Düşük emisyonlu üretim, bir rekabet avantajına dönüşebilir.

### Azaltım seçenekleri

Enerji verimliliği, yenilenebilir elektrik tedariki, hammadde ve yakıt değişimi, emisyon yoğunluğunu düşürmenin temel yollarıdır. Azaltım yatırımlarını değerlendirirken, beklenen karbon fiyatını nakit akışlarına dahil edin.

### Belirsizlik

Uygulama takvimi, varsayılan değerler ve Türkiye'deki emisyon ticaret sisteminin AB sistemiyle ilişkisi değişebilir. Bu konudaki kararlar için güncel resmî kaynakları ve danışmanlarınızı takip edin.

## Bir örnek

> **Örnek (temsili rakamlar):** Hacim, emisyon yoğunluğu, karbon fiyatı ve ürün fiyatı varsayımsaldır; ücretsiz tahsis ve geçiş dönemi indirimleri dikkate alınmamıştır. Hesaplar `scripts/cards_numbers_eco_b7.py` ile yapılmıştır.

Bir çelik üreticisi AB'ye yılda 10.000 ton ürün ihraç ediyor. Ton başına gömülü emisyon 2,0 ton CO₂, sertifika fiyatı ton CO₂ başına 80 avro.

- Yıllık karbon maliyeti: 10.000 × 2,0 × 80 = **1.600.000 avro.**
- Ton başına 160 avro; ürün fiyatı ton başına 700 avro olduğuna göre fiyatın %22,9'i kadar.

Emisyon yoğunluğu 1,5 tona düşürülürse maliyet 1.200.000 avroya iner; yıllık tasarruf 400.000 avro. Enerji verimliliği ve yenilenebilir enerji yatırımları bu açıdan da değerlendirilmelidir.

## Sık yapılan hatalar

- SKDM'yi yalnızca ithalatçının sorunu sanmak; maliyet fiyat pazarlığıyla ihracatçıya yansır.
- Ürün bazında emisyon verisi toplamamak ve doğrulatmamak.
- Kapsam dışında sanılan ürünlerin, girdi zinciri üzerinden etkilenebileceğini göz ardı etmek.
- Karbon maliyetini yatırım değerlendirmesine katmamak.

## Pratikte nasıl uygulanır?

- [ ] AB'ye sattığınız ürünlerin SKDM kapsamında olup olmadığını gümrük tarife kodlarıyla kontrol edin.
- [ ] Tesis ve ürün bazında emisyon verisi toplayan bir sistem kurun.
- [ ] AB'li müşterilerinizle veri paylaşımı ve maliyet paylaşımı konularını sözleşmeye bağlayın.
- [ ] Emisyon azaltım yatırımlarını, karbon maliyetinden kaçınılan tutarla birlikte değerlendirin.
- [ ] Güncel takvim ve kuralları AB'nin ve Türkiye'deki ilgili kurumların resmî kaynaklarından izleyin.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın.

## Daha fazlası

- European Commission, Taxation and Customs Union (2026). *Carbon Border Adjustment Mechanism*. https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en
- T.C. Çevre, Şehircilik ve İklim Değişikliği Bakanlığı (2026). *İklim Değişikliği Başkanlığı (resmî site)*. https://www.iklim.gov.tr
- Pigou, A. C. (1920). *The Economics of Welfare*.
