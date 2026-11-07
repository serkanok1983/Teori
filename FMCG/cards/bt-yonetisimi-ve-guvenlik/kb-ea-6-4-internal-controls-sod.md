---
id: kb-ea-6-4-internal-controls-sod
title: "İç kontrol ve görevler ayrılığı: Denetçi ERP'nize nasıl bakar?"
summary: "ERP'deki iç kontrolleri, özellikle görevler ayrılığını, yetki gözden geçirmesini ve değişiklik kontrolünü anlatır; çakışan yetkileri basit bir SQL sorgusuyla bulmayı örnekler."
course: ea
category: bt-yonetisimi-ve-guvenlik
tags: [ic-kontrol, denetim, yetki, erp, sql]
roles: [finans-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-6.4]
reading_minutes: 2
key_points:
  - "İç kontrol, hataları ve suistimali önlemek veya fark etmek için kurulan kurallar ve kontrollerdir."
  - "Görevler ayrılığı: Aynı kişi bir işlemi hem başlatıp hem onaylayıp hem kaydedememelidir."
  - "BT genel kontrolleri; erişim, değişiklik ve işletim kontrollerinden oluşur."
  - "Yetkiler en az üç ayda bir, iş birimi yöneticisi tarafından gözden geçirilmelidir."
  - "Çakışan yetkiler sistemden düzenli raporlanabilir; bunun için pahalı araç şart değildir."
glossary_terms: [gorevler-ayriligi, erp]
related: [kb-ea-15-2-user-roles-permissions, kb-ea-4-9-workflow-approvals, kb-ea-6-1-it-governance-decision-rights, kb-ea-20-3-procure-to-pay]
sources:
  - title: "Internal Control — Integrated Framework (2013)"
    authors: "COSO"
    year: 2013
    type: standard
    verified: false
    note: "coso.org erişilemedi."
  - title: "CISA (ISACA)"
    authors: "ISACA"
    year: 2026
    type: web
    url: "https://www.isaca.org/credentialing/cisa"
    verified: true
    checked_on: 2026-10-28
    note: "URL HTTP 200 ile açıldı, başlık/kurum eşleşti (2026-10-28)."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28

---

## Ne işe yarar?

Bağımsız denetçi ya da büyük bir müşterinin tedarikçi denetimi ERP'nize baktığında ilk sorduğu şeylerden biri, kimin neyi yapabildiğidir. Bu kart, ERP'deki **iç kontrolün** (*internal control*) temelini, özellikle **görevler ayrılığını** (*segregation of duties*) ve bunun düzenli nasıl kontrol edileceğini anlatır.

## Temel fikir

COSO çerçevesi iç kontrolü beş bileşenle tanımlar: kontrol ortamı, risk değerlendirmesi, kontrol faaliyetleri, bilgi ve iletişim, izleme. ERP tarafında denetçinin baktığı **BT genel kontrolleri** üç gruptur:

- **Erişim kontrolü:** Kullanıcılar yalnızca işi için gereken yetkiye sahip mi? Ayrılanların hesabı kapatılıyor mu?
- **Değişiklik kontrolü:** Sistemdeki ayar ve kod değişiklikleri test edilip onaylanıyor mu?
- **İşletim kontrolü:** Yedekler alınıyor mu, otomatik işler hatasız çalışıyor mu?

Görevler ayrılığının amacı, tek bir kişinin hata ya da suistimali tek başına yapıp gizleyememesidir. Tipik çakışan yetki çiftleri:

- Tedarikçi veya cari kart açmak + ödeme onaylamak
- Fatura kesmek + tahsilat kaydetmek
- Fiyat listesini değiştirmek + sipariş onaylamak
- Stok sayım farkını girmek + sayım farkını onaylamak

Küçük ekiplerde tam ayrılık mümkün olmayabilir. O zaman **telafi edici kontrol** kullanılır: Örneğin yöneticinin haftalık olarak riskli işlemleri gözden geçirmesi.

### Denetime hazırlanmak

Denetçinin sorularına hazırlıklı olmak, denetim süresini ve bulgu sayısını azaltır. Hazırlık için şu belgelerin güncel tutulması önerilir: kullanıcı ve rol listesi, kritik yetkilere sahip kullanıcılar, görevler ayrılığı çakışma raporu ve kabul edilen çakışmalar için telafi edici kontroller, değişiklik talepleri ve onayları, periyodik yetki gözden geçirmelerinin kayıtları. Küçük ekiplerde görevler ayrılığını tam sağlamak her zaman mümkün değildir; bu durumda yönetici gözden geçirmesi veya istisna raporları gibi telafi edici kontroller belgelenmelidir. COSO çerçevesi, kontrollerin risklerle ilişkilendirilerek tasarlanmasını önerir.

## Bir örnek

> **Örnek (temsili rakamlar):** Kullanıcılar ve yetkiler uydurmadır; sorgu `scripts/cards_numbers_ea_b2.py` içinde SQLite ile çalıştırılmış ve çıktı aynen aktarılmıştır.

ERP'den alınan kullanıcı–işlem yetki listesi `yetki(kullanici, islem)` tablosunda. Cari kart açma ve ödeme onaylama yetkisini birlikte taşıyanları bulan sorgu:

```sql
select a.kullanici from yetki a join yetki b on a.kullanici=b.kullanici
where a.islem='cari_kart_ac' and b.islem='odeme_onayla' order by 1;
```

Sonuç: **ali** ve **ayse**. İki kullanıcı yeni bir tedarikçi açıp ona ödeme onaylayabiliyor. Finans müdürü Ayşe'nin cari kart açma yetkisini kaldırıyor. Ali'nin iki yetkiye de gerçekten ihtiyacı olduğu için yetki kalıyor, ama Ali'nin açtığı yeni carilere yapılan ödemeler haftalık olarak genel müdüre raporlanıyor.

## Sık yapılan hatalar

- Herkese "tam yetki" vermek, sonra kısıtlamayı ertelemek.
- Ayrılan çalışanların ya da tedarikçi danışmanlarının hesaplarını açık bırakmak.
- Yetki gözden geçirmesini BT'ye bırakmak; işi bilen yönetici bakmalıdır.
- Canlı sistemde test edilmemiş değişiklik yapmak.
- Telafi edici kontrolü yazıp uygulamamak.

## Pratikte nasıl uygulanır?

- [ ] Firmanız için 5–10 çakışan yetki çiftini finans ile birlikte listeleyin.
- [ ] ERP'den kullanıcı–yetki listesini alıp çakışmaları ayda bir raporlayın.
- [ ] Yetkileri üç ayda bir iş birimi yöneticisine onaylatın.
- [ ] İşten çıkışta hesap kapatmayı İK süreci ile bağlayın.
- [ ] Kaçınılmaz çakışmalar için telafi edici kontrolü ve sorumlusunu yazın.

## Daha fazlası

- COSO, *Internal Control — Integrated Framework* (2013) (erişilemedi; doğrulanmadı).
- ISACA, CISA bilgi alanları. https://www.isaca.org/credentialing/cisa
