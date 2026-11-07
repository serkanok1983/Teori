---
id: kb-ea-29-3-drp-inventory-planning
title: "Dağıtım ihtiyaç planlaması (DRP) ve stok planlama parametreleri"
summary: "Çok depolu dağıtım ağlarında dağıtım ihtiyaç planlamasının (DRP) mantığını; güvenlik stoku, sipariş miktarı ve tedarik süresi gibi parametrelerin sistemde nasıl tanımlandığını ve planın haftalık nasıl okunacağını anlatır."
course: ea
category: tedarik-ve-depo-sistemleri
tags: [drp, stok-planlama, emniyet-stogu, ikmal]
roles: [depo-lojistik-muduru]
level: ileri
source_lessons: [EA-29.3]
reading_minutes: 2
key_points:
  - "DRP, her depo için tahmini talep, eldeki stok ve planlı girişlerden gelecekteki ikmal ihtiyacını hesaplar."
  - "Güvenlik stoku, talep ve tedarik belirsizliğine karşı tutulan ek stoktur."
  - "Sipariş miktarı ve tedarik süresi gibi parametreler planın kalitesini doğrudan belirler."
  - "Planlanan stok güvenlik stokunun altına düşeceği dönem için ikmal önerilir."
  - "Parametreler düzenli gözden geçirilmezse sistem yanlış öneri üretir."
glossary_terms: [drp, guvenlik-stoku, tedarik-suresi]
related: [kb-ea-29-2-demand-planning-systems, kb-ea-28-1-order-management, kb-ea-20-5-inventory-in-erp, kb-ea-30-1-warehouse-operations-kpis]
sources:
  - title: "Inventory and Production Management in Supply Chains"
    authors: "Silver, E. A.; Pyke, D. F.; Thomas, D. J."
    year: 2017
    type: book
    doi: "10.1201/9781315374406"
    verified: true
    checked_on: 2026-10-28
    note: "DOI Crossref kaydında başlık ve yazar eşleşti; baskı yılı karttakinden farklı olabilir."
  - title: "Orlicky's Material Requirements Planning"
    authors: "Ptak, C.; Smith, C."
    year: 2011
    type: book
    verified: false
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Merkez depo ve bölge depoları olan bir dağıtım ağında "hangi depoya, ne zaman, ne kadar mal gönderelim?" sorusu her hafta sorulur. **Dağıtım ihtiyaç planlaması** (DRP), bu soruyu sistematik olarak yanıtlar.

## Temel fikir

DRP, üretimdeki malzeme ihtiyaç planlamasının (MRP) dağıtıma uyarlanmış halidir. Her depo ve ürün için zaman dilimleri (genellikle hafta) boyunca şu tablo hesaplanır:

- **Brüt ihtiyaç:** Tahmini talep (ve kesin siparişler)
- **Planlı girişler:** Yoldaki veya onaylanmış sevkiyatlar
- **Öngörülen stok:** Önceki stok + girişler − ihtiyaç
- **Planlanan ikmal:** Öngörülen stok güvenlik stokunun altına düşecekse önerilen sevkiyat

Bölge depolarının ikmal ihtiyaçları toplanarak merkez deponun ihtiyacına dönüşür.

**Ana parametreler:**

- **Güvenlik stoku:** Belirsizliğe karşı tampon. Talep dalgalanması ve tedarik süresi arttıkça yükselir.
- **Sipariş/lot miktarı:** Bir ikmalde gönderilecek miktar (ör. tam palet, tam araç).
- **Tedarik süresi:** Sipariş ile teslim arasındaki süre. Planlanan ikmal, ihtiyaç tarihinden bu kadar önce başlatılır.

Silver, Pyke ve Thomas, bu parametrelerin hizmet düzeyi ile stok maliyeti arasındaki dengeye göre belirlenmesini anlatır.

### Parametrelerin bakımı

DRP'nin kalitesi, kullandığı parametrelerin güncelliğine bağlıdır. Sistem bir kez kurulduktan sonra parametreler güncellenmezse, öneriler kısa sürede gerçekle bağını kaybeder.

- **Gözden geçirme takvimi:** Güvenlik stoku, tedarik süresi ve sipariş miktarları belirli aralıklarla, örneğin çeyrek bazında, gözden geçirilmelidir. Mevsimsel ürünlerde bu sıklık artırılmalıdır.
- **Ürün sınıflaması:** Tüm ürünlere aynı hizmet seviyesi hedefi verilmemelidir. Ciroya katkısı yüksek ve talebi düzenli ürünlerle, düşük hacimli ve düzensiz talepli ürünler farklı parametrelerle yönetilmelidir.
- **Gerçekleşen tedarik süresi:** Tedarikçinin taahhüt ettiği süre yerine, sipariş ve mal kabul tarihlerinden ölçülen gerçek süre ve değişkenliği kullanılmalıdır.
- **Minimum sipariş ve ambalaj kısıtları:** Tedarikçinin minimum sipariş miktarı, koli ve palet katları sipariş önerisine yansıtılmalıdır.

**Planlayıcının rolü.** DRP önerileri otomatik olarak siparişe dönüştürülebilir, ancak planlayıcı istisnalara odaklanmalıdır: beklenmedik talep artışları, tedarik gecikmeleri, yeni ürünler ve sona eren ürünler. Sistem, normalden sapan önerileri ayrı bir listede göstermelidir.

**Ağ boyunca denge.** Merkez depo ile bölge depoları arasında stok dengesizliği sık görülür: bir depoda fazla, diğerinde eksik stok bulunur. Depolar arası transfer önerileri, yeni satın almadan önce değerlendirilmelidir. Silver, Pyke ve Thomas'ın vurguladığı gibi, parametre kararları hizmet seviyesi ile stok maliyeti arasındaki bilinçli bir dengedir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b6.py` ile yapılmıştır.

Bir bölge deposunda 900 koli stok var, haftalık talep 400 koli, güvenlik stoku 300, lot 400 koli. Birinci hafta sonunda öngörülen stok **500**. İkinci hafta sonunda ikmal olmazsa **100** koli kalacak, bu güvenlik stokunun altında. Sistem ikinci haftaya 400 koli giriş planlıyor; öngörülen stok **500** oluyor. Tedarik süresi bir hafta olduğu için sevkiyat birinci hafta başlatılıyor.

## Sık yapılan hatalar

- Tüm ürünlere aynı güvenlik stokunu vermek.
- Tedarik sürelerini yıllarca güncellememek.
- Sistem önerilerini gerekçesiz elle değiştirmek.
- Tahmin hatasını güvenlik stoku hesabına katmamak.

## Pratikte nasıl uygulanır?

- [ ] Ürünleri önem ve talep değişkenliğine göre gruplayın.
- [ ] Her grup için güvenlik stoku ve lot kuralı belirleyin.
- [ ] Tedarik sürelerini gerçekleşen veriden üç ayda bir güncelleyin.
- [ ] Planlanan ve gerçekleşen ikmalleri haftalık karşılaştırın.

## Daha fazlası

- Silver, Pyke ve Thomas, *Inventory and Production Management in Supply Chains*.
- Ptak ve Smith, *Orlicky's Material Requirements Planning* (kitap; doğrulanmadı).
