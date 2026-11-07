---
id: kb-ea-6-1-it-governance-decision-rights
title: "BT yönetişimi: Teknoloji kararlarını kim verir?"
summary: "BT yönetişimini, hangi teknoloji kararının kim tarafından ve hangi bilgiyle verileceğini belirleyen bir karar hakları düzeni olarak anlatır; Weill-Ross yaklaşımı ve COBIT çerçevesiyle orta ölçekli firma için basit bir karar matrisi önerir."
course: ea
category: bt-yonetisimi-ve-guvenlik
tags: [bt-yonetisimi, karar-haklari, organizasyon, butce]
roles: [uretici-sahibi, bayi-sahibi, it-yoneticisi]
level: orta
source_lessons: [EA-6.1]
reading_minutes: 3
key_points:
  - "BT yönetişimi, teknoloji kararlarında kimin karar verdiğini ve kimin görüşünün alındığını belirler."
  - "Weill ve Ross beş karar alanı tanımlar: BT ilkeleri, mimari, altyapı, iş uygulaması ihtiyaçları, yatırım ve önceliklendirme."
  - "Yatırım ve öncelik kararları iş yönetiminde, teknik standart kararları BT'de olmalıdır."
  - "COBIT, yönetişim ile yönetimi ayırır ve kontrol hedefleri için bir çerçeve sunar."
  - "Küçük firmada bile yılda dört kez toplanan bir BT yönlendirme kurulu yeterli bir başlangıçtır."
glossary_terms: [bt-yonetisimi]
related: [kb-ea-5-4-application-portfolio, kb-ea-6-2-it-service-sla, kb-ea-6-4-internal-controls-sod, kb-ea-8-1-master-data-governance]
sources:
  - title: "IT Governance: How Top Performers Manage IT Decision Rights for Superior Results"
    authors: "Weill, P.; Ross, J. W."
    year: 2004
    type: book
    verified: false
  - title: "COBIT"
    authors: "ISACA"
    year: 2019
    type: standard
    url: "https://www.isaca.org/resources/cobit"
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

Birçok firmada yazılım kararını ya patron tek başına verir ya da BT sorumlusu bütçe olmadan karar vermeye çalışır. Sonuç, kimsenin sahiplenmediği projeler ve birbirine bağlanmayan sistemlerdir. Bu kart, **BT yönetişimi** (*IT governance*) ile hangi kararı kimin vereceğini netleştirmenizi sağlar.

## Temel fikir

Weill ve Ross'a göre BT yönetişimi, BT kullanımında istenen davranışı teşvik eden karar hakları ve hesap verebilirlik düzenidir. Beş karar alanı ayırırlar:

1. **BT ilkeleri:** BT'nin işte oynayacağı rol (ör. "tek müşteri kaydı", "önce standart paket").
2. **Mimari:** Veri, uygulama ve entegrasyon standartları.
3. **Altyapı:** Sunucu, ağ, bulut, güvenlik gibi paylaşılan hizmetler.
4. **İş uygulaması ihtiyaçları:** Hangi iş ihtiyacı için hangi uygulama.
5. **Yatırım ve önceliklendirme:** Ne kadar harcanacak, hangi proje önce.

Her alan için iki soru sorulur: Kim karar verir? Kimin görüşü alınır? Genel ilke basittir: Para ve öncelik kararları iş yönetiminde, teknik standart kararları BT'de olmalıdır; uygulama ihtiyaçları ise iş birimi ile BT'nin ortak kararıdır.

**COBIT** (ISACA), yönetişimi (yön belirleme ve izleme, yönetim kurulunun işi) ile yönetimi (planlama ve uygulama, yöneticilerin işi) ayırır ve her iki taraf için hedefler tanımlar. Orta ölçekli bir firma COBIT'i bütünüyle uygulamaz ama kontrol listesi olarak kullanabilir.

### Yönetişimi uygulamaya dökmek

Weill ve Ross'un çalışması, karar haklarının açık biçimde tanımlanmasının BT'den alınan değeri artırdığını gösterir. Orta ölçekli bir şirkette bu, ağır bir yapı kurmadan şu adımlarla uygulanabilir:

- **Karar türlerini listeleyin:** BT ilkeleri, mimari, altyapı, iş uygulaması ihtiyaçları ve BT yatırımları gibi temel karar alanlarını yazın.
- **Her karar için rolleri belirleyin:** Kim önerir, kim görüş verir, kim karar verir ve kim bilgilendirilir? Bu tablo kısa ve herkesin erişebileceği bir yerde olmalıdır.
- **Yatırım değerlendirme ölçütleri:** BT projeleri, iş faydası, risk, maliyet ve stratejiye uyum açısından ortak bir formatla değerlendirilmelidir. Böylece farklı birimlerin talepleri karşılaştırılabilir.
- **Bir yönlendirme kurulu kurun:** İş birimleri ve BT temsilcilerinden oluşan küçük bir kurul, öncelikleri belirler ve büyük projeleri izler.
- **İstisna yolunu tanımlayın:** Acil veya küçük ihtiyaçlar için daha hızlı bir onay yolu bulunmalıdır; aksi hâlde birimler BT'yi atlayarak kendi çözümlerini kurar.

**Gölge BT.** Birimlerin BT'den habersiz bulut hizmetleri veya tablolarla çözüm üretmesi, çoğu zaman karşılanmayan bir ihtiyacın işaretidir. Bunu yasaklamak yerine, kayıt altına almak, riskini değerlendirmek ve uygun olanları resmî yapıya dahil etmek daha sürdürülebilirdir.

**Ölçüm.** Yönetişimin işleyip işlemediği; proje taleplerinin karar süresi, onaylanan projelerin hedeflerine ulaşma oranı ve kullanıcı memnuniyeti gibi göstergelerle izlenebilir. COBIT, bu tür göstergeler için kapsamlı bir çerçeve sunar.

## Bir örnek

> **Örnek (temsili rakamlar):** Örnek bir firmanın karar matrisidir; rakam içermez.

| Karar alanı | Karar veren | Görüşü alınan |
|---|---|---|
| BT ilkeleri | Yönetim kurulu / genel müdür | BT yöneticisi, finans |
| Mimari ve standartlar | BT yöneticisi | Tedarikçiler, iş birimleri |
| Altyapı | BT yöneticisi | Finans (bütçe) |
| Uygulama ihtiyaçları | İş birimi yöneticisi + BT | Kullanıcılar |
| Yatırım ve öncelik | BT yönlendirme kurulu | Tüm birimler |

BT yönlendirme kurulunda genel müdür, finans müdürü, satış direktörü, depo müdürü ve BT yöneticisi var; üç ayda bir toplanıp proje listesini önceliklendiriyor.

## Sık yapılan hatalar

- Bütün kararı BT'ye bırakıp iş birimlerinin sahiplenmemesi.
- Patronun teknik standart kararlarını tek başına değiştirmesi.
- Kurul kurup gündemini yalnızca sorun bildirimine çevirmek.
- Kararları yazıya dökmemek; aynı tartışmayı her yıl yeniden yapmak.

## Pratikte nasıl uygulanır?

- [ ] Beş karar alanı için yukarıdaki gibi bir matris yazın ve yönetimde onaylayın.
- [ ] Bir BT yönlendirme kurulu kurun; üyeleri, toplanma sıklığını ve yetkisini belirleyin.
- [ ] Belirli bir tutarın üzerindeki her BT harcamasını kurul onayına bağlayın.
- [ ] Kurul kararlarını ve gerekçelerini kayıt altına alın.

## Daha fazlası

- Weill ve Ross, *IT Governance* (kitap; doğrulanmadı).
- ISACA, COBIT. https://www.isaca.org/resources/cobit
