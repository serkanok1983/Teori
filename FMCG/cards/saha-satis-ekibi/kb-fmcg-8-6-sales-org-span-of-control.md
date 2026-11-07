---
id: kb-fmcg-8-6-sales-org-span-of-control
title: "Satış organizasyonu ve kontrol aralığı"
summary: "Bir saha şefinin kaç temsilciye bakacağı hem maliyeti hem de koçluk kalitesini belirler. Bu kart satış organizasyonunun temel katmanlarını, kontrol aralığını etkileyen faktörleri ve aralığı değiştirmenin maliyet ve kalite etkisini anlatır."
course: fmcg
category: saha-satis-ekibi
tags: [saha-satis, liderlik, maliyet]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: orta
source_lessons: [FMCG-8.6]
reading_minutes: 3
key_points:
  - "Kontrol aralığı, bir yöneticiye doğrudan bağlı çalışan sayısıdır."
  - "Dar aralık daha fazla koçluk imkânı, geniş aralık daha düşük yönetim maliyeti demektir."
  - "Uygun aralık; temsilcilerin deneyimine, bölgenin coğrafyasına ve şefin koçluğa ayırması beklenen süreye bağlıdır."
  - "Aralığı genişletmek ancak koçluğun başka yollarla desteklendiği durumda sağlıklıdır."
glossary_terms: [ziyaret-sikligi]
related: [kb-fmcg-8-9-coaching, kb-fmcg-8-4-sales-force-sizing, kb-fmcg-8-5-territory-routing, kb-fmcg-8-3-salesperson-performance-drivers, kb-fmcg-8-7-sales-kpi-design]
sources:
  - title: "Building a Winning Sales Force"
    authors: "Zoltners, A. A.; Sinha, P.; Lorimer, S. E."
    year: 2009
    type: book
    verified: false
    note: "Kitap; künye kontrol edilmedi."
  - title: "Sales Force Management"
    authors: "Churchill, G. A.; Ford, N. M.; Walker, O. C."
    year: 2000
    type: book
    verified: false
    note: "Kitap; baskı yılı kontrol edilmedi."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Maliyet baskısı geldiğinde ilk düşünülen adımlardan biri yönetim katmanını inceltmektir. Bu doğru olabilir, ama saha şefi sayısı azaldıkça her temsilciye ayrılan koçluk süresi de azalır. Bu kart, bu dengeyi bilinçli kurmanızı sağlar.

## Temel fikir

**Tipik katmanlar.** Hızlı tüketim saha organizasyonunda genellikle şu katmanlar bulunur:

- **Satış temsilcisi:** Noktaları ziyaret eder.
- **Saha şefi ya da takım lideri:** Temsilcilerin günlük yönetimi, koçluk, hedef takibi.
- **Bölge müdürü:** Birkaç saha şefinden sorumlu, dağıtıcı ilişkisi ve bölge planı.
- **Satış direktörü:** Kanal ya da ülke düzeyinde sorumluluk.

Dağıtıcı modelinde temsilciler dağıtıcıya bağlı olabilir. Bu durumda üreticinin saha ekibi çoğu zaman dağıtıcının temsilcilerini yönlendiren ve denetleyen bir rol üstlenir.

**Kontrol aralığı** (*span of control*). Bir yöneticiye doğrudan bağlı çalışan sayısıdır. Satış yönetimi kaynakları, uygun aralığın sabit bir sayı olmadığını; işin karmaşıklığına, ekibin deneyimine ve yöneticinin rolüne göre değiştiğini anlatır (örneğin Churchill ve arkadaşlarının satış yönetimi kitabı; Zoltners, Sinha ve Lorimer).

Aralığı etkileyen faktörler:

- **Deneyim:** Yeni temsilciler daha fazla gözetim ister.
- **Coğrafya:** Dağınık bölgelerde şefin her temsilciye eşlik etmesi zaman alır.
- **Şefin diğer işleri:** Dağıtıcı ilişkisi, büyük müşteri yönetimi ya da raporlama.
- **Koçluk hedefi:** Şefin her temsilciyle ayda kaç gün sahada olması bekleniyor?

**Kontrol aralığını belirleyen sorular.** Doğru kontrol aralığı için şu sorular sorulabilir: Temsilciler ne kadar deneyimli? Yeni temsilcilerin oranı yüksekse şef daha fazla koçluk zamanı ayırmalıdır. Bölge coğrafi olarak ne kadar dağınık? Dağınık bölgelerde ortak ziyaret için yolda geçen süre artar. Şefin idari iş yükü (raporlama, dağıtıcı toplantıları, kilit müşteri görüşmeleri) ne kadar? Bu iş yükü yüksekse koçluğa zaman kalmaz. SFA ve raporlama araçları ne kadar gelişmiş? İyi araçlar şefin izleme yükünü azaltır. Organizasyon değişikliğinden sonra koçluk sıklığını, temsilci devir oranını ve bölge sonuçlarını birkaç dönem izleyerek kararın etkisini ölçün.

## Bir örnek

> **Örnek (temsili rakamlar):** Ekip büyüklüğü ve şef maliyeti varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b4.py` ile yapılmıştır.

46 temsilcilik bir ekip. Bir saha şefinin yıllık toplam maliyeti 900.000 TL.

| Kontrol aralığı | Şef sayısı | Şef başına temsilci | Yıllık şef maliyeti |
|---|---|---|---|
| 8 | 6 | 7,7 | 5.400.000 TL |
| 12 | 4 | 11,5 | 3.600.000 TL |

Aralığı 12'ye çıkarmak yılda 1.800.000 TL tasarruf sağlıyor. Ama ayda 20 saha günü olan bir şef, 7,7 temsilciyle her birine yaklaşık iki buçuk gün, 11,5 temsilciyle ise iki günden az ayırabilir. Ekipte çok sayıda yeni temsilci varsa bu azalma performansa yansıyabilir. Karar verirken tasarrufu, koçluk süresindeki kaybın olası satış etkisiyle karşılaştırmak gerekir.

## Sık yapılan hatalar

- **Aralığı yalnızca maliyetle belirlemek.** Koçluk süresi azalınca performans da düşebilir.
- **Şefi rapor hazırlayan kişiye dönüştürmek.** Şef sahada değilse aralık ne olursa olsun koçluk yapılmaz.
- **Her bölgede aynı aralığı kullanmak.** Dağınık ve yeni ekipli bölgeler daha dar aralık ister.

## Pratikte nasıl uygulanır?

- [ ] Şeflerin zamanını nasıl kullandığını birkaç hafta boyunca ölçün.
- [ ] Her temsilci için ayda kaç gün koçluk hedeflediğinizi belirleyin.
- [ ] Bu hedeften ve şefin saha günlerinden uygun aralığı hesaplayın.
- [ ] Aralığı genişletiyorsanız raporlama yükünü azaltın ya da dijital koçluk araçlarıyla destekleyin.

## Daha fazlası

- Zoltners, A. A.; Sinha, P.; Lorimer, S. E. (2009). *Building a Winning Sales Force.* (kaynak doğrulanmadı)
- Churchill, G. A.; Ford, N. M.; Walker, O. C. (2000). *Sales Force Management.* (kaynak doğrulanmadı)
