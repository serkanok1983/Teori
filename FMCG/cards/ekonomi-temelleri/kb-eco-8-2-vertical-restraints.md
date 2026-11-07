---
id: kb-eco-8-2-vertical-restraints
title: "Üretici–bayi ilişkisinde dikey kısıtlar: fiyat, münhasırlık ve bölge"
summary: "Üreticinin bayiye koyduğu yeniden satış fiyatı, münhasırlık ve bölge kısıtlarının ekonomik mantığını, çift marjinalleşme sorununu ve Türk rekabet hukukunda genel olarak nelerin riskli olduğunu anlatır."
course: eco
category: ekonomi-temelleri
tags: [kanal, rekabet, uyum, bayi-yonetimi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru]
level: orta
source_lessons: [ECO-8.2]
reading_minutes: 3
key_points:
  - "Üretici ve bayi ayrı ayrı marj koyduğunda fiyat yükselir, hacim düşer ve kanalın toplam kârı azalır (çift marjinalleşme)."
  - "Dikey kısıtlar bu sorunu ve bayinin hizmet yatırımından kaçınmasını çözmek için kullanılır."
  - "Bayinin satış fiyatını sabitlemek veya en düşük fiyatını belirlemek rekabet hukukunda genel olarak yasaktır; tavsiye ve azami fiyat genel olarak mümkündür."
  - "Münhasırlık ve bölge kısıtlarının süre ve pazar payı sınırları vardır; sözleşmeleri hukukçuya kontrol ettirin."
glossary_terms: [cift-marjinallesme, dikey-kisit, yeniden-satis-fiyati]
related: [kb-eco-7-7-oligopoly-collusion, kb-fmcg-1-1-margin-stack, kb-fmcg-1-4-channel-power-conflict, kb-fmcg-7-5-distributor-development]
sources:
  - title: "Vertical Integration and Antitrust Policy"
    authors: "Spengler, J. J."
    year: 1950
    type: article
    doi: "10.1086/256964"
    url: "https://doi.org/10.1086/256964"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Political Economy 58(4). Çift marjinalleşme."
  - title: "Grup Muafiyeti Tebliğleri"
    authors: "Rekabet Kurumu"
    year: 2026
    type: web
    url: "https://www.rekabet.gov.tr/tr/Sayfa/Mevzuat/grup-muafiyeti-tebligleri"
    verified: true
    checked_on: 2026-10-28
    note: "Dikey anlaşmalara ilişkin grup muafiyeti düzenlemeleri bu sayfada listelenir."
  - title: "Rekabet Kurumu (resmî site)"
    authors: "Rekabet Kurumu"
    year: 2026
    type: web
    url: "https://www.rekabet.gov.tr"
    verified: true
    checked_on: 2026-10-28
  - title: "4054 sayılı Rekabetin Korunması Hakkında Kanun"
    authors: "T.C. Resmî Gazete / Mevzuat Bilgi Sistemi"
    year: 1994
    type: law
    url: "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4054.pdf"
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

Üretici olarak bayinizin raf fiyatını, hangi markaları satacağını ve hangi bölgede çalışacağını belirlemek isteyebilirsiniz. Bayi olarak ise bu kısıtların size ne getirip ne götürdüğünü bilmek istersiniz. Bu kart, dikey kısıtların ekonomik gerekçesini ve hukuki risklerin genel çerçevesini verir; somut sözleşme için hukuk görüşü gerekir.

## Temel fikir

**Dikey kısıt** (*vertical restraint*), tedarik zincirinin farklı basamaklarındaki firmalar (üretici–distribütör–perakendeci) arasındaki sözleşmede bir tarafın diğerinin ticari serbestliğini sınırlamasıdır. Başlıca türleri:

- **Yeniden satış fiyatının belirlenmesi** (*resale price maintenance*): Bayinin satış fiyatını sabitlemek, en düşük fiyatını belirlemek ya da yalnızca tavsiye etmek veya üst sınır koymak.
- **Münhasırlık:** Bayinin rakip marka satmaması ya da üreticinin bölgede başka bayi atamaması.
- **Bölge ve müşteri kısıtı:** Bayinin yalnızca belirli bölgede veya kanalda satış yapması.

**Ekonomik gerekçe:** Spengler (1950), birbirinden bağımsız iki tekelin ardışık marj koymasının (**çift marjinalleşme**, *double marginalisation*) fiyatı yükselttiğini ve toplam kârı düşürdüğünü gösterdi. Ayrıca bir bayinin yaptığı hizmet yatırımından (raf düzeni, tanıtım) diğer bayiler bedavaya yararlanıyorsa, kimse yatırım yapmak istemez. Dikey kısıtlar bu sorunları hafifletebilir.

**Hukuki çerçeve (genel):** 4054 sayılı Kanun ve Rekabet Kurumu'nun dikey anlaşmalara ilişkin düzenlemelerine göre, bayinin satış fiyatını sabitlemek veya asgari fiyat belirlemek genel olarak yasaktır; azami fiyat ve tavsiye fiyat, baskı veya teşvikle zorunlu hâle getirilmedikçe genel olarak mümkündür. Münhasırlık ve rekabet yasağı ise pazar payı eşikleri ve süre sınırlarıyla grup muafiyetinden yararlanabilir. Eşikler ve süreler değişebilir; güncel metni Rekabet Kurumu kaynaklarından kontrol edin.

## Bir örnek

> **Örnek (temsili rakamlar):** Talep fiyatı = 200 − miktar, üretim maliyeti 40 TL varsayılmıştır; hesaplar `scripts/cards_numbers_eco_b1.py` ile yapılmıştır.

- **Entegre kanal** (üretici ve bayi tek firmaymış gibi): miktar 80, fiyat 120 TL, toplam kâr **6.400 TL**.
- **Ayrı firmalar, her biri kendi marjını koyuyor:** Üretici bayiye 120 TL'den satar; bayi rafa 160 TL fiyat koyar ve 40 birim satar. Üretici 3.200 TL, bayi 1.600 TL kazanır; toplam **4.800 TL**.
- Kanal toplamda **1.600 TL** kaybeder; tüketici de daha yüksek fiyat öder.

Yasal çözüm yolları: kademeli fiyat (hacim arttıkça düşen bayi fiyatı), sabit ücret artı düşük birim fiyat, azami raf fiyatı tavsiyesi ya da ortak iş planı ile hacim hedefi.

## Sık yapılan hatalar

- Bayiye "bu fiyatın altına satarsan malı keseriz" demek; e-posta ve mesajlar delil olur.
- Tavsiye fiyatı, iskonto kesme veya teslimat geciktirme gibi baskılarla fiilen zorunlu hâle getirmek.
- Münhasırlık sözleşmelerini süresiz yapmak ya da otomatik uzatmaya bağlamak.
- Bayinin kendi bölgesi dışındaki talep edilmemiş (pasif) satışlarını engellemek.
- Ekonomik gerekçeyi (çift marjinalleşme, bedavacılık) belgelemeden kısıt koymak.

## Pratikte nasıl uygulanır?

- [ ] Bayi sözleşmelerinizdeki fiyat, münhasırlık ve bölge maddelerini listeleyin ve rekabet hukuku uzmanına kontrol ettirin.
- [ ] Tavsiye fiyatları yazılı olarak "tavsiye" diye belirtin; uymayan bayiye yaptırım uygulamayın.
- [ ] Çift marjinalleşmeyi azaltmak için hacme bağlı kademeli fiyat veya ortak iş planı gibi yasal araçları değerlendirin.
- [ ] Satış ekibinin bayilerle fiyat yazışmalarına ilişkin kısa bir yazılı kural hazırlayın.
- [ ] Pazar payınızı yıllık izleyin; muafiyet eşiklerine yaklaşıyorsanız sözleşmeleri gözden geçirin.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın.

## Daha fazlası

- Spengler, J. J. (1950). *Vertical Integration and Antitrust Policy*. https://doi.org/10.1086/256964
- Rekabet Kurumu (2026). *Grup Muafiyeti Tebliğleri*. https://www.rekabet.gov.tr/tr/Sayfa/Mevzuat/grup-muafiyeti-tebligleri
- Rekabet Kurumu (2026). *Rekabet Kurumu (resmî site)*. https://www.rekabet.gov.tr
- T.C. Resmî Gazete / Mevzuat Bilgi Sistemi (1994). *4054 sayılı Rekabetin Korunması Hakkında Kanun*. https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4054.pdf
