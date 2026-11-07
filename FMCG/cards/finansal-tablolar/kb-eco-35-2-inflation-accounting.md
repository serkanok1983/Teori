---
id: kb-eco-35-2-inflation-accounting
title: "Enflasyon muhasebesi: Tarihi rakamlar neden yanıltır ve düzeltme ne anlatır?"
summary: "Yüksek enflasyonda tarihi maliyetle tutulan tabloların neden yanıltıcı olduğunu, parasal olmayan kalemlerin endeksle düzeltilmesini, nakit ve alacak tutmanın yarattığı parasal kaybı ve düzeltilmiş tabloların yönetim kararları için ne anlama geldiğini anlatır."
course: eco
category: finansal-tablolar
tags: [muhasebe, enflasyon, raporlama]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [ECO-35.2, ECO-35.3, ECO-35.4]
reading_minutes: 3
key_points:
  - "Yüksek enflasyonda farklı tarihlerin lirası farklı satın alma gücüne sahiptir; tarihi maliyet tabloları bunları toplar."
  - "Enflasyon düzeltmesinde parasal olmayan kalemler (stok, duran varlık, özkaynak) endeksle güncellenir."
  - "Net parasal varlık (nakit, alacak) tutmak satın alma gücü kaybı, net parasal borç tutmak kazanç yaratır."
  - "Düzeltilmiş tablolar, kâr dağıtımı ve fiyatlama kararlarında daha gerçekçi bir taban sunar."
glossary_terms: [enflasyon-duzeltmesi, parasal-kalem, net-parasal-pozisyon]
related: [kb-eco-32-4-finance-in-high-inflation, kb-eco-14-2-inflation-measurement-tufe-ufe, kb-eco-35-1-reporting-regimes-tr, kb-eco-34-3-fixed-assets-depreciation]
sources:
  - title: "IAS 29 Financial Reporting in Hyperinflationary Economies"
    authors: "IFRS Foundation"
    year: 2026
    type: standard
    url: "https://www.ifrs.org/issued-standards/list-of-standards/ias-29-financial-reporting-in-hyperinflationary-economies/"
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
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28

---

## Ne işe yarar?

Fiyatların yılda yüzde onlarca arttığı bir ortamda, beş yıl önce alınmış bir depo binası ile geçen ay alınmış bir stok aynı bilançoda tarihi tutarlarıyla yan yana durur. Bu kart, enflasyon düzeltmesinin mantığını ve düzeltilmiş rakamların size ne söylediğini anlatır.

## Temel fikir

**Sorun:** Tarihi maliyet tabloları farklı tarihlerin lirasını toplar. Sonuçta duran varlıklar ve özkaynak düşük, kâr ise yüksek görünür.

**Düzeltme (TMS 29 ve benzeri uygulamalar):**

- **Parasal kalemler** (nakit, alacak, borç) zaten bugünün lirasıyla ifade edilir; düzeltilmez.
- **Parasal olmayan kalemler** (stok, duran varlık, özkaynak) edinildikleri tarihten raporlama tarihine kadar genel fiyat endeksiyle güncellenir.
- **Parasal kazanç/kayıp:** Net parasal varlık tutan şirket, enflasyon nedeniyle satın alma gücü kaybeder; net parasal borç tutan şirket kazanç elde eder. Bu fark gelir tablosunda ayrıca gösterilir.

Türkiye'de enflasyon düzeltmesi hem finansal raporlama hem vergi kayıtları açısından gündeme gelmiştir; uygulamanın kapsamı ve zamanlaması düzenlemelerle belirlenir.

Enflasyon düzeltmesinin vergi ve finansal raporlama açısından uygulanıp uygulanmayacağı, hangi dönemlerde ve hangi endeksle yapılacağı mevzuat ve KGK kararlarıyla belirlenir ve değişebilir. Bu kart genel mantığı anlatır; şirketinizin güncel yükümlülüğünü mali müşavirinizle teyit edin.

## Bir örnek

> **Örnek (temsili rakamlar):** Endeks değerleri, tutarlar ve enflasyon oranı varsayımsaldır; resmî endeks verisi değildir. Hesaplar `scripts/cards_numbers_eco_b5.py` ile yapılmıştır.

**Duran varlık:** Bir distribütör, fiyat endeksi 100 iken 2.000.000 TL'ye bir forklift filosu almış. Bugün endeks 180. Düzeltme katsayısı 1,80; filonun düzeltilmiş maliyeti 3.600.000 TL. Amortisman da bu tutar üzerinden hesaplanır.

**Parasal kayıp:** Şirket yıl boyunca 5.000.000 TL'lik net parasal varlık (nakit ve alacak fazlası) tutmuş. Yıllık enflasyon %50. Aynı satın alma gücünü korumak için bu tutarın yıl sonunda 7.500.000 TL olması gerekirdi, ama nominal olarak aynı kalmış; satın alma gücü kaybı yıl sonu fiyatlarıyla 2.500.000 TL.

Yorum: Uzun vadeli alacak taşımak yalnızca finansman maliyeti değil, doğrudan satın alma gücü kaybıdır.

## Sık yapılan hatalar

- Düzeltilmiş tablolardaki parasal kaybı muhasebe tekniği sanıp göz ardı etmek.
- Tarihi maliyetli kâr üzerinden kâr dağıtıp işletmenin reel sermayesini küçültmek.
- Yönetim raporlarında yalnızca nominal büyümeye bakmak.
- Düzeltmenin vergi etkisini önceden hesaplamamak.
- Düzeltilmiş ve düzeltilmemiş tabloları karşılaştırmak.
- Enflasyon düzeltmesinden doğan farkları kârın parçası sanıp dağıtım kararı vermek.

## Pratikte nasıl uygulanır?

- [ ] Net parasal pozisyonunuzu (parasal varlıklar − parasal borçlar) aylık izleyin.
- [ ] Yönetim raporunda temel kalemleri endeksle düzeltilmiş olarak da gösterin.
- [ ] Kâr dağıtımı kararını düzeltilmiş kâra göre değerlendirin.
- [ ] Vade ve stok politikalarını parasal kayıp etkisini de hesaba katarak belirleyin.
- [ ] Yasal enflasyon düzeltmesi yükümlülüğünüzü ve vergi etkisini mali müşavirinizle teyit edin.
- [ ] Düzeltilmiş ve düzeltilmemiş tabloların farklarını yönetim kuruluna kısa bir notla açıklayın.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın.

## Daha fazlası

- IFRS Foundation (2026). *IAS 29 Financial Reporting in Hyperinflationary Economies*. https://www.ifrs.org/issued-standards/list-of-standards/ias-29-financial-reporting-in-hyperinflationary-economies/
- KGK (2026). *Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu (resmî site)*. https://www.kgk.gov.tr
- T.C. Resmî Gazete / Mevzuat Bilgi Sistemi (1961). *213 sayılı Vergi Usul Kanunu*. https://www.mevzuat.gov.tr/MevzuatMetin/1.4.213.pdf
