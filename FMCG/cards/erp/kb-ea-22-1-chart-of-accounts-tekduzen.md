---
id: kb-ea-22-1-chart-of-accounts-tekduzen
title: "ERP'nin muhasebe motoru: Tekdüzen hesap planı ve hesap eşleştirme"
summary: "ERP'de Tekdüzen hesap planının nasıl kurulduğunu, satış, satın alma ve stok işlemlerinin hesap eşleştirme kurallarıyla genel muhasebeye nasıl aktarıldığını ve çift taraflı kayıt kuralının sistemde bir kısıt olarak nasıl korunduğunu anlatır."
course: ea
category: erp
tags: [erp, muhasebe, tekduzen, hesap-plani]
roles: [finans-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-22.1]
reading_minutes: 2
key_points:
  - "Tekdüzen hesap planı ana hesapları belirler; firma alt hesaplarla kendi ihtiyacına göre ayrıntılandırır."
  - "Hesap eşleştirme, bir işlemin hangi hesaplara gideceğini otomatik belirleyen kurallardır."
  - "Her kayıtta borç ve alacak toplamı eşit olmalıdır; ERP bunu bir kısıt olarak uygular."
  - "Yardımcı defterlerin toplamı genel muhasebedeki kontrol hesabıyla her zaman tutmalıdır."
  - "Hesap planındaki değişiklikler raporları etkiler; kontrollü yapılmalıdır."
glossary_terms: [tekduzen-hesap-plani, hesap-eslestirme, genel-muhasebe]
related: [kb-ea-20-4-record-to-report-close, kb-ea-20-2-order-to-cash, kb-ea-22-2-multi-currency-inflation-adjust-in-erp, kb-eco-43-4-kdv-vat]
sources:
  - title: "Muhasebe Sistemi Uygulama Genel Tebliği (Tekdüzen Hesap Planı)"
    authors: "T.C. Cumhurbaşkanlığı Mevzuat Bilgi Sistemi"
    year: 1992
    type: law
    url: "https://www.mevzuat.gov.tr/"
    verified: true
    checked_on: 2026-10-28
  - title: "Integrated Business Processes with ERP Systems"
    authors: "Magal, S. R.; Word, J."
    year: 2011
    type: book
    verified: false
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

ERP'de satış ekibi fatura keser, depo sevkiyat yapar; ama hiçbiri muhasebe kaydı yazmaz. Kayıtlar arka plandaki **muhasebe motoru** tarafından oluşturulur. Bu kart, motorun nasıl çalıştığını ve kurulumda nelere dikkat edilmesi gerektiğini anlatır.

## Temel fikir

**Tekdüzen hesap planı.** Türkiye'de bilanço esasına göre defter tutan işletmeler, Muhasebe Sistemi Uygulama Genel Tebliği ile belirlenen Tekdüzen hesap planını kullanır. Ana hesaplar (ör. 120 Alıcılar, 153 Ticari Mallar, 600 Yurt İçi Satışlar) sabittir; firma bunları alt hesaplarla ayrıntılandırır.

**Hesap eşleştirme.** ERP'de her işlem tipi için "hangi hesaba gidecek?" kuralı tanımlanır. Örneğin:

- Satış faturası: müşteri hesabı borç, satış hesabı ve hesaplanan KDV alacak.
- Mal kabul: stok hesabı borç, mal kabul–fatura ara hesabı alacak.
- Satış sevkiyatı: satılan malın maliyeti borç, stok alacak.

Kurallar ürün grubu, müşteri grubu veya depo bazında farklılaşabilir. Bu esneklik, kanal veya ürün grubu bazında kârlılık raporu almayı mümkün kılar.

**Çift taraflı kayıt bir kısıttır.** Her kayıtta borç toplamı alacak toplamına eşit olmalıdır. ERP dengesiz bir kaydı kaydetmez. Ayrıca müşteri cari hesaplarının toplamı, genel muhasebedeki 120 hesabının bakiyesiyle tutmalıdır. Bu tutarlılık, yardımcı defterlerden genel muhasebeye otomatik aktarımla sağlanır; elle yapılan kayıtlar ise riski artırır.

### Hesap planının bakımı

Hesap planı zamanla gereksiz alt hesaplarla dolabilir. Yeni hesap açma talepleri finans ekibinin onayından geçmeli; ihtiyaç mümkünse masraf merkezi, proje veya ürün grubu gibi ek boyutlarla karşılanmalıdır. Böylece hesap planı sade kalır, analiz ise boyutlar üzerinden yapılır. Hesap eşleştirme tablolarında yapılan değişiklikler de kayıt altına alınmalı ve yürürlük tarihleriyle yönetilmelidir; aksi hâlde aynı işlem farklı dönemlerde farklı hesaplara gider. Mevzuattaki değişikliklerin hesap planına etkisi için mali müşavirinizle düzenli görüşmeniz önerilir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b5.py` ile yapılmıştır. KDV oranı örnek olarak %20 alınmıştır.

Bir bayi 10.000,00 TL + KDV tutarında satış faturası kesiyor. ERP şu kaydı otomatik oluşturuyor:

- 120 Alıcılar: borç **12.000,00 TL**
- 600 Yurt İçi Satışlar: alacak **10.000,00 TL**
- 391 Hesaplanan KDV: alacak **2.000,00 TL**

Borç ve alacak farkı **0,00**. Satış ekibi bu kaydı hiç görmüyor; ama eşleştirme kuralı yanlış kurulsaydı (ör. tüm satışlar tek bir alt hesaba gitseydi), kanal bazlı ciro raporu alınamayacaktı.

## Sık yapılan hatalar

- Alt hesapları raporlama ihtiyacını düşünmeden açmak.
- Eşleştirme kurallarını test etmeden canlıya geçmek.
- Kontrol hesaplarına (ör. 120, 320) elle kayıt atılmasına izin vermek.
- Hesap planını yıl ortasında kontrolsüz değiştirmek.

## Pratikte nasıl uygulanır?

- [ ] Yönetim raporlarınızın hangi kırılımları istediğini yazın ve alt hesapları buna göre tasarlayın.
- [ ] Her işlem tipi için örnek kayıtları test ortamında mali müşavirinizle kontrol edin.
- [ ] Kontrol hesaplarına elle kaydı yetkiyle kısıtlayın.
- [ ] Yardımcı defter–genel muhasebe uyumunu her ay kontrol edin.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın. Hesap kodları ve KDV oranı örnek amaçlıdır; kendi hesap planınızı mali müşavirinizle kontrol edin.

## Daha fazlası

- Muhasebe Sistemi Uygulama Genel Tebliği: https://www.mevzuat.gov.tr/
- Magal ve Word, *Integrated Business Processes with ERP Systems* (kitap; doğrulanmadı).
