---
id: kb-ea-18-4-post-go-live-dip
title: "Canlıya geçiş sonrası düşüş: Hayatta kalmak ve gelişmek"
summary: "Yeni bir ERP'nin canlıya geçişinden sonraki haftalarda performansın neden düştüğünü, bu dönemin nasıl planlanacağını ve sistemi yalnızca kullanmaktan faydasını almaya geçişin nasıl yönetileceğini anlatır."
course: ea
category: yazilim-secimi-ve-proje
tags: [erp, canliya-gecis, stabilizasyon, degisim-yonetimi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, it-yoneticisi]
level: orta
source_lessons: [EA-18.4]
reading_minutes: 3
key_points:
  - "Canlıya geçişten sonra verimliliğin geçici olarak düşmesi normaldir ve planlanmalıdır."
  - "Düşüşün derinliği ve süresi; eğitim, veri kalitesi ve destek gücüyle belirlenir."
  - "Entegre sistemde bir bölümün hatası diğer bölümlere hızla yayılır."
  - "Stabilizasyondan sonra faydayı almak için süreç iyileştirme ayrı bir faz olarak yürütülmelidir."
  - "Birkaç basit göstergeyle günlük takip, sorunları erken gösterir."
glossary_terms: [erp, canliya-gecis]
related: [kb-ea-18-3-why-erp-projects-fail, kb-ea-41-5-cutover-plan, kb-ea-18-7-change-management-training, kb-ea-3-2-it-plus-process-complementarity]
sources:
  - title: "The ERP Revolution: Surviving vs. Thriving"
    authors: "Ross, J.; Vitale, M."
    year: 2000
    type: article
    doi: "10.1023/A:1026500224101"
    url: "https://doi.org/10.1023/A:1026500224101"
    verified: true
    checked_on: 2026-10-28
  - title: "Learning to Implement Enterprise Systems: An Exploratory Study of the Dialectics of Change"
    authors: "Robey, D.; Ross, J.; Boudreau, M."
    year: 2002
    type: article
    doi: "10.1080/07421222.2002.11045713"
    url: "https://doi.org/10.1080/07421222.2002.11045713"
    verified: true
    checked_on: 2026-10-28
  - title: "What Happens After ERP Implementation: Understanding the Impact of Inter Dependence and Differentiation on Plant-Level Outcomes1"
    authors: "Gattiker, T.; Goodhue, D."
    year: 2005
    type: article
    doi: "10.2307/25148695"
    url: "https://doi.org/10.2307/25148695"
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

ERP'nin canlıya alındığı gün proje bitmez; asıl zor dönem başlar. Siparişler yavaşlar, faturalar gecikir, depo eski alışkanlıklarına döner. Bu kart, bu dönemi önceden planlamanıza yardım eder.

## Temel fikir

Ross ve Vitale (2000), ERP sonrası süreci iki aşamada ele alır: önce **hayatta kalmak** (*surviving*), sonra **gelişmek** (*thriving*). Canlıya geçişin hemen ardından performans çoğu zaman düşer; firma yeni süreçleri öğrenirken eski hızına dönmeye çalışır. Ancak bu dönem atlatıldıktan sonra süreç iyileştirmeleriyle sistemden gerçek fayda alınır.

Düşüşün nedenleri:

- **Öğrenme:** Robey ve arkadaşları (2002), kullanıcıların yeni sistemi öğrenmesinin ve eski bilgiyi bırakmasının zaman aldığını gösterir.
- **Karşılıklı bağımlılık:** Gattiker ve Goodhue (2005), entegre sistemde bölümlerin birbirine daha çok bağlandığını gösterir. Satıştaki yanlış birim, depoda yanlış toplama ve muhasebede yanlış faturaya dönüşür.
- **Veri hataları:** Taşınan verideki eksikler ilk haftalarda ortaya çıkar.

İyi planlanmış bir geçişte düşüş daha sığ ve kısa olur. Bunun için yoğun destek ekibi (*hypercare*), kilit kullanıcıların sahada olması ve günlük izlenen birkaç gösterge gerekir.

### Düşüş dönemini yönetmek

Ross ve Vitale'nin çalışması, canlıya geçişten sonra performansın geçici olarak düşmesinin olağan olduğunu ve bu dönemin bilinçli yönetilmesi gerektiğini gösterir. Bu dönemde yapılabilecekler şunlardır:

- **Beklentiyi önceden yönetin:** Üst yönetime ve çalışanlara, ilk haftalarda yavaşlama ve hatalar yaşanabileceği önceden anlatılmalıdır. Beklenmeyen düşüş, projeye olan güveni sarsar.
- **Yoğun destek sağlayın:** İlk haftalarda kilit kullanıcılar ve danışmanlar kullanıcıların yanında olmalıdır. Sorulara hızlı cevap verilmesi, kullanıcıların eski yöntemlere dönmesini önler.
- **Günlük durum toplantıları:** Açık sorunlar, sipariş ve fatura hacimleri, bekleyen işlemler ve kritik hatalar her gün kısa bir toplantıda gözden geçirilmelidir.
- **Müşteri etkisini sınırlayın:** Sevkiyat ve faturalama gecikmeleri, önemli müşterilere önceden bildirilmelidir. Gerekirse kritik siparişler için geçici özel önlemler alınmalıdır.
- **Sorunları sınıflandırın:** Yazılım hatası, ayar eksikliği, veri hatası ve eğitim eksikliği farklı çözümler gerektirir.

**Düşüşten sonra.** Robey, Ross ve Boudreau'nun vurguladığı gibi, sistemin asıl faydası çoğu zaman istikrar sağlandıktan sonra, yeni yeteneklerin öğrenilip kullanılmasıyla ortaya çıkar. Bu nedenle proje, canlıya geçişle bitmemeli; iyileştirme ve ek eğitim için bir sonraki aşama planlanmalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b4.py` ile yapılmıştır.

Bir bayi, eski sistemde günde ortalama 400 sipariş işliyor. Yeni ERP'ye geçişten sonra:

| Hafta | Günlük işlenen sipariş | Önceki seviyeye göre |
|---|---|---|
| 1 | 260 | %-35,0 |
| 2 | 300 | %-25,0 |
| 4 | 360 | %-10,0 |
| 8 | 410 | %2,5 |

Bayi, ilk iki hafta için geçici personel ve fazla mesai planlamış, büyük müşterilere sevkiyatların bir gün gecikebileceğini önceden bildirmiş. Her sabah 15 dakikalık bir toplantıda açık sorunlar, işlenen sipariş sayısı ve faturalanamayan sevkiyatlar gözden geçiriliyor. Sekizinci haftada eski seviye aşılıyor ve ikinci faz olarak süreç iyileştirmeleri başlıyor.

## Sık yapılan hatalar

- Canlıya geçişi yılın en yoğun dönemine denk getirmek.
- Danışmanları canlıya geçişin ertesi haftası projeden çekmek.
- Düşüşü sistemin başarısızlığı olarak yorumlayıp eski yöntemlere (Excel) dönmek.
- Stabilizasyondan sonra iyileştirme fazını hiç başlatmamak.

## Pratikte nasıl uygulanır?

- [ ] Canlıya geçişi düşük sezona planlayın.
- [ ] İlk 4–8 hafta için yoğun destek ekibi ve kilit kullanıcı nöbeti kurun.
- [ ] Günlük takip edilecek 3–5 gösterge belirleyin.
- [ ] Büyük müşterileri ve tedarikçileri olası gecikmeler için önceden bilgilendirin.
- [ ] Stabilizasyon sonrasında fayda odaklı iyileştirme fazı planlayın.

## Daha fazlası

- Ross ve Vitale (2000), *Information Systems Frontiers*. https://doi.org/10.1023/A:1026500224101
- Robey ve ark. (2002), *Journal of Management Information Systems*. https://doi.org/10.1080/07421222.2002.11045713
- Gattiker ve Goodhue (2005), *MIS Quarterly*. https://doi.org/10.2307/25148695
