---
id: kb-eco-43-2-income-tax-withholding
title: "Stopaj (tevkifat): Başkası adına vergi kesmek"
summary: "İşletmelerin ücret, serbest meslek ve kira gibi ödemelerde vergiyi kaynağında kesip beyan etme yükümlülüğünü, net ve brüt tutar farkını ve sözleşmelerde dikkat edilmesi gerekenleri anlatır."
course: eco
category: vergi-ve-mevzuat
tags: [vergi, stopaj, gelir-vergisi]
roles: [uretici-sahibi, bayi-sahibi, finans-muduru]
level: orta
source_lessons: [ECO-43.2]
reading_minutes: 3
key_points:
  - "Stopajda vergiyi ödeme yapan işletme keser, beyan eder ve öder."
  - "Sözleşmede tutarın net mi brüt mü olduğu açıkça yazılmalıdır."
  - "Net tutar üzerinden anlaşılan ödemelerde maliyet, brüte tamamlanan tutardır."
  - "Kesilmeyen stopajın sorumluluğu ödemeyi yapan işletmeye aittir."
glossary_terms: [stopaj, brut-ucret, net-ucret]
related: [kb-eco-43-1-turkish-tax-system-overview, kb-eco-42-1-tax-basics-average-marginal, kb-eco-44-3-sgk-employer-costs, kb-eco-43-6-tax-procedure-inspection]
sources:
  - title: "193 sayılı Gelir Vergisi Kanunu"
    authors: "T.C. Resmî Gazete / Mevzuat Bilgi Sistemi"
    year: 1960
    type: law
    url: "https://www.mevzuat.gov.tr/MevzuatMetin/1.4.193.pdf"
    verified: true
    checked_on: 2026-10-28
    note: "Mevzuat Bilgi Sistemi resmî PDF metni açıldı, kanun adı ve numarası eşleşti (2026-10-28)."
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

İşletmeniz çalışanlarına ücret, avukatına serbest meslek ücreti, bir kişiye depo kirası ödediğinde, bazı durumlarda karşı tarafın vergisini siz kesip devlete ödemekle yükümlüsünüz. Bu kart, stopajın mantığını ve net-brüt farkının maliyetinizi nasıl etkilediğini anlatır.

## Temel fikir

**Stopaj (vergi tevkifatı):** Gelir Vergisi Kanunu'nda sayılan bazı ödemelerde, ödemeyi yapan işletme vergiyi kaynağında keser ve muhtasar beyanname ile beyan edip öder.

Yaygın örnekler:

- Çalışan ücretleri
- Serbest meslek ödemeleri (avukat, danışman gibi)
- Gerçek kişilerden kiralanan iş yerleri için kira ödemeleri

**Brüt ve net:** Brüt tutar stopaj dahil tutardır. Net tutar karşı tarafın eline geçendir. Net üzerinden anlaşıldıysa, işletmenin maliyeti brüte tamamlanmış tutardır:

**Brüt = Net ÷ (1 − stopaj oranı)**

Hangi ödemenin stopaja tabi olduğu ve oranı, ödemenin türüne ve karşı tarafın durumuna göre değişir.

### Stopajın işletmeye etkileri

- **Nakit akışı:** Kesilen vergi, karşı tarafa ödeme yapıldığında kesilir ama vergi dairesine daha sonra ödenir. Bu kısa süreli bir nakit avantajıdır, ama bu tutarı harcamak ciddi bir risktir; zamanında ödenmezse gecikme faizi ve ceza doğar.
- **Maliyet:** Brüt üzerinden anlaşılan ödemede stopaj karşı tarafın yüküdür. Net üzerinden anlaşılan ödemede ise stopaj sizin maliyetinize eklenir. Sözleşmede tutarın brüt mü net mi olduğunu açıkça yazın.
- **Gider yazma:** Stopaj dahil brüt tutar gider olarak kaydedilir.

### Belge ve beyan

Serbest meslek ödemelerinde karşı taraf serbest meslek makbuzu düzenler; kira ödemelerinde ise ödemenin banka aracılığıyla yapılması ve kayıtların kira sözleşmesiyle uyumlu olması gerekir. Kesilen vergiler muhtasar ve prim hizmet beyannamesiyle bildirilir.

### Kim kesmeli?

Stopaj yükümlülüğü genellikle ödemeyi yapan tüzel kişilere ve defter tutan işletmelere aittir. Karşı tarafın şirket mi, gerçek kişi mi olduğu ve ödemenin türü, stopaj olup olmadığını belirler. Emin değilseniz ödemeyi yapmadan önce mali müşavirinize danışın; sonradan düzeltme her zaman daha maliyetlidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Tutarlar varsayımsaldır; stopaj oranı **örnek oran**dır. Hesaplar `scripts/cards_numbers_eco_b6.py` ile yapılmıştır.

Bir distribütör, gerçek kişi bir mal sahibinden depo kiralıyor. Mal sahibi "aylık 80.000 TL net isterim" diyor. Örnek stopaj oranı %20.

- Brüt kira: 80.000 ÷ (1 − 0,20) = **100.000 TL.**
- İşletmenin kesip beyan edeceği stopaj: 20.000 TL.
- Mal sahibine ödenen: 80.000 TL.

Bütçeye 80.000 TL yazılırsa kira maliyeti her ay 20.000 TL eksik planlanmış olur.

## Sık yapılan hatalar

- Sözleşmede kiranın net mi brüt mü olduğunu belirtmemek.
- Gerçek kişiye yapılan ödemelerde stopaj yükümlülüğünü atlamak.
- Stopajı kesip beyan etmeyi ve ödemeyi süresinde yapmamak.
- Yıl içinde değişen oranları sistemde güncellememek.

## Pratikte nasıl uygulanır?

- [ ] Gerçek kişilere ve serbest meslek erbabına yaptığınız ödemelerin listesini çıkarın.
- [ ] Her ödeme türü için stopaj yükümlülüğünü ve güncel oranı mali müşavirinizle belirleyin.
- [ ] Sözleşmelerde tutarın brüt mü net mi olduğunu açıkça yazın.
- [ ] Bütçeyi brüt tutar üzerinden yapın.
- [ ] Muhtasar beyan ve ödeme tarihlerini vergi takviminize ekleyin.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın.

## Daha fazlası

- T.C. Resmî Gazete / Mevzuat Bilgi Sistemi (1960). *193 sayılı Gelir Vergisi Kanunu*. https://www.mevzuat.gov.tr/MevzuatMetin/1.4.193.pdf
- T.C. Resmî Gazete / Mevzuat Bilgi Sistemi (1961). *213 sayılı Vergi Usul Kanunu*. https://www.mevzuat.gov.tr/MevzuatMetin/1.4.213.pdf
