---
id: kb-eco-34-1-inventory-valuation
title: "Stok değerleme: FIFO, ağırlıklı ortalama ve net gerçekleşebilir değer"
summary: "Stok maliyet yöntemlerinin (ilk giren ilk çıkar ve ağırlıklı ortalama) brüt kârı ve dönem sonu stok değerini nasıl etkilediğini, fiyatların arttığı dönemlerde farkın neden büyüdüğünü ve net gerçekleşebilir değere göre stok değer düşüklüğünü anlatır."
course: eco
category: finansal-tablolar
tags: [muhasebe, stok, karlilik]
roles: [bayi-sahibi, bayi-yonetici, finans-muduru, depo-lojistik-muduru]
level: orta
source_lessons: [ECO-34.1]
reading_minutes: 3
key_points:
  - "Fiyatlar artarken FIFO daha düşük satış maliyeti ve daha yüksek kâr gösterir; ağırlıklı ortalama arada kalır."
  - "Yöntem kârın dönemler arasındaki dağılımını değiştirir; ekonomik gerçeği değiştirmez."
  - "Stok, maliyet ile net gerçekleşebilir değerden düşük olanıyla raporlanır."
  - "Son kullanma tarihi yaklaşan ve yavaş dönen stoklar düzenli olarak değer düşüklüğü testinden geçirilmelidir."
glossary_terms: [fifo, agirlikli-ortalama-maliyet, net-gerceklesebilir-deger]
related: [kb-eco-32-4-finance-in-high-inflation, kb-eco-35-2-inflation-accounting, kb-ea-20-5-inventory-in-erp, kb-eco-33-4-income-statement]
sources:
  - title: "IAS 2 Inventories"
    authors: "IFRS Foundation"
    year: 2026
    type: standard
    url: "https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/"
    verified: true
    checked_on: 2026-10-28
  - title: "213 sayılı Vergi Usul Kanunu"
    authors: "T.C. Resmî Gazete / Mevzuat Bilgi Sistemi"
    year: 1961
    type: law
    url: "https://www.mevzuat.gov.tr/MevzuatMetin/1.4.213.pdf"
    verified: true
    checked_on: 2026-10-28
    note: "Mevzuat Bilgi Sistemi resmî PDF metni açıldı, kanun adı ve numarası eşleşti (2026-10-28)."
  - title: "Principles of Accounting, Volume 1: Financial Accounting"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters"
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

Aynı ürünü farklı fiyatlarla satın aldığınızda, sattığınız malın maliyeti hangi fiyattan hesaplanacak? Bu seçim, özellikle fiyatların hızla arttığı dönemlerde, raporlanan kârı belirgin şekilde değiştirir. Bu kart, yöntemleri karşılaştırmanızı ve stok değer düşüklüğünü doğru ele almanızı sağlar.

## Temel fikir

**Maliyet yöntemleri (TMS 2):**

- **İlk giren ilk çıkar (FIFO):** Satılan mal, en eski alımların maliyetiyle hesaplanır. Dönem sonu stok en yeni fiyatlarla kalır.
- **Ağırlıklı ortalama:** Tüm alımların ortalama maliyeti kullanılır.
- Son giren ilk çıkar (LIFO), TFRS kapsamında kabul edilmez.

Vergi mevzuatı da stok değerleme yöntemleri konusunda kurallar içerir; yasal kayıtlarda hangi yöntemin kullanıldığını mali müşavirinizle teyit edin.

**Net gerçekleşebilir değer (NGD):** Ürünün tahmini satış fiyatından satış için gereken maliyetlerin düşülmesiyle bulunur. Stok, maliyet ile NGD'den düşük olanıyla raporlanır. NGD maliyetin altına düşerse fark gider yazılır.

**Yönetim açısından:** Hangi yöntem seçilirse seçilsin, fiyatlama kararlarında yerine koyma maliyetini esas alın; muhasebe yöntemi raporlamayı, yerine koyma maliyeti ise işin sürdürülebilirliğini belirler.

### Stok sayımı ve fireler

Değerleme yöntemi ne olursa olsun, kayıttaki miktar fiziki miktarla uyuşmuyorsa bütün hesap yanlıştır. Distribütörlerde dönem sonu sayımına ek olarak, değerli veya hızlı dönen ürünlerde düzenli dönemsel sayım (döngüsel sayım) yapmak, farkları erken yakalamayı sağlar. Sayım farkları, kırılma, bozulma ve kayıp nedeniyle ortaya çıkan fireler ayrı bir hesapta izlenmelidir. Firenin vergi açısından gider yazılabilmesi belgelendirmeye ve mevzuattaki şartlara bağlıdır; imha edilen ürünler için tutanak ve gerekirse resmî imha süreçleri gerekebilir.

### Yavaş dönen stok

Stok yaşlandırma tablosu hazırlayın: her ürünün son satıştan bu yana geçen süresi ve son kullanma tarihine kalan süresi. Belirli bir süredir hareket görmeyen ürünler için:

- Tedarikçiye iade veya takas imkânını araştırın.
- İndirimli satış, kampanya veya farklı kanala yönlendirme yapın.
- Net gerçekleşebilir değeri maliyetin altına düştüyse değer düşüklüğü ayırın.

Yavaş dönen stoğu bilançoda maliyetle taşımak, hem kârı hem de bankalara sunulan tabloları olduğundan iyi gösterir.

## Bir örnek

> **Örnek (temsili rakamlar):** Fiyat ve miktarlar varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b4.py` ile yapılmıştır.

Bir distribütör önce 1.000 adet ürünü birimi 50 TL'den, sonra 1.000 adet ürünü birimi 60 TL'den alıyor. Dönem içinde 1.000 adet birimi 80 TL'den satıyor: hasılat 80.000 TL.

| | FIFO | Ağırlıklı ortalama |
|---|---|---|
| Satılan malın maliyeti | 50.000 | 55.000 |
| Brüt kâr | 30.000 | 25.000 |
| Dönem sonu stok | 60.000 | 55.000 |

Ağırlıklı ortalama birim maliyet 55 TL. FIFO daha yüksek kâr gösteriyor; ama elde kalan stok yeni fiyatlarla değerlenmiş ve bir sonraki dönemin maliyeti daha yüksek olacak.

**Değer düşüklüğü:** Elde kalan stoktan 200 adedin son kullanma tarihi yaklaşıyor ve en fazla birimi 45 TL'ye satılabilecek. Ortalama maliyetle değerlenen bu ürünler için 3.000 TL değer düşüklüğü gideri kaydedilmeli.

## Sık yapılan hatalar

- Yöntem farkından doğan kârı gerçek performans iyileşmesi sanmak.
- Değer düşüklüğünü yıl sonuna bırakmak; aylık kârı yüksek göstermek.
- Son kullanma tarihi yaklaşan ürünleri ve yavaş dönen stokları ayrıca izlememek.
- ERP'deki maliyet yöntemiyle muhasebe kayıtlarındaki yöntemin farklı olması.
- Fiyatlamayı muhasebe maliyetine göre yapmak.

## Pratikte nasıl uygulanır?

- [ ] Kullandığınız maliyet yöntemini ve ERP ayarlarını mali müşavirinizle teyit edin.
- [ ] Stoklarınızı yaşına ve son kullanma tarihine göre aylık raporlayın.
- [ ] Değer düşüklüğü için yazılı bir kural belirleyin (ör. belirli bir yaşı geçen stoklar için).
- [ ] Yönetim raporunda brüt kârı yerine koyma maliyetiyle de hesaplayın.
- [ ] Vergi açısından değer düşüklüğünün nasıl ele alınacağını mali müşavirinizle değerlendirin.

## Daha fazlası

- IFRS Foundation (2026). *IAS 2 Inventories*. https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/
- T.C. Resmî Gazete / Mevzuat Bilgi Sistemi (1961). *213 sayılı Vergi Usul Kanunu*. https://www.mevzuat.gov.tr/MevzuatMetin/1.4.213.pdf
- OpenStax (2026). *Principles of Accounting, Volume 1: Financial Accounting*. https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters
