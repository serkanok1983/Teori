---
id: kb-ea-21-3-erp-market-turkey
title: "ERP pazarı: Küresel paketler, açık kaynak ve Türkiye'deki yerli çözümler"
summary: "Büyük küresel ERP paketleri, orta ölçekli ve açık kaynak seçenekler ile Türkiye'de yaygın yerli ERP üreticilerini; yerelleştirme ihtiyaçları (Tekdüzen hesap planı, e-belgeler, bordro) ve seçimde sorulacak sorular üzerinden tanıtır."
course: ea
category: erp
tags: [erp, pazar, yerellestirme, tedarikci-secimi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, it-yoneticisi]
level: temel
source_lessons: [EA-21.1, EA-21.2, EA-21.3]
reading_minutes: 3
key_points:
  - "ERP pazarı kabaca küresel büyük paketler, orta ölçekli/açık kaynak çözümler ve yerli üreticiler olarak gruplanabilir."
  - "Türkiye'de yerelleştirme; Tekdüzen hesap planı, e-belgeler ve bordro mevzuatı demektir."
  - "Bu üç alanın üretici tarafından mı, iş ortağı tarafından mı karşılandığını sorun."
  - "Pazar payı ve fiyat bilgisini yalnızca doğrulanabilir kaynaklardan alın."
  - "Ürün adları ve kapsamları sık değişir; teklif aşamasında güncel bilgiyi isteyin."
glossary_terms: [erp, yerellestirme]
related: [kb-ea-20-1-what-erp-does, kb-ea-17-4-vendor-selection-rfp, kb-ea-37-1-e-document-map, kb-ea-22-1-chart-of-accounts-tekduzen, kb-ea-5-5-erp-core-vs-best-of-breed]
sources:
  - title: "Logo Yazılım kurumsal web sitesi"
    authors: "Logo Yazılım"
    year: 2026
    type: web
    url: "https://www.logo.com.tr/"
    verified: true
    checked_on: 2026-10-28
  - title: "Mikro Yazılım kurumsal web sitesi"
    authors: "Mikro Yazılım"
    year: 2026
    type: web
    url: "https://www.mikro.com.tr/"
    verified: true
    checked_on: 2026-10-28
  - title: "Odoo Documentation"
    authors: "Odoo S.A."
    year: 2026
    type: web
    url: "https://www.odoo.com/documentation/"
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

ERP seçimine başlayan bir üretici ya da bayi, ilk olarak "kimler var?" sorusuyla karşılaşır. Bu kart pazarı kaba gruplara ayırır ve Türkiye'ye özgü yerelleştirme ihtiyaçlarını hatırlatır. Amaç bir ürün önermek değil, doğru soruları sormanıza yardım etmektir.

## Temel fikir

ERP pazarını üç grupta düşünebilirsiniz:

- **Küresel büyük paketler:** SAP, Oracle ve Microsoft gibi üreticilerin ürünleri. Geniş kapsam ve çok ülkeli yapı sunarlar; uygulama genellikle iş ortakları üzerinden yapılır ve proje maliyeti yüksektir.
- **Orta ölçekli ve açık kaynak çözümler:** Odoo veya ERPNext gibi modüler yapılar. Modülleri ihtiyaca göre ekleme imkânı verir; Türkiye yerelleştirmesinin kim tarafından sağlandığını ayrıca kontrol etmek gerekir.
- **Yerli üreticiler:** Logo, Mikro, Nebim (perakende ağırlıklı), Canias gibi firmalar. Türk mevzuatına yakın oldukları için e-belge, Tekdüzen hesap planı ve bordro tarafında genellikle hazır çözüm sunarlar.

Türkiye'de **yerelleştirme** üç başlıkta toplanır:

1. **Tekdüzen hesap planı** ve yasal raporlar.
2. **e-Belgeler:** e-Fatura, e-Arşiv, e-İrsaliye, e-Defter ve bunların entegratör bağlantısı.
3. **Bordro:** SGK bildirimleri, vergi dilimleri, asgari ücret değişiklikleri.

Bu alanlarda mevzuat sık değiştiği için asıl soru, güncellemenin **ne kadar hızlı ve kimin sorumluluğunda** yapıldığıdır.

Pazar payı, müşteri sayısı ve fiyat gibi bilgileri broşür ya da sunumlardan değil, doğrulanabilir kaynaklardan alın. Bu kartta bu tür rakamlara bilerek yer verilmemiştir.

### Kısa listeyi oluşturmak

Pazarda çok sayıda seçenek bulunduğu için, değerlendirmeye geçmeden önce kısa bir liste oluşturmak gerekir. Bunun için şirketinizin ölçeği, sektörünüze özgü ihtiyaçlar (saha satışı, depo, e-belge, çok şirketli yapı), bulut veya şirket içi kurulum tercihi ve bütçe aralığı ölçüt olarak kullanılabilir. Yerel mevzuat desteğinin kalitesi ve güncellenme hızı, Türkiye'de faaliyet gösteren şirketler için önemli bir ölçüttür. Ayrıca ürünün sizin bölgenizde ve sektörünüzde deneyimli uygulama ortaklarının bulunup bulunmadığı araştırılmalıdır. Ürün ve fiyat bilgileri sık değiştiği için güncel bilgiyi doğrudan üreticilerden ve referans müşterilerden almak gerekir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b5.py` ile yapılmıştır.

120 kullanıcılı bir dağıtıcı, uzun listeye 7 ürün alıyor. Yerelleştirme ve iş ortağı desteği sorularıyla liste 3 ürüne iniyor. Demolarda her üreticiden, firmanın kullandığı 6 e-belge senaryosunu (ör. temel fatura, iade, ihracat kayıtlı satış) canlı göstermesi isteniyor. Son ikisi için benzer ölçekte bir müşteriye referans ziyareti yapılıyor. Ziyarette kullanıcıların en çok şikâyet ettiği konu, mevzuat güncellemelerinin geç gelmesi oluyor; bu konu sözleşmeye hizmet seviyesi maddesi olarak ekleniyor.

## Sık yapılan hatalar

- Ürünü marka bilinirliğine göre seçmek.
- Yerelleştirmenin "hazır" olduğunu varsayıp demoda göstermesini istememek.
- Uygulama iş ortağının deneyimini ürün kadar sorgulamamak.
- Sunumdaki pazar payı rakamlarını doğrulamadan kullanmak.

## Pratikte nasıl uygulanır?

- [ ] Kısa listeyi yerelleştirme, ölçek ve iş ortağı desteği üzerinden daraltın.
- [ ] Demoda kendi e-belge senaryolarınızı ve bir bordro örneğini isteyin.
- [ ] Mevzuat güncellemesinin süresini ve sorumlusunu sözleşmeye yazın.
- [ ] Benzer ölçekteki bir müşteriyle görüşün.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın. Ürün adları ve kapsamları üretici sitelerinden derlenmiştir; satın alma kararından önce güncel bilgiyi üreticiden yazılı olarak isteyin.

## Daha fazlası

- Logo Yazılım: https://www.logo.com.tr/
- Mikro Yazılım: https://www.mikro.com.tr/
- Odoo dokümantasyonu: https://www.odoo.com/documentation/
