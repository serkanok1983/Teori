---
id: kb-ea-18-6-data-migration-opening-balances
title: "Veri taşıma ve açılış bakiyeleri"
summary: "Eski sistemden yeni sisteme veri taşırken profil çıkarma, temizleme, eşleme, deneme yüklemeleri ve mutabakat adımlarını; cari, stok ve genel muhasebe açılış bakiyelerinin nasıl doğrulanacağını anlatır."
course: ea
category: yazilim-secimi-ve-proje
tags: [veri-tasima, acilis-bakiyesi, erp, mutabakat]
roles: [finans-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-18.6]
reading_minutes: 3
key_points:
  - "Veri taşıma; profil çıkarma, temizleme, eşleme, deneme yüklemesi ve mutabakat adımlarından oluşur."
  - "Ana veri (müşteri, ürün) ile açık kalemler ve bakiyeler ayrı planlanır."
  - "Her deneme yüklemesinden sonra kayıt sayısı ve tutar mutabakatı yapılır."
  - "Açılış bakiyelerini finans müdürü kayıt bazında onaylamalıdır."
  - "Geçmiş hareketlerin tamamı yerine çoğu zaman yalnızca açık kalemler taşınır."
glossary_terms: [veri-tasima, acilis-bakiyesi, mutabakat]
related: [kb-ea-41-5-cutover-plan, kb-ea-8-2-data-quality-field, kb-ea-8-3-mdm-matching-duplicates, kb-ea-18-5-implementation-methodology]
sources:
  - title: "Beyond Accuracy: What Data Quality Means to Data Consumers"
    authors: "Wang, R.; Strong, D."
    year: 1996
    type: article
    doi: "10.1080/07421222.1996.11518099"
    url: "https://doi.org/10.1080/07421222.1996.11518099"
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

Yeni sistem ne kadar iyi olursa olsun, ilk gün müşteri bakiyeleri yanlışsa tahsilat ekibi işe başlayamaz ve kullanıcıların sisteme güveni sarsılır. Bu kart, veri taşımayı bir proje içi proje gibi yönetmenizi sağlar.

## Temel fikir

Veri taşıma beş adımda ilerler:

1. **Profil çıkarma:** Eski veride kaç kayıt var, hangi alanlar boş, hangi kayıtlar kopya?
2. **Temizleme:** Pasif müşterileri ayırmak, kopyaları birleştirmek, eksik vergi numaralarını tamamlamak. Wang ve Strong'un (1996) veri kalitesi boyutları (doğruluk, tamlık, tutarlılık, güncellik) burada kontrol listesi olarak kullanılabilir.
3. **Eşleme:** Eski alanın yeni sistemde hangi alana, hangi koda karşılık geldiği; ör. eski "bölge" kodlarının yeni satış organizasyonuna dönüşümü.
4. **Deneme yüklemeleri:** Test ortamına en az iki–üç kez yükleme. Her seferinde hatalar düzeltilir, süre ölçülür.
5. **Mutabakat:** Eski ve yeni sistemde kayıt sayısı ve tutar karşılaştırması; farkların tek tek açıklanması.

Taşınacak veri üç gruptur: **ana veri** (müşteri, tedarikçi, ürün, fiyat), **açık kalemler** (açık siparişler, ödenmemiş faturalar, açık çekler) ve **açılış bakiyeleri** (cari, stok miktar ve değeri, genel muhasebe hesapları). Geçmiş yılların tüm hareketlerini taşımak çoğu zaman gerekmez; eski sistem okuma amaçlı saklanır.

### Taşıma provaları ve onay

Veri taşıma, tek seferlik bir işlem olarak değil, birkaç prova ile olgunlaşan bir süreç olarak planlanmalıdır. Her provada kayıt sayıları, toplam bakiyeler ve örneklem kontrolleri ile kaynak ve hedef karşılaştırılır; hatalar sınıflandırılarak bir sonraki provadan önce düzeltilir. Wang ve Strong'un tanımladığı veri kalitesi boyutları, bu kontrollerin çerçevesini oluşturabilir: doğruluk, eksiksizlik ve tutarlılık gibi. Açılış bakiyeleri, finans ekibi tarafından eski sistemin kapanış raporlarıyla karşılaştırılarak yazılı olarak onaylanmalıdır. Hangi geçmiş verinin taşınmayacağı ve eski sistemin ne kadar süre okunabilir tutulacağı da önceden kararlaştırılmalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b4.py` ile yapılmıştır. Sorgu SQLite'ta çalıştırılmıştır.

Bir bayi, deneme yüklemesinden sonra cari bakiyeleri karşılaştırıyor. Bakiyeler kuruş cinsinden iki tabloda; aşağıdaki sorgu farklı olanları listeliyor:

```sql
SELECT coalesce(e.cari, y.cari) AS cari, e.bakiye_kurus AS eski, y.bakiye_kurus AS yeni,
       coalesce(y.bakiye_kurus,0) - coalesce(e.bakiye_kurus,0) AS fark
FROM eski e LEFT JOIN yeni y ON e.cari = y.cari
UNION ALL
SELECT y.cari, NULL, y.bakiye_kurus, y.bakiye_kurus FROM yeni y
WHERE y.cari NOT IN (SELECT cari FROM eski);
```

Sonuçta farkı sıfır olmayan üç kayıt çıkıyor:

| Cari | Eski | Yeni | Fark |
|---|---|---|---|
| C003 | 2.300,00 | 2.030,00 | -270,00 |
| C004 | 990,00 | yok | -990,00 |
| C006 | yok | 150,00 | 150,00 |

Toplam fark **−1.110,00 TL**. C003'te basamak kayması, C004'te yüklenmeyen bir kayıt, C006'da test kaydının silinmemesi bulunuyor. Düzeltmeden sonra ikinci deneme yüklemesinde fark sıfırlanıyor ve finans müdürü listeyi onaylıyor.

## Sık yapılan hatalar

- Yalnızca toplam tutarı karşılaştırıp kayıt bazında mutabakat yapmamak; artı ve eksiler birbirini götürebilir.
- Temizliği yeni sistemde yapmayı planlamak.
- Tek bir deneme yüklemesiyle canlıya gitmek.
- Açılış stokunu sayım yapmadan eski sistemden almak.

## Pratikte nasıl uygulanır?

- [ ] Her veri nesnesi için bir sahip ve bir eşleme dokümanı belirleyin.
- [ ] En az iki deneme yüklemesi ve her birinde kayıt bazında mutabakat yapın.
- [ ] Açılış stoku için geçişten hemen önce sayım planlayın.
- [ ] Açılış bakiyelerini finans müdürüne imzalı olarak onaylatın.

## Daha fazlası

- Wang ve Strong (1996), *Journal of Management Information Systems*. https://doi.org/10.1080/07421222.1996.11518099
