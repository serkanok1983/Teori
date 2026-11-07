---
id: kb-ea-24-1-treasury-cash-forecasting
title: "Hazine yönetimi: Nakit pozisyonu, 13 haftalık nakit tahmini ve kur riski"
summary: "Günlük nakit pozisyonunun izlenmesini, 13 haftalık nakit akış tahmininin nasıl hazırlandığını, kur ve faiz riskinin temel yönetimini ve banka ilişkilerinin düzenlenmesini üretici ve bayi gözünden anlatır."
course: ea
category: finansal-analiz
tags: [hazine, nakit-tahmini, kur-riski, banka]
roles: [uretici-sahibi, bayi-sahibi, finans-muduru]
level: orta
source_lessons: [EA-24.1]
reading_minutes: 3
key_points:
  - "Nakit pozisyonu, tüm bankalardaki bakiyelerin ve günün beklenen giriş–çıkışlarının tek görünümüdür."
  - "13 haftalık nakit tahmini kısa vadeli açıkları önceden görmeyi sağlar."
  - "Tahminin temeli vadesi gelen alacaklar, borçlar, maaş ve vergi ödemeleridir."
  - "Dövizli borç ve alacakların net pozisyonu kur riskini gösterir."
  - "Tahmin her hafta gerçekleşenle karşılaştırılarak iyileştirilir."
glossary_terms: [nakit-pozisyonu, nakit-akis-tahmini, kur-riski]
related: [kb-eco-38-2-cash-conversion-cycle, kb-eco-36-6-cash-flow-vs-profit, kb-ea-24-2-bank-statement-integration, kb-ea-24-3-credit-limits-collections-systems]
sources:
  - title: "Integrated Business Processes with ERP Systems"
    authors: "Magal, S. R.; Word, J."
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

Kârlı bir dağıtıcı bile, tahsilatlar gecikip tedarikçi ödemeleri bir haftaya yığıldığında nakit sıkıntısına düşebilir. Bu kart, **hazine yönetiminin** temel araçlarını anlatır.

## Temel fikir

**Nakit pozisyonu.** Her sabah şu sorunun cevabı bilinmelidir: Bugün tüm bankalarda ne kadar param var, bugün ne girecek, ne çıkacak? ERP'ye otomatik aktarılan banka hareketleri bu görünümü kolaylaştırır.

**13 haftalık nakit tahmini.** Kısa vadeli planlamada yaygın bir araçtır. Haftalık sütunlarda:

- **Girişler:** Vadesi gelen müşteri alacakları, çek ve senetler, DBS tahsilatları.
- **Çıkışlar:** Tedarikçi ödemeleri, maaşlar, vergi ve SGK, kira, kredi taksitleri.
- **Kapanış bakiyesi** ve belirlenen **asgari nakit** seviyesiyle karşılaştırma.

Tahminin kaynağı ERP'deki açık kalemlerdir; ancak tahsilatın vadeden ne kadar sapacağı geçmiş davranışa göre düzeltilmelidir.

**Kur ve faiz riski.** Dövizli borçlar ve alacaklar netleştirildiğinde açık pozisyon görülür. Örneğin dövizli hammadde alıp TL satış yapan bir üreticinin döviz açığı vardır. Bu açık, fiyatlama, vadeli işlemler ya da dövizli satışla yönetilebilir. Değişken faizli krediler de faiz riskini taşır.

**Banka ilişkileri.** Hangi bankanın hangi hizmet (tahsilat, DBS, kredi, POS) için kullanıldığı ve maliyetleri düzenli olarak gözden geçirilmelidir.

### Nakit tahmininin doğruluğunu artırmak

Nakit tahmini, ancak düzenli olarak gerçekleşenle karşılaştırıldığında güvenilir hâle gelir. Tahmin kalitesini artırmak için şu yöntemler kullanılabilir:

- **Kaynak verisini ERP'den alın:** Açık alacaklar, açık borçlar, onaylanmış satın alma siparişleri ve planlı maaş ödemeleri doğrudan ERP'den alınmalıdır. Elle girilen tahminler, yalnızca sistemde bulunmayan kalemler için kullanılmalıdır.
- **Gerçek tahsilat davranışını kullanın:** Müşterilerin sözleşmedeki vadeye göre değil, geçmişte gerçekten ödedikleri sürelere göre tahsilat tahmini yapın. Müşteri grupları bazında ortalama gecikme hesaplanabilir.
- **Tahmin ile gerçekleşeni karşılaştırın:** Her hafta, bir önceki tahminde o hafta için öngörülen tutar ile gerçekleşen tutar karşılaştırılmalı; büyük sapmaların nedeni kaydedilmelidir.
- **Senaryo hazırlayın:** Büyük bir müşterinin ödemesinin gecikmesi, kur artışı veya beklenmedik bir yatırım gibi durumlar için olumsuz senaryolar hazırlanmalıdır. Bu, finansman ihtiyacının önceden görülmesini sağlar.

**Birimlerle iş birliği.** Satış ekibi büyük tahsilatlar hakkında, satın alma ekibi büyük ödemeler hakkında, insan kaynakları ise ikramiye ve kıdem ödemeleri hakkında hazine ekibini önceden bilgilendirmelidir. Bu bilgi akışının düzenli bir takvimi olmalıdır.

**Kur riski için yaklaşım.** Döviz cinsinden borç ve alacakların vade bazında görünür olması, açık pozisyonun büyüklüğünü ortaya koyar. Korunma kararları, şirketin risk iştahı ve yazılı bir hazine politikası çerçevesinde verilmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b5.py` ile yapılmıştır.

Bir bayi, önümüzdeki 13 hafta için tahmin hazırlıyor:

- Açılış bakiyesi: 2.000.000 TL
- Toplam giriş: 4.500.000 TL
- Toplam çıkış: 5.100.000 TL
- Kapanış: **1.400.000,00 TL**

Asgari nakit seviyesi 1.500.000 TL olduğu için **100.000,00 TL**'lik açık görülüyor. Bayi, büyük bir tedarikçi ödemesini vadesine göre bir hafta kaydırmak için önceden görüşüyor ve gecikmiş tahsilatlar için saha ekibiyle bir takip listesi oluşturuyor.

## Sık yapılan hatalar

- Nakit tahminini yalnızca ay sonunda yapmak.
- Tahsilatları vadede gerçekleşecek gibi varsaymak.
- Vergi ve SGK gibi kesin çıkışları unutmak.
- Döviz pozisyonunu yalnızca bilanço gününde hesaplamak.

## Pratikte nasıl uygulanır?

- [ ] Banka bakiyelerini her gün tek bir ekranda görün.
- [ ] 13 haftalık tahmini her hafta güncelleyin.
- [ ] Tahmin ile gerçekleşeni karşılaştırıp sapmaları not edin.
- [ ] Döviz pozisyonunu ayda bir hesaplayın ve yönetimle paylaşın.

## Daha fazlası

- Magal ve Word, *Integrated Business Processes with ERP Systems* (kitap; doğrulanmadı).
