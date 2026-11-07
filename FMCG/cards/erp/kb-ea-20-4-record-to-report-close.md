---
id: kb-ea-20-4-record-to-report-close
title: "Kayıttan rapora (R2R): Ay sonu kapanışı"
summary: "Genel muhasebe ve yardımcı defterlerin ilişkisini, ay sonu kapanış adımlarını (mutabakat, tahakkuk, şirketler arası işlemler, kur değerlemesi) ve kapanışı hızlandırmak için ERP'de neler yapılabileceğini anlatır."
course: ea
category: erp
tags: [erp, muhasebe, kapanis, finansal-raporlama]
roles: [finans-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-20.4]
reading_minutes: 3
key_points:
  - "Satış, satın alma ve stok hareketleri yardımcı defterlerden genel muhasebeye otomatik akar."
  - "Kapanış; mutabakat, tahakkuk, değerleme, şirketler arası eşleştirme ve raporlama adımlarından oluşur."
  - "Kapanış takvimi, her görevin sahibini ve gününü gösteren bir kontrol listesidir."
  - "Hızlı kapanışın anahtarı, işi ay sonuna bırakmamak ve hesapları sürekli mutabık tutmaktır."
  - "Elle yapılan yevmiye kayıtları en çok hata ve gecikme kaynağıdır."
glossary_terms: [genel-muhasebe, ay-sonu-kapanisi, mutabakat]
related: [kb-ea-20-2-order-to-cash, kb-ea-20-3-procure-to-pay, kb-ea-22-3-consolidation-close-systems, kb-ea-22-1-chart-of-accounts-tekduzen]
sources:
  - title: "Integrated Business Processes with ERP Systems"
    authors: "Magal, S. R.; Word, J."
    year: 2011
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

Ayın ilk iki haftası "kapanış yapılıyor" diye rapor beklemek, yönetimin geçen ayı ancak bu ayın ortasında görmesi demektir. Bu kart, **kayıttan rapora** (R2R, *record-to-report*) sürecini ve kapanışı kısaltmanın yollarını anlatır.

## Temel fikir

ERP'de muhasebe iki katmanlıdır:

- **Yardımcı defterler:** Müşteri cari hesapları, tedarikçi cari hesapları, stok, sabit kıymetler. Günlük işlemler burada oluşur.
- **Genel muhasebe:** Yardımcı defterlerdeki hareketler, hesap eşleştirmeleriyle otomatik olarak genel muhasebe hesaplarına aktarılır.

Bu entegrasyon sayesinde fatura kesildiğinde ayrıca yevmiye kaydı yazmak gerekmez. Ancak kapanışta şu adımlar yine yapılır:

1. **Kesim kontrolleri:** Ay içinde sevk edilen ama faturalanmayan, ya da faturası gelen ama malı gelmeyen kalemler.
2. **Mutabakat:** Banka, cari hesaplar, stok ve ara hesapların genel muhasebeyle uyumu.
3. **Tahakkuk ve karşılıklar:** Prim, kira, yıl sonu iskontoları gibi henüz faturası gelmemiş giderler.
4. **Değerleme:** Döviz hesaplarının kur değerlemesi, stok değerlemesi.
5. **Şirketler arası işlemler:** Grup şirketleri arasındaki alacak–borcun eşleştirilmesi.
6. **Raporlama ve analiz:** Bütçe ve önceki dönemle karşılaştırma, sapmaların açıklanması.

Bu adımlar, sahibi ve günü belli bir **kapanış takviminde** toplanır.

### Kapanışı hızlandırmak

Ay sonu kapanışının uzun sürmesi, yönetimin güncel bilgiyle karar vermesini geciktirir. Kapanışı hızlandırmak ve kalitesini artırmak için şu yöntemler kullanılabilir:

- **Kapanış takvimi ve görev listesi:** Her kapanış görevinin sorumlusu, başlangıç günü ve bağımlılıkları bir listede yer almalıdır. Görevlerin tamamlanma durumu herkes tarafından görülebilmelidir.
- **İşi kapanış öncesine taşıyın:** Mutabakatların bir kısmı, ay içinde düzenli olarak yapılabilir. Örneğin banka eşleştirmeleri günlük, cari hesap mutabakatları haftalık yapıldığında ay sonu yükü azalır.
- **Tahakkuk standartları:** Tekrarlayan tahakkuklar (kira, faiz, prim karşılıkları) için şablonlar ve hesaplama yöntemleri belirlenmelidir.
- **Önemlilik eşiği:** Küçük tutarlı farkların araştırılması için önemlilik eşikleri tanımlanmalıdır; aksi hâlde ekip zamanını önemsiz farklara harcar.
- **Şirketler arası mutabakat:** Grup şirketleri arasındaki işlemlerin her iki tarafta da aynı tutar ve dönemle kaydedildiği, kapanıştan önce kontrol edilmelidir.

**Kalite kontrolleri.** Kapanıştan sonra, bilanço hesaplarının mutabakat belgeleri ile desteklendiği ve gelir tablosundaki olağan dışı değişimlerin açıklandığı bir gözden geçirme yapılmalıdır. Bu gözden geçirme, hataların dış raporlamaya yansımasını önler.

**Sürekli iyileştirme.** Her kapanıştan sonra gecikmelerin ve düzeltme kayıtlarının nedenleri kısa bir toplantıda değerlendirilmelidir. Tekrarlayan sorunlar, kaynağındaki süreçte düzeltilmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b4.py` ile yapılmıştır.

Bir üretici ay sonu kapanışını 12 iş gününde yapıyor. Gecikmenin nedenleri: Banka mutabakatı ay sonunda toplu yapılıyor, bayilerle cari mutabakatı e-postayla ve elle yürüyor, prim tahakkukları satış departmanından Excel ile geliyor.

Finans ekibi şu değişiklikleri yapıyor:

- Banka hareketleri her gün otomatik içe alınıp eşleştiriliyor.
- Prim tahakkuku, ERP'deki satış verisinden hesaplanan bir rapora bağlanıyor.
- Kapanış takviminde her görevin sahibi ve günü belirleniyor; günlük 10 dakikalık durum toplantısı yapılıyor.

Kapanış **5 iş gününe** iniyor; süre **%58,3** kısalıyor.

## Sık yapılan hatalar

- Mutabakatları yalnızca ay sonunda yapmak.
- Elle yevmiye kayıtlarını onaysız ve açıklamasız girmek.
- Kapanış görevlerini kişilerin hafızasına bırakmak.
- Ara hesapları açıklanamayan bakiyelerle bir sonraki aya devretmek.

## Pratikte nasıl uygulanır?

- [ ] Kapanış takvimi hazırlayın: görev, sahip, gün, bağımlılık.
- [ ] Banka ve cari mutabakatlarını günlük veya haftalık hale getirin.
- [ ] Elle yevmiye kayıtlarını sayın ve otomatikleştirilebilecek olanları belirleyin.
- [ ] Her kapanıştan sonra gecikme nedenlerini kısa bir toplantıda gözden geçirin.

## Daha fazlası

- Magal ve Word, *Integrated Business Processes with ERP Systems* (kitap; doğrulanmadı).
