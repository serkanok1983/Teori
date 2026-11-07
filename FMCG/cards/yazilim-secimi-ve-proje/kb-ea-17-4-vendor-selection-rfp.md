---
id: kb-ea-17-4-vendor-selection-rfp
title: "Tedarikçi seçimi: Bilgi talebi, teklif talebi, senaryolu demo ve referans"
summary: "Bir yazılım tedarikçisini seçerken uzun listeden kısa listeye inmeyi; bilgi talebi (RFI) ve teklif talebi (RFP) belgelerini, senaryolu demoyu, referans görüşmesini ve sözleşmeye girmesi gereken maddeleri anlatır."
course: ea
category: yazilim-secimi-ve-proje
tags: [yazilim-secimi, rfp, tedarikci, sozlesme]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, it-yoneticisi]
level: orta
source_lessons: [EA-17.4]
reading_minutes: 3
key_points:
  - "Seçim bir huni gibi ilerler: uzun liste, bilgi talebi, teklif talebi, demo, referans, sözleşme."
  - "Teklif talebi, önceliklendirilmiş ihtiyaçlar ve aynı fiyat kalemleriyle hazırlanmalıdır."
  - "Demoyu tedarikçi değil siz yönetirsiniz: kendi senaryolarınızı ve verinizi verin."
  - "Referans görüşmesinde benzer büyüklükte ve sektörde bir müşteriyle konuşun."
  - "Hizmet seviyesi, veri iadesi, fiyat artışı ve kilit kadro maddeleri sözleşmeye yazılmalıdır."
glossary_terms: [rfp, sla]
related: [kb-ea-17-3-writing-requirements, kb-ea-17-2-total-cost-of-ownership, kb-ea-17-1-build-buy-configure, kb-ea-6-2-it-service-sla]
sources:
  - title: "A Guide to the Business Analysis Body of Knowledge (BABOK Guide) v3"
    authors: "IIBA"
    year: 2015
    type: book
    url: "https://www.iiba.org/business-analysis-certifications/cbap/"
    verified: false
    note: "Müfredatta bu ders için dış kaynak yok (ders sentezi); BABOK genel çerçeve olarak verildi, içerik kontrol edilmedi."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Yazılım seçimi çoğu zaman en etkileyici sunumu yapan tedarikçinin kazanmasıyla biter. Bu kart, seçimi adım adım ve karşılaştırılabilir biçimde yürütmenizi sağlar.

## Temel fikir

Seçim bir huni gibi daralır:

1. **Uzun liste:** Sektördeki kullanıcılardan, iş ortaklarından ve araştırmalardan 8–10 aday.
2. **Bilgi talebi** (RFI, *request for information*): Kısa bir anketle firma büyüklüğü, sektör deneyimi, Türkiye'de destek ve e-belge uyumu sorulur.
3. **Teklif talebi** (RFP, *request for proposal*): Önceliklendirilmiş ihtiyaç listesi, kullanıcı sayıları, entegrasyonlar ve tek tip fiyat tablosu gönderilir. Tedarikçi her ihtiyaca "standart / ayarla / geliştirme / yok" diye cevap verir.
4. **Senaryolu demo:** Tedarikçiye kendi süreçlerinizden 4–6 senaryo ve örnek veri verilir. Demo hazır sunum değil, sizin senaryonuzdur.
5. **Referans görüşmesi:** Benzer büyüklükte ve sektörde, tercihen tedarikçinin seçmediği bir müşteriyle konuşulur.
6. **Sözleşme:** Hizmet seviyesi (**SLA**), veri iadesi, fiyat artış üst sınırı, kilit kadro, kabul kriterleri ve ödeme takvimi.

Puanlama ölçütleri ve ağırlıkları, teklifler açılmadan önce yazılmalıdır.

### Değerlendirmeyi adil ve izlenebilir yapmak

Tedarikçi seçimi, büyük bir yatırım kararıdır ve sonuçları yıllarca sürer. Sürecin adil ve izlenebilir olması, hem doğru kararı hem de iç onayı kolaylaştırır.

- **Ağırlıklı puanlama:** Değerlendirme ölçütleri ve ağırlıkları, teklifler gelmeden önce belirlenmelidir. Teklifler geldikten sonra ağırlıkların değiştirilmesi, sonucun belirli bir tedarikçiye göre ayarlandığı izlenimi yaratır.
- **Bağımsız puanlama:** Değerlendirme ekibi üyeleri önce bağımsız puan vermeli, ardından farklar birlikte tartışılmalıdır.
- **Senaryolu demo:** Tedarikçilere, şirketinizin gerçek iş senaryoları ve örnek verileri önceden gönderilmelidir. Demo sırasında hazır sunum yerine bu senaryoların canlı olarak yürütülmesi istenmelidir. Zor istisnalar ve ay sonu işlemleri de senaryolara dahil edilmelidir.
- **Referans görüşmeleri:** Tedarikçinin önerdiği referansların yanı sıra, benzer ölçek ve sektördeki başka müşterilerle de görüşülmeye çalışılmalıdır. Proje süresi, bütçe sapması ve canlı sonrası destek kalitesi sorulmalıdır.
- **Uygulama ortağı:** Yazılım kadar, onu kuracak ekibin deneyimi de önemlidir. Önerilen proje ekibinin kimlerden oluşacağı ve bu kişilerin özgeçmişleri istenmelidir.

**Sözleşme aşaması.** Seçimden sonra sözleşme müzakeresinde kapsam, kabul kriterleri, ödeme planının kilometre taşlarına bağlanması, fiyat artış sınırları, veri sahipliği ve çıkış koşulları ele alınmalıdır. Teklif talebindeki taahhütlerin sözleşmeye eklenmesi, sonraki tartışmaları azaltır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b4.py` ile yapılmıştır.

Bir bayi, saha satış yazılımı için 9 adaydan bilgi talebiyle 5'e, teklif talebiyle 3'e iniyor. Ağırlıklar: işlevsel uygunluk %40, maliyet %25, tedarikçi güvenilirliği %20, teknik uygunluk %15.

| Tedarikçi | Ağırlıklı puan |
|---|---|
| A | 3,60 |
| B | 3,65 |
| C | 3,55 |

Puanlar birbirine çok yakın. Bayi, A ve B'yi senaryolu demoya çağırıyor: çevrimdışı sipariş, kampanya uygulama ve iade senaryoları. Demoda B'nin kampanya senaryosunu ancak geliştirmeyle karşılayabildiği ortaya çıkıyor. Referans görüşmesinde A'nın canlı geçiş desteği iyi değerlendiriliyor. Karar A'dan yana veriliyor ve sözleşmeye kilit danışmanların proje boyunca değiştirilemeyeceği maddesi ekleniyor.

## Sık yapılan hatalar

- Puanlama ölçütlerini teklifler geldikten sonra belirlemek.
- Tedarikçinin hazır demosunu izleyip kendi senaryolarınızı denememek.
- Yalnızca tedarikçinin önerdiği referanslarla konuşmak.
- Sözleşmeyi tedarikçinin standart metniyle imzalamak.

## Pratikte nasıl uygulanır?

- [ ] Bilgi talebi için en fazla 20 soruluk kısa bir anket hazırlayın.
- [ ] Teklif talebine önceliklendirilmiş ihtiyaçları ve tek tip fiyat tablosunu ekleyin.
- [ ] Demo senaryolarını ve örnek veriyi tedarikçilere önceden gönderin.
- [ ] En az iki referansla görüşün; birini kendiniz bulun.
- [ ] Sözleşmeyi hukuk ve BT ile birlikte gözden geçirin.

## Daha fazlası

- IIBA, BABOK Guide v3 (genel çerçeve; doğrulanmadı).
