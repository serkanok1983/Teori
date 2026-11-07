---
id: kb-eco-43-3-corporate-tax
title: "Kurumlar vergisi: Ticari kârdan vergi matrahına"
summary: "Kurumlar vergisinin muhasebe kârından değil, kanunen kabul edilmeyen giderler ve istisnalarla düzeltilmiş matrah üzerinden hesaplandığını, efektif vergi oranının nasıl bulunduğunu ve geçici vergi uygulamasını anlatır."
course: eco
category: vergi-ve-mevzuat
tags: [vergi, kurumlar-vergisi, karlilik]
roles: [uretici-sahibi, bayi-sahibi, finans-muduru]
level: orta
source_lessons: [ECO-43.3]
reading_minutes: 3
key_points:
  - "Vergi matrahı = Ticari kâr + Kanunen kabul edilmeyen giderler − İstisna ve indirimler."
  - "Efektif vergi oranı, ödenen verginin muhasebe kârına oranıdır ve kanuni orandan farklı olabilir."
  - "Kurumlar vergisi yıl içinde geçici vergi dönemleriyle peşin ödenir."
  - "Kanunen kabul edilmeyen giderler belgelendirme ve harcama disiplinsizliğinin maliyetini gösterir."
glossary_terms: [kurumlar-vergisi, kkeg, efektif-vergi-orani, gecici-vergi]
related: [kb-eco-43-1-turkish-tax-system-overview, kb-eco-33-4-income-statement, kb-eco-35-2-inflation-accounting, kb-eco-43-6-tax-procedure-inspection]
sources:
  - title: "5520 sayılı Kurumlar Vergisi Kanunu"
    authors: "T.C. Resmî Gazete / Mevzuat Bilgi Sistemi"
    year: 2006
    type: law
    url: "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5520.pdf"
    verified: true
    checked_on: 2026-10-28
    note: "Mevzuat Bilgi Sistemi resmî PDF metni açıldı, kanun adı ve numarası eşleşti (2026-10-28)."
  - title: "193 sayılı Gelir Vergisi Kanunu"
    authors: "T.C. Resmî Gazete / Mevzuat Bilgi Sistemi"
    year: 1960
    type: law
    url: "https://www.mevzuat.gov.tr/MevzuatMetin/1.4.193.pdf"
    verified: true
    checked_on: 2026-10-28
    note: "Mevzuat Bilgi Sistemi resmî PDF metni açıldı, kanun adı ve numarası eşleşti (2026-10-28)."
  - title: "213 sayılı Vergi Usul Kanunu"
    authors: "T.C. Resmî Gazete / Mevzuat Bilgi Sistemi"
    year: 1961
    type: law
    url: "https://www.mevzuat.gov.tr/MevzuatMetin/1.4.213.pdf"
    verified: true
    checked_on: 2026-10-28
    note: "Mevzuat Bilgi Sistemi resmî PDF metni açıldı, kanun adı ve numarası eşleşti (2026-10-28)."
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28

---

## Ne işe yarar?

Şirketin ödeyeceği kurumlar vergisi, gelir tablosundaki kârın kanuni oranla çarpımı değildir. Bu kart, vergi matrahının nasıl bulunduğunu, efektif oranın neden farklılaştığını ve yıl içindeki peşin ödemelerin nakit planına etkisini anlatır.

## Temel fikir

Kurumlar vergisi 5520 sayılı Kurumlar Vergisi Kanunu ile düzenlenir.

**Matrah hesabı:**

1. **Ticari kâr:** Muhasebe kayıtlarındaki vergi öncesi kâr.
2. **+ Kanunen kabul edilmeyen giderler (KKEG):** Kayıtlarda gider yazılan ama vergi matrahından indirilemeyen tutarlar. Örneğin belgesiz giderler, vergi cezaları ve kanunda sayılan bazı diğer kalemler.
3. **− İstisna ve indirimler:** Kanunda sayılan, vergiden istisna edilen kazançlar ve indirimler.
4. **= Vergi matrahı** × kanuni oran = hesaplanan vergi.

**Efektif vergi oranı** = Hesaplanan vergi ÷ Ticari kâr.

**Geçici vergi:** Yıl içindeki dönem kârları üzerinden peşin vergi ödenir ve yıllık vergiden mahsup edilir.

### Ticari kâr ile vergi matrahı neden farklıdır?

Muhasebe kârı ile vergi matrahı arasındaki farklar iki türlüdür:

- **Kalıcı farklar:** Hiçbir zaman vergiden düşülemeyen giderler (ör. vergi cezaları) veya hiç vergilendirilmeyen istisna kazançlar.
- **Zamanlama farkları:** Gider veya gelirin muhasebe ve vergi açısından farklı dönemlerde dikkate alınması. Örneğin muhasebede ayrılan bazı karşılıkların vergi açısından ancak kanuni şartlar oluştuğunda indirilebilmesi.

TFRS veya BOBİ FRS ile finansal tablo hazırlayan şirketlerde zamanlama farkları **ertelenmiş vergi** olarak raporlanır.

### Yönetici neye dikkat etmeli?

- **Belge düzeni:** KKEG'in büyük kısmı belgesiz veya usulsüz belgeli giderlerden doğar. Her giderin fatura veya gider pusulası gibi geçerli bir belgeye dayanması vergi yükünü doğrudan azaltır.
- **İlişkili taraf işlemleri:** Ortaklara veya grup şirketlerine emsal bedel dışında yapılan satışlar, verilen faizsiz borçlar ve kiralamalar transfer fiyatlandırması veya örtülü kazanç dağıtımı riski doğurur.
- **Geçici vergi:** Yıl içi tahmini kârlar düşük gösterilirse fark ve ceza riski doğabilir. Yıl sonu tahmininizle geçici vergi beyanlarınızı uyumlu tutun.

## Bir örnek

> **Örnek (temsili rakamlar):** Tutarlar varsayımsaldır; vergi oranı **örnek oran**dır. Hesaplar `scripts/cards_numbers_eco_b6.py` ile yapılmıştır.

| Kalem | Tutar (TL) |
|---|---|
| Ticari kâr | 4.000.000 |
| + KKEG (belgesiz giderler, cezalar vb.) | 500.000 |
| − İstisna kazanç | 300.000 |
| **Vergi matrahı** | **4.200.000** |
| Hesaplanan vergi (örnek oran %25) | 1.050.000 |

Efektif oran %26,2, kanuni örnek oranın üzerinde. Farkın kaynağı KKEG: belgesiz harcamalar ve cezalar şirkete hem kendi tutarları hem de üzerlerindeki vergi kadar mal oluyor.

## Sık yapılan hatalar

- Vergi bütçesini ticari kâr × kanuni oran diye hesaplamak.
- Belgesiz harcamaların vergi maliyetini görmemek.
- Geçici vergi ödemelerini nakit planına almamak.
- İstisna ve teşviklerden, şartlarını kontrol etmeden yararlanmak.
- Enflasyon düzeltmesinin vergi matrahına etkisini mali müşavirle konuşmamak.
- Geçici vergi dönemlerinde tahakkuk ve karşılıkları ihmal edip yıl sonunda büyük farklarla karşılaşmak.

## Pratikte nasıl uygulanır?

- [ ] Ticari kârdan vergi matrahına geçiş tablosunu her çeyrek mali müşavirinizden isteyin.
- [ ] KKEG kalemlerini düzenli izleyin ve azaltılabilecek olanları belirleyin.
- [ ] Geçici vergi ödeme tarihlerini nakit akış tahminine ekleyin.
- [ ] Yararlanılabilecek istisna ve indirimleri yıl başında değerlendirin.
- [ ] Güncel oranı ve uygulama esaslarını Gelir İdaresi'nin resmî kaynaklarından kontrol edin.
- [ ] Her yıl KKEG listenizi çıkarın ve azaltılabilecek kalemleri mali müşavirinizle gözden geçirin.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın.

## Daha fazlası

- T.C. Resmî Gazete / Mevzuat Bilgi Sistemi (2006). *5520 sayılı Kurumlar Vergisi Kanunu*. https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5520.pdf
- T.C. Resmî Gazete / Mevzuat Bilgi Sistemi (1960). *193 sayılı Gelir Vergisi Kanunu*. https://www.mevzuat.gov.tr/MevzuatMetin/1.4.193.pdf
- T.C. Resmî Gazete / Mevzuat Bilgi Sistemi (1961). *213 sayılı Vergi Usul Kanunu*. https://www.mevzuat.gov.tr/MevzuatMetin/1.4.213.pdf
