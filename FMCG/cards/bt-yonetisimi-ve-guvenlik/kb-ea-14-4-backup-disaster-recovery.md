---
id: kb-ea-14-4-backup-disaster-recovery
title: "Yedekleme ve felaket kurtarma: RPO ve RTO ile düşünmek"
summary: "Kabul edilebilir veri kaybını (RPO) ve kabul edilebilir kesinti süresini (RTO) iş diliyle tanımlamayı, 3-2-1 yedekleme kuralını ve geri yükleme testinin neden yedeğin kendisi kadar önemli olduğunu anlatır."
course: ea
category: bt-yonetisimi-ve-guvenlik
tags: [yedekleme, felaket-kurtarma, rpo, rto, guvenlik]
roles: [uretici-sahibi, bayi-sahibi, it-yoneticisi]
level: orta
source_lessons: [EA-14.4]
reading_minutes: 3
key_points:
  - "RPO, en fazla ne kadarlık veriyi kaybetmeyi göze aldığınızdır."
  - "RTO, sistemin en geç ne kadar sürede yeniden çalışması gerektiğidir."
  - "RPO ve RTO teknik değil iş kararıdır; kısaldıkça maliyet artar."
  - "3-2-1 kuralı: üç kopya, iki farklı ortam, bir kopya başka yerde ve tercihen değiştirilemez."
  - "Test edilmemiş yedek, yedek sayılmaz; geri yükleme düzenli olarak denenmelidir."
glossary_terms: [rpo, rto]
related: [kb-ea-6-2-it-service-sla, kb-ea-6-3-information-security-basics, kb-ea-16-1-cloud-saas-basics, kb-ea-15-2-user-roles-permissions]
sources:
  - title: "Contingency Planning Guide for Federal Information Systems (SP 800-34 Rev. 1)"
    authors: "NIST"
    year: 2010
    type: standard
    url: "https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final"
    verified: true
    checked_on: 2026-10-28
    note: "URL HTTP 200 ile açıldı, başlık/kurum eşleşti (2026-10-28)."
  - title: "NIST Cybersecurity Framework 2.0"
    authors: "NIST"
    year: 2024
    type: standard
    url: "https://www.nist.gov/cyberframework"
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

Fidye yazılımı, disk arızası, yanlışlıkla silinen tablo… Soru "olur mu" değil, "olduğunda ne kadar kaybederiz"dir. Bu kart, yedekleme kararını iki rakamla iş diline çevirir.

## Temel fikir

NIST'in olağanüstü durum planlama rehberi (SP 800-34) iki hedef tanımlar:

- **RPO** (*recovery point objective*): Geri döneceğiniz noktanın en fazla ne kadar eski olabileceği. Gece yedek alınıyorsa RPO en kötü durumda neredeyse bir gündür.
- **RTO** (*recovery time objective*): Sistemin en geç ne kadar sürede çalışır hale gelmesi gerektiği.

Bu iki hedef teknik ekibe bırakılmamalıdır; çünkü cevap, "bir günlük siparişi yeniden girebilir miyiz?" ve "ERP olmadan kaç saat sevk yapabiliriz?" sorularına bağlıdır. RPO ve RTO kısaldıkça sık yedek, ikinci sunucu, yedek veri merkezi gibi maliyetler artar.

Yaygın bir pratik olan **3-2-1 kuralı**: verinin üç kopyası, iki farklı ortamda, en az biri başka bir konumda. Fidye yazılımlarına karşı bu kopyalardan birinin **değiştirilemez** (silinemez, şifrelenemez) olması önerilir. NIST Siber Güvenlik Çerçevesi de kurtarma (*recover*) işlevini ayrı bir başlık olarak ele alır.

En sık atlanan adım **geri yükleme testidir**: Yedek alındığını gösteren yeşil işaret, verinin geri getirilebildiğini kanıtlamaz.

### Planı test etmek ve güncel tutmak

Yedekleme ve felaket kurtarma planları, test edilmediği sürece yalnızca bir varsayımdır. Planın gerçekten işe yaraması için şu uygulamalar önerilir:

- **Düzenli geri yükleme testi:** Yedeklerin alındığını görmek yetmez; belirli aralıklarla bir yedekten geri yükleme yapılarak verinin eksiksiz ve kullanılabilir olduğu doğrulanmalıdır.
- **Felaket kurtarma tatbikatı:** Yılda en az bir kez, ana sistemin kullanılamadığı varsayılarak yedek ortamda çalışma denenmelidir. Tatbikatta geçen süre, hedeflenen kurtarma süresiyle karşılaştırılmalıdır.
- **Yedeklerin korunması:** Fidye yazılımları, ağdaki yedekleri de şifreleyebilir. Yedeklerin en az bir kopyasının ağdan ayrı veya değiştirilemez biçimde saklanması önerilir.
- **Bağımlılıkların listesi:** ERP'nin çalışması için gereken diğer sistemler (kimlik doğrulama, e-belge entegratörü, ağ bağlantısı) da kurtarma planında yer almalıdır.
- **İletişim planı:** Kesinti sırasında kimin karar vereceği, çalışanlara, müşterilere ve tedarikçilere nasıl bilgi verileceği önceden belirlenmelidir.

**Hedefleri iş birimleriyle belirlemek.** Kabul edilebilir veri kaybı ve kesinti süresi, BT tarafından değil, iş birimleriyle birlikte belirlenmelidir. Daha kısa hedefler daha yüksek maliyet anlamına gelir; bu nedenle her sistem için iş etkisi ile maliyet arasında bilinçli bir denge kurulmalıdır.

**Bulut hizmetleri.** SaaS sağlayıcılarının yedekleme taahhütleri, şirketin hedefleriyle karşılaştırılmalıdır. NIST rehberleri, bu planlamanın sistematik biçimde yapılması için yol gösterir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b3.py` ile yapılmıştır.

Bir bayinin ERP'si her gece 23.00'te yedekleniyor. Ertesi gün saat 16.00'da sunucu arızalanıyor:

- Son yedekten bu yana geçen süre **17 saat**.
- 08.00–16.00 arasında saatte ortalama 40 sipariş girildiği için yeniden girilecek sipariş **320**.
- Sistemin ayağa kalkması 6 saat sürüyor; saatlik ciro 150.000 TL ile risk altındaki ciro **900.000 TL**.

Bayi, işlem günlüklerinin 15 dakikada bir başka konuma kopyalanmasına karar veriyor. Bu durumda kaybedilecek sipariş en fazla **10** oluyor. RTO için de yedek sunucuya geçiş prosedürü yazılıp yılda iki kez deneniyor.

## Sık yapılan hatalar

- Yedeği aynı sunucuda veya aynı ağda tutmak; fidye yazılımı yedeği de şifreler.
- Geri yüklemeyi hiç denememek.
- RPO ve RTO'yu iş birimlerine sormadan belirlemek.
- Bulut uygulamasında yedeğin tedarikçide olduğunu varsayıp sözleşmeyi kontrol etmemek.

## Pratikte nasıl uygulanır?

- [ ] Her kritik sistem için RPO ve RTO'yu iş birimiyle birlikte yazın.
- [ ] 3-2-1 kuralına uygun olup olmadığınızı kontrol edin; bir kopyayı değiştirilemez yapın.
- [ ] Yılda en az iki kez tam geri yükleme testi yapın ve süresini ölçün.
- [ ] Bulut hizmetlerinde yedekleme ve geri yükleme koşullarını sözleşmede arayın.

## Daha fazlası

- NIST SP 800-34 Rev. 1 (doğrulanmadı).
- NIST Siber Güvenlik Çerçevesi: https://www.nist.gov/cyberframework
