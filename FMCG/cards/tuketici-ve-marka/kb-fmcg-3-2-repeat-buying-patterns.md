---
id: kb-fmcg-3-2-repeat-buying-patterns
title: "Tekrar satın alma kalıpları: Penetrasyon, sıklık ve çifte risk"
summary: "Bir markanın satışı, kaç hanenin aldığı ile bu hanelerin ne sıklıkla aldığının çarpımıdır. Bu kart küçük markaların hem daha az alıcıya sahip olduğunu hem de bu alıcıların biraz daha seyrek aldığını anlatan çifte risk kalıbını ve büyüme hedefleri için sonucunu açıklar."
course: fmcg
category: tuketici-ve-marka
tags: [tuketici, pazar-payi, kpi, raporlama]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru]
level: ileri
source_lessons: [FMCG-3.2, FMCG-3.3]
reading_minutes: 3
key_points:
  - "Satış hacmi = hane sayısı × penetrasyon × alım sıklığı × alım başına miktar."
  - "Çifte risk: Küçük markaların hem daha az alıcısı vardır hem de bu alıcılar markayı biraz daha seyrek alır."
  - "Markalar arasındaki pazar payı farkı büyük ölçüde penetrasyon farkından gelir; sadakat farkları genellikle küçüktür."
  - "Büyüme hedefi koyarken penetrasyon ve sıklık hedeflerini ayrı ayrı yazın ve hangisinin gerçekçi olduğunu sorgulayın."
glossary_terms: [penetrasyon, alim-sikligi, cifte-risk]
related: [kb-fmcg-3-4-mental-physical-availability, kb-fmcg-3-5-brand-equity, kb-fmcg-3-8-market-research-toolkit, kb-fmcg-4-2-segmentation-positioning, kb-fmcg-12-6-case-brand-growth-plan]
sources:
  - title: "Repeat-Buying: Facts, Theory and Applications"
    authors: "Ehrenberg, A. S. C."
    year: 1988
    type: book
    verified: false
    note: "Kitap; künye kontrol edilmedi."
  - title: "The Dirichlet: A Comprehensive Model of Buying Behaviour"
    authors: "Goodhardt, G. J.; Ehrenberg, A. S. C.; Chatfield, C."
    year: 1984
    type: article
    doi: "10.2307/2981696"
    url: "https://doi.org/10.2307/2981696"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of the Royal Statistical Society A 147(5), 621–655."
  - title: "Double Jeopardy Revisited"
    authors: "Ehrenberg, A. S. C.; Goodhardt, G. J.; Barwise, T. P."
    year: 1990
    type: article
    doi: "10.1177/002224299005400307"
    url: "https://doi.org/10.1177/002224299005400307"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Marketing 54(3), 82–91."
  - title: "How Brands Grow: What Marketers Don't Know"
    authors: "Sharp, B."
    year: 2010
    type: book
    verified: false
    note: "Oxford University Press; künye kontrol edilmedi."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

"Sadık müşterilerimizi daha sık aldırarak büyüyeceğiz" hedefi kulağa makul gelir, ama tüketici paneli verileri çoğu zaman başka bir şey söyler. Bu kart, hızlı tüketimde tekrar satın almanın düzenli kalıplarını anlatır ve büyüme planı, marka hedefi ve panel raporu okurken hangi soruları sormanız gerektiğini gösterir.

## Temel fikir

**Satışın bileşenleri.** Bir markanın belirli bir dönemdeki satışı şöyle ayrıştırılır:

Satış = Hane sayısı × Penetrasyon × Alım sıklığı × Alım başına miktar

- **Penetrasyon:** Dönem içinde markayı en az bir kez alan hanelerin oranı.
- **Alım sıklığı:** Markayı alan hanelerin ortalama kaç kez aldığı.

**Düzenli kalıplar.** Ehrenberg (1988) ve Goodhardt, Ehrenberg ve Chatfield (1984), birçok kategoride tekrar satın alma davranışının şaşırtıcı derecede düzenli olduğunu ve bunun Dirichlet adı verilen istatistiksel bir modelle iyi tanımlanabildiğini gösterir. Modelin matematiğine girmeden ana sonuçlar şunlardır:

- Çoğu alıcı birden fazla marka alır. Tamamen tek markaya sadık alıcı azdır.
- Bir markanın alıcılarının büyük kısmı o markayı seyrek alır.
- Markaların pazar payı farkları en çok penetrasyondan kaynaklanır.

**Çifte risk** (*double jeopardy*): Ehrenberg, Goodhardt ve Barwise (1990), küçük markaların iki kez cezalandırıldığını gösterir: Hem daha az alıcıları vardır, hem de bu alıcılar markayı büyük markaların alıcılarına göre biraz daha seyrek alır. Yani küçük bir marka "az ama sadık müşteri" profiline nadiren sahiptir.

Sharp (2010) bu bulgulardan yola çıkarak büyümenin çoğunlukla penetrasyon artışıyla, yani daha fazla haneye ulaşarak geldiğini savunur. Bu görüş pazarlama çevrelerinde tartışılsa da büyüme planlarında penetrasyonun sorgulanması gerektiği konusunda güçlü bir uyarıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek bir panele ait değildir; hesaplar `scripts/cards_numbers_fmcg_b1.py` ile yapılmıştır.

10.000 hanelik bir panelde iki marka:

| Marka | Penetrasyon | Alıcı | Sıklık | Toplam alım |
|---|---|---|---|---|
| A | %40 | 4.000 | 3,0 | 12.000 |
| B | %10 | 1.000 | 2,4 | 2.400 |

İki marka arasında alım payı A için yaklaşık **%83,3**. Fark büyük ölçüde penetrasyondan geliyor (dört kat); sıklık farkı daha küçük (3,0'a karşı 2,4). Bu tablo çifte riskin tipik görüntüsüdür.

B markasının yönetimi %20 büyüme hedefliyor. Hesap olarak iki yol da aynı sonucu verir:

- Penetrasyonu %10'dan %12'ye çıkarmak: **2.880** alım
- Sıklığı 2,4'ten 2,88'e çıkarmak: **2.880** alım

Ama kalıplar, küçük bir markanın sıklığını büyük markaların seviyesine taşımanın zor olduğunu gösterir. Daha gerçekçi yol, B'yi daha fazla hanenin görmesi ve bulabilmesidir: dağıtım, görünürlük ve hatırlanırlık.

## Sık yapılan hatalar

- Büyüme hedefini yalnızca "sadakat" ya da "sıklık" üzerine kurmak.
- Küçük markanın düşük sıklığını özel bir sadakat sorunu sanmak; bu çoğu zaman markanın büyüklüğüyle tutarlı bir kalıptır.
- Panel raporlarında penetrasyon ve sıklığı ayrı okumadan yalnızca toplam hacme bakmak.
- Kısa dönemli bir promosyondan gelen penetrasyon artışını kalıcı büyüme sanmak.
- Çok kısa dönemlerle (bir ay) penetrasyon karşılaştırmak; seyrek alınan kategorilerde yıllık bakış gerekir.

## Pratikte nasıl uygulanır?

- [ ] Panel ya da sadakat kartı verinizden markalarınız için penetrasyon ve sıklığı ayrı ayrı çıkarın.
- [ ] Rakip markalarla birlikte bir tablo kurun ve çifte risk kalıbına uyup uymadığınıza bakın.
- [ ] Büyüme planında hedefi penetrasyon ve sıklık olarak ikiye ayırın; her biri için hangi faaliyetin işe yarayacağını yazın.
- [ ] Bayi ve satış ekibi için penetrasyonun saha karşılığını tanımlayın: dağıtım, raf görünürlüğü, yeni nokta açılışı.
- [ ] Promosyon sonrasında yeni alıcıların tekrar alıp almadığını ölçün.

## Daha fazlası

- Ehrenberg, A. S. C. (1988). *Repeat-Buying: Facts, Theory and Applications.* (kaynak doğrulanmadı)
- Goodhardt, G. J.; Ehrenberg, A. S. C.; Chatfield, C. (1984). *The Dirichlet: A Comprehensive Model of Buying Behaviour.* Journal of the Royal Statistical Society A 147(5), 621–655. https://doi.org/10.2307/2981696
- Ehrenberg, A. S. C.; Goodhardt, G. J.; Barwise, T. P. (1990). *Double Jeopardy Revisited.* Journal of Marketing 54(3), 82–91. https://doi.org/10.1177/002224299005400307
- Sharp, B. (2010). *How Brands Grow: What Marketers Don't Know.* (kaynak doğrulanmadı)
