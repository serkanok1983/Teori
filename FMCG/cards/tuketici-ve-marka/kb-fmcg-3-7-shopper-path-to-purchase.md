---
id: kb-fmcg-3-7-shopper-path-to-purchase
title: "Alışveriş yolculuğu: Tüketiciyi alıcıya çeviren adımlar"
summary: "Tüketici markanızı bilmekten tekrar almaya kadar birkaç adımdan geçer ve her adımda bir kısmı kaybolur. Bu kart yolculuğu bir huni olarak okumayı, en büyük kaybın nerede olduğunu bulmayı ve sahada hangi adımı düzeltebileceğinizi anlatır."
course: fmcg
category: tuketici-ve-marka
tags: [tuketici, saha-satis, perakende, dagitim]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, saha-satis-temsilcisi]
level: temel
source_lessons: [FMCG-3.7]
reading_minutes: 3
key_points:
  - "Alışveriş yolculuğunu bilinirlik, değerlendirme, mağazada bulma, rafta seçme ve tekrar alma gibi adımlara ayırmak sorunun yerini gösterir."
  - "Adımlar çarpımsal çalışır; zayıf bir adım, diğerlerinin iyi olmasını boşa çıkarır."
  - "Saha ekibinin en doğrudan etkilediği adımlar mağazada bulma ve rafta seçmedir."
  - "Tüketici (kullanan) ile alıcı (mağazada satın alan) aynı kişi olmayabilir; ikisini ayrı düşünmek gerekir."
glossary_terms: [alisveris-yolculugu, donusum-orani, raf-bulunurlugu]
related: [kb-fmcg-3-1-consumer-decisions, kb-fmcg-3-4-mental-physical-availability, kb-fmcg-9-5-perfect-store, kb-fmcg-9-4-osa-out-of-stock, kb-fmcg-13-8-sales-funnel-math]
sources:
  - title: "The Interplay among Category Characteristics, Customer Characteristics, and Customer Activities on In-Store Decision Making"
    authors: "Inman, J. J.; Winer, R. S.; Ferraro, R."
    year: 2009
    type: article
    doi: "10.1509/jmkg.73.5.19"
    url: "https://doi.org/10.1509/jmkg.73.5.19"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Marketing 73(5), 19–29."
  - title: "Kantar"
    authors: "Kantar"
    year: 2026
    type: web
    url: "https://www.kantar.com/"
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

Satış düştüğünde pazarlama "reklam az", satış "fiyat yüksek", zincir "ürün dönmüyor" der. Alışveriş yolculuğunu (*path to purchase*) adım adım ölçmek, tartışmayı görüşten veriye taşır ve kaybın en büyük olduğu adımı gösterir.

## Temel fikir

**Tüketici ve alıcı.** Hızlı tüketimde ürünü kullanan kişi ile mağazada alan kişi farklı olabilir. Çocuk bisküvisini çocuk yer, anne ya da baba alır. Mağazadaki kararı veren kişiye **alıcı** (*shopper*) denir. Raf, fiyat etiketi ve promosyon alıcıya konuşur.

**Yolculuğun adımları.** Kategoriye göre değişse de tipik bir sıra şöyledir:

1. **Bilinirlik:** Alıcı markayı biliyor mu?
2. **Değerlendirme:** İhtiyaç anında markayı seçenekler arasına alıyor mu?
3. **Mağazada bulma:** Gittiği mağazada ürün var mı ve kolay bulunuyor mu?
4. **Rafta seçme:** Raf önünde rakip yerine sizi seçiyor mu?
5. **Tekrar alma:** Kullandıktan sonra yeniden alıyor mu?

Her adımın **dönüşüm oranı** (*conversion rate*), bir önceki adımdan geçenlerin ne kadarının bu adımı da geçtiğini gösterir. Adımlar çarpımsal çalıştığı için zayıf bir adım bütün sonucu aşağı çeker.

**Kararın bir kısmı mağazada.** Inman, Winer ve Ferraro (2009), mağaza içinde planlanmamış alımların kategori, müşteri ve mağaza içi davranışla ilişkisini inceler. Bu tür çalışmalar, raf önündeki adımın küçümsenmemesi gerektiğini gösterir. Kantar gibi tüketici paneli sağlayıcıları da bu adımları ölçmeye yarayan veriler sunar.

**Yolculuğu araştırmak.** Alışveriş yolculuğunu anlamak için farklı yöntemler birlikte kullanılabilir: alışveriş sonrası anketler, mağaza içi gözlem, sepet ve sadakat kartı verileri, çevrim içi arama ve tıklama verileri. Her yöntem yolculuğun farklı bir kısmını gösterir; örneğin anketler niyeti, sepet verisi gerçekleşen davranışı ölçer. Kategoriye göre öncelikli soruları belirleyin: Alışverişçi kategoriye mağazaya girmeden mi karar veriyor, rafta mı? Marka mı, boy mu, fiyat mı önce seçiliyor? Bu soruların yanıtı, bütçenin medya, mağaza içi iletişim ve raf düzeni arasında nasıl dağıtılacağını belirler.

## Bir örnek

> **Örnek (temsili rakamlar):** Oranlar varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b2.py` ile yapılmıştır.

Bir bölgede kategoriyi alan 10.000 hane düşünün.

| Adım | Dönüşüm | Kalan hane |
|---|---|---|
| Bilinirlik | %80 | 8.000 |
| Değerlendirme | %50 | 4.000 |
| Mağazada bulma | %70 | 2.800 |
| Rafta seçme | %60 | 1.680 |
| Tekrar alma | %45 | 756 |

Satış ekibi bulunurluk ve raf yerleşimi çalışmasıyla "mağazada bulma" oranını %70'ten %85'e çıkarırsa, ilk alım yapan hane sayısı **1.680'den 2.040'a** çıkar. Bu, reklamla bilinirliği artırmaktan çok daha ucuz bir yol olabilir.

## Sık yapılan hatalar

- **Tek bir adıma odaklanmak.** Bilinirliği yükseltmek, ürün rafta yoksa satışa dönmez.
- **Tüketiciyle alıcıyı karıştırmak.** Reklam kullanana, raf malzemesi alıcıya konuşmalıdır.
- **Oranları kanal ayrımı yapmadan okumak.** Zincir marketle bakkalda dönüşüm oranları çok farklı olabilir.
- **Tekrar almayı ihmal etmek.** İlk alımı artıran promosyon, ürün beklentiyi karşılamıyorsa kalıcı büyüme getirmez.

## Pratikte nasıl uygulanır?

- [ ] Kategorinize uygun adımları tanımlayın ve her biri için bir ölçü seçin: anket, panel, saha ziyaret kaydı ya da satış verisi.
- [ ] Adımları kanal bazında hesaplayın ve en büyük kaybın nerede olduğunu bulun.
- [ ] Saha ekibinin etkileyebileceği adımlar (bulma, seçme) için somut hedefler koyun: rafta bulunurluk, raf payı, fiyat etiketi.
- [ ] Her iyileştirmenin kaç alıcı getirdiğini yukarıdaki gibi hesaplayıp maliyetiyle karşılaştırın.
- [ ] Ölçümü her çeyrek tekrarlayın ve iyileştirmenin hangi adımı gerçekten değiştirdiğini kontrol edin.

## Daha fazlası

- Inman, J. J.; Winer, R. S.; Ferraro, R. (2009). *The Interplay among Category Characteristics, Customer Characteristics, and Customer Activities on In-Store Decision Making.* Journal of Marketing 73(5), 19–29. https://doi.org/10.1509/jmkg.73.5.19
- Kantar (2026). *Kantar.* https://www.kantar.com/
