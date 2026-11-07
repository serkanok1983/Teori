---
id: kb-ea-39-5-ml-forecast-recommendation
title: "İş uygulamalarında makine öğrenmesi"
summary: "Talep tahmini, satış ekibine sonraki en iyi aksiyon önerisi ve anormallik tespiti gibi makine öğrenmesi kullanımlarını; model yaşam döngüsü (MLOps) ve yönetişim gerekliliklerini anlatır."
course: ea
category: yapay-zeka-ve-otomasyon
tags: [makine-ogrenmesi, tahmin, oneri, anormallik, mlops]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, it-yoneticisi]
level: orta
source_lessons: [EA-39.5]
reading_minutes: 2
key_points:
  - "İş uygulamalarında makine öğrenmesinin üç yaygın kullanımı tahmin, öneri ve anormallik tespitidir."
  - "Sonraki en iyi aksiyon, satış temsilcisine ziyaret veya ürün önerisi sunar."
  - "Model başarısı yalnızca doğrulukla değil, kullanıcının öneriyi benimsemesiyle de ölçülmelidir."
  - "MLOps, modelin eğitim, yayın, izleme ve yenilenme süreçlerini kapsar."
  - "Model kararlarının açıklanabilirliği ve sahibi önceden belirlenmelidir."
glossary_terms: [sonraki-en-iyi-aksiyon, mlops, anormallik-tespiti]
related: [kb-ea-29-2-demand-planning-systems, kb-ea-39-4-ai-assistants-on-company-data, kb-ea-26-1-retail-execution-sfa]
sources:
  - title: "Machine Learning Operations (MLOps): Overview, Definition, and Architecture"
    authors: "Kreuzberger, D.; Kühl, N.; Hirschl, S."
    year: 2023
    type: article
    doi: "10.1109/ACCESS.2023.3262138"
    url: "https://doi.org/10.1109/ACCESS.2023.3262138"
    verified: true
    checked_on: 2026-10-28
  - title: "Hidden Technical Debt in Machine Learning Systems"
    authors: "Sculley, D. vd."
    year: 2015
    type: web
    url: "https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems"
    verified: true
    checked_on: 2026-10-28
    note: "URL HTTP 200 ile açıldı, başlık/kurum eşleşti (2026-10-28)."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28

---

## Ne işe yarar?

Makine öğrenmesi, "yapay zekâ projesi" olarak ayrı yürütüldüğünde çoğu zaman pilotta kalır. Değer, modelin günlük iş uygulamasına gömülmesiyle ortaya çıkar. Bu kart yaygın kullanımları ve modeli canlıda tutmanın gereklerini anlatır.

## Temel fikir

**Yaygın kullanımlar:**

- **Tahmin:** Ürün ve bölge bazında talep tahmini; planlama sistemine girdi olur.
- **Öneri (sonraki en iyi aksiyon):** Satış uygulamasında temsilciye "bu bayiye şu ürünü önerin" veya "bu hafta şu bayiyi ziyaret edin" önerisi.
- **Anormallik tespiti:** Olağandışı iade, iskonto veya ödeme hareketlerini işaretlemek.

**Başarı ölçümü:** Teknik doğruluk tek başına yetmez. Önerilerin kabul oranı, kabul edilen önerilerin sonucu ve kullanıcı geri bildirimi de izlenmelidir.

**MLOps:** Modelin veri hazırlığı, eğitimi, yayına alınması, performansının izlenmesi ve veriler değiştikçe yeniden eğitilmesi için tanımlı süreç.

**Yönetişim:** Her modelin bir iş sahibi olmalı; hangi verilerle eğitildiği, nerede kullanıldığı ve kararlarının nasıl açıklandığı belgelenmelidir.

### Bir modelin yaşam döngüsü

Kreuzberger ve arkadaşlarının MLOps derlemesi, modelin yalnızca geliştirilmesini değil, canlıda sürdürülmesini de kapsayan bir süreç tanımlar. Yönetici açısından bu döngünün adımları şöyle özetlenebilir:

1. **Problem tanımı:** Hangi karar iyileştirilecek ve başarı nasıl ölçülecek?
2. **Veri hazırlığı:** Geçmiş satış, promosyon, fiyat ve stok verisi temizlenir; eksik ve hatalı kayıtlar ayıklanır.
3. **Eğitim ve doğrulama:** Model geçmiş veriyle eğitilir ve modelin görmediği bir dönemde test edilir.
4. **Yayın:** Model, kullanıcının çalıştığı uygulamaya bağlanır.
5. **İzleme:** Tahmin hatası, öneri kabul oranı ve veri dağılımındaki değişim izlenir.
6. **Yenileme:** Performans düştüğünde veya iş koşulları değiştiğinde model yeniden eğitilir.

**Gizli maliyetler.** Sculley ve arkadaşları, makine öğrenmesi sistemlerinde modelin kendisinin, etrafındaki veri boru hatları ve yapılandırma kodunun yanında küçük bir parça olduğunu vurgular. Bu nedenle bütçe yalnızca model geliştirmeyi değil, veri altyapısını ve sürekli bakımı da kapsamalıdır.

**Basit başlayın.** Çoğu iş probleminde önce basit bir kural veya istatistiksel yöntemle bir karşılaştırma noktası oluşturmak gerekir. Karmaşık bir model, ancak bu karşılaştırma noktasını anlamlı biçimde geçiyorsa devreye alınmalıdır.

### Modelin izlenmesi

Canlıdaki modelin doğruluğu düzenli olarak ölçülmeli; düşüş görüldüğünde yeniden eğitim planlanmalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b8.py` ile yapılmıştır.

Bir satış uygulaması bir ayda temsilcilere 1.000 ürün önerisi sunuyor; 180'i kabul ediliyor: **%18,0**. Görüşmeler, temsilcilerin önerinin gerekçesini görmedikleri için güvenmediklerini gösteriyor. Ekip önerinin yanına kısa bir gerekçe ekliyor ve kabul oranını izlemeye devam ediyor.

## Sık yapılan hatalar

- Modeli kullanıcı iş akışına gömmeden "başarılı pilot" ilan etmek.
- Yalnızca teknik doğruluğu raporlamak.
- Canlıdaki modeli izlememek ve güncellememek.
- Modelin sahibini belirsiz bırakmak.
- Basit bir karşılaştırma noktası kurmadan karmaşık modele geçmek.
- Bütçede yalnızca model geliştirmeyi hesaba katıp veri altyapısını unutmak.

## Pratikte nasıl uygulanır?

- [ ] Kullanım senaryosunu bir iş kararına bağlayın.
- [ ] Başarı ölçütlerini (doğruluk, kabul oranı, iş sonucu) önceden yazın.
- [ ] Model izleme ve yeniden eğitim takvimi kurun.
- [ ] Her model için iş sahibi ve dokümantasyon belirleyin.

## Daha fazlası

- Kreuzberger, Kühl ve Hirschl (2023), MLOps derlemesi, IEEE Access.
- Sculley ve arkadaşları (2015), makine öğrenmesi sistemlerinde gizli teknik borç, NeurIPS.
