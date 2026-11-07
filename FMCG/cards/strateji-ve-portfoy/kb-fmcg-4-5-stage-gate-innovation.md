---
id: kb-fmcg-4-5-stage-gate-innovation
title: "Aşama-kapı süreci: Yeni ürün fikirlerini erken elemek"
summary: "Yeni ürün projelerinin çoğu pazara ulaşmaz ya da pazarda tutunamaz. Aşama-kapı süreci, projeyi aşamalara böler ve her aşamanın sonunda devam ya da dur kararı verir. Bu kart süreci ve erken elemenin neden para kazandırdığını anlatır."
course: fmcg
category: strateji-ve-portfoy
tags: [strateji, portfoy, inovasyon]
roles: [uretici-sahibi, uretici-yonetici]
level: orta
source_lessons: [FMCG-4.5]
reading_minutes: 3
key_points:
  - "Aşama-kapı süreci, yeni ürün projesini aşamalara ve aralarındaki karar noktalarına (kapılara) böler."
  - "Her kapıda önceden belirlenmiş ölçütlerle devam, dur, bekle ya da yeniden çalış kararı verilir."
  - "Maliyetler ilerleyen aşamalarda hızla arttığı için zayıf projeleri erken durdurmak büyük tasarruf sağlar."
  - "Kapı toplantısı bir onay töreni değildir; dur kararı verilemiyorsa süreç işlemiyor demektir."
glossary_terms: [asama-kapi]
related: [kb-fmcg-4-4-portfolio-management, kb-fmcg-4-7-launch-forecasting, kb-fmcg-4-2-segmentation-positioning, kb-fmcg-2-4-roi-roce-npv, kb-fmcg-3-8-market-research-toolkit]
sources:
  - title: "Stage-Gate Systems: A New Tool for Managing New Products"
    authors: "Cooper, R. G."
    year: 1990
    type: article
    doi: "10.1016/0007-6813(90)90040-I"
    url: "https://doi.org/10.1016/0007-6813(90)90040-I"
    verified: true
    checked_on: 2026-10-28
    note: "Business Horizons 33(3), 44–54."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Yeni ürün fikirleri her zaman bütçeden fazladır. Bir fikri çok geç durdurmak, kalıp, ambalaj, reklam ve listeleme masraflarını boşa harcamak demektir. Bu kart, aşama-kapı sürecinin nasıl çalıştığını ve beklenen maliyeti nasıl düşürdüğünü gösterir.

## Temel fikir

Cooper (1990), aşama-kapı sistemini (*stage-gate*) yeni ürün geliştirmeyi yönetmek için bir yol haritası olarak tanımlar. Proje birbirini izleyen **aşamalara** bölünür. Her aşamada belirli işler yapılır ve bilgi toplanır. Aşamalar arasında **kapılar** vardır. Kapıda yönetim, önceden belirlenmiş ölçütlere göre karar verir.

Hızlı tüketimde tipik bir akış şöyledir:

1. **Fikir taraması:** Fikir, kategori stratejisine ve hedef segmente uyuyor mu?
2. **Konsept testi:** Tüketici konsepti anlıyor ve ilgi gösteriyor mu?
3. **Geliştirme:** Formül, ambalaj, maliyet ve üretim hazırlığı.
4. **Test pazarı ya da sınırlı lansman:** Gerçek raf koşullarında deneme ve tekrar alma.
5. **Tam lansman.**

**Kapı ölçütleri.** Kapılarda kullanılan tipik ölçütler: stratejik uyum, tüketici ilgisi, hedef maliyet ve marja ulaşılabilirlik, üretim ve tedarik fizibilitesi, beklenen hacim ve yatırım getirisi. Ölçütler toplantıdan önce yazılmalıdır.

**Neden erken elemek?** Aşamaların maliyeti genellikle ilerledikçe artar. Bir fikir taraması birkaç bin TL tutarken test pazarı milyonlar tutabilir. Zayıf projeyi ilk kapılarda durdurmak, pahalı aşamalara yalnızca umut vadeden projelerin girmesini sağlar.

**Süreci işletmek.** Aşama-kapı süreci, kapılarda karar verecek kişiler net olmadığında işlemez. Her kapıda pazarlama, satış, finans, ar-ge ve tedarik zinciri temsilcilerinden oluşan bir karar grubu ve önceden tanımlanmış ölçütler bulunmalıdır. Kapı kararları dört türden biri olabilir: devam, dur, bekle ya da ek çalışmayla tekrar gel. "Bekle" kararının çok sık verilmesi, portföyde kaynak tüketen ama ilerlemeyen projeler bırakır. Proje portföyü düzenli olarak bir bütün olarak gözden geçirilmeli; kaynakların en umut verici projelere ayrıldığından emin olunmalıdır. Lansman sonrası değerlendirme de sürecin son kapısı olarak görülmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Aşama maliyetleri ve geçiş olasılıkları varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b2.py` ile yapılmıştır.

| Aşama | Maliyet | Sonraki aşamaya geçme olasılığı |
|---|---|---|
| Fikir taraması | 50.000 TL | %50 |
| Konsept testi | 300.000 TL | %60 |
| Geliştirme | 1.200.000 TL | %70 |
| Test pazarı | 2.500.000 TL | %60 |

Bir projenin bütün kapılardan geçme olasılığı 0,5 × 0,6 × 0,7 × 0,6 = **%12,60**.

- Kapılar çalışıyorsa, her proje yalnızca geçtiği aşamaların maliyetini öder. Proje başına beklenen maliyet **1.085.000 TL**, başarılı ürün başına **8.611.111 TL**.
- Kapılar çalışmıyorsa ve her proje sonuna kadar gidiyorsa, proje başına maliyet **4.050.000 TL**, başarılı ürün başına **32.142.857 TL**.

Aynı sayıda başarılı ürün için kapısız süreç yaklaşık dört kat pahalıya geliyor.

## Sık yapılan hatalar

- **Her projeyi kapıdan geçirmek.** Dur kararı hiç çıkmıyorsa kapılar yalnızca bürokrasidir.
- **Ölçütleri toplantıda belirlemek.** Projeye duygusal olarak bağlanan ekip, ölçütleri esnetir.
- **Batık maliyete bakmak.** "Bu kadar harcadık, bırakamayız" yaklaşımı geçmişteki harcamayı geleceğin kararına katar.
- **Satış ve zincir bilgisini geç almak.** Listeleme koşulları ve raf gerçeği lansmandan çok önce bilinmelidir.

## Pratikte nasıl uygulanır?

- [ ] Kendi aşamalarınızı ve her kapının ölçütlerini yazılı hâle getirin.
- [ ] Her kapıya satış, finans ve tedarik zinciri temsilcilerini çağırın.
- [ ] Aşama maliyetlerinizi ve tarihsel geçiş oranlarınızı kaydedin; yukarıdaki hesabı kendi verinizle yapın.
- [ ] Dur kararlarını ve nedenlerini kaydedin; bunlar sürecin işlediğinin kanıtıdır.
- [ ] Küçük ve düşük riskli projeler için kısaltılmış bir yol tanımlayın; her ambalaj değişikliğini beş kapıdan geçirmek gereksiz yavaşlık yaratır.

## Daha fazlası

- Cooper, R. G. (1990). *Stage-Gate Systems: A New Tool for Managing New Products.* Business Horizons 33(3), 44–54. https://doi.org/10.1016/0007-6813(90)90040-I
