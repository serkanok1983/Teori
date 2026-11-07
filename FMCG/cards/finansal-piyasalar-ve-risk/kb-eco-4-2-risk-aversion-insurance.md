---
id: kb-eco-4-2-risk-aversion-insurance
title: "Risk ve sigorta: Ne zaman sigorta yaptırmalı, ne zaman riski üstlenmeli?"
summary: "Beklenen kayıp ile sigorta primini karşılaştırmayı, büyük ve nadir risklerin neden sigortalanması gerektiğini, küçük ve sık risklerin ne zaman şirket içinde üstlenilebileceğini ve muafiyetin etkisini anlatır."
course: eco
category: finansal-piyasalar-ve-risk
tags: [risk-yonetimi, sigorta, karar-verme]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [ECO-4.2]
reading_minutes: 3
key_points:
  - "Beklenen kayıp, olasılık ile kayıp tutarının çarpımıdır; sigorta primi genellikle bundan yüksektir."
  - "Şirketi batırabilecek büyük ve nadir riskleri sigortalamak, beklenen maliyeti aşsa da mantıklıdır."
  - "Küçük, sık ve öngörülebilir riskleri şirket içinde üstlenmek çoğu zaman daha ucuzdur."
  - "Muafiyet (franchise) primi düşürür; şirketin taşıyabileceği tutarda belirlenmelidir."
glossary_terms: [beklenen-kayip, muafiyet]
related: [kb-eco-52-1-business-insurance, kb-eco-32-3-risk-management-stress-test, kb-eco-24-3-turkey-crises-lessons]
sources:
  - title: "On the Corporate Demand for Insurance"
    authors: "Mayers, D.; Smith, C. W., Jr."
    year: 1982
    type: article
    doi: "10.1086/296165"
    url: "https://doi.org/10.1086/296165"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Business 55(2)."
  - title: "Türkiye Sigorta Birliği (resmî site)"
    authors: "TSB"
    year: 2026
    type: web
    url: "https://www.tsb.org.tr"
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

Depo yangını, araç kazaları, stok bozulması, alacak kaybı... Bir dağıtım şirketi ya da üretici her yıl sigorta poliçelerini yeniler. Bu kart, hangi riskleri sigortalayacağınızı, hangilerini üstleneceğinizi ve muafiyet seviyesini nasıl belirleyeceğinizi mantıklı bir hesapla kararlaştırmanızı sağlar.

## Temel fikir

**Beklenen kayıp** (*expected loss*) = olasılık × kayıp tutarı. Sigorta şirketi, hasar ödemelerine ek olarak giderlerini ve kârını da karşılamak zorunda olduğundan, prim ortalamada beklenen kayıptan yüksektir. Yani sigorta, ortalamada para kaybettiren bir işlemdir.

Peki neden sigorta yaptırılır? Çünkü bazı kayıplar şirketin taşıyabileceğinden büyüktür. Mayers ve Smith (1982), şirketlerin sigorta talebini finansal sıkıntı maliyetleri, vergi ve sözleşme ilişkileri gibi nedenlerle açıklar: Büyük bir kayıp şirketi iflasa ya da pahalı acil finansmana sürükleyebilir.

Bu nedenle pratik kural şudur:

- **Büyük ve nadir riskler** (depo yangını, büyük sorumluluk davası): Sigortalayın; prim beklenen kayıptan yüksek olsa bile.
- **Küçük ve sık riskler** (küçük araç hasarları, ufak fireler): Şirketin nakit akışı kaldırabiliyorsa, kendi üstlenmeyi değerlendirin.
- **Muafiyet:** Kaybın ilk kısmını sizin üstlenmeniz, primi düşürür. Muafiyeti şirketin rahatça taşıyabileceği seviyede tutun.

## Bir örnek

> **Örnek (temsili rakamlar):** Olasılıklar, prim ve hasar tutarları varsayımsaldır; gerçek sigorta fiyatlarını temsil etmez. Hesaplar `scripts/cards_numbers_eco_b2.py` ile yapılmıştır.

**Depo yangını:** Yıllık olasılık %1, kayıp 20.000.000 TL. Beklenen kayıp 200.000 TL, prim 300.000 TL. Prim beklenen kayıptan 100.000 TL yüksek. Ama şirketin özkaynağı 15.000.000 TL; tek bir yangın şirketi batırır. **Sigortalanmalı.**

**Muafiyet seçeneği:** 1.000.000 TL muafiyetle prim 220.000 TL'ye düşüyor; yıllık prim tasarrufu 80.000 TL. Bu seçenekte şirketin üstlendiği ek beklenen kayıp yalnızca 10.000 TL. Muafiyet tutarı şirketin taşıyabileceği bir seviyedeyse mantıklı bir tercihtir.

**Araç filosu küçük hasarları:** 40 araç, her birinde yıllık %15 küçük hasar olasılığı, hasar başına 60.000 TL. Beklenen yıllık hasar 360.000 TL; kasko eki primi 486.000 TL. Fark 126.000 TL. Bu tür küçük ve öngörülebilir hasarlar için riski üstlenmek ucuz olabilir (zorunlu sigortalar hariç).

## Sık yapılan hatalar

- Her riski sigortalamak ya da tasarruf için büyük riskleri sigortasız bırakmak.
- Sigorta değerini eski stok ve bina değerlerine göre bırakmak; yüksek enflasyonda eksik sigortaya düşmek.
- Poliçe istisnalarını ve muafiyetleri okumamak.
- Alacak riskini sigorta, teminat veya limit yönetimiyle ele almamak.
- Hasar sonrası belge ve bildirim sürelerine uymamak.
- Küçük ve sık hasarları sigortalayıp büyük ama seyrek riskleri açık bırakmak.
- Sigorta primini yalnızca maliyet olarak görmek; büyük bir hasarın şirketin devamlılığına etkisini hesaba katmamak.

## Pratikte nasıl uygulanır?

- [ ] Risklerinizi olasılık ve etki büyüklüğüne göre bir tabloda sınıflandırın.
- [ ] Şirketin taşıyabileceği azami tek seferlik kaybı belirleyin; bunun üstündeki riskleri sigortalayın.
- [ ] Muafiyet seçeneklerini prim tasarrufu ile ek beklenen kayıp üzerinden karşılaştırın.
- [ ] Sigorta bedellerini enflasyona göre en az yılda bir güncelleyin.
- [ ] Poliçe koşullarını sigorta danışmanınızla birlikte gözden geçirin.
- [ ] Şirketi ciddi biçimde sarsabilecek en büyük beş riski listeleyin ve her birinin sigortalı olup olmadığını kontrol edin.
- [ ] Muafiyet tutarlarını şirketin kolayca karşılayabileceği seviyeye göre belirleyin.

## Daha fazlası

- Mayers, D.; Smith, C. W., Jr. (1982). *On the Corporate Demand for Insurance*. https://doi.org/10.1086/296165
- TSB (2026). *Türkiye Sigorta Birliği (resmî site)*. https://www.tsb.org.tr
- OpenStax (2026). *Principles of Finance*. https://openstax.org/books/principles-finance/pages/1-why-it-matters
