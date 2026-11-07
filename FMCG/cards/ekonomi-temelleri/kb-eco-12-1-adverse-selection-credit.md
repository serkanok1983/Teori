---
id: kb-eco-12-1-adverse-selection-credit
title: "Ters seçim ve sinyal: Vadeli satışta riskli müşteri neden kapınıza gelir?"
summary: "Bilgi asimetrisinin müşteri kredisinde ters seçim yarattığını, gevşek vade koşullarının neden riskli müşteriyi çektiğini ve tarama ile sinyal araçlarıyla müşteri portföyünün nasıl iyileştirileceğini anlatır."
course: eco
category: ekonomi-temelleri
tags: [kredi-riski, tahsilat, bilgi-asimetrisi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [ECO-12.1, ECO-12.2]
reading_minutes: 3
key_points:
  - "Müşteri kendi ödeme gücünü sizden daha iyi bilir; bu bilgi farkı ters seçim yaratır."
  - "Herkese aynı gevşek vade ve limit verildiğinde, bu koşulları en çok isteyen riskli müşteri olur."
  - "Tek bir riskli müşterinin zararı, birçok iyi müşterinin kârını silebilir."
  - "Tarama (bilgi toplama) ve sinyal (teminat, peşinat, geçmiş ödeme kaydı) ters seçimi azaltır."
glossary_terms: [ters-secim, bilgi-asimetrisi, sinyal]
related: [kb-eco-37-3-customer-credit-analysis, kb-eco-38-3-distributor-credit-risk-dbs, kb-fmcg-7-3-credit-collections-dso, kb-eco-12-3-principal-agent]
sources:
  - title: "The Market for \"Lemons\": Quality Uncertainty and the Market Mechanism"
    authors: "Akerlof, G. A."
    year: 1970
    type: article
    doi: "10.2307/1879431"
    url: "https://doi.org/10.2307/1879431"
    verified: true
    checked_on: 2026-10-28
    note: "Quarterly Journal of Economics 84(3)."
  - title: "Job Market Signaling"
    authors: "Spence, M."
    year: 1973
    type: article
    doi: "10.2307/1882010"
    url: "https://doi.org/10.2307/1882010"
    verified: true
    checked_on: 2026-10-28
    note: "Quarterly Journal of Economics 87(3)."
  - title: "Equilibrium in Competitive Insurance Markets: An Essay on the Economics of Imperfect Information"
    authors: "Rothschild, M.; Stiglitz, J."
    year: 1976
    type: article
    doi: "10.2307/1885326"
    url: "https://doi.org/10.2307/1885326"
    verified: true
    checked_on: 2026-10-28
    note: "Quarterly Journal of Economics 90(4)."
  - title: "Findeks"
    authors: "Kredi Kayıt Bürosu"
    year: 2026
    type: web
    url: "https://www.findeks.com"
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

Yeni bir bölgeye girerken ya da satışları hızlandırmak için vadeyi uzatıp limitleri açtığınızda, hemen gelen müşterilerin bir kısmı başka tedarikçilerden kredi alamayanlardır. Bu kart, bu durumun nedenini ve müşteri kredisi politikanızı buna göre nasıl kuracağınızı anlatır.

## Temel fikir

**Bilgi asimetrisi** (*information asymmetry*), işlemin bir tarafının diğerinden daha fazla bilgiye sahip olmasıdır. Müşteri kendi nakit durumunu, başka borçlarını ve ödeme niyetini sizden iyi bilir.

**Ters seçim** (*adverse selection*): Akerlof (1970), kaliteyi ayırt edemeyen alıcıların ortalama fiyat önermesinin iyi satıcıları piyasadan çektiğini ve piyasada kötü kalitenin kaldığını gösterdi. Vadeli satışta da benzer bir mekanizma çalışır: Herkese aynı gevşek koşulları verirseniz, bu koşullara en çok ihtiyacı olan, yani en riskli müşteriler orantısız şekilde gelir.

İki çözüm yolu vardır:

- **Tarama** (*screening*): Siz bilgi toplarsınız ya da farklı müşteri tiplerinin farklı seçeceği koşullar sunarsınız. Örneğin "peşin ödemede indirim, uzun vadede yüksek fiyat" menüsü. Rothschild ve Stiglitz (1976) sigorta piyasasında bu tür seçenek menülerinin tipleri ayırabileceğini gösterdi.
- **Sinyal** (*signalling*): Müşteri kendi kalitesini kanıtlayan, taklit etmesi pahalı bir adım atar: teminat, çek yerine banka garantili ödeme, peşinat, düzenli ödeme geçmişi. Spence (1973) bu fikri iş piyasasında eğitim üzerinden modelledi.

## Bir örnek

> **Örnek (temsili rakamlar):** Müşteri sayıları, satışlar ve temerrüt oranları varsayımsaldır; hesaplar `scripts/cards_numbers_eco_b1.py` ile yapılmıştır.

Yeni bir bölgede her müşteriye yılda 50.000 TL satış, brüt marj %10 (müşteri başı 5.000 TL).

- **İyi müşteri:** temerrüt olasılığı %1, beklenen kayıp 500 TL, net katkı **4.500 TL**.
- **Riskli müşteri:** temerrüt olasılığı %15, beklenen kayıp 7.500 TL, net katkı **−2.500 TL**.

Gevşek vade ile gelen 100 müşterinin 80'i iyi, 20'si riskli. Ortalama temerrüt %3,8; toplam net katkı 310.000 TL.

Basit bir tarama (Findeks raporu, ilk iki sipariş peşin, referans kontrolü) riskli müşteri sayısını 5'e indirirse toplam net katkı **347.500 TL** olur: daha az müşteriyle **37.500 TL** daha fazla kâr.

## Sık yapılan hatalar

- Satış hedefine ulaşmak için yeni müşterilere ilk siparişten yüksek limit ve uzun vade vermek.
- Vade koşullarını tüm müşterilere aynı uygulamak; ödeme davranışına göre farklılaştırmamak.
- Müşteri sayısındaki artışı başarı saymak; portföyün risk dağılımına bakmamak.
- Teminat ve peşinat isteğini müşteriyi kaçıracak bir hareket olarak görmek; iyi müşteri için bu bir fırsattır.
- Ödeme geçmişi verisini sistemde tutmamak ya da limit kararlarında kullanmamak.
- Vade koşullarını gevşetince gelen yeni müşterilerin risk profilini ayrıca izlememek.

## Pratikte nasıl uygulanır?

- [ ] Yeni müşteriler için yazılı bir kabul prosedürü (kimlik ve vergi kaydı, Findeks veya benzeri rapor, referans) belirleyin.
- [ ] İlk siparişleri peşin veya düşük limitle başlatın; limiti ödeme performansına göre kademeli artırın.
- [ ] Peşin indirimli ve vadeli fiyatlı bir koşul menüsü sunarak müşterilerin kendini ayrıştırmasını sağlayın.
- [ ] Bölge ve temsilci bazında temerrüt ve gecikme oranını raporlayın; satış primine tahsilat performansını ekleyin.
- [ ] Teminat, banka garantili ödeme veya DBS gibi araçları müşteri büyüklüğüne göre zorunlu tutun.
- [ ] Yeni müşterilerin ilk altı aylık ödeme performansını ayrı bir raporda takip edin.

## Daha fazlası

- Akerlof, G. A. (1970). *The Market for "Lemons": Quality Uncertainty and the Market Mechanism*. https://doi.org/10.2307/1879431
- Spence, M. (1973). *Job Market Signaling*. https://doi.org/10.2307/1882010
- Rothschild, M.; Stiglitz, J. (1976). *Equilibrium in Competitive Insurance Markets: An Essay on the Economics of Imperfect Information*. https://doi.org/10.2307/1885326
- Kredi Kayıt Bürosu (2026). *Findeks*. https://www.findeks.com
