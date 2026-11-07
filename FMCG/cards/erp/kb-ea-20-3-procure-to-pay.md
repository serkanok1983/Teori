---
id: kb-ea-20-3-procure-to-pay
title: "Satın almadan ödemeye (P2P): Üçlü eşleştirme"
summary: "Satın alma talebinden tedarikçi ödemesine kadar olan süreci; satın alma siparişi, mal kabul, fatura kontrolü, üçlü eşleştirme, mal kabul–fatura ara hesabı ve ödeme adımlarını ERP'deki karşılıklarıyla anlatır."
course: ea
category: erp
tags: [erp, satin-alma, p2p, ic-kontrol, odeme]
roles: [bayi-sahibi, bayi-yonetici, finans-muduru, depo-lojistik-muduru, it-yoneticisi]
level: temel
source_lessons: [EA-20.3]
reading_minutes: 3
key_points:
  - "Süreç: talep, satın alma siparişi, mal kabul, fatura kontrolü, ödeme."
  - "Üçlü eşleştirme; sipariş, mal kabul ve faturanın miktar ve fiyatta uyumunu kontrol eder."
  - "Uyumsuz fatura ödemeye kapatılır ve farkın nedeni araştırılır."
  - "Mal kabul–fatura ara hesabı, gelmiş ama faturası gelmemiş (ya da tersi) malları gösterir."
  - "Talep, onay, mal kabul ve ödeme adımları farklı kişilerde olmalıdır."
glossary_terms: [uclu-eslestirme, satinalma-siparisi, gorevler-ayriligi]
related: [kb-ea-20-2-order-to-cash, kb-ea-34-1-purchasing-supplier-management, kb-ea-6-4-internal-controls-sod, kb-ea-20-5-inventory-in-erp]
sources:
  - title: "Integrated Business Processes with ERP Systems"
    authors: "Magal, S. R.; Word, J."
    year: 2011
    type: book
    verified: false
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Fazla ödenen bir fatura, gelmeyen mal için yapılan ödeme ya da iki kez ödenen bir tedarikçi… Bunların çoğu satın alma sürecinin adımları birbirine bağlı olmadığında olur. Bu kart, **satın almadan ödemeye** (P2P, *procure-to-pay*) sürecini ERP'deki kontrol noktalarıyla anlatır.

## Temel fikir

Magal ve Word'ün anlattığı standart akış:

1. **Satın alma talebi:** İhtiyacı olan bölüm talep açar (ör. depo, ambalaj malzemesi).
2. **Satın alma siparişi:** Satın alma, onaylı tedarikçi ve fiyatla sipariş oluşturur; tutara göre onay alınır.
3. **Mal kabul:** Depo, gelen malı siparişe referansla kabul eder. Stok artar; muhasebede stok hesabı borçlanır, **mal kabul–fatura ara hesabı** alacaklanır.
4. **Fatura kontrolü:** Tedarikçi faturası (çoğunlukla e-Fatura) siparişe ve mal kabule eşlenir.
5. **Ödeme:** Vadesi gelen ve onaylı faturalar ödeme listesine girer.

**Üçlü eşleştirme**, siparişteki fiyat ve miktarı, mal kabuldeki miktarı ve faturadaki fiyat ve miktarı karşılaştırır. Tolerans dışındaki farklar faturayı ödemeye kapatır.

**Ara hesap**, sürecin aynasıdır: Bakiye, faturası gelmemiş mal kabulleri ya da malı gelmemiş faturaları gösterir. Ay sonunda bu hesabın kalem kalem açıklanabilmesi gerekir.

Kontrol açısından talep, sipariş onayı, mal kabul ve ödeme farklı kişilerde olmalıdır (**görevler ayrılığı**).

### P2P sürecinde kontrol ve verimlilik

Satın almadan ödemeye süreci, hem şirketin parasının korunması hem de tedarikçi ilişkilerinin sağlıklı yürümesi açısından önemlidir. Süreçte dikkat edilmesi gereken başlıca konular şunlardır:

- **Siparişsiz fatura:** Sipariş olmadan gelen faturalar, eşleştirme kontrolünü devre dışı bırakır. Hizmet alımları ve küçük harcamalar dışında, siparişsiz fatura kabul edilmemesi bir politika olarak belirlenmelidir.
- **Tolerans ayarları:** Sipariş ile fatura arasında küçük fiyat ve miktar farkları için toleranslar tanımlanabilir. Toleransların çok geniş olması kontrolü zayıflatır, çok dar olması ise gereksiz iş yükü yaratır.
- **Mal kabulün zamanında kaydı:** Mal kabul sisteme geç girilirse, fatura eşleştirilemez ve ödeme gecikir. Bu durum tedarikçi ilişkilerini bozar ve erken ödeme iskontolarının kaçırılmasına yol açar.
- **Ara hesabın izlenmesi:** Mal alındı ancak faturası gelmedi veya fatura geldi ancak mal alınmadı durumlarını gösteren ara hesap, düzenli olarak analiz edilmelidir. Uzun süredir bekleyen kalemler, süreç sorunlarının işaretidir.
- **Mükerrer ödeme kontrolü:** Aynı tedarikçiden aynı numara ve tutarla gelen faturalar otomatik olarak işaretlenmelidir.

**Ödeme planlaması.** Ödemeler, vade tarihine göre planlanmalı ve nakit tahminine yansıtılmalıdır. Erken ödeme iskontosu sunan tedarikçiler için iskontonun finansman maliyetiyle karşılaştırılması gerekir.

**Ölçüm.** Fatura işleme süresi, otomatik eşleşme oranı ve vadesinde ödeme oranı, P2P sürecinin temel göstergeleridir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b4.py` ile yapılmıştır.

Bir bayi, 1.000 adet ürünü adet fiyatı 42,00 TL'den sipariş ediyor. Depo 980 adet kabul ediyor. Tedarikçinin faturası 1.000 adet üzerinden **42.000,00 TL**.

- Mal kabul değeri: **41.160,00 TL**
- Fark: 20 adet, **840,00 TL**

ERP, miktar farkı nedeniyle faturayı ödemeye kapatıyor. Satın alma, tedarikçiden 20 adet için iade faturası istiyor ya da eksik malın gönderilmesini bekliyor. Bu kontrol olmasaydı fatura tam ödenecek ve fark ancak stok sayımında ortaya çıkacaktı.

## Sık yapılan hatalar

- Siparişsiz alım yapıp faturayı sonradan sisteme işlemek.
- Mal kabulü fiziksel sayım yapmadan, irsaliyedeki miktarla girmek.
- Ödemeye kapatılan faturaları toplu olarak "serbest bırakmak".
- Ara hesabın bakiyesini aylarca açıklamadan bırakmak.

## Pratikte nasıl uygulanır?

- [ ] Belirli bir tutarın üzerindeki tüm alımlar için siparişi zorunlu kılın.
- [ ] Üçlü eşleştirme toleranslarını (fiyat ve miktar) yazılı belirleyin.
- [ ] Ödemeye kapatılan faturaları haftalık olarak raporlayın.
- [ ] Mal kabul–fatura ara hesabını her ay kalem bazında açıklayın.

## Daha fazlası

- Magal ve Word, *Integrated Business Processes with ERP Systems* (kitap; doğrulanmadı).
