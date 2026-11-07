---
id: kb-eco-50-4-tcmb-policy-rate-credit
title: "Politika faizi ve kredi koşulları: Merkez Bankası kararı şirketinize nasıl ulaşır?"
summary: "TCMB politika faizindeki değişimin banka kredisi faizine, kredi bulunabilirliğine ve vadeli satışın finansman maliyetine nasıl yansıdığını ve şirketin buna nasıl hazırlanacağını anlatır."
course: eco
category: makroekonomi-ve-enflasyon
tags: [faiz, kredi, finansman, makroekonomi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [ECO-18.2, ECO-50.4]
reading_minutes: 3
key_points:
  - "Politika faizi, bankaların fonlama maliyetini ve dolayısıyla kredi faizlerini etkiler."
  - "Kredi faizi yalnızca politika faizine değil, makroihtiyati düzenlemelere ve bankanın risk algısına da bağlıdır."
  - "Faizdeki değişim, işletme sermayesi kredisinin ve vadeli satışın finansman maliyetini doğrudan değiştirir."
  - "Para politikasının sıkılaştığı dönemlerde kredi miktarı da daralabilir; nakit planını buna göre yapın."
glossary_terms: [politika-faizi, isletme-sermayesi]
related: [kb-eco-21-1-monetary-policy-tcmb, kb-eco-18-3-real-vs-nominal-interest-fisher, kb-eco-50-3-working-with-banks, kb-eco-38-2-cash-conversion-cycle]
sources:
  - title: "Para Politikası"
    authors: "TCMB"
    year: 2026
    type: web
    url: "https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Temel+Faaliyetler/Para+Politikasi"
    verified: true
    checked_on: 2026-10-28
  - title: "Bankacılık Düzenleme ve Denetleme Kurumu (resmî site)"
    authors: "BDDK"
    year: 2026
    type: web
    url: "https://www.bddk.org.tr"
    verified: true
    checked_on: 2026-10-28
  - title: "Inside the Black Box: The Credit Channel of Monetary Policy Transmission"
    authors: "Bernanke, B. S.; Gertler, M."
    year: 1995
    type: article
    doi: "10.1257/jep.9.4.27"
    url: "https://doi.org/10.1257/jep.9.4.27"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Economic Perspectives 9(4)."
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Merkez Bankası faiz kararı açıklandığında bankanızın size teklif ettiği kredi faizi, vadeli alımlarınızın maliyeti ve müşterilerinize verebileceğiniz vade değişir. Bu kart, bu aktarım kanalını anlamanızı ve finansman maliyetinizi faiz senaryolarına göre planlamanızı sağlar.

## Temel fikir

**Politika faizi** (*policy rate*), merkez bankasının bankalara likidite sağlarken uyguladığı temel faiz oranıdır. Türkiye'de bu kararı TCMB Para Politikası Kurulu verir. Aktarım şöyle işler:

1. **Fonlama maliyeti:** Politika faizi değişince bankaların borçlanma maliyeti ve mevduat faizleri değişir.
2. **Kredi faizi:** Bankalar fonlama maliyetine kendi risk ve kâr marjlarını ekleyerek kredi fiyatlar.
3. **Kredi bulunabilirliği:** Bernanke ve Gertler (1995), para politikasının yalnızca faiz düzeyiyle değil, firmaların bilanço gücü ve bankaların kredi verme isteği üzerinden de etkili olduğunu tartıştı. Sıkılaşma dönemlerinde küçük ve teminatı zayıf firmalar krediye en zor erişenlerdir.
4. **Makroihtiyati araçlar:** TCMB ve BDDK, kredi büyümesi, zorunlu karşılık ve benzeri düzenlemelerle kredi koşullarını politika faizinden bağımsız olarak da etkileyebilir. Bu düzenlemeler sık değişir.

Distribütör ve üretici için sonuç: Faiz yükseldiğinde hem kendi kredinizin hem de müşterilerinize tanıdığınız vadenin maliyeti artar.

## Bir örnek

> **Örnek (temsili rakamlar):** Faiz oranları örnek amaçlıdır, güncel politika faizi veya kredi faizini temsil etmez. Hesaplar `scripts/cards_numbers_eco_b2.py` ile yapılmıştır.

**İşletme sermayesi kredisi.** 10.000.000 TL, 90 gün vadeli kredi:

- Yıllık faiz %50 ise faiz maliyeti **1.232.877 TL**.
- Yıllık faiz %45'e düşerse faiz maliyeti **1.109.589 TL**; fark 123.288 TL.

**Vadeli satışın maliyeti.** Müşterilere 60 gün vadeyle 20.000.000 TL alacak taşıyorsanız ve finansman maliyetiniz yıllık %50 ise, bu vadenin bir dönemlik maliyeti **1.643.836 TL**'dir. Faiz yükseldiğinde bu maliyeti fiyat, vade farkı ya da vade kısaltmayla telafi etmeniz gerekir.

## Sık yapılan hatalar

- Kredi limitlerinin her zaman açık kalacağını varsaymak; sıkılaşmada limitler daralabilir.
- Faiz yükselirken müşterilere verilen vadeyi aynı tutmak; finansman maliyetini fiyata yansıtmamak.
- Değişken faizli krediyi faiz senaryosu yapmadan almak.
- Makroihtiyati düzenlemelerin (kredi büyüme sınırları vb.) etkisini izlememek.
- Politika faizindeki indirimin kredi faizlerine hemen ve tamamen yansıyacağını varsaymak; bankaların fonlama maliyeti ve makroihtiyati düzenlemeler bu geçişi geciktirebilir.
- Kredi erişimini yalnızca faize bağlı düşünmek; sıkı dönemlerde limit bulmak faizden daha zor olabilir.

## Pratikte nasıl uygulanır?

- [ ] TCMB Para Politikası Kurulu toplantı takvimini ve karar metinlerini izleyin.
- [ ] Nakit planınızda finansman maliyetini en az üç faiz senaryosuyla hesaplayın.
- [ ] Müşteri vadelerinin finansman maliyetini her ay hesaplayın; vade farkı politikanızı buna göre güncelleyin.
- [ ] Birden fazla bankayla çalışın; limitlerinizi kullanmasanız da açık tutun.
- [ ] Kredi düzenlemelerinin şirketinize etkisini bankanızla ve mali danışmanınızla düzenli olarak gözden geçirin.
- [ ] Kredi vadelerinizi Para Politikası Kurulu takvimiyle birlikte bir tabloda izleyin.
- [ ] Faiz değişiminin yıllık faiz giderinize etkisini bütçede ayrı bir satırda hesaplayın.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın.

## Daha fazlası

- TCMB (2026). *Para Politikası*. https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Temel+Faaliyetler/Para+Politikasi
- BDDK (2026). *Bankacılık Düzenleme ve Denetleme Kurumu (resmî site)*. https://www.bddk.org.tr
- Bernanke, B. S.; Gertler, M. (1995). *Inside the Black Box: The Credit Channel of Monetary Policy Transmission*. https://doi.org/10.1257/jep.9.4.27
