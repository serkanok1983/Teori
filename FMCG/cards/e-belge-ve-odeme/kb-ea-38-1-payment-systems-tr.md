---
id: kb-ea-38-1-payment-systems-tr
title: "Türkiye'de ödeme sistemleri haritası"
summary: "EFT, FAST, kartlı ödeme sistemleri, BKM ve TR Karekod gibi Türkiye ödeme altyapılarını; TCMB'nin işletici ve düzenleyici rolünü ve bunların tahsilat süreçlerine etkisini anlatır."
course: ea
category: e-belge-ve-odeme
tags: [odeme, eft, fast, bkm, karekod]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: temel
source_lessons: [EA-38.1]
reading_minutes: 2
key_points:
  - "TCMB, EFT ve FAST gibi temel ödeme sistemlerini işletir ve 6493 sayılı Kanun çerçevesinde düzenleyici rol üstlenir."
  - "FAST, anlık ve günün her saati çalışan bir para transferi sistemidir."
  - "Kartlı ödemelerde BKM, Türkiye içi takas ve mutabakat altyapısında rol oynar."
  - "TR Karekod, karekodla ödeme için ortak bir standarttır."
  - "Tahsilat yönteminin seçimi nakit akışını ve mutabakat yükünü doğrudan etkiler."
glossary_terms: [fast, eft, tr-karekod]
related: [kb-ea-24-2-bank-statement-integration, kb-ea-24-3-credit-limits-collections-systems, kb-ea-38-3-findeks-credit-bureau]
sources:
  - title: "Ödeme sistemleri"
    authors: "TCMB"
    year: 2026
    type: web
    url: "https://www.tcmb.gov.tr/"
    verified: false
  - title: "Bankalararası Kart Merkezi"
    authors: "BKM"
    year: 2026
    type: web
    url: "https://bkm.com.tr/"
    verified: true
    checked_on: 2026-10-28
    note: "URL HTTP 200 ile açıldı, başlık/kurum eşleşti (2026-10-28)."
  - title: "6493 sayılı Kanun"
    authors: "TBMM"
    year: 2013
    type: web
    url: "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6493.pdf"
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

Dağıtıcı için tahsilat; havale, kart, çek ve senet gibi pek çok kanaldan gelir. Her kanal farklı hız, maliyet ve mutabakat yükü taşır. Bu kart, ödeme altyapısının haritasını çıkarır.

## Temel fikir

**Kurumlar:**

- **TCMB:** EFT ve FAST gibi sistemleri işletir; 6493 sayılı Kanun çerçevesinde ödeme sistemlerini düzenler ve gözetir.
- **BKM:** Kartlı ödemelerde Türkiye içi işlemlerin takas ve mutabakatında rol alır.
- **Bankalar ve ödeme kuruluşları:** Müşteriye hizmeti sunan taraflardır.

**Sistemler:**

- **EFT:** Bankalar arası para transferi.
- **FAST:** Anlık ve kesintisiz çalışan transfer sistemi; tutar sınırları dönemsel olarak değişebilir.
- **Kartlı ödeme:** Sanal POS, fiziki POS ve mobil POS.
- **TR Karekod:** Karekodla ödeme için ortak standart.
- **Doğrudan borçlandırma sistemi (DBS):** Bayilerin bankalar aracılığıyla vadeli ödeme yapmasına yarayan yaygın bir ticari modeldir.

**İş sistemlerine etkisi:** Banka hesap hareketleri ERP'ye otomatik alınmalı, ödeme açıklamasından müşteri ve fatura eşleşmesi yapılmalıdır.

### Tahsilat kanalı seçiminde değerlendirme ölçütleri

Bir dağıtıcı için tahsilat kanalı seçimi yalnızca müşteri tercihine bırakılmamalıdır. Her kanal aşağıdaki ölçütlere göre değerlendirilebilir:

- **Hız:** Para hesabınıza ne zaman geçiyor? Anlık transfer ile kartlı ödemede valör süresi arasında önemli fark olabilir.
- **Maliyet:** Banka işlem ücreti, kart komisyonu, POS kirası ve çek tahsil masrafı gibi doğrudan maliyetler ile vade nedeniyle oluşan finansman maliyeti birlikte hesaplanmalıdır.
- **Risk:** Karşılıksız çek, ödenmeyen senet veya ters ibraz gibi tahsil edilememe riskleri kanala göre değişir.
- **Mutabakat kolaylığı:** Ödemenin hangi müşteriye ve hangi faturaya ait olduğu ne kadar kolay belirlenebiliyor? Açıklama alanı serbest metin olan havalelerde eşleştirme zorlaşır.
- **Müşteri deneyimi:** Bayi için ödeme ne kadar kolay? Zor ödeme yöntemleri tahsilatı geciktirir.

**Eşleştirmeyi kolaylaştırmak.** Müşteriye özel ödeme referansı tanımlamak, sanal hesap numarası kullanmak veya ödeme bağlantısını faturaya eklemek, otomatik eşleştirme oranını artırır. Banka hesap hareketlerinin ERP'ye düzenli ve otomatik alınması, tahsilat ekibinin işini elle eşleştirmeden istisna yönetimine kaydırır.

**Düzenleme takibi.** Ödeme sistemlerine ilişkin limitler, işlem saatleri ve kurallar düzenleyici kararlarla değişebilir. Bankanızdan düzenli bilgi almak ve sistem parametrelerini buna göre güncellemek gerekir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b8.py` ile yapılmıştır.

Bir bayi 500.000 TL'lik siparişi 30 gün vadeyle ödüyor. Varsayımsal yıllık %36 finansman maliyetiyle bu vadenin dağıtıcıya maliyeti **14.794,52 TL** olur. Dağıtıcı, peşin FAST ödemesine iskonto tanımlayıp hangi seçeneğin daha avantajlı olduğunu hesaplıyor.

## Sık yapılan hatalar

- Tahsilat kanallarının maliyetini ve vade etkisini hesaplamamak.
- Banka hareketlerini elle eşleştirmek.
- FAST veya EFT sınırlarını ve saatlerini güncel kontrol etmemek.
- Kart komisyonlarını fiyatlamaya yansıtmamak.

## Pratikte nasıl uygulanır?

- [ ] Tahsilat kanallarınızı ve her birinin payını çıkarın.
- [ ] Her kanal için maliyet ve tahsil süresini hesaplayın.
- [ ] Banka hareketlerini ERP'ye otomatik aktarın.
- [ ] Güncel limit ve kuralları bankanızla kontrol edin.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın.

## Daha fazlası

- TCMB ödeme sistemleri sayfaları (doğrulanmadı).
- BKM sitesi.
- 6493 sayılı Ödeme ve Menkul Kıymet Mutabakat Sistemleri, Ödeme Hizmetleri ve Elektronik Para Kuruluşları Hakkında Kanun.
