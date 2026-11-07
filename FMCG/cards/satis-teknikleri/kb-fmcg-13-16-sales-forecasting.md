---
id: kb-fmcg-13-16-sales-forecasting
title: "Satış tahmini: Baz iş ve fırsatlar"
summary: "Satış tahmini; mevcut müşterilerden gelen baz iş ile henüz kazanılmamış fırsatların olasılıklarla ağırlıklandırılmış değerini birleştirir. Bu kart ağırlıklı fırsat tahminini, satış tahmini yönetimini ve tahminin doğruluğunu iyileştirme yollarını anlatır."
course: fmcg
category: satis-teknikleri
tags: [satis-yonetimi, tahmin, planlama]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: orta
source_lessons: [FMCG-13.16]
reading_minutes: 3
key_points:
  - "Satış tahmini; baz iş ve fırsat tahmini olmak üzere iki bölümden oluşur."
  - "Fırsatlar, kazanılma olasılıklarıyla ağırlıklandırılmalıdır."
  - "Ağırlıksız toplam, tahmini sistematik olarak şişirir."
  - "Mentzer ve Moon, satış tahminini bir yönetim süreci olarak ele alır: yöntem, süreç, sistem ve performans ölçümü."
  - "Tahmin doğruluğu düzenli ölçülmeli ve olasılıklar geçmiş kazanma oranlarıyla kalibre edilmelidir."
glossary_terms: [baz-satis, tahmin-hatasi, satis-hunisi, satis-ve-operasyon-planlamasi]
related: [kb-fmcg-13-8-sales-funnel-math, kb-fmcg-13-2-strategic-selling, kb-fmcg-13-3-challenger-meddic-sandler, kb-fmcg-11-2-demand-forecasting]
sources:
  - title: "Sales Forecasting Management: A Demand Management Approach"
    authors: "Mentzer, J. T.; Moon, M. A."
    year: 2005
    type: book
    doi: "10.4135/9781452204444"
    verified: true
    checked_on: 2026-10-28
    note: "DOI Crossref kaydında başlık ve yazar eşleşti; baskı yılı karttakinden farklı olabilir."
  - title: "ZS"
    authors: "ZS Associates"
    year: 2026
    type: web
    url: "https://www.zs.com/"
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

Satış müdürü, bölge ekibinden çeyreklik tahmin ister. Temsilciler bütün fırsatları toplar ve tahmin hedefin çok üzerinde çıkar. Çeyrek sonunda gerçekleşme hedefin altında kalır; üretim ve stok planlaması da yanlış tahmine göre yapılmıştır. Bu kart, baz işi ve fırsatları ayırarak gerçekçi bir satış tahmini yapmanızı sağlar.

## Temel fikir

**İki bölüm.**

- **Baz iş:** Mevcut müşterilerden, mevcut ürünlerle beklenen satış. Geçmiş satışlar, sezonsallık ve bilinen değişikliklerle tahmin edilir.
- **Fırsatlar:** Yeni listeleme, yeni müşteri, ek kampanya gibi henüz kesinleşmemiş işler. Her biri kazanılma olasılığıyla ağırlıklandırılır.

**Ağırlıklı tahmin.** Ağırlıklı fırsat değeri = Fırsat büyüklüğü × Kazanılma olasılığı. Bütün fırsatların ağırlıklı toplamı, baz işe eklenir. Ağırlıksız toplam, bütün fırsatların kazanılacağını varsayar ve tahmini şişirir.

**Olasılıkların belirlenmesi.** Olasılıklar, fırsatın aşamasına bağlı standart oranlarla ya da nitelendirme ölçütlerine göre belirlenir. Örneğin yalnızca ilk görüşmesi yapılmış bir fırsat düşük, karar toplantısına gelmiş bir fırsat yüksek olasılık alır. Bu oranlar, geçmiş fırsatların gerçek kazanma oranlarıyla düzenli olarak karşılaştırılmalıdır.

**Bir yönetim süreci olarak tahmin.** Mentzer ve Moon'un *Sales Forecasting Management* kitabı, satış tahminini yalnızca bir hesaplama tekniği olarak değil, bir yönetim süreci olarak ele alır. Kitap; tahmin yöntemlerini, tahminin şirket içinde nasıl hazırlanıp paylaşıldığını, kullanılan sistemleri ve tahmin performansının ölçülmesini birlikte değerlendirmeyi önerir. Satış tahmini, talep planlaması ve satış ve operasyon planlaması süreçlerine girdi olur.

**Önyargılar.** Satış ekipleri, hedef baskısı ya da prim sistemleri nedeniyle tahmini yukarı ya da aşağı çekebilir. Tahmini hedeften ayrı tutmak ve doğruluğunu ölçmek, bu önyargıları azaltır.

**Tahmin toplantısı.** Birçok şirkette satış tahmini, satış, pazarlama, finans ve tedarik zinciri ekiplerinin katıldığı düzenli bir toplantıda kesinleştirilir. Toplantıda önce bir önceki dönemin tahmin hatası gözden geçirilir; sonra baz işteki değişiklikler (kaybedilen ya da kazanılan müşteriler, fiyat değişiklikleri) ve büyük fırsatların durumu konuşulur. Her büyük fırsat için sorumlu kişi, beklenen karar tarihi ve olasılığın gerekçesi kayıt altına alınmalıdır. Tahminin tek bir rakam yerine iyimser, beklenen ve kötümser senaryolarla verilmesi, üretim ve stok kararlarında riskin görünür olmasını sağlar.

## Bir örnek

> **Örnek (temsili rakamlar):** Baz iş, fırsat büyüklükleri ve olasılıklar varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b8.py` ile yapılmıştır.

Bir bölgenin çeyreklik baz işi **4.000.000 TL**. Açık fırsatlar:

| Fırsat | Büyüklük (TL) | Olasılık | Ağırlıklı (TL) |
|---|---:|---:|---:|
| Yerel zincirde yeni seri | 1.000.000 | %60 | 600.000 |
| Toptancı kampanyası | 500.000 | %30 | 150.000 |
| Yeni ulusal zincir | 2.000.000 | %10 | 200.000 |
| **Toplam** | **3.500.000** | | **950.000** |

Ağırlıklı tahmin: 4.000.000 + 950.000 = **4.950.000 TL**. Ağırlıksız toplam (**3.500.000 TL** fırsat) eklenseydi tahmin 7.500.000 TL olurdu ve büyük olasılıkla gerçekleşmezdi. Müdür, çeyrek sonunda her olasılık grubunun gerçek kazanma oranını kontrol edecek.

## Sık yapılan hatalar

- **Fırsatları ağırlıklandırmamak.** Tahmin sistematik olarak şişer.
- **Tahmini hedefe eşitlemek.** Tahmin, beklenen sonucu göstermelidir.
- **Büyük fırsata yüksek olasılık vermek.** Büyük fırsatlar genellikle daha belirsizdir.
- **Doğruluğu ölçmemek.** Hatalar tekrarlanır.
- **Baz işi sabit varsaymak.** Müşteri kayıpları ve sezonsallık hesaba katılmalıdır.

## Pratikte nasıl uygulanır?

- [ ] Baz işi ve fırsatları ayrı tahmin edin.
- [ ] Fırsat aşamalarına standart olasılıklar atayın.
- [ ] Ağırlıklı tahmini talep planlama ekibiyle paylaşın.
- [ ] Tahmin hatasını her dönem ölçün.
- [ ] Olasılıkları geçmiş kazanma oranlarına göre güncelleyin.

## Daha fazlası

- Mentzer, J. T.; Moon, M. A. (2005). *Sales Forecasting Management: A Demand Management Approach.*
- ZS Associates (2026). *ZS.* https://www.zs.com/
