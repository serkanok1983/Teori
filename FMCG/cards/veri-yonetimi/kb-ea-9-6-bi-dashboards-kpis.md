---
id: kb-ea-9-6-bi-dashboards-kpis
title: "İş zekâsı panoları ve KPI tasarımı"
summary: "Analitiğin dört düzeyini (ne oldu, neden oldu, ne olacak, ne yapmalı), iyi bir performans göstergesinin özelliklerini ve satış ekibinin gerçekten kullandığı bir panonun nasıl kurulacağını sayısal ve ağırlıklı dağıtım örneğiyle anlatır."
course: ea
category: veri-yonetimi
tags: [raporlama, kpi, is-zekasi, dagitim]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, it-yoneticisi]
level: temel
source_lessons: [EA-9.6]
reading_minutes: 3
key_points:
  - "Analitik dört düzeydedir: tanımlayıcı, teşhis edici, tahmin edici ve yönlendirici."
  - "İyi bir KPI tek tanımlı, ölçülebilir, sahibi belli ve karar değiştirebilen bir göstergedir."
  - "Pano, kullanıcının sorusuyla başlamalı; mümkün olan her grafiği koymak kullanımı düşürür."
  - "Ortak tanımlar bir anlam katmanında tutulursa her rapor aynı ciroyu gösterir."
  - "Sayısal ve ağırlıklı dağıtım birlikte okunduğunda dağıtımın kalitesi görünür."
glossary_terms: [kpi, is-zekasi]
related: [kb-ea-9-1-reporting-vs-transaction-systems, kb-ea-9-2-sell-in-sell-out-reporting, kb-ea-23-3-balanced-scorecard-okr, kb-ea-8-2-data-quality-field]
sources:
  - title: "Business intelligence and analytics: From big data to big impact"
    authors: "Chen, H.; Chiang, R. H. L.; Storey, V. C."
    year: 2012
    type: article
    doi: "10.2307/41703503"
    url: "https://doi.org/10.2307/41703503"
    verified: true
    checked_on: 2026-10-28
  - title: "The current state of business intelligence"
    authors: "Watson, H. J.; Wixom, B. H."
    year: 2007
    type: article
    doi: "10.1109/MC.2007.331"
    url: "https://doi.org/10.1109/MC.2007.331"
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

Birçok firmada onlarca grafikli bir pano kurulur ve birkaç hafta sonra kimse açmaz. Bu kart, **iş zekâsı** (BI, *business intelligence*) panolarını yöneticinin sorusundan başlayarak kurmayı ve doğru **performans göstergesini** (KPI) seçmeyi anlatır.

## Temel fikir

Analitiğin dört düzeyi vardır:

1. **Tanımlayıcı:** Ne oldu? (Geçen ay ciro.)
2. **Teşhis edici:** Neden oldu? (Hangi bölge, hangi ürün düştü?)
3. **Tahmin edici:** Ne olacak? (Gelecek ay talep.)
4. **Yönlendirici:** Ne yapmalı? (Hangi noktaya hangi ürün önerilmeli?)

Watson ve Wixom (2007) BI'ın değerinin teknolojiden çok kullanımla ortaya çıktığını vurgular; Chen, Chiang ve Storey (2012) ise BI ve analitiğin gelişimini özetler.

İyi bir KPI'ın özellikleri:

- **Tek tanım:** "Ciro" iadeler düşülmüş mü, KDV hariç mi? Yazılı olmalı.
- **Sahip:** Göstergeden sorumlu kişi belli olmalı.
- **Eylem:** Değer kötüleşince ne yapılacağı belli olmalı.
- **Hedef ve eşik:** Yeşil–sarı–kırmızı sınırları önceden konmalı.

Ortak tanımların tek yerde tutulduğu yapıya **anlam katmanı** (*semantic layer*) denir. Böylece her pano aynı ciroyu gösterir.

### Panoyu kullanılır kılmak

Teknik olarak doğru bir pano bile kullanıcılar tarafından açılmıyorsa değer üretmez. Panoların gerçekten kullanılması için şu ilkeler önerilir:

- **Kullanıcıya göre tasarlayın:** Genel müdür, bölge müdürü ve satış temsilcisi farklı sorular sorar. Herkese aynı panoyu sunmak yerine, her rol için az sayıda göstergeyle başlayan ayrı görünümler hazırlanmalıdır.
- **Önce özet, sonra ayrıntı:** Pano, ilk bakışta durumun iyi mi kötü mü olduğunu göstermeli; kullanıcı isterse bölge, müşteri veya ürün ayrıntısına inebilmelidir.
- **Karşılaştırma ekleyin:** Bir rakam tek başına anlam taşımaz. Hedef, önceki dönem veya geçen yıl ile karşılaştırma, rakamın yorumlanmasını sağlar.
- **Görsel sadelik:** Gereksiz renkler, üç boyutlu grafikler ve süslemeler, okunabilirliği azaltır. Renk, yalnızca dikkat çekilmesi gereken sapmaları göstermek için kullanılmalıdır.
- **Güncellik bilgisi:** Verinin hangi tarih ve saate kadar güncel olduğu her panoda görünmelidir.

**Toplantılara bağlayın.** Panolar, yönetim toplantılarının ve haftalık satış toplantılarının temel aracı olduğunda kullanılmaya başlar. Toplantılarda farklı kaynaklardan hazırlanmış tablolar kullanılmaya devam ederse, pano ikinci planda kalır.

**Kullanımı ölçün.** Hangi panoların kimler tarafından ne sıklıkla açıldığı izlenmelidir. Kullanılmayan panolar ya iyileştirilmeli ya da kaldırılmalıdır. Watson ve Wixom'un vurguladığı gibi, iş zekâsının değeri, kararların bilgiyle desteklenmesinde ortaya çıkar.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b2.py` ile yapılmıştır.

Bir bölge müdürünün sorusu: "Yeni ürünümüz pazarda ne kadar yaygın?" Bölgede 2.000 aktif nokta var; ürün 1.300'ünde bulunuyor.

- **Sayısal dağıtım:** 1.300 ÷ 2.000 = **%65,0**.
- **Ağırlıklı dağıtım:** Ürünü bulunduran noktaların kategori cirosu 41 milyon TL, tüm noktalarınki 50 milyon TL → **%82,0**.

İki gösterge birlikte okunduğunda ürünün büyük noktalara girdiği, küçük noktaların ise eksik kaldığı görülüyor. Panoda bu iki gösterge, eksik noktaların temsilci bazlı listesiyle yan yana konuyor; müdür listeyi doğrudan haftalık rota planına aktarabiliyor.

## Sık yapılan hatalar

- Panoyu mevcut veriye göre kurmak; kullanıcının sorusunu sormamak.
- Aynı göstergeyi farklı raporlarda farklı tanımlamak.
- Eylem gerektirmeyen "güzel" göstergelerle ekranı doldurmak.
- Veri kalitesi sorununu panoda gizlemek; eksik veri oranını göstermemek.

## Pratikte nasıl uygulanır?

- [ ] Her rol için cevaplanması gereken en önemli 3–5 soruyu yazın.
- [ ] Her soru için bir KPI, tanımı, sahibi ve eşikleri belirleyin.
- [ ] Tanımları ortak bir sözlükte veya anlam katmanında tutun.
- [ ] Panoda göstergeden ayrıntı listesine inebilmeyi sağlayın.
- [ ] Üç ay sonra kullanım istatistiklerine bakın; açılmayan sayfaları kaldırın.

## Daha fazlası

- Chen, Chiang ve Storey (2012), *MIS Quarterly*. https://doi.org/10.2307/41703503
- Watson ve Wixom (2007), *Computer*. https://doi.org/10.1109/MC.2007.331
