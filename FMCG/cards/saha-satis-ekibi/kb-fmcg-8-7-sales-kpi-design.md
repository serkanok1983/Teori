---
id: kb-fmcg-8-7-sales-kpi-design
title: "Satış performans göstergelerini tasarlamak"
summary: "Ölçtüğünüz şey, ekibin önceliği olur. Bu kart satış performans göstergelerini sonuç ve faaliyet göstergeleri olarak ayırmayı, gösterge ağacı kurmayı ve ağırlıklı bir skor kartı hazırlamayı anlatır."
course: fmcg
category: saha-satis-ekibi
tags: [saha-satis, analitik, liderlik]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: temel
source_lessons: [FMCG-8.7]
reading_minutes: 3
key_points:
  - "Sonuç göstergeleri neyin olduğunu, faaliyet göstergeleri bunun neden olduğunu gösterir."
  - "Gösterge ağacı, satış gibi bir sonucu temsilcinin etkileyebileceği alt göstergelere ayırır."
  - "Skor kartında az sayıda, net tanımlı ve ağırlıklandırılmış gösterge bulunmalıdır."
  - "Göstergeler birbirini dengelemeli; yalnızca hacim ölçülürse tahsilat ve kalite bozulur."
glossary_terms: [sayisal-dagitim, ziyaret-sikligi]
related: [kb-fmcg-8-3-salesperson-performance-drivers, kb-fmcg-8-8-incentive-compensation, kb-fmcg-8-13-sales-analytics, kb-fmcg-9-5-perfect-store, kb-fmcg-7-4-distributor-selection-kpis]
sources:
  - title: "Sales Force Management"
    authors: "Churchill, G. A.; Ford, N. M.; Walker, O. C."
    year: 2000
    type: book
    verified: false
    note: "Kitap; baskı yılı kontrol edilmedi."
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

Birçok satış raporu onlarca gösterge içerir ve hiçbiri ekibin ne yapması gerektiğini net söylemez. Bu kart, az ama doğru göstergeyle bir skor kartı kurmanızı ve göstergeleri birbirine bağlamanızı sağlar.

## Temel fikir

**Sonuç ve faaliyet göstergeleri.** Satış yönetimi kaynakları, satış ekibinin değerlendirilmesinde sonuç ve davranış ölçütlerinin birlikte kullanılmasını önerir (örneğin Churchill ve arkadaşlarının satış yönetimi kitabı).

- **Sonuç göstergeleri:** Satış, hedef gerçekleşme, büyüme, sayısal dağıtım, tahsilat.
- **Faaliyet göstergeleri:** Ziyaret sayısı, plana uyum, sipariş oranı, kalem sayısı, mağaza içi uygulama puanı.

Sonuç göstergeleri gecikmeli gelir. Faaliyet göstergeleri ise erken uyarı verir.

**Gösterge ağacı.** Bir sonucu, onu oluşturan bileşenlere ayırırsınız:

- Satış = ziyaret × sipariş oranı × kalem sayısı × kalem tutarı
- Sayısal dağıtım = ürünü bulunduran nokta / toplam nokta

Her dal, temsilcinin etkileyebileceği bir davranışa bağlanır.

**İyi bir göstergenin özellikleri.**

- **Net tanım:** Nasıl hesaplandığı herkes için aynı.
- **Etkilenebilirlik:** Temsilci göstergeyi davranışıyla değiştirebilmeli.
- **Veri güvenilirliği:** Kaynağı ve güncellenme sıklığı belli.
- **Denge:** Bir göstergeyi şişirmek, başka bir göstergeyi bozuyorsa ikisi birlikte ölçülmeli.

**Skor kartı.** Dört ile altı arası gösterge, her birine bir ağırlık. Uç değerlerin skoru bozmaması için her göstergede bir üst sınır konabilir.

**Gösterge sayısı ve veri kalitesi.** Bir temsilcinin aynı anda takip edebileceği gösterge sayısı sınırlıdır. Pratikte birincil puan kartında birkaç sonuç ve birkaç faaliyet göstergesi tutmak, geri kalanları yöneticinin izleme panosuna bırakmak daha etkilidir. Her göstergenin tanımı, veri kaynağı (SFA, ERP, dağıtıcı raporu), güncelleme sıklığı ve sorumlusu yazılı olmalıdır. Temsilcinin doğrudan etkileyemediği göstergeler (örneğin merkezi fiyat kararları) prim hesabına girmemeli, ama izlenmelidir. Göstergeler değiştirildiğinde eski ve yeni tanımlar bir dönem birlikte raporlanmalı; aksi hâlde eğilimler karşılaştırılamaz. Son olarak, her göstergenin istenmeyen bir davranışa yol açıp açmadığını, örneğin dönem sonunda stok yüklemeyi teşvik edip etmediğini düzenli kontrol edin.

## Bir örnek

> **Örnek (temsili rakamlar):** Göstergeler, ağırlıklar ve gerçekleşmeler varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b4.py` ile yapılmıştır.

Bir temsilcinin üç aylık skor kartı (her gösterge en fazla %120 ile sınırlı):

| Gösterge | Ağırlık | Hedefe göre gerçekleşme |
|---|---|---|
| Satış hedefi | %40 | %105 |
| Sayısal dağıtım hedefi | %25 | %92 |
| Tahsilat | %20 | %98 |
| Mükemmel mağaza puanı | %15 | %110 |

Ağırlıklı skor: **%101,1**. Temsilci toplamda hedefin üstünde. Ama dağıtım hedefinin altında kalmış. Satış hedefini mevcut noktalardaki hacimle aşmış, yeni noktalara yeterince ulaşmamış olabilir. Skor kartı bu dengesizliği görünür kılıyor.

## Sık yapılan hatalar

- **Çok fazla gösterge.** On beş gösterge, hiçbirine öncelik verilmemesi demektir.
- **Yalnızca hacim.** Tahsilat ve dağıtım ölçülmezse ekip kolay hacme yönelir.
- **Tanımı belirsiz göstergeler.** Herkes farklı hesaplarsa tartışma rakamın doğruluğu üzerine olur.
- **Temsilcinin etkileyemediği göstergeler.** Kontrol dışı bir gösterge motivasyonu düşürür.

## Pratikte nasıl uygulanır?

- [ ] Ana sonuç göstergelerini belirleyin ve her biri için bir gösterge ağacı çizin.
- [ ] Skor kartına dört ile altı gösterge seçin; her birinin tanımını ve veri kaynağını yazın.
- [ ] Ağırlıkları stratejinize göre verin; örneğin dağıtım dönemi için dağıtımın ağırlığını artırın.
- [ ] Faaliyet göstergelerini haftalık, sonuç göstergelerini aylık izleyin.
- [ ] Göstergeleri yılda bir gözden geçirin ve kullanılmayanları kaldırın.

## Daha fazlası

- Churchill, G. A.; Ford, N. M.; Walker, O. C. (2000). *Sales Force Management.* (kaynak doğrulanmadı)
- Zoltners, A. A.; Sinha, P.; Lorimer, S. E. (2009). *Building a Winning Sales Force.* (kaynak doğrulanmadı)
