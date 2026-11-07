---
id: kb-ea-5-4-application-portfolio
title: "Uygulama envanteri ve portföy kararı: Hangi sistem kalsın, hangisi gitsin?"
summary: "Firmanın kullandığı uygulamaları iş yetenekleriyle eşleştirip iş uygunluğu ve teknik kaliteye göre puanlamayı; her biri için yatırım, koruma, taşıma ya da kaldırma kararı vermeyi anlatır."
course: ea
category: is-sistemleri-temelleri
tags: [uygulama-portfoyu, yazilim-secimi, butce, bt-yonetisimi]
roles: [it-yoneticisi]
level: orta
source_lessons: [EA-5.4]
reading_minutes: 3
key_points:
  - "Önce firmanın ne yaptığını (iş yetenekleri), sonra bunu hangi uygulamanın desteklediğini listeleyin."
  - "Her uygulama iki eksende puanlanır: işe uygunluk ve teknik kalite."
  - "TIME yaklaşımı dört karar önerir: yatırım yap, koru, taşı, kaldır."
  - "Excel tabloları ve küçük araçlar da portföyün parçasıdır; çoğu risk oradadır."
  - "Portföy yılda bir gözden geçirilir; karar, bütçe ve yol haritasına bağlanır."
glossary_terms: [uygulama-portfoyu, erp]
related: [kb-ea-1-1-what-is-an-enterprise-system, kb-ea-5-5-erp-core-vs-best-of-breed, kb-ea-41-1-case-distributor-app-landscape, kb-ea-6-1-it-governance-decision-rights]
sources:
  - title: "TOGAF Series Guides (The Open Group)"
    authors: "The Open Group"
    year: 2026
    type: standard
    verified: false
    note: "Yetenek haritası kavramı; erişilmedi."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Büyüyen bir firmada uygulamalar zamanla birikir: eski bir ön muhasebe programı, ERP, birinin yazdığı prim Excel'i, depo için alınmış bir barkod uygulaması, artık kimsenin sevmediği eski mobil sipariş programı. Bu kart, bu yığını bir **uygulama portföyü** (*application portfolio*) olarak ele alıp her uygulama için bilinçli karar vermenizi sağlar. Bütçe dönemi ve yeni yazılım seçimi öncesinde işe yarar.

## Temel fikir

Portföy çalışması üç adımdır.

**1. Yetenek haritası.** Firmanın yaptığı işler, organizasyondan bağımsız olarak listelenir: müşteri yönetimi, sipariş alma, fiyatlama, stok yönetimi, sevkiyat, faturalama, tahsilat, satın alma, raporlama, insan kaynakları. Bunlara **iş yeteneği** (*business capability*) denir. Organizasyon değişse de yetenekler kalır.

**2. Eşleme.** Her yeteneği hangi uygulamanın desteklediği yazılır. İki sorun hemen görünür: aynı yeteneği birden çok uygulamanın yapması (çakışma) ve hiçbir uygulamanın desteklemediği, Excel'le yürüyen yetenekler (boşluk).

**3. Puanlama ve karar.** Her uygulama iki eksende puanlanır (ör. 1–5):

- **İşe uygunluk:** İşin ihtiyacını ne kadar karşılıyor, kullanıcı ne kadar memnun?
- **Teknik kalite:** Güvenli mi, destekleniyor mu, entegre olabiliyor mu, bakımı kolay mı?

Yaygın kullanılan **TIME** sınıflaması dört karar önerir:

| İşe uygunluk | Teknik kalite | Karar |
|---|---|---|
| Yüksek | Yüksek | **Yatırım yap** (*Invest*): geliştirmeye devam |
| Düşük | Yüksek | **Koru/izle** (*Tolerate*): olduğu gibi bırak, yatırım yapma |
| Yüksek | Düşük | **Taşı** (*Migrate*): işlevi daha sağlam bir platforma aktar |
| Düşük | Düşük | **Kaldır** (*Eliminate*): kapat, verisini arşivle |

### Portföy kararlarını uygulamaya dökmek

Uygulama envanteri ve puanlama, ancak somut kararlara ve bir yol haritasına dönüştüğünde değer üretir. Kararların uygulanmasında şu adımlar önerilir:

- **Karar türleri:** Her uygulama için dört temel karardan biri verilir: koru, geliştir, değiştir veya kaldır. İşe uygunluğu yüksek ve teknik kalitesi iyi uygulamalar korunur; işe uygun ancak teknik olarak zayıf olanlar yenilenir; işe uygunluğu düşük olanlar değiştirilir veya kaldırılır.
- **Bağımlılıkları görün:** Bir uygulamanın kaldırılması, ona bağlı entegrasyonları, raporları ve kullanıcıları etkiler. ArchiMate gibi modelleme dilleri, bu bağımlılıkların görselleştirilmesine yardımcı olur.
- **Sıralama:** Tüm değişiklikleri aynı anda yapmak mümkün değildir. Önce riski en yüksek ve iş etkisi en büyük alanlar ele alınmalıdır.
- **Maliyet bilgisi:** Her uygulamanın lisans, bakım, altyapı ve destek maliyeti envantere eklenmelidir. Maliyet bilgisi, kaldırma kararlarının gerekçelendirilmesini kolaylaştırır.
- **Sahiplik:** Her uygulamanın bir iş sahibi ve bir teknik sahibi olmalıdır. Sahibi olmayan uygulamalar, genellikle kimsenin karar vermeye cesaret edemediği uygulamalardır.

**Envanterin güncel tutulması.** Envanter, yeni uygulama satın alındığında, bir uygulama kaldırıldığında veya önemli bir değişiklik yapıldığında güncellenmelidir. Yılda bir kez yapılan genel gözden geçirme, envanterin gerçekle bağını korur.

**Gölge uygulamalar.** Birimlerin kendi başına kullandığı tablolar ve bulut hizmetleri de envantere dahil edilmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Uygulamalar ve puanlar gerçek değildir; sınıflama `scripts/cards_numbers_ea_b1.py` ile yapılmıştır (eşik: 3 ve üstü "yüksek").

| Uygulama | İşe uygunluk | Teknik kalite | Karar |
|---|---|---|---|
| ERP | 4 | 4 | Yatırım yap |
| Eski ön muhasebe programı | 2 | 2 | Kaldır |
| Excel prim tablosu | 4 | 1 | Taşı |
| Depo barkod uygulaması | 2 | 4 | Koru/izle |
| Eski mobil sipariş programı | 3 | 2 | Taşı |

Prim tablosu işin tam ihtiyacını karşılıyor ama tek bir kişinin bilgisayarında, sürüm kontrolü yok ve elle besleniyor. Kararı "taşı": prim hesabı ERP ya da saha uygulamasındaki bir modüle aktarılacak. Eski ön muhasebe programı yalnızca geçmiş yıllara bakmak için açılıyor; verisi arşivlenip lisansı kapatılacak.

## Sık yapılan hatalar

- Envantere yalnızca satın alınan yazılımları yazmak; Excel ve makroları atlamak.
- Puanlamayı yalnızca BT'nin yapması; işe uygunluğu kullanıcılara sormamak.
- "Kaldır" kararı verip verinin nasıl arşivleneceğini planlamamak.
- Portföy kararlarını bütçe ve proje planına bağlamamak.

## Pratikte nasıl uygulanır?

- [ ] Firmanızın 10–15 ana iş yeteneğini tek sayfada listeleyin.
- [ ] Kullanılan tüm uygulamaları (Excel dahil) sahibi, kullanıcı sayısı ve yıllık maliyetiyle yazın.
- [ ] Her uygulamayı kullanıcılar işe uygunluk, BT teknik kalite açısından puanlasın.
- [ ] TIME kararlarını yönetimle onaylayın; her "taşı" ve "kaldır" için bir tarih koyun.
- [ ] Çakışan ve boş kalan yetenekleri yeni yazılım seçiminde öncelik olarak kullanın.
- [ ] Portföyü yılda bir güncelleyin.

## Daha fazlası

- The Open Group, TOGAF Series Guides — yetenek haritası (erişilmedi; doğrulanmadı).
- TIME sınıflaması piyasada yaygın bir uygulamadır; burada genel yöntem olarak anlatılmıştır.
