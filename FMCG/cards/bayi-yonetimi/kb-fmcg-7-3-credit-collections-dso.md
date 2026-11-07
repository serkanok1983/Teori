---
id: kb-fmcg-7-3-credit-collections-dso
title: "Kredi, tahsilat ve alacak tahsil süresi"
summary: "Satış yapmak kadar parayı zamanında tahsil etmek de önemlidir. Bu kart alacak tahsil süresini hesaplamayı, alacakları yaşlandırmayı, şüpheli alacak karşılığını ve vadeyi kısaltmanın nakit etkisini anlatır."
course: fmcg
category: bayi-yonetimi
tags: [finans, dagitim, saha-satis]
roles: [bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, saha-satis-temsilcisi, finans-muduru]
level: temel
source_lessons: [FMCG-7.3]
reading_minutes: 3
key_points:
  - "Alacak tahsil süresi, alacakların ortalama kaç günlük satışa denk geldiğini gösterir."
  - "Alacakları vadesinden bu yana geçen süreye göre gruplamak, tahsilat riskini gösterir."
  - "Vadeyi birkaç gün kısaltmak önemli miktarda nakit serbest bırakabilir."
  - "Kredi limiti, ödeme geçmişi ve teminat kuralları satış ekibiyle birlikte uygulanmalıdır."
glossary_terms: [alacak-tahsil-suresi, vade, isletme-sermayesi]
related: [kb-fmcg-7-2-distributor-roi, kb-fmcg-7-1-distributor-pnl, kb-fmcg-5-6-pricing-in-high-inflation, kb-fmcg-1-5-turkish-fmcg-landscape, kb-fmcg-12-7-case-distributor-turnaround]
sources:
  - title: "Principles of Corporate Finance"
    authors: "Brealey, R. A.; Myers, S. C.; Allen, F."
    year: 2020
    type: book
    verified: false
    note: "Kitap; baskı yılı kontrol edilmedi."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Tahsil edilmeyen satış, satış değildir. Yüksek faiz ve enflasyon ortamında alacakta bekleyen her gün, değer kaybı ve finansman maliyeti demektir. Bu kart, alacakları ölçmenizi ve yönetmenizi sağlayan temel araçları anlatır.

## Temel fikir

**Alacak tahsil süresi** (*days sales outstanding*, DSO) = alacak bakiyesi / dönem satışı × dönemdeki gün sayısı. Örneğin yıllık satış ve yıl sonu alacakla hesaplanır. Aylık izlemede son üç ayın satışını kullanmak, mevsimselliğin etkisini azaltır.

**Yaşlandırma** (*aging*). Alacakları vadesinden bu yana geçen süreye göre gruplarsınız: vadesi gelmemiş, 0–30 gün gecikmiş, 31–60 gün, 61–90 gün, 90 günden fazla. Gecikme uzadıkça tahsil olasılığı düşer.

**Karşılık.** Tahsil edilemeyebilecek alacaklar için finansal tablolarda karşılık ayrılır. Muhasebe ve vergi açısından karşılığın nasıl ayrılacağı mevzuata bağlıdır; bunu mali müşavirinizle belirleyin. Yönetim raporlamasında ise her yaş grubuna bir tahsil edilememe oranı uygulayarak riski kabaca ölçebilirsiniz.

**Vadenin nakit etkisi.** Brealey, Myers ve Allen, işletme sermayesi yönetiminin firmanın nakit ihtiyacını doğrudan belirlediğini anlatır. Alacak tahsil süresindeki her gün, bir günlük satış kadar nakdi bağlar.

**Kredi politikası.** Müşteriye kredi limiti, ödeme geçmişine, işletmenin büyüklüğüne ve varsa teminata göre verilir. Limit aşımında sevkiyatın durdurulması gibi kurallar yazılı olmalı ve satış ekibi tarafından da bilinmelidir. Gıda ürünlerinde yasal azami ödeme sürelerini de hesaba katın.

**Kredi kararını kim verir?** Kredi limitleri satış ekibinin değil, finans ekibinin onayıyla belirlenmelidir; ancak satış ekibi müşteri hakkındaki saha bilgisini paylaşmalıdır. Limit kararında müşterinin ödeme geçmişi, çalışma süresi, sipariş büyüklüğü ve varsa teminatlar dikkate alınır. Limit aşımlarında sevkiyatın otomatik durdurulması ya da onaya bağlanması, sistemde tanımlanmalıdır. Tahsilat takibinde düzenli bir takvim önemlidir: vadesi yaklaşan alacaklar için hatırlatma, vadesi geçenler için arama ve ziyaret, uzun süre gecikenler için hukuki süreç. Hukuki takibe geçmeden önce hukuk danışmanınızla görüşün.

## Bir örnek

> **Örnek (temsili rakamlar):** Satış, alacak ve oranlar varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b4.py` ile yapılmıştır.

Yıllık satışı 60.000.000 TL olan bir dağıtıcının alacak bakiyesi 7.397.260 TL.

- DSO: 7.397.260 / 60.000.000 × 365 = **45,0 gün**

Alacak tahsil süresi 35 güne inerse 60.000.000 × 10 / 365 = **1.643.836 TL** nakit serbest kalır. Aylık %3 finansman maliyetiyle bunun yıllık değeri yaklaşık **699.881 TL**.

Yaşlandırma tablosu (toplam 7.400.000 TL):

| Grup | Tutar | Varsayılan kayıp oranı |
|---|---|---|
| 0–30 gün | 4.200.000 TL | %0 |
| 31–60 gün | 2.000.000 TL | %2 |
| 61–90 gün | 800.000 TL | %10 |
| 90+ gün | 400.000 TL | %50 |

Tahmini kayıp riski: **320.000 TL**. Bu rakam, 90 günü geçen alacakların ne kadar pahalı olduğunu gösterir.

## Sık yapılan hatalar

- **Satış ekibini yalnızca satışla ödüllendirmek.** Tahsilat hedefi olmayan ekip, riskli müşteriye satış yapar.
- **Yaşlandırmayı ay sonunda bakmak.** Gecikme erken fark edilmezse tahsil olasılığı düşer.
- **Limit aşımını tolere etmek.** Kural uygulanmazsa kural yoktur.
- **Vade pazarlığını fiyattan ayrı yapmak.** Uzun vade, gizli bir fiyat indirimidir.

## Pratikte nasıl uygulanır?

- [ ] DSO'yu ve yaşlandırma tablosunu her hafta, müşteri ve temsilci bazında raporlayın.
- [ ] Her müşteri için yazılı bir kredi limiti ve ödeme koşulu belirleyin.
- [ ] Satış ekibinin hedeflerine tahsilat ya da gecikmiş alacak oranı ekleyin.
- [ ] 60 günü geçen alacaklar için bir tahsilat süreci tanımlayın.
- [ ] Karşılık ve hukuki takip konularında mali müşavir ve hukukçunuzla çalışın.

## Daha fazlası

- Brealey, R. A.; Myers, S. C.; Allen, F. (2020). *Principles of Corporate Finance.* (kaynak doğrulanmadı)
