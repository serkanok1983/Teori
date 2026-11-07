---
id: kb-eco-39-3-abc-customer-profitability
title: "Müşteri kârlılığı: Hizmet maliyetini hesaba katmak"
summary: "Aynı ciroyu ve brüt marjı getiren iki müşterinin sipariş, teslimat ve vade maliyetleri nedeniyle nasıl çok farklı kârlılığa sahip olabileceğini ve hizmet maliyeti analizinin nasıl yapılacağını anlatır."
course: eco
category: maliyet-ve-butce
tags: [maliyet, musteri, karlilik, distributor]
roles: [bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: orta
source_lessons: [ECO-39.3, EA-23.5]
reading_minutes: 3
key_points:
  - "Brüt kâr, müşterinin gerçek kârlılığını göstermez; hizmet maliyeti de düşülmelidir."
  - "Sipariş sayısı, teslimat noktası, iade ve vade, başlıca hizmet maliyeti sürücüleridir."
  - "Zarar ettiren müşteriyi bırakmadan önce hizmet koşullarını değiştirmeyi deneyin."
  - "Faaliyet tabanlı maliyetleme müşteri bazında da uygulanabilir."
glossary_terms: [hizmet-maliyeti, faaliyet-tabanli-maliyetleme, maliyet-surucusu]
related: [kb-eco-39-2-product-costing, kb-eco-55-1-case-distributor-credit-decision, kb-eco-38-2-cash-conversion-cycle, kb-eco-6-4-price-discrimination]
sources:
  - title: "Cost and Effect: Using Integrated Cost Systems to Drive Profitability and Performance"
    authors: "Kaplan, R. S.; Cooper, R."
    year: 1998
    type: book
    verified: true
    checked_on: 2026-10-28
  - title: "Principles of Accounting, Volume 2: Managerial Accounting"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-managerial-accounting/pages/1-why-it-matters"
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

Distribütörler müşterilerini genellikle ciro ve brüt kâra göre sıralar. Oysa küçük ve sık siparişler, çok noktalı teslimatlar ve uzun vade, brüt kârı sessizce eritir. Bu kart, müşteri bazında gerçek kârlılığı hesaplamanızı ve fiyat ile hizmet koşullarını buna göre ayarlamanızı sağlar.

## Temel fikir

**Müşteri kârı = Brüt kâr − Hizmet maliyeti**

Hizmet maliyetinin başlıca kalemleri:

- **Sipariş işleme:** Her siparişin girişi, toplanması, faturalanması.
- **Teslimat:** Teslimat noktası sayısı, mesafe, araç doluluğu.
- **Vade:** Alacakta bağlı kalan paranın finansman maliyeti.
- **Diğerleri:** İadeler, raf hizmeti, promosyon desteği, satış temsilcisi ziyaretleri.

Bu, faaliyet tabanlı maliyetlemenin müşteriye uygulanmış hâlidir: Her faaliyetin birim maliyetini bulur, müşterinin bu faaliyeti ne kadar kullandığıyla çarparsınız.

### Verileri nereden bulursunuz?

ABC için mükemmel bir maliyet sistemi gerekmez; mevcut kayıtlardan makul bir yaklaşım kurabilirsiniz:

- **Sipariş sayısı ve satır sayısı:** ERP'deki sipariş kayıtlarından. Depo toplama maliyeti çoğu zaman sipariş tutarından çok satır sayısıyla ilişkilidir.
- **Teslimat sayısı ve mesafe:** Sevkiyat kayıtları veya araç takip sisteminden. Aynı güzergâhtaki müşterilere araç maliyetini durak sayısına göre dağıtabilirsiniz.
- **Ortalama tahsilat süresi:** Cari hesap yaşlandırma raporundan. Finansman maliyeti, ortalama alacak bakiyesi × şirketin borçlanma maliyeti ile yaklaşık hesaplanır.
- **Satış temsilcisi zamanı:** Ziyaret planlarından.

Faaliyet havuzlarının toplamı, gerçekte katlanılan dağıtım ve satış giderlerine eşit olmalıdır. Bu kontrol, maliyetlerin uydurulmadığını gösterir.

### Sonuçla ne yaparsınız?

Zarar eden müşteriyi hemen bırakmak yerine önce hizmet modelini değiştirin: minimum sipariş tutarı, daha seyrek teslimat, sipariş birleştirme, vade farkı veya telesatışa geçiş. Bazı müşteriler sabit giderleri paylaştığı için bırakıldığında toplam kâr düşebilir. Bu yüzden karar verirken ilgili maliyetlere bakın.

## Bir örnek

> **Örnek (temsili rakamlar):** Müşteriler, birim maliyetler ve oranlar varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b6.py` ile yapılmıştır.

İki müşterinin yıllık cirosu 10.000.000 TL, brüt marjı %15; ikisinin de brüt kârı 1.500.000 TL. Sipariş başına maliyet 600 TL, teslimat başına 900 TL, yıllık finansman maliyeti %36.

| | Müşteri X | Müşteri Y |
|---|---|---|
| Sipariş / teslimat sayısı | 50 / 50 | 1.000 / 800 |
| Ortalama tahsilat süresi | 30 gün | 90 gün |
| Sipariş + teslimat maliyeti | 75.000 TL | 1.320.000 TL |
| Vade maliyeti | 295.890 TL | 887.671 TL |
| **Müşteri kârı** | **1.129.110 TL** | **707.671 TL zarar** |

Y'yi bırakmadan önce şunlar denenebilir: minimum sipariş tutarı, haftada sabit teslimat günü, vadeye bağlı fiyat farkı veya merkezî teslimat.

## Sık yapılan hatalar

- Satış primlerini yalnızca ciro veya brüt kâra bağlamak.
- Hizmet maliyetini "genel gider" diye bütün müşterilere eşit dağıtmak.
- Zarar eden müşteriyi hemen bırakmak; sabit maliyetlerin bir kısmı kalacağı için önce katkı payına bakmak gerekir.
- Analizi bir kez yapıp müşteri davranışı değişince güncellememek.
- Bütün maliyetleri dağıtmaya çalışıp analizi aylarca uzatmak; en büyük birkaç faaliyetle başlamak çoğu zaman yeterlidir.

## Pratikte nasıl uygulanır?

- [ ] Sipariş, teslimat ve vade için birim maliyetleri muhasebe ve lojistik verisinden hesaplayın.
- [ ] İlk 50 müşteriniz için hizmet maliyeti tablosunu çıkarın.
- [ ] Müşterileri kârlılık ve ciroya göre dört gruba ayırın ve her gruba ayrı hizmet modeli tanımlayın.
- [ ] Satış temsilcisi hedeflerine müşteri kârını ekleyin.
- [ ] Analizi yılda en az iki kez güncelleyin.
- [ ] Analiz sonucunu satış ekibiyle paylaşın ve müşteri bazlı hizmet modeli kararlarını birlikte alın.

## Daha fazlası

- Kaplan, R. S.; Cooper, R. (1998). *Cost and Effect: Using Integrated Cost Systems to Drive Profitability and Performance*.
- OpenStax (2026). *Principles of Accounting, Volume 2: Managerial Accounting*. https://openstax.org/books/principles-managerial-accounting/pages/1-why-it-matters
