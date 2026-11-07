---
id: kb-fmcg-10-1-key-account-management
title: "Kilit müşteri yönetimi ve müşteri kâr-zararı"
summary: "Birkaç büyük zincir, bir üreticinin satışının önemli bir kısmını oluşturabilir. Bu kart kilit müşteri yönetiminin yapısını, ekip rollerini ve her kilit müşteri için liste fiyatından müşteri katkısına inen bir kâr-zarar tablosunun nasıl hazırlanacağını anlatır."
course: fmcg
category: kilit-musteri-ve-kategori
tags: [kilit-musteri, zincir-market, finans]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: orta
source_lessons: [FMCG-10.1, FMCG-10.8]
reading_minutes: 3
key_points:
  - "Kilit müşteri yönetimi; özel ekip, müşteri bazlı plan ve üst yönetim katılımıyla yürütülen bir yapıdır, yalnızca bir unvan değildir."
  - "Araştırmalar, kilit müşteri yönetiminin farklı yapılandırmalarının belirgin biçimde farklı sonuçlar verdiğini gösterir."
  - "Müşteri kâr-zararı; liste fiyatından başlayıp fatura altı ve fatura dışı indirimler, ürün maliyeti ve hizmet maliyetleri düşülerek müşteri katkısına iner."
  - "Vade ve hizmet maliyeti çoğu zaman görünmez kalır, ama müşteri katkısını önemli ölçüde etkiler."
  - "Satış hacmi en büyük müşteri, en kârlı müşteri olmayabilir."
glossary_terms: [kilit-musteri-yonetimi, fiyat-selalesi, ciro-primi, hizmet-maliyeti, vade]
related: [kb-fmcg-10-2-trade-terms, kb-fmcg-10-4-negotiating-with-chains, kb-fmcg-10-7-joint-business-planning, kb-fmcg-6-3-cost-to-serve, kb-fmcg-9-1-retailer-economics]
sources:
  - title: "A Configurational Perspective on Key Account Management"
    authors: "Homburg, C.; Workman, J. P.; Jensen, O."
    year: 2002
    type: article
    doi: "10.1509/jmkg.66.2.38.18471"
    url: "https://doi.org/10.1509/jmkg.66.2.38.18471"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Marketing 66(2), 38–60."
  - title: "Category Management Association"
    authors: "Category Management Association"
    year: 2026
    type: web
    url: "https://www.categorymanagement.org/"
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

Ulusal zincirlerle çalışan bir üreticide, birkaç müşteri satışın yarısına yakınını oluşturabilir. Bu müşterilerle ilişki, sıradan bir satış ziyaretinden çok daha karmaşıktır: yıllık ticari koşul görüşmeleri, merkez ve bölge alıcıları, promosyon takvimi, lojistik, fatura mutabakatı. Bu kart, kilit müşteri yönetimini (*key account management*, KAM) bir yapı olarak kurmanızı ve her kilit müşterinin size gerçekte ne kazandırdığını görmenizi sağlar.

## Temel fikir

**Yapı.** Homburg, Workman ve Jensen (2002), şirketlerin kilit müşterileri yönetme biçimlerini dört boyutta inceledi: hangi faaliyetlerin yapıldığı, kimlerin katıldığı, ne kadar resmîleştirildiği ve hangi kaynakların ayrıldığı. Farklı yapılandırmalar arasında performansın belirgin biçimde değiştiğini, iyi tasarlanmış ve üst yönetimin dahil olduğu yaklaşımların daha iyi sonuç verdiğini gösterdiler. Pratik ders şudur: Birine "kilit müşteri yöneticisi" unvanı vermek yeterli değildir; yapının, sürecin ve kaynakların da tanımlanması gerekir.

**Ekip.** Tipik bir kilit müşteri ekibi şunlardan oluşur:

- **Kilit müşteri yöneticisi:** İlişkinin ve ticari planın sahibi.
- **Kategori ya da pazarlama desteği:** Kategori analizi ve promosyon planı.
- **Tedarik zinciri temsilcisi:** Sipariş, teslimat ve bulunurluk.
- **Finans desteği:** Müşteri kâr-zararı, prim hesapları ve mutabakat.
- **Üst yönetim sponsoru:** Müşterinin üst yönetimiyle yılda birkaç kez görüşen yönetici.

**Müşteri kâr-zararı.** Her kilit müşteri için şu tablo hazırlanır:

1. Liste fiyatıyla brüt satış
2. Fatura altı indirimler → fatura tutarı
3. Fatura dışı indirimler (ciro primi, listeleme, promosyon katkısı) → net-net satış
4. Satılan malın maliyeti → brüt kâr
5. Hizmet maliyetleri: lojistik, müşteriye ayrılan ekip, vade finansman maliyeti → **müşteri katkısı**

Kategori yönetimi derneğinin kaynakları da, müşteriyle ilişkinin kategori ve kâr bakışıyla yönetilmesini önerir.

## Bir örnek

> **Örnek (temsili rakamlar):** Bütün tutarlar ve oranlar varsayımdır; vade maliyeti yıllık %40 sermaye maliyetiyle hesaplanmıştır; hesaplar `scripts/cards_numbers_fmcg_b6.py` ile yapılmıştır.

| Kalem | Tutar (TL) |
|---|---|
| Liste fiyatıyla satış | 20.000.000 |
| Fatura altı indirim (%10) | −2.000.000 |
| Fatura tutarı | 18.000.000 |
| Ciro primi (%4) | −720.000 |
| Listeleme ücretleri | −300.000 |
| Promosyon katkısı | −900.000 |
| **Net-net satış** | **16.080.000** |
| Satılan malın maliyeti | −9.000.000 |
| Brüt kâr | 7.080.000 |
| Lojistik (net-net satışın %3'ü) | −482.400 |
| Kilit müşteri ekibi | −600.000 |
| Vade maliyeti (60 gün) | −1.183.562 |
| **Müşteri katkısı** | **4.814.038** |

Müşteri katkısı, liste fiyatıyla satışın %24,1'i, net-net satışın %29,9'u. Dikkat çeken kalem vade: 60 günlük ödeme süresinin finansman maliyeti, ciro priminden ve listeleme ücretlerinin toplamından daha büyük. Enflasyonun ve faizlerin yüksek olduğu dönemlerde vade, ticari koşul pazarlığının en pahalı kalemi olabilir.

## Sık yapılan hatalar

- **Müşteriyi yalnızca satış hacmine göre değerlendirmek.** En büyük müşteri, koşulları nedeniyle en düşük katkıyı veriyor olabilir.
- **Vade ve hizmet maliyetini hesaba katmamak.** Bu kalemler çoğu zaman genel giderlerde kaybolur.
- **Kilit müşteri yöneticisini tek başına bırakmak.** Ekip ve üst yönetim desteği olmadan ilişki tek kişiye bağımlı kalır.
- **Kâr-zararı yılda bir kez hazırlamak.** Promosyon ve prim gerçekleşmeleri yıl içinde değişir; en az üç ayda bir güncelleyin.
- **Müşterinin önceliklerini bilmemek.** Müşterinin stratejisini, hedeflerini ve kategori rollerini anlamadan plan yapılamaz.

## Pratikte nasıl uygulanır?

- [ ] Satışın büyük kısmını oluşturan müşterileri kilit müşteri olarak belirleyin ve her biri için bir sorumlu atayın.
- [ ] Her kilit müşteri için yukarıdaki kâr-zarar tablosunu hazırlayın ve üç ayda bir güncelleyin.
- [ ] Müşteri katkısını müşteriler arasında karşılaştırın; düşük katkılı müşterilerde koşulları ve hizmet modelini gözden geçirin.
- [ ] Ekip rollerini ve toplantı ritmini yazılı hâle getirin.
- [ ] Her kilit müşteri için bir üst yönetim sponsoru belirleyin.
- [ ] Yıllık ticari görüşmeye müşteri kâr-zararıyla hazırlanın.

## Daha fazlası

- Homburg, C.; Workman, J. P.; Jensen, O. (2002). *A Configurational Perspective on Key Account Management.* Journal of Marketing 66(2), 38–60. https://doi.org/10.1509/jmkg.66.2.38.18471
- Category Management Association (2026). *Category Management Association.* https://www.categorymanagement.org/
