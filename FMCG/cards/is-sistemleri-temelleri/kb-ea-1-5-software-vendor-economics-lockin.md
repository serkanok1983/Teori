---
id: kb-ea-1-5-software-vendor-economics-lockin
title: "Yazılım firmaları nasıl para kazanır? Lisans, abonelik ve bağımlılık"
summary: "Lisans ile abonelik modelini beş yıllık maliyetle karşılaştırır; geçiş maliyeti ve tedarikçiye bağımlılığın sözleşme aşamasında nasıl yönetileceğini anlatır."
course: ea
category: is-sistemleri-temelleri
tags: [yazilim-secimi, lisans, abonelik, sozlesme, butce]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, it-yoneticisi]
level: orta
source_lessons: [EA-1.5]
reading_minutes: 3
key_points:
  - "Lisans modelinde büyük ödeme başta yapılır, ardından yıllık bakım ödenir; abonelikte ödeme kullanıcı ve süreyle yayılır."
  - "Hangi modelin ucuz olduğu, kullanım süresine ve kullanıcı sayısına bağlıdır; karşılaştırma en az beş yıl için yapılmalıdır."
  - "Geçiş maliyeti; veri taşıma, eğitim, entegrasyon ve kayıp verimi kapsar ve tedarikçinin pazarlık gücünü artırır."
  - "Veri çıkışı, fiyat artış sınırı ve sözleşme bitişindeki haklar imzadan önce yazılı hale getirilmelidir."
  - "Analist firma raporları pazar hakkında fikir verir ama tek başına seçim gerekçesi değildir."
glossary_terms: [gecis-maliyeti, saas]
related: [kb-ea-17-2-total-cost-of-ownership, kb-ea-17-4-vendor-selection-rfp, kb-ea-16-1-cloud-saas-basics, kb-ea-21-3-erp-market-turkey, kb-ea-19-3-working-with-it-partners]
sources:
  - title: "Information Rules: A Strategic Guide to the Network Economy"
    authors: "Shapiro, C.; Varian, H. R."
    year: 1999
    type: book
    verified: false
    note: "Geçiş maliyeti ve kilitlenme (lock-in) kavramları."
  - title: "The Business of Software"
    authors: "Cusumano, M. A."
    year: 2004
    type: book
    verified: false
    note: "Yazılım firmalarının gelir modelleri."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

ERP ya da saha satış yazılımı alırken önünüze iki tür teklif gelir: bir kerelik lisans artı yıllık bakım ya da kullanıcı başına aylık abonelik. Hangisinin ucuz olduğu, ilk yılın faturasına bakarak anlaşılmaz. Bu kart, yazılım firmalarının gelir modelini ve sizi onlara bağlayan **geçiş maliyetini** (*switching cost*) anlamanızı, sözleşmeyi buna göre kurmanızı sağlar.

## Temel fikir

Yazılım üretmenin maliyeti büyük ölçüde baştadır; bir müşteriye daha satmanın ek maliyeti düşüktür. Bu yüzden yazılım firmaları müşteriyi uzun süre elde tutmaya çalışır. Gelir modelleri genelde şunlardır:

- **Kalıcı lisans:** Yazılımı kullanma hakkı bir kez satın alınır. Güncelleme ve destek için genellikle lisans bedelinin belli bir yüzdesi kadar yıllık bakım ödenir.
- **Abonelik / SaaS** (*software as a service*, hizmet olarak yazılım): Yazılım tedarikçinin altyapısında çalışır; kullanıcı ve ay başına ödenir. Ödemeyi bıraktığınızda kullanım hakkı da biter.
- **Uygulama ve danışmanlık:** Kurulum, uyarlama ve eğitim çoğu zaman yazılım firmasının iş ortakları tarafından ayrıca faturalanır.

Kilitlenme (*lock-in*), yazılımı değiştirmenin maliyeti yükseldikçe oluşur. Geçiş maliyetinin parçaları: verinin taşınması, entegrasyonların yeniden yazılması, kullanıcıların yeniden eğitilmesi, geçiş döneminde düşen verim ve firmaya özel geliştirmelerin kaybı. Bu maliyet ne kadar yüksekse yenileme döneminde tedarikçinin fiyat artırma gücü o kadar fazladır.

Pazar raporları (analist firmaların sıralamaları gibi) hangi ürünlerin var olduğunu görmek için yararlıdır. Ancak bunlar akademik ya da bağımsız denetimli kaynak değildir; sizin sektörünüze ve ölçeğinize uygunluğu kendiniz test etmelisiniz.

## Bir örnek

> **Örnek (temsili rakamlar):** Fiyatlar gerçek bir teklife dayanmaz; hesaplar `scripts/cards_numbers_ea_b1.py` ile yapılmıştır.

25 kullanıcılı bir bayi iki teklif alıyor:

- **Lisans:** 900.000 TL lisans + her yıl lisansın %20'si bakım (180.000 TL).
- **Abonelik:** kullanıcı başına aylık 1.800 TL → yıllık 540.000 TL.

| Yıl | Lisans (kümülatif) | Abonelik (kümülatif) |
|---|---|---|
| 1 | 1.080.000 TL | 540.000 TL |
| 2 | 1.260.000 TL | 1.080.000 TL |
| 3 | 1.440.000 TL | 1.620.000 TL |
| 4 | 1.620.000 TL | 2.160.000 TL |
| 5 | 1.800.000 TL | 2.700.000 TL |

Abonelik ilk iki yıl daha ucuz; üçüncü yıldan itibaren lisans öne geçiyor. Ancak bu tablo sunucu, yedekleme ve BT personeli gibi lisans tarafında sizin taşıdığınız maliyetleri içermiyor; tam karşılaştırma için toplam sahip olma maliyeti hesabı gerekir. Ayrıca yüksek enflasyon döneminde abonelik bedelinin yıllık artış oranı sözleşmede sınırlanmamışsa tablo hızla değişir.

Geçiş maliyetini de ekleyin: Üç yıl sonra başka ürüne geçmenin veri taşıma, eğitim ve entegrasyon maliyeti 350.000 TL ise bu tutar yıllık aboneliğin **0,65** katıdır. Tedarikçi, bu tutarın altında kalan her zammı kabul etme eğiliminde olacağınızı bilir.

## Sık yapılan hatalar

- Teklifleri yalnızca ilk yıl maliyetiyle karşılaştırmak.
- Abonelikte yıllık fiyat artışını sözleşmede sınırlamamak.
- Verinin sözleşme bitiminde hangi biçimde ve ne sürede teslim edileceğini yazmamak.
- Firmaya özel geliştirmelerin fikrî haklarını ve kaynak kodu durumunu konuşmamak.
- Pazar raporundaki sıralamayı uygunluk kanıtı saymak.

## Pratikte nasıl uygulanır?

- [ ] Teklifleri en az beş yıllık kümülatif maliyetle, aynı tabloda karşılaştırın.
- [ ] Kullanıcı sayısı artarsa ve azalırsa fiyatın nasıl değişeceğini yazılı isteyin.
- [ ] Sözleşmeye yıllık fiyat artış sınırı ve bildirim süresi koyun.
- [ ] Veri çıkışı (biçim, süre, ücret) ve sözleşme sonrası erişim hakkını maddeleştirin.
- [ ] Geçiş maliyetini kabaca hesaplayın; yenileme pazarlığında bu rakamı bilin.
- [ ] Uygulama ortağının (iş ortağı) ayrılması durumunda desteğin nasıl süreceğini sorun.

## Daha fazlası

- Shapiro ve Varian (1999), *Information Rules* — geçiş maliyeti ve kilitlenme (kitap; doğrulanmadı).
- Cusumano (2004), *The Business of Software* — yazılım firmalarının gelir modelleri (kitap; doğrulanmadı).
