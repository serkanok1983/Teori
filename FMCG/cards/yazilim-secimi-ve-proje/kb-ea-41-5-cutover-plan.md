---
id: kb-ea-41-5-cutover-plan
title: "Vaka: Eski sistemden yeni ERP ve satış uygulamasına geçiş planı"
summary: "Kurgusal bir dağıtıcının eski sistemden yeni ERP ve satış uygulamasına geçişinde canlıya geçiş (cutover) planını, açılış bakiyelerini, geri dönüş kararını ve değişim yönetimini adım adım anlatır."
course: ea
category: yazilim-secimi-ve-proje
tags: [vaka, cutover, canliya-gecis, veri-tasima, degisim-yonetimi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, it-yoneticisi]
level: ileri
source_lessons: [EA-41.5]
reading_minutes: 2
key_points:
  - "Canlıya geçiş planı, eski sistemin kapatılıp yeni sistemin açıldığı dönemin saat saat görev listesidir."
  - "Açılış bakiyeleri ve açık kalemler mutabakatla taşınmalı, iş birimince onaylanmalıdır."
  - "Önceden tanımlı geri dönüş kriterleri, kriz anında karar vermeyi kolaylaştırır."
  - "Prova geçişler, gerçek geçişteki sürprizleri azaltır."
  - "Kullanıcı eğitimi ve ilk haftalardaki yoğun destek planın parçasıdır."
glossary_terms: [canliya-gecis, geri-donus-plani]
related: [kb-ea-18-6-data-migration-opening-balances, kb-ea-41-1-case-distributor-app-landscape, kb-ea-40-4-integrating-sfa-with-erp]
sources:
  - title: "Practical Data Migration"
    authors: "Morris, J."
    year: 2012
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

Yeni sistem projelerinin en riskli anı canlıya geçiştir. Siparişler duramaz, faturalar kesilmeye devam etmelidir. Bu vaka kartı, bir dağıtıcı için geçiş planının nasıl kurulacağını gösterir.

## Temel fikir

**1. Strateji:** Tek seferde geçiş mi, bölge bölge mi? Dağıtıcıda genellikle ERP tek seferde, satış uygulaması bölge bölge açılır.

**2. Dondurma:** Geçişten önce ana veri değişiklikleri ve yeni ürün açılışı durdurulur.

**3. Prova geçişler:** En az bir veya iki tam prova yapılır; süreler ölçülür, hatalar düzeltilir.

**4. Geçiş penceresi görevleri:**

- Eski sistemde son işlemler ve dönem kapanışı
- Stok sayımı
- Açılış bakiyeleri: müşteri ve tedarikçi açık kalemleri, stok, banka
- Mutabakat ve iş birimi onayı
- Entegrasyonların açılması (SFA, e-belge entegratörü, banka)
- İlk sipariş ve ilk e-faturanın test edilmesi

**5. Geri dönüş kriterleri:** Hangi durumda eski sisteme dönüleceği önceden yazılır (örneğin belirli saate kadar e-fatura kesilemezse).

**6. Değişim yönetimi:** Eğitimler, kısa kullanım kılavuzları, ilk haftalarda sahada ve merkezde destek ekibi.

### Geçiş öncesi hazırlık kontrolü

Canlıya geçiş kararı, bir takvim tarihine değil, hazır olma kriterlerine bağlanmalıdır. Geçişten önce yönlendirme komitesinin gözden geçirmesi gereken başlıca konular şunlardır:

- **Test sonuçları:** Kritik iş senaryoları (sipariş, sevkiyat, fatura, tahsilat, satın alma, ay sonu) uçtan uca test edilmiş ve kabul edilmiş mi? Açık kalan hataların hangileri geçişi engeller, hangileri sonraya bırakılabilir?
- **Veri:** Ana veri taşıma provalarında hata oranı kabul edilebilir düzeyde mi? Müşteri, ürün ve fiyat kayıtları iş birimlerince örneklemeyle kontrol edildi mi?
- **Entegrasyonlar:** E-belge entegratörü, banka, satış uygulaması ve depo sistemi bağlantıları canlı ortamda test edildi mi?
- **Kullanıcılar:** Eğitimler tamamlandı mı, kullanıcı hesapları ve yetkileri hazır mı?
- **Destek:** İlk haftalar için destek ekibi, iletişim kanalları ve sorun önceliklendirme kuralları belirlendi mi?

**İletişim planı.** Geçiş, yalnızca şirket içini değil, müşterileri ve tedarikçileri de etkiler. Fatura görünümündeki değişiklikler, olası sevkiyat gecikmeleri ve yeni sipariş kanalları önceden duyurulmalıdır.

**Geçiş sonrası istikrar dönemi.** İlk haftalarda günlük kısa toplantılarla açık sorunlar, sipariş ve fatura hacimleri ve kullanıcı geri bildirimleri izlenmelidir. Proje ekibinin bu dönem bitmeden dağıtılması, sorunların çözümünü uzatır. Morris'in veri taşıma üzerine yazdıkları da, taşımanın teknik bir iş değil, iş birimlerinin sahiplenmesi gereken bir süreç olduğunu vurgular.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b8.py` ile yapılmıştır.

Kurgusal dağıtıcı, hafta sonunu kapsayan 48 saatlik bir geçiş penceresi belirliyor ve 36 görev planlıyor. Açılış bakiyesi mutabakatında 1.250 müşterinin açık bakiyesi tek tek karşılaştırılıyor. Prova geçişte mutabakat beklenenden uzun sürdüğü için gerçek geçişte bu adıma ek ekip atanıyor.

## Sık yapılan hatalar

- Prova geçiş yapmamak.
- Açılış bakiyelerini iş birimi onayı olmadan taşımak.
- Geri dönüş kriterini kriz anında tartışmak.
- Kullanıcı eğitimini son haftaya bırakmak.
- İlk haftalarda destek kapasitesini az tutmak.

## Pratikte nasıl uygulanır?

- [ ] Geçiş stratejisini ve tarihini belirleyin.
- [ ] Saat bazında görev listesi ve sorumlular hazırlayın.
- [ ] En az bir tam prova geçiş yapın.
- [ ] Mutabakat ve onay formlarını hazırlayın.
- [ ] Geri dönüş kriterlerini yazılı hâle getirin.
- [ ] Eğitim ve destek planını takvime bağlayın.

## Daha fazlası

- Morris, *Practical Data Migration* (kitap; doğrulanmadı).
- Bu vaka kurgusaldır ve ders kapsamındaki kartların sentezidir.
