---
id: kb-ea-33-3-incentive-compensation-systems
title: "Satış prim sistemleri: Kural, hesaplama ve itiraz"
summary: "Satış ekiplerinin prim planlarının sistemde nasıl tanımlandığını; hedef, gerçekleşme ve ödeme eğrisi mantığını, veri kaynaklarını, şeffaf hesaplama ve itiraz sürecini anlatır."
course: ea
category: saha-satis-ve-dms
tags: [prim, tesvik, satis-ekibi, hedef, odeme-egrisi]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: orta
source_lessons: [EA-33.3]
reading_minutes: 2
key_points:
  - "Prim planı hedef, ölçü, ağırlık ve ödeme eğrisinden oluşur."
  - "Ödeme eğrisi, gerçekleşme oranına göre ödenecek primi belirler; alt eşik ve üst sınır içerebilir."
  - "Prim hesabında kullanılan veri, satış raporlarıyla aynı kaynaktan gelmelidir."
  - "Temsilcinin kendi gerçekleşmesini dönem içinde görebilmesi motivasyonu artırır."
  - "İtiraz süreci yazılı ve süreli olmalıdır."
glossary_terms: [prim-plani, odeme-egrisi]
related: [kb-ea-33-1-hr-systems, kb-ea-33-2-payroll-basics, kb-ea-26-1-retail-execution-sfa, kb-ea-28-2-b2b-ordering-portals]
sources:
  - title: "Building a Winning Sales Force"
    authors: "Zoltners, A. A.; Sinha, P.; Lorimer, S. E."
    year: 2009
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

Satış primi Excel'de hesaplandığında hatalar, gecikmeler ve "benim rakamım yanlış" tartışmaları kaçınılmazdır. Bu kart, prim sistemlerinin temel yapısını anlatır.

## Temel fikir

**Prim planının parçaları:**

- **Ölçüler:** Ciro, hacim, yeni nokta, tahsilat, ürün dağılımı gibi.
- **Ağırlıklar:** Her ölçünün primdeki payı.
- **Hedefler:** Kişi veya bölge bazında.
- **Ödeme eğrisi:** Gerçekleşme oranına göre ödenecek prim. Ör. bir alt eşiğin altında prim yok, belirli bir üst sınırdan sonra artış yok.

Zoltners, Sinha ve Lorimer, prim planının basit, anlaşılır ve şirketin stratejisiyle uyumlu olmasının önemini vurgular.

**Sistem gereksinimleri:**

- Gerçekleşme verisi ERP veya SFA'dan otomatik gelmeli.
- Müşteri ve bölge atamaları dönem boyunca tarihli tutulmalı (devredilen müşteri kimin hedefine sayılır?).
- Temsilci kendi gerçekleşmesini dönem içinde görebilmeli.
- Hesaplama adım adım izlenebilir olmalı.

**İtiraz süreci.** Temsilcinin ne kadar süre içinde, hangi kanıtla itiraz edebileceği ve kimin karar vereceği yazılı olmalıdır.

### Prim planı tasarımında denge

Prim planı, satış ekibinin davranışını şirketin her yazılı politikasından daha güçlü yönlendirir. Bu nedenle tasarımda bazı dengeler gözetilmelidir:

- **Az sayıda ölçü:** Çok fazla ölçü primi anlaşılmaz kılar ve temsilcinin dikkatini dağıtır. Genellikle birkaç ana ölçü ve net ağırlıklar daha etkili olur.
- **Kontrol edilebilirlik:** Temsilci, ölçünün sonucunu kendi çabasıyla etkileyebilmelidir. Örneğin fiyat artışından gelen ciro artışı, temsilcinin performansını tam yansıtmaz.
- **Kârlılık ile hacim dengesi:** Yalnızca ciroya dayalı prim, aşırı iskonto ve vade verilmesini teşvik edebilir. Tahsilat veya brüt kâr gibi bir ölçünün eklenmesi bu riski azaltır.
- **Hedef belirleme:** Hedefin geçmiş performansa, pazar potansiyeline ve bölgedeki değişikliklere dayanması gerekir. Ulaşılamaz hedefler motivasyonu, çok kolay hedefler ise bütçeyi bozar.

**Sistemin şeffaflığı.** Temsilcinin dönem içinde gerçekleşmesini ve tahmini primini görmesi, dönem sonundaki itiraz sayısını azaltır. Hesaplamanın her adımı (hangi faturanın kime sayıldığı, hangi iadenin düşüldüğü) kayıt altında olmalıdır.

**Plan değişiklikleri.** Dönem ortasında kural değiştirmek güveni zedeler. Değişiklikler dönem başında, yazılı olarak ve örnek hesaplarla duyurulmalıdır.

### Primin açıklanabilirliği

Her temsilci, primini nasıl hesapladığını kendi ekranında görebilmelidir. Şeffaf hesaplama, itirazları ve güvensizliği azaltır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b7.py` ile yapılmıştır.

Bir temsilcinin çeyreklik ciro hedefi 1.000.000 TL, gerçekleşme 1.080.000 TL: **%108,0**. Plan, hedef primini (20.000 TL) gerçekleşme oranıyla çarpıyor ve bir üst sınır uyguluyor. Prim **21.600,00 TL**. Temsilci hesabı uygulamada satır satır görebildiği için itiraz gelmiyor.

## Sık yapılan hatalar

- Prim verisini satış raporlarından farklı kaynaktan almak.
- Müşteri devirlerini tarihli tutmamak.
- Primleri dönem kapandıktan aylar sonra açıklamak.
- Çok sayıda ölçü ekleyip primi anlaşılmaz hâle getirmek.
- Yalnızca ciroya prim verip iskonto ve vade artışını teşvik etmek.
- Dönem ortasında kuralları değiştirmek.
- Hesaplamayı tablolarda elle yapıp izlenemez bırakmak.

## Pratikte nasıl uygulanır?

- [ ] Plan başına en fazla birkaç ölçü kullanın.
- [ ] Ödeme eğrisini yazılı ve örnekli paylaşın.
- [ ] Gerçekleşmeyi temsilcilere haftalık gösterin.
- [ ] İtiraz süresini ve karar verecek kişiyi belirleyin.

## Daha fazlası

- Zoltners, Sinha ve Lorimer, *Building a Winning Sales Force* (kitap; doğrulanmadı).
