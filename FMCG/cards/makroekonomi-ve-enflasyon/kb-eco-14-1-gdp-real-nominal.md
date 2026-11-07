---
id: kb-eco-14-1-gdp-real-nominal
title: "GSYH, reel büyüme ve iş döngüsü: Makro veriyi satış planına çevirmek"
summary: "Gayrisafi yurt içi hasılanın ne ölçtüğünü, nominal ve reel büyümenin farkını, iş döngüsünün dağıtım ve üretim talebine etkisini ve kendi büyümenizi ekonomiyle nasıl kıyaslayacağınızı anlatır."
course: eco
category: makroekonomi-ve-enflasyon
tags: [makroekonomi, planlama, buyume]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: temel
source_lessons: [ECO-14.1, ECO-14.3]
reading_minutes: 3
key_points:
  - "GSYH, bir ülkede belli bir dönemde üretilen nihai mal ve hizmetlerin toplam değeridir."
  - "Nominal GSYH fiyat artışını da içerir; büyümeyi değerlendirmek için reel GSYH'ye bakın."
  - "Ekonomi daralırken temel gıda ve temizlik daha az, dayanıklı ve lüks ürünler daha çok etkilenir."
  - "Kendi reel hacim büyümenizi ekonominin ve sektörün reel büyümesiyle kıyaslayarak pay kazanıp kaybettiğinizi görün."
glossary_terms: [gsyh, reel-buyume, deflator]
related: [kb-eco-2-5-growth-rates-and-logs, kb-eco-14-2-inflation-measurement-tufe-ufe, kb-eco-21-1-monetary-policy-tcmb, kb-fmcg-13-16-sales-forecasting]
sources:
  - title: "Türkiye İstatistik Kurumu (resmî site)"
    authors: "TÜİK"
    year: 2026
    type: web
    url: "https://www.tuik.gov.tr"
    verified: true
    checked_on: 2026-10-28
  - title: "The Economy 2.0"
    authors: "CORE Econ"
    year: 2026
    type: web
    url: "https://www.core-econ.org/the-economy/"
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

Yıllık bütçeyi hazırlarken "ekonomi büyüyecek mi, daralacak mı?" sorusu, hacim hedefini, stok seviyesini ve işe alım planını doğrudan etkiler. Bu kart, açıklanan büyüme verilerini doğru okumanızı ve kendi performansınızı ekonomiyle karşılaştırmanızı sağlar.

## Temel fikir

**Gayrisafi yurt içi hasıla** (*GDP*, GSYH), bir ülkede belli bir dönemde üretilen nihai mal ve hizmetlerin piyasa değeridir. Üç yoldan ölçülebilir: üretim (sektörlerin katma değeri), harcama (tüketim + yatırım + kamu harcaması + net ihracat) ve gelir. Türkiye'de resmî veriyi TÜİK çeyreklik olarak yayımlar.

- **Nominal GSYH** cari fiyatlarla hesaplanır; hem üretim artışını hem fiyat artışını içerir.
- **Reel GSYH** sabit fiyatlarla hesaplanır; yalnızca miktar değişimini gösterir. Büyüme denince genellikle reel GSYH'nin değişimi kastedilir.
- **GSYH deflatörü** (*GDP deflator*), nominal ile reel GSYH arasındaki oran; ekonomideki genel fiyat düzeyini gösterir.

**İş döngüsü:** Ekonomi genişleme ve daralma dönemlerinden geçer. Harcama tarafında tüketim çoğu ülkede en büyük kalemdir; bu yüzden hane gelirindeki değişim hızlı tüketim ürünleri talebine yansır. Ancak tepki ürünlere göre farklıdır: temel gıda ve temizlik ürünleri daralmaya daha dayanıklıdır, premium ürünler ve dayanıklı mallar daha hassastır. Daralmada tüketici küçük ambalaja, özel markaya ve indirim kanallarına kayar.

### Veriyi nereden ve nasıl izlersiniz?

GSYH verileri Türkiye'de TÜİK tarafından çeyreklik olarak yayımlanır. İlk açıklanan rakamlar sonradan revize edilebilir; bu yüzden tek bir açıklamaya göre büyük karar vermek yerine eğilime bakın.

Haber ve raporlarda üç farklı büyüme ölçüsüne rastlarsınız:

- **Yıllık büyüme:** Bu çeyreğin geçen yılın aynı çeyreğine göre değişimi. Mevsimsellikten etkilenmez ama dönüm noktalarını geç gösterir.
- **Çeyreklik büyüme:** Mevsim ve takvim etkilerinden arındırılmış veriyle bir önceki çeyreğe göre değişim. Ekonominin yön değiştirdiğini daha erken gösterir.
- **Yıllık toplam:** Son dört çeyreğin toplamı; en dengeli ama en gecikmeli göstergedir.

### Kendi işinizle bağlantı

Kendi satış miktarınızı reel GSYH ve özellikle hanehalkı tüketimiyle karşılaştırın. Satışlarınız ekonomiden daha hızlı büyüyorsa pazar payı kazanıyor olabilirsiniz; daha yavaşsa pazar payı kaybediyor olabilirsiniz. Gıda ve temel tüketim ürünleri ekonomik dalgalanmalardan daha az etkilenirken, dayanıklı tüketim malları ve yatırım malları çok daha sert dalgalanır. Hangi grupta olduğunuzu bilmek, bütçe senaryolarınızı gerçekçi kurmanızı sağlar.

## Bir örnek

> **Örnek (temsili rakamlar):** Endeks değerleri ve büyüme oranları varsayımsaldır; gerçek GSYH verisi değildir. Hesaplar `scripts/cards_numbers_eco_b2.py` ile yapılmıştır.

**Nominalden reele.** Bir yılda nominal GSYH %60, deflatör %45 artmış. Reel büyüme = 1,60 / 1,45 − 1 = **%10,34**. Haberlerdeki büyük nominal rakam, reel olarak çok daha küçüktür.

**Kendinizi kıyaslamak.** Bir distribütörün koli bazında reel hacim büyümesi %6, ekonominin reel büyümesi %3. Ekonomiye göre görece büyüme 1,06 / 1,03 − 1 = **%2,91**. Daha doğru kıyas için ekonomi yerine kendi kategorinizin pazar büyümesini (perakende paneli veya üretici verisi) kullanın.

## Sık yapılan hatalar

- Nominal büyüme rakamlarını reel büyüme gibi yorumlamak.
- Yalnızca yıllık büyümeye bakıp çeyrekler arası ivme kaybını kaçırmak.
- İlk açıklanan verinin sonradan revize edilebileceğini unutmak.
- Ekonominin genel büyümesini her ürün grubuna aynı oranda uygulamak.
- Daralma dönemlerinde premium ürün stoklarını aynı seviyede tutmak.

## Pratikte nasıl uygulanır?

- [ ] Bütçe varsayımlarına ekonomik büyüme için en az iki senaryo (büyüme ve daralma) yazın.
- [ ] Ürün portföyünüzü daralmaya dayanıklı ve hassas gruplara ayırın; her senaryoda hacim etkisini ayrı tahmin edin.
- [ ] TÜİK'in çeyreklik büyüme açıklamalarında harcama kalemlerine (özellikle hane tüketimi) bakın.
- [ ] Kendi reel hacim büyümenizi kategori ve ekonomi büyümesiyle her çeyrek kıyaslayın.
- [ ] Daralma işaretlerinde (tüketim yavaşlaması, kredi daralması) küçük ambalaj ve uygun fiyatlı ürün dağıtımını güçlendirin.

## Daha fazlası

- TÜİK (2026). *Türkiye İstatistik Kurumu (resmî site)*. https://www.tuik.gov.tr
- CORE Econ (2026). *The Economy 2.0*. https://www.core-econ.org/the-economy/
