---
id: kb-fmcg-8-5-territory-routing
title: "Bölge tasarımı ve rota planlama"
summary: "Temsilcinin zamanının büyük kısmı yolda geçer. Bu kart dengeli bölge tasarımını, rota günlerini ve yol süresini kısaltmanın ziyaret kapasitesine etkisini anlatır."
course: fmcg
category: saha-satis-ekibi
tags: [saha-satis, pazara-giris, operasyon]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, depo-lojistik-muduru]
level: orta
source_lessons: [FMCG-8.5]
reading_minutes: 3
key_points:
  - "İyi bir bölge tasarımı iş yükünü ve potansiyeli temsilciler arasında dengeler."
  - "Günlük ziyaret kapasitesi, kullanılabilir süre bölü ziyaret ve yol süresi toplamıdır."
  - "Ziyaret arası yol süresini birkaç dakika kısaltmak aylık kapasiteyi belirgin artırır."
  - "Sabit rota günleri, noktanın siparişini planlamasını ve temsilcinin disiplinini kolaylaştırır."
glossary_terms: [ziyaret-sikligi, nokta-evreni]
related: [kb-fmcg-8-4-sales-force-sizing, kb-fmcg-6-1-rtm-channels-formats, kb-fmcg-8-6-sales-org-span-of-control, kb-fmcg-8-10-sfa-data-driven-selling, kb-fmcg-6-2-outlet-universe-segmentation]
sources:
  - title: "Sales Territory Design: Thirty Years of Modeling and Implementation"
    authors: "Zoltners, A. A.; Sinha, P."
    year: 2005
    type: article
    doi: "10.1287/mksc.1050.0133"
    url: "https://doi.org/10.1287/mksc.1050.0133"
    verified: true
    checked_on: 2026-10-28
    note: "Marketing Science 24(3), 313–331."
  - title: "Building a Winning Sales Force"
    authors: "Zoltners, A. A.; Sinha, P.; Lorimer, S. E."
    year: 2009
    type: book
    verified: false
    note: "Kitap; künye kontrol edilmedi."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Ekip büyüklüğü doğru olsa bile bölgeler dengesizse bazı temsilciler aşırı yüklenir, bazıları boş kalır. Rota kötü planlanmışsa temsilci günün önemli kısmını trafikte geçirir. Bu kart, bölge ve rota tasarımının kapasiteye etkisini somut olarak gösterir.

## Temel fikir

**Bölge tasarımı.** Zoltners ve Sinha (2005), satış bölgesi tasarımı üzerine yaptıkları çalışmada iyi tasarlanmış bölgelerin iş yükünü ve potansiyeli temsilciler arasında dengelediğini ve yol süresini azalttığını anlatır. Dengesiz bölgeler hem satış kaybına hem de adil olmayan hedeflere yol açar.

Dengeleme ölçütleri:

- **İş yükü:** Ziyaret ihtiyacı (nokta sayısı × sıklık × ziyaret süresi) ve yol süresi.
- **Potansiyel:** Bölgedeki karşılanmamış satış fırsatı.
- **Coğrafya:** Bölgenin bütünlüğü, trafik ve ulaşım kolaylığı.

**Günlük kapasite.** Kullanılabilir süre / (ortalama ziyaret süresi + ortalama yol süresi). Kullanılabilir süre, çalışma süresinden mola, ofis ve yükleme gibi işler çıkarılarak bulunur.

**Rota planlama.** Bölge, haftanın günlerine göre rotalara ayrılır. Her rota coğrafi olarak bir arada olan noktalardan oluşur. Sık ziyaret edilmesi gereken noktalar birden fazla rotada yer alır. Sabit rota günleri, nokta sahibinin temsilciyi hangi gün bekleyeceğini bilmesini sağlar.

**Teknoloji.** Rota optimizasyon yazılımları ve satış otomasyon sistemleri (SFA), noktaların konumunu kullanarak rotaları planlayabilir ve gerçekleşen ziyaretleri izleyebilir.

**Bölgeleri dengelemek.** Dengeli bir bölge, yalnızca nokta sayısında değil, iş yükünde ve potansiyelde de dengelidir. İş yükü; ziyaret sayısı, ziyaret süresi ve yol süresinin toplamıdır. Potansiyel ise bölgedeki noktaların toplam kategori satışıdır. Bir bölgenin iş yükü çok yüksekse ziyaretler kısalır ya da atlanır; potansiyeli çok düşükse temsilcinin hedefi ve primi adil olmaz. Rota planlamasında noktaları coğrafi kümelere ayırıp her kümeyi haftanın bir gününe bağlamak yaygın bir yöntemdir. Trafik, pazar günleri ve noktaların açılış saatleri rotayı etkiler; SFA'daki konum ve ziyaret süresi verileri, planın gerçekte nasıl uygulandığını görmenizi sağlar.

## Bir örnek

> **Örnek (temsili rakamlar):** Süreler ve gün sayısı varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b4.py` ile yapılmıştır.

Bir temsilcinin günlük kullanılabilir süresi 7 saat (420 dakika). Ortalama ziyaret 20 dakika.

| Ortalama yol süresi | Günlük ziyaret | Aylık ziyaret (22 gün) |
|---|---|---|
| 15 dakika | 12 | 264 |
| 10 dakika | 14 | 308 |

Rotalar yeniden düzenlenip yol süresi 5 dakika kısalınca, temsilci ayda **44** ziyaret daha yapabiliyor. Bu, yaklaşık iki günlük ek kapasite demek. Bu kapasite yeni noktalara, öncelikli noktalara daha sık ziyarete ya da daha uzun mağaza içi çalışmaya ayrılabilir.

## Sık yapılan hatalar

- **Bölgeleri yalnızca satışa göre bölmek.** Satış, mevcut durumu gösterir; potansiyel ve iş yükü de hesaba katılmalı.
- **Rotaları yıllarca değiştirmemek.** Nokta evreni değiştikçe rotalar da güncellenmeli.
- **Yol süresini ölçmemek.** Ölçülmeyen kayıp görülmez.
- **Plana uyumu izlememek.** Plan yapılır, ama temsilci farklı bir sıra izliyorsa fayda kaybolur.

## Pratikte nasıl uygulanır?

- [ ] Her noktanın konumunu, segmentini ve ziyaret sıklığını sisteme girin.
- [ ] Temsilci başına iş yükünü ve potansiyeli hesaplayın; dengesiz bölgeleri belirleyin.
- [ ] Rotaları coğrafi yakınlığa göre yeniden düzenleyin ve yol süresini ölçün.
- [ ] Plana uyumu (planlanan ziyaretlerin gerçekleşme oranını) her hafta izleyin.
- [ ] Rotaları yılda en az bir kez, nokta evreni güncellendiğinde gözden geçirin.

## Daha fazlası

- Zoltners, A. A.; Sinha, P. (2005). *Sales Territory Design: Thirty Years of Modeling and Implementation.* Marketing Science 24(3), 313–331. https://doi.org/10.1287/mksc.1050.0133
- Zoltners, A. A.; Sinha, P.; Lorimer, S. E. (2009). *Building a Winning Sales Force.* (kaynak doğrulanmadı)
