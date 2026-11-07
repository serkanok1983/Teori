---
id: kb-ea-8-1-master-data-governance
title: "Ana veri ve veri yönetişimi: Müşteri ve ürün kartının sahibi kim?"
summary: "Ana veri, hareket verisi ve referans veriyi ayırır; müşteri ve ürün kartlarının kimin sorumluluğunda olacağını, veri sahibi ve veri sorumlusu rollerini ve basit veri politikalarını anlatır."
course: ea
category: veri-yonetimi
tags: [ana-veri, veri-kalitesi, veri-yonetisimi, erp, musteri]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru, it-yoneticisi]
level: temel
source_lessons: [EA-6.5, EA-8.1]
reading_minutes: 3
key_points:
  - "Ana veri; müşteri, ürün, tedarikçi, çalışan gibi işlemlerde tekrar tekrar kullanılan temel kayıtlardır."
  - "Hareket verisi (sipariş, fatura) ana veriye dayanır; ana veri hatalıysa tüm işlemler hatalı olur."
  - "Veri yönetişimi, veriyle ilgili kararları kimin verdiğini ve hangi kuralların geçerli olduğunu belirler."
  - "Her ana veri alanının bir iş sahibi ve günlük bakımını yapan bir veri sorumlusu olmalıdır."
  - "Kart açma ve değiştirme yetkisi sınırlı tutulmalı, zorunlu alanlar sistemde denetlenmelidir."
glossary_terms: [ana-veri, veri-yonetisimi]
related: [kb-ea-8-2-data-quality-field, kb-ea-8-3-mdm-matching-duplicates, kb-ea-8-4-gs1-barcodes-pim, kb-ea-6-1-it-governance-decision-rights]
sources:
  - title: "Designing data governance"
    authors: "Khatri, V.; Brown, C. V."
    year: 2010
    type: article
    doi: "10.1145/1629175.1629210"
    url: "https://doi.org/10.1145/1629175.1629210"
    verified: true
    checked_on: 2026-10-28
  - title: "DAMA-DMBOK: Data Management Body of Knowledge (2nd ed.)"
    authors: "DAMA International"
    year: 2017
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

Aynı market ERP'de üç kez, saha uygulamasında iki kez farklı adla kayıtlıysa, ne doğru ciro raporu alırsınız ne de doğru kredi limiti uygularsınız. Bu kart, **ana veriyi** (*master data*) ve onu yöneten **veri yönetişimini** (*data governance*) anlatır.

## Temel fikir

DAMA-DMBOK'taki ayrımla dört tür veri vardır:

| Tür | Örnek | Özellik |
|---|---|---|
| **Ana veri** | Müşteri, ürün, tedarikçi, depo, personel | Az değişir, çok işlemde kullanılır |
| **Hareket verisi** | Sipariş, fatura, sevkiyat, tahsilat | Sürekli oluşur, ana veriye bağlanır |
| **Referans veri** | İl–ilçe listesi, döviz kodları, birimler | Sabit kod listeleri |
| **Üst veri** (*metadata*) | Alan tanımları, kim ne zaman değiştirdi | Veri hakkında veri |

Ana veri hatası çarpan etkisi yapar: Yanlış ürün koli içi adedi, binlerce siparişte yanlış miktar demektir.

Khatri ve Brown (2010), veri yönetişimini veriyle ilgili karar alanları ve bu kararları kimin verdiği üzerinden tanımlar: veri ilkeleri, veri kalitesi, üst veri, erişim ve veri yaşam döngüsü. Pratikte iki rol öne çıkar:

- **Veri sahibi** (*data owner*): İş tarafındaki yönetici. Örneğin müşteri verisinde satış direktörü, ürün verisinde ürün/kategori müdürü. Kuralları onaylar.
- **Veri sorumlusu** (*data steward*): Kartları açan, düzelten, kalite raporlarını takip eden kişi.

### Yönetişimi küçük başlatmak

Veri yönetişimi çoğu zaman büyük bir organizasyon projesi olarak düşünülür ve bu nedenle hiç başlamaz. Orta ölçekli bir şirkette pratik bir başlangıç şöyle olabilir:

- **Bir veri alanı seçin:** Örneğin müşteri ana verisi. Sorunların en görünür olduğu ve iş etkisinin en büyük olduğu alanla başlamak, desteği kolaylaştırır.
- **Sahibi adıyla belirleyin:** Müşteri verisinin sahibi genellikle satış veya finans yöneticisidir. Sahip, alan tanımlarını ve kalite hedeflerini onaylar.
- **Sorumluyu atayın:** Kayıt açma, değiştirme ve kontrol işlerini günlük olarak yapan bir veya birkaç kişi belirleyin.
- **Tanımları yazın:** Müşteri, nokta, bayi, zincir gibi kavramların şirketinizde ne anlama geldiğini ve hangi alanların zorunlu olduğunu kısa bir sözlükte toplayın.
- **Değişiklik akışı kurun:** Kredi limiti, fiyat grubu veya banka bilgisi gibi kritik alanlardaki değişiklikler için onay akışı tanımlayın.

**Düzenli gözden geçirme.** Veri sahibi ve sorumluları, aylık kısa bir toplantıda kalite göstergelerini, açık sorunları ve tanım değişikliklerini gözden geçirmelidir. Bu toplantı, yönetişimin kâğıt üzerinde kalmamasını sağlar.

**Genişletmek.** İlk alanda kazanılan deneyimle ürün, tedarikçi ve fiyat verisine geçilebilir. Khatri ve Brown'un vurguladığı gibi, yönetişim kararlarının kimin tarafından ve hangi kapsamda verileceği açıkça tanımlanmalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b2.py` ile yapılmıştır.

12.000 müşteri kaydı olan bir bayide kayıtların %8'inin mükerrer olduğu tahmin ediliyor; bu **960** kayıt demek. Kart açma yetkisi 35 temsilcide, zorunlu alan yok. Yeni düzen:

- Müşteri verisinin sahibi satış direktörü; sorumlusu merkez ofiste bir satış destek uzmanı.
- Temsilci sahada yalnızca "aday müşteri" açabiliyor; vergi numarası ve konum zorunlu.
- Aday kart, sorumlunun mükerrer kontrolü ve onayından sonra ERP'ye aktif müşteri olarak geçiyor.

## Sık yapılan hatalar

- Ana veriyi BT'nin işi saymak; kuralları iş tarafının koyması gerekir.
- Kart açma yetkisini herkese vermek.
- Mükerrer kayıtları birleştirmeden yeni sisteme taşımak.
- Zorunlu alanları yalnızca eğitimde anlatıp sistemde denetlememek.

## Pratikte nasıl uygulanır?

- [ ] Müşteri, ürün ve tedarikçi verisi için birer veri sahibi ve veri sorumlusu atayın.
- [ ] Her ana veri türü için zorunlu alanları ve doğrulama kurallarını yazın.
- [ ] Kart açma ve değiştirme yetkisini sorumlularla sınırlayın; sahadan "aday" kayıt akışı kurun.
- [ ] Ayda bir veri kalitesi raporu (eksik alan, mükerrer şüphesi) inceleyin.

## Daha fazlası

- Khatri ve Brown (2010), *Communications of the ACM*. https://doi.org/10.1145/1629175.1629210
- DAMA International, *DAMA-DMBOK* 2. baskı (kitap; doğrulanmadı).
