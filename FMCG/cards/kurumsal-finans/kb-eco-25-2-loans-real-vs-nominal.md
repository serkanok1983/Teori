---
id: kb-eco-25-2-loans-real-vs-nominal
title: "Kredi seçimi: TL mi döviz mi, nominal mi reel maliyet mi?"
summary: "TL ve döviz kredilerinin gerçek maliyetini kur beklentisiyle karşılaştırmayı, kredinin reel maliyetini hesaplamayı, eşit taksitli kredinin toplam faiz yükünü ve aylık faizin yıllık bileşik karşılığını anlatır."
course: eco
category: kurumsal-finans
tags: [finansman, kredi, faiz, kur]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: temel
source_lessons: [ECO-25.2]
reading_minutes: 3
key_points:
  - "Döviz kredisinin TL cinsinden maliyeti, döviz faizi ile kur artışının birleşimidir."
  - "TL ve döviz kredisi maliyetinin eşitlendiği kur artışını (başabaş kur) hesaplayın."
  - "Kredinin reel maliyeti, nominal faizin enflasyondan arındırılmış hâlidir."
  - "Aylık faizin 12 ile çarpılması, yıllık bileşik maliyeti olduğundan düşük gösterir."
  - "Kredi kararını faiz oranına değil, toplam maliyete ve geri ödeme kaynağının para birimine göre verin."
glossary_terms: [efektif-faiz, reel-faiz, kur-riski]
related: [kb-eco-18-3-real-vs-nominal-interest-fisher, kb-eco-23-2-currency-crises-business, kb-eco-50-3-working-with-banks, kb-eco-50-4-tcmb-policy-rate-credit]
sources:
  - title: "Principles of Finance"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-finance/pages/1-why-it-matters"
    verified: true
    checked_on: 2026-10-28
  - title: "Bankacılık Düzenleme ve Denetleme Kurumu (resmî site)"
    authors: "BDDK"
    year: 2026
    type: web
    url: "https://www.bddk.org.tr"
    verified: true
    checked_on: 2026-10-28
  - title: "Türkiye Bankalar Birliği (resmî site)"
    authors: "TBB"
    year: 2026
    type: web
    url: "https://www.tbb.org.tr"
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

Banka size iki teklif getiriyor: yüksek faizli TL kredisi ve düşük faizli döviz kredisi. Ya da aylık faiz oranıyla eşit taksitli bir kredi. Bu kart, teklifleri gerçek maliyetleri üzerinden karşılaştırmanızı sağlar.

## Temel fikir

**Döviz kredisinin TL maliyeti:** Kredi dövizle geri ödenir; TL ile kazanıyorsanız kur artışı maliyete eklenir:

TL cinsinden maliyet = (1 + döviz faizi) × (1 + kur artışı) − 1

**Başabaş kur artışı:** (1 + TL faizi) / (1 + döviz faizi) − 1. Kur bundan az artarsa döviz kredisi, fazla artarsa TL kredisi ucuz kalır. Kur beklentisi belirsiz olduğundan, kararı yalnızca beklenen değere göre değil, kötü senaryodaki kayba göre de verin.

**Reel maliyet:** (1 + nominal faiz) / (1 + enflasyon) − 1. Satış fiyatlarınız enflasyonla artıyorsa, sizin için önemli olan reel maliyettir.

**Aylık ve yıllık faiz:** Bankalar çoğu zaman aylık faiz söyler. Yıllık bileşik karşılığı (1 + aylık)¹² − 1'dir; basit çarpım bundan düşüktür. Kredi tekliflerini karşılaştırırken faize ek olarak dosya masrafı, sigorta ve vergi gibi tüm kalemleri içeren **efektif maliyete** bakın.

### Kredi türünü seçmek

- **Rotatif kredi:** Limit içinde kullanıp geri ödeyebildiğiniz esnek kredi. Mevsimsel işletme sermayesi ihtiyacı için uygundur, ama faiz genellikle değişkendir.
- **Spot kredi:** Belirli bir süre için tek seferlik kullanılır. Vadesi kısa olduğundan sürekli yenileme riski taşır.
- **Taksitli ticari kredi:** Yatırım veya kalıcı işletme sermayesi ihtiyacı için. Ödeme planı nakit akışınıza uygun olmalıdır.
- **Dövize endeksli veya döviz kredisi:** Ancak döviz geliri veya korunma imkânı varsa düşünülmelidir. Türkiye'de döviz kredisi kullanımı, işletmenin döviz geliri ve büyüklüğü gibi koşullara bağlanmış olabilir; güncel kuralları bankanızla kontrol edin.

### Sabit mi, değişken mi?

Faizlerin düşmesi bekleniyorsa değişken faiz, yükselmesi bekleniyorsa sabit faiz avantajlı görünür. Ancak faiz tahmini yapmak zordur. Kararı tahmine değil, şirketin faiz artışına dayanma gücüne göre verin: Faiz giderindeki ani bir artış kârınızı ortadan kaldırıyorsa, sabit faizin getirdiği öngörülebilirlik bir sigorta gibi değerlidir.

### Erken kapama

Faizler düştüğünde krediyi erken kapatıp yeniden finanse etmek isteyebilirsiniz. Sözleşmedeki erken ödeme koşullarını ve ücretlerini kredi kullanmadan önce okuyun.

## Bir örnek

> **Örnek (temsili rakamlar):** Faiz, kur ve enflasyon oranları varsayımsaldır; güncel kredi koşullarını yansıtmaz. Hesaplar `scripts/cards_numbers_eco_b3.py` ile yapılmıştır.

**TL mi döviz mi?** TL kredisi yıllık %50, dolar kredisi %9. Kurun bir yılda %35 artacağı varsayılıyor.

- Dolar kredisinin TL maliyeti = 1,09 × 1,35 − 1 = **%47,15**.
- Başabaş kur artışı **%37,6**. Kur bundan fazla artarsa döviz kredisi daha pahalı olur.
- Enflasyon %35 ise reel maliyet TL kredisinde %11,11, dolar kredisinde %9,00. Fark küçük ama döviz kredisi kur riskini de taşır.

**Eşit taksitli kredi:** 10.000.000 TL, aylık %3,5, 12 ay.

- Aylık taksit **1.034.839 TL**; toplam ödeme 12.418.074 TL, toplam faiz 2.418.074 TL.
- Aylık %3,5 faiz basit çarpımla %42 görünür; yıllık bileşik karşılığı **%51,1**.

## Sık yapılan hatalar

- Döviz kredisini düşük faizi nedeniyle seçip kur riskini hesaba katmamak.
- Aylık faizi 12 ile çarparak yıllık maliyeti olduğundan düşük hesaplamak.
- Masraf, komisyon ve sigortaları maliyete eklememek.
- Kısa vadeli işletme sermayesi ihtiyacını uzun vadeli yatırım kredisiyle (ya da tersi) finanse etmek.
- Değişken faizli kredide faiz artış senaryosunu düşünmemek.

## Pratikte nasıl uygulanır?

- [ ] Tüm kredi tekliflerini yıllık bileşik efektif maliyet üzerinden aynı tabloda karşılaştırın.
- [ ] Döviz kredisi tekliflerinde başabaş kur artışını hesaplayın ve kötü bir kur senaryosuyla test edin.
- [ ] Geliriniz TL ise borcunuzun büyük kısmını TL tutun ya da kur riskini korunma araçlarıyla sınırlayın.
- [ ] Kredi vadesini, finanse ettiğiniz varlığın ömrü ve nakit döngüsüyle eşleştirin.
- [ ] Teklifleri değerlendirirken bankanızdan masraf ve vergileri içeren ödeme planını yazılı isteyin.

## Daha fazlası

- OpenStax (2026). *Principles of Finance*. https://openstax.org/books/principles-finance/pages/1-why-it-matters
- BDDK (2026). *Bankacılık Düzenleme ve Denetleme Kurumu (resmî site)*. https://www.bddk.org.tr
- TBB (2026). *Türkiye Bankalar Birliği (resmî site)*. https://www.tbb.org.tr
