---
id: kb-ea-9-2-sell-in-sell-out-reporting
title: "Sell-in ve sell-out raporlaması: Boyutsal model ve yıldız şema"
summary: "Üreticiden dağıtıcıya satış (sell-in) ile dağıtıcıdan noktaya satışı (sell-out) aynı modelde birleştirmeyi; olgu ve boyut tabloları, tanecik seçimi ve yavaş değişen boyutlarla kurulan yıldız şemayı küçük bir SQL örneğiyle anlatır."
course: ea
category: veri-yonetimi
tags: [raporlama, veri-ambari, sell-in, sell-out, sql, dagitici]
roles: [it-yoneticisi]
level: ileri
source_lessons: [EA-9.2]
reading_minutes: 3
key_points:
  - "Boyutsal model, ölçülen olayları olgu tablolarında, bağlamı boyut tablolarında tutar."
  - "Tanecik, olgu tablosundaki bir satırın neyi temsil ettiğidir ve modelin ilk kararıdır."
  - "Sell-in ve sell-out ayrı olgu tablolarıdır; ortak ürün, tarih ve dağıtıcı boyutlarıyla birleştirilir."
  - "Sell-in ile sell-out farkı dağıtıcı stokundaki değişimi gösterir."
  - "Müşterinin bölgesi veya kanalı değişince geçmişin nasıl raporlanacağı yavaş değişen boyut kuralıyla belirlenir."
glossary_terms: [sell-in, sell-out, veri-ambari]
related: [kb-ea-9-1-reporting-vs-transaction-systems, kb-ea-26-6-dms-secondary-sales, kb-ea-9-6-bi-dashboards-kpis, kb-ea-29-3-drp-inventory-planning]
sources:
  - title: "The Data Warehouse Toolkit"
    authors: "Kimball, R.; Ross, M."
    year: 2013
    type: book
    verified: false
    note: "3. baskı."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Üretici kendi faturalarından dağıtıcıya ne sattığını (sell-in) bilir. Dağıtıcının noktalara ne sattığını (sell-out) ise ancak dağıtıcı sisteminden gelen veriyle görür. İkisini birlikte görmeden "satışlar arttı mı, yoksa dağıtıcı depoları mı doldu?" sorusu cevaplanamaz. Bu kart, iki veriyi tek bir raporlama modelinde birleştirmenin yolunu anlatır.

## Temel fikir

Kimball ve Ross'un **boyutsal modelleme** yaklaşımında iki tür tablo vardır:

- **Olgu tablosu** (*fact*): Ölçülen olaylar. Örneğin bir fatura satırının miktarı ve tutarı.
- **Boyut tablosu** (*dimension*): Olayın bağlamı. Ürün, tarih, dağıtıcı, nokta, temsilci.

Ortada olgu, çevresinde boyutlar olduğu için bu yapıya **yıldız şema** denir.

Modelin ilk kararı **tanecik**tir (*grain*): Bir olgu satırı neyi temsil eder? Sell-in için "fatura satırı", sell-out için dağıtıcının verisi elveriyorsa "nokta–ürün–gün", vermiyorsa "dağıtıcı–ürün–hafta" olabilir. İki olgu tablosunun taneciği farklı olabilir; ortak boyutlar (ürün, tarih, dağıtıcı) üzerinden ortak düzeyde karşılaştırılır.

**Yavaş değişen boyut** (*slowly changing dimension*): Bir nokta başka bölgeye geçtiğinde geçmiş satışları eski bölgede mi, yeni bölgede mi göreceksiniz? Tip 1 eskinin üzerine yazar; tip 2 yeni bir satır açıp geçerlilik tarihleri tutar ve geçmişi korur.

### Raporların doğru okunması

Sell-in ve sell-out verileri farklı zamanlamalara sahiptir: üreticinin distribütöre satışı, tüketiciye satıştan haftalar önce gerçekleşebilir. Bu nedenle iki seri aynı dönemde karşılaştırılırken distribütör stokundaki değişim de birlikte gösterilmelidir. Sell-in'in sürekli sell-out'un üzerinde seyretmesi, kanalda stok biriktiğinin işaretidir ve ileride sipariş düşüşüne yol açabilir. Kimball ve Ross'un boyutsal modelinde iki ayrı olgu tablosunun ortak ürün, müşteri ve tarih boyutlarıyla bağlanması, bu karşılaştırmayı mümkün kılar.

## Bir örnek

> **Örnek (temsili rakamlar):** Veriler uydurmadır; sorgu `scripts/cards_numbers_ea_b2.py` içinde SQLite ile çalıştırılmış ve çıktı aynen aktarılmıştır.

Bir süt ürünleri üreticisinin eylül ayı verisi: `sell_in(tarih, urun_id, koli)`, `sell_out(tarih, urun_id, koli)` ve `urun(urun_id, urun_adi)` tabloları. Ürün bazında karşılaştırma:

```sql
select u.urun_adi, i.koli sell_in, o.koli sell_out, i.koli-o.koli stok_degisimi,
 round(100.0*o.koli/i.koli,1) devir_yuzde
from urun u join (select urun_id,sum(koli) koli from sell_in group by urun_id) i using(urun_id)
join (select urun_id,sum(koli) koli from sell_out group by urun_id) o using(urun_id) order by u.urun_id;
```

| Ürün | Sell-in | Sell-out | Stok değişimi | Sell-out / sell-in |
|---|---|---|---|---|
| Ayran 200 ml | 700 | 630 | 70 | %90,0 |
| Yoğurt 1 kg | 250 | 200 | 50 | %80,0 |
| Peynir 500 g | 120 | 115 | 5 | %95,8 |

Yoğurtta dağıtıcıya gönderilen her 100 kolinin yalnızca 80'i noktaya çıkmış. Kısa raf ömürlü bir üründe 50 kolilik stok artışı, ay sonu yükleme baskısının ya da sahadaki satış sorununun işareti olabilir; ekim ayı yükleme planı buna göre düşürülüyor.

## Sık yapılan hatalar

- Taneciği belirlemeden tablo tasarlamaya başlamak.
- Üretici ve dağıtıcı sistemlerinde farklı ürün kodlarını eşlemeden birleştirmek.
- Bölge değişikliklerinde geçmişi yeniden yazıp eski raporları değiştirmek.
- Sell-out verisinin hangi dağıtıcılardan eksik geldiğini raporda göstermemek.

## Pratikte nasıl uygulanır?

- [ ] Sell-in ve sell-out için tanecik kararını yazılı alın.
- [ ] Ürün, tarih ve dağıtıcı boyutlarını iki tarafta ortak hale getirin; kod eşleme tablosu tutun.
- [ ] Bölge ve kanal gibi değişen alanlar için tip 2 kuralını kullanın.
- [ ] Ürün bazında sell-out / sell-in oranını ve dağıtıcı stok gününü aylık izleyin.

## Daha fazlası

- Kimball ve Ross, *The Data Warehouse Toolkit*, 3. baskı (kitap; doğrulanmadı).
