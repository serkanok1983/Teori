---
id: kb-eco-7-1-game-theory-for-managers
title: "Yöneticiler için oyun teorisi: Rakip ne yapacak, siz ne yapmalısınız?"
summary: "Kararınızın sonucunun rakibin kararına bağlı olduğu durumları (fiyat savaşı, iskonto yarışı, raf pazarlığı) basit bir getiri tablosuyla analiz etmeyi ve tekrarlanan ilişkilerde neden işbirliğinin sürebildiğini anlatır."
course: eco
category: ekonomi-temelleri
tags: [strateji, rekabet, pazarlik]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: orta
source_lessons: [ECO-7.1, ECO-7.3, ECO-7.4]
reading_minutes: 3
key_points:
  - "Sonucunuz rakibin hamlesine bağlıysa, kendi seçeneklerinizi rakibin olası tepkileriyle birlikte bir tabloda değerlendirin."
  - "Herkesin kendi çıkarına en iyi hamlesi, toplamda herkes için kötü bir sonuca götürebilir (mahkûmlar ikilemi)."
  - "Tekrarlanan ilişkilerde gelecek yeterince değerliyse karşılıklı makul davranış sürdürülebilir."
  - "Hamle sırası ve inandırıcı taahhüt, sonucu değiştirebilir."
  - "Rakiplerle fiyat veya bölge konusunda anlaşmak yasaktır; oyun teorisi kendi kararınızı vermek içindir."
glossary_terms: [nash-dengesi, mahkumlar-ikilemi]
related: [kb-eco-7-7-oligopoly-collusion, kb-eco-7-5-auctions-tenders, kb-fmcg-13-14-negotiation-structure, kb-fmcg-4-3-competitive-strategy]
sources:
  - title: "Principles of Economics 3e, §3.1 Demand, Supply, and Equilibrium in Markets for Goods and Services"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-economics-3e/pages/3-1-demand-supply-and-equilibrium-in-markets-for-goods-and-services"
    verified: true
    checked_on: 2026-10-28
  - title: "The Economy 2.0"
    authors: "CORE Econ"
    year: 2026
    type: web
    url: "https://www.core-econ.org/the-economy/"
    verified: true
    checked_on: 2026-10-28
  - title: "Rekabet Kurumu (resmî site)"
    authors: "Rekabet Kurumu"
    year: 2026
    type: web
    url: "https://www.rekabet.gov.tr"
    verified: true
    checked_on: 2026-10-28
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

Rakip distribütör bir zincire ek iskonto verdiğinde siz de verecek misiniz? Bir bölgede fiyat kırmak pazar payı getirir mi, yoksa herkesin marjını mı eritir? Bu kart, sonucu yalnızca sizin değil rakibinizin de kararına bağlı olan durumları sistematik düşünmenizi sağlar.

## Temel fikir

Oyun teorisi (*game theory*), birbirinin kararından etkilenen tarafların stratejik davranışını inceler. Yönetici için üç kavram yeterlidir:

- **Getiri tablosu:** Satırlar sizin seçenekleriniz, sütunlar rakibin seçenekleri; hücrelerde her iki tarafın sonucu. Tabloyu doldurmak bile çoğu zaman tartışmayı netleştirir.
- **Nash dengesi** (*Nash equilibrium*): Rakibin hamlesi verildiğinde hiçbir tarafın kendi hamlesini değiştirmek istemediği durum.
- **Mahkûmlar ikilemi** (*prisoner's dilemma*): Her taraf için tek başına en iyi hamle (iskonto vermek) olsa da, iki taraf da bunu yapınca ikisi de, ikisinin de vermediği duruma göre daha kötü durumda kalır.

**Tekrarlanan oyun:** Aynı rakiplerle yıllarca aynı pazarda iseniz, bugünkü saldırgan hamle yarın karşılık görür. Geleceğe verdiğiniz değer (iskonto faktörü) yeterince yüksekse, herkesin makul fiyatlama yaptığı durum, rakiplerle hiçbir konuşma olmadan, kendi kendine sürebilir. Bu, rakiplerle anlaşma anlamına gelmez; her firmanın kendi çıkarını hesapladığı bağımsız bir davranıştır.

**Hamle sırası ve taahhüt:** İlk hamleyi yapan ve geri dönüşü zor bir taahhütte bulunan (ör. kapasite yatırımı, kamuya açık fiyat politikası) taraf, rakibin seçeneklerini daraltabilir.

## Bir örnek

> **Örnek (temsili rakamlar):** İki distribütörün aylık kâr endeksleri varsayımsaldır; hesaplar `scripts/cards_numbers_eco_b1.py` ile yapılmıştır.

İki distribütör aynı bölgede, her ay "normal fiyat" ya da "ek iskonto" seçiyor. Getiriler (her biri için):

- İkisi de normal fiyat: 10
- Siz iskonto, rakip normal: siz 13, rakip 6
- İkisi de iskonto: 7

Tek seferlik oyunda iskonto vermek her durumda daha iyi görünür (13 > 10 ve 7 > 6). Sonuç: ikisi de iskonto verir ve ikisi de 7 alır, oysa 10 alabilirlerdi.

Tekrarlanan oyunda, rakip "bir kez iskonto verirsen ben de hep veririm" tepkisi gösteriyorsa:

- Normal fiyatta kalmanın toplam değeri, iskonto faktörü 0,8 iken: 10 / (1 − 0,8) = **50**.
- Bir kez iskonto verip sonra fiyat savaşına girmenin değeri: 13 + 0,8 × 7 / (1 − 0,8) = **41**.
- İskonto faktörü 0,50 üzerindeyse makul fiyatlamada kalmak daha kârlıdır.

Pazardan çıkmayı düşünen ya da kısa vadeli nakit sıkıntısı olan bir rakip için gelecek değeri düşüktür; fiyat savaşı başlatma olasılığı artar.

## Sık yapılan hatalar

- Rakibin tepkisini düşünmeden fiyat kırmak; ilk ay kazanılan payı sonraki aylarda kaybetmek.
- Rakibin de sizin kadar akılcı ve iyi bilgili olduğunu varsaymamak ya da tam tersine onu her şeyi bilen biri sanmak.
- Tek seferlik ihaleyi tekrarlanan ilişki gibi değerlendirmek (veya tersi).
- İnandırıcı olmayan tehditler savurmak ("fiyat kırarsanız hepinizi bitiririz").
- Rakiplerle fiyat, bölge ya da müşteri paylaşımı konuşmak; 4054 sayılı Kanun kapsamında ağır yaptırımı olan bir ihlaldir.

## Pratikte nasıl uygulanır?

- [ ] Kritik fiyat ve iskonto kararlarında 2×2 bir getiri tablosu hazırlayın; rakibin olası tepkisini her hücrede yazın.
- [ ] Rakiplerin finansal durumunu ve pazardaki kalış süresini izleyin; gelecek değeri düşük rakip daha saldırgan olabilir.
- [ ] Fiyat politikanızı açık ve tutarlı tutun; ani ve gerekçesiz indirimler fiyat savaşı başlatabilir.
- [ ] Zincir pazarlıklarında alıcının da bir oyuncu olduğunu, rakiplerinizin tekliflerini size karşı kullanabileceğini hesaba katın.
- [ ] Ekibinize rakiplerle fiyat, bölge ve müşteri konuşmanın yasak olduğunu düzenli olarak hatırlatın.

## Daha fazlası

- OpenStax (2026). *Principles of Economics 3e, §3.1 Demand, Supply, and Equilibrium in Markets for Goods and Services*. https://openstax.org/books/principles-economics-3e/pages/3-1-demand-supply-and-equilibrium-in-markets-for-goods-and-services
- CORE Econ (2026). *The Economy 2.0*. https://www.core-econ.org/the-economy/
- Rekabet Kurumu (2026). *Rekabet Kurumu (resmî site)*. https://www.rekabet.gov.tr
- T.C. Resmî Gazete / Mevzuat Bilgi Sistemi (1994). *4054 sayılı Rekabetin Korunması Hakkında Kanun*. https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4054.pdf
