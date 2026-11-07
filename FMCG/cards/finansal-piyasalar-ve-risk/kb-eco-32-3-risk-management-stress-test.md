---
id: kb-eco-32-3-risk-management-stress-test
title: "Risk yönetimi ve stres testi: Kötü bir yılda özkaynağınızın ne kadarı kalır?"
summary: "Kur, alacak, stok ve faiz risklerini aynı anda gerçekleşecek şekilde bir stres senaryosunda birleştirmeyi, özkaynak ve nakit üzerindeki etkiyi ölçmeyi ve sonuçlardan risk sınırları ve önlem planı çıkarmayı anlatır."
course: eco
category: finansal-piyasalar-ve-risk
tags: [risk-yonetimi, stres-testi, finansal-planlama]
roles: [finans-muduru]
level: ileri
source_lessons: [ECO-32.3]
reading_minutes: 3
key_points:
  - "Stres testi, olası en kötü ama gerçekçi koşulların birlikte gerçekleştiğini varsayarak şirketin dayanıklılığını ölçer."
  - "Distribütörlerde ana riskler kur, alacak, stok ve faizdir; krizlerde bunlar genellikle birlikte gerçekleşir."
  - "Sonuç, özkaynak kaybı ve ek nakit ihtiyacı olarak raporlanmalıdır."
  - "Stres testinin değeri, sonucuna göre risk sınırları ve önlemler belirlendiğinde ortaya çıkar."
glossary_terms: [stres-testi, kur-riski, likidite-tamponu]
related: [kb-eco-23-2-currency-crises-business, kb-eco-24-3-turkey-crises-lessons, kb-eco-31-10-scenario-sensitivity, kb-eco-4-2-risk-aversion-insurance]
sources:
  - title: "The Twin Crises: The Causes of Banking and Balance-of-Payments Problems"
    authors: "Kaminsky, G. L.; Reinhart, C. M."
    year: 1999
    type: article
    doi: "10.1257/aer.89.3.473"
    url: "https://doi.org/10.1257/aer.89.3.473"
    verified: true
    checked_on: 2026-10-28
    note: "American Economic Review 89(3)."
  - title: "Bankacılık Düzenleme ve Denetleme Kurumu (resmî site)"
    authors: "BDDK"
    year: 2026
    type: web
    url: "https://www.bddk.org.tr"
    verified: true
    checked_on: 2026-10-28
  - title: "Principles of Finance"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-finance/pages/1-why-it-matters"
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

Bankalar düzenli olarak stres testi yapar; şirketler ise çoğu zaman yapmaz. Oysa bir dağıtım şirketi ya da üretici için kur sıçraması, büyük bir müşterinin batması ve faiz artışı aynı yıl içinde gelebilir. Bu kart, basit bir stres testi kurmanızı ve sonuçlarını kararlara bağlamanızı sağlar.

## Temel fikir

**Risk haritası:** Önce ana riskleri listeleyin:

- **Kur riski:** Döviz borcu, döviz bazlı tedarikçi borcu, ithal stok.
- **Kredi riski:** Müşteri alacaklarının bir kısmının tahsil edilememesi.
- **Stok riski:** Değer kaybı, son kullanma tarihi, talep düşüşü.
- **Faiz riski:** Değişken faizli kredilerde ve kredi yenilemede faiz artışı.
- **Likidite riski:** Banka limitlerinin daralması, tedarikçi vadelerinin kısalması.

**Senaryo:** Bu risklerin birlikte gerçekleştiği, olası ama sert bir senaryo kurun. Kaminsky ve Reinhart'ın (1999) gösterdiği gibi, kur ve bankacılık krizleri sıklıkla birlikte görülür; bu yüzden riskleri tek tek değil, birlikte test etmek önemlidir.

**Ölçüm:** Her riskin özkaynak ve nakit etkisini hesaplayın, toplayın. Sonra iki soruyu yanıtlayın: Özkaynak sıfırın üzerinde kalıyor mu? Ek nakit ihtiyacı karşılanabilir mi?

### Stres testinden eyleme

Stres testinin amacı korkutmak değil, önceden karar almaktır. Sonuçlara göre:

- **Tampon belirleyin:** Kötü senaryoda ihtiyaç duyulacak asgari nakit ve kullanılmamış kredi limiti tutarını hedef olarak koyun.
- **Erken uyarı göstergeleri seçin:** Kur, faiz, tahsilat süresi ve stok süresi için eşikler tanımlayın. Eşik aşıldığında hangi önlemin devreye gireceğini yazın.
- **Önlem listesi hazırlayın:** Yatırımları erteleme, stok seviyesini düşürme, vade kısaltma, döviz pozisyonunu kapatma gibi adımların sırası ve sorumlusu.

### Riskler birlikte gelir

Türkiye'de kur, faiz ve tahsilat riskleri genellikle aynı anda gerçekleşir. Kur yükseldiğinde faizler artar, bankalar limitleri daraltır ve müşterilerin ödeme gücü zayıflar. Bu nedenle riskleri tek tek ölçmek, toplam etkiyi olduğundan küçük gösterir. Senaryonuzu geçmişteki gerçek bir kriz dönemine dayandırmak, varsayımların gerçekçi olmasını sağlar.

### Kimin işi?

Risk yönetimi yalnızca finans biriminin görevi değildir. Satış, satın alma ve depo yöneticileri risklerin kaynağına en yakın kişilerdir. Stres testi sonuçlarını yönetim toplantılarında düzenli olarak gözden geçirin.

## Bir örnek

> **Örnek (temsili rakamlar):** Bilanço tutarları ve şok büyüklükleri varsayımsaldır; vergi etkisi dikkate alınmamıştır. Hesaplar `scripts/cards_numbers_eco_b4.py` ile yapılmıştır.

Bir distribütörün özkaynağı 40.000.000 TL. 1.000.000 dolar döviz borcu, 60.000.000 TL alacak, 30.000.000 TL stok ve 50.000.000 TL değişken faizli TL kredisi var.

| Şok | Varsayım | Kayıp (TL) |
|---|---|---|
| Kur | 34 → 47,6 TL (%40) | 13.600.000 |
| Alacak | Alacakların %10'u tahsil edilemez | 6.000.000 |
| Stok | Stok değerinde %10 kayıp | 3.000.000 |
| Faiz | Kredi faizinde 10 puan artış (bir yıl) | 5.000.000 |
| **Toplam** | | **27.600.000** |

Özkaynak 12.400.000 TL'ye iniyor (−%69). Şirket ayakta kalıyor, ama bankaların kredi koşullarını sıkılaştırması için yeterli bir bozulma bu. Kur kaybının toplam kaybın yarısı kadar olduğu görülüyor; ilk önlem döviz pozisyonunu sınırlamak olmalı.

## Sık yapılan hatalar

- Riskleri tek tek test edip birlikte gerçekleşme ihtimalini göz ardı etmek.
- Şokları gerçekçi olmayan küçüklükte (ör. kur %5) seçmek.
- Yalnızca kâr etkisine bakıp nakit ve banka limitlerine etkisini ihmal etmek.
- Stres testini bir kez yapıp güncellememek.
- Sonuçları risk sınırlarına ve önlemlere dönüştürmemek.

## Pratikte nasıl uygulanır?

- [ ] Ana risklerinizi ve bilançodaki karşılıklarını (döviz borcu, alacak, stok, değişken faizli kredi) listeleyin.
- [ ] Yılda en az bir kez birleşik bir stres senaryosu çalıştırın; dönemsel olarak kur ve faiz varsayımlarını güncelleyin.
- [ ] Özkaynak kaybı ve ek nakit ihtiyacı için kabul edilebilir sınırlar belirleyin.
- [ ] Sınırı aşan riskler için önlem planı hazırlayın: döviz korunması, müşteri limitleri, stok azaltma, faiz sabitleme.
- [ ] Sonuçları yönetim kurulu ve ana bankalarınızla paylaşmayı değerlendirin.

## Daha fazlası

- Kaminsky, G. L.; Reinhart, C. M. (1999). *The Twin Crises: The Causes of Banking and Balance-of-Payments Problems*. https://doi.org/10.1257/aer.89.3.473
- BDDK (2026). *Bankacılık Düzenleme ve Denetleme Kurumu (resmî site)*. https://www.bddk.org.tr
- OpenStax (2026). *Principles of Finance*. https://openstax.org/books/principles-finance/pages/1-why-it-matters
