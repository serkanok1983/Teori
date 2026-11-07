---
id: kb-ea-41-1-case-distributor-app-landscape
title: "Vaka: Bir hızlı tüketim dağıtıcısının uygulama haritası"
summary: "Kurgusal bir hızlı tüketim dağıtıcısının yeteneklerinden sistemlerine ve entegrasyonlarına uzanan uygulama haritasını adım adım çıkararak, ders boyunca anlatılan kavramları tek bir vakada birleştirir."
course: ea
category: is-sistemleri-temelleri
tags: [vaka, uygulama-haritasi, yetenek-haritasi, dagitici, mimari]
roles: [bayi-sahibi, bayi-yonetici, it-yoneticisi]
level: ileri
source_lessons: [EA-41.1]
reading_minutes: 2
key_points:
  - "Uygulama haritası, iş yeteneklerinden başlar ve sistemlere iner."
  - "Her yetenek için ana sistem ve veri sahibi belirlenir."
  - "Sistemler arası arayüzler bir listede, yön ve sıklığıyla gösterilir."
  - "Harita boşlukları, çakışmaları ve elle yapılan aktarımları görünür kılar."
  - "Vaka kurgusaldır; kendi şirketinize uyarlanmalıdır."
glossary_terms: [uygulama-haritasi]
related: [kb-ea-5-4-application-portfolio, kb-ea-5-5-erp-core-vs-best-of-breed, kb-ea-20-2-order-to-cash, kb-ea-26-1-retail-execution-sfa, kb-ea-41-5-cutover-plan]
sources:
  - title: "ArchiMate 3.2 Specification"
    authors: "The Open Group"
    year: 2022
    type: web
    url: "https://pubs.opengroup.org/architecture/archimate32-doc/"
    verified: true
    checked_on: 2026-10-28
    note: "URL HTTP 200 ile açıldı, başlık/kurum eşleşti (2026-10-28)."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28

---

## Ne işe yarar?

Ders boyunca ERP, satış uygulaması, depo, taşıma, e-belge ve analitik ayrı ayrı ele alındı. Bu vaka kartı, hepsinin bir dağıtıcıda nasıl bir araya geldiğini gösterir ve kendi haritanızı çıkarmanız için şablon sunar.

## Temel fikir

**Adım 1 – Yetenekler:** Satış ve sipariş, fiyat ve iskonto, depo, sevkiyat, faturalama ve e-belge, tahsilat ve risk, satın alma, finans, İK ve bordro, raporlama.

**Adım 2 – Sistemler:** Her yeteneğe ana sistem atanır:

| Yetenek | Ana sistem |
|---|---|
| Sipariş, stok, finans, satın alma | ERP |
| Saha satış ve ziyaret | Satış uygulaması (SFA) |
| Depo içi görevler | WMS |
| Sevkiyat ve araç | TMS |
| E-fatura, e-irsaliye | Özel entegratör |
| İK ve bordro | İK/bordro sistemi |
| Raporlama | Veri ambarı ve BI |
| Banka hareketleri | Banka entegrasyonu |
| Belge arşivi | Arşiv sistemi |

**Adım 3 – Arayüzler:** Her bağlantı için kaynak, hedef, veri, yön ve sıklık yazılır (örneğin ERP → SFA, fiyat listesi, günlük).

**Adım 4 – Görünüm:** Harita, ArchiMate gibi bir gösterimle veya basit kutu-ok diyagramıyla çizilir.

**Adım 5 – Bulgular:** Elle yapılan aktarımlar, aynı verinin iki ana kaynağı ve sahipsiz sistemler işaretlenir.

### Haritayı okumak: Hangi soruları sorarsınız?

Harita çizildikten sonra asıl değer, onun üzerinden sorulan sorulardan gelir. Her yetenek ve arayüz için aşağıdaki sorular sırayla sorulabilir:

- **Ana kaynak kim?** Müşteri, ürün ve fiyat gibi her ana veri türünün tek bir ana kaynağı olmalıdır. İki sistemde ayrı ayrı açılan kayıtlar, ileride mükerrer müşteri ve tutarsız fiyat sorununa dönüşür.
- **Arayüz nasıl çalışıyor?** Anlık API, gece çalışan toplu aktarım, dosya bırakma veya elle kopyalama. Elle yapılan her aktarım, hem iş gücü hem hata riski demektir.
- **Arayüz bozulursa ne olur?** Sipariş akışını durduran arayüzler kritik sayılmalı; izleme ve uyarı öncelikle bunlar için kurulmalıdır.
- **Sistemin sahibi kim?** Her sistemin bir iş sahibi (süreçten sorumlu yönetici) ve bir teknik sahibi olmalıdır. Sahipsiz sistemler güncellenmez ve güvenlik açığı biriktirir.
- **Sözleşme ve lisans ne zaman bitiyor?** Yenileme tarihleri, değişiklik için doğal fırsat pencereleridir.

Bu sorulara verilen cevaplar, haritayı statik bir çizimden yönetilebilir bir yol haritasına dönüştürür. Haritayı yılda en az bir kez ve her büyük sistem değişikliğinden sonra güncellemek, bir sonraki yatırım kararında aynı analizi sıfırdan yapma ihtiyacını ortadan kaldırır.

### Haritanın kullanımı

Uygulama haritası, yeni bir sistem seçiminde, entegrasyon değişikliğinde ve bütçe planlamasında başvurulan ortak bir belge olmalıdır. Haritanın güncel tutulmasından sorumlu bir kişi belirlenmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b8.py` ile yapılmıştır.

Kurgusal dağıtıcının haritasında 9 sistem ve 14 arayüz çıkıyor. Arayüzlerden biri, banka hareketlerinin Excel ile elle aktarılması; bir diğeri, müşteri ana verisinin hem ERP'de hem SFA'da ayrı ayrı açılması. Bu iki bulgu, yol haritasının ilk iki maddesi oluyor.

## Sık yapılan hatalar

- Haritayı sistemlerden başlatıp iş yeteneklerini atlamak.
- Elle yapılan aktarımları "arayüz" saymamak.
- Haritayı bir kez çizip güncellememek.
- Veri sahipliğini belirtmemek.
- Haritayı yalnızca BT ekibiyle çizip iş birimlerine doğrulatmamak.

## Pratikte nasıl uygulanır?

- [ ] Şirketinizin yetenek listesini çıkarın.
- [ ] Her yeteneğe ana sistem ve veri sahibi atayın.
- [ ] Arayüz listesini kaynak, hedef, veri, yön ve sıklıkla doldurun.
- [ ] Elle aktarımları ve çift kaynakları işaretleyin.
- [ ] Bulguları önceliklendirip yol haritasına taşıyın.

## Daha fazlası

- The Open Group, ArchiMate 3.2 Spesifikasyonu (doğrulanmadı).
- Bu vaka kurgusaldır ve ders kapsamındaki kartların sentezidir.
