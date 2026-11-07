---
id: kb-eco-42-1-tax-basics-average-marginal
title: "Vergi temelleri: Ortalama ve marjinal vergi oranı"
summary: "Artan oranlı vergi tarifesinde ortalama ve marjinal oran arasındaki farkı, ek gelirin ve primlerin net etkisinin nasıl hesaplanacağını ve sık yapılan 'üst dilime geçince her şeyim vergilenir' yanılgısını anlatır."
course: eco
category: vergi-ve-mevzuat
tags: [vergi, gelir-vergisi, ucret]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: temel
source_lessons: [ECO-42.1]
reading_minutes: 3
key_points:
  - "Artan oranlı tarifede her oran yalnızca kendi dilimindeki gelire uygulanır."
  - "Ortalama oran = toplam vergi ÷ toplam gelir; marjinal oran = son 1 TL'ye uygulanan oran."
  - "Ek gelir, prim ve zam kararlarında marjinal orana bakılır."
  - "Üst dilime geçmek, önceki dilimlerdeki gelirin vergisini artırmaz."
glossary_terms: [marjinal-vergi-orani, ortalama-vergi-orani, artan-oranli-tarife]
related: [kb-eco-43-1-turkish-tax-system-overview, kb-eco-43-2-income-tax-withholding, kb-eco-9-2-minimum-wage-labour-costs, kb-eco-44-3-sgk-employer-costs, kb-eco-1-5-price-controls-tax-incidence]
sources:
  - title: "193 sayılı Gelir Vergisi Kanunu"
    authors: "T.C. Resmî Gazete / Mevzuat Bilgi Sistemi"
    year: 1960
    type: law
    url: "https://www.mevzuat.gov.tr/MevzuatMetin/1.4.193.pdf"
    verified: true
    checked_on: 2026-10-28
    note: "Mevzuat Bilgi Sistemi resmî PDF metni açıldı, kanun adı ve numarası eşleşti (2026-10-28)."
  - title: "Hazine ve Maliye Bakanlığı (resmî site)"
    authors: "T.C. Hazine ve Maliye Bakanlığı"
    year: 2026
    type: web
    url: "https://www.hmb.gov.tr"
    verified: true
    checked_on: 2026-10-28
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Prim, zam veya ek iş kararlarında "Bunun ne kadarı vergiye gidecek?" sorusu hep gündemdedir. Bu kart, ortalama ve marjinal vergi oranını ayırt etmenizi ve ek gelirin net etkisini doğru hesaplamanızı sağlar. Türkiye'de gelir vergisi artan oranlı bir tarifeyle alınır; dilim sınırları ve oranlar her yıl değişebilir.

## Temel fikir

**Artan oranlı tarife:** Gelir dilimlere ayrılır, her dilime ayrı oran uygulanır. Yüksek oran yalnızca o dilimi aşan tutara uygulanır.

- **Ortalama vergi oranı** = Toplam vergi ÷ Toplam gelir.
- **Marjinal vergi oranı** = Bir sonraki 1 TL gelire uygulanacak oran.

Ek gelirin net etkisini marjinal oran belirler. Toplam vergi yükünü ise ortalama oran gösterir.

### Türkiye'de nerede karşınıza çıkar?

- **Ücretler:** Ücretlerden alınan gelir vergisi artan oranlı tarifeye göre hesaplanır ve vergi matrahı yıl içinde kümülatif olarak hesaplanır. Bu nedenle aynı brüt ücreti alan bir çalışanın net ücreti yılın sonraki aylarında, matrah üst dilimlere geçtikçe düşebilir. Bu durum, ücret pazarlıklarında ve bordro maliyetinde dikkate alınmalıdır.
- **Şahıs işletmeleri:** Şahıs işletmesi sahipleri ticari kazançları için artan oranlı tarifeye tabidir. Kazanç arttıkça şirketleşmenin vergi açısından avantajlı olup olmadığı sorusu gündeme gelir. Bu karar yalnızca orana göre değil, kâr dağıtımında alınan vergi, muhasebe maliyetleri ve sorumluluk yapısına göre verilmelidir.
- **Kurumlar vergisi:** Genel olarak tek oranlıdır; bu durumda ortalama ve marjinal oran büyük ölçüde örtüşür. Ancak istisna ve indirimler efektif oranı kanuni oranın altına çekebilir.

### Karar için kullanmak

Ek bir çalışma, prim veya gelir kalemi değerlendirilirken net etkiyi marjinal oranla hesaplayın. Toplam vergi yükünü veya sektörel karşılaştırmayı ise ortalama oranla yapın. Tarife dilimleri her yıl güncellendiğinden hesaplarda geçerli yılın tarifesini kullanın.

## Bir örnek

> **Örnek (temsili rakamlar):** Dilimler ve oranlar **örnek oran**dır, güncel tarife değildir. Hesaplar `scripts/cards_numbers_eco_b6.py` ile yapılmıştır.

Örnek tarife: 100.000 TL'ye kadar %15, 250.000 TL'ye kadar %20, 600.000 TL'ye kadar %27, üstü %35.

Yıllık 400.000 TL matrah için vergi:

- İlk dilim: 15.000 TL
- İkinci dilim: 30.000 TL
- Üçüncü dilimdeki kısım: 40.500 TL
- **Toplam: 85.500 TL.** Ortalama oran %21,4, marjinal oran %27.

Bu kişiye 50.000 TL prim verilirse ek vergi 13.500 TL, net ele geçen 36.500 TL olur. Primin vergisini ortalama oranla hesaplamak, net tutarı olduğundan yüksek gösterir.

## Sık yapılan hatalar

- Üst dilime geçince bütün gelirin yüksek oranla vergilendiğini sanmak.
- Ek gelirin net etkisini ortalama oranla hesaplamak.
- Ücretlerde yıl içinde kümülatif matrah arttıkça net maaşın düşebileceğini çalışanlara önceden anlatmamak.
- Geçen yılın dilimlerini bu yılın planlamasında kullanmak.
- Vergi oranını, sosyal güvenlik primleri gibi diğer kesintilerle karıştırmak.

## Pratikte nasıl uygulanır?

- [ ] Her yıl başında güncel tarifeyi resmî kaynaktan (Gelir İdaresi, Resmî Gazete) alın.
- [ ] Prim ve zam tekliflerinde marjinal orana göre net tutarı hesaplayın.
- [ ] Bordro planlamasında yıl içi dilim geçişlerini önceden gösterin.
- [ ] Net ücret garantili sözleşmelerde işveren maliyetinin dilim geçişiyle artacağını bütçeye yansıtın.
- [ ] Bordro ve vergi hesaplarını mali müşavirinize doğrulatın.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın.

## Daha fazlası

- T.C. Resmî Gazete / Mevzuat Bilgi Sistemi (1960). *193 sayılı Gelir Vergisi Kanunu*. https://www.mevzuat.gov.tr/MevzuatMetin/1.4.193.pdf
- T.C. Hazine ve Maliye Bakanlığı (2026). *Hazine ve Maliye Bakanlığı (resmî site)*. https://www.hmb.gov.tr
