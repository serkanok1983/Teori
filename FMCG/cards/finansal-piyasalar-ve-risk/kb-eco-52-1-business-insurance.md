---
id: kb-eco-52-1-business-insurance
title: "İşletme sigortası: Eksik sigorta ve doğru teminat"
summary: "Depo, stok, araç filosu ve sorumluluk risklerinin sigortalanmasında sigorta bedelinin gerçek değere göre belirlenmesinin önemini, eksik sigortada tazminatın orantılı azalmasını ve poliçe seçiminde dikkat edilmesi gerekenleri anlatır."
course: eco
category: finansal-piyasalar-ve-risk
tags: [sigorta, risk-yonetimi, stok]
roles: [uretici-sahibi, bayi-sahibi, finans-muduru]
level: orta
source_lessons: [ECO-52.1]
reading_minutes: 3
key_points:
  - "Sigorta bedeli gerçek değerin altındaysa, kısmi hasarda da tazminat orantılı olarak azalabilir."
  - "Yüksek enflasyonda sigorta bedelleri dönem içinde güncellenmezse eksik sigorta kendiliğinden oluşur."
  - "Muafiyet, istisna ve teminat dışı hâller poliçenin en önemli bölümleridir."
  - "Sigorta, olasılığı düşük ama etkisi büyük riskler için uygundur."
glossary_terms: [eksik-sigorta, muafiyet, sigorta-bedeli]
related: [kb-eco-4-2-risk-aversion-insurance, kb-eco-32-3-risk-management-stress-test, kb-eco-34-1-inventory-valuation, kb-eco-12-1-adverse-selection-credit]
sources:
  - title: "6102 sayılı Türk Ticaret Kanunu"
    authors: "T.C. Resmî Gazete / Mevzuat Bilgi Sistemi"
    year: 2011
    type: law
    url: "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6102.pdf"
    verified: true
    checked_on: 2026-10-28
    note: "Mevzuat Bilgi Sistemi resmî PDF metni açıldı, kanun adı ve numarası eşleşti (2026-10-28)."
  - title: "Türkiye Sigorta Birliği (resmî site)"
    authors: "TSB"
    year: 2026
    type: web
    url: "https://www.tsb.org.tr"
    verified: true
    checked_on: 2026-10-28
  - title: "On the Corporate Demand for Insurance"
    authors: "Mayers, D.; Smith, C. W., Jr."
    year: 1982
    type: article
    doi: "10.1086/296165"
    url: "https://doi.org/10.1086/296165"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Business 55(2)."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Bir distribütörün en büyük varlıkları genellikle depo, stok ve araç filosudur. Yangın, su baskını veya hırsızlık bu varlıkları bir gecede yok edebilir. Bu kart, poliçenizin gerçekten korunduğunuzu düşündüğünüz tutarı ödeyip ödemeyeceğini değerlendirmenizi sağlar.

## Temel fikir

**Sigorta değeri ve sigorta bedeli:** Sigorta değeri, sigortalanan varlığın gerçek değeridir. Sigorta bedeli ise poliçede yazan tutardır.

**Eksik sigorta:** Sigorta bedeli sigorta değerinin altındaysa, Türk Ticaret Kanunu'nun sigorta hükümleri uyarınca sigortacı, aksi kararlaştırılmadıkça zararı bedelin değere oranında öder. Yani kısmi bir hasarda bile tazminat azalır.

**Muafiyet:** Hasarın sigortalıda kalan kısmı. Primi düşürür ama küçük hasarları size bırakır. Sık yaşanan küçük hasarları kendiniz karşılayıp büyük hasarları sigortaya bırakmak çoğu zaman daha ekonomiktir.

**İstisnalar:** Poliçenin karşılamadığı durumlar. Örneğin bazı doğal afet ve terör riskleri ek teminat alınmadıkça kapsam dışı olabilir.

**Distribütör için temel teminatlar:**

- Bina, makine ve stok için yangın ve genişletilmiş teminatlar
- Kâr kaybı (iş durması): Hasar sonrası satış yapılamayan dönemdeki brüt kâr ve sabit giderler
- Emtia nakliyat: Yoldaki malın hasarı
- Üçüncü kişi ve işveren sorumluluğu
- Araç filosu için zorunlu trafik sigortası ve kasko

**Neden sigorta?** Mayers ve Smith (1982), şirketlerin sigortayı yalnızca risk sevmedikleri için değil, iflas maliyetlerini, finansman maliyetini ve vergi etkilerini azaltmak için de aldıklarını açıklar.

## Bir örnek

> **Örnek (temsili rakamlar):** Değerler, prim oranı ve hasar tutarı varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b7.py` ile yapılmıştır.

Bir distribütörün deposundaki stokun gerçek değeri 20.000.000 TL, ancak poliçedeki sigorta bedeli geçen yılın değeri olan 12.000.000 TL (gerçek değerin %60'ı).

Yangında 5.000.000 TL'lik stok zarar görüyor.

- Beklenen tazminat: 5.000.000 TL
- Eksik sigorta nedeniyle ödenen: 5.000.000 × %60 = **3.000.000 TL**
- Şirkette kalan zarar: **2.000.000 TL**

Örnek prim oranı binde 1,5 ile tam bedelli poliçenin primi 30.000 TL, mevcut poliçeninki 18.000 TL. Yıllık 12.000 TL'lik tasarruf, 2.000.000 TL'lik zarara yol açtı.

## Sık yapılan hatalar

- Sigorta bedelini yıllık yenilemede güncellemeden aynen devam ettirmek.
- Stok miktarının yıl içinde dalgalandığını hesaba katmamak.
- Muafiyet ve istisnaları okumadan poliçeyi imzalamak.
- Kâr kaybı ve üçüncü kişi sorumluluk teminatlarını atlamak.
- Hasar sonrası ihbar ve belge sürelerini bilmemek.
- Yangın söndürme, alarm ve kamera gibi önlemleri poliçedeki beyanla uyumlu tutmamak.
- Kiracı olunan depoda binanın sigortasını mal sahibine bırakıp kiracı sorumluluğunu sigortalamamak.

## Pratikte nasıl uygulanır?

- [ ] Sigorta bedellerini en az yılda bir, yüksek enflasyonda daha sık güncelleyin.
- [ ] Stok için dönemsel değer bildirimli veya en yüksek değere göre bir teminat yapısı isteyin.
- [ ] Poliçedeki muafiyet, istisna ve ek teminatları bir tabloda özetleyin.
- [ ] Kâr kaybı ve sorumluluk teminatlarını değerlendirin.
- [ ] Hasar anında izlenecek adımları yazılı bir prosedüre dönüştürün ve sigorta aracınızla gözden geçirin.
- [ ] Poliçe yenilemeden en az bir ay önce stok, makine ve bina değerlerini güncel rakamlarla sigortacınıza bildirin.

## Daha fazlası

- T.C. Resmî Gazete / Mevzuat Bilgi Sistemi (2011). *6102 sayılı Türk Ticaret Kanunu*. https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6102.pdf
- TSB (2026). *Türkiye Sigorta Birliği (resmî site)*. https://www.tsb.org.tr
- Mayers, D.; Smith, C. W., Jr. (1982). *On the Corporate Demand for Insurance*. https://doi.org/10.1086/296165
