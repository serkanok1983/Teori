---
id: kb-ea-19-1-project-management-basics
title: "Proje yönetimi temelleri: Kapsam, süre, maliyet ve kazanılmış değer"
summary: "BT projelerinde kapsam, süre ve maliyet dengesini, risk kaydını, değişiklik kontrolünü ve projenin gerçek durumunu gösteren kazanılmış değer yöntemini (CPI, SPI) anlatır."
course: ea
category: yazilim-secimi-ve-proje
tags: [proje-yonetimi, risk, kazanilmis-deger, butce]
roles: [it-yoneticisi]
level: orta
source_lessons: [EA-19.1]
reading_minutes: 3
key_points:
  - "Kapsam, süre ve maliyetten biri değişirse diğerleri de etkilenir."
  - "Risk kaydı; olasılık, etki, sahip ve önlemle birlikte düzenli güncellenmelidir."
  - "Kazanılmış değer, harcanan parayla bitirilen işi karşılaştırır."
  - "CPI 1'in altındaysa maliyet, SPI 1'in altındaysa takvim sorunu vardır."
  - "Değişiklik talepleri etkisi hesaplanmadan kabul edilmemelidir."
glossary_terms: [kazanilmis-deger, risk-kaydi]
related: [kb-ea-18-5-implementation-methodology, kb-ea-19-3-working-with-it-partners, kb-ea-18-3-why-erp-projects-fail, kb-ea-17-2-total-cost-of-ownership]
sources:
  - title: "A Guide to the Project Management Body of Knowledge (PMBOK Guide), 7. baskı"
    authors: "Project Management Institute"
    year: 2021
    type: book
    verified: false
    note: "PMI sitesi otomatik erişime kapalı; kitap içeriği kontrol edilmedi."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

"Proje %50'de" cümlesi genellikle harcanan bütçeyi ya da geçen süreyi anlatır, tamamlanan işi değil. Bu kart, bir BT projesinin gerçek durumunu birkaç basit göstergeyle okumanızı sağlar.

## Temel fikir

Proje Yönetim Enstitüsü'nün (PMI) rehberi PMBOK'un son baskısı, proje yönetimini paydaşlar, ekip, planlama, belirsizlik ve ölçüm gibi performans alanları üzerinden ele alır. Yöneticinin bilmesi gereken temel kavramlar:

- **Kapsam, süre, maliyet:** Birini değiştirince diğerleri de etkilenir. Yeni bir rapor isteği ya süreyi ya maliyeti artırır ya da başka bir işi kapsam dışına iter.
- **Değişiklik kontrolü:** Her değişiklik talebi yazılır, etkisi hesaplanır ve yetkili kurul tarafından onaylanır.
- **Risk kaydı:** Her risk için olasılık, etki, sahip ve önlem yazılır; liste her hafta güncellenir.
- **Kazanılmış değer** (*earned value*):
  - **PV** (planlanan değer): Bugüne kadar yapılması planlanan işin bütçesi.
  - **EV** (kazanılmış değer): Bugüne kadar gerçekten bitirilen işin bütçesi.
  - **AC** (gerçekleşen maliyet): Bugüne kadar harcanan.
  - **CPI = EV / AC** (maliyet performansı) ve **SPI = EV / PV** (takvim performansı). 1'in altı kötü demektir.
  - Tamamlanma tahmini: **EAC = toplam bütçe / CPI**.

### Bir ERP projesinde proje yönetiminin günlük pratiği

Proje yönetimi yöntemleri, ancak düzenli uygulandığında değer üretir. Bir ERP veya iş uygulaması projesinde günlük pratik şu unsurlardan oluşur:

- **Proje başlatma belgesi:** Projenin amacı, kapsamı, kapsam dışı konular, başarı ölçütleri, bütçe, ana kilometre taşları ve rol dağılımı tek bir belgede yazılmalı ve sponsor tarafından onaylanmalıdır.
- **Haftalık durum raporu:** Tamamlanan işler, gecikmeler, açık riskler ve karar bekleyen konular kısa bir formatta raporlanmalıdır. Durum rengi, gerçek ilerlemeyi yansıtmalı; sorunlar gizlenmemelidir.
- **Karar kaydı:** Projede alınan önemli kararlar, kimin tarafından ve hangi gerekçeyle alındığıyla birlikte kayıt altına alınmalıdır. Bu kayıt, aylar sonra tekrarlanan tartışmaları önler.
- **Risk ve sorun ayrımı:** Risk henüz gerçekleşmemiş bir olasılıktır; sorun ise gerçekleşmiş bir durumdur. Her ikisi de sahibi ve eylem planıyla izlenmelidir.
- **İş birimi kaynakları:** Kilit kullanıcıların projeye ayıracağı zaman, yöneticileriyle yazılı olarak kararlaştırılmalıdır. Günlük işlerinin azaltılmadığı kullanıcılar, projeye yeterli katkı veremez.

**Uyarlanabilir yaklaşım.** PMBOK'un güncel sürümü, tahmine dayalı ve uyarlanabilir yöntemlerin proje koşullarına göre birlikte kullanılabileceğini vurgular. Örneğin ERP çekirdeği planlı aşamalarla yürütülürken, raporlama ve saha uygulaması gibi bileşenler kısa döngülerle geliştirilebilir.

**Sponsorun rolü.** Proje sponsoru, öncelik çatışmalarını çözen, kaynak sağlayan ve değişikliğin gerekliliğini şirket içinde savunan kişidir. Sponsorun düzenli olarak projeye zaman ayırması, başarı için belirleyicidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b4.py` ile yapılmıştır.

Bir saha satış projesinin toplam bütçesi 1.200.000 TL. Plana göre bugün işin %50'si bitmiş olmalıydı; gerçekte %40'ı bitti ve 560.000 TL harcandı.

| Gösterge | Değer |
|---|---|
| PV | 600.000 TL |
| EV | 480.000 TL |
| AC | 560.000 TL |
| CPI | 0,86 |
| SPI | 0,80 |
| Tamamlanma tahmini (EAC) | 1.400.000 TL |

Proje hem pahalıya hem de geç ilerliyor. Bu gidişle toplam maliyet 1.400.000 TL'ye çıkacak. Yönlendirme kurulu iki rapor isteğini ikinci faza erteliyor ve en büyük risk olan entegrasyon testine ek kaynak veriyor.

## Sık yapılan hatalar

- İlerlemeyi harcanan bütçe veya geçen süreyle ölçmek.
- "%90 bitti" denilen işleri olduğu gibi kabul etmek; iş ya bitmiştir ya bitmemiştir.
- Risk kaydını proje başında yazıp bir daha açmamak.
- Küçük değişiklikleri kayıt altına almamak; toplamları büyür.

## Pratikte nasıl uygulanır?

- [ ] Projeyi ölçülebilir teslimatlara bölün ve her birine bütçe atayın.
- [ ] Aylık raporda PV, EV, AC, CPI ve SPI isteyin.
- [ ] Risk kaydını yönlendirme kurulunda her toplantıda gözden geçirin.
- [ ] Değişiklik talepleri için tek sayfalık bir form ve onay yolu tanımlayın.

## Daha fazlası

- PMI, *PMBOK Guide*, 7. baskı (kitap; doğrulanmadı).
