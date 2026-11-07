---
id: kb-ea-32-2-food-safety-traceability
title: "Gıda güvenliği ve parti izlenebilirliği: Sistem gereksinimleri"
summary: "Gıda ve içecek işletmelerinde hammaddeden müşteriye parti izlenebilirliğinin sistemde nasıl kurulduğunu, gıda güvenliği yönetim sistemlerinin kayıt beklentilerini ve geri çağırma sürecini anlatır."
course: ea
category: tedarik-ve-depo-sistemleri
tags: [gida-guvenligi, izlenebilirlik, parti, geri-cagirma]
roles: [uretici-sahibi, uretici-yonetici, depo-lojistik-muduru]
level: orta
source_lessons: [EA-32.2]
reading_minutes: 3
key_points:
  - "Gıda zincirinde her işletme, ürünü kimden aldığını ve kime verdiğini gösterebilmelidir."
  - "Parti izlenebilirliği hammadde partisinden ürün partisine ve müşteriye kadar kayıt zinciri ister."
  - "Gıda güvenliği yönetim sistemleri kayıtların düzenli tutulmasını ve denetlenebilir olmasını bekler."
  - "Geri çağırma hızı, sistemdeki parti kayıtlarının bütünlüğüne bağlıdır."
  - "Yasal yükümlülükler için güncel mevzuat ve resmi kurum kaynakları esas alınmalıdır."
glossary_terms: [izlenebilirlik, geri-cagirma, parti-takibi]
related: [kb-ea-30-4-barcodes-traceability, kb-ea-32-1-mes-oee, kb-ea-34-1-purchasing-supplier-management]
sources:
  - title: "Tarım ve Orman Bakanlığı Gıda ve Kontrol Genel Müdürlüğü"
    authors: "T.C. Tarım ve Orman Bakanlığı"
    year: 2026
    type: web
    url: "https://www.tarimorman.gov.tr/GKGM"
    verified: true
    checked_on: 2026-10-28
    note: "URL HTTP 200 ile açıldı, başlık/kurum eşleşti (2026-10-28)."
  - title: "ISO 22000 Food safety management"
    authors: "ISO"
    year: 2018
    type: web
    url: "https://www.iso.org/iso-22000-food-safety-management.html"
    verified: false
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Gıda ve içecek işletmelerinde bir partideki sorun, insan sağlığını ve markayı doğrudan etkiler. Bu kart, izlenebilirliğin sistemde nasıl kurulacağını ve hangi kayıtların tutulması gerektiğini genel hatlarıyla anlatır.

## Temel fikir

**Bir adım geri, bir adım ileri.** Gıda zincirinde yaygın ilke, her işletmenin ürünü kimden aldığını ve kime verdiğini gösterebilmesidir. Sistem açısından bu üç kayıt halkası demektir:

1. **Mal kabul:** Tedarikçi, hammadde partisi, kabul tarihi.
2. **Üretim:** Hangi hammadde partilerinin hangi ürün partisinde kullanıldığı.
3. **Sevkiyat:** Hangi ürün partisinin hangi müşteriye, hangi irsaliyeyle gittiği.

**Gıda güvenliği yönetim sistemleri.** ISO 22000 gibi standartlar, tehlike analizini ve kayıtların düzenli, denetlenebilir tutulmasını bekler. ERP, MES veya WMS bu kayıtların ana kaynağıdır.

**Geri çağırma süreci:**

- Sorunlu partinin tespiti,
- Geriye doğru: hangi hammaddeler, hangi diğer partiler etkilenmiş olabilir,
- İleriye doğru: hangi müşterilere gitmiş,
- Müşterilerin bilgilendirilmesi ve ürünün toplanması,
- Resmi kurumlara bildirim (mevzuata göre).

### İzlenebilirliği sistemde kurmak

İzlenebilirlik, yalnızca bir yazılım özelliği değil; mal kabulden sevkiyata kadar her adımda parti bilgisinin eksiksiz kaydedilmesi disiplinidir. Sistem tasarımında dikkat edilmesi gereken noktalar şunlardır:

- **Mal kabulde parti kaydı:** Tedarikçiden gelen her teslimatta parti numarası ve son kullanma tarihi kaydedilmelidir. Tedarikçinin parti bilgisini barkodla göndermesi, elle girişi ve hatayı azaltır.
- **Depo içi hareketler:** Lokasyon değişiklikleri, paketleme ve bölme işlemleri sırasında parti bilgisi korunmalıdır. Farklı partilerin aynı lokasyonda karıştırılması, izlenebilirliği zayıflatır.
- **Sevkiyatta okutma:** Hangi partinin hangi müşteriye gönderildiği, sevkiyat sırasında okutularak kaydedilmelidir. Bu adım atlanırsa geri çağırmada geniş bir müşteri grubunu kapsamak gerekir.
- **İadeler:** Müşteriden dönen ürünlerin partisi tespit edilmeli ve kalite kontrolünden geçmeden tekrar satışa açılmamalıdır.

**Geri çağırma tatbikatı.** Sistemin gerçekten çalıştığını görmenin en iyi yolu, düzenli aralıklarla bir parti seçerek tatbikat yapmaktır: Bu parti kimden geldi, hangi depolarda bulunuyor, hangi müşterilere gitti? Cevapların ne kadar sürede ve ne kadar eksiksiz bulunduğu ölçülmelidir.

**Kayıtların saklanması.** İzlenebilirlik kayıtlarının, ürünün raf ömrü ve ilgili mevzuatın öngördüğü süre boyunca erişilebilir tutulması gerekir. Gıda güvenliği yönetim sistemi belgelendirmesi olan şirketlerde, bu kayıtlar denetimlerin de konusudur. Uygulamadaki güncel yükümlülükler için hukuk danışmanınıza ve gıda mevzuatı uzmanınıza başvurmanız önerilir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b7.py` ile yapılmıştır.

Bir tedarikçi, gönderdiği 1 hammadde partisinde sorun bildiriyor. Üretim kayıtları bu partinin 3 ürün partisinde kullanıldığını, sevkiyat kayıtları ise bu partilerin 14 müşteriye gittiğini gösteriyor. Şirket aynı gün yalnızca bu 14 müşteriyle iletişime geçiyor.

## Sık yapılan hatalar

- Üretimde hammadde partisini kaydetmemek.
- Parti bilgisini kâğıt formlarda tutmak.
- Geri çağırma tatbikatı yapmamak.
- Tedarikçilerin izlenebilirlik kayıtlarını sorgulamamak.

## Pratikte nasıl uygulanır?

- [ ] Mal kabul, üretim ve sevkiyatta parti kaydını zorunlu yapın.
- [ ] Bir partinin geriye ve ileriye izini süren raporu hazırlayın.
- [ ] Yılda en az bir geri çağırma tatbikatı yapın.
- [ ] Yükümlülükleri uzman desteğiyle güncel mevzuata göre doğrulayın.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın. Gıda mevzuatından doğan kayıt ve geri çağırma yükümlülükleri için gıda hukuku konusunda uzman bir avukat veya danışmana danışın.

## Daha fazlası

- T.C. Tarım ve Orman Bakanlığı Gıda ve Kontrol Genel Müdürlüğü: https://www.tarimorman.gov.tr/GKGM
- ISO 22000 (doğrulanmadı): https://www.iso.org/iso-22000-food-safety-management.html
