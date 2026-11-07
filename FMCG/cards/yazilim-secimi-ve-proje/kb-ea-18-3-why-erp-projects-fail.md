---
id: kb-ea-18-3-why-erp-projects-fail
title: "ERP projeleri neden başarısız olur? Kritik başarı ve risk faktörleri"
summary: "ERP projelerinin bütçe ve süreyi neden aştığını; araştırmalarda öne çıkan kritik başarı faktörlerini (üst yönetim desteği, net kapsam, güçlü proje ekibi, veri, değişim yönetimi) ve risk işaretlerini anlatır."
course: ea
category: yazilim-secimi-ve-proje
tags: [erp, proje, risk, basari-faktorleri]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, it-yoneticisi]
level: orta
source_lessons: [EA-18.1, EA-18.2, EA-18.3]
reading_minutes: 2
key_points:
  - "ERP projelerinin çoğu teknik değil, örgütsel nedenlerle sorun yaşar."
  - "Üst yönetimin sahiplenmesi, en sık tekrarlanan kritik başarı faktörüdür."
  - "Kapsamın sürekli genişlemesi ve aşırı özelleştirme, süre ve bütçeyi en çok büyüten risklerdir."
  - "En iyi çalışanlarınızı projeye vermezseniz sistem işinizi öğrenemez."
  - "Veri temizliği ve kullanıcı eğitimi proje planında ayrı iş paketleri olmalıdır."
glossary_terms: [erp, kritik-basari-faktoru]
related: [kb-ea-18-4-post-go-live-dip, kb-ea-18-5-implementation-methodology, kb-ea-18-7-change-management-training, kb-ea-17-1-build-buy-configure]
sources:
  - title: "A critical success factors model for ERP implementation"
    authors: "Holland, C.; Light, B."
    year: 1999
    type: article
    doi: "10.1109/52.765784"
    url: "https://doi.org/10.1109/52.765784"
    verified: true
    checked_on: 2026-10-28
  - title: "Risk factors in enterprise-wide/ERP projects"
    authors: "Sumner, M."
    year: 2000
    type: article
    doi: "10.1080/02683960010009079"
    url: "https://doi.org/10.1080/02683960010009079"
    verified: true
    checked_on: 2026-10-28
  - title: "Critical factors for successful implementation of enterprise systems"
    authors: "Fui‐Hoon Nah, F.; Lee‐Shang Lau, J.; Kuang, J."
    year: 2001
    type: article
    doi: "10.1108/14637150110392782"
    url: "https://doi.org/10.1108/14637150110392782"
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

ERP projeleri, bir firmanın yapacağı en pahalı ve en riskli BT yatırımları arasındadır. Bu kart, araştırmalarda tekrar tekrar karşımıza çıkan başarı ve başarısızlık nedenlerini proje başlamadan önce kontrol edebileceğiniz bir listeye çevirir.

## Temel fikir

Holland ve Light (1999), Nah ve arkadaşları (2001) ve Sumner (2000) farklı firmalardaki ERP projelerini inceleyerek benzer sonuçlara ulaşır: Sorunların çoğu yazılımdan değil, projenin yönetiminden kaynaklanır.

**Kritik başarı faktörleri** (öne çıkanlar):

- **Üst yönetimin sahiplenmesi:** Karar verebilen bir yöneticinin projeye düzenli zaman ayırması.
- **Net kapsam ve iş gerekçesi:** Neyin projeye girdiği ve neyin girmediği yazılı olmalıdır.
- **Güçlü proje ekibi:** İşi en iyi bilen çalışanların projeye ayrılması.
- **Süreç uyumu ve az özelleştirme:** Süreci pakete uydurmaya istekli olmak.
- **Veri ve test:** Veri temizliği ve gerçekçi testler için yeterli zaman.
- **Değişim yönetimi ve eğitim.**

**Risk işaretleri** (Sumner'ın vurguladıkları dahil): kapsamın sürekli genişlemesi, iç kadronun deneyimsizliği, danışmana aşırı bağımlılık, ERP'yi bir BT projesi olarak görmek ve proje ekibinin günlük işleriyle birlikte projeyi yürütmek zorunda kalması.

### Projenin ortasında risk değerlendirmesi

Risk işaretleri, proje başında olduğu kadar proje sürerken de düzenli olarak değerlendirilmelidir. Yönlendirme kurulu, her toplantıda şu soruları sorabilir: Kilit kullanıcılar planlanan zamanı ayırabiliyor mu? Açık tasarım kararlarının sayısı azalıyor mu, artıyor mu? Özelleştirme talepleri kontrol altında mı? Veri taşıma provaları planlandığı gibi ilerliyor mu? Bu soruların dürüstçe cevaplanması, sorunların büyümeden görülmesini sağlar. Holland ve Light'ın modeli, stratejik ve taktik faktörlerin proje aşamalarına göre ağırlık değiştirdiğini gösterir; bu nedenle aynı kontrol listesi her aşamada farklı vurgularla kullanılmalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b4.py` ile yapılmıştır.

Bir üreticinin ERP projesi 8 ay ve 3.000.000 TL olarak planlanıyor; 13 ay ve 4.200.000 TL'de tamamlanıyor. Süre sapması **%62,5**, bütçe sapması **%40,0**.

Proje sonrası değerlendirmede nedenler şöyle sıralanıyor:

- Projeye satış ve depo süreçlerini en iyi bilen kişiler değil, "o sırada müsait olanlar" verilmiş.
- Gerçekleştirme aşamasında 31 yeni rapor ve ekran isteği kapsamı genişletmiş.
- Müşteri ve ürün verisi temizliği son aya kalmış; test verisi gerçekçi olmamış.
- Genel müdür yalnızca açılış ve kapanış toplantılarına katılmış.

Firma, sonraki fazda bir yönlendirme kurulu kuruyor, değişiklik taleplerini bu kurula bağlıyor ve kilit kullanıcıların zamanının yarısını projeye ayırıyor.

## Sık yapılan hatalar

- ERP'yi BT'nin projesi olarak görmek.
- Kapsam değişikliklerini kayıt altına almadan kabul etmek.
- Veri temizliğini ve eğitimi "en sona" bırakmak.
- Proje ekibine günlük işlerinden zaman açmamak.

## Pratikte nasıl uygulanır?

- [ ] Projeye karar yetkisi olan bir sponsor ve haftalık toplanan bir yönlendirme kurulu atayın.
- [ ] Kapsamı yazılı hale getirin; her değişikliği etkisiyle birlikte kurula götürün.
- [ ] Kilit kullanıcıların proje için ayrılan zamanını yazılı olarak planlayın.
- [ ] Veri temizliği ve eğitimi proje planında ayrı iş paketleri yapın.

## Daha fazlası

- Holland ve Light (1999), *IEEE Software*. https://doi.org/10.1109/52.765784
- Sumner (2000), *Journal of Information Technology*. https://doi.org/10.1080/02683960010009079
- Nah ve ark. (2001), *Business Process Management Journal*. https://doi.org/10.1108/14637150110392782
