---
id: kb-ea-33-1-hr-systems
title: "İnsan kaynakları sistemleri: Personel kaydından performansa"
summary: "Personel ana verisi, organizasyon yapısı, izin ve puantaj, işe alım, performans ve eğitim süreçlerini yöneten İK sistemlerini; bordro ile ilişkisini ve kişisel verilerin korunması açısından dikkat edilmesi gerekenleri anlatır."
course: ea
category: is-sistemleri-temelleri
tags: [ik, insan-kaynaklari, puantaj, performans, kvkk]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru]
level: orta
source_lessons: [EA-33.1]
reading_minutes: 2
key_points:
  - "İK sisteminin temeli doğru personel ana verisi ve güncel organizasyon şemasıdır."
  - "İzin ve puantaj verisi bordronun ana girdisidir."
  - "İşe alım, performans ve eğitim modülleri genellikle aynı ana veriyi kullanır."
  - "Personel verisi kişisel veri, sağlık gibi bilgiler özel nitelikli kişisel veridir."
  - "Yetkiler, yöneticinin yalnızca kendi ekibinin verisini görmesini sağlamalıdır."
glossary_terms: [personel-ana-verisi, puantaj]
related: [kb-ea-33-2-payroll-basics, kb-ea-33-3-incentive-compensation-systems, kb-ea-35-1-document-archive-retention]
sources:
  - title: "6698 sayılı Kişisel Verilerin Korunması Kanunu"
    authors: "T.C."
    year: 2016
    type: law
    url: "https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6698.pdf"
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

Çalışan sayısı arttıkça izinler, puantaj, işe giriş-çıkış ve performans değerlendirmeleri Excel'de yönetilemez hale gelir. Bu kart, İK sistemlerinin kapsamını ve dikkat edilecek noktaları anlatır.

## Temel fikir

**Temel modüller:**

- **Personel ana verisi:** Kimlik, iletişim, pozisyon, departman, işe giriş tarihi, ücret bilgisi.
- **Organizasyon yapısı:** Pozisyonlar ve raporlama ilişkileri. Onay akışları buradan beslenir.
- **İzin ve puantaj:** İzin talepleri, onaylar, devam kayıtları ve fazla mesai.
- **İşe alım:** İlan, aday takibi, mülakat ve teklif.
- **Performans:** Hedefler, değerlendirme dönemleri, geri bildirim.
- **Eğitim:** Zorunlu ve gelişim eğitimleri, sertifikalar.

**Bordroyla ilişki.** Puantaj, izin ve ücret değişiklikleri bordronun girdisidir. İK ve bordro farklı sistemlerdeyse aktarımın zamanı ve kontrolü net olmalıdır.

**Kişisel verilerin korunması.** 6698 sayılı Kanun kapsamında personel verisi kişisel veridir; sağlık raporları gibi bilgiler özel nitelikli kişisel veri sayılır. Erişim yetkileri buna göre sınırlanmalı, saklama süreleri belirlenmelidir.

### Sistem seçerken ve kurarken neye bakılır?

İK sistemi seçimi çoğu zaman bordro ihtiyacıyla başlar, ancak uzun vadede değer, verinin diğer sistemleri doğru beslemesinden gelir.

- **Organizasyon yapısının tek kaynağı:** Onay akışları, satış hedefleri ve bölge yöneticisi atamaları organizasyon yapısından beslenir. Bu yapı İK sisteminde güncel tutulmazsa ERP ve satış uygulamasındaki onaylar yanlış kişiye gider.
- **İşe giriş ve çıkış süreçleri:** Yeni bir çalışanın kullanıcı hesabının açılması, cihaz teslimi ve yetkilerin verilmesi İK kaydıyla tetiklenmelidir. Daha da önemlisi, işten ayrılan çalışanın tüm sistemlerdeki erişimi aynı gün kapatılmalıdır.
- **Çalışan self servisi:** Çalışanın izin talebini, bordro pusulasını ve kişisel bilgilerini kendisinin görmesi, İK biriminin rutin yükünü azaltır.
- **Saha çalışanları:** Satış temsilcileri ve sürücüler masa başında değildir; mobil erişim ve basit ekranlar önemlidir.
- **Raporlama:** Personel devir hızı, devamsızlık ve eğitim tamamlama oranları gibi göstergeler, verinin tek sistemde tutulmasıyla güvenilir hâle gelir.

Kişisel veri açısından, her modül için kimlerin hangi alanları görebileceği rol bazında tanımlanmalı ve saklama süreleri hukuk birimiyle birlikte belirlenmelidir.

### İK verisinin diğer sistemlerle bağlantısı

Organizasyon ve pozisyon bilgisi, onay akışlarını ve yetkileri besler. İK sistemi bu verinin tek kaynağı olmalıdır.

**Bordroyla bağlantı.** İşe giriş, ücret değişikliği, izin ve işten çıkış kayıtları bordroya doğrudan akmalıdır. Elle aktarım, hem yanlış ödeme hem de SGK bildirimlerinde gecikme riski doğurur.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b7.py` ile yapılmıştır.

250 çalışanlı bir distribütörde bir yılda 30 kişi ayrılıyor: devir oranı **%12,0**. İK sistemine geçmeden önce bu rakam yalnızca yıl sonunda elle hesaplanıyordu. Artık departman ve pozisyon bazında aylık izleniyor; ayrılışların saha satış ekibinde yoğunlaştığı görülüyor.

## Sık yapılan hatalar

- Organizasyon şemasını güncel tutmamak; onaylar yanlış kişiye gider.
- Tüm yöneticilere tüm personel verisini açmak.
- İzin bakiyelerini bordrodan ayrı Excel'de tutmak.
- Ayrılan personelin verisini süresiz saklamak.
- İşten ayrılan çalışanın sistem erişimlerini kapatmayı unutmak.
- Saha çalışanlarının mobil erişim ihtiyacını göz ardı etmek.

## Pratikte nasıl uygulanır?

- [ ] Personel ana verisini tek sistemde toplayın.
- [ ] Organizasyon şemasını sistemde güncel tutun.
- [ ] Rol bazlı erişim yetkilerini tanımlayın.
- [ ] Devir oranını aylık raporlayın.

## Daha fazlası

- 6698 sayılı Kişisel Verilerin Korunması Kanunu: https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6698.pdf
