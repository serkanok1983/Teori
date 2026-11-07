---
id: kb-fmcg-5-3-price-pack-architecture
title: "Fiyat-paket mimarisi: Doğru boyut, doğru fiyat, doğru kanal"
summary: "Fiyat-paket mimarisi, hangi ambalaj boyutunu hangi fiyat noktasında ve hangi kanalda satacağınızı planlamaktır. Bu kart birim fiyat merdivenini, gramaj küçültmenin gerçek etkisini ve kanal bazlı paket kararlarını anlatır."
course: fmcg
category: fiyatlama-ve-promosyon
tags: [fiyatlama, portfoy, perakende]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: orta
source_lessons: [FMCG-5.3]
reading_minutes: 3
key_points:
  - "Paket boyutları bir fiyat merdiveni oluşturur; büyük paketin kilogram fiyatı genellikle daha düşüktür."
  - "Merdivende basamaklar arasındaki fark, tüketiciyi büyük pakete yönlendirmeli ama küçük paketi anlamsız kılmamalıdır."
  - "Aynı fiyatla gramajı küçültmek gizli bir birim fiyat artışıdır; tüketici ve mevzuat açısından dikkat ister."
  - "Kanala göre farklı paketler, aynı ürünün farklı alıcı ihtiyaçlarına uymasını sağlar."
glossary_terms: [fiyat-paket-mimarisi, birim-fiyat]
related: [kb-fmcg-5-1-price-elasticity, kb-fmcg-5-6-pricing-in-high-inflation, kb-fmcg-5-7-rgm-system, kb-fmcg-6-1-rtm-channels-formats, kb-fmcg-4-4-portfolio-management]
sources:
  - title: "Marketing Management"
    authors: "Kotler, P.; Keller, K. L."
    year: 2016
    type: book
    verified: false
    note: "Kitap; baskı yılı kontrol edilmedi."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Fiyatı artırmak zor olduğunda üreticiler çoğu zaman paket boyutunu değiştirir. Bakkal için küçük paket, indirim marketi için tek bir orta boy, toptancı için büyük ambalaj gibi kararlar da aynı mantığın parçasıdır. Bu kart, fiyat-paket mimarisini (*price pack architecture*) sistemli kurmanıza yardım eder.

## Temel fikir

**Fiyat merdiveni.** Bir ürünün farklı boyutları, birim fiyat (*unit price*) açısından bir merdiven oluşturur. Tüketici büyük paketi alırken kilogram başına daha az öder; üretici de daha az ambalaj ve elleçleme maliyetiyle daha fazla hacim satar. Merdiven tasarlanırken iki şey dengelenir:

- Basamaklar arasındaki birim fiyat farkı, tüketiciyi büyük pakete geçmeye teşvik edecek kadar belirgin olmalıdır.
- Küçük paket de anlamlı kalmalıdır: Bütçesi kısıtlı ya da deneme yapan alıcı için giriş fiyat noktasıdır.

**Fiyat noktaları.** Tüketicinin aklındaki eşikler, örneğin yuvarlak rakamlar, paket kararlarını etkiler. Bir paketi kritik bir fiyat noktasının altında tutmak için gramaj ayarlanabilir.

**Gramaj küçültme.** Fiyatı aynı tutup içeriği azaltmak, tüketicinin fark etmeyebileceği bir birim fiyat artışıdır. Kısa vadede hacim kaybını sınırlayabilir. Ancak tüketici fark ettiğinde güven kaybı yaşanabilir. Etiket ve birim fiyat gösterimi kurallarına uyum için güncel mevzuatı ilgili uzmanınızla kontrol edin.

**Kanal ve paket.** Kotler ve Keller'ın da vurguladığı gibi ürün ve fiyat kararları hedef müşteriye göre şekillenir. Hızlı tüketimde bu, kanala göre paket demektir: Bakkalda küçük ve tek kullanımlık, zincir markette aile boyu, toptancıda koli ya da büyük ambalaj. Kanallar arasında aynı paketin çok farklı fiyatlarla satılması kanal çatışmasına yol açabilir; farklı paketler bu çatışmayı azaltabilir.

**Mimarinin bakımı.** Fiyat-paket mimarisi bir kez kurulup bırakılmamalıdır. Hammadde maliyetleri, rakip paketleri ve kanal yapısı değiştikçe boylar arasındaki birim fiyat farkları bozulabilir. Yılda en az bir kez bütün paketlerin birim fiyatlarını, kanal bazlı satış paylarını ve kârlılıklarını tek bir tabloda gözden geçirmek, çakışan ya da boşlukta kalan paketleri gösterir.

## Bir örnek

> **Örnek (temsili rakamlar):** Fiyatlar varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b2.py` ile yapılmıştır.

| Paket | Raf fiyatı | Kilogram fiyatı |
|---|---|---|
| 500 g | 45,00 TL | 90,00 TL |
| 1 kg | 82,00 TL | 82,00 TL |
| 2 kg | 150,00 TL | 75,00 TL |

Merdiven düzgün: Her büyük basamak kilogram başına daha ucuz.

Maliyetler arttı ve 1 kg paketi aynı fiyatla 900 g'a indirmeyi düşünüyorsunuz. Yeni kilogram fiyatı 82 / 0,9 = 91,11 TL olur. Bu, **%11,11'lik** bir birim fiyat artışıdır. Üstelik 900 g'ın kilogram fiyatı artık 500 g paketten daha yüksek; merdiven bozulur ve dikkatli tüketici küçük pakete kayabilir.

## Sık yapılan hatalar

- **Merdiveni ters çevirmek.** Büyük paketin birim fiyatı küçükten yüksek olursa tüketici bunu fark eder ve güven kaybedersiniz.
- **Her kanala aynı paketi vermek.** Bakkal müşterisinin ihtiyacı ile zincir market müşterisininki farklıdır.
- **Çok fazla boyut.** Her yeni boyut bir SKU daha, yani daha fazla karmaşıklık demektir.
- **Gramaj küçültmeyi tek başına çözüm sanmak.** Tekrarlandıkça fark edilir ve markaya zarar verebilir.

## Pratikte nasıl uygulanır?

- [ ] Her ürün için paket boyutlarını, raf fiyatlarını ve birim fiyatları tek tabloda gösterin.
- [ ] Merdivenin her basamakta düzgün indiğini kontrol edin.
- [ ] Kanal başına hangi paketin ana paket olacağını belirleyin.
- [ ] Gramaj değişikliği planlıyorsanız yeni birim fiyatı hesaplayın ve merdivende nereye oturduğuna bakın.
- [ ] Rakiplerin paket ve birim fiyatlarını da aynı tabloya ekleyin.

## Daha fazlası

- Kotler, P.; Keller, K. L. (2016). *Marketing Management.* (kaynak doğrulanmadı)
