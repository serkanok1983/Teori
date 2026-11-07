---
id: kb-eco-25-6-bond-types-treasury-instruments
title: "Tahvil, bono ve hazine araçları: Şirketin fazla nakdini nereye koymalı?"
summary: "İskontolu bono ile kuponlu tahvilin getirisinin nasıl hesaplandığını, faiz değiştiğinde tahvil fiyatının neden ters yönde hareket ettiğini ve şirketin geçici nakit fazlası için vade ve risk seçimini anlatır."
course: eco
category: finansal-piyasalar-ve-risk
tags: [finansal-piyasalar, nakit-yonetimi, faiz]
roles: [finans-muduru]
level: orta
source_lessons: [ECO-25.6]
reading_minutes: 3
key_points:
  - "İskontolu bono nominal değerinin altında satılır; getiri, alış fiyatı ile itfa değeri arasındaki farktır."
  - "Piyasa faizi yükselirse mevcut tahvillerin fiyatı düşer, faiz düşerse fiyatı yükselir."
  - "Vade uzadıkça faiz değişimine karşı fiyat duyarlılığı artar."
  - "Kısa vadeli bir getiriyi yıllıklaştırırken bileşik hesap kullanın."
  - "İşletme nakdi için öncelik getiriden önce anaparanın korunması ve ihtiyaç anında ulaşılabilirliktir."
glossary_terms: [hazine-bonosu, devlet-tahvili, kupon]
related: [kb-eco-25-1-time-value-npv-irr, kb-eco-18-3-real-vs-nominal-interest-fisher, kb-eco-50-3-working-with-banks, kb-eco-32-3-risk-management-stress-test]
sources:
  - title: "Hazine ve Maliye Bakanlığı (resmî site)"
    authors: "T.C. Hazine ve Maliye Bakanlığı"
    year: 2026
    type: web
    url: "https://www.hmb.gov.tr"
    verified: true
    checked_on: 2026-10-28
  - title: "Sermaye Piyasası Kurulu (resmî site)"
    authors: "SPK"
    year: 2026
    type: web
    url: "https://www.spk.gov.tr"
    verified: true
    checked_on: 2026-10-28
  - title: "Principles of Finance"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-finance/pages/1-why-it-matters"
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

Kampanya döneminden sonra ya da büyük bir tahsilattan sonra şirket hesabında birkaç aylık nakit birikebilir. Mevduat, hazine bonosu, devlet tahvili, fon ya da ters repo gibi seçenekler arasında karar verirken getiriyi doğru hesaplamanız ve riskleri bilmeniz gerekir. Bu kart temel araçları ve fiyat–faiz ilişkisini anlatır.

## Temel fikir

**Temel araçlar:**

- **Hazine bonosu:** Hazinenin bir yıldan kısa vadeli borçlanma aracı. Genellikle iskontolu satılır: Bugün nominal değerin altında ödersiniz, vadede nominal değeri alırsınız.
- **Devlet tahvili:** Bir yıldan uzun vadeli araç. Sabit kuponlu, değişken faizli, TÜFE'ye endeksli ya da döviz cinsinden olabilir.
- **Özel sektör tahvili ve finansman bonosu:** Şirketlerin ihraç ettiği araçlar. Getiri daha yüksektir, ama ihraççının kredi riski de vardır.

**Fiyat–faiz ilişkisi:** Sabit kuponlu bir tahvilin fiyatı, gelecekteki kupon ve anaparanın piyasa faiziyle iskonto edilmiş değeridir. Piyasa faizi yükselirse bu iskonto büyür ve fiyat düşer. Vadesinden önce satmak zorunda kalırsanız zarar edebilirsiniz.

**Riskler:** Faiz riski (fiyat dalgalanması), kredi riski (ihraççının ödeyememesi), likidite riski (istediğiniz anda satamama) ve enflasyon riski (sabit getirinin reel olarak erimesi). Vergi ve stopaj uygulamaları araç türüne göre değişir; seçim yapmadan önce mali müşavirinizle kontrol edin.

## Bir örnek

> **Örnek (temsili rakamlar):** Fiyat ve faiz oranları varsayımsaldır; güncel piyasa verisi değildir. Hesaplar `scripts/cards_numbers_eco_b3.py` ile yapılmıştır.

**İskontolu bono:** Nominal değer 100 TL olan bir yıllık bonoyu 80 TL'ye alıyorsunuz. Getiri = 100 / 80 − 1 = **%25**.

**Kısa vade:** 3 ay vadeli bonoyu 92 TL'ye alırsanız dönem getirisi %8,70. Bu getiriyi yılda dört kez tekrar ettiğinizi varsayarsanız yıllık bileşik karşılığı **%39,6**.

**Fiyat duyarlılığı:** %30 yıllık kuponlu, 2 yıl vadeli bir tahvil, piyasa faizi %30 iken 100,00 TL.

| Piyasa faizi | Tahvil fiyatı (TL) | Fiyat değişimi |
|---|---|---|
| %25 | 107,20 | %7,2 |
| %30 | 100,00 | %0,0 |
| %35 | 93,55 | −%6,4 |

Faiz 5 puan arttığında tahvil %6,4 değer kaybediyor. Bu nakde üç ay içinde ihtiyacınız varsa, 2 yıllık tahvil uygun bir araç değildir.

## Sık yapılan hatalar

- İşletme nakdini, ihtiyaç tarihinden daha uzun vadeli araçlara yatırmak.
- Yalnızca en yüksek getiriye bakıp ihraççının kredi riskini göz ardı etmek.
- Kısa vadeli getiriyi basit çarpımla yıllıklaştırıp farklı vadeleri yanlış karşılaştırmak.
- Vergi ve stopaj farklarını hesaba katmamak.
- Tek bir araca ya da tek bir kuruma yoğunlaşmak.
- Tahvilin vade sonuna kadar tutulmayacaksa faiz değişimlerinden kaynaklanan fiyat riskini göz ardı etmek.

## Pratikte nasıl uygulanır?

- [ ] Nakit fazlasını ihtiyaç zamanına göre üçe ayırın: hemen gerekebilecek, birkaç ay içinde gerekecek, uzun süre gerekmeyecek.
- [ ] Hemen gerekebilecek nakit için yalnızca kısa vadeli ve likit araçları kullanın.
- [ ] Farklı vadeleri yıllık bileşik net getiri üzerinden karşılaştırın.
- [ ] Yönetim kurulu onaylı yazılı bir nakit yatırım politikası oluşturun: izin verilen araçlar, vade ve kurum sınırları.
- [ ] Vergi etkisini ve aracın sizin için uygunluğunu mali müşavirinizle ve aracı kurumunuzla teyit edin.
- [ ] Aracı kurum ve bankaların komisyon ve saklama ücretlerini karşılaştırın.

## Daha fazlası

- T.C. Hazine ve Maliye Bakanlığı (2026). *Hazine ve Maliye Bakanlığı (resmî site)*. https://www.hmb.gov.tr
- SPK (2026). *Sermaye Piyasası Kurulu (resmî site)*. https://www.spk.gov.tr
- OpenStax (2026). *Principles of Finance*. https://openstax.org/books/principles-finance/pages/1-why-it-matters
