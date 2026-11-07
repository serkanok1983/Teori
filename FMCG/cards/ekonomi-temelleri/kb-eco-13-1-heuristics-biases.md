---
id: kb-eco-13-1-heuristics-biases
title: "Karar verirken düştüğümüz tuzaklar: çapalama, aşırı güven ve kayıptan kaçınma"
summary: "Yöneticilerin tahmin, bütçe, fiyat ve pazarlık kararlarında sık düştüğü düşünce hatalarını ve bunları azaltan basit karar alışkanlıklarını anlatır."
course: eco
category: ekonomi-temelleri
tags: [karar-verme, davranissal-ekonomi, planlama]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: temel
source_lessons: [ECO-13.1]
reading_minutes: 3
key_points:
  - "İnsanlar karmaşık kararlarda kısa yollar kullanır; bu kısa yollar sistematik hatalara yol açar."
  - "İlk duyulan rakam (çapa), sonraki tahmin ve pazarlıkları farkında olmadan etkiler."
  - "Yöneticiler tahminlerine genellikle olduğundan fazla güvenir ve proje sürelerini kısa tahmin eder."
  - "Kayıplar, aynı büyüklükteki kazançlardan daha çok acıtır; bu, zararlı kararlardan dönmeyi zorlaştırır."
  - "Hataları azaltmanın yolu iradeden çok süreçtir: dış referans, kontrol listesi, geçmiş tahmin kaydı."
glossary_terms: [capalama, kayiptan-kacinma, asiri-guven]
related: [kb-eco-1-1-opportunity-cost-sunk-cost, kb-fmcg-13-7-behavioural-economics-selling, kb-fmcg-13-14-negotiation-structure, kb-eco-31-10-scenario-sensitivity]
sources:
  - title: "Judgment under Uncertainty: Heuristics and Biases"
    authors: "Tversky, A.; Kahneman, D."
    year: 1974
    type: article
    doi: "10.1126/science.185.4157.1124"
    url: "https://doi.org/10.1126/science.185.4157.1124"
    verified: true
    checked_on: 2026-10-28
    note: "Science 185(4157)."
  - title: "Prospect Theory: An Analysis of Decision under Risk"
    authors: "Kahneman, D.; Tversky, A."
    year: 1979
    type: article
    doi: "10.2307/1914185"
    url: "https://doi.org/10.2307/1914185"
    verified: true
    checked_on: 2026-10-28
    note: "Econometrica 47(2)."
  - title: "Mental accounting matters"
    authors: "Thaler, R. H."
    year: 1999
    type: article
    doi: "10.1002/(SICI)1099-0771(199909)12:3<183::AID-BDM318>3.0.CO;2-F"
    url: "https://doi.org/10.1002/(SICI)1099-0771(199909)12:3<183::AID-BDM318>3.0.CO;2-F"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Behavioral Decision Making 12(3)."
  - title: "The psychology of sunk cost"
    authors: "Arkes, H. R.; Blumer, C."
    year: 1985
    type: article
    doi: "10.1016/0749-5978(85)90049-4"
    url: "https://doi.org/10.1016/0749-5978(85)90049-4"
    verified: true
    checked_on: 2026-10-28
    note: "Organizational Behavior and Human Decision Processes 35(1)."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Bütçe toplantısında ilk söylenen büyüme oranı, herkesin tahminini belirler. Yeni proje her seferinde planlanandan uzun sürer. Zarardaki ürün grubunu kapatmak bir türlü mümkün olmaz. Bu kart, bu tekrarlayan hataların arkasındaki düşünce kalıplarını ve bunlara karşı kullanabileceğiniz basit yöntemleri anlatır.

## Temel fikir

Tversky ve Kahneman (1974), insanların belirsizlik altında yargıda bulunurken birkaç kısa yola (sezgisel kural, *heuristic*) dayandığını ve bunun sistematik **yanılgılar** (*bias*) ürettiğini gösterdi. Yönetici için en önemlileri:

- **Çapalama** (*anchoring*): İlk duyulan rakam, sonraki tahminleri kendine doğru çeker. Pazarlıkta ilk teklif, bütçede geçen yılın rakamı ya da üst yöneticinin ilk söylediği hedef çapa olur.
- **Aşırı güven** (*overconfidence*): Tahminlerimizin isabetine olduğundan fazla güveniriz; tahmin aralıklarımız çok dardır. Bunun bir türü olan **planlama yanılgısı**, proje süre ve maliyetlerini sistematik olarak düşük tahmin etmektir.
- **Kayıptan kaçınma** (*loss aversion*): Kahneman ve Tversky (1979), kayıpların aynı büyüklükteki kazançlardan daha güçlü hissedildiğini gösterdi. Sonuç: Zarardaki kararı kabul etmek yerine devam ettirmek ve "zam" kelimesine karşı aşırı tepki.
- **Zihinsel hesap** (*mental accounting*): Thaler (1999), insanların parayı ayrı zihinsel hesaplara böldüğünü ve bunun aynı tutara farklı davranılmasına yol açtığını anlattı. Örneğin "promosyon bütçesinden" harcanan parayı daha rahat harcamak.
- **Doğrulama yanlılığı:** Mevcut kanaatimizi destekleyen veriyi arama ve ötekini görmezden gelme eğilimi.

## Bir örnek

> **Örnek (temsili rakamlar):** Bir satış direktörünün geçmiş tahmin kaydı varsayımsaldır; hesaplar `scripts/cards_numbers_eco_b2.py` ile yapılmıştır.

**Aşırı güven testi.** Direktör geçen yıl 10 kalem için (bölge satışları, yeni ürün hacmi, rakip fiyat artışı) "%90 eminim" dediği alt–üst aralıklar vermiş. Yıl sonunda gerçekleşenlerin yalnızca %60'ı aralıkların içinde kalmış. Aralıklar çok dar; doğru kalibrasyon için aralıkları genişletmek gerekir.

**Planlama yanılgısı.** Son beş iç projenin (yeni depo düzeni, el terminali, yeni bölge açılışı vb.) planlanan süresi ortalama 3,0 ay, gerçekleşen süresi ortalama 4,5 ay: **%50** aşım. Bir sonraki proje planına bu aşım oranını "dış referans" olarak eklemek, iyimser tahminden daha isabetli sonuç verir.

## Sık yapılan hatalar

- Bütçe toplantısını, üst yöneticinin hedefi söylemesiyle başlatmak.
- Pazarlıkta karşı tarafın ilk teklifini referans alıp oradan pazarlık etmek.
- Tahminleri tek bir rakam olarak vermek; belirsizlik aralığı göstermemek.
- Geçmiş tahminleri kaydetmemek; hiçbir zaman isabet ölçmemek.
- "Bu sefer farklı" diyerek benzer projelerin geçmiş sonuçlarını göz ardı etmek.
- Geçmişte iyi sonuç veren bir kararı, koşullar değişmiş olsa da tekrarlamak.
- Toplantılarda ilk konuşan kıdemli kişinin görüşüne çapalanmak.

## Pratikte nasıl uygulanır?

- [ ] Bütçe ve hedef toplantılarında önce herkesin tahminini ayrı ayrı yazılı olarak toplayın, sonra tartışın.
- [ ] Pazarlığa girmeden önce kendi hedef ve masadan kalkma noktanızı yazın; ilk teklifi mümkünse siz verin.
- [ ] Önemli tahminleri alt–üst aralıkla verin ve yıl sonunda isabeti ölçün.
- [ ] Proje planlarında benzer geçmiş projelerin gerçekleşen süre ve maliyetini referans alın.
- [ ] Büyük kararlarda bir kişiyi "karşı görüşü savunmakla" görevlendirin.
- [ ] Önemli kararlardan önce "bu karar başarısız olursa nedeni ne olur?" sorusunu ekipçe tartışın.
- [ ] Tahminlerinizi kaydedip gerçekleşmeyle düzenli olarak karşılaştırın.

## Daha fazlası

- Tversky, A.; Kahneman, D. (1974). *Judgment under Uncertainty: Heuristics and Biases*. https://doi.org/10.1126/science.185.4157.1124
- Kahneman, D.; Tversky, A. (1979). *Prospect Theory: An Analysis of Decision under Risk*. https://doi.org/10.2307/1914185
- Thaler, R. H. (1999). *Mental accounting matters*. https://doi.org/10.1002/(SICI)1099-0771(199909)12:3<183::AID-BDM318>3.0.CO;2-F
- Arkes, H. R.; Blumer, C. (1985). *The psychology of sunk cost*. https://doi.org/10.1016/0749-5978(85)90049-4
