---
id: kb-ea-27-2-tpm-promotion-settlement
title: "Ticari promosyon yönetimi (TPM): Planlama, tahakkuk ve mahsuplaşma"
summary: "Ticari promosyonların sistemde planlanmasını, bütçe ve tahakkuk mantığını, kampanya sonrası müşteri talepleri ile mahsuplaşmayı, promosyon optimizasyonunu ve gelir büyümesi yönetimi sistemleriyle ilişkisini anlatır."
course: ea
category: saha-satis-ve-dms
tags: [tpm, promosyon, tahakkuk, mahsuplasma, rgm]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: ileri
source_lessons: [EA-27.2]
reading_minutes: 2
key_points:
  - "TPM sistemi promosyon planını, bütçesini, uygulamasını ve sonucunu tek yerde izler."
  - "Promosyon maliyeti, satış gerçekleştikçe tahakkuk edilir; fatura beklenmez."
  - "Kampanya sonunda müşteri talebi ile tahakkuk karşılaştırılır ve fark çözülür."
  - "Promosyon optimizasyonu, geçmiş kampanyaların ek satışını ve kârlılığını ölçerek yeni planı önerir."
  - "Gerçekleşen veri olmadan promosyon getirisi ölçülemez."
glossary_terms: [tpm, promosyon-tahakkuku, mahsuplasma]
related: [kb-fmcg-5-4-promotion-economics, kb-fmcg-5-5-trade-spend-roi, kb-fmcg-5-7-rgm-system, kb-ea-27-1-pricing-engine-conditions, kb-ea-26-6-dms-secondary-sales]
sources:
  - title: "The Strategy and Tactics of Pricing"
    authors: "Nagle, T. T.; Müller, G."
    year: 2018
    type: book
    doi: "10.4324/9781315266220"
    verified: true
    checked_on: 2026-10-28
    note: "DOI Crossref kaydında başlık ve yazar eşleşti; baskı yılı karttakinden farklı olabilir."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28

---

## Ne işe yarar?

Hızlı tüketim üreticilerinde ticari harcamalar cironun önemli bir bölümünü oluşturur. Ama çoğu firmada bu harcamalar Excel'de planlanır, faturalar aylar sonra gelir ve hangi kampanyanın işe yaradığı bilinmez. Bu kart, **ticari promosyon yönetimi** (TPM) sistemlerinin bu süreci nasıl düzenlediğini anlatır.

## Temel fikir

TPM sisteminde bir promosyonun yaşam döngüsü:

1. **Planlama:** Müşteri, ürün, dönem, mekanik (ör. koli başı 15 TL iskonto), beklenen hacim ve bütçe.
2. **Onay:** Bütçe sahibinin onayı; müşteri bazlı ticari harcama bütçesinden düşülmesi.
3. **Uygulama:** İskontonun fiyat motoruna aktarılması (fatura üstü) veya sonradan ödenecek olarak kaydedilmesi (fatura dışı).
4. **Tahakkuk:** Satış gerçekleştikçe promosyon maliyetinin gider olarak tahakkuk edilmesi. Böylece dönem kârı gerçeği yansıtır.
5. **Mahsuplaşma:** Kampanya sonunda müşterinin talebi (fatura veya fiyat farkı talebi) tahakkukla karşılaştırılır; fark çözülür.
6. **Değerlendirme:** Ek satış, kârlılık ve yatırım getirisi.

**Promosyon optimizasyonu (TPO).** Geçmiş kampanyaların sonuçlarından hangi mekanik, derinlik ve dönemin daha iyi çalıştığını tahmin eder ve plan önerir.

**Gelir büyümesi yönetimi (RGM).** Fiyat, paket, karma ve promosyon kararlarını bir arada ele alır; TPM bunun promosyon ayağıdır.

### Promosyon döngüsünü kapatmak

TPM'nin asıl değeri, planlanan promosyonun gerçekleşen sonucuyla karşılaştırılabilmesidir. Bu döngünün kapanması için şu adımlar gerekir:

- **Plan kaydı:** Her promosyonun türü, süresi, kapsadığı ürünler ve müşteriler, beklenen hacim ve bütçesi sisteme kaydedilmelidir. Elle tutulan tablolarda bu bilgiler genellikle dağınık kalır.
- **Taban satış tahmini:** Promosyonun etkisini ölçmek için, promosyon olmasaydı satılacak miktarın tahmin edilmesi gerekir. Bu taban olmadan, promosyon dönemindeki tüm satış promosyona atfedilir.
- **Tahakkuk:** Promosyon maliyeti, satışlar gerçekleştikçe muhasebede tahakkuk ettirilmelidir. Böylece dönem sonunda büyük ve beklenmedik bir gider ortaya çıkmaz.
- **Mahsuplaşma:** Müşteriden gelen promosyon talepleri, plan ve gerçekleşen satışla eşleştirilerek kontrol edilmelidir. Belgesiz veya plana uymayan talepler ayrı bir onay akışından geçmelidir.
- **Değerlendirme:** Promosyon sonrası ek hacim, maliyet ve kârlılık hesaplanarak bir sonraki planlamaya girdi olarak kullanılmalıdır.

**Öne çekme ve kanibalizasyon.** Bir promosyon, müşterinin gelecekteki alımlarını öne çekebilir veya aynı şirketin başka ürünlerinin satışını azaltabilir. Promosyon sonrası dönemdeki satış düşüşü ve ilişkili ürünlerdeki değişim de değerlendirmeye dahil edilmelidir.

**Satış ve finans iş birliği.** Promosyon bütçesinin sahibi, onay yetkileri ve mahsuplaşma kuralları satış ve finans ekiplerince birlikte belirlenmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b6.py` ile yapılmıştır.

Bir üretici, bir zincire 2.000 koli için koli başı 15 TL promosyon planlıyor ve **30.000,00 TL** tahakkuk ediyor. Kampanya sonunda zincirin talebi 1.700 koli üzerinden **25.500,00 TL**. Kalan **4.500,00 TL** tahakkuktan çözülüyor ve dönem kârına geri yazılıyor. Promosyonun ek satış etkisi ise zincirin satış verisi geldikten sonra değerlendiriliyor.

## Sık yapılan hatalar

- Promosyon maliyetini müşteri faturası gelince gider yazmak.
- Tahakkukları kampanya bitince kapatmayı unutmak.
- Talepleri kampanya planıyla karşılaştırmadan ödemek.
- Promosyon başarısını yalnızca kampanya dönemi satışıyla ölçmek.

## Pratikte nasıl uygulanır?

- [ ] Her promosyonu planlanan hacim ve bütçeyle sistemde kaydedin.
- [ ] Satış gerçekleştikçe otomatik tahakkuk kurun.
- [ ] Açık tahakkukları ay sonu kapanış listesine ekleyin.
- [ ] Büyük kampanyalar için kampanya sonrası değerlendirme yapın.

## Daha fazlası

- Nagle ve Müller, *The Strategy and Tactics of Pricing*.
