---
id: kb-ea-33-2-payroll-basics
title: "Bordro temelleri: Brütten nete ve sistem kontrolü"
summary: "Bordronun brüt ücretten kesintilerle nete nasıl ulaştığını genel mantıkla, bordro sisteminin girdilerini, yasal oran ve parametrelerin güncellenmesini ve bordro sonrası muhasebe ve bildirim adımlarını anlatır."
course: ea
category: vergi-ve-mevzuat
tags: [bordro, brut-net, sgk, gelir-vergisi, parametre]
roles: [uretici-sahibi, bayi-sahibi, finans-muduru]
level: orta
source_lessons: [EA-33.2]
reading_minutes: 2
key_points:
  - "Bordro, brüt ücretten sosyal güvenlik ve vergi kesintileri düşülerek net ücrete ulaşır."
  - "Oranlar, tavanlar ve istisnalar mevzuatla sık değişir; sistem parametreleri her dönem kontrol edilmelidir."
  - "Puantaj, izin ve ek ödemeler bordronun ana girdileridir."
  - "Bordro sonrası muhasebe kaydı, ödeme dosyası ve resmi bildirimler oluşturulur."
  - "Bordro sonuçları mali müşavir veya bordro uzmanıyla doğrulanmalıdır."
glossary_terms: [brut-ucret, net-ucret, bordro-parametresi]
related: [kb-ea-33-1-hr-systems, kb-ea-33-3-incentive-compensation-systems, kb-ea-22-1-chart-of-accounts-tekduzen]
sources:
  - title: "Sosyal Güvenlik Kurumu"
    authors: "SGK"
    year: 2026
    type: web
    url: "https://www.sgk.gov.tr/"
    verified: true
    checked_on: 2026-10-28
    note: "URL HTTP 200 ile açıldı, başlık/kurum eşleşti (2026-10-28)."
  - title: "Gelir İdaresi Başkanlığı"
    authors: "GİB"
    year: 2026
    type: web
    url: "https://www.gib.gov.tr/"
    verified: false
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Bordro hatası hem çalışan memnuniyetini hem de şirketin yasal yükümlülüklerini etkiler. Bu kart, bordronun genel mantığını ve bir yönetici olarak sistemde neyi kontrol etmeniz gerektiğini anlatır. Güncel oran ve tutarlar burada verilmez.

## Temel fikir

**Brütten nete genel akış:**

1. **Brüt ücret:** Sözleşmedeki ücret + ek ödemeler (fazla mesai, prim vb.).
2. **Çalışan sosyal güvenlik kesintileri:** Belirli oranlarda, tavanlar dahilinde.
3. **Vergi matrahı:** Brüt ücretten bu kesintiler düşülerek bulunur.
4. **Gelir vergisi ve damga vergisi:** Matrah ve yasal istisnalara göre hesaplanır.
5. **Net ücret:** Çalışana ödenen tutar.

Ayrıca işveren tarafında, çalışanın brüt ücretine eklenen işveren payları vardır; şirketin toplam maliyeti bu nedenle brüt ücretten yüksektir.

**Sistem açısından:**

- **Girdiler:** Puantaj, izin, ek ödemeler, kesintiler (avans, icra).
- **Parametreler:** Oranlar, tavanlar, vergi dilimleri, asgari ücret istisnası. Mevzuat değiştikçe güncellenmelidir.
- **Çıktılar:** Bordro pusulası, muhasebe kaydı, banka ödeme dosyası, resmi bildirimler.

### Bordro sürecinde kontrol ve güvenlik

Bordro hataları, hem çalışan memnuniyetini hem de yasal yükümlülükleri doğrudan etkiler. Sistem ve süreç açısından kurulması gereken kontroller şunlardır:

- **Parametre güncellemeleri:** Asgari ücret, vergi dilimleri, sigorta prim tavanı ve istisna tutarları gibi parametreler dönemsel olarak değişir. Her değişiklik, yürürlük tarihiyle birlikte sisteme girilmeli ve ikinci bir kişi tarafından kontrol edilmelidir. Güncel değerler için mali müşavirinize ve resmî kaynaklara başvurun.
- **Dönem karşılaştırması:** Her bordro döneminde, bir önceki aya göre büyük fark gösteren çalışanlar listelenmeli ve nedenleri incelenmelidir.
- **Puantaj girdisi:** Devamsızlık, fazla mesai ve izin bilgilerinin kaynağı ve onay akışı belli olmalıdır. Elle girilen puantaj, en sık hata kaynaklarından biridir.
- **Ödeme dosyası:** Bankaya gönderilen ödeme dosyasının toplamı, bordro toplamıyla karşılaştırılmalıdır. Banka hesap bilgisi değişiklikleri ayrıca onaydan geçmelidir.
- **Muhasebe kaydı:** Bordro sonuçları, gider ve borç hesaplarına doğru masraf merkezleriyle aktarılmalıdır.

**Erişim ve gizlilik.** Bordro verisi, şirketteki en hassas kişisel verilerdendir. Erişim, yalnızca ihtiyacı olan kişilerle sınırlandırılmalı; raporlar ve dışa aktarımlar kayıt altına alınmalıdır. Bordro hizmeti dışarıdan alınıyorsa, veri paylaşımının kapsamı ve güvenliği sözleşmede düzenlenmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar ve oranlar gerçek değildir, mevzuatı yansıtmaz; hesaplar `scripts/cards_numbers_ea_b7.py` ile yapılmıştır.

Brüt ücret 50.000 TL. Varsayımsal %15 çalışan kesintisi **7.500,00 TL**; matrah **42.500,00 TL**. Varsayımsal %15 vergiyle vergi **6.375,00 TL**. Net ücret **36.125,00 TL**. Gerçek bordroda tavanlar, dilimler ve istisnalar bu hesabı değiştirir.

## Sık yapılan hatalar

- Yıl başında ve ara dönemlerde parametre güncellemesini kontrol etmemek.
- Puantajı bordro kesiminden sonra değiştirmek.
- Bordro sonuçlarını önceki ayla karşılaştırmadan onaylamak.
- Bordro erişimini geniş bir gruba açmak.

## Pratikte nasıl uygulanır?

- [ ] Parametre değişikliklerini dönem başında kontrol listesiyle doğrulayın.
- [ ] Puantaj kesim tarihini belirleyin.
- [ ] Önceki aya göre büyük sapmaları kontrol edin.
- [ ] Sonuçları mali müşavir veya bordro uzmanıyla doğrulayın.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın. Bordro oranları, tavanları ve istisnaları sık değiştiği için hesaplamaları mutlaka mali müşaviriniz veya bordro uzmanınızla doğrulayın.

## Daha fazlası

- Sosyal Güvenlik Kurumu: https://www.sgk.gov.tr/
- Gelir İdaresi Başkanlığı (doğrulanmadı): https://www.gib.gov.tr/
