---
id: kb-ea-28-4-card-virtual-pos
title: "Kart ödemeleri ve sanal POS: Komisyon, valör ve mutabakat"
summary: "Fiziki ve sanal POS ile kart tahsilatının işleyişini, komisyon ve valör kavramlarını, banka hesap ekstresiyle mutabakatı ve kart verisinin güvenliği için PCI DSS standardının önemini anlatır."
course: ea
category: e-belge-ve-odeme
tags: [sanal-pos, kart, komisyon, valor, pci-dss]
roles: [finans-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-28.4]
reading_minutes: 2
key_points:
  - "Kart tahsilatı, banka komisyonu düşülerek ve belirli bir valörle hesaba geçer."
  - "Sanal POS, internet ve uzaktan ödemelerde kullanılan bankaya bağlı ödeme altyapısıdır."
  - "Her tahsilat banka ekstresindeki net tutarla eşleştirilmelidir."
  - "Kart bilgisi saklayan veya işleyen sistemler PCI DSS gereksinimlerine uymalıdır."
  - "Kart verisini kendi sisteminizde tutmamak riski en çok azaltan yoldur."
glossary_terms: [sanal-pos, valor, pci-dss]
related: [kb-ea-28-3-pos-okc, kb-ea-38-1-payment-systems-tr, kb-ea-28-2-b2b-ordering-portals, kb-ea-20-2-order-to-cash]
sources:
  - title: "PCI Security Standards Council"
    authors: "PCI SSC"
    year: 2026
    type: web
    url: "https://www.pcisecuritystandards.org/"
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

Bayiler kartla ödemeyi giderek daha çok tercih ediyor. Kart tahsilatı nakitten daha güvenlidir ama komisyon, valör ve mutabakat işleri getirir. Bu kart, kart ödemelerinin muhasebe ve sistem tarafını anlatır.

## Temel fikir

**Fiziki ve sanal POS.**

- **Fiziki POS:** Kartın cihaza okutulduğu terminal (mağaza, saha mobil POS).
- **Sanal POS:** İnternet sitesi, B2B portal veya ödeme linki üzerinden kartla ödeme altyapısı. Banka veya ödeme kuruluşu tarafından sağlanır.

**Komisyon.** Banka, her işlemden bir oran veya sabit tutar keser. Taksitli işlemlerde oran genellikle yükselir.

**Valör.** Tahsilatın hesaba geçme süresidir. Anlaşmaya göre ertesi gün veya daha uzun olabilir; erken valör genellikle daha yüksek komisyonla gelir.

**Mutabakat.** Her kart tahsilatı:

- Müşterinin cari hesabından brüt tutarla düşülür,
- Banka hesabına net tutarla girer,
- Aradaki fark komisyon gideri olarak kaydedilir.

Bu eşleştirme otomatik yapılmazsa açık kalemler birikir.

**Güvenlik ve PCI DSS.** Kart verisini saklayan, işleyen veya ileten sistemler, kart şemalarının kurduğu PCI Güvenlik Standartları Konseyi'nin PCI DSS standardına uymalıdır. En pratik yol, kart verisini kendi sisteminize hiç almamaktır: ödeme sayfasını ödeme kuruluşuna yönlendirmek ve sisteminizde yalnızca işlem numarasını tutmak.

### Kart tahsilatını yönetmek

Kartla tahsilat arttıkça, komisyon ve mutabakat yükü de büyür. Finans ve satış ekiplerinin birlikte yönetmesi gereken başlıca konular şunlardır:

- **Komisyonu kime yansıtacaksınız?** Kartla ödeme yapan bayiye ek maliyet yansıtılıp yansıtılmayacağı, ticari politika ve sözleşme koşullarıyla birlikte değerlendirilmelidir. Taksitli satışlarda vade farkı hesabı açıkça tanımlanmalıdır.
- **Banka seçimi ve yönlendirme:** Birden fazla bankayla çalışılıyorsa, işlemin hangi bankaya yönlendirileceği maliyet, valör ve onay oranına göre belirlenebilir. Ancak her ek banka, mutabakat yükünü de artırır.
- **Ters ibraz (chargeback) süreci:** Kart sahibinin itiraz ettiği işlemler için belge sunma süresi sınırlıdır. Teslimat belgeleri ve sipariş kayıtları hızlıca bulunabilmelidir.
- **Mutabakat otomasyonu:** Banka ekstresi, POS raporları ve ERP'deki tahsilat kayıtları günlük olarak eşleştirilmelidir. Komisyon ve iade kesintileri ayrı hesaplarda izlenmelidir.
- **Kart verisinin korunması:** Kart numarası sizin sistemlerinizde saklanmamalıdır. Sanal POS çözümlerinde ödeme sayfası bankada veya ödeme kuruluşunda barındırılırsa, kart verisi güvenliği yükü büyük ölçüde azalır. Tekrarlayan ödemelerde ödeme kuruluşunun sunduğu kart saklama hizmetleri kullanılmalıdır.

**Ölçüm.** Kanal bazında tahsilat payı, ortalama komisyon oranı, valör süresi ve eşleştirilemeyen işlem sayısı aylık olarak izlenmelidir. Bu göstergeler, banka sözleşmelerinin yenilenmesinde pazarlık için de veri sağlar.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b6.py` ile yapılmıştır.

Bir distribütör B2B portalında ayda 1.000.000 TL kartla tahsilat yapıyor. Varsayımsal %2,5 komisyonla aylık maliyet **25.000,00 TL**. Muhasebe ekibi, banka ekstresindeki net tutarları cari hesaplarla otomatik eşleştiren bir kural kuruyor; ay sonunda açık kalan kalemler yalnızca iade ve iptaller oluyor.

## Sık yapılan hatalar

- Kart tahsilatını banka ekstresi yerine POS fişinden kaydetmek.
- Komisyon giderini ayrı izlememek.
- Kart numaralarını kendi veritabanında veya e-postalarda tutmak.
- Taksitli satışların gerçek maliyetini fiyata yansıtmamak.

## Pratikte nasıl uygulanır?

- [ ] Kullandığınız tüm POS ve sanal POS anlaşmalarını, oranları ve valörleri listeleyin.
- [ ] Banka ekstresi ile otomatik eşleştirme kurun.
- [ ] Kart verisinin sisteminize girmediğini doğrulayın.
- [ ] Komisyon oranlarını yılda bir yeniden pazarlık edin.

## Daha fazlası

- PCI Security Standards Council: https://www.pcisecuritystandards.org/
