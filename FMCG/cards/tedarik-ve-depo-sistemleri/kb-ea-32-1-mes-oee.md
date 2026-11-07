---
id: kb-ea-32-1-mes-oee
title: "Üretim yürütme sistemi (MES) ve toplam ekipman etkinliği (OEE)"
summary: "Üretim hattından anlık veri toplayan MES sistemlerinin rolünü, ERP ile ilişkisini ve kullanılabilirlik, performans ve kalite çarpımından oluşan OEE göstergesinin nasıl hesaplandığını anlatır."
course: ea
category: tedarik-ve-depo-sistemleri
tags: [mes, oee, uretim, kayip-analizi]
roles: [uretici-sahibi, uretici-yonetici, depo-lojistik-muduru]
level: orta
source_lessons: [EA-32.1]
reading_minutes: 2
key_points:
  - "ERP ne üretileceğini planlar, MES üretimin hatta nasıl gerçekleştiğini izler."
  - "OEE, kullanılabilirlik, performans ve kalite oranlarının çarpımıdır."
  - "Kullanılabilirlik duruşları, performans yavaş çalışmayı, kalite hatalı ürünü yansıtır."
  - "Duruş nedenlerinin kodlanması iyileştirmenin başlangıcıdır."
  - "OEE, makineler arası karşılaştırmadan çok aynı makinenin zaman içindeki gelişimi için anlamlıdır."
glossary_terms: [mes, oee]
related: [kb-ea-32-4-asset-maintenance, kb-ea-32-2-food-safety-traceability, kb-ea-29-3-drp-inventory-planning]
sources:
  - title: "Introduction to TPM: Total Productive Maintenance"
    authors: "Nakajima, S."
    year: 1988
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

Üretim yapan bir firmada ERP, iş emrini ve malzeme ihtiyacını bilir; ama hattın gün içinde kaç dakika durduğunu bilmez. Bu kart, **üretim yürütme sistemlerinin** (MES) bu boşluğu nasıl doldurduğunu ve OEE göstergesini anlatır.

## Temel fikir

**MES ne yapar?**

- İş emirlerini ERP'den alır, hatta başlatır ve bitirir.
- Makinelerden veya operatör ekranından üretim adedi, duruş ve hata verisi toplar.
- Hangi partinin hangi hammaddeyle üretildiğini kaydeder.
- Gerçekleşen üretimi ve tüketimi ERP'ye bildirir.

**OEE (toplam ekipman etkinliği).** Nakajima'nın toplam verimli bakım yaklaşımında tanımlanan göstergedir:

- **Kullanılabilirlik** = Çalışma süresi / Planlı üretim süresi
- **Performans** = (Üretilen adet × ideal çevrim süresi) / Çalışma süresi
- **Kalite** = Sağlam adet / Üretilen adet
- **OEE** = Kullanılabilirlik × Performans × Kalite

Her bileşen ayrı bir kayıp türünü gösterir: duruşlar, yavaş çalışma ve hatalı ürün.

**Duruş kodları.** Operatörün her duruşa bir neden seçmesi (arıza, ürün değişimi, malzeme bekleme) iyileştirme çalışmasının veri tabanını oluşturur.

### OEE'yi doğru kullanmak

OEE güçlü bir göstergedir, ancak yanlış kullanıldığında yanıltıcı olabilir. Dikkat edilmesi gereken noktalar şunlardır:

- **Planlı süre tanımı:** Kullanılabilirlik hesabında temel alınan süre, toplam takvim süresi mi yoksa planlı üretim süresi mi? Planlı bakım ve vardiya dışı zamanın nasıl ele alınacağı yazılı olmalıdır; aksi hâlde hatlar ve dönemler karşılaştırılamaz.
- **İdeal hız:** Performans oranı, makinenin teorik hızına göre hesaplanır. Bu hız ürün bazında doğru tanımlanmazsa, farklı ürün üreten hatların OEE değerleri anlamsızlaşır.
- **Tek sayıya indirgemek:** OEE, üç oranın çarpımıdır. Aynı OEE değeri, düşük kullanılabilirlik veya düşük kalite gibi çok farklı sorunlardan kaynaklanabilir. Bu nedenle iyileştirme kararı için üç bileşen ayrı ayrı izlenmelidir.

**Duruş nedenlerini toplamak.** MES'in en büyük katkısı, duruşların anında ve sınıflandırılmış olarak kaydedilmesidir. Elle tutulan kayıtlarda kısa duruşlar genellikle hiç yazılmaz; oysa bunların toplamı büyük bir kayıp olabilir. Duruş kodları az sayıda, anlaşılır ve operatörün kolayca seçebileceği biçimde tasarlanmalıdır.

**ERP ile bağlantı.** Üretim emirleri ERP'den MES'e iner; gerçekleşen miktar, fire ve tüketilen malzeme MES'ten ERP'ye döner. Bu bağlantı kopuksa stok ve maliyet verisi gecikmeli ve hatalı olur. Parti numaralarının da bu akışta taşınması, izlenebilirliğin üretim adımını tamamlar.

Nakajima'nın toplam üretken bakım yaklaşımında OEE, bakım ve üretim ekiplerinin ortak dili olarak konumlanır; gösterge tek başına bir hedef değil, kayıpları görünür kılmanın aracıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b7.py` ile yapılmıştır.

Bir hatta 480 dakikalık vardiyada 60 dakika duruş var; kullanılabilirlik **%87,5**. Dakikada 1 adet ideal hızla çalışan hat 378 adet üretiyor; performans **%90,0**. 370 adet sağlam; kalite **%97,9**. OEE **%77,1**. En büyük kayıp duruşlar olduğu için ekip ürün değişim süresine odaklanıyor.

## Sık yapılan hatalar

- OEE'yi tek bir rakam olarak izleyip bileşenlere bakmamak.
- Duruş nedenlerini kodlamamak.
- Planlı duruşları ve planlı üretim süresini net tanımlamamak.
- MES verisini ERP'ye aktarmayıp çift giriş yapmak.

## Pratikte nasıl uygulanır?

- [ ] Planlı üretim süresi ve ideal çevrim süresini hat bazında tanımlayın.
- [ ] Duruş nedenleri listesi oluşturun.
- [ ] OEE ve üç bileşenini vardiya bazında raporlayın.
- [ ] En büyük kayıp için aylık iyileştirme hedefi koyun.

## Daha fazlası

- Nakajima, *Introduction to TPM* (kitap; doğrulanmadı).
