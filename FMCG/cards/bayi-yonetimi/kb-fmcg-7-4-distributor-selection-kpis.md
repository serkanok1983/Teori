---
id: kb-fmcg-7-4-distributor-selection-kpis
title: "Dağıtıcı seçimi ve performans göstergeleri"
summary: "Yanlış dağıtıcı seçimi bir bölgeyi yıllarca geride bırakabilir. Bu kart dağıtıcı adaylarını ağırlıklı bir puan tablosuyla karşılaştırmayı ve seçimden sonra izlenecek temel performans göstergelerini anlatır."
course: fmcg
category: bayi-yonetimi
tags: [dagitim, analitik, strateji]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: orta
source_lessons: [FMCG-7.4]
reading_minutes: 3
key_points:
  - "Dağıtıcı seçiminde kapsama, finansal güç, lojistik kapasite, yönetim kalitesi ve uyum birlikte değerlendirilmelidir."
  - "Ağırlıklı puan tablosu, kararı tek bir kişinin izlenimine bırakmaz."
  - "Puanlar birbirine yakınsa, en zayıf alanın düzeltilebilir olup olmadığı kararı belirler."
  - "Seçimden sonra kapsama, sipariş karşılama, stok günü, tahsilat ve satış büyümesi düzenli izlenmelidir."
glossary_terms: [bayi, siparis-karsilama-orani, stok-gun-sayisi]
related: [kb-fmcg-7-5-distributor-development, kb-fmcg-7-1-distributor-pnl, kb-fmcg-7-2-distributor-roi, kb-fmcg-6-4-direct-vs-indirect, kb-fmcg-8-7-sales-kpi-design]
sources:
  - title: "Marketing Channels"
    authors: "Coughlan, A. T.; Anderson, E.; Stern, L. W.; El-Ansary, A. I."
    year: 2006
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

Yeni bir bölgeye girerken ya da mevcut dağıtıcıyı değiştirirken birkaç aday arasından seçim yapmanız gerekir. Bu kart, seçimi yapılandırmanızı ve seçilen dağıtıcının performansını ilk günden ölçmenizi sağlar.

## Temel fikir

**Seçim ölçütleri.** Coughlan ve arkadaşları, kanal üyesi seçiminde aracının üstleneceği işlevleri ne kadar iyi yapabileceğine bakmayı önerir. Hızlı tüketimde tipik ölçütler:

- **Kapsama:** Kaç noktaya, hangi sıklıkla ulaşıyor? Hedef nokta tiplerinde güçlü mü?
- **Finansal güç:** Stok ve alacak için yeterli sermayesi ve kredi kullanım imkânı var mı?
- **Lojistik kapasite:** Depo, araç, soğuk zincir ihtiyacı varsa ekipman.
- **Yönetim kalitesi:** Sahip ve yöneticilerin yetkinliği, sistem kullanımı, raporlama.
- **Uyum:** Portföyündeki diğer ürünler sizinle çatışıyor mu, tamamlıyor mu?

Her ölçüte bir ağırlık verip adayları 1–5 arası puanlayarak toplam puan hesaplanır.

**Performans göstergeleri.** Seçimden sonra izlenecekler:

- **Kapsama:** Aktif nokta sayısı ve sayısal dağıtım.
- **Sipariş karşılama oranı:** Gelen siparişlerin ne kadarı tam ve zamanında teslim edildi?
- **Stok günü:** Dağıtıcının elindeki stok kaç günlük satışa yetiyor? Çok düşükse stoksuzluk, çok yüksekse son kullanma tarihi riski.
- **Tahsilat:** Alacak tahsil süresi ve gecikmiş alacak oranı.
- **Satış büyümesi:** Hedefe göre ve bölge pazarına göre.

**Puan tablosunun ötesi.** Ağırlıklı puan tablosu karşılaştırmayı düzenler, ama tek başına karar vermez. Seçimden önce adayların mali tablolarını ve banka referanslarını finans ekibinizle inceleyin; depoyu ve araç filosunu yerinde görün; adayın mevcut müşterilerinden birkaçıyla konuşun. Adayın taşıdığı diğer markaların sizin kategorinizle çatışıp çatışmadığını ve yönetimin bir sonraki kuşağa nasıl devredileceğini sorun; aile şirketlerinde bu konu sık görülen bir risktir. Seçimden sonra ilk yıl için açık hedefler, üç aylık gözden geçirme takvimi ve performans yetersiz kalırsa izlenecek adımlar sözleşmede yazılı olmalıdır. Bu adımların hukuki yönü için hukuk danışmanınıza başvurun.

Seçim süreci boyunca adaylara aynı bilgileri vermek ve aynı ölçütlerle değerlendirmek, kararın hem adil hem de sonradan savunulabilir olmasını sağlar.

## Bir örnek

> **Örnek (temsili rakamlar):** Ağırlıklar ve puanlar varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b4.py` ile yapılmıştır.

| Ölçüt | Ağırlık | A | B | C |
|---|---|---|---|---|
| Kapsama | %30 | 4 | 3 | 5 |
| Finansal güç | %25 | 3 | 5 | 2 |
| Lojistik | %20 | 4 | 3 | 4 |
| Yönetim | %15 | 3 | 4 | 4 |
| Uyum | %10 | 5 | 3 | 2 |
| **Toplam** | | **3,70** | **3,65** | **3,60** |

Puanlar çok yakın. Bu durumda zayıf alanların düzeltilebilirliğine bakın. C'nin kapsaması en iyi, ama finansal gücü zayıf; büyüdükçe stok ve alacağı finanse edemeyebilir. A'nın finansal gücü ortalama ve portföyü uyumlu. B finansal olarak güçlü, kapsamayı zamanla geliştirebilir. Ekip, A ile başlamaya ve ilk yılın sonunda kapsama hedefini değerlendirmeye karar verir.

## Sık yapılan hatalar

- **Tek ölçüte göre seçmek.** En büyük kapsama, zayıf finansla birleşince sorun çıkarır.
- **Puanları tek kişiye vermek.** Satış, finans ve lojistik birlikte puanlamalıdır.
- **Göstergeleri sözleşmeye yazmamak.** Beklenti yazılı değilse performans konuşması zorlaşır.

## Pratikte nasıl uygulanır?

- [ ] Ölçütleri ve ağırlıkları adaylarla görüşmeden önce belirleyin.
- [ ] Her aday için saha ziyareti yapın, finansal bilgi ve referans isteyin.
- [ ] Puan tablosunu en az üç farklı birimden kişiyle doldurun.
- [ ] Sözleşmede performans göstergelerini, hedefleri ve gözden geçirme takvimini yazın.
- [ ] Göstergeleri aylık izleyin ve üç ayda bir dağıtıcıyla birlikte değerlendirin.

## Daha fazlası

- Coughlan, A. T.; Anderson, E.; Stern, L. W.; El-Ansary, A. I. (2006). *Marketing Channels.* (kaynak doğrulanmadı)
