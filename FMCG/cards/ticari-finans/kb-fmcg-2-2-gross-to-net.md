---
id: kb-fmcg-2-2-gross-to-net
title: "Brütten nete (fiyat şelalesi): Liste fiyatından cep fiyatına"
summary: "Liste fiyatı ile şirketin gerçekte elde ettiği fiyat arasında fatura altı iskontolar, primler, promosyon destekleri ve sabit ücretler vardır. Bu kart fiyat şelalesini adım adım kurmayı ve sızıntıları bulmayı gösterir."
course: fmcg
category: ticari-finans
tags: [fiyatlama, promosyon, marj, zincir-market]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: orta
source_lessons: [FMCG-2.2]
reading_minutes: 3
key_points:
  - "Fiyat şelalesi, liste fiyatından başlayıp her indirim ve desteği düşerek cebe kalan net fiyata ulaşır."
  - "Fatura dışı kalemler (ciro primi, listeleme bedeli, promosyon desteği) görünmediği için en çok sızıntı buradadır."
  - "Sabit ücretleri adet başına çevirmek, müşteriler arasında gerçek fiyatı karşılaştırmanın tek yoludur."
  - "Brütten nete oranını müşteri ve ürün bazında izleyin; ortalama oran sorunlu müşteriyi gizler."
glossary_terms: [fiyat-selalesi, cep-fiyati, ciro-primi, ticari-harcama, net-satis]
related: [kb-fmcg-2-1-fmcg-pnl, kb-fmcg-10-2-trade-terms, kb-fmcg-5-5-trade-spend-roi, kb-ea-27-1-pricing-engine-conditions, kb-ea-27-2-tpm-promotion-settlement]
sources:
  - title: "Marketing Management"
    authors: "Kotler, P.; Keller, K. L."
    year: 2016
    type: book
    verified: false
    note: "Kitap; baskı yılı kontrol edilmedi."
  - title: "An Empirical Analysis of the Determinants of Retail Margins: The Role of Store-Brand Share"
    authors: "Ailawadi, K. L.; Harlam, B."
    year: 2004
    type: article
    doi: "10.1509/jmkg.68.1.147.24027"
    url: "https://doi.org/10.1509/jmkg.68.1.147.24027"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Marketing 68(1), 147–165."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Aynı ürünü iki farklı zincire aynı liste fiyatıyla satıyor olabilirsiniz. Ama biri yıl sonu primi, diğeri listeleme bedeli ve promosyon desteği aldığında cebinize kalan fiyat çok farklıdır. Bu kart, liste fiyatından gerçek net fiyata giden yolu, yani **fiyat şelalesini** (*price waterfall*) kurmayı gösterir. Ticari şart görüşmesi, müşteri kârlılık analizi ve fiyat artışı planlamasında kullanılır.

## Temel fikir

Şelale şu basamaklardan oluşur:

1. **Liste fiyatı:** Fiyat listesindeki birim fiyat.
2. **Fatura altı iskonto** (*on-invoice*): Faturada görünen, kalıcı veya kampanyalı indirimler.
3. **Fatura fiyatı:** Müşterinin faturada ödediği fiyat.
4. **Fatura dışı indirimler** (*off-invoice*): Ciro primi, hacim primi, erken ödeme iskontosu, promosyon desteği, teşhir ve broşür bedeli.
5. **Sabit ücretler:** Listeleme, açılış, raf kiralama gibi bir defalık veya dönemsel bedeller.
6. **Cep fiyatı** (*pocket price*): Tüm bunlardan sonra şirkete kalan birim fiyat.

**Neden önemli?** Fatura fiyatı satış sisteminde görünür, ama fatura dışı kalemler çoğu zaman finans tarafında, dönem sonunda ve toplu hâlde kaydedilir. Satış ekibi faturaya bakıp kârlı bir anlaşma yaptığını düşünürken cep fiyatı beklenenden düşük olabilir. Fiyat şelalesi bu görünmeyen kısmı ortaya çıkarır.

**Sabit ücretleri adetlendirin.** 180.000 TL'lik listeleme bedeli tek başına anlamsızdır; o müşteriye yılda kaç adet sattığınıza bölündüğünde gerçek fiyat etkisi görünür.

**Karşı tarafın marjı.** Perakendeci de kendi marjını yönetir. Ailawadi ve Harlam (2004), perakende marjlarını belirleyen etkenleri ve mağaza markası payının bu marjlardaki rolünü inceler. Pazarlıkta zincirin marj kaygısını anlamak, şelalenin hangi basamağının esneyebileceğini görmenizi kolaylaştırır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek bir anlaşmaya ait değildir; hesaplar `scripts/cards_numbers_fmcg_b1.py` ile yapılmıştır.

Bir zincirle yıllık anlaşma: liste fiyatı 100,00 TL, %8 fatura altı iskonto, fatura tutarı üzerinden %3 ciro primi, adet başına 2,50 TL promosyon desteği ve 180.000 TL listeleme bedeli. Yıllık satış 120.000 adet.

| Basamak | TL/adet |
|---|---|
| Liste fiyatı | 100,00 |
| Fatura altı iskonto (%8) | −8,00 |
| **Fatura fiyatı** | **92,00** |
| Ciro primi (%3 × 92,00) | −2,76 |
| Promosyon desteği | −2,50 |
| Listeleme bedeli (180.000 ÷ 120.000) | −1,50 |
| **Cep fiyatı** | **85,24** |

Brütten nete oranı **%14,76**. Satış ekibi faturada %8 indirim gördü, ama gerçekte neredeyse iki katı verildi. Satış 120.000 adetin altında kalırsa listeleme bedelinin adet payı yükselir ve cep fiyatı daha da düşer.

## Sık yapılan hatalar

- Müşteri kârlılığını fatura fiyatıyla hesaplamak.
- Yüzde primleri hangi taban üzerinden (liste mi, fatura mı) hesaplandığını yazmadan anlaşmaya koymak.
- Sabit ücretleri adete çevirmemek; küçük müşterideki yüksek etkiyi görmemek.
- Promosyon desteklerini tahakkuk etmeden, ödendiği dönemde kaydetmek; bu ayları karşılaştırılamaz yapar.
- Fiyat artışında liste fiyatını artırıp fatura dışı kalemleri aynı oranda büyütmek.

## Pratikte nasıl uygulanır?

- [ ] İlk 10 müşteriniz ve ilk 10 ürününüz için yukarıdaki gibi bir şelale tablosu kurun.
- [ ] Her yüzde primin tabanını (liste, fatura, net) sözleşmede açıkça yazın.
- [ ] Sabit ücretleri beklenen yıllık adede bölerek adet başı etkiyi raporlayın.
- [ ] Brütten nete oranını müşteri bazında sıralayın; ortalamanın çok üzerindekileri inceleyin.
- [ ] Fiyatlama ve promosyon sisteminizde (ERP, TPM) fatura dışı kalemlerin müşteri ve ürün bazında tahakkuk edildiğinden emin olun.

## Daha fazlası

- Kotler, P.; Keller, K. L. (2016). *Marketing Management.* (kaynak doğrulanmadı)
- Ailawadi, K. L.; Harlam, B. (2004). *An Empirical Analysis of the Determinants of Retail Margins: The Role of Store-Brand Share.* Journal of Marketing 68(1), 147–165. https://doi.org/10.1509/jmkg.68.1.147.24027
