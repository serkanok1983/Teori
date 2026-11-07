---
id: kb-ea-32-4-asset-maintenance
title: "Varlık ve bakım yönetimi: Planlı bakım, MTBF ve MTTR"
summary: "Makine, araç ve soğutucu gibi varlıkların sistemde kaydını, arıza ve planlı bakım iş emirlerini, yedek parça yönetimini ve arızalar arası ortalama süre (MTBF) ile ortalama onarım süresi (MTTR) göstergelerini anlatır."
course: ea
category: tedarik-ve-depo-sistemleri
tags: [bakim, varlik-yonetimi, mtbf, mttr, cmms]
roles: [depo-lojistik-muduru]
level: orta
source_lessons: [EA-32.4]
reading_minutes: 2
key_points:
  - "Bakım yönetim sistemi varlıkları, bakım planlarını ve iş emirlerini kayıt altına alır."
  - "Planlı bakım, arıza olmadan önce takvime veya kullanıma göre yapılan bakımdır."
  - "MTBF, arızalar arasındaki ortalama çalışma süresidir; yüksek olması iyidir."
  - "MTTR, bir arızanın ortalama onarım süresidir; düşük olması iyidir."
  - "Satış noktalarındaki soğutucu gibi varlıklar da aynı mantıkla yönetilebilir."
glossary_terms: [planli-bakim, mtbf, mttr]
related: [kb-ea-32-1-mes-oee, kb-ea-31-1-tms-fleet-telematics, kb-ea-34-1-purchasing-supplier-management]
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

Duran bir hat, arızalı bir araç veya bozulmuş bir soğutucu doğrudan satış kaybıdır. Bu kart, bakım yönetiminin sistemde nasıl kurulduğunu ve iki temel göstergeyi anlatır.

## Temel fikir

**Varlık kaydı.** Her makine, araç veya noktaya verilen soğutucu bir varlık kartıyla tanımlanır: seri numarası, konum, alım tarihi, garanti, sorumlu.

**İş emirleri:**

- **Arıza bakımı:** Arıza bildirimiyle açılır.
- **Planlı bakım:** Takvime (ör. üç ayda bir) veya kullanıma (ör. kilometre ya da çalışma saati) göre sistem tarafından otomatik açılır.

Her iş emrinde harcanan süre, kullanılan yedek parça ve maliyet kaydedilir.

**Göstergeler:**

- **MTBF (arızalar arası ortalama süre):** Toplam çalışma süresi / arıza sayısı.
- **MTTR (ortalama onarım süresi):** Toplam onarım süresi / arıza sayısı.

Nakajima'nın toplam verimli bakım yaklaşımı, operatörlerin günlük temel bakımı üstlenmesini ve planlı bakımın arıza bakımının yerini almasını önerir.

**Saha varlıkları.** Hızlı tüketimde noktalara verilen soğutucular da varlıktır. Hangi noktada hangi soğutucunun olduğu, son bakım tarihi ve arıza geçmişi aynı sistemde izlenebilir.

### Bakım stratejisini seçmek

Her varlık aynı bakım yaklaşımını gerektirmez. Yaygın üç yaklaşım şunlardır:

- **Arıza sonrası bakım:** Ekipman bozulunca onarılır. Arızası işi durdurmayan, ucuz ve kolay değiştirilen ekipmanlar için kabul edilebilir.
- **Planlı (önleyici) bakım:** Takvime veya kullanım miktarına göre bakım yapılır. Araç filosu, forkliftler ve soğuk zincir ekipmanı gibi arızası maliyetli varlıklar için temel yaklaşımdır.
- **Duruma dayalı bakım:** Sıcaklık, titreşim veya motor verisi gibi ölçümler izlenir; bakım, belirli bir eşik aşıldığında yapılır. Sensör ve veri altyapısı gerektirir.

**Kritiklik sınıflandırması.** Varlıklar, arızalarının işe etkisine göre sınıflandırılmalıdır. Soğuk depo kompresörü ile ofis yazıcısının aynı önceliğe sahip olmaması gerekir.

**Sistemde kayıt.** Bakım iş emirleri, kullanılan yedek parçalar, harcanan işçilik ve arıza nedenleri kaydedilmezse MTBF ve MTTR hesaplanamaz. Bu kayıtlar ayrıca hangi ekipmanın yenilenmesi gerektiğine karar verirken toplam sahip olma maliyetinin temel girdisidir.

**Yedek parça stoğu.** Kritik ekipmanın yedek parçalarının stokta bulunmaması, kısa bir arızayı uzun bir duruşa dönüştürebilir. Yedek parça stoğu, varlığın kritikliğine ve tedarik süresine göre planlanmalıdır.

### Bakım verisinin kullanımı

Bakım kayıtları, yenileme kararlarında da kullanılmalıdır. Onarım maliyeti sürekli artan bir varlık için yenileme zamanı gelmiş olabilir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b7.py` ile yapılmıştır.

Bir dolum makinesi bir dönemde 2.000 saat çalışıyor ve 4 kez arızalanıyor: MTBF **500** saat. Dört arızanın onarımı toplam 12 saat sürüyor: MTTR **3,0** saat. Arızaların ikisi aynı parçadan kaynaklandığı için bu parça planlı bakım listesine ekleniyor.

## Sık yapılan hatalar

- Bakımı yalnızca arıza olunca yapmak.
- İş emirlerini kâğıtta tutup süre ve maliyeti kaydetmemek.
- Noktalardaki soğutucuların yerini bilmemek.
- Tüm varlıklara aynı bakım yaklaşımını uygulamak.
- Arıza nedenlerini kaydetmeyip MTBF ve MTTR'yi hesaplanamaz bırakmak.
- Kritik ekipmanın yedek parçasını stokta tutmamak.

## Pratikte nasıl uygulanır?

- [ ] Kritik varlıkların listesini çıkarın.
- [ ] Her biri için planlı bakım takvimi tanımlayın.
- [ ] Arıza iş emirlerinde neden ve süreyi zorunlu yapın.
- [ ] MTBF ve MTTR'yi üç ayda bir raporlayın.

## Daha fazlası

- Nakajima, *Introduction to TPM* (kitap; doğrulanmadı).
