---
id: kb-ea-17-3-writing-requirements
title: "İhtiyaç yazmak: Kullanıcı hikâyesi, kabul kriteri ve önceliklendirme"
summary: "Yazılım seçimi veya geliştirme için iş ihtiyaçlarını test edilebilir biçimde yazmayı; iş analizi bilgi alanlarını, kullanıcı hikâyesi ile ayrıntılı şartname farkını, kabul kriterlerini ve MoSCoW önceliklendirmesini anlatır."
course: ea
category: yazilim-secimi-ve-proje
tags: [ihtiyac-analizi, is-analizi, yazilim-secimi, proje]
roles: [it-yoneticisi]
level: orta
source_lessons: [EA-17.3]
reading_minutes: 2
key_points:
  - "İyi bir ihtiyaç, çözümü değil sorunu ve beklenen sonucu tarif eder."
  - "Her ihtiyaç test edilebilir olmalı; bunun için kabul kriteri yazılır."
  - "Kullanıcı hikâyesi kısa ve konuşmaya açıktır; ayrıntılı şartname sözleşme ve ihale için uygundur."
  - "MoSCoW yöntemi ihtiyaçları olmazsa olmaz, olmalı, olabilir ve bu sefer değil diye ayırır."
  - "Her ihtiyacın bir sahibi ve bir kaynağı (süreç adımı) olmalıdır."
glossary_terms: [kullanici-hikayesi, kabul-kriteri, moscow]
related: [kb-ea-17-1-build-buy-configure, kb-ea-17-2-total-cost-of-ownership, kb-ea-4-3-process-maps-bpmn, kb-ea-18-3-why-erp-projects-fail]
sources:
  - title: "A Guide to the Business Analysis Body of Knowledge (BABOK Guide) v3"
    authors: "IIBA"
    year: 2015
    type: book
    url: "https://www.iiba.org/business-analysis-certifications/cbap/"
    verified: false
    note: "IIBA sayfası erişilebilir; kitabın içeriği kontrol edilmedi."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

"Sistem raporlama yapabilmeli" gibi bir ihtiyaç, her tedarikçinin "evet" diyeceği ama hiçbir şeyi garanti etmeyen bir cümledir. Bu kart, ihtiyaçları karşılaştırılabilir ve test edilebilir biçimde yazmanızı sağlar.

## Temel fikir

Uluslararası İş Analizi Enstitüsü'nün (IIBA) rehberi BABOK, iş analizini planlama, ihtiyaç toplama, ihtiyaç yönetimi, strateji analizi, ihtiyaç analizi ve çözüm değerlendirme gibi bilgi alanlarına ayırır. Yönetici için en kritik kısım ihtiyacın **nasıl yazıldığıdır**.

İyi bir ihtiyacın özellikleri:

- **Sorunu anlatır, çözümü dikte etmez:** "Excel'e aktarma butonu" değil, "bölge müdürü haftalık satışları müşteri bazında görebilmeli".
- **Test edilebilir:** Bir **kabul kriteri** vardır: "Rapor 5.000 müşteri için 10 saniyede açılır."
- **Kaynağı bellidir:** Hangi süreç adımından ve kimden geldiği yazılır.
- **Önceliği vardır.**

İki yazım biçimi:

- **Kullanıcı hikâyesi:** "Bir [rol] olarak, [amaç] için [ihtiyaç] istiyorum." Kısa, konuşmayı başlatan ve aşamalı geliştirmeye uygun bir biçimdir.
- **Ayrıntılı şartname:** Numaralı, ölçülebilir maddeler. Paket seçimi ve sözleşme için daha uygundur.

**MoSCoW** önceliklendirmesi: *Must* (olmazsa olmaz), *Should* (olmalı), *Could* (olabilir), *Won't* (bu sefer değil).

### İhtiyaç toplama ve doğrulama yöntemleri

İyi yazılmış ihtiyaçlar, doğru toplanmış bilgiye dayanır. İhtiyaçları toplarken ve doğrularken şu yöntemler birbirini tamamlar:

- **Görüşme:** Süreç sahipleri ve kullanıcılarla yapılan görüşmeler, mevcut sorunları ve beklentileri ortaya çıkarır. Yalnızca yöneticilerle değil, işi her gün yapan çalışanlarla da görüşmek gerekir.
- **Gözlem:** Bir çalışanın işini yaparken izlenmesi, görüşmede söylenmeyen ara adımları, elle tutulan tabloları ve geçici çözümleri gösterir.
- **Belge ve veri incelemesi:** Mevcut formlar, raporlar ve sistem kayıtları, işlem hacimlerini ve istisnaların sıklığını gösterir.
- **Atölye çalışması:** Farklı birimlerin bir araya geldiği oturumlar, birimler arası çelişkili beklentileri erkenden görünür kılar.

**Doğrulama.** Yazılan ihtiyaçlar, sahibine geri okutulmalı ve onaylatılmalıdır. Kabul kriterleri, test senaryolarının temelini oluşturur; bu nedenle test ekibinin ihtiyaçları erken aşamada okuması, belirsiz ifadeleri yakalamaya yardımcı olur. BABOK'ta da vurgulandığı gibi, ihtiyaçların hangi iş hedefine hizmet ettiği izlenebilir olmalıdır.

**Kapsam kayması.** Proje ilerledikçe yeni istekler gelir. Her yeni isteğin bir değişiklik talebi olarak kaydedilmesi, önceliklendirilmesi ve maliyet ile takvim etkisinin değerlendirilmesi gerekir. Bu disiplin olmadan, öncelikli ihtiyaçlar küçük isteklerin arasında kaybolur.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b3.py` ile yapılmıştır.

Bir üretici, saha satış uygulaması seçimi için 140 ihtiyaç topluyor ve önceliklendiriyor:

| Öncelik | Adet | Pay |
|---|---|---|
| Must | 46 | %32,9 |
| Should | 52 | %37,1 |
| Could | 30 | %21,4 |
| Won't | 12 | %8,6 |

Bir "Must" örneği: "Satış temsilcisi olarak, bağlantı yokken sipariş alabilmek istiyorum; böylece kırsal rotalarda satış kaybetmem." Kabul kriteri: "Çevrimdışı alınan sipariş, bağlantı geldiğinde 5 dakika içinde ERP'ye aktarılır ve kopya kayıt oluşmaz." Tedarikçilere yalnızca "Must" maddeler için canlı demo isteniyor.

## Sık yapılan hatalar

- Her şeyi "Must" yapmak; öncelik anlamını yitirir.
- Mevcut sistemin ekranlarını ihtiyaç olarak kopyalamak.
- Kabul kriteri yazmamak; tedarikçinin "evet"i doğrulanamaz.
- İhtiyaçları yalnızca BT'nin toplaması, kullanıcıları dinlememek.

## Pratikte nasıl uygulanır?

- [ ] İhtiyaçları süreç adımlarından türetin ve her birine sahip atayın.
- [ ] Her ihtiyaç için en az bir kabul kriteri yazın.
- [ ] MoSCoW ile önceliklendirin; "Must" payını sınırlı tutun.
- [ ] "Must" maddeleri tedarikçi demolarında senaryo olarak test edin.

## Daha fazlası

- IIBA, BABOK Guide v3 (kitap; içerik doğrulanmadı): https://www.iiba.org/business-analysis-certifications/cbap/
