---
id: kb-ea-30-1-warehouse-operations-kpis
title: "Depo operasyonları ve temel performans göstergeleri"
summary: "Bir dağıtım deposunda mal kabul, yerleştirme, toplama, sevkiyat ve sayım akışını; toplama doğruluğu, zamanında sevk ve verimlilik gibi temel göstergelerin nasıl tanımlanıp sistemden ölçüleceğini anlatır."
course: ea
category: tedarik-ve-depo-sistemleri
tags: [depo, kpi, toplama, sevkiyat, verimlilik]
roles: [bayi-sahibi, bayi-yonetici, depo-lojistik-muduru]
level: temel
source_lessons: [EA-30.1]
reading_minutes: 2
key_points:
  - "Depo akışı mal kabul, yerleştirme, ikmal, toplama, paketleme, sevkiyat ve sayım adımlarından oluşur."
  - "Toplama doğruluğu, hatasız toplanan satırların toplam satırlara oranıdır."
  - "Zamanında sevk, söz verilen zamanda yola çıkan siparişlerin oranıdır."
  - "Verimlilik genellikle saat başına toplanan satır veya koli ile ölçülür."
  - "Göstergelerin tanımı yazılı olmalı ve aynı veriden hesaplanmalıdır."
glossary_terms: [toplama-dogrulugu, zamaninda-sevk]
related: [kb-ea-30-2-slotting-picking, kb-ea-30-3-wms-what-it-does, kb-ea-20-5-inventory-in-erp, kb-ea-29-3-drp-inventory-planning]
sources:
  - title: "Warehouse Management"
    authors: "Richards, G."
    year: 2021
    type: book
    verified: false
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Depo, dağıtım işinin en çok el emeği isteyen yeridir. Hatalı toplanan bir sipariş iade, ek sevkiyat ve müşteri şikâyeti demektir. Bu kart, depo akışını ve yönetimin izlemesi gereken temel göstergeleri anlatır.

## Temel fikir

**Depo akışı:**

1. **Mal kabul:** Gelen malın irsaliye ve siparişle karşılaştırılması.
2. **Yerleştirme:** Malın raf veya palet lokasyonuna konması.
3. **İkmal:** Toplama lokasyonlarının yedek stoktan doldurulması.
4. **Toplama:** Sipariş satırlarının raftan alınması.
5. **Paketleme ve kontrol.**
6. **Sevkiyat:** Araca yükleme ve irsaliye.
7. **Sayım:** Dönemsel veya dönüşümlü (cycle count) sayım.

**Temel göstergeler:**

- **Toplama doğruluğu:** Hatasız satır / toplam satır.
- **Zamanında sevk:** Zamanında çıkan sipariş / toplam sipariş.
- **Verimlilik:** Saat başına toplanan satır (veya koli).
- **Stok doğruluğu:** Sistemle sayımı tutan lokasyon oranı.
- **Mal kabul süresi:** Araç gelişinden stoğun satılabilir olmasına kadar geçen süre.

Richards, depo performansını ölçerken maliyet, hız ve kalite göstergelerinin birlikte izlenmesini önerir; yalnızca hıza bakmak hatayı artırabilir.

### Göstergeleri doğru kurmak

Bir göstergenin yararlı olması için yalnızca formülü değil, ölçüm kuralı da net olmalıdır. Aşağıdaki konular yazılı hâle getirilmezse farklı vardiyalar ve depolar aynı göstergeyi farklı hesaplar:

- **Hata tanımı:** Yanlış ürün, eksik miktar, fazla miktar ve hasarlı ürün ayrı ayrı mı sayılacak? Müşteri şikâyetiyle öğrenilen hatalar mı, sevkiyat öncesi kontrolde yakalananlar mı esas alınacak?
- **Zamanında sevk tanımı:** Söz verilen zaman siparişin alındığı anda mı belirleniyor, yoksa sevk planında mı? Müşterinin isteğiyle ertelenen siparişler nasıl sayılacak?
- **Verimlilik birimi:** Satır, koli ve palet farklı iş yüklerini temsil eder. Koli bazlı ve parça bazlı toplamanın aynı göstergeyle karşılaştırılması yanıltıcıdır.

**Göstergeleri dengelemek.** Hız, doğruluk ve maliyet birbirini etkiler. Yalnızca verimliliğe prim veren bir depoda hata oranının yükselmesi şaşırtıcı değildir. Bu yüzden göstergeler bir arada, aynı panoda izlenmeli ve hedefler birlikte belirlenmelidir.

**Kök neden analizi.** Hata oranı yükseldiğinde ilk soru "kim yaptı?" değil, "neden oldu?" olmalıdır. Benzer ambalajlı ürünlerin yan yana durması, okunmayan etiketler ve yoğun saatlerde yetersiz personel, çoğu toplama hatasının arkasındaki gerçek nedenlerdir.

### Göstergelerin paylaşılması

Göstergeler, vardiya başında ekiplerle kısa toplantılarda paylaşılmalıdır. Ekipler kendi sonuçlarını gördüğünde iyileştirme önerileri de gelir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b7.py` ile yapılmıştır.

Bir depoda bir haftada 5.000 satır toplanıyor; 40 satırda hata çıkıyor. Toplama doğruluğu **%99,2**. 1.200 siparişin 1.128'i zamanında sevk ediliyor: **%94,0**. Toplamda 320 işçilik saati harcanmış; verimlilik saat başına **15,6** satır. Yönetim üç göstergeyi aynı panoda izliyor.

## Sık yapılan hatalar

- Göstergeleri farklı kaynaklardan, farklı tanımlarla hesaplamak.
- Yalnızca verimliliği ödüllendirip doğruluğu ihmal etmek.
- Hataları müşteri şikâyetiyle öğrenmek.
- Sayımı yılda bir kez yapmak.
- Hata tanımını yazmadan vardiyaları birbiriyle kıyaslamak.
- Koli ve parça toplamayı aynı verimlilik göstergesiyle ölçmek.
- Hata arttığında kök neden yerine suçlu aramak.

## Pratikte nasıl uygulanır?

- [ ] Beş temel göstergeyi ve formüllerini yazılı tanımlayın.
- [ ] Verileri ERP veya depo sisteminden otomatik çekin.
- [ ] Haftalık depo panosu oluşturun.
- [ ] Dönüşümlü sayım takvimi kurun.

## Daha fazlası

- Richards, *Warehouse Management* (kitap; doğrulanmadı).
