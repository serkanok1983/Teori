---
id: kb-ea-2-2-user-adoption
title: "Saha ekibi uygulamayı neden kullanmıyor? Benimseme ve başarı ölçümü"
summary: "Kullanıcıların bir sistemi neden benimsediğini ya da direndiğini açıklayan iki temel modeli ve sistemin başarısını yalnızca kurulumla değil kullanım ve iş sonucuyla ölçmeyi anlatır."
course: ea
category: is-sistemleri-temelleri
tags: [sfa, benimseme, kpi, degisim-yonetimi, saha-satis]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, it-yoneticisi]
level: orta
source_lessons: [EA-2.2, EA-2.3]
reading_minutes: 3
key_points:
  - "Kullanıcı bir sistemi, işine yarayacağına ve kolay kullanılacağına inandığında benimser."
  - "Fayda algısı, kullanım kolaylığından genellikle daha güçlü bir belirleyicidir."
  - "Sistem başarısı; sistem, bilgi ve hizmet kalitesi, kullanım, memnuniyet ve net fayda üzerinden birlikte ölçülür."
  - "Kullanım oranını gerçek faaliyetle kıyaslayarak ölçün; giriş sayısı tek başına yanıltır."
  - "Düşük benimsemenin çaresi çoğu zaman zorlamak değil, temsilcinin işini kolaylaştıran bir özellik eklemektir."
glossary_terms: [teknoloji-kabul-modeli, sfa]
related: [kb-ea-18-7-change-management-training, kb-ea-18-4-post-go-live-dip, kb-ea-26-1-retail-execution-sfa, kb-ea-9-6-bi-dashboards-kpis]
sources:
  - title: "Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology"
    authors: "Davis, F. D."
    year: 1989
    type: article
    doi: "10.2307/249008"
    url: "https://doi.org/10.2307/249008"
    verified: true
    checked_on: 2026-10-28
  - title: "User Acceptance of Information Technology: Toward a Unified View"
    authors: "Venkatesh, V.; Morris, M. G.; Davis, G. B.; Davis, F. D."
    year: 2003
    type: article
    doi: "10.2307/30036540"
    url: "https://doi.org/10.2307/30036540"
    verified: true
    checked_on: 2026-10-28
  - title: "The DeLone and McLean Model of Information Systems Success: A Ten-Year Update"
    authors: "DeLone, W. H.; McLean, E. R."
    year: 2003
    type: article
    doi: "10.1080/07421222.2003.11045748"
    url: "https://doi.org/10.1080/07421222.2003.11045748"
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

Saha satış uygulaması kuruldu, eğitim verildi; üç ay sonra temsilcilerin bir kısmı siparişi hâlâ telefonla ya da WhatsApp'tan iletiyor. Bu kart, kullanıcıların bir sistemi neden benimsediğini ya da ondan kaçındığını açıklayan iki yerleşik modeli ve sistem başarısını nasıl ölçeceğinizi gösterir. Böylece "kullanmıyorlar" şikâyetini ölçülebilir bir soruna çevirirsiniz.

## Temel fikir

**Teknoloji kabul modeli** (*technology acceptance model, TAM*), Davis'in (1989) çalışmasına dayanır. Kullanıcının bir sistemi kullanma niyetini iki algı belirler:

- **Algılanan fayda:** "Bu uygulama işimi daha iyi yapmamı sağlar mı?"
- **Algılanan kullanım kolaylığı:** "Bunu öğrenmek ve kullanmak zahmetli mi?"

Venkatesh ve arkadaşlarının (2003) birleştirdiği modelde bunlara **sosyal etki** (yöneticim ve arkadaşlarım kullanıyor mu?) ve **kolaylaştırıcı koşullar** (cihaz, internet, destek var mı?) eklenir. Pratikte fayda algısı genellikle daha güçlü belirleyicidir: Temsilci, uygulama ona prim takibi ya da hızlı stok bilgisi gibi somut bir şey kazandırıyorsa zahmete katlanır.

Sistemin başarısını ölçmek için DeLone ve McLean (2003) altı boyut önerir: sistem kalitesi (hız, kesintisizlik), bilgi kalitesi (doğru ve güncel veri), hizmet kalitesi (destek), kullanım, kullanıcı memnuniyeti ve net fayda (iş sonucuna etkisi). Boyutlar birbirini etkiler; örneğin yanlış stok bilgisi gösteren bir uygulama, ne kadar hızlı olursa olsun kullanılmaz.

Bu modellerin sınırı da var: Niyeti açıklarlar ama alışkanlığı, zorunlu kullanımı ve kullanıcının sistemi kendi işine göre "eğip bükmesini" iyi açıklamazlar. O yüzden anketi gerçek kullanım verisiyle birlikte okuyun.

## Bir örnek

> **Örnek (temsili rakamlar):** Ekip ve puanlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b1.py` ile yapılmıştır.

40 temsilcili bir bayide bir ayda rota planına göre 1.840 ziyaret yapılmış, uygulamada 1.288 ziyaret kaydı var. Kayıtlı ziyaret oranı 1.288 ÷ 1.840 = **%70,0**. Hedef %90 ise **368** ziyaretin daha uygulamaya girilmesi gerekiyor.

Kısa bir ankette (1–7 ölçek) üç temsilci grubunun ortalamaları:

| Grup | Algılanan fayda | Kullanım kolaylığı | Yorum |
|---|---|---|---|
| A | 6,1 | 3,2 | İşe yaradığını düşünüyor, ekranlar zor |
| B | 3,4 | 5,9 | Kolay buluyor ama "bana ne faydası var" diyor |
| C | 5,8 | 5,6 | Benimsemiş |

A grubu için ekran sadeleştirme ve eğitim; B grubu için uygulamaya temsilcinin kendi hedef ve prim durumunu gösteren bir ekran eklemek daha etkili olur. Aynı çözüm iki gruba birden uymaz.

## Sık yapılan hatalar

- Benimsemeyi uygulamaya giriş sayısıyla ölçmek; girişin gerçek işe karşılık gelip gelmediğine bakmamak.
- Düşük kullanımı yalnızca zorunluluk ve yaptırımla çözmeye çalışmak.
- Uygulamayı yöneticinin rapor ihtiyacına göre tasarlayıp temsilciye hiçbir kolaylık sunmamak.
- Bilgi kalitesini ihmal etmek: Yanlış stok ya da fiyat gösteren sistem hızla güven kaybeder.
- Anket sonuçlarını tek başına yeterli saymak.

## Pratikte nasıl uygulanır?

- [ ] Kullanım oranını gerçek faaliyetle kıyaslayarak ölçün (kayıtlı ziyaret ÷ yapılan ziyaret).
- [ ] Üç ayda bir kısa bir fayda/kolaylık anketi yapın; sonuçları bölge ve ekip bazında ayırın.
- [ ] Temsilcinin uygulamadan kendisi için ne aldığını (hedef, prim, stok, müşteri geçmişi) listeleyin.
- [ ] Satış şeflerinin uygulamayı kendi takiplerinde kullanmasını sağlayın; sosyal etki yukarıdan başlar.
- [ ] Cihaz, şarj ve mobil veri gibi kolaylaştırıcı koşulları kontrol edin.
- [ ] Destek taleplerini kategorilere ayırıp en sık üç sorunu her ay çözün.

## Daha fazlası

- Davis (1989), *MIS Quarterly*. https://doi.org/10.2307/249008
- Venkatesh, Morris, Davis ve Davis (2003), *MIS Quarterly*. https://doi.org/10.2307/30036540
- DeLone ve McLean (2003), *Journal of Management Information Systems*. https://doi.org/10.1080/07421222.2003.11045748
