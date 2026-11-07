---
id: kb-fmcg-8-4-sales-force-sizing
title: "Satış ekibinin büyüklüğü: Bir temsilci daha eklemeli misiniz?"
summary: "Satış ekibi büyüklüğü iş yükü hesabıyla başlar, ama asıl soru ek bir temsilcinin maliyetini karşılayacak ek katkı yaratıp yaratmadığıdır. Bu kart iş yükü yaklaşımını, marjinal katkı yaklaşımını ve satış tepki eğrisi fikrini anlatır."
course: fmcg
category: saha-satis-ekibi
tags: [saha-satis, pazara-giris, analitik]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: orta
source_lessons: [FMCG-8.4]
reading_minutes: 3
key_points:
  - "İş yükü yaklaşımı, nokta sayısı ve ziyaret sıklığından gereken temsilci sayısını hesaplar."
  - "Marjinal yaklaşım, ek temsilcinin yaratacağı ek katkıyı maliyetiyle karşılaştırır."
  - "Satış ekibi harcamasının satışa etkisi azalan getirilidir; bir noktadan sonra ek temsilci kâr getirmez."
  - "Ek temsilci, potansiyeli yüksek bölgeye eklendiğinde kârlı olabilirken düşük potansiyelli bölgede zarar yaratabilir."
glossary_terms: [ziyaret-sikligi, nokta-evreni, katki-payi]
related: [kb-fmcg-6-1-rtm-channels-formats, kb-fmcg-8-5-territory-routing, kb-fmcg-8-6-sales-org-span-of-control, kb-fmcg-8-1-selling-formats, kb-fmcg-6-2-outlet-universe-segmentation]
sources:
  - title: "Building a Winning Sales Force"
    authors: "Zoltners, A. A.; Sinha, P.; Lorimer, S. E."
    year: 2009
    type: book
    verified: false
    note: "Kitap; künye kontrol edilmedi."
  - title: "Personal Selling Elasticities: A Meta-Analysis"
    authors: "Albers, S.; Mantrala, M. K.; Sridhar, S."
    year: 2010
    type: article
    doi: "10.1509/jmkr.47.5.840"
    url: "https://doi.org/10.1509/jmkr.47.5.840"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Marketing Research 47(5), 840–853."
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

"Daha fazla temsilci, daha fazla satış" düşüncesi kısmen doğrudur. Ama her ek temsilci maaş, araç ve yönetim maliyeti getirir. Bu kart, ekip büyüklüğüne iki farklı yönden bakmanızı ve ek temsilci kararını katkı üzerinden vermenizi sağlar.

## Temel fikir

**İş yükü yaklaşımı.** Toplam ziyaret ihtiyacı = her segmentteki nokta sayısı × ziyaret sıklığı. Bunu bir temsilcinin aylık ziyaret kapasitesine bölünce gereken temsilci sayısı çıkar. Bu yöntem basit ve anlaşılırdır. Ama ziyaret sıklığının doğru olduğunu varsayar; sıklığın getirisini sorgulamaz.

**Satış tepki eğrisi.** Satış ekibi çabası arttıkça satış da artar, ama artış giderek azalır. Lodish (1971), temsilcilerin zamanını müşteriler arasında bu tür tepki eğrilerine göre dağıtan bir karar destek modeli geliştirdi. Albers ve arkadaşlarının (2010) meta-analizi, kişisel satış çabasının satışa etkisini ölçen çalışmaları bir araya getirerek bu etkinin anlamlı ama sınırlı olduğunu ortaya koydu.

**Marjinal yaklaşım.** Zoltners, Sinha ve Lorimer, ekip büyüklüğünü belirlerken ek temsilcinin yaratacağı ek satıştan elde edilecek katkıyı, temsilcinin toplam maliyetiyle karşılaştırmayı önerir. Ek katkı maliyetten büyükse temsilci eklenir. Ayrıca etkinin hemen değil zamanla geldiğini hesaba katmak gerekir.

**Nereye eklendiği önemli.** Ek temsilcinin getirisi, ekleneceği bölgenin karşılanmamış potansiyeline bağlıdır. Aynı karar bir bölgede kârlı, başka bir bölgede zararlı olabilir.

**Karardan önce kontrol edilecekler.** Ekibe temsilci eklemeden önce mevcut kapasitenin verimli kullanıldığından emin olun. Rota planlaması iyileştirilebilir mi? Düşük potansiyelli noktalar telefonla ya da toptancı üzerinden hizmet alabilir mi? Temsilcilerin idari iş yükü azaltılabilir mi? Bu adımlar, yeni bir temsilcinin maliyetinden daha ucuz olabilir. Ek temsilci kararı verilirse, işe alımdan tam verime ulaşana kadar geçen süre hesaba katılmalıdır; yeni temsilcinin ilk aylarda tam performans göstermesi beklenmez. Kararın sonucu, eklenen bölgedeki satış ve kapsama değişikliğiyle bir yıl boyunca izlenmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Ek satış tahminleri, katkı payı ve maliyet varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b4.py` ile yapılmıştır.

Bir temsilcinin toplam yıllık maliyeti 540.000 TL. Katkı payı %30.

- **B bölgesi:** Ek temsilcinin yıllık 800.000 TL ek satış getirmesi bekleniyor. Ek katkı 240.000 TL. Maliyetle fark: **−300.000 TL**.
- **A bölgesi:** Nokta evreninin önemli kısmına hiç gidilmiyor. Ek temsilcinin yıllık 2.200.000 TL ek satış getirmesi bekleniyor. Ek katkı 660.000 TL. Fark: **+120.000 TL**.

İş yükü hesabı iki bölgede de bir temsilci açığı gösterebilir. Marjinal hesap ise yalnızca A bölgesinde eklemenin kârlı olduğunu söylüyor. B bölgesinde ziyaret sıklığını gözden geçirmek ya da telefonla satışı denemek daha doğru olabilir.

## Sık yapılan hatalar

- **Yalnızca iş yükü hesabı yapmak.** Ziyaret sıklığı gereğinden yüksekse ekip de gereğinden büyük çıkar.
- **Ek satışı iyimser tahmin etmek.** Tahmini bir pilot bölgeyle ya da benzer bölgelerle doğrulayın.
- **Etkinin gecikmesini unutmak.** Yeni temsilci ilk aylarda tam verimle çalışmaz.
- **Bütün bölgelere eşit ekleme yapmak.** Potansiyel farklıysa getiri de farklıdır.

## Pratikte nasıl uygulanır?

- [ ] Önce iş yükü yaklaşımıyla mevcut ihtiyacı hesaplayın.
- [ ] Her bölgenin karşılanmamış potansiyelini nokta evreni verisiyle tahmin edin.
- [ ] Ek temsilci için ek satış ve katkıyı, gecikmeyi de hesaba katarak tahmin edin.
- [ ] Mümkünse bir bölgede pilot yapın ve sonucu kontrol bölgesiyle karşılaştırın.
- [ ] Kararı yılda bir, bütçe döneminde yeniden değerlendirin.

## Daha fazlası

- Zoltners, A. A.; Sinha, P.; Lorimer, S. E. (2009). *Building a Winning Sales Force.* (kaynak doğrulanmadı)
- Albers, S.; Mantrala, M. K.; Sridhar, S. (2010). *Personal Selling Elasticities: A Meta-Analysis.* Journal of Marketing Research 47(5), 840–853. https://doi.org/10.1509/jmkr.47.5.840
- Lodish, L. M. (1971). *CALLPLAN: An Interactive Salesman's Call Planning System.* Management Science 18(4-II), P25–P40. https://doi.org/10.1287/mnsc.18.4.P25
