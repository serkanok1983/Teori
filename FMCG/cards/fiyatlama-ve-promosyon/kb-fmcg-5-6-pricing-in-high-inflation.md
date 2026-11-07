---
id: kb-fmcg-5-6-pricing-in-high-inflation
title: "Yüksek enflasyonda fiyatlama: Gecikmenin maliyeti"
summary: "Maliyetler her ay artarken fiyatı yılda bir kez güncellemek, marjın sessizce erimesi demektir. Bu kart fiyat güncelleme sıklığının marja etkisini, nominal ile reel büyümeyi ve enflasyonda zincir ve dağıtıcıyla nasıl çalışılacağını anlatır."
course: fmcg
category: fiyatlama-ve-promosyon
tags: [fiyatlama, maliyet, finans, perakende]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: orta
source_lessons: [FMCG-5.6]
reading_minutes: 3
key_points:
  - "Maliyet her ay artarken fiyat sabit kaldıkça marj erir; güncelleme gecikmesi doğrudan kâr kaybıdır."
  - "Fiyat güncelleme sıklığı arttıkça dönem ortalaması marj hedefe yaklaşır."
  - "Yüksek enflasyonda nominal ciro artışı yanıltıcıdır; büyümeyi hacimle ya da enflasyondan arındırılmış ciroyla okuyun."
  - "Fiyat artışını zincire ve dağıtıcıya maliyet verisiyle ve önceden bildirmek pazarlığı kolaylaştırır."
glossary_terms: [katki-payi, net-satis]
related: [kb-fmcg-5-1-price-elasticity, kb-fmcg-5-3-price-pack-architecture, kb-fmcg-10-2-trade-terms, kb-fmcg-7-3-credit-collections-dso, kb-fmcg-2-6-price-volume-mix-variance]
sources:
  - title: "Principles of Corporate Finance"
    authors: "Brealey, R. A.; Myers, S. C.; Allen, F."
    year: 2020
    type: book
    verified: false
    note: "Kitap; baskı yılı kontrol edilmedi."
  - title: "New Empirical Generalizations on the Determinants of Price Elasticity"
    authors: "Bijmolt, T. H. A.; van Heerde, H. J.; Pieters, R. G. M."
    year: 2005
    type: article
    doi: "10.1509/jmkr.42.2.141.62296"
    url: "https://doi.org/10.1509/jmkr.42.2.141.62296"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Marketing Research 42(2), 141–156."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Yüksek enflasyon dönemlerinde fiyatlama, yılda bir yapılan bir iş olmaktan çıkar ve sürekli bir yönetim konusuna dönüşür. Bu kart, fiyat güncellemesini geciktirmenin marjınıza ne kadar mal olduğunu hesaplamanızı ve büyümeyi doğru okumanızı sağlar.

## Temel fikir

**Marj erimesi.** Fiyatı belirlediğiniz gün marjınız hedefte olabilir. Maliyet her ay arttıkça fiyat sabit kalırsa marj her ay biraz daha düşer. Güncelleme aralığı uzadıkça dönemin ortalama marjı hedeften o kadar uzaklaşır.

**Güncelleme sıklığı.** Fiyatı daha sık güncellemek marjı korur, ama maliyeti de vardır: fiyat listesi değişikliği, zincirlerle yeniden pazarlık, raf etiketleri, dağıtıcının sistem güncellemesi ve müşteri tepkisi. Doğru sıklık, enflasyon hızına ve bu maliyetlere göre belirlenir.

**Nominal ve reel.** Brealey, Myers ve Allen'ın kurumsal finans kitabı, nominal ve reel değerleri birbirinden ayırmanın önemini vurgular. Satış raporlarında da aynı ayrım gerekir. Ciro %45 artarken genel fiyat seviyesi %50 arttıysa reel olarak küçülmüş olabilirsiniz. Reel büyüme = (1 + nominal büyüme) / (1 + enflasyon) − 1. Büyümeyi ayrıca hacim (adet, kilogram) ile de izleyin.

**Esneklik değişebilir.** Bijmolt, van Heerde ve Pieters (2005), fiyat esnekliğinin ekonomik koşullar dahil birçok etkene göre değiştiğini inceler. Yüksek enflasyonda tüketicinin fiyat duyarlılığı artabilir ve mağaza markasına ya da küçük pakete kayış hızlanabilir.

**Uygulamada fiyat güncelleme süreci.** Sık fiyat güncellemesi, iyi bir süreç gerektirir. Maliyet ve kur değişimlerini izleyen bir gösterge seti, hangi eşik aşıldığında fiyatın gözden geçirileceğini belirleyen bir kural ve kararı kimin onaylayacağı baştan yazılmalıdır. Zincirlerle yapılan sözleşmelerde fiyat değişikliği için bildirim süreleri olabilir; bunlar takvime eklenmelidir. Fiyat listeleri ERP'de, dağıtıcı sistemlerinde ve SFA'da aynı anda güncellenmezse farklı kanallarda farklı fiyatlar oluşur. Son olarak, fiyat artışından sonra hacim, karma ve rakip fiyatları birkaç dönem izlenmeli; esnekliğin beklenenden farklı çıkması bir sonraki kararı değiştirmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Maliyet artışı ve fiyatlama kuralı varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b3.py` ile yapılmıştır.

Birim maliyetiniz her ay %3 artıyor (yıllık yaklaşık **%42,58**). Fiyatı her güncellemede maliyetin 1,25 katı olarak belirliyorsunuz; hedef brüt marj %20.

| Güncelleme sıklığı | 12 aylık ortalama brüt marj |
|---|---|
| Yılda bir | %5,39 |
| 6 ayda bir | %13,75 |
| 3 ayda bir | %17,58 |
| Her ay | %20,00 |

Yılda bir güncellemede ortalama marj hedefin dörtte birine iniyor. Nominal büyüme için de aynı dikkat gerekir: Ciro %45 arttı, enflasyon %50 ise reel büyüme **eksi %3,33**.

## Sık yapılan hatalar

- **Yıllık fiyat takvimine bağlı kalmak.** Enflasyon hızlandığında takvim de değişmelidir.
- **Maliyet artışını tek seferde yansıtmaya çalışmak.** Büyük ve geç artış, zincir ve tüketiciden sert tepki alır.
- **Nominal ciro hedefiyle yönetmek.** Hedef tutarken hacim düşüyor olabilir.
- **Vadeyi unutmak.** Uzun vadeli satışta tahsilat gününe kadar paranın değeri düşer; vade, fiyatın bir parçasıdır.

## Pratikte nasıl uygulanır?

- [ ] Ana maliyet kalemlerinizi aylık izleyin ve marj erimesini ürün bazında raporlayın.
- [ ] Enflasyon hızına göre bir fiyat güncelleme sıklığı belirleyin ve müşterilere önceden açıklayın.
- [ ] Fiyat artış taleplerini maliyet verisiyle destekleyin ve uygulama tarihini yazılı olarak bildirin.
- [ ] Satış performansını nominal ciro, reel ciro ve hacim olarak üç ayrı göstergeyle izleyin.
- [ ] Vade ve tahsilat koşullarını fiyat kararlarıyla birlikte değerlendirin.

## Daha fazlası

- Brealey, R. A.; Myers, S. C.; Allen, F. (2020). *Principles of Corporate Finance.* (kaynak doğrulanmadı)
- Bijmolt, T. H. A.; van Heerde, H. J.; Pieters, R. G. M. (2005). *New Empirical Generalizations on the Determinants of Price Elasticity.* Journal of Marketing Research 42(2), 141–156. https://doi.org/10.1509/jmkr.42.2.141.62296
