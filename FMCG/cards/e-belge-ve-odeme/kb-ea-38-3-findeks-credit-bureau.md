---
id: kb-ea-38-3-findeks-credit-bureau
title: "Kredi bürosu verisi: KKB ve Findeks"
summary: "Kredi Kayıt Bürosu ve Findeks gibi risk verisi kaynaklarını, bu verilerin bayi kredi limiti ve tahsilat süreçlerinde nasıl kullanılabileceğini ve kişisel veri açısından dikkat edilecek noktaları anlatır."
course: ea
category: e-belge-ve-odeme
tags: [kkb, findeks, kredi-riski, bayi, limit]
roles: [bayi-sahibi, bayi-yonetici, finans-muduru]
level: orta
source_lessons: [EA-38.3]
reading_minutes: 2
key_points:
  - "KKB, bankacılık sektörünün kredi ve risk verisini paylaştığı kuruluştur."
  - "Findeks, KKB'nin kişi ve firmalara yönelik risk raporu ve hizmet platformudur."
  - "Büro verisi, bayi kredi limiti kararında iç verilerle birlikte kullanılabilir."
  - "Rapor alımı için ilgili tarafın onayı ve kişisel veri kurallarına uyum gerekir."
  - "Büro verisi tek başına karar vermez; ödeme geçmişi ve saha bilgisiyle birleştirilmelidir."
glossary_terms: [kredi-burosu, risk-raporu]
related: [kb-ea-24-3-credit-limits-collections-systems, kb-ea-38-1-payment-systems-tr, kb-ea-20-2-order-to-cash]
sources:
  - title: "Kredi Kayıt Bürosu"
    authors: "KKB"
    year: 2026
    type: web
    url: "https://www.kkb.com.tr/"
    verified: true
    checked_on: 2026-10-28
    note: "URL HTTP 200 ile açıldı, başlık/kurum eşleşti (2026-10-28)."
  - title: "Findeks"
    authors: "KKB"
    year: 2026
    type: web
    url: "https://www.findeks.com/"
    verified: true
    checked_on: 2026-10-28
    note: "URL HTTP 200 ile açıldı, başlık/kurum eşleşti (2026-10-28)."
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28

---

## Ne işe yarar?

Bayilere vadeli satış yapan bir dağıtıcının en büyük risklerinden biri tahsil edilemeyen alacaktır. Kendi ödeme geçmişiniz yalnızca sizinle olan ilişkiyi gösterir. Kredi bürosu verisi, bayinin diğer finansal yükümlülüklerine dair ek bir görüş sağlar.

## Temel fikir

- **KKB (Kredi Kayıt Bürosu):** Bankalar ve finans kuruluşlarının kredi ve risk verilerini paylaştığı kuruluştur.
- **Findeks:** KKB'nin bireylere ve firmalara risk raporu, kredi notu ve çek raporu gibi hizmetler sunduğu platformdur.

**Kredi sürecinde kullanım:**

1. Yeni bayi başvurusunda onay alınarak risk raporu istenir.
2. Rapor, iç verilerle (sipariş geçmişi, ödeme performansı, saha ziyaret notları) birlikte değerlendirilir.
3. Limit önerisi ERP'deki kredi limiti alanına onay akışıyla girilir.
4. Belirli aralıklarla veya risk sinyalinde yeniden değerlendirme yapılır.

**Uyum:** Rapor alımı, ilgili tarafın onayına ve kişisel veri mevzuatına uygun olmalıdır. Raporların kimlerin görebileceği rol bazında sınırlanmalıdır.

### Kredi sürecinde büro verisinin yeri

Büro verisi, kredi kararını destekleyen bir girdidir; tek başına karar mekanizması değildir. Sağlıklı bir bayi kredi süreci genellikle şu bileşenlerden oluşur:

- **Kimlik ve belge kontrolü:** Vergi levhası, imza sirküleri ve ticaret sicil bilgileri gibi temel belgelerin doğrulanması.
- **İç veri:** Sizinle olan sipariş geçmişi, ödeme performansı, iade oranı ve çek veya senet geçmişi.
- **Dış veri:** Kredi bürosu raporu ve, mümkünse, sektördeki diğer tedarikçilerden alınan referanslar.
- **Saha bilgisi:** Temsilcinin noktanın büyüklüğü, konumu ve işleyişi hakkındaki gözlemleri.
- **Teminat:** Doğrudan borçlandırma sistemi, banka teminat mektubu veya kefalet gibi güvenceler.

**Puanlama tablosu.** Bu bileşenler, ağırlıkları önceden belirlenmiş basit bir puanlama tablosuyla birleştirilebilir. Puan aralıklarına göre limit önerisi ve onay seviyesi belirlenir. Böylece kararlar kişiden kişiye değişmez ve sonradan açıklanabilir.

**Erken uyarı.** Limit belirlendikten sonra da izleme sürmelidir. Ödeme gecikmelerinin artması, sipariş düzeninin bozulması veya büro raporunda olumsuz bir değişiklik, limitin yeniden değerlendirilmesi için sinyal olabilir. ERP'deki kredi limiti kontrolü, tahsilat hatırlatmalarıyla birlikte çalışmalıdır.

**Kişisel veri.** Şahıs işletmelerinde firma bilgisi ile kişisel bilgi iç içedir. Bu nedenle rapor alma, saklama ve paylaşma kuralları kişisel veri mevzuatı açısından ayrıca değerlendirilmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b8.py` ile yapılmıştır.

Bir dağıtıcı 200 bayinin yıllık gözden geçirmesini yapıyor. Büro verisi ve iç ödeme geçmişi birleştirildiğinde 30 bayi yüksek riskli çıkıyor: **%15,0**. Bu bayiler için limit azaltılmıyor, önce saha ekibiyle görüşme ve teminat seçenekleri değerlendiriliyor.

## Sık yapılan hatalar

- Büro puanını tek karar kriteri yapmak.
- Onay almadan rapor istemek.
- Raporları geniş bir ekiple e-postayla paylaşmak.
- Limiti bir kez belirleyip hiç güncellememek.

## Pratikte nasıl uygulanır?

- [ ] Bayi başvuru formuna rapor onayı ekleyin ve metni avukatınıza kontrol ettirin.
- [ ] Limit kararını iç veri ve büro verisini birleştiren bir puanlama tablosuna bağlayın.
- [ ] Rapor erişimini rol bazında sınırlayın.
- [ ] Yıllık ve sinyale dayalı gözden geçirme takvimi kurun.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın. Rapor alma onayı ve kişisel veri işleme için gereken izinleri mutlaka avukatınızla teyit edin.

## Daha fazlası

- KKB sitesi (doğrulanmadı).
- Findeks sitesi.
