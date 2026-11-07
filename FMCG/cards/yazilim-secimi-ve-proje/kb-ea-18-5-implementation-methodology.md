---
id: kb-ea-18-5-implementation-methodology
title: "Uygulama yöntemi: Aşamalar, standarda uyum ve şelale–çevik dengesi"
summary: "Bir ERP veya iş uygulaması projesinin aşamalarını; standart süreçten başlayan uyum atölyelerini, şelale, çevik ve karma yaklaşımların farkını ve geçiş (cutover) planının yerini anlatır."
course: ea
category: yazilim-secimi-ve-proje
tags: [erp, proje, metodoloji, cevik]
roles: [it-yoneticisi]
level: orta
source_lessons: [EA-18.5]
reading_minutes: 3
key_points:
  - "Tipik aşamalar: hazırlık, keşif, gerçekleştirme ve canlıya geçiş; ardından destek."
  - "Standarda uyum yaklaşımı, önce paketin standart sürecini gösterip yalnızca gerçek boşlukları tartışır."
  - "Şelale, kapsamı belli işlerde; çevik, belirsiz ve sık değişen işlerde güçlüdür."
  - "ERP projelerinin çoğu karmadır: Ana plan aşamalı, yapılandırma ve raporlar kısa döngülerle ilerler."
  - "Her aşamanın sonunda yazılı bir kabul kapısı olmalıdır."
glossary_terms: [uyum-bosluk-analizi, canliya-gecis]
related: [kb-ea-18-3-why-erp-projects-fail, kb-ea-41-5-cutover-plan, kb-ea-18-6-data-migration-opening-balances, kb-ea-19-1-project-management-basics]
sources:
  - title: "A model of ERP project implementation"
    authors: "Parr, A.; Shanks, G."
    year: 2000
    type: article
    doi: "10.1080/02683960010009051"
    url: "https://doi.org/10.1080/02683960010009051"
    verified: true
    checked_on: 2026-10-28
  - title: "A spiral model of software development and enhancement"
    authors: "Boehm, B."
    year: 1988
    type: article
    doi: "10.1109/2.59"
    url: "https://doi.org/10.1109/2.59"
    verified: true
    checked_on: 2026-10-28
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Uygulama ortağınız size bir proje planı getirdiğinde, aşamaların neden o sırayla olduğunu ve her aşamanın sonunda ne teslim alacağınızı bilmeniz gerekir. Bu kart, ERP uygulama yöntemlerinin ortak iskeletini anlatır.

## Temel fikir

Parr ve Shanks (2000), ERP projelerini planlama, proje ve geliştirme sonrası aşamalarına ayıran bir model önerir. Proje aşaması kendi içinde kurulum, yeniden tasarım, yapılandırma, test ve kurulum adımlarından oluşur. Günümüz tedarikçi yöntemleri de benzer bir iskelet kullanır:

1. **Hazırlık:** Proje ekibi, kapsam, plan, ortamların kurulması.
2. **Keşif:** **Standarda uyum** atölyeleri. Önce paketin standart süreci örnek veriyle gösterilir; yalnızca gerçekten karşılanmayan adımlar boşluk olarak kaydedilir. Klasik "ihtiyacınızı anlatın, biz yazalım" yaklaşımından daha az özelleştirme doğurur.
3. **Gerçekleştirme:** Yapılandırma, geliştirmeler, entegrasyonlar, veri taşıma provaları ve testler.
4. **Canlıya geçiş:** Son kullanıcı eğitimi, geçiş planı, canlıya geçiş ve yoğun destek.

**Şelale ve çevik:** Şelale yaklaşımında her aşama bitmeden sonrakine geçilmez; kapsamı net işlerde öngörülebilirdir. Boehm'in (1988) spiral modeli, riskleri erken görmek için yinelemeli ilerlemeyi önerir. Çevik yöntemler de kısa döngülerde çalışan parçalar teslim eder. ERP'de çoğunlukla **karma** bir yol izlenir: Ana plan ve kapılar aşamalıdır, yapılandırma ve raporlar iki–üç haftalık döngülerle gösterilir.

Her aşamanın sonunda bir **kabul kapısı** olur: Hangi belgeler onaylandı, hangi testler geçti, hangi riskler açık?

### Yöntemi projeye uyarlamak

Parr ve Shanks'in ERP uygulama modeli, projenin planlama, uygulama ve canlı sonrası aşamalarının her birinde farklı başarı faktörlerinin öne çıktığını gösterir. Uygulama yöntemi seçilirken şu noktalar göz önünde bulundurulmalıdır:

- **Standarda uyum:** Yazılımın standart süreçlerini temel almak, özelleştirme ihtiyacını ve riski azaltır. Bunun için tasarım atölyelerinde önce standart süreç gösterilmeli, ardından gerçekten gerekli farklılıklar tartışılmalıdır.
- **Uyumsuzluk listesi:** Standart süreçle karşılanamayan ihtiyaçlar, gerekçeleri ve çözüm önerileriyle birlikte bir listede toplanmalıdır. Her uyumsuzluk için süreç değişikliği, ayar veya geliştirme seçeneklerinden biri seçilmelidir.
- **Aşama kapıları:** Her aşamanın sonunda, bir sonraki aşamaya geçmek için gerekli koşullar kontrol edilmelidir: tasarım onayı, test sonuçları, veri hazırlığı gibi.
- **Çevik unsurlar:** Raporlar, ekranlar ve entegrasyonlar gibi bileşenler, kısa döngülerde geliştirilip kullanıcılara gösterilebilir. Bu, geri bildirimin erken alınmasını sağlar.
- **Risk odaklı planlama:** Boehm'in sarmal modelinde vurgulandığı gibi, en yüksek riskli konular projenin başında ele alınmalıdır. Örneğin karmaşık bir entegrasyon veya veri taşıma, erken bir prototiple denenebilir.

**Aşamalı veya tek seferde geçiş.** Tüm modüllerin ve şubelerin aynı anda canlıya alınması ile aşamalı geçiş arasındaki seçim, risk ve maliyet dengesine göre yapılmalıdır. Aşamalı geçiş riski azaltır, ancak geçici entegrasyonlar gerektirebilir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b4.py` ile yapılmıştır.

Bir bayinin 25 haftalık ERP planı:

| Aşama | Hafta | Pay |
|---|---|---|
| Hazırlık | 3 | %12,0 |
| Keşif (standarda uyum) | 6 | %24,0 |
| Gerçekleştirme | 12 | %48,0 |
| Canlıya geçiş | 4 | %16,0 |

Keşif aşamasında satış, satın alma, depo ve finans için standart süreçler gösteriliyor; 22 boşluk kaydediliyor. Bunların 14'ü süreç değişikliğiyle, 8'i yapılandırma veya küçük geliştirmeyle kapatılıyor. Gerçekleştirme aşaması dört döngüye bölünüyor ve her döngü sonunda kilit kullanıcılar sistemi kendi senaryolarıyla deniyor.

## Sık yapılan hatalar

- Keşif aşamasını kısaltıp boşlukları gerçekleştirme sırasında keşfetmek.
- "Çevik" adı altında kapsamı ve kabul kapılarını belirsiz bırakmak.
- Veri taşıma provalarını tek bir son denemeye bırakmak.
- Kabul kapılarında açık riskleri yazmadan imza atmak.

## Pratikte nasıl uygulanır?

- [ ] Uygulama ortağından aşamalar, teslimatlar ve kabul kapılarını içeren yazılı yöntem isteyin.
- [ ] Keşif atölyelerine kilit kullanıcıları tam gün katın.
- [ ] Boşlukları "süreç değişikliği / yapılandırma / geliştirme" olarak sınıflandırın.
- [ ] En az iki veri taşıma provası ve bir genel prova planlayın.

## Daha fazlası

- Parr ve Shanks (2000), *Journal of Information Technology*. https://doi.org/10.1080/02683960010009051
- Boehm (1988), *IEEE Computer*. https://doi.org/10.1109/2.59
