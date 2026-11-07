---
id: kb-fmcg-6-2-outlet-universe-segmentation
title: "Nokta evreni ve segmentasyon: Hangi noktaya, ne sıklıkla?"
summary: "Satış ekibinin zamanı sınırlıdır ve her nokta aynı potansiyele sahip değildir. Bu kart bölgenizdeki satış noktalarının tamamını listelemeyi, onları potansiyele göre gruplamayı ve ziyaret sıklığından gereken temsilci sayısına ulaşmayı anlatır."
course: fmcg
category: dagitim-modeli
tags: [dagitim, saha-satis, analitik]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, saha-satis-temsilcisi]
level: temel
source_lessons: [FMCG-6.2]
reading_minutes: 3
key_points:
  - "Nokta evreni, bölgede kategorinizi satan ya da satabilecek bütün noktaların listesidir; yalnızca bugün müşteriniz olanlar değil."
  - "Noktaları potansiyele göre gruplamak, ziyaret sıklığını ve hizmet düzeyini farklılaştırmayı sağlar."
  - "Toplam ziyaret ihtiyacı, nokta sayısı ile ziyaret sıklığının çarpımıdır; temsilci sayısı buradan çıkar."
  - "Düşük potansiyelli noktaları daha seyrek ya da farklı bir modelle (telefon, toptancı, çevrim içi) hizmetlendirmek maliyeti düşürür."
glossary_terms: [nokta-evreni, ziyaret-sikligi, sayisal-dagitim]
related: [kb-fmcg-6-1-rtm-channels-formats, kb-fmcg-6-3-cost-to-serve, kb-fmcg-8-4-sales-force-sizing, kb-fmcg-8-5-territory-routing, kb-fmcg-3-4-mental-physical-availability]
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
  - title: "CALLPLAN: An Interactive Salesman's Call Planning System"
    authors: "Lodish, L. M."
    year: 1971
    type: article
    doi: "10.1287/mnsc.18.4.P25"
    url: "https://doi.org/10.1287/mnsc.18.4.P25"
    verified: true
    checked_on: 2026-10-28
    note: "Management Science 18(4-II), P25–P40."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

"Kaç satış temsilcisine ihtiyacımız var?" ve "Hangi noktaya haftada kaç kez gidelim?" soruları, bölgenizdeki noktaları ne kadar iyi tanıdığınıza bağlıdır. Bu kart, nokta evreninizi kurmanızı ve ziyaret planını potansiyele göre yapmanızı sağlar.

## Temel fikir

**Nokta evreni** (*outlet universe*). Bölgenizde kategorinizi satan ya da satabilecek bütün noktaların listesidir. Bugünkü müşterilerinizin yanı sıra rakibin çalıştığı, sizin henüz girmediğiniz noktaları da içerir. Kaynakları: kendi müşteri listeniz, dağıtıcının listesi, saha taraması, ticari rehberler ve panel sağlayıcılarının verileri.

**Segmentasyon.** Her noktaya aynı sıklıkta gitmek kaynak israfıdır. Noktalar genellikle iki ölçüte göre gruplanır:

- **Potansiyel:** Noktanın kategori satışı ya da büyüklüğü, konumu, müşteri trafiği.
- **Mevcut performans:** Sizin oradaki satışınız ve payınız.

Basit bir uygulama A, B ve C gruplarıdır: A en yüksek potansiyelli noktalar, C en düşük. Her gruba farklı ziyaret sıklığı ve hizmet düzeyi verilir.

**Ziyaret sıklığından ekip büyüklüğüne.** Toplam ziyaret ihtiyacı, her gruptaki nokta sayısının ziyaret sıklığıyla çarpımlarının toplamıdır. Bunu bir temsilcinin aylık ziyaret kapasitesine bölerseniz gereken temsilci sayısını bulursunuz. Lodish (1971), ziyaret sıklığını her müşterinin ziyarete verdiği tepkiye göre belirleyen bir planlama modeli önerir. Zoltners ve Sinha (2005), satış bölgesi tasarımı üzerine otuz yıllık modelleme ve uygulama deneyimini özetler. Bu çalışmalar, ziyaret kararlarını potansiyele dayandırmanın değerini gösterir.

**Nokta evrenini güncel tutmak.** Geleneksel kanalda noktalar sık açılır, kapanır ve el değiştirir. Bu nedenle nokta evreni bir kez çıkarılıp bırakılmamalı; temsilcilerin saha gözlemleri, dağıtıcı müşteri listeleri ve gerekirse saha sayımlarıyla düzenli güncellenmelidir. Her nokta için temel bilgiler (kanal türü, büyüklük, konum, kategoriyi satıp satmadığı, hangi dağıtıcıdan aldığı) SFA'da tutulmalıdır. Segment ölçütleri de basit ve gözlemlenebilir olmalıdır; temsilcinin sahada ölçemediği bir ölçüt tutarsız uygulanır. Segmentler yılda en az bir kez gözden geçirilip ziyaret sıklıkları buna göre yeniden planlanmalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Nokta sayıları, sıklıklar ve kapasite varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b3.py` ile yapılmıştır.

| Grup | Nokta | Aylık ziyaret | Toplam ziyaret |
|---|---|---|---|
| A | 500 | 4 | 2.000 |
| B | 1.500 | 2 | 3.000 |
| C | 3.000 | 1 | 3.000 |

Toplam **8.000 ziyaret/ay**. Bir temsilci günde 8 ziyaret, ayda 22 iş günü çalışıyor: 176 ziyaret. Gereken temsilci: 8.000 / 176 = 45,45, yani **46 temsilci**.

C grubunu iki ayda bir ziyarete indirip araya telefonla sipariş koyarsanız toplam ziyaret **6.500'e**, gereken temsilci **37'ye** düşer.

## Sık yapılan hatalar

- **Evreni yalnızca mevcut müşterilerle sınırlamak.** Girmediğiniz noktalar büyüme fırsatınızdır.
- **Listeyi güncellememek.** Noktalar açılır, kapanır, el değiştirir; eski liste yanlış planlama demektir.
- **Herkese aynı sıklık.** Küçük noktaya haftalık ziyaret, büyük noktaya aylık ziyaret kadar verimsizdir.
- **Gruplamayı yalnızca bugünkü satışa göre yapmak.** Potansiyeli yüksek ama payınız düşük noktalar C grubuna düşer ve hiç büyümez.

## Pratikte nasıl uygulanır?

- [ ] Bölge bazında nokta evrenini çıkarın ve her noktaya bir potansiyel puanı verin.
- [ ] Noktaları A, B ve C gruplarına ayırın; her grubun ziyaret sıklığını ve hizmet modelini belirleyin.
- [ ] Toplam ziyaret ihtiyacını ve gereken temsilci sayısını hesaplayın.
- [ ] Listeyi en az yılda bir kez saha taramasıyla güncelleyin.

## Daha fazlası

- Zoltners, A. A.; Sinha, P. (2005). *Sales Territory Design: Thirty Years of Modeling and Implementation.* Marketing Science 24(3), 313–331. https://doi.org/10.1287/mksc.1050.0133
- Lodish, L. M. (1971). *CALLPLAN: An Interactive Salesman's Call Planning System.* Management Science 18(4-II), P25–P40. https://doi.org/10.1287/mnsc.18.4.P25
