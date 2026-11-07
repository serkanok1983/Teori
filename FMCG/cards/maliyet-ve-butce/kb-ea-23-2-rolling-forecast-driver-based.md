---
id: kb-ea-23-2-rolling-forecast-driver-based
title: "Sürücü bazlı planlama, kayan tahmin ve sıfır tabanlı bütçe"
summary: "Satış ve maliyetleri hacim, fiyat ve verimlilik gibi sürücüler üzerinden planlamayı, her ay ileriye doğru uzayan kayan tahmini, sıfır tabanlı bütçeyi ve yüksek enflasyon döneminde Türkiye'de planlamanın nasıl uyarlanabileceğini anlatır."
course: ea
category: maliyet-ve-butce
tags: [planlama, kayan-tahmin, butce, enflasyon]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [EA-23.2]
reading_minutes: 3
key_points:
  - "Sürücü bazlı planlamada sonuçlar hacim, fiyat ve verimlilik gibi birkaç temel sürücüden hesaplanır."
  - "Kayan tahmin her ay güncellenir ve her zaman aynı uzunlukta bir dönemi kapsar."
  - "Sıfır tabanlı bütçe, her gider kalemini geçen yıla bakmadan yeniden gerekçelendirir."
  - "Yüksek enflasyonda fiyat ve maliyet sürücüleri ayrı izlenmeli, hacim ayrıca okunmalıdır."
  - "Az sayıda doğru sürücü, ayrıntılı ama güncellenmeyen bir bütçeden daha değerlidir."
glossary_terms: [kayan-tahmin, surucu-bazli-planlama, sifir-tabanli-butce]
related: [kb-ea-23-1-budgeting-purposes-games, kb-ea-29-2-demand-planning-systems, kb-fmcg-5-6-pricing-in-high-inflation, kb-eco-32-4-finance-in-high-inflation]
sources:
  - title: "Beyond Budgeting: How Managers Can Break Free from the Annual Performance Trap"
    authors: "Hope, J.; Fraser, R."
    year: 2003
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

Fiyatların her ay değiştiği bir ortamda, bir yıl önce yapılmış ayrıntılı bütçe hızla eskir. Bu kart, planlamayı daha hızlı ve daha gerçekçi yapmanın üç yolunu anlatır.

## Temel fikir

**Sürücü bazlı planlama.** Her satırı tek tek tahmin etmek yerine, sonuçları birkaç temel sürücüden hesaplarsınız:

- Ciro = hacim (koli) × net fiyat
- Dağıtım maliyeti = sevk edilen koli × koli başı maliyet
- Saha gideri = rut sayısı × rut başı maliyet

Bir sürücü değiştiğinde (ör. fiyat artışı) tüm plan otomatik güncellenir.

**Kayan tahmin.** Yıllık bütçe yerine, her ay bir sonraki 12 ayı (ya da 4–6 çeyreği) kapsayan tahmin yapılır. Geçen ay plandan çıkar, yeni bir ay eklenir. Böylece ufuk hep aynı uzunlukta kalır. Hope ve Fraser bu yaklaşımı yıllık bütçeye alternatif olarak önerir.

**Sıfır tabanlı bütçe.** Her gider kalemi "geçen yıl + enflasyon" yerine sıfırdan gerekçelendirilir. Tüm bütçeye her yıl uygulamak yorucudur; pazarlama veya genel giderler gibi seçili alanlarda dönemsel kullanmak daha pratiktir.

**Yüksek enflasyonda planlama.** Türkiye pratiğinde sık görülen uyarlamalar:

- Fiyat ve maliyet artışlarını ayrı sürücüler olarak tutmak,
- Büyümeyi hacim (koli, ton) üzerinden okumak, TL ciro büyümesini tek başına başarı saymamak,
- Planı aylık ya da üç aylık güncellemek.

### Sürücü bazlı modeli kurmak

Sürücü bazlı bir planlama modeli, iş sonuçlarını belirleyen az sayıdaki temel değişkene dayanır. Modeli kurarken şu adımlar izlenebilir:

- **Sürücüleri belirleyin:** Bir dağıtım şirketi için satışı belirleyen sürücüler; aktif nokta sayısı, ziyaret sıklığı, ziyaret başına sipariş oranı ve ortalama sipariş tutarı olabilir. Maliyet tarafında ise araç sayısı, kilometre, depo hacmi ve personel sayısı öne çıkar.
- **İlişkileri doğrulayın:** Sürücüler ile sonuçlar arasındaki ilişki, geçmiş verilerle kontrol edilmelidir. Varsayılan ilişki gerçek veriyle desteklenmiyorsa model yanıltıcı olur.
- **Sorumluları atayın:** Her sürücünün tahmininden bir birim sorumlu olmalıdır. Örneğin nokta sayısı satış, kilometre lojistik ekibi tarafından tahmin edilir.
- **Basit tutun:** Çok sayıda sürücü içeren modeller, bakımı zor ve anlaşılmaz hâle gelir. Sonuçları en çok etkileyen sürücülere odaklanılmalıdır.

**Kayan tahminin ritmi.** Kayan tahmin, her ay veya çeyrekte güncellenir ve her güncellemede tahmin ufku bir dönem ileri kayar. Güncellemenin kısa sürede yapılabilmesi için, sürücü verilerinin sistemlerden otomatik alınması gerekir. Aksi hâlde tahmin süreci, bütçe kadar zahmetli hâle gelir.

**Senaryo analizi.** Sürücü bazlı model, farklı senaryoların hızlıca hesaplanmasını sağlar: fiyat artışı, nokta kaybı veya yakıt maliyetinin yükselmesi gibi. Hope ve Fraser'ın vurguladığı gibi, amaç sabit bir hedefe kilitlenmek değil, değişen koşullara hızlı uyum sağlamaktır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b5.py` ile yapılmıştır.

Bir üretici bir çeyrek için 120.000 koli ve koli başı 250 TL net fiyat planlıyor: **30.000.000,00 TL** ciro. Aylık %3 fiyat artışı beklendiğinde üç ayda bileşik artış **%9,3** oluyor; yeni fiyat **273,18 TL**, yeni ciro **32.781.810,00 TL**. Sürücü bazlı modelde bu değişiklik tek bir hücrede yapılıyor. Yönetim de cironun arttığını ama hacmin aynı kaldığını açıkça görüyor.

## Sık yapılan hatalar

- Yüzlerce satırlık bütçe hazırlayıp yıl içinde hiç güncellememek.
- TL ciro büyümesini hacim büyümesi sanmak.
- Kayan tahmini bütçe hedefiyle karıştırmak.
- Sürücüleri tanımlamadan "ortalama artış" varsaymak.

## Pratikte nasıl uygulanır?

- [ ] Cironuzu ve ana giderlerinizi açıklayan 5–10 sürücü seçin.
- [ ] Her ay sürücüleri güncelleyip 12 aylık kayan tahmin üretin.
- [ ] Fiyat, hacim ve karma etkisini ayrı raporlayın.
- [ ] Seçili bir gider alanında sıfır tabanlı bütçe deneyin.

## Daha fazlası

- Hope ve Fraser, *Beyond Budgeting* (kitap; doğrulanmadı).
