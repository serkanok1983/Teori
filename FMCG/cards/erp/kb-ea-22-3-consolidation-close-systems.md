---
id: kb-ea-22-3-consolidation-close-systems
title: "Konsolidasyon ve kapanış sistemleri: Grup şirketleri tek tabloda"
summary: "Birden fazla şirketi olan grupların finansal tablolarını birleştirirken yapılan şirketler arası eliminasyonu, sahiplik oranlarının etkisini, kapanış yönetimi araçlarını ve dipnot hazırlığını sistem açısından anlatır."
course: ea
category: erp
tags: [konsolidasyon, eliminasyon, grup-sirketleri, kapanis]
roles: [finans-muduru, it-yoneticisi]
level: ileri
source_lessons: [EA-22.3]
reading_minutes: 3
key_points:
  - "Konsolidasyon, grup şirketlerinin tablolarını tek bir ekonomik birim gibi birleştirir."
  - "Şirketler arası satış, alacak–borç ve kâr eliminasyonla çıkarılır."
  - "Eliminasyon için şirketler arası işlemlerin ERP'de ayrı işaretlenmesi şarttır."
  - "Sahiplik oranı, kontrol gücü olmayan payların ayrı gösterilmesini gerektirir."
  - "Kapanış yönetimi araçları görevleri, onayları ve mutabakatları tek yerde izler."
glossary_terms: [konsolidasyon, sirketler-arasi-eliminasyon]
related: [kb-ea-20-4-record-to-report-close, kb-ea-22-2-multi-currency-inflation-adjust-in-erp, kb-ea-22-1-chart-of-accounts-tekduzen]
sources:
  - title: "Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu (TMS/TFRS)"
    authors: "KGK"
    year: 2026
    type: web
    url: "https://www.kgk.gov.tr/"
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

Bir üretici, ayrı bir dağıtım şirketi ve belki bir ihracat şirketi kurmuş olabilir. Yönetim, grubun gerçek cirosunu ve kârını görmek ister. Bu kart, **konsolidasyonun** sistem tarafını ve kapanışı hızlandıran araçları anlatır.

## Temel fikir

Konsolidasyonda grup şirketleri tek bir ekonomik birim gibi raporlanır. Bunun için şu adımlar izlenir:

1. **Veri toplama:** Her şirketin mizanı, ortak bir grup hesap planına eşlenir.
2. **Para birimi çevrimi:** Yurt dışı şirketlerin tabloları grup para birimine çevrilir.
3. **Şirketler arası eliminasyon:**
   - Grup içi satış ve alışlar,
   - Grup içi alacak ve borçlar,
   - Henüz gruptan dışarı satılmamış stoklardaki **gerçekleşmemiş kâr** çıkarılır.
4. **Sahiplik:** Yüzde yüz sahip olunmayan şirketlerde kontrol gücü olmayan paylar ayrı gösterilir.
5. **Raporlama ve dipnotlar:** Konsolide tablolar ve açıklamalar hazırlanır.

Sistem tarafında en kritik nokta, şirketler arası işlemlerin kaynağında **işaretlenmesidir**. ERP'de karşı şirket alanı (ör. "ilişkili şirket kodu") her faturada dolu olursa eliminasyon otomatik yapılabilir. Aksi halde her ay Excel'de eşleştirme yapılır.

Grup büyüdükçe **kapanış yönetimi** araçları devreye girer: Görev listeleri, onay akışları, mutabakat takibi ve dipnot taslakları tek yerde izlenir. Bu araçlar ERP'nin içinde ya da ayrı bir konsolidasyon yazılımı olarak bulunabilir.

### Konsolidasyon sürecini kolaylaştırmak

Konsolidasyonun zorluğu, büyük ölçüde grup şirketlerinin muhasebe uygulamalarındaki farklılıklardan kaynaklanır. Süreci kolaylaştırmak için şu adımlar önerilir:

- **Grup hesap planı:** Tüm şirketlerin yerel hesap planlarının, ortak bir grup raporlama hesap planına eşleştirilmesi gerekir. Bu eşleştirme her yeni hesap açıldığında güncellenmelidir.
- **Grup muhasebe politikaları:** Stok değerleme, amortisman, karşılıklar ve gelir tanıma gibi konularda grup politikaları yazılı olmalıdır. Yerel uygulamalar farklıysa, konsolidasyon için yapılacak düzeltmeler tanımlanmalıdır.
- **Şirketler arası işlemler:** Grup şirketleri arasındaki satış, alış, borç ve alacaklar ayrı hesaplarda ve karşı şirket bilgisiyle kaydedilmelidir. Kapanıştan önce iki tarafın tutarlarının mutabık olduğu kontrol edilmelidir.
- **Kur çevrimi:** Farklı para birimlerinde tutulan şirketlerin tabloları, belirlenmiş kurlar ve yöntemlerle çevrilmelidir. Kur farklarının nerede raporlanacağı açıkça tanımlanmalıdır.
- **Takvim:** Tüm şirketlerin aynı kapanış takvimine uyması, konsolidasyonun gecikmesini önler.

**Sistem seçimi.** Az sayıda şirketten oluşan gruplarda konsolidasyon tablo programlarıyla yapılabilir; ancak şirket sayısı arttıkça, eşleştirme, eleme ve kur çevrimini otomatikleştiren bir konsolidasyon aracı daha güvenli hâle gelir. Seçilen yöntem ne olursa olsun, düzeltme kayıtlarının gerekçeleriyle birlikte izlenebilir olması gerekir. Uygulanacak raporlama standartları için KGK yayınlarına ve mali müşavirinize başvurun.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b5.py` ile yapılmıştır.

Üretim şirketi, grubun dağıtım şirketine maliyeti 400.000 TL olan ürünleri **500.000,00 TL**'ye satıyor. Dönem sonunda dağıtım şirketi bu ürünlerin yarısını henüz satmamış.

- Grup cirosundan **500.000,00 TL**'lik iç satış çıkarılır.
- Dağıtım şirketinin stoğundaki **50.000,00 TL**'lik gerçekleşmemiş kâr elimine edilir.

İki şirketin faturalarında karşı şirket kodu dolu olduğu için eşleştirme otomatik yapılıyor. Kodun boş bırakıldığı birkaç fatura ise ayrıca bulunup düzeltiliyor.

## Sık yapılan hatalar

- Şirketler arası faturaları normal müşteri faturası gibi kesmek.
- İki şirketin karşılıklı bakiyelerini ay sonundan önce mutabık etmemek.
- Grup hesap planı eşlemesini yıllarca güncellememek.
- Stoktaki gerçekleşmemiş kârı unutmak.

## Pratikte nasıl uygulanır?

- [ ] Her grup şirketini ERP'de ilişkili şirket olarak tanımlayın.
- [ ] Şirketler arası alacak–borç mutabakatını kapanış takvimine ekleyin.
- [ ] Grup hesap planı eşlemesini yazılı tutun.
- [ ] Grup büyüdükçe kapanış yönetimi aracı ihtiyacını değerlendirin.

## Daha fazlası

- TMS/TFRS metinleri için Kamu Gözetimi Kurumu: https://www.kgk.gov.tr/
