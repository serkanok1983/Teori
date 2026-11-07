---
id: kb-eco-47-3-sampling-confidence
title: "Örneklem ve güven aralığı: Bir anketten ne kadar emin olabilirsiniz?"
summary: "Saha anketleri ve mağaza denetimleri gibi örneklem verilerinden yapılan tahminlerin hata payını, güven aralığının nasıl hesaplanıp yorumlanacağını ve gereken örneklem büyüklüğünü anlatır."
course: eco
category: veri-ve-istatistik
tags: [istatistik, orneklem, saha-arastirmasi]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: orta
source_lessons: [ECO-47.3]
reading_minutes: 2
key_points:
  - "Örneklemden elde edilen oran, gerçek değerin bir tahminidir ve hata payı taşır."
  - "%95 güven aralığı yaklaşık olarak tahmin ± 1,96 × standart hatadır."
  - "Hata payını yarıya indirmek için örneklemi yaklaşık dört katına çıkarmak gerekir."
  - "Örneklemin rastgele ve temsil edici olması, büyüklüğünden daha önemlidir."
glossary_terms: [orneklem, guven-araligi, standart-hata, hata-payi]
related: [kb-eco-47-1-descriptive-statistics, kb-eco-47-4-ab-testing-significance, kb-eco-48-7-test-vs-control-did]
sources:
  - title: "Introductory Statistics 2e"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/introductory-statistics-2e/pages/1-introduction"
    verified: true
    checked_on: 2026-10-28
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Saha ekipleri bayilerin bir kısmını ziyaret eder, raf denetimleri bazı mağazalarda yapılır, müşteri anketleri sınırlı sayıda kişiye uygulanır. Bu kart, bu tür verilerden çıkan bir oranın ne kadar güvenilir olduğunu ve kaç gözleme ihtiyacınız olduğunu hesaplamanızı sağlar.

## Temel fikir

**Örneklem:** Bütün kitlenin (ör. tüm bayiler) bir alt kümesi.

**Standart hata:** Örneklem tahmininin, tekrarlanan örneklemlerde ne kadar değişeceğinin ölçüsü. Bir oran için:

**SH = √(p × (1 − p) ÷ n)**

**%95 güven aralığı:** p ± 1,96 × SH. Yaklaşık yorumu: Bu yöntemle yapılan tahminlerin %95'i gerçek değeri kapsar.

**Gereken örneklem büyüklüğü:** n ≈ 1,96² × p × (1 − p) ÷ (istenen hata payı)².

**Temsil edicilik:** Yalnızca kolay ulaşılan veya büyük bayileri ziyaret etmek, örneklem ne kadar büyük olursa olsun yanlı sonuç verir.

### Örneklemi nasıl seçersiniz?

- **Basit rastgele örneklem:** Bütün bayi listesinden rastgele seçim. Excel'de rastgele sayı sütunu ekleyip sıralamak yeterlidir.
- **Tabakalı örneklem:** Bayileri bölge veya ciro grubuna ayırıp her gruptan ayrı seçim yapmak. Küçük ama önemli grupların örneklemde yeterince yer almasını sağlar.
- **Küme örneklemi:** Birkaç ilçeyi seçip oradaki bütün noktaları ziyaret etmek. Saha maliyetini düşürür, ama ilçeler birbirinden farklıysa hata payını büyütür.

### Sonuçları nasıl okursunuz?

Güven aralığı, tahminin ne kadar kesin olduğunu gösterir. İki bölgenin oranları farklı görünse bile aralıklar büyük ölçüde örtüşüyorsa farkın gerçek olduğundan emin olamazsınız. Hata payı örneklem büyüklüğünün kareköküyle azalır: Hata payını yarıya indirmek için örneklemi yaklaşık dört katına çıkarmanız gerekir. Bu yüzden önce kararınız için ne kadar kesinliğe ihtiyacınız olduğunu belirleyin, sonra saha bütçesini planlayın. Yanıt vermeyen bayiler de bir yanlılık kaynağıdır; yanıt oranını mutlaka raporlayın.

## Bir örnek

> **Örnek (temsili rakamlar):** Denetim sonuçları varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b7.py` ile yapılmıştır.

Bir üretici, rastgele seçilen 400 bakkalda rafta stok yokluğu oranını %30 olarak ölçüyor.

- Standart hata: yaklaşık 2,29 puan.
- Hata payı: ± 4,5 puan.
- **%95 güven aralığı: %25,5 ile %34,5 arası.**

Yönetim hata payının ± 3 puan olmasını istiyorsa yaklaşık 897 bakkal denetlenmelidir. Bir sonraki dönem oran birkaç puan düşük çıkarsa, bu düşüş hata payı içinde kaldığı sürece "iyileşme" olarak yorumlanmamalıdır.

## Sık yapılan hatalar

- Örneklem oranını kesin değer gibi raporlamak.
- Hata payı içindeki değişimleri gerçek iyileşme veya kötüleşme sanmak.
- Kolay ulaşılan noktaları seçip örneklemi yanlı hâle getirmek.
- Alt gruplara (ör. bölge bazında) bölünce örneklemin ne kadar küçüldüğünü göz ardı etmek.
- Yalnızca anketi yanıtlayan bayilerin sonuçlarını bütün bayilere genellemek.
- Alt grupları (bölge, kanal) ayrı ayrı yorumlarken her alt grubun küçük örneklemini ve geniş güven aralığını unutmak.

## Pratikte nasıl uygulanır?

- [ ] Denetim ve anket raporlarına güven aralığını ekleyin.
- [ ] Örneklemi rastgele ve bölge, kanal, büyüklük gibi katmanlara göre seçin.
- [ ] İstediğiniz hata payına göre örneklem büyüklüğünü önceden hesaplayın.
- [ ] Dönemler arası karşılaştırmada farkın hata payını aşıp aşmadığını kontrol edin.
- [ ] Saha çalışmasından önce hedef hata payını ve gereken örneklem büyüklüğünü yazın.
- [ ] Sonuçlarla birlikte yanıt oranını ve güven aralığını raporlayın.

## Daha fazlası

- OpenStax (2026). *Introductory Statistics 2e*. https://openstax.org/books/introductory-statistics-2e/pages/1-introduction
