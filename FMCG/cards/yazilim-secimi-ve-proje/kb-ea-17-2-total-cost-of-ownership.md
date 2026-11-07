---
id: kb-ea-17-2-total-cost-of-ownership
title: "Toplam sahip olma maliyeti (TSM): Yazılımın gerçek fiyatı"
summary: "Bir yazılımın yalnızca lisans ya da abonelik fiyatıyla değil; uygulama, veri taşıma, eğitim, entegrasyon, iç personel zamanı, işletme ve çıkış maliyetleriyle beş yıllık bir modelde nasıl karşılaştırılacağını anlatır."
course: ea
category: yazilim-secimi-ve-proje
tags: [tsm, maliyet, yazilim-secimi, butce]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-17.2]
reading_minutes: 3
key_points:
  - "Lisans ya da abonelik bedeli, toplam maliyetin genellikle yalnızca bir kısmıdır."
  - "TSM; ilk yatırım, yıllık işletme ve çıkış maliyetlerini birlikte ele alır."
  - "İç personel zamanı en sık unutulan maliyet kalemidir."
  - "Teklifler aynı süre (ör. beş yıl) ve aynı kalemlerle karşılaştırılmalıdır."
  - "Büyük tutarlarda paranın zaman değeri için net bugünkü değer de hesaplanmalıdır."
glossary_terms: [toplam-sahip-olma-maliyeti, net-bugunku-deger]
related: [kb-ea-17-1-build-buy-configure, kb-ea-16-1-cloud-saas-basics, kb-ea-17-3-writing-requirements, kb-ea-16-5-cloud-cost-data-residency]
sources:
  - title: "Total cost of ownership: An analysis approach for purchasing"
    authors: "Ellram, L. M."
    year: 1995
    type: article
    doi: "10.1108/09600039510099928"
    url: "https://doi.org/10.1108/09600039510099928"
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

İki teklif geldi: Biri yıllık abonelik, diğeri tek seferlik lisans ve bakım. Hangisinin ucuz olduğunu ilk yıl faturasına bakarak söyleyemezsiniz. Bu kart, teklifleri **toplam sahip olma maliyeti** (TSM) ile aynı zemine taşır.

## Temel fikir

Ellram (1995), satın almada fiyatın ötesine geçen bu yaklaşımı sistematik hale getirir. TSM, bir yazılımı seçtiğiniz günden bıraktığınız güne kadar ödediğiniz her şeydir. Kalemleri üç gruba ayırmak işinizi kolaylaştırır:

- **İlk yatırım:** Lisans (varsa), uygulama ve danışmanlık, veri taşıma, entegrasyon geliştirme, eğitim, donanım.
- **Yıllık işletme:** Abonelik veya bakım bedeli, altyapı ve destek, entegrasyon bakımı, sürüm yükseltme testleri, iç personel zamanı.
- **Çıkış:** Verinin dışarı alınması, paralel çalışma, sözleşme fesih bedelleri.

**İç personel zamanı**, projede ve sonrasında kendi çalışanlarınızın harcadığı zamandır. Faturası gelmediği için çoğu zaman tabloya girmez.

Teklifleri aynı süre (genellikle beş yıl), aynı kullanıcı sayısı ve aynı kalemlerle karşılaştırın. Tutarlar büyükse ve ödeme zamanları çok farklıysa, gelecek ödemeleri bugüne indirgeyen net bugünkü değer de hesaplanmalıdır.

### TSM hesabını güvenilir kılmak

TSM tablosu, karar vericilere yalnızca bir sayı değil, varsayımlarıyla birlikte bir tablo sunmalıdır. Hesabın güvenilirliğini artırmak için şu adımlar önerilir:

- **Aynı kapsamla karşılaştırın:** Teklifler farklı modül, kullanıcı ve hizmet kapsamıyla gelir. Karşılaştırmadan önce tüm teklifleri aynı kapsam listesine göre düzenleyin; eksik kalemler için tedarikçiden ek fiyat isteyin.
- **Büyümeyi hesaba katın:** Kullanıcı sayısı, işlem hacmi ve veri miktarı yıllar içinde artacaktır. Lisans ve bulut abonelik ücretlerinin bu büyümeyle nasıl değiştiği, sözleşme koşullarından okunmalıdır.
- **Fiyat artış maddelerine bakın:** Abonelik ve bakım ücretlerinin yıllık artış oranı, sözleşme yenilemesinde pazarlık gücünü belirler. Artış için bir üst sınır pazarlık konusu yapılmalıdır.
- **Gizli maliyetleri arayın:** Test ortamı, ek depolama, yedekleme, entegrasyon araçları, raporlama lisansları ve yerel mevzuat uyarlamaları genellikle temel fiyata dahil değildir.
- **Duyarlılık analizi yapın:** Proje süresinin uzaması veya danışmanlık gününün artması gibi senaryoların toplam maliyete etkisini gösterin. Bu, karar vericilerin riski görmesini sağlar.

**Maliyetin yanında fayda.** TSM tek başına bir karar ölçütü değildir. Daha pahalı bir çözüm, daha hızlı devreye alınıyor, daha az özelleştirme gerektiriyor veya daha iyi destek sunuyorsa toplamda daha avantajlı olabilir. Bu nedenle TSM, beklenen faydalar ve risklerle birlikte bir iş gerekçesi belgesinde sunulmalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b3.py` ile yapılmıştır.

Bir üreticinin bulut ERP için beş yıllık TSM modeli (TL):

| Kalem | İlk yatırım | Yıllık | 5 yıl toplam |
|---|---|---|---|
| Abonelik | 0 | 540.000 | 2.700.000 |
| Uygulama hizmeti | 650.000 | 0 | 650.000 |
| Veri taşıma | 120.000 | 0 | 120.000 |
| Eğitim | 80.000 | 20.000 | 180.000 |
| Entegrasyon bakımı | 150.000 | 60.000 | 450.000 |
| İç personel zamanı | 300.000 | 180.000 | 1.200.000 |
| Altyapı ve destek | 0 | 90.000 | 450.000 |
| **Toplam** | | | **5.750.000** |

Birinci yıl maliyeti **2.190.000 TL**. Abonelik, beş yıllık toplamın yalnızca **%47,0**'si. İç personel zamanı tek başına 1.200.000 TL ile ikinci büyük kalem. Firma, diğer teklifi de aynı tabloya dökerek karşılaştırıyor.

## Sık yapılan hatalar

- Bir teklifin ilk yılını diğerinin beş yılıyla kıyaslamak.
- İç personel zamanını ve entegrasyon bakımını yok saymak.
- Abonelik fiyat artışını ve kullanıcı artışını modele koymamak.
- Çıkış maliyetini hiç düşünmemek.

## Pratikte nasıl uygulanır?

- [ ] Tüm tedarikçilerden aynı kalem listesine göre teklif isteyin.
- [ ] Beş yıllık bir tablo kurun; kullanıcı ve fiyat artışı varsayımlarını açıkça yazın.
- [ ] İç personel zamanını gün sayısı ve maliyetle tahmin edin.
- [ ] Varsayımları değiştirince sıralamanın değişip değişmediğini kontrol edin.

## Daha fazlası

- Ellram (1995), *International Journal of Physical Distribution & Logistics Management*. https://doi.org/10.1108/09600039510099928
