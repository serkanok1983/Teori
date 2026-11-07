---
id: kb-ea-17-1-build-buy-configure
title: "Yaz, satın al, ayarla: Yazılım edinme kararı"
summary: "Bir iş ihtiyacı için hazır paketi olduğu gibi kullanmak, paketi ayarlamak ve genişletmek ya da özel yazılım geliştirmek arasındaki seçimi; uyum–boşluk analizini, özelleştirme borcunu ve ağırlıklı puanlamayla karar vermeyi anlatır."
course: ea
category: yazilim-secimi-ve-proje
tags: [yazilim-secimi, erp, ozellestirme, karar-verme]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, it-yoneticisi]
level: orta
source_lessons: [EA-17.1, EA-41.2]
reading_minutes: 3
key_points:
  - "Seçenekler: paketi olduğu gibi kullanmak, paketi ayarlamak ve genişletmek, özel yazılım geliştirmek."
  - "Uyum–boşluk analizi, paketin süreçlerinizin ne kadarını karşıladığını gösterir."
  - "Her özelleştirme, sürüm yükseltmelerinde ödenen bir borç yaratır."
  - "Farklılaştıran süreçte özel çözüm, standart süreçte paket genellikle daha mantıklıdır."
  - "Karar ağırlıklı puanlama, toplam sahip olma maliyeti ve risk ile birlikte verilmelidir."
glossary_terms: [uyum-bosluk-analizi, ozellestirme-borcu, toplam-sahip-olma-maliyeti]
related: [kb-ea-17-2-total-cost-of-ownership, kb-ea-17-3-writing-requirements, kb-ea-5-5-erp-core-vs-best-of-breed, kb-ea-18-3-why-erp-projects-fail]
sources:
  - title: "Enterprise resource planning: cultural fits and misfits: is ERP a universal solution?"
    authors: "Soh, C.; Kien, S. S.; Tay-Yap, J."
    year: 2000
    type: article
    doi: "10.1145/332051.332070"
    url: "https://doi.org/10.1145/332051.332070"
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

"Bu paket bizim işimize uymuyor, kendimiz yazalım" ya da "Paketi alalım, eksikleri yazdırırız" kararları yıllarca sürecek maliyet doğurur. Bu kart, kararı yapılandırılmış biçimde vermenize yardım eder.

## Temel fikir

Üç ana seçenek vardır:

1. **Olduğu gibi kullanmak:** Paketi standart haliyle kullanır, süreci pakete uyarlarsınız. Hızlı ve ucuzdur; ama süreç değişikliği gerektirir.
2. **Ayarlamak ve genişletmek:** Paketin parametreleriyle, ek alanlarla ve tedarikçinin desteklediği eklentilerle uyarlarsınız.
3. **Özel yazılım:** İhtiyaca tam uyar; ama geliştirme, bakım ve kişiye bağımlılık riski sizdedir.

Bu seçeneklere bir dördüncüsü eklenir: birkaç hazır hizmeti API'lerle birleştirmek.

Kararın temeli **uyum–boşluk analizidir** (*fit-gap*): Süreç adımları tek tek yazılır, her biri için paketin standart olarak karşılayıp karşılamadığı işaretlenir. Soh ve arkadaşları (2000), ERP paketlerinin içine gömülü süreç varsayımlarının yerel iş uygulamalarıyla çatışabildiğini gösterir. Bu boşluklar ya süreci değiştirerek ya da paketi özelleştirerek kapatılır.

Her özelleştirme bir **özelleştirme borcu** yaratır: Sürüm yükseltmelerinde yeniden test edilmesi, belki yeniden yazılması gerekir. Genel kural: Rakiplerden sizi ayıran süreçlerde özel çözüm düşünülebilir; muhasebe ve stok gibi standart süreçlerde pakete uyum genellikle daha mantıklıdır.

### Karar için değerlendirme çerçevesi

Yazma, satın alma veya ayarlama kararı, her ihtiyaç için ayrı ayrı verilmelidir. Değerlendirmede şu sorular yol gösterir:

- **Süreç standart mı?** Muhasebe, bordro ve e-belge gibi alanlarda süreçler büyük ölçüde mevzuatla belirlenir. Bu alanlarda yazılım geliştirmek, sürekli mevzuat takibi gerektirir; hazır ürün genellikle daha güvenlidir.
- **Farklılaştırıcı mı?** Şirketinizin rekabet avantajı sağlayan süreçlerinde, hazır ürünün sizi rakiplerinizle aynı yönteme zorlaması bir dezavantaj olabilir. Bu alanlarda ayarlama veya geliştirme daha anlamlı olabilir.
- **İç kapasite var mı?** Kendi yazılımınızı geliştirmek, yalnızca ilk geliştirmeyi değil, yıllarca sürecek bakım, güvenlik ve destek yükünü de üstlenmek demektir. Bu kapasite tek bir kişiye bağlıysa risk yüksektir.
- **Zaman baskısı:** Hazır ürün daha hızlı devreye alınabilir; ancak süreç uyumsuzlukları, beklenmedik uyarlama ihtiyaçları doğurabilir.
- **Uyumsuzluk boyutu:** Soh ve arkadaşlarının vurguladığı gibi, hazır ürün ile şirket süreçleri arasındaki uyumsuzluklar ya süreç değiştirilerek ya da ürün özelleştirilerek kapatılır. Hangisinin seçileceği, maliyet ve değişim direnci açısından değerlendirilmelidir.

**Özelleştirmenin uzun vadeli maliyeti.** Hazır ürün üzerinde yapılan ağır özelleştirmeler, sürüm yükseltmelerini zorlaştırır ve tedarikçi desteğini sınırlayabilir. Bu nedenle özelleştirme yerine ürünün sunduğu ayar seçenekleri, uzantı noktaları veya ayrı bir uygulama katmanı tercih edilmelidir.

**Karar kaydı.** Hangi ihtiyaç için hangi yolun seçildiği ve gerekçesi yazılı olarak saklanmalıdır. Koşullar değiştiğinde bu kararlar yeniden değerlendirilebilir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b3.py` ile yapılmıştır.

Bir bayi saha satış çözümü için üç seçeneği beş ölçütle 1–5 arası puanlıyor:

| Ölçüt (ağırlık) | Paket olduğu gibi | Paket + ayar | Özel yazılım |
|---|---|---|---|
| İşe uygunluk (%30) | 3 | 4 | 5 |
| Toplam maliyet (%25) | 5 | 4 | 2 |
| Zaman (%15) | 5 | 4 | 1 |
| Risk (%15) | 4 | 4 | 2 |
| Farklılaşma (%15) | 2 | 3 | 5 |
| **Ağırlıklı puan** | **3,80** | **3,85** | **3,20** |

İlk iki seçenek birbirine çok yakın. Bayi kararı, ağırlıkları değiştirdiğinde sıralamanın değişip değişmediğine bakarak ve beş yıllık maliyet hesabıyla birlikte veriyor. Özel yazılım en uygun çözüm olsa da maliyet ve zaman nedeniyle geride kalıyor.

## Sık yapılan hatalar

- Uyum–boşluk analizini tedarikçinin satış sunumuna bırakmak.
- Her boşluğu özelleştirmeyle kapatmak, süreci değiştirmeyi hiç düşünmemek.
- Özel yazılımın bakım ve kişi bağımlılığı maliyetini hesaba katmamak.
- Puanlama ağırlıklarını sonuç belli olduktan sonra ayarlamak.

## Pratikte nasıl uygulanır?

- [ ] Kritik süreçleri adım adım yazın ve her adım için uyum–boşluk işareti koyun.
- [ ] Her boşluk için "süreci değiştir" ve "paketi özelleştir" seçeneklerini maliyetiyle karşılaştırın.
- [ ] Ölçütleri ve ağırlıkları teklifleri görmeden önce belirleyin.
- [ ] Özelleştirmeleri bir listede tutun ve her sürüm yükseltmesinde gözden geçirin.

## Daha fazlası

- Soh ve ark. (2000), *Communications of the ACM*. https://doi.org/10.1145/332051.332070
