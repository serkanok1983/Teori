---
id: kb-eco-38-3-distributor-credit-risk-dbs
title: "Distribütörde kredi riski ve DBS: Tedarikçi limiti, teminat ve banka garantisi"
summary: "Distribütörün iki yönlü kredi riskini, yani müşterilerine açtığı ve tedarikçisinin ona açtığı krediyi, Doğrudan Borçlandırma Sistemi'nin (DBS) işleyişini, DBS limitinin satın alma hacmi ve vadeyle uyumunu ve teminat türlerinin karşılaştırmasını anlatır."
course: eco
category: finansal-analiz
tags: [kredi-riski, finansman, tedarikci]
roles: [bayi-sahibi, bayi-yonetici, finans-muduru]
level: orta
source_lessons: [ECO-38.3]
reading_minutes: 3
key_points:
  - "Distribütör hem müşterilerine kredi verir hem de tedarikçisinden kredi alır."
  - "DBS'de banka, alıcının tedarikçiye olan faturalarını vade gününde, alıcıya tanınan limit dahilinde öder."
  - "Gereken DBS limiti, aylık alım ile vade süresine bağlıdır; limit yetersizse sevkiyatlar aksar."
  - "Teminat türlerinin maliyeti, likiditesi ve hukuki gücü birbirinden farklıdır."
glossary_terms: [dbs, teminat-mektubu, kredi-limiti]
related: [kb-eco-37-3-customer-credit-analysis, kb-eco-38-2-cash-conversion-cycle, kb-eco-34-2-receivables-doubtful-debts, kb-eco-50-4-tcmb-policy-rate-credit]
sources:
  - title: "Türkiye Bankalar Birliği (resmî site)"
    authors: "TBB"
    year: 2026
    type: web
    url: "https://www.tbb.org.tr"
    verified: true
    checked_on: 2026-10-28
  - title: "Bankacılık Düzenleme ve Denetleme Kurumu (resmî site)"
    authors: "BDDK"
    year: 2026
    type: web
    url: "https://www.bddk.org.tr"
    verified: true
    checked_on: 2026-10-28
  - title: "Trade Credit: Theories and Evidence"
    authors: "Petersen, M. A.; Rajan, R. G."
    year: 1997
    type: article
    doi: "10.1093/rfs/10.3.661"
    url: "https://doi.org/10.1093/rfs/10.3.661"
    verified: true
    checked_on: 2026-10-28
    note: "Review of Financial Studies 10(3). Ticari kredinin işlevi."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Büyük üreticiler, distribütörlerine açtıkları krediyi çoğu zaman banka garantisiyle güvenceye alır. Bu yapının en yaygın biçimlerinden biri DBS'dir. Bu kart, DBS'nin işleyişini, limit ihtiyacınızı hesaplamayı ve teminat seçeneklerini karşılaştırmayı anlatır.

## Temel fikir

**İki yönlü kredi:** Distribütör, bir yanda müşterilerine vade verir (alacak riski), diğer yanda tedarikçisinden vade alır. Tedarikçi, distribütörün ödeme riskini sınırlamak için teminat ister.

**DBS (Doğrudan Borçlandırma Sistemi):**

- Banka, distribütöre tedarikçi ödemeleri için bir limit tanır.
- Tedarikçi faturalarını sisteme yükler; banka vade gününde distribütörün hesabından ödeme yapar.
- Hesapta yeterli bakiye yoksa banka, limit dahilinde ödemeyi yapar ve distribütörü kredilendirir.
- Böylece tedarikçi için tahsilat riski büyük ölçüde bankaya geçer.

Sistemin işleyiş ayrıntıları, ücretleri ve kredilendirme koşulları bankaya ve sözleşmeye göre değişir; kendi sözleşmenizi bankanızla netleştirin.

**Diğer teminat türleri:** Teminat mektubu, ipotek, müşteri çek ve senetlerinin ciro edilmesi, kefalet. Her birinin maliyeti, hazırlanma süresi ve tedarikçi gözündeki gücü farklıdır.

### DBS'nin distribütöre maliyeti

DBS ilk bakışta tedarikçinin aracı gibi görünse de distribütör için de bir kredi ürünüdür:

- DBS limiti, bankanın size tanıdığı toplam kredi riskinin bir parçasıdır. Diğer kredi limitlerinizi daraltabilir.
- Vade gününde bakiyeniz yoksa kullanılan tutar faizli krediye dönüşür. Bu faiz, normal kredi faizinden yüksek olabilir.
- Banka limit tahsisi için komisyon alabilir ve teminat isteyebilir.

### Nakit planlaması

DBS ödemeleri belirli günlerde otomatik olarak gerçekleşir. Bu yüzden haftalık nakit planınızda DBS vadelerini ayrı bir satırda izleyin. Müşteri tahsilatlarınızın vadesiyle DBS ödeme günleri uyumsuzsa, sürekli kısa süreli kredi kullanırsınız.

### Tedarikçiyle müzakere

Teminat türü, vadeyle birlikte müzakere edilmelidir. Örneğin DBS veya teminat mektubu sunduğunuzda tedarikçinin riski azalır; karşılığında daha uzun vade, daha yüksek limit veya daha iyi fiyat talep edebilirsiniz. Teminat maliyetini (komisyon, bloke) tedarikçinin sağladığı avantajla karşılaştırın. Birden fazla tedarikçiyle çalışıyorsanız, teminatlarınızın toplamını ve hangi bankada ne kadar limit kullandığınızı tek bir tabloda izleyin.

## Bir örnek

> **Örnek (temsili rakamlar):** Tutarlar ve süreler varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b5.py` ile yapılmıştır.

Bir distribütörün ana tedarikçisinden aylık alımı 15.000.000 TL; vade 45 gün. Herhangi bir anda açık fatura tutarı yaklaşık **22.500.000 TL.**

DBS limiti ise 20.000.000 TL. Aradaki 2.500.000 TL'lik açık nedeniyle yeni faturalar sisteme yüklenemez ve sevkiyatlar gecikir; özellikle kampanya ve sezon dönemlerinde ciddi satış kaybı yaşanır.

Seçenekler: Limiti artırmak için bankayla görüşmek, ek teminat vermek ya da vadeyi kısaltmak. Mevcut limitle sorunsuz çalışmak için vade en fazla 40 gün olmalı.

## Sık yapılan hatalar

- DBS limitini sezonsal alım artışlarını hesaba katmadan belirlemek.
- DBS'yi bedava finansman sanmak; vadesinde ödenmeyen tutarların kredilendirme maliyetini göz ardı etmek.
- Tedarikçi riskini teminatla, müşteri riskini ise teminatsız yönetmek; iki taraf arasında uyumsuzluk yaratmak.
- Teminat mektubu ve DBS komisyonlarını ürün kârlılığına yansıtmamak.
- Tek bir bankaya bağımlı kalmak.

## Pratikte nasıl uygulanır?

- [ ] Her tedarikçi için gereken limiti aylık alım ve vadeye göre hesaplayıp sezonsal tepe değeriyle karşılaştırın.
- [ ] DBS ve teminat maliyetlerini bir tabloda toplayın ve tedarikçi kârlılığına yansıtın.
- [ ] Limitlerinizi birden fazla bankaya dağıtmayı değerlendirin.
- [ ] Müşteri tarafındaki teminat politikanızı tedarikçi tarafındaki yükümlülüklerinizle uyumlu hâle getirin.
- [ ] Sözleşme koşullarını bankanız ve hukuk danışmanınızla gözden geçirin.

## Daha fazlası

- TBB (2026). *Türkiye Bankalar Birliği (resmî site)*. https://www.tbb.org.tr
- BDDK (2026). *Bankacılık Düzenleme ve Denetleme Kurumu (resmî site)*. https://www.bddk.org.tr
- Petersen, M. A.; Rajan, R. G. (1997). *Trade Credit: Theories and Evidence*. https://doi.org/10.1093/rfs/10.3.661
