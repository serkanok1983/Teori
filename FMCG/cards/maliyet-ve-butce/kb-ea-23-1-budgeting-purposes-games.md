---
id: kb-ea-23-1-budgeting-purposes-games
title: "Bütçenin amaçları ve bütçe oyunları"
summary: "Bütçenin planlama, koordinasyon, kaynak dağıtımı ve performans değerlendirme gibi farklı amaçlarını, bu amaçlar çatıştığında ortaya çıkan bütçe payı ve harca ya da kaybet davranışlarını ve Beyond Budgeting eleştirisini anlatır."
course: ea
category: maliyet-ve-butce
tags: [butce, yonetim-kontrolu, performans, davranis]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [EA-23.1]
reading_minutes: 3
key_points:
  - "Bütçe aynı anda plan, hedef, kaynak dağıtımı ve prim ölçütü olarak kullanılır; bu amaçlar çatışabilir."
  - "Bütçe primlere bağlandığında yöneticiler hedefleri düşük göstermeye yönelir."
  - "‘Harca ya da kaybet’ davranışı dönem sonunda gereksiz harcama doğurur."
  - "Beyond Budgeting yaklaşımı sabit yıllık hedef yerine göreceli hedefler ve sürekli tahmin önerir."
  - "Tahmin ile hedefi ayırmak bütçe oyunlarını azaltır."
glossary_terms: [butce-payi, yonetim-kontrolu]
related: [kb-ea-23-2-rolling-forecast-driver-based, kb-ea-23-3-balanced-scorecard-okr, kb-eco-39-4-budgeting-standard-costs, kb-ea-33-3-incentive-compensation-systems]
sources:
  - title: "Management Control Systems"
    authors: "Anthony, R. N.; Govindarajan, V."
    year: 2007
    type: book
    verified: false
  - title: "Beyond Budgeting: How Managers Can Break Free from the Annual Performance Trap"
    authors: "Hope, J.; Fraser, R."
    year: 2003
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

Her yıl sonbaharda haftalar süren bütçe toplantıları yapılır; ama yılın ortasında bütçe çoğu zaman gerçekle bağını kaybeder. Bu kart, bütçenin neden zorlandığını ve davranışları nasıl etkilediğini anlatır.

## Temel fikir

Anthony ve Govindarajan, bütçeyi bir **yönetim kontrolü** aracı olarak ele alır. Bütçe aynı anda birkaç işe yarar:

- **Planlama:** Gelecek yılın beklenen satış ve maliyetleri.
- **Koordinasyon:** Satış, üretim ve satın alma planlarının uyumu.
- **Kaynak dağıtımı:** Hangi bölüme ne kadar harcama yetkisi verileceği.
- **Performans değerlendirme:** Yöneticinin başarısının ölçülmesi ve primlendirilmesi.

Sorun, bu amaçların çatışmasıdır. Bütçe hem en iyi tahmin hem de prim hedefi olunca yöneticiler hedefi düşük göstermeye yönelir. Buna **bütçe payı** denir. Benzer şekilde, "bu yıl harcamazsam gelecek yıl bütçem kesilir" düşüncesi dönem sonunda gereksiz harcamaya yol açar.

Hope ve Fraser'ın **Beyond Budgeting** eleştirisi şunu önerir:

- Sabit yıllık hedefler yerine rakiplere veya geçmişe göre **göreceli hedefler**,
- Yılda bir kez yerine **sürekli tahmin**,
- Kaynakların ihtiyaç doğdukça dağıtılması,
- Kararların sahaya yakın ekiplere bırakılması.

Bu yaklaşımı tümüyle uygulamak zorunda değilsiniz; ama en azından **tahmini ve hedefi ayırmak** oyunları azaltır.

### Bütçe sürecini iyileştirmek

Bütçe oyunları, büyük ölçüde sürecin tasarımından kaynaklanır. Merchant ve Van der Stede'nin yönetim kontrol sistemleri üzerine yazdıkları, bu oyunları azaltmak için tasarım seçeneklerine dikkat çeker. Uygulamada şu adımlar yardımcı olur:

- **Amaçları ayırın:** Tek bir bütçe rakamı hem tahmin, hem hedef, hem de prim temeli olarak kullanıldığında, yöneticiler rakamı kendi lehlerine çekmeye çalışır. Tahmin ile hedefin ayrı tutulması, gerçekçi tahmini teşvik eder.
- **Varsayımları görünür kılın:** Bütçe rakamlarının arkasındaki hacim, fiyat, maliyet ve kur varsayımları yazılı olmalıdır. Böylece sapmalar, varsayım değişikliği ile performans farkı olarak ayrıştırılabilir.
- **Göreli değerlendirme:** Performansı yalnızca bütçeye göre değil, önceki yıla, rakiplere veya benzer bölgelere göre de değerlendirmek, bütçeyi düşük tutma eğilimini azaltır.
- **Yuvarlanan tahmin:** Yıllık bütçenin yanında, her çeyrek güncellenen bir ileriye dönük tahmin, yıl içinde değişen koşullara uyum sağlar.
- **"Kullan ya da kaybet" etkisini azaltın:** Yıl sonunda harcanmayan bütçenin bir sonraki yıl kesileceği beklentisi, gereksiz harcamaya yol açar. Bu tür harcamalar izlenmeli ve tasarruflar ödüllendirilmelidir.

**Sistem desteği.** Bütçe hazırlığının tablolar arasında e-postayla dolaşması, sürüm karmaşasına ve hatalara yol açar. Bir planlama aracı veya en azından merkezi ve kilitli bir şablon, varsayımların ve onayların izlenmesini kolaylaştırır. Hope ve Fraser'ın bütçesiz yönetim yaklaşımı ise sabit yıllık bütçenin yerine esnek hedefler ve dinamik kaynak dağıtımını önerir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b5.py` ile yapılmıştır.

Bir dağıtıcıda bölge müdürleri primlerini bütçeye göre alıyor. Bir bölge, gerçek potansiyeli 11.500.000 TL iken bütçeyi 10.000.000 TL olarak öneriyor. Fark **1.500.000,00 TL**; potansiyelin **%13,0**'ı. Yönetim, bu bölgenin bütçeyi her yıl belirgin bir farkla aştığını fark ediyor. Ertesi yıl prim hedefini pazar payı değişimine bağlıyor ve bölgelerden ayrıca "en iyi tahmin" istiyor.

## Sık yapılan hatalar

- Bütçeyi hem tahmin hem prim hedefi olarak kullanmak.
- Bütçeyi yıl boyunca hiç güncellememek.
- Harcanmayan bütçeyi bir sonraki yıl otomatik kesmek.
- Bütçe aşımlarını nedenlerine bakmadan cezalandırmak.

## Pratikte nasıl uygulanır?

- [ ] Bütçenin hangi amaçla kullanıldığını yazılı olarak belirleyin.
- [ ] Prim hedefleri ile tahminleri ayrı tutun.
- [ ] Son yıllardaki bütçe–gerçekleşen farklarını bölge bazında inceleyin.
- [ ] Yıl içinde en az üç ayda bir güncel tahmin yapın.

## Daha fazlası

- Anthony ve Govindarajan, *Management Control Systems* (kitap; doğrulanmadı).
- Hope ve Fraser, *Beyond Budgeting* (kitap; doğrulanmadı).
