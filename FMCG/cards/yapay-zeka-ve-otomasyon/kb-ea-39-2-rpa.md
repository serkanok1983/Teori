---
id: kb-ea-39-2-rpa
title: "Robotik süreç otomasyonu (RPA)"
summary: "Robotik süreç otomasyonunun ne olduğunu, \"hafif BT\" olarak hangi işlere uyduğunu, hangi işlere uymadığını ve bakım, güvenlik ve kırılganlık risklerini anlatır."
course: ea
category: yapay-zeka-ve-otomasyon
tags: [rpa, otomasyon, yazilim-robotu, surec, hafif-bt]
roles: [finans-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-39.2]
reading_minutes: 2
key_points:
  - "RPA, insanın ekran üzerinden yaptığı kural tabanlı işleri yazılım robotlarıyla taklit eder."
  - "Van der Aalst ve arkadaşları RPA'yı mevcut sistemlerin üstünde çalışan \"hafif BT\" olarak konumlar."
  - "Yüksek hacimli, kuralları net ve sık değişmeyen işler RPA için uygundur."
  - "Ekran değişikliklerinde robot bozulabilir; bakım maliyeti hesaba katılmalıdır."
  - "Mümkünse önce API entegrasyonu veya süreç sadeleştirme düşünülmelidir."
glossary_terms: [rpa, yazilim-robotu]
related: [kb-ea-39-1-low-code, kb-ea-4-6-process-analysis-cycle-time, kb-ea-11-6-apis-for-managers]
sources:
  - title: "Robotic Process Automation"
    authors: "van der Aalst, W.; Bichler, M.; Heinzl, A."
    year: 2018
    type: article
    doi: "10.1007/s12599-018-0542-4"
    url: "https://doi.org/10.1007/s12599-018-0542-4"
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

Bir çalışan her sabah banka portalından dosya indirip ERP'ye yüklüyor, bir başkası e-postadaki siparişleri sisteme tek tek giriyorsa RPA akla gelir. Bu kart, RPA'nın doğru kullanıldığı ve yanlış kullanıldığı yerleri anlatır.

## Temel fikir

**Tanım:** RPA, insanın bir ekranda yaptığı tıklama, kopyalama ve veri girişi gibi adımları kurallara göre tekrarlayan yazılım robotlarıdır. Arka plandaki sistemleri değiştirmez; onların kullanıcı arayüzü üzerinden çalışır.

**Hafif BT:** Van der Aalst, Bichler ve Heinzl, RPA'yı ana sistemlere dokunmadan üst katmanda çalışan "hafif BT" olarak tartışır. Bu, hızlı devreye almayı sağlar ama kalıcı mimari çözümün yerine geçmez.

**Uygun işler:**

- Yüksek hacimli ve tekrarlayan
- Kuralları açık, istisnası az
- Yapılandırılmış girdiye sahip
- Ekranları sık değişmeyen sistemler

**Uygun olmayan işler:** Sık değişen süreçler, çok istisna ve yargı gerektiren kararlar, API'si olan sistemler.

**Riskler:** Ekran değişince robotun bozulması, robot hesabının geniş yetkileri, hataların sessizce birikmesi.

### RPA programını yönetmek

Tek bir robot kolayca kurulur; zorluk, robot sayısı arttığında başlar. Sürdürülebilir bir RPA programı için şu unsurlar gerekir:

- **Aday seçimi:** Süreçler; hacim, kural netliği, girdi yapısı, istisna oranı ve sistem değişim sıklığına göre puanlanmalıdır. Puanı yüksek olmayan bir süreç, sırf otomasyon hedefi tutsun diye robota verilmemelidir.
- **Belgelenmiş süreç:** Robot, belgelenmemiş bir süreci öğrenemez. Her robotun hangi adımları izlediği, hangi istisnada durduğu ve kimi uyardığı yazılı olmalıdır.
- **İstisna yönetimi:** Robotun çözemediği durumlar bir iş kuyruğuna düşmeli ve bir çalışan tarafından ele alınmalıdır. İstisnaların sessizce birikmesi, RPA'nın en yaygın gizli riskidir.
- **Değişiklik yönetimi:** Robotun çalıştığı sistemlerde ekran veya alan değişikliği planlandığında, robot sahibi önceden bilgilendirilmelidir. Bu, BT değişiklik sürecinin bir adımı olmalıdır.
- **Güvenlik:** Robot hesapları gerçek kullanıcılar gibi yetkilendirilir; parolaları güvenli bir kasada tutulmalı ve yetkileri düzenli gözden geçirilmelidir.

**Kazancı ölçmek.** Robotun tasarruf ettiği süre, yalnızca çalışılan işlem sayısıyla değil, istisnaları çözmek ve robotu onarmak için harcanan süre de düşülerek hesaplanmalıdır. Van der Aalst ve arkadaşlarının vurguladığı gibi, RPA'nın değeri en çok, tam entegrasyonun ekonomik olmadığı, uzun kuyruktaki süreçlerde ortaya çıkar.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b8.py` ile yapılmıştır.

Bir dağıtıcıda ayda 1.200 tahsilat kaydı banka portalından ERP'ye elle aktarılıyor; her biri 4 dakika sürüyor. Bu ayda **80,0** saat ediyor. Ekip önce bankanın hesap hareketi entegrasyonunu araştırıyor; bu mümkün olmadığı için geçici bir RPA robotu kuruyor ve hata raporunu her gün kontrol ediyor.

## Sık yapılan hatalar

- Bozuk bir süreci düzeltmeden otomatikleştirmek.
- API varken RPA kullanmak.
- Robot hesaplarına gereğinden geniş yetki vermek.
- Bakım ve izleme maliyetini hesaba katmamak.

## Pratikte nasıl uygulanır?

- [ ] Aday işleri hacim, kural netliği ve değişim sıklığına göre puanlayın.
- [ ] Her aday için önce süreç sadeleştirme ve API seçeneğini değerlendirin.
- [ ] Robot hesaplarına en az yetki verin ve logları saklayın.
- [ ] Her robot için sahibini ve hata izleme yöntemini belirleyin.

## Daha fazlası

- van der Aalst, Bichler ve Heinzl (2018), *Robotic Process Automation*, Business & Information Systems Engineering.
