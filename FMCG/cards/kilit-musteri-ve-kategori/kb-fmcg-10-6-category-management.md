---
id: kb-fmcg-10-6-category-management
title: "Kategori yönetimi ve kategori kaptanlığı"
summary: "Kategori yönetimi, bir ürün kategorisini perakendeci ile tedarikçinin birlikte, kategorinin toplam satış ve kârını büyütecek biçimde yönetmesidir. Bu kart klasik süreci, kategori rollerini, kategori kaptanlığının faydalarını ve rekabet hukuku risklerini anlatır."
course: fmcg
category: kilit-musteri-ve-kategori
tags: [kilit-musteri, kategori-yonetimi, raf]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: orta
source_lessons: [FMCG-10.5, FMCG-10.6]
reading_minutes: 3
key_points:
  - "Kategori yönetimi, tek tek markalar yerine kategoriyi bir iş birimi olarak ele alır."
  - "Klasik süreç; kategori tanımı, kategori rolü, değerlendirme, hedefler, strateji, taktikler, uygulama ve gözden geçirme adımlarından oluşur."
  - "Kategori rolü (örneğin trafik yaratan ya da kâr getiren kategori), ürün çeşidi, fiyat ve promosyon kararlarını yönlendirir."
  - "Kategori kaptanı, perakendeciye öneri hazırlayan tedarikçidir; öneriler tarafsız olmalıdır."
  - "Rakiplerle ilgili bilgi paylaşımı ve rakipleri dışlayan öneriler rekabet hukuku riski yaratır."
glossary_terms: [kategori-yonetimi, planogram, raf-payi, talep-transferi]
related: [kb-fmcg-9-3-shelf-space-planogram, kb-fmcg-9-1-retailer-economics, kb-fmcg-4-6-sku-rationalisation, kb-fmcg-10-7-joint-business-planning, kb-fmcg-12-5-ethics-compliance-trade]
sources:
  - title: "Category Management Association"
    authors: "Category Management Association"
    year: 2026
    type: web
    url: "https://www.categorymanagement.org/"
    verified: true
    checked_on: 2026-10-28
  - title: "4054 sayılı Rekabetin Korunması Hakkında Kanun"
    authors: "T.C. Mevzuat Bilgi Sistemi"
    year: 1994
    type: law
    url: "https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=4054&MevzuatTur=1&MevzuatTertip=5"
    verified: true
    checked_on: 2026-10-28
  - title: "Rekabet Kurumu"
    authors: "Rekabet Kurumu"
    year: 2026
    type: web
    url: "https://www.rekabet.gov.tr/"
    verified: true
    checked_on: 2026-10-28
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Perakendecinin kategori yöneticisi her yıl onlarca kategori için ürün çeşidi, raf düzeni, fiyat ve promosyon kararı verir. Kategoriyi iyi bilen bir tedarikçi, bu kararlara veri ve öneriyle katkı sunarak hem perakendeciye değer yaratır hem de kendi markalarının yerini güçlendirir. Bu kart, kategori yönetimi (*category management*) sürecini ve tedarikçinin bu süreçteki rolünü anlatır.

## Temel fikir

**Klasik süreç.** 1990'larda tüketiciye etkin yanıt (ECR) çalışmalarıyla yaygınlaşan ve kategori yönetimi derneğinin kaynaklarında da anlatılan süreç sekiz adımdan oluşur:

1. **Kategori tanımı:** Tüketicinin gözünde hangi ürünler birbirinin yerine geçer?
2. **Kategori rolü:** Bu kategori mağaza için ne işe yarıyor?
3. **Kategori değerlendirmesi:** Satış, pay, büyüme ve kâr verisiyle mevcut durum.
4. **Hedefler ve ölçütler:** Satış, kâr, pay, stok devir hızı.
5. **Strateji:** Trafik yaratmak, sepeti büyütmek, kâr üretmek, imaj yaratmak.
6. **Taktikler:** Ürün çeşidi, fiyat, promosyon, raf düzeni.
7. **Uygulama:** Mağazalarda hayata geçirme.
8. **Gözden geçirme:** Sonuçları ölçme ve düzeltme.

**Kategori rolleri.** Tipik roller şunlardır:

- **Hedef kategori:** Mağazayı tercih ettiren, perakendecinin farklılaştığı kategori.
- **Rutin kategori:** Düzenli ihtiyaç; rekabetçi fiyat ve sürekli bulunurluk gerekir.
- **Mevsimlik ya da dönemsel kategori:** Belirli dönemlerde öne çıkar.
- **Kolaylık kategorisi:** Tek seferde alışverişi tamamlamaya yardımcı olur.

Rol, kararları yönlendirir. Rutin bir kategoride fiyat rekabetçiliği önemliyken, hedef bir kategoride geniş ürün çeşidi ve teşhir öne çıkar.

**Kategori kaptanlığı.** Perakendeci, bir tedarikçiyi kategori analizleri ve öneriler hazırlamak üzere "kaptan" olarak seçebilir. Faydası açıktır: Tedarikçinin verisi ve uzmanlığı kullanılır. Riski de vardır: Kaptan, kendi markalarını kayıracak ya da rakipleri dışlayacak öneriler yapabilir. Ayrıca rakiplerin fiyat, promosyon ya da plan bilgilerine erişim, 4054 sayılı Kanun açısından rekabeti kısıtlayıcı bilgi değişimi riski yaratabilir. Kaptan önerileri tarafsız olmalı, rakip bilgileri kaptana açılmamalı ve son karar perakendecide kalmalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Satış ve kanibalizasyon oranı varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b6.py` ile yapılmıştır.

Aylık satışı 5.000.000 TL olan bir kategoride tedarikçi, yeni bir ürün listelemesi öneriyor. Yeni ürünün aylık **40.000 TL** satması bekleniyor.

Ancak benzer ürünlerdeki deneyim, yeni ürün satışının yaklaşık **%60**'ının kategorideki diğer ürünlerden geleceğini gösteriyor: **24.000 TL**. Kategorinin net artışı **16.000 TL**, yani yaklaşık **%0,32**.

Perakendeci bu hesabı mutlaka yapar. Tedarikçi, öneriyi yalnızca "yeni ürün 40.000 TL satacak" diye sunarsa güven kaybeder. Daha güçlü bir öneri şudur: Yeni ürünü listelerken, kategoride yavaş dönen ve talebi büyük ölçüde başka ürünlere geçecek iki ürünü listeden çıkarmak. Böylece raf alanı açılır ve kategorinin metre başına verimi artar.

## Sık yapılan hatalar

- **Kategori yönetimini kendi markanızı satma aracı olarak kullanmak.** Perakendeci bunu fark eder ve kaptanlığı başka bir tedarikçiye verir.
- **Kanibalizasyonu göz ardı etmek.** Yeni ürünün brüt satışı, kategoriye net katkısı değildir.
- **Kategori rolünü bilmeden öneri yapmak.** Rutin bir kategoriye hedef kategori stratejisi önermek tutarsızdır.
- **Rakip bilgilerini istemek ya da kullanmak.** Rekabet hukuku açısından ciddi risk yaratır.
- **Uygulamayı izlememek.** Planogram önerisi mağazaya yansımıyorsa sonuç gelmez.

## Pratikte nasıl uygulanır?

- [ ] Ana kategorileriniz için tüketici karar ağacını ve kategori tanımını çıkarın.
- [ ] Her kilit müşteride kategorinin rolünü öğrenin.
- [ ] Önerilerinizi kategorinin toplam satış ve kârına etkisiyle sunun; kanibalizasyonu açıkça hesaplayın.
- [ ] Kaptanlık yapıyorsanız, rakip bilgileri için yazılı kurallar ve bilgi duvarları oluşturun; rekabet hukuku danışmanından görüş alın.
- [ ] Önerilerin uygulanmasını ve sonuçlarını üç ayda bir perakendeciyle birlikte gözden geçirin.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın.

## Daha fazlası

- Category Management Association (2026). *Category Management Association.* https://www.categorymanagement.org/
- T.C. Mevzuat Bilgi Sistemi (1994). *4054 sayılı Rekabetin Korunması Hakkında Kanun.* https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4054.pdf
- Rekabet Kurumu (2026). *Rekabet Kurumu.* https://www.rekabet.gov.tr/
