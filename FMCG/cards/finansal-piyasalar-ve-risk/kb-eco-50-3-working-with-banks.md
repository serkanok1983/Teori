---
id: kb-eco-50-3-working-with-banks
title: "Bankalarla çalışmak: Kredi teklifinin gerçek maliyeti"
summary: "Bir işletme kredisinin nominal faiz yerine komisyon, bloke tutar ve vergiler dahil efektif maliyetle nasıl karşılaştırılacağını, bankanın kredi değerlendirmesinde neye baktığını ve banka ilişkisinin nasıl yönetileceğini anlatır."
course: eco
category: finansal-piyasalar-ve-risk
tags: [banka, finansman, kredi, faiz]
roles: [uretici-sahibi, bayi-sahibi, finans-muduru]
level: orta
source_lessons: [ECO-50.3]
reading_minutes: 3
key_points:
  - "Kredi teklifleri nominal faizle değil, kullanılabilir tutar üzerinden efektif maliyetle karşılaştırılır."
  - "Dosya masrafı, komisyon, bloke mevduat ve kredi işlemlerine ilişkin vergiler maliyeti artırır."
  - "Banka; mali tablolara, nakit akışına, teminata ve ödeme geçmişine bakar."
  - "Birden fazla bankayla düzenli ve şeffaf ilişki, kriz anında finansmana erişimi kolaylaştırır."
glossary_terms: [efektif-faiz, teminat-mektubu, dbs, kredi-limiti]
related: [kb-eco-25-2-loans-real-vs-nominal, kb-eco-38-3-distributor-credit-risk-dbs, kb-eco-50-4-tcmb-policy-rate-credit, kb-eco-31-4-debt-vs-equity, kb-eco-12-1-adverse-selection-credit]
sources:
  - title: "Bankacılık Düzenleme ve Denetleme Kurumu (resmî site)"
    authors: "BDDK"
    year: 2026
    type: web
    url: "https://www.bddk.org.tr"
    verified: true
    checked_on: 2026-10-28
  - title: "Türkiye Bankalar Birliği (resmî site)"
    authors: "TBB"
    year: 2026
    type: web
    url: "https://www.tbb.org.tr"
    verified: true
    checked_on: 2026-10-28
  - title: "Findeks"
    authors: "Kredi Kayıt Bürosu"
    year: 2026
    type: web
    url: "https://www.findeks.com"
    verified: true
    checked_on: 2026-10-28
  - title: "The Benefits of Lending Relationships: Evidence from Small Business Data"
    authors: "Petersen, M. A.; Rajan, R. G."
    year: 1994
    type: article
    doi: "10.1111/j.1540-6261.1994.tb04418.x"
    url: "https://doi.org/10.1111/j.1540-6261.1994.tb04418.x"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Finance 49(1). Banka ilişkisi ve kredi erişimi."
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Distribütörler ve üreticiler işletme sermayesini büyük ölçüde banka kredileri, DBS ve teminat mektuplarıyla finanse eder. Bu kart, kredi tekliflerini doğru karşılaştırmanızı ve banka ilişkisini daha iyi yönetmenizi sağlar.

## Temel fikir

**Efektif maliyet:** Kredinin gerçek maliyeti, ödenen tüm faiz ve masrafların fiilen kullanılabilen tutara oranıdır. Maliyeti artıran kalemler:

- Dosya masrafı ve kredi komisyonu
- Bloke tutulan mevduat veya kredi şartı olarak satılan sigorta ve benzeri ürünler
- Kredi işlemlerine ilişkin vergi ve fonlar (oranları kredi türüne ve mevzuata göre değişir)
- Faiz ödeme sıklığı (aylık bileşik faiz, yıllık nominal faizden yüksektir)

**Bankanın baktıkları:** Mali tablolar ve bağımsız denetim raporu, nakit akışı ve borç ödeme gücü, teminatlar, Findeks ve Risk Merkezi kayıtları, hesap hareketleri. Banka sizin için bir "kredi notu" oluşturur; bu not hem limiti hem de faizi belirler. Mali tablolarınızın vergi beyanlarıyla tutarlı olması, notu doğrudan etkiler.

**İlişki bankacılığı:** Petersen ve Rajan (1994), küçük işletmelerin bankalarla kurduğu yakın ilişkinin krediye erişimi kolaylaştırdığını göstermiştir. Bankanın sizi tanıması, bilgi asimetrisini azaltır. Öte yandan tek bir bankaya bağımlılık pazarlık gücünü azaltır ve o bankanın kredi politikasını sıkılaştırdığı dönemde sizi savunmasız bırakır.

**Limit yapısı:** Nakdi kredi (rotatif, spot, taksitli) ve gayrinakdi kredi (teminat mektubu, DBS, akreditif) limitleri ayrı değerlendirilir ama toplam riskiniz birlikte izlenir. Kullanmadığınız limitler için de komisyon ödeyebilirsiniz.

## Bir örnek

> **Örnek (temsili rakamlar):** Faiz, komisyon ve bloke oranları varsayımsaldır; vergi ve fonlar dahil edilmemiştir. Hesaplar `scripts/cards_numbers_eco_b7.py` ile yapılmıştır.

Bir banka 12 ay vadeli 10.000.000 TL işletme kredisi teklif ediyor: aylık faiz %3,5, yani yıllık nominal %42. Faiz aylık ödenirse yıllık bileşik maliyet %51,1.

Ek koşullar: %1 dosya masrafı (100.000 TL) ve kredinin %10'unun (1.000.000 TL) faizsiz hesapta bloke tutulması.

- Toplam faiz: 4.200.000 TL
- Fiilen kullanılabilen tutar: 8.900.000 TL
- **Efektif maliyet (basit): %48,3**

Bloke ve masraf hesaba katılmadığında %42 görünen teklifin efektif maliyeti %48,3. Daha yüksek nominal faizli ama koşulsuz bir teklif, gerçekte daha ucuz olabilir.

## Sık yapılan hatalar

- Teklifleri yalnızca nominal faizle karşılaştırmak.
- Bloke mevduat, zorunlu sigorta veya ürün satışlarını maliyete katmamak.
- Bankaya yalnızca kredi ihtiyacı olduğunda gitmek; düzenli bilgi paylaşmamak.
- Bütün kredi ve teminat ihtiyacını tek bankaya bağlamak.
- Kredi sözleşmelerindeki erken ödeme, faiz değişikliği ve temerrüt maddelerini okumamak.
- Kısa vadeli krediyle uzun vadeli yatırım finanse edip her yenilemede faiz riskine açık kalmak.

## Pratikte nasıl uygulanır?

- [ ] Kredi tekliflerini efektif maliyet tablosunda karşılaştırın.
- [ ] Bankalarla dönemsel olarak mali tablo ve bütçe paylaşın.
- [ ] Kredi, DBS ve teminat mektubu limitlerini en az iki-üç bankaya dağıtın.
- [ ] Findeks ve Risk Merkezi raporlarınızı düzenli kontrol edin.
- [ ] Kredi vadelerini, finanse edilen varlığın ömrüyle uyumlu hâle getirin.
- [ ] Kredi işlemlerine ilişkin güncel vergi ve fon oranlarını bankanızdan yazılı olarak isteyin.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın.

## Daha fazlası

- BDDK (2026). *Bankacılık Düzenleme ve Denetleme Kurumu (resmî site)*. https://www.bddk.org.tr
- TBB (2026). *Türkiye Bankalar Birliği (resmî site)*. https://www.tbb.org.tr
- Kredi Kayıt Bürosu (2026). *Findeks*. https://www.findeks.com
- Petersen, M. A.; Rajan, R. G. (1994). *The Benefits of Lending Relationships: Evidence from Small Business Data*. https://doi.org/10.1111/j.1540-6261.1994.tb04418.x
