---
id: kb-ea-1-1-what-is-an-enterprise-system
title: "Kurumsal bilgi sistemi nedir? Yazılımdan fazlası"
summary: "Kurumsal sistemi yalnızca program olarak değil; insan, süreç, veri ve teknolojinin birlikte çalıştığı bir bütün olarak görmeyi ve uygulama ailelerinin değer zincirine nasıl oturduğunu anlatır."
course: ea
category: is-sistemleri-temelleri
tags: [erp, sfa, dms, wms, entegrasyon, veri-kalitesi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, it-yoneticisi]
level: temel
source_lessons: [EA-1.1, EA-1.2]
reading_minutes: 3
key_points:
  - "Bilgi sistemi; insan, prosedür, veri ve teknolojinin birlikte çalışmasıdır, tek başına yazılım değildir."
  - "Kurumsal sistemi kurumsal yapan şey, satış, depo ve muhasebenin aynı veriyi paylaşmasıdır."
  - "Aynı bilgiyi birden fazla yere elle girmek hem zaman kaybı hem de hata kaynağıdır."
  - "Her uygulama ailesi (ERP, SFA, DMS, WMS, CRM, BI) değer zincirinde belirli bir faaliyete hizmet eder."
  - "Yazılım seçmeden önce hangi kararı, kimin, hangi veriyle vereceğini netleştirin."
glossary_terms: [kurumsal-bilgi-sistemi, erp, sfa]
related: [kb-ea-20-1-what-erp-does, kb-ea-5-4-application-portfolio, kb-ea-3-2-it-plus-process-complementarity, kb-ea-41-1-case-distributor-app-landscape, kb-ea-8-1-master-data-governance]
sources:
  - title: "Management Information Systems: Managing the Digital Firm"
    authors: "Laudon, K. C.; Laudon, J. P."
    year: 2020
    type: book
    verified: false
    note: "Ders kitabı; baskı ve yıl yayımlamadan önce kontrol edilmeli."
  - title: "What is ERP?"
    authors: "Klaus, H.; Rosemann, M.; Gable, G. G."
    year: 2000
    type: article
    doi: "10.1023/A:1026543906354"
    url: "https://doi.org/10.1023/A:1026543906354"
    verified: true
    checked_on: 2026-10-28
  - title: "Competitive Advantage: Creating and Sustaining Superior Performance"
    authors: "Porter, M. E."
    year: 1985
    type: book
    verified: false
    note: "Değer zinciri kavramı."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

"Bize iyi bir program lazım" cümlesi çoğu yazılım projesinin başlangıcıdır. Oysa sorun çoğu zaman programda değil, bilginin firmada nasıl dolaştığındadır. Bu kart, **kurumsal bilgi sistemini** (*enterprise information system*) doğru tanımlamanıza ve hangi uygulama ailesinin hangi işe yaradığını bir arada görmenize yardım eder. Yazılım seçerken, mevcut düzeni değerlendirirken ya da BT ekibiyle konuşurken ortak bir dil sağlar.

## Temel fikir

Veri, kaydedilmiş ham bilgidir: "20", bir barkod numarası, bir tarih. Bilgi ise veriyi bir karara yarayacak şekilde bağlamına oturtur: "Bakkal Yıldız bugün 20 koli bisküvi istedi, depoda 2 koli çay kaldı."

Bilgi sistemi dört parçadan oluşur: **insan**, **prosedür**, **veri** ve **teknoloji**. Kimsenin sipariş girmediği, "sipariş ne zaman onaylanmış sayılır" kuralı olmayan bir veritabanı, sadece bir BT parçasıdır; bilgi sistemi değildir. Bu yüzden yeni bir yazılım, iş yapma biçimi ve sorumluluklar değişmeden tek başına sonuç getirmez.

Bir sistemi **kurumsal** yapan, satış, depo ve muhasebe gibi birimleri kesmesi ve bu birimlerin **aynı veriyi** paylaşmasıdır. Temsilci, toplayıcı ve muhasebeci aynı sipariş kaydını okur. Ayrı ayrı tutulan Excel'ler ve elle aktarılan listeler ise bu özelliği bozar.

Uygulama aileleri, firmanın değer zincirindeki faaliyetlere karşılık gelir:

| Faaliyet | Tipik uygulama |
|---|---|
| Satın alma, stok, muhasebe | ERP (kurumsal kaynak planlama) |
| Saha ziyareti, sipariş, tahsilat | SFA (saha satış otomasyonu) |
| Üretici–bayi veri paylaşımı | DMS (distribütör yönetim sistemi) |
| Depo içi hareketler | WMS (depo yönetim sistemi) |
| Müşteri ilişkisi ve hizmet | CRM (müşteri ilişkileri yönetimi) |
| Raporlama ve analiz | BI (iş zekâsı) |

Bir başka ayrım da sistemlerin rolüdür: **kayıt sistemi** (resmî kaydın tutulduğu yer, ör. ERP), **etkileşim sistemi** (insanların işini yaptığı ekran, ör. saha uygulaması) ve **içgörü sistemi** (karar için analiz, ör. BI). Bir bilginin "doğru" halinin hangi sistemde durduğu baştan belli olmalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Firma ve rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b1.py` ile yapılmıştır.

Bir bayi günde 120 sipariş alıyor. Temsilci siparişi kâğıda yazıyor; ofiste sipariş ERP'ye, ardından depo için ayrı bir listeye tekrar giriliyor. Yani her sipariş iki kez daha elle yazılıyor ve her giriş ortalama 1,5 dakika sürüyor.

- Günlük ek giriş süresi: 120 × 2 × 1,5 = **360 dakika (6,0 saat)**.
- 22 iş günlük bir ayda: **132 saat**, yani neredeyse bir kişinin tam zamanlı işi.
- Her elle girişte %2 hata olduğunu varsayarsak günde 120 × 2 × 0,02 = **4,8** hatalı kayıt, ayda yaklaşık **106** hatalı kayıt.

Ortak veri üzerinde çalışan bir saha uygulaması ve ERP ile sipariş bir kez girilir; depo ve muhasebe aynı kaydı görür. Kazanç yalnızca zaman değildir: yanlış ürün gönderme, yanlış fatura ve müşteri şikâyeti de azalır.

## Sık yapılan hatalar

- Sistemi yalnızca yazılım satın almak olarak görmek; prosedür ve sorumlulukları tanımlamamak.
- Aynı müşteri ya da ürün bilgisini birkaç yerde ayrı ayrı tutmak.
- Hangi sistemin "doğru kayıt" olduğunu belirlememek; raporlar arasında çıkan farkları tartışmakla vakit kaybetmek.
- Uygulama ailelerini karıştırmak; örneğin depo sorununu satış uygulamasıyla çözmeye çalışmak.

## Pratikte nasıl uygulanır?

- [ ] Firmanızda sipariş, stok, fatura ve tahsilat bilgisinin hangi sistemde ilk kez oluştuğunu tek sayfada çıkarın.
- [ ] Aynı bilginin elle ikinci kez girildiği noktaları sayın ve süresini ölçün.
- [ ] Her ana veri için (müşteri, ürün, fiyat) tek bir "doğru kaynak" belirleyin.
- [ ] Yeni yazılım konuşulurken "hangi kararı, kim, hangi veriyle verecek?" sorusunu yazılı cevaplayın.
- [ ] Uygulamalarınızı yukarıdaki tabloya göre listeleyip boşlukları ve çakışmaları işaretleyin.

## Daha fazlası

- Klaus, Rosemann ve Gable (2000), "What is ERP?", *Information Systems Frontiers*. https://doi.org/10.1023/A:1026543906354
- Laudon ve Laudon, *Management Information Systems* (ders kitabı; baskı doğrulanmadı).
- Porter (1985), *Competitive Advantage* — değer zinciri kavramı (kitap; doğrulanmadı).
