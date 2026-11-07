---
id: kb-eco-7-7-oligopoly-collusion
title: "Az sayıda rakibin olduğu pazarlar: Oligopol, fiyat savaşı ve yasak anlaşmalar"
summary: "Az sayıda büyük oyuncunun olduğu pazarlarda fiyat ve miktar kararlarının birbirini nasıl etkilediğini, anlaşmanın neden hem yasak hem de kırılgan olduğunu ve fiyat savaşından kaçınmanın meşru yollarını anlatır."
course: eco
category: ekonomi-temelleri
tags: [rekabet, strateji, fiyatlama, uyum]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru]
level: ileri
source_lessons: [ECO-7.6, ECO-7.7]
reading_minutes: 3
key_points:
  - "Az sayıda rakibin olduğu pazarda her firmanın kararı rakiplerin fiyatını ve kârını doğrudan etkiler."
  - "Rakiplerin fiyat, miktar, bölge ya da müşteri paylaşımı konusunda anlaşması 4054 sayılı Kanun'a göre yasaktır."
  - "Yasak anlaşmalar ekonomik olarak da kırılgandır: Her katılımcının anlaşmayı bozmak için güçlü bir nedeni vardır."
  - "Ürünleri benzer ve kapasitesi bol olan firmalar fiyatla rekabet ettiğinde fiyat maliyete kadar inebilir."
  - "Fiyat savaşından kaçınmanın meşru yolu farklılaşma, hizmet ve maliyet avantajıdır."
glossary_terms: [oligopol, kartel, nash-dengesi]
related: [kb-eco-7-1-game-theory-for-managers, kb-eco-8-2-vertical-restraints, kb-fmcg-12-5-ethics-compliance-trade, kb-fmcg-1-2-scale-and-concentration]
sources:
  - title: "Noncooperative Collusion under Imperfect Price Information"
    authors: "Green, E. J.; Porter, R. H."
    year: 1984
    type: article
    doi: "10.2307/1911462"
    url: "https://doi.org/10.2307/1911462"
    verified: true
    checked_on: 2026-10-28
    note: "Econometrica 52(1)."
  - title: "Principles of Economics 3e, §3.1 Demand, Supply, and Equilibrium in Markets for Goods and Services"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-economics-3e/pages/3-1-demand-supply-and-equilibrium-in-markets-for-goods-and-services"
    verified: true
    checked_on: 2026-10-28
  - title: "Rekabet Kurumu (resmî site)"
    authors: "Rekabet Kurumu"
    year: 2026
    type: web
    url: "https://www.rekabet.gov.tr"
    verified: true
    checked_on: 2026-10-28
  - title: "Grup Muafiyeti Tebliğleri"
    authors: "Rekabet Kurumu"
    year: 2026
    type: web
    url: "https://www.rekabet.gov.tr/tr/Sayfa/Mevzuat/grup-muafiyeti-tebligleri"
    verified: true
    checked_on: 2026-10-28
    note: "Dikey anlaşmalara ilişkin grup muafiyeti düzenlemeleri bu sayfada listelenir."
  - title: "4054 sayılı Rekabetin Korunması Hakkında Kanun"
    authors: "T.C. Resmî Gazete / Mevzuat Bilgi Sistemi"
    year: 1994
    type: law
    url: "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4054.pdf"
    verified: true
    checked_on: 2026-10-28
    note: "Mevzuat Bilgi Sistemi resmî PDF metni açıldı, kanun adı ve numarası eşleşti (2026-10-28)."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28

---

## Ne işe yarar?

Türkiye'de birçok ürün grubunda pazar, birkaç büyük üretici ve her bölgede birkaç güçlü distribütör arasında paylaşılır. Bu yapıda fiyat kararları birbirine bağlıdır. Bu kart, rakiplerin olası tepkisini hesaba katarak karar vermenizi ve yasal sınırların nerede başladığını hatırlamanızı sağlar.

## Temel fikir

**Oligopol** (*oligopoly*), az sayıda firmanın pazarın büyük kısmını tuttuğu yapıdır. İki temel davranış modeli vardır:

- **Miktar rekabeti (Cournot):** Firmalar üretim veya kapasite miktarını belirler, fiyatı pazar oluşturur. Fiyat, tam rekabetin üstünde ama tekelin altında kalır.
- **Fiyat rekabeti (Bertrand):** Ürünler benzer ve kapasite bolsa, her firma rakibin biraz altına inerek tüm pazarı almak ister. Sonuç: fiyat maliyete kadar düşer.

**Kartel** (*cartel*), rakiplerin fiyatı yükseltmek ya da pazarı paylaşmak için anlaşmasıdır. İki neden kartelden uzak durmanızı gerektirir:

1. **Yasaktır.** 4054 sayılı Rekabetin Korunması Hakkında Kanun, rakipler arasında fiyat tespiti, bölge veya müşteri paylaşımı ve teklif koordinasyonu gibi anlaşmaları ve uyumlu eylemleri yasaklar. Yazılı anlaşma olmasa da bilgi paylaşımı ve uyumlu davranış ihlal sayılabilir; para cezası ciroya bağlı olarak ağırdır.
2. **Kırılgandır.** Anlaşmaya uyan her firma için gizlice biraz fazla satmak kârlıdır. Green ve Porter (1984), talep dalgalanmasının hileyi gizlediği durumlarda bu tür anlaşmaların periyodik fiyat savaşlarıyla çöktüğünü modellemiştir.

## Bir örnek

> **Örnek (temsili rakamlar):** Talep fiyatı = 200 − toplam miktar, birim maliyet 50 TL olan iki firmalı bir pazar varsayılmıştır; hesaplar `scripts/cards_numbers_eco_b1.py` ile yapılmıştır. Örnek yalnızca neden fiyat savaşının ve anlaşmanın sonuçlarını anlamak içindir.

- **Miktar rekabeti:** Her firma 50 birim üretir, fiyat **100 TL**, firma başı kâr **2.500 TL**.
- **Tekel benzeri sonuç (yasak anlaşma):** Toplam 75 birim, her firma 37,5; fiyat 125 TL, firma başı kâr 2.812,5 TL.
- **Anlaşmayı bozma dürtüsü:** Rakip 37,5 birimde kalırken bir firma 56,25 birime çıkarsa fiyat 106,25 TL olur; bozan firma **3.164,06 TL**, uyan firma 2.109,38 TL kazanır.
- **Fiyat rekabeti:** Ürünler aynı ve kapasite bolsa fiyat **50 TL**'ye, yani maliyete iner; kâr sıfırlanır.

Ders: Fiyat savaşından korunmanın yolu rakiple anlaşmak değil; müşterinin gözünde farklı olmak (hizmet sıklığı, raf uygulaması, ödeme koşulları, ürün yelpazesi) ve maliyet avantajı yaratmaktır.

## Sık yapılan hatalar

- Fuarda, dernek toplantısında ya da yemekte rakiplerle fiyat artış tarihlerini veya iskonto planlarını konuşmak.
- Ortak bir distribütör veya tedarikçi üzerinden rakiplerin fiyat bilgisini almak ve paylaşmak.
- Bölge ya da kanal paylaşımını "centilmenlik anlaşması" olarak görmek.
- Rakibin tek bir fiyat indirimine anında ve sert karşılık verip fiyat savaşı başlatmak.
- Her şeyi fiyatla çözmeye çalışmak; farklılaşma fırsatlarını görmemek.

## Pratikte nasıl uygulanır?

- [ ] Satış ve yönetim ekibine yılda en az bir kez rekabet hukuku uyum eğitimi verin; kurallar için rekabet hukuku uzmanından destek alın.
- [ ] Rakiplerle ortak katıldığınız toplantılar için gündem ve tutanak kuralı belirleyin; fiyat konuşması başlarsa toplantıyı terk edip kayda geçirin.
- [ ] Rakip fiyat bilgisini yalnızca kamuya açık kaynaklardan ve saha gözlemiyle toplayın; kaynağını kaydedin.
- [ ] Fiyat kararlarını rakip tepkisi senaryolarıyla (karşılık verir/vermez) değerlendirin.
- [ ] Rekabet avantajınızı ölçün: hizmet maliyeti, teslim sıklığı, raf uygulaması ve müşteri memnuniyetinde rakiplere göre neredesiniz?

## Daha fazlası

- Green, E. J.; Porter, R. H. (1984). *Noncooperative Collusion under Imperfect Price Information*. https://doi.org/10.2307/1911462
- OpenStax (2026). *Principles of Economics 3e, §3.1 Demand, Supply, and Equilibrium in Markets for Goods and Services*. https://openstax.org/books/principles-economics-3e/pages/3-1-demand-supply-and-equilibrium-in-markets-for-goods-and-services
- Rekabet Kurumu (2026). *Rekabet Kurumu (resmî site)*. https://www.rekabet.gov.tr
- Rekabet Kurumu (2026). *Grup Muafiyeti Tebliğleri*. https://www.rekabet.gov.tr/tr/Sayfa/Mevzuat/grup-muafiyeti-tebligleri
- T.C. Resmî Gazete / Mevzuat Bilgi Sistemi (1994). *4054 sayılı Rekabetin Korunması Hakkında Kanun*. https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4054.pdf
