---
id: kb-eco-37-3-customer-credit-analysis
title: "Müşteri kredi analizi: Kime ne kadar vade ve limit verilir?"
summary: "Bir müşteriye açılacak kredi limitini ödeme geçmişi, finansal tablolar, Findeks gibi kayıtlar ve teminatlarla değerlendirmeyi, risk tutarını ve beklenen zararı hesaplamayı ve beklenen zararı müşterinin getirdiği kârla karşılaştırarak limit ve vade kararı vermeyi anlatır."
course: eco
category: finansal-analiz
tags: [kredi-riski, alacak-yonetimi, musteri]
roles: [bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: orta
source_lessons: [ECO-37.3]
reading_minutes: 3
key_points:
  - "Vadeli satış, müşteriye verilen teminatsız bir kredidir."
  - "Risk tutarı, aylık alım ile vade süresinden kabaca tahmin edilebilir."
  - "Beklenen zarar = Temerrüt olasılığı × Temerrüt hâlinde kayıp oranı × Risk tutarı."
  - "Bir müşterinin batması durumundaki kayıp, o müşteriden aylarca elde edilen brüt kârı silebilir."
glossary_terms: [kredi-limiti, temerrut-olasiligi, beklenen-kredi-zarari]
related: [kb-eco-34-2-receivables-doubtful-debts, kb-eco-38-3-distributor-credit-risk-dbs, kb-eco-37-4-distress-signals-z-score, kb-eco-33-7-reading-annual-report]
sources:
  - title: "Findeks"
    authors: "Kredi Kayıt Bürosu"
    year: 2026
    type: web
    url: "https://www.findeks.com"
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

Distribütörler, müşterilerine bankalardan çok daha fazla kredi verir; ama bunu çoğu zaman bir banka kadar sistemli yapmaz. Bu kart, müşteri limitlerini veriye dayalı belirlemenizi ve riski kârla karşılaştırmanızı sağlar.

## Temel fikir

**Bilgi kaynakları:**

- **Kendi ödeme geçmişiniz:** Ortalama gecikme, karşılıksız çek ya da protestolu senet geçmişi.
- **Finansal tablolar:** Özellikle büyük müşteriler için kârlılık, borçluluk ve alacak süresi.
- **Dış kayıtlar:** Findeks gibi kredi raporları (müşterinin onayıyla), ticaret sicili bilgileri, sektördeki diğer tedarikçilerden gelen bilgiler.
- **Saha bilgisi:** Satış temsilcisinin gözlemleri, mağaza trafiği, ortaklık değişiklikleri.

Petersen ve Rajan (1997), ticari kredinin tedarikçilerin müşteriler hakkında bankalardan daha iyi bilgiye sahip olabildiği durumlarda önem kazandığını tartışır. Bu bilgi avantajını sistemli kullanmak gerekir.

**Hesap:**

- **Risk tutarı:** Aylık alım × (vade gün / 30), artı sipariş aşamasındaki tutar.
- **Beklenen zarar:** Temerrüt olasılığı × Temerrüt hâlinde kayıp oranı × Risk tutarı.
- **Karşılaştırma:** Beklenen zarar ve finansman maliyeti, müşteriden elde edilen brüt kârla karşılaştırılır.

### Müşterileri sınıflandırmak

Her müşteri için aynı derinlikte analiz yapmak maliyetlidir. Risk tutarına göre kademeli bir süreç kurun:

- **Küçük riskler:** Ödeme geçmişi ve temel kayıt kontrolüyle otomatik limit.
- **Orta riskler:** Kredi raporu, ticaret sicili bilgileri ve satış temsilcisi değerlendirmesi.
- **Büyük riskler:** Finansal tablo analizi, ziyaret, teminat ve yönetim onayı.

Her müşteriye bir risk notu verin (ör. A, B, C, D) ve vade, limit ve teminat koşullarını bu nota bağlayın.

### Limiti güncel tutmak

Kredi limiti bir kez belirlenip unutulmamalıdır. Müşterinin alımları, ödeme davranışı ve dış kayıtlarındaki değişiklikler düzenli olarak izlenmeli; büyük müşterilerde limitler en az yılda bir yeniden değerlendirilmelidir. Limit aşımı taleplerini kimin onaylayacağı yazılı olmalıdır.

### Kişisel verilerin korunması

Gerçek kişi müşteriler veya şahıs işletmeleri hakkında kredi bilgisi toplarken kişisel verilerin korunması mevzuatına uyun. Kredi raporu gibi bilgileri ancak müşterinin onayıyla ve amacına uygun olarak kullanın.

## Bir örnek

> **Örnek (temsili rakamlar):** Olasılık, kayıp oranı ve tutarlar varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b5.py` ile yapılmıştır.

Bir market zinciri ayda 2.000.000 TL alım yapıyor ve 60 gün vade istiyor. Risk tutarı yaklaşık **4.000.000 TL.**

Bir yıllık temerrüt olasılığı %5, temerrüt hâlinde kayıp oranı %60 kabul edilirse beklenen yıllık zarar 120.000 TL. Müşteri yılda 24.000.000 TL alım yapıyor; %8 brüt marjla 1.920.000 TL brüt kâr getiriyor. Beklenen zarar brüt kârın küçük bir kısmı.

Ama müşteri batarsa kayıp 2.400.000 TL olur; bu, müşteriden yaklaşık 15,0 ayda elde edilen brüt kâra eşit. Bu yüzden limiti teminatla desteklemek ya da vadeyi kısaltmak değerlendirilmelidir.

## Sık yapılan hatalar

- Limiti satış ekibinin talebine göre belirlemek.
- Büyük müşteriye "zaten büyük" diye analiz yapmamak.
- Limitleri yılda bir kez belirleyip ödeme davranışı değiştiğinde güncellememek.
- Teminatları (çek, senet, teminat mektubu, DBS) değerlerini kontrol etmeden kabul etmek.
- Tek bir müşteriye aşırı yoğunlaşmak.

## Pratikte nasıl uygulanır?

- [ ] Müşterileri risk sınıflarına ayırın (ör. A, B, C) ve her sınıf için limit ve vade kuralları belirleyin.
- [ ] Yeni müşteri ve limit artışı için standart bir değerlendirme formu kullanın.
- [ ] Büyük müşterilerden yıllık finansal tablo isteyin.
- [ ] Limit aşımında ve gecikmede sevkiyat durdurma kuralını sisteme tanımlayın.
- [ ] En büyük 10 müşterinin toplam riskinizdeki payını izleyin.

## Daha fazlası

- Kredi Kayıt Bürosu (2026). *Findeks*. https://www.findeks.com
- Petersen, M. A.; Rajan, R. G. (1997). *Trade Credit: Theories and Evidence*. https://doi.org/10.1093/rfs/10.3.661
- OpenStax (2026). *Principles of Finance*. https://openstax.org/books/principles-finance/pages/1-why-it-matters
