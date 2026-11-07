---
id: kb-ea-4-3-process-maps-bpmn
title: "Süreç haritası çizmek: BPMN'in temel öğeleri ve iyi model kuralları"
summary: "Süreç haritalarında yaygın kullanılan BPMN gösteriminin temel öğelerini (olay, faaliyet, karar noktası, kulvar) ve okunabilir bir model için uyulacak basit kuralları bir kredi limiti kontrolü örneğiyle anlatır."
course: ea
category: surec-yonetimi
tags: [surec, bpmn, siparis, kredi-limiti, dokumantasyon]
roles: [it-yoneticisi]
level: orta
source_lessons: [EA-4.3, EA-4.4]
reading_minutes: 3
key_points:
  - "BPMN, süreçleri herkesin okuyabileceği ortak bir gösterimle çizmeyi sağlar."
  - "Dört temel öğe yeterlidir: olay, faaliyet, karar noktası ve kulvar."
  - "Her karar noktasında olası yolların tamamı ve her yolun payı gösterilmelidir."
  - "İyi model küçük, tek başlangıçlı ve fiil–nesne biçiminde adlandırılmış faaliyetlerden oluşur."
  - "Model, yazılım ekibine verilecek gereksinimin temelidir; belirsiz harita belirsiz yazılım üretir."
glossary_terms: [bpmn, is-sureci]
related: [kb-ea-4-2-bpm-lifecycle, kb-ea-4-9-workflow-approvals, kb-ea-17-3-writing-requirements, kb-ea-24-3-credit-limits-collections-systems]
sources:
  - title: "Business Process Model and Notation (BPMN) Version 2.0.2"
    authors: "Object Management Group"
    year: 2014
    type: standard
    url: "https://www.omg.org/spec/BPMN/2.0.2/"
    verified: true
    checked_on: 2026-10-28
  - title: "Seven process modeling guidelines (7PMG)"
    authors: "Mendling, J.; Reijers, H. A.; van der Aalst, W. M. P."
    year: 2010
    type: article
    doi: "10.1016/j.infsof.2009.08.004"
    url: "https://doi.org/10.1016/j.infsof.2009.08.004"
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

Süreci konuşurken herkes kafasındaki farklı bir resmi anlatır. Kâğıda dökülmüş, ortak bir dille çizilmiş bir harita bu tartışmayı kısaltır. Bu kart, en yaygın süreç gösterimi olan **BPMN**'in (*Business Process Model and Notation*) yönetici için yeterli olan çekirdeğini ve okunur bir harita için birkaç basit kuralı anlatır. Yazılım firmasına gereksinim anlatırken ya da iç denetimde kontrolleri gösterirken işe yarar.

## Temel fikir

BPMN, Object Management Group'un yayımladığı bir standarttır. Yüzlerce sembolü olsa da günlük kullanım için dört öğe yeterlidir:

| Öğe | Şekil | Anlamı |
|---|---|---|
| Olay | Daire | Sürecin başlangıcı, bitişi ya da arada beklenen bir şey (ör. "ödeme geldi") |
| Faaliyet | Köşeleri yuvarlak dikdörtgen | Yapılan iş (ör. "limit kontrol et") |
| Karar noktası (*gateway*) | Baklava | Yolun ayrıldığı ya da birleştiği yer |
| Kulvar (*lane*) | Yatay şerit | İşi yapan rol ya da birim |

Farklı firmalar arasındaki yazışmalar (ör. bayi ile müşteri arasında sipariş) ayrı havuzlarda (*pool*) çizilir ve kesik çizgili mesaj oklarıyla bağlanır.

Mendling, Reijers ve van der Aalst (2010), anlaşılır model için yedi kural önerir. Yönetici için özeti şudur:

- Modeli küçük tutun; çok büyükse alt süreçlere bölün.
- Tek başlangıç ve tek bitiş olayı kullanın.
- Faaliyetleri fiil–nesne biçiminde adlandırın: "Sipariş onayla", "Limiti kontrol et".
- Ayrılan yollar mümkünse aynı tür karar noktasıyla yeniden birleşsin.

Başka gösterimler de vardır: olay güdümlü süreç zinciri (EPC), değer akış haritası. Değer akış haritası bekleme sürelerini göstermek için, BPMN ise kimin neyi yaptığını ve karar kurallarını göstermek için daha uygundur.

### Modeli kim için çiziyorsunuz?

Aynı süreç için farklı okuyuculara farklı ayrıntı düzeyinde modeller gerekebilir. Yöneticiler için ana adımları ve sorumluları gösteren sade bir genel bakış yeterliyken, sistem tasarımı için istisnaları ve olayları içeren ayrıntılı bir model gerekir. Modelin amacını ve okuyucusunu baştan belirlemek, gereksiz karmaşıklığı önler.

## Bir örnek

> **Örnek (temsili rakamlar):** Oranlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b1.py` ile yapılmıştır.

Kredi limiti kontrollü sipariş sürecinin metinle anlatılmış BPMN modeli:

1. **Başlangıç olayı:** Sipariş alındı (kulvar: Saha temsilcisi).
2. **Faaliyet:** Limiti kontrol et (kulvar: Sistem).
3. **Karar noktası (dışlayıcı):** "Açık bakiye + sipariş tutarı limiti aşıyor mu?"
   - Hayır → 5. adıma.
   - Evet → **Faaliyet:** Limit aşımını değerlendir (kulvar: Satış müdürü) → **Karar noktası:** "Onaylandı mı?" Evet → 5. adıma; Hayır → **Bitiş olayı:** Sipariş reddedildi.
5. **Faaliyet:** Sevkiyatı planla (kulvar: Depo) → **Bitiş olayı:** Sipariş sevke hazır.

Ayda 1.000 sipariş için, siparişlerin %18'i limiti aşıyor ve bunların %60'ı onaylanıyorsa:

- Limit aşan: **180**; onaylanan: **108**; reddedilen: **72**.
- Doğrudan geçen: **820**; sevke giden toplam: 820 + 108 = **928**.

Satış müdürünün ayda 180 karar verdiği görülüyor. Model, "limit aşımı %5'in altındaysa şef onaylasın" gibi bir kural tartışmasını rakamla yapmayı sağlar.

## Sık yapılan hatalar

- Tek sayfaya her istisnayı sığdırmaya çalışmak.
- Karar noktalarında "hayır" yolunu çizmeyi unutmak.
- Faaliyetleri "Muhasebe" gibi birim adlarıyla adlandırmak; ne yapıldığını yazmamak.
- Modeli bir kez çizip süreç değiştiğinde güncellememek.

## Pratikte nasıl uygulanır?

- [ ] Kritik 3–5 sürecinizi dört temel BPMN öğesiyle çizin.
- [ ] Her karar noktasına kuralı ve aylık vaka sayısını yazın.
- [ ] Kulvarları rol adıyla (kişi adıyla değil) adlandırın.
- [ ] Modeli süreçteki kişilere okutun; "gerçekte böyle mi oluyor?" diye sorun.
- [ ] Yazılım gereksinim dokümanına modeli ek olarak koyun.

## Daha fazlası

- Object Management Group, BPMN 2.0.2. https://www.omg.org/spec/BPMN/2.0.2/
- Mendling, Reijers ve van der Aalst (2010), *Information and Software Technology*. https://doi.org/10.1016/j.infsof.2009.08.004
