---
id: kb-fmcg-1-3-channel-actors
title: "Kanal aktörleri: Üretici, bayi, toptancı ve perakendeci kim, ne iş yapar?"
summary: "Hızlı tüketim ürünleri rafa birkaç el değiştirerek ulaşır. Bu kart her aktörün üstlendiği kanal işlevlerini, aracının neden var olduğunu ve dikey ilişkilerde marj yığılmasının sonucunu sade bir dille anlatır."
course: fmcg
category: sektor-ve-kanal
tags: [bayi, geleneksel-kanal, zincir-market, dagitim]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: temel
source_lessons: [FMCG-1.3]
reading_minutes: 3
key_points:
  - "Kanal işlevleri (stok tutma, bölme, kredi, taşıma, satış, raf düzeni) ortadan kalkmaz; yalnızca kimin yapacağı değişir."
  - "Aracı, üretici ile binlerce satış noktası arasındaki temas sayısını azalttığı için vardır."
  - "Aracının marjı, üstlendiği işlevlerin karşılığıdır; işlevi almadan marjı kısmak hizmeti bozar."
  - "Bağımsız marjların yığılması raf fiyatını yükseltir; ticari şartlar bu dikey ilişkiyi yönetmek içindir."
glossary_terms: [kanal-islevleri, bayi, toptanci, cift-marjinallesme]
related: [kb-fmcg-1-1-margin-stack, kb-fmcg-1-4-channel-power-conflict, kb-fmcg-6-4-direct-vs-indirect, kb-fmcg-6-1-rtm-channels-formats, kb-fmcg-7-1-distributor-pnl]
sources:
  - title: "Marketing Channels"
    authors: "Coughlan, A. T.; Anderson, E.; Stern, L. W.; El-Ansary, A. I."
    year: 2006
    type: book
    verified: false
    note: "Kitap; baskı yılı kontrol edilmedi."
  - title: "Vertical Integration and Antitrust Policy"
    authors: "Spengler, J. J."
    year: 1950
    type: article
    doi: "10.1086/256964"
    url: "https://doi.org/10.1086/256964"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Political Economy 58(4), 347–352."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

"Bu bayi ne iş yapıyor ki bu marjı alıyor?" ya da "Üretici bizi aradan çıkarır mı?" soruları kanal işlevleri anlaşılmadan cevaplanamaz. Bu kart, üreticiden rafa uzanan zincirdeki her aktörün rolünü ve aldığı payın neyin karşılığı olduğunu açıklar. Bayi sözleşmesi, doğrudan dağıtım ya da marj pazarlığı öncesinde okunması faydalıdır.

## Temel fikir

**Aktörler.** Türkiye'de geleneksel kanalda tipik zincir şöyledir: **üretici (marka sahibi) → bayi / distribütör → bakkal, market, büfe → tüketici**. Bazı bölgelerde ve kategorilerde araya **toptancı** girer: Bayiden ya da üreticiden alıp küçük perakendeciye satar. Ulusal ve indirim zincirleri ise çoğu zaman üreticiden doğrudan alır.

**Kanal işlevleri.** Coughlan ve arkadaşlarının kanal yaklaşımına göre bir ürünün tüketiciye ulaşması için belirli işler mutlaka yapılmalıdır:

- Stok tutmak ve depolamak
- Büyük partileri küçük siparişlere bölmek
- Müşteriye vade, yani kredi vermek ve tahsilatı yapmak
- Taşımak ve teslim etmek
- Satış yapmak: ziyaret, sipariş alma, yeni ürün sunma
- Rafı düzenlemek ve satış noktası malzemesi kullanmak
- Bilgi toplamak: satış, stok ve rakip verisi

Bu işlevler ortadan kaldırılamaz. Bayiyi aradan çıkaran üretici, bu işleri kendisi yapmak ve maliyetine katlanmak zorundadır. Bayinin marjı da tam olarak bu işlevlerin karşılığıdır.

**Aracı neden var?** Üretici sayısı ile satış noktası sayısı büyüdükçe, herkesin herkesle doğrudan çalışması hem pahalı hem de dağınık hâle gelir. Aracı, temas sayısını toplamaya indirger. Ayrıca bölgeyi tanır, yerel krediyi yönetir ve birden fazla markayı aynı araçla taşıyarak maliyeti paylaştırır.

**Dikey ilişki ve marj yığılması.** Zincirdeki her halka bağımsız bir işletmedir ve kendi marjını korumak ister. Her biri kendi kârını en yükseğe çıkaran fiyatı seçtiğinde raf fiyatı yükselir ve toplam satış düşer. Spengler (1950) bunu çift marjinalleşme olarak tanımladı. Sade anlamıyla: Taraflar fiyatı birlikte düşünmezse herkes kaybedebilir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar bir bölgeyi temsil eden varsayımlardır; hesaplar `scripts/cards_numbers_fmcg_b1.py` ile yapılmıştır.

Bir ilçede 5 üretici ve 200 satış noktası olduğunu düşünün.

- **Herkes doğrudan çalışırsa:** Her üretici her noktaya ayrı ayrı gider. Temas sayısı 5 × 200 = **1.000**'dir. Her biri ayrı bir ziyaret, sipariş, fatura, teslimat ve tahsilat demektir.
- **Tek bir bayi üzerinden:** Üreticiler bayiyle, bayi noktalarla çalışır. Temas sayısı 5 + 200 = **205**'e iner.

Bayi aynı araçla beş markayı taşır, tek ziyarette beş markanın siparişini alır ve tek tahsilat yapar. Bu verimliliğin bir kısmı bayinin marjı olarak kalır, bir kısmı da üreticiye düşük dağıtım maliyeti olarak döner. Üreticinin "bayiyi aradan çıkarırsam marjı ben alırım" hesabı, 1.000 temasın maliyetini hesaba katmadığında yanıltıcıdır.

## Sık yapılan hatalar

- Bayi marjını "aracı payı" diye görüp karşılığındaki işlevleri (kredi, stok, teslimat) saymamak.
- Doğrudan dağıtıma geçerken bayinin taşıdığı alacak riskini ve stok finansmanını maliyete eklememek.
- Bayiden marj kısıp aynı hizmet seviyesini beklemek.
- Toptancıyı yalnızca fiyat bozan bir oyuncu olarak görmek; ulaşılması zor küçük noktalara hizmet ettiğini unutmak.
- Zincirdeki tarafların fiyatı ve hacmi birlikte planlamaması.

## Pratikte nasıl uygulanır?

- [ ] Kanalınızdaki her aktör için hangi işlevi kimin yaptığını gösteren basit bir tablo çıkarın.
- [ ] Bayi olarak üstlendiğiniz işlevleri (vade gün sayısı, stok gün sayısı, ziyaret sıklığı) rakamla ifade edin; marj görüşmesinde bunları kullanın.
- [ ] Üretici olarak bir işlevi geri almayı düşünüyorsanız önce o işlevin tam maliyetini hesaplayın.
- [ ] Toptancıların hangi noktalara hizmet ettiğini öğrenin; fiyat ve bölge kurallarını buna göre koyun.
- [ ] Satış müdürleri ve şefler için "bayi bize ne kazandırıyor" sorusunun cevabını tek sayfada toplayın.

## Daha fazlası

- Coughlan, A. T.; Anderson, E.; Stern, L. W.; El-Ansary, A. I. (2006). *Marketing Channels.* (kaynak doğrulanmadı)
- Spengler, J. J. (1950). *Vertical Integration and Antitrust Policy.* Journal of Political Economy 58(4), 347–352. https://doi.org/10.1086/256964
