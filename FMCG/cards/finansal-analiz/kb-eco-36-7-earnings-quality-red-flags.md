---
id: kb-eco-36-7-earnings-quality-red-flags
title: "Kâr kalitesi ve uyarı işaretleri: Kâr gerçek mi?"
summary: "Raporlanan kârın nakde dönüşüp dönüşmediğini ölçmeyi, tahakkuk oranını, alacak ve stok sürelerindeki ani uzamaları, dönem sonu satış yüklemelerini ve ilişkili taraf işlemlerini müşteri, tedarikçi ve kendi şirketiniz için uyarı işaretleri olarak okumayı anlatır."
course: eco
category: finansal-analiz
tags: [finansal-analiz, kar-kalitesi, risk]
roles: [finans-muduru]
level: ileri
source_lessons: [ECO-36.7]
reading_minutes: 3
key_points:
  - "Kalitesi yüksek kâr, zaman içinde nakde dönüşür."
  - "Net kâr ile işletme nakit akışı arasındaki fark sürekli büyüyorsa, kâr tahakkuklardan geliyordur."
  - "Alacak ve stok sürelerinin aniden uzaması, dönem sonu satış yüklemeleri ve ilişkili taraf işlemleri tipik uyarı işaretleridir."
  - "Uyarı işaretleri kanıt değildir; daha fazla soru sorulmasını gerektirir."
glossary_terms: [kar-kalitesi, tahakkuk-orani, iliskili-taraf-islemi]
related: [kb-eco-33-7-reading-annual-report, kb-eco-36-6-cash-flow-vs-profit, kb-eco-37-3-customer-credit-analysis, kb-eco-37-4-distress-signals-z-score]
sources:
  - title: "Do Stock Prices Fully Reflect Information in Accruals and Cash Flows about Future Earnings?"
    authors: "Sloan, R. G."
    year: 1996
    type: article
    doi: "10.2308/tar-9608042309"
    url: "https://doi.org/10.2308/tar-9608042309"
    verified: true
    checked_on: 2026-10-28
    note: "The Accounting Review 71(3). Tahakkuk ağırlıklı kârın kalıcılığı."
  - title: "The Quality of Accruals and Earnings: The Role of Accrual Estimation Errors"
    authors: "Dechow, P. M.; Dichev, I. D."
    year: 2002
    type: article
    doi: "10.2308/accr.2002.77.s-1.35"
    url: "https://doi.org/10.2308/accr.2002.77.s-1.35"
    verified: true
    checked_on: 2026-10-28
    note: "The Accounting Review 77(s-1)."
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

Büyük bir müşteriniz her yıl kâr açıklıyor ama ödemeleri gecikiyorsa ya da kendi satış ekibiniz dönem sonlarında olağanüstü satış yapıyorsa, raporlanan kârın kalitesini sorgulamanız gerekir. Bu kart, kâr kalitesini ölçmenizi ve uyarı işaretlerini erken fark etmenizi sağlar.

## Temel fikir

**Tahakkuk oranı:** Net kâr ile işletme nakit akışı arasındaki fark, ortalama toplam varlıklara bölünür. Sloan (1996), kârın tahakkuk bileşeni yüksek olan şirketlerin kârlılığının daha az kalıcı olduğunu göstermiştir. Dechow ve Dichev (2002) ise tahakkukların nakde dönüşme derecesini kâr kalitesinin bir ölçüsü olarak önermiştir.

**Distribütörler için tipik uyarı işaretleri:**

- Alacak süresi satıştan bağımsız olarak hızla uzuyor.
- Stok süresi uzuyor; özellikle yavaş dönen ve son kullanma tarihi yaklaşan stok artıyor.
- Dönem sonlarında olağandışı satış artışı, sonraki dönem başında iadeler.
- Tedarikçi primlerinin ve ciro primlerinin tahmini tutarlarla kâra yazılması.
- İlişkili taraflarla (ortakların diğer şirketleri) büyük tutarlı satış ve alacaklar.
- Karşılıklarda ani azalma ya da muhasebe yöntemlerinde değişiklik.
- Denetçi değişikliği veya şartlı görüş.

### İşaretleri nasıl araştırırsınız?

Bir uyarı işareti, kesin bir sorun olduğunu göstermez; daha fazla soru sormanız gerektiğini gösterir:

- **Alacak süresi uzuyorsa:** Yaşlandırma tablosunu ve en büyük alacakların listesini isteyin. Vadesi çok geçmiş, ilişkili taraf veya tek bir büyük müşteriye yoğunlaşmış alacaklar var mı?
- **Dönem sonu satışları yüksekse:** Sonraki ayın iade ve iskonto kayıtlarına bakın. Faturası kesilmiş ama sevk edilmemiş mal var mı?
- **Tedarikçi primleri yüksekse:** Primlerin hangi sözleşmeye dayandığını ve tahsil edilip edilmediğini kontrol edin.
- **Karşılıklar azaldıysa:** Bu değişikliğin gerekçesini ve önceki yılların gerçekleşmelerini sorun.

### Kimin için önemlidir?

- **Müşteri değerlendiren tedarikçi:** Büyük bir müşterinin kârı güçlü görünürken nakit akışı zayıfsa, vade ve limit kararlarında daha temkinli olun.
- **Şirket satın alan veya ortak alan yatırımcı:** Düzeltilmiş kâr ve nakit akışı, değerlemenin temelidir.
- **Kendi şirketiniz:** Yönetim raporlarınızda bu işaretleri kendiniz izlerseniz, bankalar ve denetçilerle görüşmelere daha hazırlıklı girersiniz.

## Bir örnek

> **Örnek (temsili rakamlar):** Tutarlar varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b5.py` ile yapılmıştır.

Bir müşterinizin son üç yılda toplam net kârı 8.000.000 TL. Aynı dönemde işletme faaliyetlerinden toplam 3.000.000 TL nakit çıkışı olmuş. Kâr ile nakit arasındaki fark 11.000.000 TL; ortalama toplam varlıklar 100.000.000 TL olduğuna göre üç yıllık tahakkuk oranı **%11**.

Aynı dönemde alacak süresi 55 günden 80 güne uzamış.

Yorum: Kâr nakde dönüşmüyor ve alacaklar şişiyor. Bu, şirketin satışlarını uzun vadeyle zorladığını, tahsil edilemeyen alacaklar için yeterli karşılık ayırmadığını ya da ilişkili taraflara satış yaptığını gösterebilir. Kredi limitini artırmadan önce dipnotları ve alacak yaşlandırmasını isteyin.

## Sık yapılan hatalar

- Müşterinin kârlı olmasını ödeme gücü sanmak.
- Uyarı işaretlerini tek tek görüp birlikte değerlendirmemek.
- Kendi şirketinizde dönem sonu satış yüklemelerini hedef baskısının doğal sonucu olarak kabul etmek.
- İlişkili taraf işlemlerini incelememek.
- Bir uyarı işaretini doğrudan usulsüzlük kanıtı saymak.

## Pratikte nasıl uygulanır?

- [ ] Önemli müşterileriniz için kâr ile işletme nakit akışını yıllık karşılaştırın.
- [ ] Kendi şirketinizde dönem sonu satışlarını ve sonraki ay iadelerini izleyin.
- [ ] İlişkili taraf satış ve alacaklarını ayrı raporlayın.
- [ ] Uyarı işaretleri için basit bir kontrol listesi hazırlayın ve kredi kararlarına bağlayın.
- [ ] Şüpheli bir durumda karar vermeden önce mali müşavir veya denetçi görüşü alın.

## Daha fazlası

- Sloan, R. G. (1996). *Do Stock Prices Fully Reflect Information in Accruals and Cash Flows about Future Earnings?*. https://doi.org/10.2308/tar-9608042309
- Dechow, P. M.; Dichev, I. D. (2002). *The Quality of Accruals and Earnings: The Role of Accrual Estimation Errors*. https://doi.org/10.2308/accr.2002.77.s-1.35
- OpenStax (2026). *Principles of Accounting, Volume 1: Financial Accounting*. https://openstax.org/books/principles-financial-accounting/pages/1-why-it-matters
