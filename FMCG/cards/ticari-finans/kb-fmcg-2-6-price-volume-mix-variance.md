---
id: kb-fmcg-2-6-price-volume-mix-variance
title: "Fiyat-hacim-karma analizi: Kâr bütçeden neden saptı?"
summary: "Bütçeyle gerçekleşen arasındaki kâr farkı fiyat, hacim, ürün karması ve maliyet etkilerine ayrılabilir. Bu kart iki ürünlü bir örnekle farkı parçalara ayırmayı ve her parçayı kime soracağınızı gösterir."
course: fmcg
category: ticari-finans
tags: [raporlama, butce, marj, fiyatlama]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: orta
source_lessons: [FMCG-2.6]
reading_minutes: 3
key_points:
  - "Toplam kâr farkı; hacim, karma, fiyat ve maliyet etkilerinin toplamına eşit olacak şekilde ayrıştırılmalıdır."
  - "Hacim etkisi toplam adet değişimini bütçedeki ortalama birim katkıyla değerler."
  - "Karma etkisi, satışın daha kârlı ya da daha az kârlı ürünlere kaymasının sonucudur ve çoğu zaman gözden kaçar."
  - "Fiyat etkisi gerçekleşen adet üzerinden hesaplanır; net fiyat kullanılmazsa ticari indirim sızıntısı fiyat etkisinde görünmez."
glossary_terms: [fiyat-hacim-karma-analizi, katki-payi, net-satis]
related: [kb-fmcg-2-1-fmcg-pnl, kb-fmcg-2-2-gross-to-net, kb-fmcg-8-13-sales-analytics, kb-eco-39-4-budgeting-standard-costs, kb-fmcg-4-4-portfolio-management]
sources:
  - title: "Cost & Effect: Using Integrated Cost Systems to Drive Profitability and Performance"
    authors: "Kaplan, R. S.; Cooper, R."
    year: 1998
    type: book
    verified: false
    note: "Kitap; faaliyet tabanlı maliyetleme. Künye kontrol edilmedi."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

"Satış hedefi tuttu ama kâr düştü" ya da "adet düştü ama kâr arttı" gibi durumlar ayrıştırma yapılmadan açıklanamaz. Fiyat-hacim-karma analizi (*price-volume-mix analysis*), kâr farkını sorumlu kişilerle konuşulabilir parçalara böler. Aylık performans toplantısı, bölge karşılaştırması ve bütçe revizyonunda kullanılır.

## Temel fikir

Kâr farkını dört etkiye ayırırız. Her etki, bir değişkeni değiştirip diğerlerini sabit tutarak hesaplanır:

1. **Hacim etkisi:** Toplam adet bütçeden ne kadar saptı? Fark, bütçedeki ortalama birim katkıyla çarpılır.
   - Hacim etkisi = (Gerçek toplam adet − Bütçe toplam adet) × Bütçe ortalama birim katkı
2. **Karma etkisi:** Toplam adet aynı kalsaydı, ürünler arasındaki dağılımın değişmesi kârı nasıl etkilerdi?
   - Karma etkisi = Σ (Gerçek adet − Gerçek toplam adet × Bütçe payı) × Bütçe birim katkı
3. **Fiyat etkisi:** Gerçek satılan adet üzerinden, net fiyattaki sapma.
   - Fiyat etkisi = Σ Gerçek adet × (Gerçek net fiyat − Bütçe net fiyat)
4. **Maliyet etkisi:** Gerçek adet üzerinden, birim değişken maliyetteki sapma (maliyet artışı negatif etkidir).

Dört etkinin toplamı, toplam katkı farkına tam olarak eşit olmalıdır. Eşit değilse hesapta hata vardır.

Hesap sırası ve ayrıştırma yöntemi şirketten şirkete biraz farklılık gösterebilir. Önemli olan, yöntemi bir kez seçip her dönem aynı biçimde uygulamaktır.

**Kime sorulur?** Hacim etkisi satış ekibine, karma etkisi satış ve pazarlamaya, fiyat etkisi ticari şartları yönetenlere (anahtar müşteri ve gelir yönetimi), maliyet etkisi tedarik ve üretime aittir.

**Analizi düzenli kullanmak.** Fiyat-hacim-karma analizi, aylık ya da üç aylık sonuç toplantılarının standart bir parçası olduğunda en yararlıdır. Her etki için bir sorumlu ve bir açıklama istenmelidir: Fiyat etkisi planlandığı gibi mi gerçekleşti? Hacim kaybı rekabetten mi, stoksuzluktan mı? Karma değişimi bilinçli bir portföy kararı mı, yoksa kanallar arası kayma mı? Bu sorular, rakamları eyleme dönüştürür.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek bir şirkete ait değildir; hesaplar `scripts/cards_numbers_fmcg_b1.py` ile yapılmıştır.

İki ürün: A (premium) ve B (ekonomik).

| | Bütçe adet | Bütçe fiyat | Gerçek adet | Gerçek fiyat | Birim maliyet |
|---|---|---|---|---|---|
| A | 10.000 | 50,00 TL | 8.000 | 52,00 TL | 30,00 TL |
| B | 10.000 | 30,00 TL | 14.000 | 30,00 TL | 22,00 TL |

- Bütçe katkı: 10.000 × 20 + 10.000 × 8 = **280.000 TL**
- Gerçek katkı: 8.000 × 22 + 14.000 × 8 = **288.000 TL**
- Toplam fark: **+8.000 TL**

Ayrıştırma (bütçe ortalama birim katkı 14,00 TL):

| Etki | TL |
|---|---|
| Hacim (22.000 − 20.000) × 14,00 | +28.000 |
| Karma (satış B'ye kaydı) | −36.000 |
| Fiyat (A'da +2,00 TL × 8.000) | +16.000 |
| Maliyet | 0 |
| **Toplam** | **+8.000** |

Toplam tabloya bakan biri "her şey yolunda" der. Ayrıştırma ise farklı bir hikâye anlatır: Adet arttı, ama satış ucuz ürüne kaydığı için 36.000 TL kaybedildi. Kârı kurtaran, premium üründeki fiyat artışı oldu. Premium üründe adet kaybı fiyat artışından mı kaynaklanıyor? Bir sonraki toplantının sorusu budur.

## Sık yapılan hatalar

- Yalnızca toplam farka bakıp karma etkisini görmemek.
- Fiyat etkisini liste fiyatıyla hesaplamak; net fiyat kullanılmazsa iskonto artışı görünmez.
- Etkilerin toplamının toplam farka eşit olduğunu kontrol etmemek.
- Her ay farklı bir ayrıştırma yöntemi kullanmak.
- Ürün sayısı çoksa ayrıştırmayı yalnızca marka düzeyinde yapıp alt kırılımdaki kaymaları kaçırmak.

## Pratikte nasıl uygulanır?

- [ ] Aylık raporunuza bu dört satırlık köprü tablosunu ekleyin.
- [ ] Fiyat etkisi için fatura dışı indirimleri de içeren net fiyatı kullanın.
- [ ] Karma etkisini hem ürün hem kanal bazında hesaplayın; bölge müdürleriyle paylaşın.
- [ ] Hesabı tabloda otomatik kontrolle kurun: dört etkinin toplamı fark ile eşleşmiyorsa uyarı versin.
- [ ] Her etkinin sahibini belirleyin ve toplantıda o kişiden açıklama isteyin.

## Daha fazlası

- Kaplan, R. S.; Cooper, R. (1998). *Cost & Effect: Using Integrated Cost Systems to Drive Profitability and Performance.* (kaynak doğrulanmadı)
