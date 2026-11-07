---
id: kb-ea-3-2-it-plus-process-complementarity
title: "Aynı yazılım, farklı sonuç: Teknoloji ile süreç değişikliğinin birlikteliği"
summary: "Aynı ERP'nin bir firmada kazanç, diğerinde hayal kırıklığı yaratmasının nedenini; yazılım yatırımının iş yapma biçimi, yetki ve ölçüm değişiklikleriyle birlikte yapılması gerektiğini anlatır."
course: ea
category: is-sistemleri-temelleri
tags: [erp, surec, degisim-yonetimi, yatirim, kpi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, it-yoneticisi]
level: orta
source_lessons: [EA-3.2]
reading_minutes: 3
key_points:
  - "Yazılımın getirisi, onunla birlikte değişen süreç, yetki ve ölçüm sistemine bağlıdır."
  - "Eski süreci yeni yazılımın içine taşımak, maliyeti artırır ama faydayı getirmez."
  - "Tamamlayıcı değişiklikler yazılım bütçesinde görünmez; ayrıca planlanmalıdır."
  - "Fayda, sürecin ölçtüğünüz çıktılarında (teslim süresi, hata) görünür; kurulum tarihi başarı ölçüsü değildir."
glossary_terms: [erp, is-sureci]
related: [kb-ea-3-6-it-business-case, kb-ea-18-3-why-erp-projects-fail, kb-ea-4-2-bpm-lifecycle, kb-ea-18-7-change-management-training]
sources:
  - title: "Beyond Computation: Information Technology, Organizational Transformation and Business Performance"
    authors: "Brynjolfsson, E.; Hitt, L. M."
    year: 2000
    type: article
    doi: "10.1257/jep.14.4.23"
    url: "https://doi.org/10.1257/jep.14.4.23"
    verified: true
    checked_on: 2026-10-28
  - title: "Information Technology and Organizational Performance: An Integrative Model of IT Business Value"
    authors: "Melville, N.; Kraemer, K.; Gurbaxani, V."
    year: 2004
    type: article
    doi: "10.2307/25148636"
    url: "https://doi.org/10.2307/25148636"
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

İki bayi aynı ERP'yi, aynı uygulama firmasıyla, aynı yıl kuruyor. Bir yıl sonra birinin teslim süresi yarıya inmiş, diğerinde neredeyse hiçbir şey değişmemiş. Bu kart, bu farkın nedenini açıklar ve yazılım yatırımını planlarken bütçenin görünmeyen yarısını, yani süreç ve organizasyon değişikliğini hesaba katmanızı sağlar.

## Temel fikir

Brynjolfsson ve Hitt (2000), bilgi teknolojisi yatırımlarının getirisinin firmalar arasında çok farklı olduğunu ve farkın büyük kısmının teknolojiyle birlikte yapılan organizasyonel değişikliklerden geldiğini gösterir. Melville ve arkadaşları (2004) da aynı sonuca daha geniş bir çerçeveyle varır: BT'nin değeri, onu tamamlayan kaynaklarla birleştiğinde ortaya çıkar.

**Tamamlayıcılık** (*complementarity*), iki şeyin birlikte yapıldığında ayrı ayrı yapılmalarının toplamından fazla değer yaratmasıdır. ERP için tamamlayıcı değişiklikler şunlardır:

- **Süreç:** Siparişin onay, toplama ve sevk adımlarının yeniden tasarlanması; gereksiz kontrollerin kaldırılması.
- **Yetki:** Kararın veriye en yakın kişiye verilmesi; örneğin limit içindeki siparişi şefin değil sistemin onaylaması.
- **Ölçüm ve teşvik:** Yeni sürecin çıktısının (teslim süresi, hatalı sipariş oranı) izlenmesi ve hedeflere bağlanması.
- **Beceri:** Kullanıcıların yalnızca ekranı değil yeni iş akışını öğrenmesi.

Bunlar yapılmadan kurulan sistem, eski düzeni dijital olarak kopyalar. Maliyet artar, çünkü artık hem yazılım hem de eski alışkanlıklar sürdürülür.

### Yatırım planına tamamlayıcıları eklemek

Bir teknoloji yatırımı planlanırken, bütçe ve takvim yalnızca yazılımı değil, tamamlayıcı değişiklikleri de kapsamalıdır: süreçlerin yeniden tasarımı, yetki ve rol değişiklikleri, yeni performans göstergeleri ve eğitim. Brynjolfsson ve Hitt'in bulguları, bu tamamlayıcı yatırımların çoğu zaman yazılımın kendisinden daha büyük olduğunu düşündürür. Yatırım gerekçesinde her beklenen fayda için hangi süreç değişikliğinin gerektiği ve bunun sahibinin kim olduğu yazılmalıdır. Böylece faydanın gerçekleşmemesi durumunda nedenin teknoloji mi yoksa eksik kalan süreç değişikliği mi olduğu anlaşılabilir.

## Bir örnek

> **Örnek (temsili rakamlar):** Bayiler ve rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b1.py` ile yapılmıştır.

İki bayi aynı ERP'ye 1.500.000 TL yatırım yapıyor. Her ikisi de yılda 30.000 sipariş işliyor; hatalı bir siparişin (yanlış ürün, iade, yeniden sevk) maliyeti ortalama 450 TL.

- **Bayi A**, kurulumla birlikte onay adımını kaldırdı, depoda barkodla toplamaya geçti ve hatalı siparişi haftalık izlemeye başladı.
- **Bayi B**, eski kâğıt onay ve elle toplama düzenini aynen korudu.

| Gösterge | Bayi A | Bayi B |
|---|---|---|
| Teslim süresi (gün) | 2 → 1 (**−%50,0**) | 2 → 1,8 (**−%10,0**) |
| Hatalı sipariş oranı | %3,1 → %0,9 (**−%71,0**) | %3,1 → %2,7 (**−%12,9**) |
| Yılda önlenen hatalı sipariş | 30.000 × (0,031 − 0,009) = **660** | 30.000 × (0,031 − 0,027) = **120** |
| Yıllık tasarruf | 660 × 450 = **297.000 TL** | 120 × 450 = **54.000 TL** |

Yatırım aynı, sonuç beş kattan fazla farklı. Bayi A'nın ek maliyeti süreç tasarımına ve barkod eğitimine ayırdığı yönetici zamanıdır; bu kalem yazılım teklifinde hiç görünmez.

## Sık yapılan hatalar

- Yazılımı "mevcut süreci aynen yapsın" diye uyarlatmak.
- Süreç değişikliğini kurulumdan sonraya bırakmak; o noktada ekip yorgun ve bütçe tükenmiş olur.
- Yetkiyi değiştirmeden sistem kurmak: Sistem onaylıyor ama yönetici yine elle onay istiyor.
- Başarıyı "sistem canlıya geçti" diye ölçmek; süreç çıktısını hiç izlememek.

## Pratikte nasıl uygulanır?

- [ ] Yazılım projesine başlamadan önce iyileştirmek istediğiniz 2–3 süreç çıktısını ve bugünkü değerini yazın.
- [ ] Her süreç için "sistem geldikten sonra kim neyi farklı yapacak?" sorusunu cevaplayın.
- [ ] Kaldırılacak onay, kâğıt ve tekrar giriş adımlarını listeleyin.
- [ ] Süreç sahibi olarak bir iş yöneticisi atayın; BT'ye bırakmayın.
- [ ] Bütçeye süreç tasarımı ve eğitim için ayrı satır koyun.
- [ ] Canlıya geçişten 3 ve 6 ay sonra seçtiğiniz göstergeleri tekrar ölçün.

## Daha fazlası

- Brynjolfsson ve Hitt (2000), *Journal of Economic Perspectives*. https://doi.org/10.1257/jep.14.4.23
- Melville, Kraemer ve Gurbaxani (2004), *MIS Quarterly*. https://doi.org/10.2307/25148636
