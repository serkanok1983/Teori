---
id: kb-fmcg-6-7-e-grocery-quick-commerce
title: "Çevrim içi market ve hızlı teslimat: Sepet ekonomisi"
summary: "Çevrim içi market ve dakikalar içinde teslimat yapan hızlı ticaret uygulamaları, hızlı tüketim için büyüyen kanallardır. Bu kart bu kanalların sepet ekonomisini, üretici olarak dikkat edilecek noktaları ve kanalın sizden ne istediğini anlatır."
course: fmcg
category: dagitim-modeli
tags: [dagitim, e-ticaret, perakende]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: orta
source_lessons: [FMCG-6.7]
reading_minutes: 3
key_points:
  - "Çevrim içi siparişte toplama, paketleme ve teslimat maliyeti her sepete eklenir; küçük sepetler zarar edebilir."
  - "Sepet büyüklüğü, bu kanalın kârlılığındaki en kritik değişkendir."
  - "Kanal, üreticiden içerik, görsel, dijital görünürlük ödemesi ve stok sürekliliği bekler."
  - "Dijital raf da fiziksel raf gibi yönetilir: arama sonucu, kategori sayfası ve ürün sayfası."
glossary_terms: [hizli-ticaret, sepet-buyuklugu]
related: [kb-fmcg-6-1-rtm-channels-formats, kb-fmcg-9-7-retail-media, kb-fmcg-9-4-osa-out-of-stock, kb-fmcg-5-3-price-pack-architecture, kb-fmcg-6-3-cost-to-serve]
sources:
  - title: "Marketing Channels"
    authors: "Coughlan, A. T.; Anderson, E.; Stern, L. W.; El-Ansary, A. I."
    year: 2006
    type: book
    verified: false
    note: "Kitap; baskı yılı kontrol edilmedi."
  - title: "NielsenIQ"
    authors: "NielsenIQ"
    year: 2026
    type: web
    url: "https://www.nielseniq.com/"
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

Çevrim içi market siparişleri ve hızlı teslimat uygulamaları, özellikle büyük şehirlerde kategorinizin satışında giderek daha görünür bir pay alabilir. Bu kart, bu kanalların nasıl para kazandığını ya da kaybettiğini ve üretici olarak ne yapmanız gerektiğini anlatır. Kanal çok hızlı değiştiği için buradaki çerçeveyi kendi pazarınızın güncel verisiyle tamamlayın.

## Temel fikir

**İki model.**

- **Çevrim içi market** (*e-grocery*): Zincir marketlerin ya da çevrim içi oyuncuların, genellikle belirli bir zaman aralığında teslim ettiği siparişler. Sepetler daha büyük, teslimat süresi daha uzundur.
- **Hızlı ticaret** (*quick commerce*): Şehir içindeki küçük depolardan dakikalar içinde teslimat. Ürün yelpazesi dar, sepetler küçük, teslimat maliyeti sepete göre yüksektir.

**Sepet ekonomisi.** Fiziksel mağazada toplama ve taşıma işini tüketici yapar. Çevrim içi kanalda bu işi platform yapar ve her siparişe toplama, paketleme, teslimat ve ödeme işlem maliyeti eklenir. Coughlan ve arkadaşlarının kanal işlevleri yaklaşımıyla bakarsanız, işlevler tüketiciden platforma geçmiştir ve birinin bunun maliyetini taşıması gerekir. Bu yüzden **sepet büyüklüğü** (*basket size*), kanalın kârlılığını belirleyen en önemli değişkendir.

**Üretici için anlamı.** Platformlar marjlarını korumak için üreticiden şunları isteyebilir:

- Görünürlük ve reklam ödemeleri (perakende medya).
- Kanala özel promosyonlar.
- İyi ürün görselleri, açıklamalar ve doğru ana veri.
- Yüksek stok sürekliliği; çevrim içi stoksuzluk müşteriyi hemen rakibe yönlendirir.

**Üretici açısından yönetilecek konular.** Çevrim içi kanalda rafın yerini arama sonucu ve kategori sayfası alır. Ürün görselleri, başlıklar ve açıklamalar alışverişçinin ürünü bulup seçmesini doğrudan etkiler; bunların platformlara doğru ve güncel aktarılması bir iş süreci olarak yönetilmelidir. Stoksuzluk çevrim içi kanalda daha görünürdür, çünkü alışverişçi tek tıkla rakip ürüne geçebilir. Hızlı teslimat uygulamalarında küçük depolar sınırlı ürün çeşidi taşır; bu nedenle hangi ürünlerinizin listede olacağı ayrı bir pazarlık konusudur. Platformların reklam ve görünürlük ücretleri, ticari harcamanın bir parçası olarak diğer kanallarla aynı ölçütlerle değerlendirilmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Sepet tutarları, marj ve maliyetler varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b3.py` ile yapılmıştır.

Bir platformun brüt marjı %25. Sipariş başına toplama 25 TL, teslimat 45 TL, paketleme 5 TL; ödeme işlem maliyeti sepetin %1,5'i.

| Sepet | Brüt marj | Sipariş maliyeti | Katkı |
|---|---|---|---|
| 400 TL | 100,00 TL | 81,00 TL | 19,00 TL |
| 250 TL | 62,50 TL | 78,75 TL | −16,25 TL |

Başabaş sepet yaklaşık **319,15 TL**. Bu yüzden platformlar asgari sepet tutarı, teslimat ücreti ya da sepeti büyüten promosyonlar uygular. Üretici olarak sepeti büyüten çoklu paketler ve tamamlayıcı ürün paketleri önermek, platformla ilişkinizi güçlendirebilir.

## Sık yapılan hatalar

- **Çevrim içi kanala mağazadaki ürün sayfasını kopyalamak.** Küçük ekranda okunmayan ambalaj görseli tıklanmaz.
- **Stoğu kanala göre ayırmamak.** Çevrim içi stoksuzluk arama sonuçlarında sizi geriye düşürebilir.
- **Kanal çatışmasını unutmak.** Platforma özel fiyat, fiziksel zincirlerle sorun çıkarabilir.

## Pratikte nasıl uygulanır?

- [ ] Ana platformlardaki ürün sayfalarınızı görsel, açıklama ve ana veri açısından kontrol edin.
- [ ] Kategorinizde arama yapıldığında hangi sırada çıktığınızı düzenli olarak izleyin.
- [ ] Platformlarla sepet büyüklüğünü artıran paket ve promosyonları konuşun.
- [ ] Çevrim içi satışları ve stok sürekliliğini ayrı bir rapor olarak takip edin.

## Daha fazlası

- Coughlan, A. T.; Anderson, E.; Stern, L. W.; El-Ansary, A. I. (2006). *Marketing Channels.* (kaynak doğrulanmadı)
- NielsenIQ (2026). *NielsenIQ.* https://www.nielseniq.com/
