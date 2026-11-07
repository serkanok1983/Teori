---
id: kb-ea-16-5-cloud-cost-data-residency
title: "Bulut maliyeti (FinOps) ve verinin nerede tutulduğu"
summary: "Bulut faturasının neden beklenenden yüksek çıktığını, FinOps yaklaşımıyla maliyetin nasıl görünür ve sahipli hale getirildiğini; verinin hangi ülkede tutulduğunun KVKK ve sektör düzenlemeleri açısından neden önemli olduğunu anlatır."
course: ea
category: bt-yonetisimi-ve-guvenlik
tags: [bulut, finops, maliyet, veri-konumu, kvkk, mevzuat]
roles: [finans-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-16.5]
reading_minutes: 3
key_points:
  - "Bulutta ödeme kullanıma göredir; açık unutulan kaynak her saat fatura üretir."
  - "FinOps, bulut maliyetini finans, BT ve iş birimlerinin birlikte sahiplendiği bir disiplindir."
  - "Etiketleme, bütçe uyarısı ve mesai dışı kapatma en hızlı tasarruf adımlarıdır."
  - "Verinin hangi ülkede tutulduğu KVKK'daki yurt dışına aktarım kurallarını etkiler."
  - "Bankacılık gibi düzenlenmiş sektörlerde ek veri konumu kuralları olabilir; güncel düzenleme kontrol edilmelidir."
glossary_terms: [finops, veri-konumu, bulut-bilisim]
related: [kb-ea-16-1-cloud-saas-basics, kb-ea-15-5-kvkk-basics, kb-ea-17-2-total-cost-of-ownership, kb-ea-6-2-it-service-sla]
sources:
  - title: "What is FinOps?"
    authors: "FinOps Foundation"
    year: 2026
    type: web
    url: "https://www.finops.org/introduction/what-is-finops/"
    verified: true
    checked_on: 2026-10-28
  - title: "Bankacılık Düzenleme ve Denetleme Kurumu"
    authors: "BDDK"
    year: 2026
    type: web
    url: "https://www.bddk.org.tr/"
    verified: true
    checked_on: 2026-10-28
    note: "Site erişimi doğrulandı; ilgili yönetmelik metni ayrıca kontrol edilmeli."
  - title: "Kişisel Verileri Koruma Kurumu"
    authors: "KVKK"
    year: 2026
    type: web
    url: "https://www.kvkk.gov.tr/"
    verified: true
    checked_on: 2026-10-28
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Buluta geçen birçok firma, birkaç ay sonra faturanın tahmin edilenin üzerine çıktığını görür. Bir de "verimiz nerede duruyor?" sorusu vardır. Bu kart, iki konuyu yönetici gözüyle ele alır.

## Temel fikir

**Maliyet.** Bulutta sabit bir sunucu satın almazsınız; sanal sunucu, depolama ve veri transferi için kullandığınız kadar ödersiniz. Bu esneklik, unutulan test sunucusu ya da gece boş çalışan makine gibi israfları da faturaya yansıtır.

FinOps Vakfı'nın tanımladığı **FinOps** yaklaşımı, bulut maliyetini yalnızca BT'nin değil finans ve iş birimlerinin de ortak sorumluluğu yapar. Tekrarlanan üç aşaması vardır:

1. **Görünür kılmak:** Her kaynağı proje, bölüm ve ortam (canlı, test) ile etiketlemek; maliyeti sahibine göre raporlamak.
2. **İyileştirmek:** Gereğinden büyük sunucuları küçültmek, mesai dışında kapatmak, uzun süreli kullanım için taahhütlü fiyatlardan yararlanmak.
3. **İşletmek:** Bütçe ve uyarı eşikleri, aylık maliyet gözden geçirme toplantısı.

**Veri konumu.** Bulut sağlayıcısının veriyi hangi ülkede tuttuğu önemlidir. Kişisel veri içeren bir sistemin yurt dışında barındırılması, KVKK kapsamında yurt dışına aktarım sayılabilir ve bu kurallar 2024'te değişmiştir. Bankacılık ve bazı kamu alanlarında ise BDDK gibi düzenleyicilerin ek kuralları bulunabilir. Bu kart kuralların ayrıntısını vermez; güncel metinler kontrol edilmelidir.

### Maliyet ve uyum için düzenli gözden geçirme

Bulut maliyeti ve veri konumu, bir kez karara bağlanıp bırakılacak konular değildir. Aylık maliyet raporu, hizmet ve birim bazında incelenmeli; kullanılmayan kaynaklar, gereksiz büyük boyutlandırmalar ve unutulan test ortamları kapatılmalıdır. Her kaynağın bir sahibi ve maliyet merkezi etiketi olması, bu incelemeyi mümkün kılar. Veri konumu açısından ise yeni bir hizmet devreye alınırken verinin hangi bölgede işleneceği, yedeklerin nerede tutulacağı ve destek ekiplerinin veriye hangi ülkeden erişebileceği kontrol listesine eklenmelidir. Sektöre özgü düzenlemeler ve kişisel veri mevzuatındaki değişiklikler için hukuk danışmanınızla düzenli görüşmeniz önerilir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b3.py` ile yapılmıştır.

Bir üreticinin raporlama sunucusu yalnızca mesai saatlerinde kullanılıyor ama 7/24 açık:

| Çalışma düzeni | Aylık saat | Saatlik 9,40 TL ile aylık maliyet |
|---|---|---|
| 7/24 (30 gün) | 720 | 6.768,00 TL |
| Günde 12 saat, 22 iş günü | 264 | 2.481,60 TL |

Otomatik açma–kapatma ile bu sunucuda **%63,3** tasarruf sağlanıyor. Firma, tüm kaynaklara "bölüm" ve "ortam" etiketi zorunluluğu getiriyor ve aylık bütçenin %80'ine ulaşıldığında finans müdürüne uyarı gönderiyor.

Aynı gözden geçirmede CRM verisinin yurt dışındaki bir veri merkezinde tutulduğu fark ediliyor. Konu hukuk danışmanına iletiliyor ve sağlayıcının Türkiye bölgesi seçeneği soruluyor.

## Sık yapılan hatalar

- Test ortamlarını iş bittikten sonra kapatmamak.
- Etiketsiz kaynaklara izin vermek; kimse maliyetin sahibi olmaz.
- Veri konumunu sözleşmede sormamak.
- Taahhütlü fiyata kullanım belli olmadan uzun süre bağlanmak.

## Pratikte nasıl uygulanır?

- [ ] Bulut faturasını bölüm ve proje bazında görünür hale getirin.
- [ ] Mesai dışında gerekmeyen kaynaklar için otomatik kapatma kurun.
- [ ] Bütçe uyarılarını finans ve BT'ye birlikte gönderin.
- [ ] Her bulut hizmeti için veri konumunu ve aktarım dayanağını hukukla birlikte kayda geçirin.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın. Veri konumu ve yurt dışına aktarım için hukuk danışmanı görüşü alınmalıdır.

## Daha fazlası

- FinOps Vakfı: https://www.finops.org/introduction/what-is-finops/
- KVKK: https://www.kvkk.gov.tr/
- BDDK: https://www.bddk.org.tr/
