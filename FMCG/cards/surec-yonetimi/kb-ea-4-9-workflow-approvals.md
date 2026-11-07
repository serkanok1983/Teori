---
id: kb-ea-4-9-workflow-approvals
title: "İş akışı ve onay süreçleri: Kim neyi, hangi tutara kadar onaylar?"
summary: "İskonto, iade, satın alma ve harcama onaylarını e-posta ve kâğıttan çıkarıp kurala bağlı bir iş akışına taşımayı; onay matrisini tasarlamayı ve bekleme süresini ölçmeyi anlatır."
course: ea
category: surec-yonetimi
tags: [surec, onay, is-akisi, iskonto, ic-kontrol]
roles: [it-yoneticisi]
level: orta
source_lessons: [EA-4.9, EA-35.3]
reading_minutes: 3
key_points:
  - "İş akışı yazılımı, bir talebi kurallara göre doğru kişiye yönlendirir, bekletir, hatırlatır ve kaydını tutar."
  - "Onay matrisi; işlem türü, tutar eşiği ve onaylayıcı rolünden oluşur."
  - "Onayların çoğu alt kademede bitmeli; üst yöneticiye yalnızca gerçekten önemli talepler gitmelidir."
  - "Her onay adımına süre sınırı ve vekil tanımlanmazsa iş akışı yeni bir darboğaz olur."
  - "Onay kaydı, iç kontrol ve denetim için kanıttır."
glossary_terms: [is-akisi, gorevler-ayriligi]
related: [kb-ea-4-3-process-maps-bpmn, kb-ea-6-4-internal-controls-sod, kb-ea-39-1-low-code, kb-ea-15-2-user-roles-permissions]
sources:
  - title: "Business Process Management: Concepts, Languages, Architectures"
    authors: "Weske, M."
    year: 2019
    type: book
    verified: false
    note: "3. baskı yılı kontrol edilmeli."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

"Bu iskontoyu kim onayladı?" sorusunun cevabı bir WhatsApp mesajında, bir e-postada ya da kimsenin hatırlamadığı bir telefon görüşmesindeyse, hem süreç yavaştır hem de kontrol zayıftır. Bu kart, onayları kurala bağlı bir **iş akışına** (*workflow*) taşımayı ve onay matrisini doğru kurmayı anlatır. Satış yöneticisi hızı, finans müdürü kontrolü, BT yöneticisi de kurulum seçeneklerini burada bulur.

## Temel fikir

İş akışı yazılımı (ayrı bir ürün, ERP'nin onay modülü ya da düşük kodlu bir platform olabilir) bir talebi alır ve:

- kurala göre doğru onaylayıcıya yönlendirir,
- süre dolunca hatırlatır ya da bir üst kademeye taşır,
- onaylayıcı yoksa vekiline gönderir,
- kim, ne zaman, hangi gerekçeyle onayladı bilgisini değiştirilemez şekilde kaydeder.

Bu yapının kalbi **onay matrisidir**: işlem türü × tutar ya da oran eşiği × onaylayıcı rol. Örneğin fatura altı ek iskonto için %2'ye kadar şef, %2–5 arası müdür, %5 üstü direktör.

İyi bir matris iki şeyi dengeler: hız ve kontrol. Her talebin üst yöneticiye gitmesi kontrol sağlamaz; yönetici okumadan onaylamaya başlar. Ayrıca talebi oluşturan kişinin kendi talebini onaylayamaması gerekir. Bu, **görevler ayrılığı** (*segregation of duties*) ilkesinin basit bir uygulamasıdır.

İki tür süreç ayrılmalıdır. Yapısı belli, tekrar eden işler (iskonto, satın alma talebi) kural tabanlı iş akışına uygundur. Her seferinde farklı ilerleyen işler (büyük bir müşteri şikâyeti) ise vaka yönetimi (*case management*) mantığıyla, esnek görev listeleriyle yürütülür.

### Onay matrisinin bakımı

Onay matrisi, organizasyon değiştikçe güncellenmelidir. Görevden ayrılan veya pozisyon değiştiren yöneticilerin onay yetkileri zamanında devredilmezse, iş akışları ya durur ya da yetkisiz kişiler tarafından onaylanır. Bu nedenle onay yetkileri kişilere değil, pozisyonlara bağlanmalı ve insan kaynakları sistemindeki değişikliklerle otomatik olarak güncellenmelidir. Vekâlet kuralları da sistemde tanımlanmalı, vekâleten verilen onaylar ayrıca raporlanmalıdır. Weske'nin vurguladığı gibi, iş akışı modeli ile organizasyon modelinin ayrı tutulması bu esnekliği sağlar.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b1.py` ile yapılmıştır.

Bir bayide ayda 600 ek iskonto talebi var. Eskiden tüm talepler satış direktörüne e-postayla gidiyordu; ortalama onay bekleme süresi 26 saatti. Yeni matris:

| Ek iskonto | Onaylayıcı | Talep payı | Aylık talep |
|---|---|---|---|
| %2'ye kadar | Satış şefi | %70 | 420 |
| %2–5 | Satış müdürü | %25 | 150 |
| %5 üstü | Satış direktörü | %5 | 30 |

Direktöre giden talep 600'den **30**'a iniyor. Her kademeye 4 saatlik süre sınırı ve vekil tanımlandıktan sonra ortalama bekleme 4,5 saate düşüyor; bu **%82,7**'lik bir azalma. Direktör artık yalnızca gerçekten önemli talepleri görüyor ve her birine bakabiliyor.

## Sık yapılan hatalar

- Matrisi kurup eşikleri hiç gözden geçirmemek; enflasyonla tutar eşikleri anlamını yitirir.
- Vekil ve süre sınırı tanımlamamak; tatildeki yöneticide iş yığılması.
- Talep sahibinin kendi talebini onaylayabilmesi.
- Onayın sistem dışında (telefonla) alınıp sisteme sonradan "temsilen" girilmesi.
- Her istisna için yeni bir onay adımı ekleyip süreci uzatmak.

## Pratikte nasıl uygulanır?

- [ ] Onay gerektiren işlemleri listeleyin: iskonto, iade, kredi limiti aşımı, satın alma, masraf.
- [ ] Her biri için eşik ve onaylayıcı rolü içeren bir matris yazın; finans ile birlikte onaylayın.
- [ ] Her adıma süre sınırı, hatırlatma ve vekil tanımlayın.
- [ ] Talep sahibinin kendi talebini onaylayamadığını test edin.
- [ ] Aylık olarak onay bekleme süresini ve kademe başına talep sayısını raporlayın.
- [ ] Tutar eşiklerini yılda en az bir kez, enflasyonu dikkate alarak güncelleyin.

## Daha fazlası

- Weske, *Business Process Management: Concepts, Languages, Architectures* (kitap; doğrulanmadı).
