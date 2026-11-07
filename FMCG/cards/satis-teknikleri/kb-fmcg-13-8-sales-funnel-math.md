---
id: kb-fmcg-13-8-sales-funnel-math
title: "Satış hunisi matematiği: Hedeften geriye ziyaret sayısına"
summary: "Satış hunisi, bir hedefe ulaşmak için kaç görüşme, teklif ve kapanış gerektiğini aşamaların dönüşüm oranlarıyla hesaplar. Bu kart huni hesabını, hızlı tüketimde listeleme ve yeni nokta açma hedeflerine uygulanmasını ve dönüşüm oranını iyileştirmenin etkisini anlatır."
course: fmcg
category: satis-teknikleri
tags: [satis-yonetimi, satis-hunisi, planlama]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: orta
source_lessons: [FMCG-13.8]
reading_minutes: 3
key_points:
  - "Huni, satış sürecini ziyaret, teklif ve kapanış gibi aşamalara ayırır."
  - "Toplam dönüşüm oranı, aşama oranlarının çarpımıdır."
  - "Gereken ziyaret sayısı, hedefin toplam dönüşüm oranına bölünmesiyle bulunur."
  - "Bir aşamadaki küçük bir iyileşme, gereken iş yükünü belirgin biçimde azaltabilir."
  - "Oranlar, temsilcinin ve müşteri segmentinin kendi geçmiş verisinden hesaplanmalıdır."
glossary_terms: [satis-hunisi, donusum-orani, ziyaret-sikligi, nokta-evreni]
related: [kb-fmcg-13-9-prospecting-account-segmentation, kb-fmcg-13-16-sales-forecasting, kb-fmcg-13-3-challenger-meddic-sandler, kb-fmcg-8-2-structured-sales-call]
sources:
  - title: "ZS"
    authors: "ZS Associates"
    year: 2026
    type: web
    url: "https://www.zs.com/"
    verified: true
    checked_on: 2026-10-28
  - title: "Breaking the Sales Force Incentive Addiction: A Balanced Approach to Sales Force Effectiveness"
    authors: "Zoltners, A. A.; Sinha, P.; Lorimer, S. E."
    year: 2012
    type: article
    doi: "10.2753/PSS0885-3134320201"
    url: "https://doi.org/10.2753/PSS0885-3134320201"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Personal Selling & Sales Management 32(2), 171–186."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Satış müdürü, bir temsilciye çeyrek sonuna kadar **30** yeni noktada listeleme hedefi verir. Temsilci bunun için kaç market ziyaret etmesi gerektiğini bilmezse, ya çok geç harekete geçer ya da zamanını yanlış yerlere harcar. Satış hunisi (*sales funnel*), hedefi gereken faaliyet miktarına çevirir ve hangi aşamanın iyileştirilmesi gerektiğini gösterir.

## Temel fikir

**Aşamalar.** Hızlı tüketimde yeni nokta açma ya da listeleme süreci tipik olarak şu aşamalardan oluşur:

1. **İlk ziyaret:** Potansiyel noktayla ilk görüşme
2. **Teklif:** Karar vericiye somut bir öneri sunulması
3. **Deneme ya da anlaşma:** Ürünün denenmesi ya da ilk sipariş
4. **Kalıcı listeleme:** Ürünün düzenli sipariş edilmesi

Her aşama arasında bir dönüşüm oranı (*conversion rate*) vardır.

**Hesap.** Toplam dönüşüm oranı, aşama oranlarının çarpımıdır. Gereken ilk ziyaret sayısı:

Gereken ziyaret = Hedef ÷ Toplam dönüşüm oranı

Bu basit hesap, iki soruya yanıt verir: Hedef bu iş yüküyle ulaşılabilir mi? Hangi aşamada iyileşme en büyük etkiyi yaratır?

**Oranların kaynağı.** Dönüşüm oranları sezgiye değil, SFA sistemindeki geçmiş verilere dayanmalıdır. Oranlar kanala, müşteri segmentine ve temsilcinin deneyimine göre farklılık gösterir. Satış gücü yönetimi literatürü (örneğin Zoltners ve arkadaşlarının çalışmaları), faaliyet ve sonuç ölçütlerinin birlikte izlenmesini önerir.

**Huniyi zamana yaymak.** Huni hesabı yalnızca kaç ziyaret gerektiğini değil, ne zaman başlanması gerektiğini de gösterir. İlk ziyaretten kalıcı listelemeye geçen ortalama süre biliniyorsa, çeyrek sonu hedefi için ziyaretlerin hangi haftalarda yapılması gerektiği geriye doğru planlanabilir. Ayrıca huninin her aşamasında bekleyen fırsat sayısını haftalık izlemek, erken uyarı verir: Teklif aşamasında yeterli fırsat yoksa, birkaç hafta sonra kapanış sayısı da düşecektir. Huni verisi temsilciyi denetlemek için değil, koçluk için kullanılmalıdır; hangi aşamada kayıp olduğu, hangi becerinin geliştirilmesi gerektiğini gösterir.

## Bir örnek

> **Örnek (temsili rakamlar):** Hedef ve dönüşüm oranları varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b8.py` ile yapılmıştır.

Hedef: çeyrek sonunda **30** kalıcı listeleme. Temsilcinin geçmiş oranları:

| Aşama | Dönüşüm oranı |
|---|---:|
| İlk ziyaret → teklif | 0,4 |
| Teklif → deneme | 0,5 |
| Deneme → kalıcı listeleme | 0,6 |
| **Toplam** | **%12,0** |

Gereken ilk ziyaret: 30 ÷ 0,12 = **250**.

Temsilci ve müdürü, deneme önerilerini iyileştirmek için daha net bir teklif şablonu hazırlıyor. Teklif → deneme oranı **0,5**'ten **0,6**'ya çıkarsa toplam oran **%14,4** olur ve gereken ziyaret sayısı yaklaşık **208**'e düşer. Yani bir aşamadaki iyileşme, yaklaşık **42** ziyaretlik iş yükünden tasarruf sağlar; bu süre mevcut müşterilerin hizmetine ayrılabilir.

## Sık yapılan hatalar

- **Yalnızca son sonuca bakmak.** Hangi aşamada kayıp olduğunu görmeden iyileştirme yapılamaz.
- **Genel oranları herkese uygulamak.** Yeni ve deneyimli temsilcilerin oranları farklıdır.
- **Ziyaret sayısını artırmayı tek çözüm görmek.** Kalite iyileşmesi çoğu zaman daha ucuzdur.
- **Süreyi hesaba katmamak.** Aşamalar arasında haftalar geçebilir; ziyaretler zamanında başlamalıdır.
- **Verileri SFA'ya girmemek.** Oranlar hesaplanamaz.

## Pratikte nasıl uygulanır?

- [ ] Satış sürecinizin aşamalarını tanımlayın ve SFA'da izleyin.
- [ ] Her aşamanın dönüşüm oranını segment ve temsilci düzeyinde hesaplayın.
- [ ] Hedeflerden geriye gereken faaliyet miktarını hesaplayın.
- [ ] En düşük oranlı aşamaya koçluk ve araç desteği verin.
- [ ] Oranları çeyreklik olarak güncelleyin.

## Daha fazlası

- ZS Associates (2026). *ZS.* https://www.zs.com/
- Zoltners, A. A.; Sinha, P.; Lorimer, S. E. (2012). *Breaking the Sales Force Incentive Addiction: A Balanced Approach to Sales Force Effectiveness.* Journal of Personal Selling & Sales Management 32(2), 171–186. https://doi.org/10.2753/PSS0885-3134320201
