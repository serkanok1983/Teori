---
id: kb-fmcg-5-4-promotion-economics
title: "Promosyon ekonomisi: Hacim arttı, peki kâr?"
summary: "Fiyat indirimli promosyon satışı hemen artırır, ama artışın bir kısmı öne çekilmiş ya da zaten olacak satıştır. Bu kart promosyonun gerçek katkısını baz satış, artımsal hacim ve promosyon sonrası düşüşle hesaplamayı anlatır."
course: fmcg
category: fiyatlama-ve-promosyon
tags: [promosyon, fiyatlama, analitik]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: orta
source_lessons: [FMCG-5.4]
reading_minutes: 3
key_points:
  - "Promosyonun etkisi, promosyon olmasaydı satılacak baz hacme göre ölçülür."
  - "Promosyon hacminin bir kısmı stok yapan tüketiciden ya da rakipten değil, kendi gelecekteki satışınızdan gelir."
  - "İndirim birim katkıyı düşürdüğü için, katkıyı korumak için gereken hacim artışı çoğu zaman sezgiden çok daha yüksektir."
  - "Promosyon sonrası düşüşü ve kardeş ürünlerden kaymayı hesaba katmadan promosyon başarılı ilan edilmemelidir."
glossary_terms: [baz-satis, artimsal-hacim, katki-payi]
related: [kb-fmcg-5-5-trade-spend-roi, kb-fmcg-5-1-price-elasticity, kb-fmcg-5-7-rgm-system, kb-fmcg-2-3-contribution-breakeven, kb-fmcg-3-5-brand-equity]
sources:
  - title: "How Promotions Work"
    authors: "Blattberg, R. C.; Briesch, R.; Fox, E. J."
    year: 1995
    type: article
    doi: "10.1287/mksc.14.3.G122"
    url: "https://doi.org/10.1287/mksc.14.3.G122"
    verified: true
    checked_on: 2026-10-28
    note: "Marketing Science 14(3), G122–G132."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Promosyon haftasında satış iki katına çıktığında herkes memnundur. Ama sonraki haftalarda satış normalin altına düşüyorsa ve indirim birim katkıyı yarıya indirdiyse, promosyon para kaybettirmiş olabilir. Bu kart, promosyonun gerçek etkisini hesaplamanızı sağlar.

## Temel fikir

**Baz satış** (*baseline*). Promosyon olmasaydı satılacak hacimdir. Genellikle promosyon dışı haftaların ortalamasından, mevsimsellik düzeltilerek tahmin edilir.

**Artımsal hacim** (*incremental volume*). Promosyon döneminde baz satışın üstüne çıkan hacimdir. Ancak bu hacmin hepsi "yeni" değildir. Blattberg, Briesch ve Fox (1995), promosyonların nasıl çalıştığına dair ampirik bulguları derler. Bu bulgulara göre fiyat promosyonları satışta belirgin bir geçici artış yaratır, ama artışın bir kısmı şu kaynaklardan gelebilir:

- **Stok yapma ve öne çekme:** Tüketici normalde sonra alacağı ürünü şimdi alır. Promosyondan sonra satış bir süre düşer.
- **Marka değiştirme:** Rakibin alıcısı geçici olarak size geçer.
- **Kendi ürününüzden kayma:** Kardeş ürünün ya da başka paketin alıcısı promosyonlu ürüne geçer.
- **Kategori genişlemesi:** Bazı kategorilerde tüketim de bir miktar artabilir.

Yalnızca gerçekten yeni gelen hacim katkı yaratır.

**İndirimin katkıya etkisi.** %20 indirim, birim katkıyı %20'den çok daha fazla düşürebilir. Katkıyı korumak için gereken hacim, baz katkının promosyonlu birim katkıya oranıdır.

**Promosyonu değerlendirme süreci.** Her promosyon için, başlamadan önce hedefi ve başarı ölçütü yazılmalıdır: yeni alışverişçi kazanmak mı, stok eritmek mi, rakip lansmanına yanıt vermek mi? Promosyon bittikten sonra baz satış, artımsal hacim, katkı değişimi ve promosyon sonrası düşüş birlikte hesaplanmalıdır. Sonuçlar, benzer promosyonlarla karşılaştırılabilecek bir veri tabanında saklanmalıdır. Zamanla bu veri tabanı, hangi indirim derinliğinin, hangi mekanik türünün ve hangi müşterinin daha iyi sonuç verdiğini gösterir. Perakendeciyle paylaşılan sonuçlar, bir sonraki yılın ortak iş planının temelini oluşturur.

## Bir örnek

> **Örnek (temsili rakamlar):** Fiyat, maliyet ve hacimler varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b3.py` ile yapılmıştır.

Bir ürünün net fiyatı 30 TL, değişken maliyeti 18 TL, haftalık baz satışı 1.000 adet. Bir hafta %20 indirimle 24 TL'ye satıyorsunuz; satış 1.800 adede çıkıyor. Sonraki haftalarda toplam 200 adet baz altı satış oluyor.

- Baz katkı: (30 − 18) × 1.000 = **12.000 TL**
- Promosyon haftası katkısı: (24 − 18) × 1.800 = **10.800 TL**
- Promosyon sonrası kayıp: 12 × 200 = **2.400 TL**
- Net etki: 10.800 − 2.400 − 12.000 = **−3.600 TL**

Hacim %80 artmasına rağmen promosyon katkıyı düşürdü. Katkıyı korumak için promosyon haftasında 12.000 / 6 = **2.000 adet** satmak, yani hacmi **%100** artırmak gerekirdi. Üstelik zincire ödenen ek ücretler ve raf malzemesi bu hesaba dahil değil.

## Sık yapılan hatalar

- **Promosyon haftasını önceki haftayla kıyaslamak.** Baz satışı doğru tahmin etmeden artış ölçülemez.
- **Sonraki haftalara bakmamak.** Öne çekilen satış, sonradan kayıp olarak döner.
- **Kardeş ürünleri unutmak.** Portföy toplamında hacim değişmemiş olabilir.
- **Her promosyonu tekrar etmek.** Sık indirim, tüketicinin indirimi beklemesini ve normal fiyatı reddetmesini öğretebilir.

## Pratikte nasıl uygulanır?

- [ ] Her promosyondan önce katkıyı korumak için gereken hacim artışını hesaplayın.
- [ ] Baz satışı promosyon dışı haftalardan, mevsimsellik ve dağıtım değişikliklerini düzelterek tahmin edin.
- [ ] Promosyon sonrası en az birkaç haftayı ve kardeş ürünleri de analiz edin.
- [ ] Promosyonları net katkıya göre sıralayın; zarar edenleri yeniden tasarlayın ya da takvimden çıkarın.

## Daha fazlası

- Blattberg, R. C.; Briesch, R.; Fox, E. J. (1995). *How Promotions Work.* Marketing Science 14(3), G122–G132. https://doi.org/10.1287/mksc.14.3.G122
