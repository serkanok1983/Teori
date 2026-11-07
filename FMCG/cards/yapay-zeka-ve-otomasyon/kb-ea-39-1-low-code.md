---
id: kb-ea-39-1-low-code
title: "Low-code ve no-code platformlar"
summary: "Az kodla veya kodsuz uygulama geliştirme platformlarının ne sağladığını, \"vatandaş geliştirici\" yaklaşımını, yönetişim ihtiyacını ve bu araçların sınırlarını anlatır."
course: ea
category: yapay-zeka-ve-otomasyon
tags: [low-code, no-code, vatandas-gelistirici, yonetisim, otomasyon]
roles: [it-yoneticisi]
level: orta
source_lessons: [EA-39.1]
reading_minutes: 2
key_points:
  - "Low-code platformlar, görsel araçlarla form, iş akışı ve basit uygulama geliştirmeyi hızlandırır."
  - "Vatandaş geliştirici, BT dışından olup bu araçlarla çözüm üreten çalışandır."
  - "Hız avantajı, yönetişim olmadan kontrolsüz uygulama yığınına dönüşebilir."
  - "Veri erişimi, yetki ve sahiplik kuralları baştan tanımlanmalıdır."
  - "Karmaşık, yüksek hacimli veya kritik süreçler için low-code her zaman uygun değildir."
glossary_terms: [low-code, vatandas-gelistirici]
related: [kb-ea-35-1-document-archive-retention, kb-ea-39-2-rpa, kb-ea-5-4-application-portfolio, kb-ea-15-2-user-roles-permissions]
sources:
  - title: "Low-Code Platform"
    authors: "Bock, A.; Frank, U."
    year: 2021
    type: article
    doi: "10.1007/s12599-021-00726-8"
    url: "https://doi.org/10.1007/s12599-021-00726-8"
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

Her küçük ihtiyaç için BT kuyruğunda aylarca beklemek iş birimlerini Excel'e ve e-postaya iter. Low-code platformlar bu boşluğu doldurabilir. Bu kart, faydayı ve riskleri birlikte ele alır.

## Temel fikir

**Ne sağlar?**

- Sürükle-bırak ile form ve ekran tasarımı
- Onay akışları ve bildirimler
- Hazır bağlayıcılarla ERP, e-posta ve tablo gibi sistemlere erişim
- Hızlı değişiklik ve deneme

**Vatandaş geliştirici:** Süreci en iyi bilen iş birimi çalışanı, BT'nin belirlediği sınırlar içinde kendi çözümünü geliştirir.

**Yönetişim ihtiyacı:**

- Hangi verilere erişilebileceği
- Kimin uygulama yayınlayabileceği
- Her uygulamanın bir sahibi ve yedeği olması
- Uygulamaların envantere kaydı

**Sınırlar:** Yüksek hacimli işlemler, karmaşık iş kuralları, sıkı performans veya güvenlik gerektiren süreçler ve ana iş sistemlerinin yerine geçecek çözümler için low-code genellikle doğru araç değildir. Ayrıca platforma bağımlılık ve lisans maliyeti değerlendirilmelidir.

### Doğru yerde kullanmak: Basit bir karar çerçevesi

Bir ihtiyacın low-code ile mi, ana sistemde mi, yoksa klasik yazılım geliştirmeyle mi karşılanacağına karar verirken şu sorular yardımcı olur:

- **Kaç kişi kullanacak?** Bir birimin iç ihtiyacı low-code için uygundur; tüm şirketin ve müşterilerin kullanacağı uygulamalar daha sağlam bir yapı gerektirir.
- **Veri nerede yaşayacak?** Uygulama ana iş verisini (müşteri, sipariş, fiyat) değiştiriyorsa, bu değişikliğin ana sistemin kurallarından geçmesi gerekir. Low-code uygulamanın kendi tablosunda ana verinin kopyasını tutması, tutarsızlığa yol açar.
- **Ne kadar kritik?** Uygulama durduğunda sipariş akışı duruyorsa, destek, yedekleme ve izleme gereksinimleri artar.
- **Ne sıklıkla değişecek?** Kuralları sık değişen, deneme niteliğindeki süreçler low-code'un en güçlü olduğu alandır.

**BT'nin rolü.** Low-code, BT'yi ortadan kaldırmaz; rolünü değiştirir. BT; platformu, bağlayıcıları, güvenlik kurallarını ve şablonları sağlar, iş birimleri ise bu çerçeve içinde çözüm üretir. Ortak bileşenler (onay akışı şablonu, kullanıcı doğrulama, ERP bağlayıcısı) bir kez hazırlanıp herkesin kullanımına açıldığında, hem hız hem tutarlılık artar.

Bock ve Frank, bu platformların yeni bir kavramdan çok, model güdümlü geliştirme gibi daha eski yaklaşımların ticari olarak yeniden paketlenmesi olduğunu tartışır; bu, beklentileri gerçekçi tutmak için yararlı bir bakıştır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b8.py` ile yapılmıştır.

Bir dağıtıcıda iş birimlerinin 15 form ihtiyacı (ziyaret talebi, numune isteği, iade onayı gibi) bekliyor. Klasik yöntemle her biri ortalama 10 gün, low-code ile 2 gün sürüyor. Toplam **120** geliştirme günü kazanılıyor. BT, tüm formların bir envanterde tutulmasını ve her birinin sahibinin belirlenmesini şart koşuyor.

## Sık yapılan hatalar

- Low-code uygulamalarını envantere almamak.
- Sahibi ayrılan çalışanın uygulamasını sahipsiz bırakmak.
- Kişisel veriye geniş erişim vermek.
- Ana iş sistemini low-code ile yeniden yazmaya çalışmak.
- Ana iş verisinin kopyasını low-code uygulamanın kendi tablosunda tutmak.

## Pratikte nasıl uygulanır?

- [ ] Low-code için uygun ve uygun olmayan işleri yazılı tanımlayın.
- [ ] Yayın yetkisini ve veri erişim kurallarını belirleyin.
- [ ] Her uygulamaya sahip ve yedek atayın.
- [ ] Uygulamaları portföy envanterine ekleyin.

## Daha fazlası

- Bock ve Frank (2021), low-code platformları üzerine, Business & Information Systems Engineering.
