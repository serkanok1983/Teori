---
id: kb-ea-20-2-order-to-cash
title: "Siparişten tahsilata: Bir satış sistemlerde nasıl ilerler?"
summary: "Bir bayi siparişinin saha uygulamasından ERP'ye, depodan faturaya ve tahsilata kadar izlediği yolu; her adımda hangi belgenin oluştuğunu ve muhasebeye ne yazıldığını sayısal bir örnekle anlatır."
course: ea
category: erp
tags: [erp, sfa, siparis, e-fatura, e-irsaliye, tahsilat, muhasebe]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru, it-yoneticisi]
level: temel
source_lessons: [EA-20.2]
reading_minutes: 4
key_points:
  - "Siparişten tahsilata süreci; sipariş, stok kontrolü, sevkiyat, fatura, alacak ve tahsilat adımlarından oluşur."
  - "Her adım bir belge üretir ve bir önceki belgeye bağlanır; bu zincir kopmadığı sürece hangi siparişin neden eksik gittiği ya da tahsil edilmediği izlenebilir."
  - "Fatura, sipariş edilen miktara göre değil, sevk edilen miktara göre kesilir."
  - "ERP, faturayla birlikte satış, KDV ve alacak kayıtlarını; sevkiyatla birlikte stok ve satılan malın maliyeti kayıtlarını otomatik oluşturur."
  - "Saha uygulaması ile ERP arasında müşteri, ürün ve fiyat verisi aynı değilse süreç en çok burada kırılır."
glossary_terms: [siparisten-tahsilata, erp, sfa, e-fatura, e-irsaliye, siparis-karsilama-orani]
related: [kb-ea-20-1-what-erp-does, kb-ea-20-3-procure-to-pay, kb-ea-37-1-e-document-map, kb-ea-26-5-van-sales-presales, kb-ea-8-2-data-quality-field, kb-eco-38-2-cash-conversion-cycle, kb-ea-40-4-integrating-sfa-with-erp]
sources:
  - title: "What is ERP?"
    authors: "Klaus, H.; Rosemann, M.; Gable, G. G."
    year: 2000
    type: article
    doi: "10.1023/A:1026543906354"
    url: "https://doi.org/10.1023/A:1026543906354"
    verified: true
    checked_on: 2026-10-28
    note: "Information Systems Frontiers 2(2), 141–162."
  - title: "Integrated Business Processes with ERP Systems"
    authors: "Magal, S. R.; Word, J."
    year: 2011
    type: book
    verified: false
    note: "Kitap; sipariş-tahsilat sürecinin belge akışı. Yıl ve baskı yayımlamadan önce kontrol edilmeli."
  - title: "e-Belge (Gelir İdaresi Başkanlığı e-belge portalı)"
    authors: "Gelir İdaresi Başkanlığı"
    year: 2026
    type: web
    url: "https://ebelge.gib.gov.tr/"
    verified: false
    note: "2026-10-28'de kutudan erişilemedi (TLS hatası). e-fatura/e-irsaliye kapsamı yayımlamadan önce buradan doğrulanmalı."
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Bir müşteri "siparişim eksik geldi", muhasebe "bu fatura hangi sevkiyata ait", satış müdürü "bu ayki ciro neden ERP'de farklı görünüyor" diye sorduğunda, cevap hep aynı süreçtedir: **siparişten tahsilata** (*order-to-cash*). Bu kart, bir satışın saha uygulamasından tahsilata kadar hangi adımlardan geçtiğini ve her adımda hangi kaydın oluştuğunu gösterir. Süreci bilen yönetici, sorunun hangi halkada olduğunu çok daha hızlı bulur.

## Temel fikir

**ERP** (*Enterprise Resource Planning*, kurumsal kaynak planlama), satış, stok, satın alma ve muhasebenin aynı veritabanını kullandığı yazılımdır. Saha satış uygulaması (*SFA*, *sales force automation*) ise siparişin sahada toplandığı yerdir. Tipik bir bayide süreç şu adımlardan geçer:

| Adım | Ne olur? | Oluşan belge / kayıt |
|---|---|---|
| 1. Sipariş | Temsilci müşteride siparişi alır; fiyat ve iskonto uygulanır. | Satış siparişi |
| 2. Stok kontrolü | Sistem, istenen miktarın depoda olup olmadığına bakar. | Rezervasyon |
| 3. Toplama ve sevkiyat | Depo ürünleri toplar, araç yüklenir, mal çıkışı yapılır. | Sevk irsaliyesi (e-irsaliye), stok çıkış kaydı |
| 4. Faturalama | Sevk edilen miktar üzerinden fatura kesilir. | Fatura (e-fatura ya da e-arşiv fatura), satış ve KDV kaydı |
| 5. Alacak | Müşterinin cari hesabına borç yazılır, vade başlar. | Cari hesap hareketi |
| 6. Tahsilat | Ödeme gelir, açık faturayla eşleştirilir. | Tahsilat makbuzu / banka kaydı |

Her belge bir öncekine bağlanır: fatura irsaliyeye, irsaliye siparişe. Bu bağ, "ne sipariş edildi, ne gitti, ne faturalandı, ne tahsil edildi" sorularının her birine tek tıkla cevap verilmesini sağlar.

## Bir örnek

> **Örnek (temsili rakamlar):** Müşteri, ürün ve fiyatlar gerçek değildir; tüm tutarlar `scripts/pilot_numbers.py` ile hesaplanmıştır. KDV oranı yalnızca örnek içindir; ürününüzün güncel oranını kontrol edin.

Bir bakkal, temsilciye 40 koli sipariş veriyor. Kolide 12 adet var, liste fiyatı 30,00 TL/adet, fatura altı iskonto %5, KDV %20 (örnek oran), bayinin birim maliyeti 26,00 TL.

**Adım 1–2 — Sipariş ve stok kontrolü.** Sipariş 40 × 12 = 480 adet. Depoda yalnızca 38 koli var; sistem 38 koliyi rezerve ediyor.

**Adım 3 — Sevkiyat.** 38 × 12 = **456 adet** sevk ediliyor. Eksik kalan 24 adet. Sipariş karşılama oranı 456 ÷ 480 = **%95,0**.

**Adım 4 — Fatura (sevk edilen miktar üzerinden).**

| Kalem | Hesap | Tutar |
|---|---|---|
| Brüt tutar | 456 × 30,00 | 13.680,00 TL |
| İskonto (%5) | 13.680,00 × 0,05 | 684,00 TL |
| Net tutar | 13.680,00 − 684,00 | 12.996,00 TL |
| KDV (%20, örnek) | 12.996,00 × 0,20 | 2.599,20 TL |
| **Fatura toplamı** | 12.996,00 + 2.599,20 | **15.595,20 TL** |

**Muhasebe kaydı (Tekdüzen Hesap Planı ile, örnek gösterim).** ERP faturayı onaylarken şu kaydı kendisi oluşturur:

| Hesap | Borç | Alacak |
|---|---|---|
| 120 Alıcılar | 15.595,20 | |
| 611 Satış İskontoları | 684,00 | |
| 600 Yurt İçi Satışlar | | 13.680,00 |
| 391 Hesaplanan KDV | | 2.599,20 |
| **Toplam** | **16.279,20** | **16.279,20** |

Mal çıkışıyla birlikte maliyet kaydı da oluşur: 456 × 26,00 = **11.856,00 TL** (621 Satılan Ticari Mallar Maliyeti borç, 153 Ticari Mallar alacak). Bu satıştan bayinin brüt kârı 12.996,00 − 11.856,00 = **1.140,00 TL**, net satışa oranı **%8,8**.

> **İpucu:** Bazı firmalar fatura altı iskontoyu ayrı hesapta izlemek yerine satışı doğrudan net tutarla 600 hesabına kaydeder. Hangisini kullandığınız muhasebe politikanıza bağlıdır; önemli olan saha raporu ile ERP raporunun aynı tanımı kullanmasıdır.

**Adım 5–6 — Alacak ve tahsilat.** 15.595,20 TL bakkalın cari hesabına borç yazılır. Vade sonunda ödeme bankaya geldiğinde 102 Bankalar borç, 120 Alıcılar alacak kaydıyla fatura kapanır.

**Kayıp satış.** Eksik giden 24 adetin net satış değeri 24 × 28,50 = **684,00 TL**'dir. Bu tutar hiçbir faturada görünmez; ancak sipariş ile sevkiyat karşılaştırılırsa fark edilir.

## Sık yapılan hatalar

- Ciroyu saha uygulamasındaki sipariş toplamından izlemek: ERP'deki faturalı satış her zaman daha düşük çıkar, çünkü eksik sevkiyat ve iadeler düşülmüştür.
- Faturayı sipariş miktarı üzerinden kesmek; sonra iade ya da fiyat farkı faturasıyla düzeltmek zorunda kalmak.
- Saha uygulaması ile ERP'de farklı fiyat listesi veya farklı müşteri kodu kullanmak.
- Tahsilatı belirli bir faturayla eşleştirmeden "hesaba" kaydetmek; hangi faturanın açık kaldığının bilinmemesi.
- Kayıp satışı (karşılanamayan siparişi) hiç ölçmemek.

## Pratikte nasıl uygulanır?

- [ ] Siparişten tahsilata akışınızı yukarıdaki tablo gibi tek sayfada çizin; her adımda hangi sistemin ve kimin sorumlu olduğunu yazın.
- [ ] Müşteri, ürün ve fiyat listesinin tek bir "doğru kaynağı" olsun; saha uygulaması bunu ERP'den alsın.
- [ ] Sipariş karşılama oranını (sevk edilen ÷ sipariş edilen) ürün ve depo bazında haftalık izleyin.
- [ ] Satış raporlarında "sipariş", "sevk" ve "fatura" rakamlarını ayrı ayrı gösterin.
- [ ] Tahsilatların fatura bazında eşleştirildiğinden emin olun; vadesi geçmiş faturaları temsilci bazında listeleyin.
- [ ] e-fatura / e-arşiv ve e-irsaliye kapsamınızı mali müşavirinizle yılda bir gözden geçirin.

> **Mevzuat notu:** Bu karttaki e-belge ve KDV bilgileri 2026-10-28 tarihi itibarıyla genel hatlarıyla derlenmiştir ve örnek amaçlıdır. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın.

## Daha fazlası

- Klaus, H., Rosemann, M. ve Gable, G. G. (2000). *What is ERP?* Information Systems Frontiers, 2(2), 141–162. https://doi.org/10.1023/A:1026543906354
- Magal, S. R. ve Word, J. *Integrated Business Processes with ERP Systems.* Wiley (kitap).
- Gelir İdaresi Başkanlığı, e-Belge portalı: https://ebelge.gib.gov.tr/
