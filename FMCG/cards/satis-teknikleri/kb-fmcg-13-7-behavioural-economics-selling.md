---
id: kb-fmcg-13-7-behavioural-economics-selling
title: "Satışta davranışsal ekonomi: Çapalama, çerçeveleme ve kayıptan kaçınma"
summary: "İnsanlar kararlarını her zaman tam rasyonel hesapla vermez; ilk duydukları rakam, seçeneklerin nasıl sunulduğu ve kayıp algısı kararı etkiler. Bu kart Tversky ve Kahneman'ın temel bulgularını, fiyat ve teklif sunumunda nasıl kullanılabileceğini ve sınırlarını anlatır."
course: fmcg
category: satis-teknikleri
tags: [satis-teknikleri, davranissal-ekonomi, fiyatlandirma]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, saha-satis-temsilcisi]
level: orta
source_lessons: [FMCG-13.7, ECO-13.2, ECO-13.3]
reading_minutes: 3
key_points:
  - "Çapalama: İlk duyulan rakam, sonraki tahminleri ve pazarlığı etkiler."
  - "Çerçeveleme: Aynı bilgi, kazanç ya da kayıp olarak sunulduğunda farklı kararlara yol açabilir."
  - "Kayıptan kaçınma: İnsanlar kayıpları, aynı büyüklükteki kazançlardan daha güçlü hisseder."
  - "Kullanılabilirlik ve temsil edicilik gibi kısayollar, alıcının risk algısını etkiler."
  - "Bu etkiler doğru bilgiyle kullanılmalıdır; müşteriyi yanıltmak için değil, anlaşılır kılmak için."
glossary_terms: [capalama, kayiptan-kacinma, ticari-harcama, birim-fiyat]
related: [kb-fmcg-13-6-persuasion-science, kb-fmcg-13-14-negotiation-structure, kb-fmcg-13-11-objections-closing-upsell, kb-fmcg-13-2-spin-solution-selling]
sources:
  - title: "Judgment under Uncertainty: Heuristics and Biases"
    authors: "Tversky, A.; Kahneman, D."
    year: 1974
    type: article
    doi: "10.1126/science.185.4157.1124"
    url: "https://doi.org/10.1126/science.185.4157.1124"
    verified: true
    checked_on: 2026-10-28
    note: "Science 185(4157), 1124–1131."
  - title: "The Framing of Decisions and the Psychology of Choice"
    authors: "Tversky, A.; Kahneman, D."
    year: 1981
    type: article
    doi: "10.1126/science.7455683"
    url: "https://doi.org/10.1126/science.7455683"
    verified: true
    checked_on: 2026-10-28
    note: "Science 211(4481), 453–458."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Bir temsilci "%10 indirim" yerine "10 alana 1 bedava" der; bir başkası "bu kampanyaya katılırsanız ayda 1.800 TL kazanırsınız" yerine "katılmazsanız ayda 1.800 TL kaybedersiniz" der. Rakamlar benzer görünür ama müşterinin tepkisi farklı olabilir. Bu kart, teklif sunumunun karar üzerindeki etkisini anlamanızı ve teklifinizi hem etkili hem dürüst biçimde sunmanızı sağlar.

## Temel fikir

**Belirsizlik altında yargı.** Tversky ve Kahneman'ın 1974'te *Science* dergisinde yayımlanan çalışması, insanların belirsizlik altında karar verirken kullandığı üç zihinsel kısayolu (*heuristic*) tanımlar:

- **Temsil edicilik:** Bir olayın olasılığı, tipik bir örneğe ne kadar benzediğine göre değerlendirilir.
- **Kullanılabilirlik:** Akla kolay gelen örnekler daha olası görünür. Bir alıcı, son başarısız lansmanı hatırlıyorsa yeni ürünü daha riskli görebilir.
- **Çapalama ve ayarlama** (*anchoring*): İnsanlar bir başlangıç değerinden yola çıkar ve genellikle yeterince uzaklaşmaz. Pazarlıkta ilk teklif bu nedenle önemlidir.

**Çerçeveleme.** Tversky ve Kahneman'ın 1981 tarihli çalışması, aynı seçeneklerin kazanç ya da kayıp olarak sunulmasının tercihleri değiştirebildiğini gösterir (*framing*). Bu, beklenti teorisinin (*prospect theory*) bir sonucudur: İnsanlar kayıplara karşı kazançlardan daha duyarlıdır (kayıptan kaçınma, *loss aversion*).

**Satışa uyarlama.**

- **Teklif sunumu:** Fiyatı ve faydayı müşterinin anlayacağı birimle sunun. "Kutu başına 2 TL" ile "yılda 24.000 TL" farklı algılanır.
- **Kayıp çerçevesi:** Stoksuzluk ya da kaçırılan kampanya, müşterinin kaybı olarak gösterildiğinde daha dikkat çekicidir. Ancak abartılmamalıdır.
- **Çapa:** Pazarlıkta ilk teklifi gerekçeli ve gerçekçi biçimde siz verin.
- **Bedava ürün ile indirim:** "Bedava" ifadesi güçlü bir çekiciliğe sahip olabilir, ama gerçek indirim oranını müşteriyle şeffaf biçimde paylaşın.

## Bir örnek

> **Örnek (temsili rakamlar):** Kampanya ve kayıp değerleri varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b8.py` ile yapılmıştır.

**Bedava ürün mü, indirim mi?** "10 alana 1 bedava" kampanyasında müşteri 11 ürün alır ama 10'unun parasını öder. Etkin indirim 1 ÷ 11 = yaklaşık **%9,09**'dur; yani "%10 indirimden" biraz daha düşüktür. Temsilci iki seçeneği sunarken bu oranı açıkça belirtir; müşteri, raf etkisi ve stok açısından hangisinin işine geldiğine karar verir.

**Kayıp çerçevesi.** Bir market, bölgesel kampanyaya katılmazsa, benzer marketlerin sonuçlarına göre ayda yaklaşık **1.800 TL**, yılda **21.600 TL** ek kârı kaçıracaktır. Temsilci bunu "kaybedeceğiniz kâr" olarak sunar, ama rakamın dayandığı karşılaştırmayı da gösterir.

## Sık yapılan hatalar

- **Çerçeveleme ile yanıltmak.** Gerçek rakamlar gizlenirse güven kaybolur.
- **Gerçekçi olmayan bir çapa.** Aşırı yüksek ilk teklif, görüşmeyi koparabilir.
- **Bütün müşterilere aynı çerçeveyi kullanmak.** Deneyimli alıcılar etkiyi fark eder.
- **Kendi önyargılarınızı görmemek.** Satış ekipleri de çapalama ve kullanılabilirlik etkisine açıktır; örneğin geçen yılın hedefini çapa almak.

## Pratikte nasıl uygulanır?

- [ ] Teklifin faydasını müşterinin anlayacağı birimle hesaplayın.
- [ ] Kampanya seçeneklerinin etkin indirim oranlarını açıkça gösterin.
- [ ] Stoksuzluk ya da kaçırılan fırsatı kayıp olarak, ama kanıtla sunun.
- [ ] Pazarlıkta gerekçeli bir ilk teklif hazırlayın.
- [ ] Kendi tahmin ve hedeflerinizde de çapa etkisini sorgulayın.

## Daha fazlası

- Tversky, A.; Kahneman, D. (1974). *Judgment under Uncertainty: Heuristics and Biases.* Science 185(4157), 1124–1131. https://doi.org/10.1126/science.185.4157.1124
- Tversky, A.; Kahneman, D. (1981). *The Framing of Decisions and the Psychology of Choice.* Science 211(4481), 453–458. https://doi.org/10.1126/science.7455683
