---
id: kb-ea-9-1-reporting-vs-transaction-systems
title: "İşlem sistemi ve raporlama sistemi neden ayrılır? Veri ambarına giriş"
summary: "Günlük işlemleri yürüten sistemlerle (OLTP) analiz ve raporlama sistemlerinin (OLAP, veri ambarı) neden ayrı tasarlandığını; büyük raporları ERP'nin canlı veritabanında çalıştırmanın risklerini ve iki temel veri ambarı yaklaşımını anlatır."
course: ea
category: veri-yonetimi
tags: [raporlama, veri-ambari, erp, performans]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, it-yoneticisi]
level: orta
source_lessons: [EA-9.1]
reading_minutes: 3
key_points:
  - "İşlem sistemleri (OLTP) çok sayıda küçük kayıt yazmak, raporlama sistemleri (OLAP) çok sayıda kaydı okumak için tasarlanır."
  - "Ağır raporları canlı ERP'de çalıştırmak fatura kesen kullanıcıları yavaşlatabilir."
  - "Veri ambarı, farklı kaynaklardan veriyi tarihçesiyle toplayan ayrı bir veritabanıdır."
  - "Inmon önce merkezi ambar, Kimball önce iş alanına göre boyutsal modeller önerir."
  - "Raporlama verisi genellikle gece veya belirli aralıklarla yüklenir; 'canlı' olmadığı bilinmelidir."
glossary_terms: [veri-ambari, erp]
related: [kb-ea-9-2-sell-in-sell-out-reporting, kb-ea-9-6-bi-dashboards-kpis, kb-ea-10-1-why-integration-is-hard, kb-ea-20-4-record-to-report-close]
sources:
  - title: "An overview of data warehousing and OLAP technology"
    authors: "Chaudhuri, S.; Dayal, U."
    year: 1997
    type: article
    doi: "10.1145/248603.248616"
    url: "https://doi.org/10.1145/248603.248616"
    verified: true
    checked_on: 2026-10-28
  - title: "Building the Data Warehouse"
    authors: "Inmon, W. H."
    year: 2005
    type: book
    verified: false
  - title: "The Data Warehouse Toolkit"
    authors: "Kimball, R.; Ross, M."
    year: 2013
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

Ay sonunda finans büyük bir satış analizini çalıştırdığında depoda fatura kesimi yavaşlıyorsa, işlem ve raporlama yükü aynı yerde çakışıyor demektir. Bu kart, bu iki işin neden ayrı sistemlerde yapıldığını ve **veri ambarının** (*data warehouse*) ne işe yaradığını anlatır.

## Temel fikir

Chaudhuri ve Dayal (1997), iki tür iş yükünü ayırır:

| | İşlem sistemi (OLTP) | Raporlama sistemi (OLAP) |
|---|---|---|
| Örnek | ERP, saha satış uygulaması | Veri ambarı, iş zekâsı aracı |
| İş | Sipariş girmek, fatura kesmek | Aylık, bölgesel, ürün bazlı analiz |
| Kayıt başına | Birkaç satır yazar veya okur | Milyonlarca satırı toplar |
| Veri | Güncel durum | Tarihçe (geçmiş dönemler dahil) |
| Tasarım | Hızlı ve tutarlı kayıt | Hızlı okuma ve toplama |

Veri ambarı, ERP, saha uygulaması, e-ticaret, müşteri ve dağıtıcı verilerinden düzenli aralıklarla veri çeker, temizler ve analiz için düzenler. Bu süreç ETL (*extract, transform, load*: çıkar, dönüştür, yükle) olarak adlandırılır.

İki klasik yaklaşım vardır:

- **Inmon:** Önce tüm firma için merkezi, normalleştirilmiş bir ambar; iş birimlerine özel veri pazarları onun üzerine.
- **Kimball:** İş süreçlerine göre (satış, stok, tahsilat) boyutsal modeller; ortak boyutlarla (ürün, müşteri, tarih) birbirine bağlanır.

Orta ölçekli firmalarda genellikle Kimball yaklaşımıyla küçük başlanır.

### Veri ambarı projesinde ilk adımlar

Veri ambarı projeleri, çoğu zaman teknik bir altyapı işi olarak başlar ve iş kullanıcılarının sorularından uzaklaşır. Kimball ve Ross'un önerdiği yaklaşım, işe iş süreçlerinden ve yöneticilerin sorduğu sorulardan başlamaktır. Pratik bir başlangıç için şu adımlar önerilir:

- **Bir iş süreci seçin:** Örneğin satış. Hangi sorular soruluyor? Bölge, temsilci, müşteri, ürün ve dönem bazında satış, iskonto ve kârlılık gibi.
- **Ayrıntı düzeyini belirleyin:** Veriyi fatura satırı düzeyinde mi, günlük toplam düzeyinde mi tutacaksınız? En ayrıntılı düzeyde tutmak, ileride sorulacak beklenmedik soruları cevaplamayı mümkün kılar.
- **Boyutları ortak tanımlayın:** Müşteri, ürün ve tarih gibi boyutların tüm raporlarda aynı tanımla kullanılması, farklı raporlardaki rakamların tutarlı olmasını sağlar.
- **Tarihçeyi koruyun:** Müşterinin bölgesi veya temsilcisi değiştiğinde, geçmiş satışların hangi bölgeye yazılacağı önceden kararlaştırılmalıdır.

**Veri yükleme ve güncellik.** İşlem sistemlerinden veri ambarına aktarım genellikle gece yapılır. Kullanıcılar, raporun hangi tarihe kadar güncel olduğunu her zaman görebilmelidir. Gün içinde güncel bilgi gereken durumlar ayrıca değerlendirilmelidir.

**Rakamların doğrulanması.** Veri ambarındaki toplamlar, muhasebe ve ERP raporlarıyla düzenli olarak karşılaştırılmalıdır. Kullanıcıların rakamlara güvenmemesi, veri ambarı projelerinin en yaygın başarısızlık nedenlerinden biridir. Inmon'un vurguladığı gibi, kurumsal veri ambarının değeri, tek ve tutarlı bir bilgi kaynağı olmasından gelir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b2.py` ile yapılmıştır.

Bir bayi günde 8.000 fatura satırı oluşturuyor. Ayda 22 iş günü ile yılda **2.112.000** satır eder. Üç yıllık ürün–müşteri–ay kırılımlı bir analiz 6 milyondan fazla satırı tarar. Bu rapor mesai saatinde canlı ERP'de çalıştığında fatura ekranları yavaşlıyor.

Çözüm: Fatura ve sipariş verisi her gece raporlama veritabanına aktarılıyor; yönetim panoları buradan besleniyor. Panolarda "veriler dün akşam 23.00 itibarıyla" notu gösteriliyor. Gün içi anlık ihtiyaçlar için ERP'de yalnızca küçük, hazır raporlar kalıyor.

## Sık yapılan hatalar

- Tüm raporları canlı ERP veritabanında çalıştırmak.
- Her departmanın kendi Excel'ine veri çekmesi; aynı ciro için üç farklı rakam.
- Ambar verisinin hangi saatte güncellendiğini kullanıcıya göstermemek.
- Ambarı, kaynak sistemde düzeltilmemiş veriyle doldurup "rapor yanlış" demek.

## Pratikte nasıl uygulanır?

- [ ] Canlı ERP'de çalışan en ağır raporları belirleyin ve çalışma saatlerini kontrol edin.
- [ ] Ayrı bir raporlama veritabanı ya da ERP'nin raporlama kopyasını kullanmayı değerlendirin.
- [ ] Ciro, brüt kâr, stok gibi temel ölçülerin tanımını yazılı hale getirin.
- [ ] Panolarda verinin güncellenme zamanını gösterin.

## Daha fazlası

- Chaudhuri ve Dayal (1997), *ACM SIGMOD Record*. https://doi.org/10.1145/248603.248616
- Inmon, *Building the Data Warehouse*; Kimball ve Ross, *The Data Warehouse Toolkit* (kitaplar; doğrulanmadı).
