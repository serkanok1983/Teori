---
id: kb-ea-25-1-crm-basics
title: "Strateji olarak CRM: Operasyonel, analitik ve iş birliği CRM'i"
summary: "Müşteri ilişkileri yönetimini bir yazılımdan önce bir strateji olarak ele alan Payne ve Frow çerçevesini; operasyonel, analitik ve iş birliği CRM'i ayrımını ve üretici ile bayi için CRM'in nereden başlatılabileceğini anlatır."
course: ea
category: saha-satis-ve-dms
tags: [crm, musteri, strateji, satis]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: orta
source_lessons: [EA-25.1]
reading_minutes: 3
key_points:
  - "CRM önce bir müşteri stratejisidir, yazılım bunun aracıdır."
  - "Payne ve Frow beş süreç önerir: strateji, değer yaratma, çok kanallı entegrasyon, bilgi yönetimi ve performans değerlendirme."
  - "Operasyonel CRM günlük satış ve hizmet işlerini, analitik CRM veriden öğrenmeyi destekler."
  - "İş birliği CRM'i müşteriyle ve iş ortaklarıyla bilgi paylaşımını kapsar."
  - "Müşteri ana verisi temiz değilse hiçbir CRM aracı işe yaramaz."
glossary_terms: [crm, operasyonel-crm, analitik-crm]
related: [kb-ea-25-2-customer-lifetime-value, kb-ea-26-1-retail-execution-sfa, kb-ea-25-5-customer-service-cases, kb-ea-25-4-consent-iys-marketing]
sources:
  - title: "A Strategic Framework for Customer Relationship Management"
    authors: "Payne, A.; Frow, P."
    year: 2005
    type: article
    doi: "10.1509/jmkg.2005.69.4.167"
    url: "https://doi.org/10.1509/jmkg.2005.69.4.167"
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

"CRM aldık ama kimse kullanmıyor" cümlesi sık duyulur. Çoğu zaman sorun yazılım değil, neyin amaçlandığının belirsiz olmasıdır. Bu kart, CRM'i önce strateji olarak düşünmenize yardım eder.

## Temel fikir

Payne ve Frow (2005), CRM'i birbirine bağlı beş süreçle tanımlar:

1. **Strateji geliştirme:** Hangi müşterilere, hangi değer önerisiyle odaklanacağız?
2. **Değer yaratma:** Müşteriye ne sunuyoruz, karşılığında müşteriden ne kazanıyoruz?
3. **Çok kanallı entegrasyon:** Saha satış, telefon, B2B portal ve e-posta gibi kanalların tutarlı çalışması.
4. **Bilgi yönetimi:** Müşteri verisinin toplanması, birleştirilmesi ve analiz edilmesi.
5. **Performans değerlendirme:** CRM'in ciro, kârlılık ve müşteri sadakatine etkisinin ölçülmesi.

Yazılım açısından üç tür CRM'den söz edilir:

- **Operasyonel CRM:** Ziyaret planı, fırsat takibi, teklif, sipariş ve şikâyet kaydı gibi günlük işler.
- **Analitik CRM:** Müşteri segmentasyonu, kayıp riski, çapraz satış fırsatları gibi veriden öğrenme.
- **İş birliği CRM'i:** Bayi portalları, ortak planlama ve müşteriyle paylaşılan bilgiler.

Üretici ve bayi dünyasında "müşteri" iki katmanlıdır: Bayi veya distribütör ile onların sattığı noktalar (bakkal, market, kafe). Hangi katmanı yöneteceğinizi baştan netleştirmek gerekir.

### CRM'i strateji olarak ele almak

Payne ve Frow, CRM'i bir yazılım değil, müşteri ilişkilerini yöneten süreçler bütünü olarak tanımlar. Bu bakış açısıyla bir CRM girişimi, şu sorularla başlamalıdır:

- **Hangi müşterilere odaklanıyoruz?** Tüm müşterilere aynı hizmeti vermek yerine, değer ve potansiyele göre segmentler tanımlanmalıdır. Büyük zincirler, orta ölçekli bayiler ve küçük noktalar farklı ilişki modelleri gerektirir.
- **Her segment için değer önerisi nedir?** Ziyaret sıklığı, ödeme koşulları, sipariş kanalları ve destek seviyesi segmentlere göre farklılaştırılabilir.
- **Hangi kanallarla temas ediyoruz?** Saha ziyareti, çağrı merkezi, portal, e-posta ve mesajlaşma kanallarının her birinin rolü ve müşteri bilgisini nasıl paylaştığı belirlenmelidir.
- **Bilgiyi nasıl topluyor ve kullanıyoruz?** Müşteriyle ilgili bilgiler (siparişler, şikâyetler, ziyaret notları) tek bir yerde toplanmalı ve ilgili tüm çalışanlar tarafından görülebilmelidir.
- **Başarıyı nasıl ölçüyoruz?** Müşteri elde tutma, müşteri başına kârlılık ve memnuniyet gibi göstergeler tanımlanmalıdır.

**Yaygın tuzak.** CRM projelerinin önemli bir kısmı, yazılım kurulduktan sonra kullanıcıların sistemi benimsememesi nedeniyle beklenen faydayı sağlayamaz. Satış ekibine, veri girişinin kendilerine ne kazandıracağını göstermek gerekir: daha iyi hazırlanmış ziyaretler, otomatik hatırlatmalar ve daha az rapor yükü.

**Kişisel veri.** Müşteri kişilerine ait iletişim bilgileri ve tercihleri kişisel veridir. Toplama amacı, izinler ve saklama süreleri tanımlanmalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b5.py` ile yapılmıştır.

Bir dağıtıcının sisteminde 2.400 satış noktası kayıtlı. Son üç ayda sipariş veren nokta sayısı 1.800; aktif oran **%75,0**. Kalan **600** noktanın bir kısmı kapanmış, bir kısmı ise rakibe geçmiş. Firma CRM projesine yazılım seçerek değil, şu soruyla başlıyor: "Pasif noktaların hangilerini geri kazanmak istiyoruz?" Önce müşteri ana verisi temizleniyor, sonra saha ekibine geri kazanım ziyaret listeleri veriliyor.

## Sık yapılan hatalar

- CRM'i yalnızca satış ekibinin rapor aracı olarak görmek.
- Müşteri verisini temizlemeden yeni sisteme taşımak.
- Kanalların (saha, telefon, portal) ayrı müşteri listeleri tutması.
- Başarıyı yazılımın kullanım oranıyla ölçüp iş sonucuna bakmamak.

## Pratikte nasıl uygulanır?

- [ ] Hangi müşteri grubuna, hangi sonuç için odaklanacağınızı yazın.
- [ ] Müşteri ana verisini tek kaynakta toplayın.
- [ ] Operasyonel CRM'le başlayın; analitiği veri oturduktan sonra ekleyin.
- [ ] CRM'in etkisini ciro, aktif müşteri ve tahsilat üzerinden ölçün.

## Daha fazlası

- Payne ve Frow (2005), *Journal of Marketing*. https://doi.org/10.1509/jmkg.2005.69.4.167
