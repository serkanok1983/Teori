---
id: kb-ea-19-3-working-with-it-partners
title: "BT iş ortaklarıyla çalışmak: Dış kaynak ve uygulama destek sözleşmesi"
summary: "Uygulama ortağı, yazılım evi ve destek firmasıyla çalışırken dış kaynak kararının mantığını; uygulama yönetim hizmeti (AMS) sözleşmesinin saat paketi, öncelik seviyeleri, raporlama ve ilişki yönetimi boyutlarını anlatır."
course: ea
category: yazilim-secimi-ve-proje
tags: [dis-kaynak, ams, sozlesme, sla, tedarikci]
roles: [it-yoneticisi]
level: orta
source_lessons: [EA-19.3]
reading_minutes: 3
key_points:
  - "Dış kaynak; uzmanlık ve esneklik sağlar ama bilgiyi ve kontrolü dışarı taşıma riski taşır."
  - "Başarılı ilişkilerde firma içinde sözleşmeyi ve işi yöneten yetkin bir ekip kalır."
  - "Uygulama destek sözleşmesinde saat paketi, öncelik seviyeleri ve yanıt süreleri net olmalıdır."
  - "Aylık raporda talep sayısı, çözüm süresi, harcanan saat ve tekrar eden sorunlar yer almalıdır."
  - "Dokümantasyon ve bilgi devri sözleşmenin parçası olmalıdır."
glossary_terms: [ams, sla]
related: [kb-ea-6-2-it-service-sla, kb-ea-17-4-vendor-selection-rfp, kb-ea-19-1-project-management-basics, kb-ea-1-5-software-vendor-economics-lockin]
sources:
  - title: "A review of the IT outsourcing literature: Insights for practice"
    authors: "Lacity, M.; Khan, S.; Willcocks, L."
    year: 2009
    type: article
    doi: "10.1016/j.jsis.2009.06.002"
    url: "https://doi.org/10.1016/j.jsis.2009.06.002"
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

Orta ölçekli üretici ve bayilerin çoğu, ERP ve saha uygulamalarının bakımını bir iş ortağına bırakır. Bu kart, iş ortağıyla ilişkiyi şikâyet döngüsünden çıkarıp ölçülebilir bir hizmete dönüştürmenize yardım eder.

## Temel fikir

Lacity, Khan ve Willcocks (2009), BT dış kaynak kullanımı üzerine yapılan çok sayıda çalışmayı özetler. Öne çıkan sonuçlardan bazıları:

- Dış kaynağa yalnızca maliyet düşürmek için gitmek çoğu zaman beklentiyi karşılamaz; uzmanlığa erişim ve odaklanma daha sağlam gerekçelerdir.
- Başarı için firmanın içinde **sözleşmeyi ve işi yöneten yetkin bir ekip** kalmalıdır.
- Ayrıntılı sözleşme ve iyi ilişki birbirinin alternatifi değil, tamamlayıcısıdır.

**Uygulama yönetim hizmeti** (AMS, *application management services*) sözleşmesinin ana maddeleri:

- **Kapsam:** Hangi sistemler, hangi işler (hata çözümü, küçük geliştirme, kullanıcı desteği, sürüm yükseltme).
- **Saat paketi:** Aylık sabit saat ve aşım fiyatı; kullanılmayan saatlerin devri.
- **Öncelik seviyeleri:** Ör. P1 "sevkiyat durdu", P4 "rapor biçimi". Her biri için yanıt ve çözüm süresi.
- **Raporlama:** Aylık talep sayısı, ortalama çözüm süresi, harcanan saat, tekrar eden sorunlar.
- **Bilgi devri ve dokümantasyon:** Her geliştirmenin yazılı kaydı; sözleşme biterse devir planı.
- **Kilit kişiler:** Sistemi bilen danışmanların izinsiz değiştirilmemesi.

### İlişkiyi sağlıklı yönetmek

Lacity, Khan ve Willcocks'un dış kaynak kullanımı üzerine çalışmaları, başarının büyük ölçüde sözleşmeden çok ilişkinin yönetimine bağlı olduğunu gösterir. Sağlıklı bir iş ortaklığı için şu uygulamalar önerilir:

- **İçeride yetkinlik tutun:** Tüm bilgiyi iş ortağına devretmek, şirketi bağımlı hâle getirir. Sistemin nasıl çalıştığını bilen, ihtiyaçları tanımlayabilen ve iş ortağının önerilerini değerlendirebilen bir iç ekip olmalıdır.
- **Tek iletişim noktası:** Her iki tarafta da ilişkiden sorumlu birer yönetici belirlenmelidir. Taleplerin farklı kanallardan dağınık gelmesi, önceliklerin karışmasına yol açar.
- **Düzenli toplantılar:** Aylık hizmet toplantılarında talep istatistikleri, açık konular ve saat paketi kullanımı gözden geçirilmelidir. Yıllık olarak ise ilişkinin genel değerlendirmesi yapılmalıdır.
- **Önceliklendirme:** Saat paketinin hangi işlere harcanacağına iş birimleri birlikte karar vermelidir. Aksi hâlde paket, en yüksek sesle talep eden birimin işlerine harcanır.
- **Belgelendirme:** İş ortağının yaptığı geliştirmelerin ve ayarların belgelenmesi, sözleşmede bir yükümlülük olarak yer almalıdır.

**Geçiş ve çıkış planı.** İş ortağının değiştirilmesi gerektiğinde bilginin nasıl devredileceği, kaynak kodların ve belgelerin kime ait olduğu ve geçiş döneminde desteğin nasıl süreceği önceden tanımlanmalıdır. Bu planın varlığı, ilişkide pazarlık gücünü de dengeler.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b4.py` ile yapılmıştır.

Bir bayinin ERP destek sözleşmesi aylık 80 saat, saati 2.000 TL. Bir ayda 15 saat aşım oluyor; aşım saati 2.400 TL:

- Paket: **160.000 TL**
- Aşım: **36.000 TL**
- Toplam: **196.000 TL**; aşım, toplam saatin **%15,8**'i.

Aylık raporda aşımın büyük kısmının aynı entegrasyon hatasının tekrar tekrar elle düzeltilmesinden geldiği görülüyor. Bayi, sorunun kökten çözülmesini ayrı bir iş olarak planlatıyor ve rapora "tekrar eden sorunlar" bölümünü zorunlu hale getiriyor.

## Sık yapılan hatalar

- Saat paketini takip etmeden faturayı ödemek.
- Tüm bilgiyi iş ortağında bırakıp içeride kimseyi yetiştirmemek.
- Öncelik seviyelerini tanımlamadan "acil" talepler göndermek.
- Geliştirmelerin dokümantasyonunu istememek.

## Pratikte nasıl uygulanır?

- [ ] Kapsamı, öncelik seviyelerini ve yanıt sürelerini sözleşmeye yazın.
- [ ] Aylık hizmet raporu ve üç ayda bir yönetim toplantısı isteyin.
- [ ] Tekrar eden sorunları kök neden çalışmasına dönüştürün.
- [ ] İçeride sistemi bilen en az bir kişi yetiştirin.
- [ ] Sözleşme sonu için bilgi devri maddesi koyun.

## Daha fazlası

- Lacity, Khan ve Willcocks (2009), *Journal of Strategic Information Systems*. https://doi.org/10.1016/j.jsis.2009.06.002
