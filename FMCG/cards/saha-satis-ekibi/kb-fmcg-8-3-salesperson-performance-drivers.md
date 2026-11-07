---
id: kb-fmcg-8-3-salesperson-performance-drivers
title: "Satış temsilcisinin performansını ne belirler?"
summary: "Satış performansı yetenek kadar rol netliği, beceri, motivasyon ve çevre koşullarına da bağlıdır. Bu kart satış performansı üzerine yapılmış meta-analizlerin genel bulgularını ve bunları saha yönetiminde nasıl kullanacağınızı anlatır."
course: fmcg
category: saha-satis-ekibi
tags: [saha-satis, liderlik, analitik]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: orta
source_lessons: [FMCG-8.3]
reading_minutes: 3
key_points:
  - "Meta-analizler, kişisel özelliklerin tek başına performansın küçük bir kısmını açıkladığını gösterir."
  - "Rol algısı, beceri ve motivasyon gibi yönetilebilir faktörler performansla daha güçlü ilişkilidir."
  - "Satış rakamı çarpanlara ayrılınca, temsilcinin hangi alanda geliştirilmesi gerektiği görülür."
  - "Bölge potansiyeli gibi temsilcinin kontrolü dışındaki faktörler ayrıştırılmadan performans değerlendirilmemelidir."
glossary_terms: [ziyaret-sikligi, sepet-buyuklugu]
related: [kb-fmcg-8-2-structured-sales-call, kb-fmcg-8-9-coaching, kb-fmcg-8-12-salesperson-motivation, kb-fmcg-8-7-sales-kpi-design, kb-fmcg-8-13-sales-analytics]
sources:
  - title: "The Determinants of Salesperson Performance: A Meta-Analysis"
    authors: "Churchill, G. A.; Ford, N. M.; Hartley, S. W.; Walker, O. C."
    year: 1985
    type: article
    doi: "10.2307/3151357"
    url: "https://doi.org/10.2307/3151357"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Marketing Research 22(2), 103–118."
  - title: "Drivers of Sales Performance: A Contemporary Meta-Analysis"
    authors: "Verbeke, W.; Dietz, B.; Verwaal, E."
    year: 2011
    type: article
    doi: "10.1007/s11747-010-0211-8"
    url: "https://doi.org/10.1007/s11747-010-0211-8"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of the Academy of Marketing Science 39(3), 407–428 (Crossref çevrimiçi yılı 2010)."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

En iyi satıcıyı işe almak önemlidir. Ama sahadaki ekibin çoğu ortalama performans gösterir ve asıl fark, bu ekibin nasıl yönetildiğinden çıkar. Bu kart, performansın hangi faktörlere bağlı olduğunu ve yöneticinin neyi değiştirebileceğini gösterir.

## Temel fikir

**Meta-analiz bulguları.** Churchill, Ford, Hartley ve Walker (1985), satış performansının belirleyicileri üzerine yayımlanmış çalışmaları birleştiren bir meta-analiz yaptı. Yetenek, beceri, rol algısı, motivasyon, kişisel faktörler ve örgütsel faktörleri karşılaştırdılar. Bulgulara göre, tek başına hiçbir faktör grubu performansın büyük kısmını açıklamıyordu. Kişisel özellikler (yaş, boy, geçmiş gibi) zayıf ilişkiliydi. Rol algısı ve beceri ise görece daha güçlü ilişkiliydi.

Verbeke, Dietz ve Verwaal (2011), daha sonra yapılan çalışmaları da ekleyerek bu analizi güncelledi. Onların bulgularında da satışa ilişkin bilgi, uyarlanabilir satış, rol netliği ve bilişsel yetenek öne çıkan belirleyiciler arasındaydı.

**Yöneticiye düşen.** Bu bulgulardan çıkan sonuç: Performansın önemli bir kısmı yönetilebilir faktörlere bağlıdır. Temsilci neyin beklendiğini net biliyor mu, ürünü ve müşteriyi tanıyor mu, ziyareti doğru yapıyor mu, motivasyonu yerinde mi?

**Performansı çarpanlara ayırmak.** Satış = ziyaret sayısı × sipariş oranı × sipariş başı kalem × kalem tutarı. Düşük satışın nedeni hangi çarpandaysa gelişim de oraya yönelmelidir:

- **Ziyaret sayısı düşük:** Planlama, rota ya da disiplin sorunu.
- **Sipariş oranı düşük:** Hazırlık, ilişki ya da ikna becerisi.
- **Kalem sayısı düşük:** Mağaza kontrolü ve önerilen sipariş becerisi.
- **Kalem tutarı düşük:** Ürün karması ve bölge yapısı.

**Değerlendirmeyi kullanmak.** Performans etkenlerini bilmek, her temsilci için farklı bir gelişim planı yapmayı sağlar. Bilgi eksikliği olan bir temsilciye eğitim, motivasyon sorunu olan birine hedef ve ödül tasarımı, rol belirsizliği olan birine net öncelikler gerekir. Saha şefinin bu ayrımı ortak ziyaretlerde gözlemleyerek yapması, tek tip bir eğitim programından daha etkilidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Ziyaret sayısı, oranlar ve tutarlar varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b4.py` ile yapılmıştır.

İki temsilci aynı sayıda ziyaret yapıyor: ayda 176.

- Temsilci A: sipariş oranı %60, kalem 4, kalem tutarı 600 TL → **253.440 TL**
- Temsilci B: sipariş oranı %70, kalem 5, kalem tutarı 600 TL → **369.600 TL**

Aradaki fark ziyaret sayısından değil, sipariş oranı ve kalem sayısından geliyor. A'ya "daha fazla ziyaret yap" demek yanlış bir reçete olur. A için gelişim konusu, mağaza kontrolü ve önerilen sipariş hazırlamaktır. Sadece sipariş oranını %70'e çıkarsa satışı **295.680 TL** olur. Sadece kalem sayısını 5'e çıkarsa **316.800 TL** olur.

## Sık yapılan hatalar

- **Yalnızca toplam satışa bakmak.** Neden düşük olduğu görülmezse gelişim planı genel kalır.
- **Bölge farkını göz ardı etmek.** Potansiyeli düşük bir bölgedeki temsilci haksız yere zayıf görünür.
- **Kişisel özelliklere göre işe almak.** Araştırmalar bu özelliklerin performansla zayıf ilişkili olduğunu gösterir.
- **Rol netliğini ihmal etmek.** Temsilci önceliklerini bilmiyorsa her şeyi biraz yapar.

## Pratikte nasıl uygulanır?

- [ ] Her temsilcinin satışını dört çarpana ayırarak raporlayın.
- [ ] Benzer potansiyelli bölgeleri karşılaştırın; potansiyel farkını ayrı gösterin.
- [ ] Her temsilci için en zayıf çarpana odaklanan bir gelişim hedefi belirleyin.
- [ ] Rol beklentilerini, öncelikli ürünleri ve hedefleri yazılı ve kısa tutun.

## Daha fazlası

- Churchill, G. A.; Ford, N. M.; Hartley, S. W.; Walker, O. C. (1985). *The Determinants of Salesperson Performance: A Meta-Analysis.* Journal of Marketing Research 22(2), 103–118. https://doi.org/10.2307/3151357
- Verbeke, W.; Dietz, B.; Verwaal, E. (2011). *Drivers of Sales Performance: A Contemporary Meta-Analysis.* Journal of the Academy of Marketing Science 39(3), 407–428 (Crossref çevrimiçi yılı 2010). https://doi.org/10.1007/s11747-010-0211-8
