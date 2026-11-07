---
id: kb-eco-39-2-product-costing
title: "Ürün maliyeti: Genel giderleri doğru dağıtmak"
summary: "Direkt madde ve işçiliğin yanında genel üretim giderlerinin ürünlere nasıl dağıtıldığını, geleneksel dağıtımın düşük hacimli ve karmaşık ürünleri nasıl ucuz gösterdiğini ve faaliyet tabanlı yaklaşımın farkını anlatır."
course: eco
category: maliyet-ve-butce
tags: [maliyet, uretim, fiyatlama]
roles: [uretici-sahibi, uretici-yonetici, finans-muduru]
level: orta
source_lessons: [ECO-39.2]
reading_minutes: 3
key_points:
  - "Ürün maliyeti = direkt madde + direkt işçilik + dağıtılan genel üretim gideri."
  - "Genel giderleri tek bir ölçüye (ör. işçilik saati) göre dağıtmak, karmaşık ürünlerin maliyetini düşük gösterebilir."
  - "Faaliyet tabanlı maliyetleme, gideri onu doğuran faaliyete (kurulum, sipariş, kalite kontrol) göre dağıtır."
  - "Yanlış maliyet, yanlış fiyat ve yanlış ürün karması kararına yol açar."
glossary_terms: [faaliyet-tabanli-maliyetleme, genel-uretim-gideri, maliyet-surucusu]
related: [kb-eco-39-3-abc-customer-profitability, kb-eco-39-4-budgeting-standard-costs, kb-eco-39-5-relevant-costs-decisions, kb-eco-34-1-inventory-valuation]
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

Üreticiler fiyat, iskonto ve ürün gamı kararlarını birim maliyete göre verir. Birim maliyetin büyük kısmı ise doğrudan ölçülemeyen genel giderlerdir: makine ayarı, bakım, kalite kontrol, planlama. Bu kart, bu giderlerin ürünlere nasıl dağıtıldığını ve dağıtım yönteminin kararlarınızı nasıl değiştirdiğini gösterir.

## Temel fikir

**Direkt maliyetler** ürüne doğrudan izlenebilir: hammadde, ambalaj, üretim hattındaki işçilik.

**Genel üretim giderleri** birden fazla ürüne ortaktır. Bunlar bir **dağıtım anahtarıyla** ürünlere yüklenir.

- **Geleneksel yöntem:** Tek bir anahtar kullanılır (işçilik saati, makine saati). Yüksek hacimli ürün giderin büyük kısmını taşır.
- **Faaliyet tabanlı maliyetleme:** Gider önce faaliyetlere (kurulum, sipariş işleme, kalite kontrol) ayrılır, sonra her faaliyetin **maliyet sürücüsüne** (kurulum sayısı, parti sayısı) göre ürünlere dağıtılır. Kaplan ve Cooper (1998) bu yaklaşımı ayrıntılı biçimde anlatır.

Az adetli, sık kurulum gerektiren ürünler kaynakları orantısız tüketir. Geleneksel yöntem bunu gizler.

### Distribütör için ürün maliyeti

Distribütörler ürün üretmez, ama aynı mantık geçerlidir. Bir ürünün alış fiyatı, gerçek maliyetinin yalnızca bir kısmıdır. Depoda kapladığı alan, toplama süresi, kırılma ve son kullanma tarihi kayıpları, iade oranı ve stokta bekleme süresinin finansman maliyeti de ürüne aittir. Hacimli ama ucuz ürünler (ör. içecek, kâğıt ürünleri) depo ve taşıma maliyetinin büyük kısmını tüketirken, küçük ve pahalı ürünler bu kaynakları çok daha az kullanır.

### Maliyet bilgisini nerede kullanırsınız?

- **Fiyatlama:** Tam maliyetin altında fiyatlanan ürünleri belirlemek.
- **Ürün yelpazesi:** Düşük hacimli, yüksek karmaşıklık yaratan ürünlerin gerçekten kâr getirip getirmediğini görmek.
- **Minimum sipariş miktarları:** Küçük partilerin kurulum maliyetini yansıtan sipariş veya üretim miktarları belirlemek.
- **Tedarikçi müzakereleri:** Paketleme, palet düzeni ve teslimat sıklığının size maliyetini somut olarak göstermek.

### Dikkat

Ürün maliyeti, sabit giderlerin dağıtımını içerdiği için kısa vadeli kararlarda yanıltıcı olabilir. Bir ürünü bırakmak, ona yüklenen sabit giderlerin ortadan kalkacağı anlamına gelmez. Bırakma kararları için ilgili maliyetlere bakın.

## Bir örnek

> **Örnek (temsili rakamlar):** Ürünler, giderler ve dağıtım oranları varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b6.py` ile yapılmıştır.

Bir gıda üreticisinin yıllık genel üretim gideri 3.000.000 TL. A ürünü yılda 100.000 adet, B ürünü 10.000 adet üretiliyor. İşçilik saatinin %80'i A'ya ait; ancak kurulumların yarısı B için yapılıyor ve giderin yarısı kurulumdan doğuyor.

| Birim (TL) | A, geleneksel | B, geleneksel | A, faaliyet tabanlı | B, faaliyet tabanlı |
|---|---|---|---|---|
| Direkt madde + işçilik | 40 + 10 | 50 + 12 | 40 + 10 | 50 + 12 |
| Genel gider payı | 24 | 60 | 15 | 150 |
| Birim maliyet | 74 | 122 | 65 | 212 |
| Satış fiyatı | 85 | 160 | 85 | 160 |
| Birim marj | 11 | 38 | 20 | **52 zarar** |

Geleneksel hesapla B en kârlı ürün görünüyor ve satış ekibi onu öne çıkarıyor. Faaliyet tabanlı hesapla B her adette 52 TL kaybettiriyor. Çözüm: B'nin fiyatını gözden geçirmek, parti büyüklüğünü artırmak veya kurulum süresini kısaltmak.

## Sık yapılan hatalar

- Bütün genel giderleri tek bir anahtarla dağıtıp sonucu kesin doğru kabul etmek.
- Dağıtılan sabit gideri, kısa vadeli kararlarda (özel sipariş gibi) değişken maliyet gibi kullanmak.
- Faaliyet tabanlı sistemi aşırı ayrıntılı kurup güncellenemez hâle getirmek.
- Maliyet hesabını yılda bir kez yapıp girdi fiyatları değişince güncellememek.

## Pratikte nasıl uygulanır?

- [ ] Genel giderlerinizi 4–6 ana faaliyete ayırın.
- [ ] Her faaliyet için ölçülebilir bir maliyet sürücüsü seçin.
- [ ] En çok satan ve en az satan beş ürünün maliyetini iki yöntemle karşılaştırın.
- [ ] Büyük fark çıkan ürünlerde fiyat, minimum sipariş miktarı ve parti büyüklüğünü yeniden değerlendirin.
- [ ] Maliyet kartlarını enflasyon dönemlerinde en az üç ayda bir güncelleyin.

## Daha fazlası

- Kaplan, R. S.; Cooper, R. (1998). *Cost and Effect: Using Integrated Cost Systems to Drive Profitability and Performance*.
- OpenStax (2026). *Principles of Accounting, Volume 2: Managerial Accounting*. https://openstax.org/books/principles-managerial-accounting/pages/1-why-it-matters
