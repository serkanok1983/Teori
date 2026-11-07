---
id: kb-ea-8-4-gs1-barcodes-pim
title: "Ürün bilgisi ve GS1 kimlikleri: GTIN, GLN ve SSCC"
summary: "Ürün bilgisinin tek kaynaktan yönetilmesini (PIM) ve GS1 kimlik numaralarının (GTIN, GLN, SSCC) dağıtım zincirindeki rolünü anlatır; GTIN kontrol hanesinin nasıl hesaplandığını örnekler."
course: ea
category: veri-yonetimi
tags: [ana-veri, barkod, gs1, urun, zincir-market]
roles: [uretici-sahibi, uretici-yonetici, depo-lojistik-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-8.4]
reading_minutes: 3
key_points:
  - "GTIN ürünü, GLN yeri veya firmayı, SSCC ise bir lojistik birimi (palet, koli) tanımlar."
  - "Tüketici birimi, koli ve palet için ayrı GTIN gerekir; koli içi adet ana veride doğru tutulmalıdır."
  - "GTIN'in son hanesi kontrol hanesidir ve diğer hanelerden hesaplanır; hatalı girişi yakalar."
  - "Ürün bilgisi yönetimi (PIM), ürünün ölçü, içerik, görsel ve barkod bilgisini tek kaynaktan dağıtır."
  - "Zincir marketlere hatalı ürün verisi göndermek, sipariş ve fatura uyuşmazlığına yol açar."
glossary_terms: [gtin, ana-veri]
related: [kb-ea-8-1-master-data-governance, kb-ea-11-4-edi-with-chains, kb-ea-30-4-barcodes-traceability, kb-ea-30-3-wms-what-it-does]
sources:
  - title: "GS1 General Specifications"
    authors: "GS1"
    year: 2026
    type: standard
    verified: false
    note: "gs1.org ve gs1tr.org kutudan erişilemedi; kontrol hanesi algoritması yayımlamadan önce teyit edilmeli."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Bir zincir market yeni ürününüzü listelemek için sizden barkod, koli içi adet, boyut, ağırlık ve görsel ister. Bu bilgiler ERP'de, pazarlamanın Excel'inde ve depo sisteminde farklıysa, ilk siparişte sorun çıkar. Bu kart, ürün kimliklerinin ortak dili olan GS1 numaralarını ve **ürün bilgisi yönetimini** (PIM, *product information management*) anlatır.

## Temel fikir

GS1, ürün ve lojistik kimlikleri için küresel standartlar yayımlayan bir kuruluştur. Dağıtımda en çok kullanılan üç kimlik:

| Kimlik | Neyi tanımlar | Örnek kullanım |
|---|---|---|
| **GTIN** (*Global Trade Item Number*) | Ticari ürün: tüketici birimi, koli, paket | Kasadaki barkod, siparişteki ürün kodu |
| **GLN** (*Global Location Number*) | Firma veya yer: merkez, depo, mağaza | Elektronik siparişte teslim yeri |
| **SSCC** (*Serial Shipping Container Code*) | Tek bir lojistik birim: palet, koli | Palet etiketi, sevk bildirimi |

Tüketici birimi, koli ve palet ayrı ticari birimlerse her biri ayrı GTIN alır. Koli içi adet de ana verinin parçasıdır.

GTIN-13'ün son hanesi **kontrol hanesidir**. İlk 12 hane soldan başlayarak sırasıyla 1 ve 3 ile çarpılır, toplanır; toplamı 10'un katına tamamlayan sayı kontrol hanesidir. Böylece elle girilen yanlış bir hane çoğunlukla yakalanır.

**PIM**, ürünün tüm özelliklerini (ad, içerik, ölçü, ağırlık, görsel, barkodlar, koli içi adet) tek kaynakta tutar ve ERP'ye, e-ticaret sitesine ve müşterilere dağıtır. Küçük firmada ayrı PIM yerine ERP'deki ürün kartı ve onay kuralları yeterli olabilir.

### Ürün bilgisinin yönetimi

Ürün kimlikleri doğru tanımlansa bile, ürünle ilgili diğer bilgilerin dağınık ve tutarsız olması, satış ve lojistikte sorunlara yol açar. Ürün bilgisi yönetiminde dikkat edilmesi gereken konular şunlardır:

- **Lojistik bilgiler:** Ürünün, kolinin ve paletin ağırlığı, boyutları ve koli içi adedi doğru olmalıdır. Bu bilgiler depo yerleşimi, araç yükleme planı ve navlun hesabı için kullanılır. Hatalı boyut bilgisi, depoda yer sorununa ve yanlış yükleme planına yol açar.
- **Ambalaj hiyerarşisi:** Adet, koli ve palet seviyelerinin her biri için ayrı tanımlayıcı ve birim dönüşüm oranları tutulmalıdır.
- **Ticari bilgiler:** Ürün adı, açıklaması, kategori, marka ve görseller tüm kanallarda tutarlı olmalıdır. Zincir müşteriler ve e-ticaret platformları belirli formatlarda ürün bilgisi talep eder.
- **Yasal bilgiler:** Gıda ürünlerinde içerik, alerjen ve besin değeri bilgileri doğru ve güncel olmalıdır.
- **Ürün yaşam döngüsü:** Yeni ürün açılışı, ambalaj değişikliği ve ürünün satıştan kalkması için onay akışları tanımlanmalıdır.

**Ambalaj değişikliklerinin yönetimi.** Ürünün boyutu veya içeriği değiştiğinde yeni bir kimlik gerekip gerekmediği, GS1'in kimlik tahsis kurallarına göre değerlendirilmelidir. Değişiklik, müşterilerin sistemlerini de etkileyebilir; bu nedenle önceden duyurulmalıdır.

**Veri paylaşımı.** Ürün bilgilerinin müşterilerle standart formatlarda paylaşılması, her müşteri için ayrı tablo hazırlama yükünü azaltır.

## Bir örnek

> **Örnek (temsili rakamlar):** Numaralar gösterim amaçlıdır; kontrol haneleri `scripts/cards_numbers_ea_b2.py` ile hesaplanmıştır.

İlk 12 hanesi `590123412345` olan bir GTIN için kontrol hanesi 7 bulunur: tam numara **5901234123457**. `400638133393` için kontrol hanesi 1'dir: **4006381333931**.

Bir üretici, ERP'ye girilen ürün kartında GTIN'in kontrol hanesini otomatik doğrulayan bir kural ekliyor. Ayrıca yeni ürün kartı için koli içi adet, brüt ağırlık ve boyut zorunlu alan oluyor; kart, kalite ekibinin onayı olmadan zincir marketlere gönderilmiyor.

## Sık yapılan hatalar

- Koli ve tüketici birimine aynı barkodu vermek.
- Ürün değişince (gramaj, içerik) yeni GTIN gerekip gerekmediğini kontrol etmemek.
- Ürün verisini müşteriye e-posta ile Excel olarak göndermek; sürüm karışır.
- Kontrol hanesini doğrulamadan barkodu sisteme almak.

## Pratikte nasıl uygulanır?

- [ ] Ürün kartında tüketici birimi, koli ve palet için ayrı barkod alanları açın.
- [ ] GTIN kontrol hanesi doğrulamasını sisteme ekletin.
- [ ] Ürün verisinin sahibini belirleyin ve yeni ürün açılışını onaya bağlayın.
- [ ] Ürün değişikliklerinde yeni GTIN kuralını GS1 kılavuzundan teyit edin.

## Daha fazlası

- GS1 General Specifications (erişilemedi; doğrulanmadı). Türkiye'deki üyelik ve numara tahsisi için GS1 Türkiye'ye başvurulmalıdır.
