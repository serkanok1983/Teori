---
id: kb-eco-54-3-governance-sustainability-reporting
title: "Kurumsal yönetim ve sürdürülebilirlik raporlaması: İlk adımlar"
summary: "Kurumsal yönetimin temel ilkelerini, sürdürülebilirlik raporlamasının finansal raporlamayla bağlantısını, kapsam 1 ve kapsam 2 emisyonlarının basit hesabını ve müşteriler ile finansman kuruluşlarından gelen veri taleplerine hazırlığı anlatır."
course: eco
category: finansal-piyasalar-ve-risk
tags: [yonetisim, surdurulebilirlik, raporlama, emisyon]
roles: [uretici-sahibi, bayi-sahibi]
level: ileri
source_lessons: [ECO-54.3]
reading_minutes: 3
key_points:
  - "Kurumsal yönetim, şirketin karar alma, denetim ve hesap verme düzenidir."
  - "Sürdürülebilirlik raporlaması, iklim ve diğer sürdürülebilirlik risklerinin şirket değerine etkisini açıklamayı amaçlar."
  - "Kapsam 1 doğrudan emisyonları, kapsam 2 satın alınan enerjiden kaynaklanan emisyonları kapsar."
  - "Raporlama zorunluluğu olmasa da büyük müşteriler ve bankalar bu verileri giderek daha fazla istemektedir."
glossary_terms: [kurumsal-yonetim, surdurulebilirlik-raporlamasi, kapsam-1-2-emisyon, tsrs]
related: [kb-eco-31-5-agency-governance-family-firm, kb-eco-40-4-environmental-taxes-cbam, kb-eco-33-7-reading-annual-report, kb-eco-35-1-reporting-regimes-tr]
sources:
  - title: "Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu (resmî site)"
    authors: "KGK"
    year: 2026
    type: web
    url: "https://www.kgk.gov.tr"
    verified: true
    checked_on: 2026-10-28
    note: "TFRS/TMS ve BOBİ FRS metinlerinin Türkiye'deki yayımcısı."
  - title: "General Sustainability-related Disclosures (IFRS S1) — project page"
    authors: "IFRS Foundation"
    year: 2026
    type: web
    url: "https://www.ifrs.org/projects/completed-projects/2023/general-sustainability-related-disclosures/"
    verified: true
    checked_on: 2026-10-28
  - title: "Sermaye Piyasası Kurulu (resmî site)"
    authors: "SPK"
    year: 2026
    type: web
    url: "https://www.spk.gov.tr"
    verified: true
    checked_on: 2026-10-28
  - title: "Theory of the firm: Managerial behavior, agency costs and ownership structure"
    authors: "Jensen, M. C.; Meckling, W. H."
    year: 1976
    type: article
    doi: "10.1016/0304-405X(76)90026-X"
    url: "https://doi.org/10.1016/0304-405X(76)90026-X"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Financial Economics 3(4)."
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Uluslararası müşteriler, AB'ye ihracat yapan üreticiler ve bankalar, tedarikçi ve distribütörlerinden giderek daha fazla yönetim ve sürdürülebilirlik bilgisi istiyor. Bu kart, kurumsal yönetimin temel unsurlarını ve sürdürülebilirlik raporlamasına başlamak için gereken ilk adımları anlatır.

## Temel fikir

**Kurumsal yönetim:** Ortaklar, yönetim ve diğer paydaşlar arasındaki ilişkiyi düzenleyen kurallar. Temel unsurlar: yönetim kurulunun yapısı, iç kontrol ve iç denetim, bağımsız denetim, ilişkili taraf işlemlerinin şeffaflığı ve yetki matrisi. Jensen ve Meckling (1976), sahiplik ile yönetimin ayrılmasından doğan vekalet maliyetlerini açıklar. Halka açık şirketler için Sermaye Piyasası Kurulu'nun kurumsal yönetim düzenlemeleri de bulunur; halka açık olmayan aile şirketleri bu ilkeleri gönüllü olarak örnek alabilir.

**Sürdürülebilirlik raporlaması:** Türkiye'de Kamu Gözetimi Kurumu, ISSB standartlarıyla uyumlu Türkiye Sürdürülebilirlik Raporlama Standartlarını (TSRS) yayımlamıştır. Hangi şirketlerin hangi tarihten itibaren raporlama yapacağı KGK düzenlemeleriyle belirlenir ve değişebilir. Raporlama zorunluluğu olmayan şirketler de büyük müşterilerinin ve bankalarının değer zinciri verisi talepleri nedeniyle dolaylı olarak etkilenir.

**Sera gazı emisyonu kapsamları:**

- **Kapsam 1:** Şirketin kendi kaynaklarından doğrudan emisyon (araç yakıtı, kazan).
- **Kapsam 2:** Satın alınan elektrik ve ısıdan kaynaklanan dolaylı emisyon.
- **Kapsam 3:** Değer zincirindeki diğer dolaylı emisyonlar (tedarikçiler, ürünlerin taşınması ve kullanımı).

Basit hesap: Tüketim miktarı × emisyon faktörü.

## Bir örnek

> **Örnek (temsili rakamlar):** Tüketimler, ciro ve emisyon faktörleri **örnek değerdir**; resmî faktör değildir. Hesaplar `scripts/cards_numbers_eco_b7.py` ile yapılmıştır.

Bir distribütörün araç filosu yılda 200.000 litre motorin, depoları 1.000.000 kWh elektrik tüketiyor.

- Kapsam 1: 200.000 litre × 2,68 kg CO₂/litre ≈ **536 ton CO₂**
- Kapsam 2: 1.000.000 kWh × 0,44 kg CO₂/kWh ≈ **440 ton CO₂**
- Toplam: 976 ton CO₂

Yıllık ciro 500 milyon TL ise emisyon yoğunluğu milyon TL başına yaklaşık 1,95 ton. Bu basit tablo, müşteri anketlerine yanıt vermek ve azaltım hedefi koymak için başlangıç noktasıdır. Rota optimizasyonu, araç yenileme ve yenilenebilir elektrik tedariki en doğrudan azaltım kalemleridir.

## Sık yapılan hatalar

- Sürdürülebilirlik raporlamasını yalnızca halkla ilişkiler belgesi olarak görmek.
- Verileri kaynak belgeye dayanmadan tahminle doldurmak.
- Emisyon faktörlerinin kaynağını ve yılını belirtmemek.
- Yönetim kurulunda iklim ve sürdürülebilirlik risklerinin sorumlusunu belirlememek.
- Aile şirketlerinde ilişkili taraf işlemlerini kayıt dışı veya belgesiz bırakmak.
- Müşteri anketlerine farklı birimlerin farklı rakamlarla yanıt vermesi.

## Pratikte nasıl uygulanır?

- [ ] Yakıt ve elektrik faturalarından aylık tüketim tablosu oluşturun.
- [ ] Resmî veya uluslararası kabul görmüş kaynaklardan güncel emisyon faktörlerini alın ve kaynağını not edin.
- [ ] Yönetim kurulunda sürdürülebilirlik ve risk konularından sorumlu bir üye veya komite belirleyin.
- [ ] Yetki matrisi ve ilişkili taraf işlemleri politikasını yazılı hâle getirin.
- [ ] Raporlama zorunluluğunuz olup olmadığını güncel KGK düzenlemeleri üzerinden denetçinizle kontrol edin.
- [ ] Sürdürülebilirlik verileri için tek bir sorumlu ve tek bir veri kaynağı belirleyin.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın.

## Daha fazlası

- KGK (2026). *Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu (resmî site)*. https://www.kgk.gov.tr
- IFRS Foundation (2026). *General Sustainability-related Disclosures (IFRS S1) — project page*. https://www.ifrs.org/projects/completed-projects/2023/general-sustainability-related-disclosures/
- SPK (2026). *Sermaye Piyasası Kurulu (resmî site)*. https://www.spk.gov.tr
- Jensen, M. C.; Meckling, W. H. (1976). *Theory of the firm: Managerial behavior, agency costs and ownership structure*. https://doi.org/10.1016/0304-405X(76)90026-X
