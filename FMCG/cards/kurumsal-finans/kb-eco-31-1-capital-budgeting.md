---
id: kb-eco-31-1-capital-budgeting
title: "Yatırım bütçeleme: Depo otomasyonu ya da yeni araç yatırımı nasıl değerlendirilir?"
summary: "Bir yatırımın nakit akışlarını kurmayı, net bugünkü değer, iç verim oranı ve geri ödeme süresiyle değerlendirmeyi, enflasyonun tasarruflara etkisini ve ekonomik ömür varsayımının kararı nasıl değiştirdiğini anlatır."
course: eco
category: kurumsal-finans
tags: [yatirim, kurumsal-finans, karar-verme]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: orta
source_lessons: [ECO-31.1]
reading_minutes: 3
key_points:
  - "Yatırım kararı, yalnızca o yatırımın yaratacağı ek nakit akışlarına göre verilmelidir."
  - "Geri ödeme süresi pratik bir ölçüdür ama paranın zaman değerini ve sonraki nakitleri yok sayar."
  - "Nominal iskonto oranı kullanıyorsanız tasarrufları da enflasyonla artan nominal tutarlarla yazın."
  - "Ekonomik ömür ve tasarruf varsayımı yatırımın sonucunu en çok değiştiren değişkenlerdir."
glossary_terms: [net-bugunku-deger, ic-verim-orani, geri-odeme-suresi]
related: [kb-eco-25-1-time-value-npv-irr, kb-eco-31-2-cost-of-capital, kb-eco-31-10-scenario-sensitivity, kb-eco-1-1-opportunity-cost-sunk-cost]
sources:
  - title: "Principles of Finance"
    authors: "OpenStax"
    year: 2026
    type: web
    url: "https://openstax.org/books/principles-finance/pages/1-why-it-matters"
    verified: true
    checked_on: 2026-10-28
  - title: "The theory and practice of corporate finance: evidence from the field"
    authors: "Graham, J. R.; Harvey, C. R."
    year: 2001
    type: article
    doi: "10.1016/S0304-405X(01)00044-7"
    url: "https://doi.org/10.1016/S0304-405X(01)00044-7"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Financial Economics 60(2–3). Şirketlerin NBD/İVO ve sermaye maliyeti uygulamaları."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Depo otomasyonu, yeni frigorifik araçlar, güneş paneli, ERP geçişi, yeni bir şube... Bu kart, bir yatırım teklifini sistematik olarak değerlendirmenizi ve sık yapılan hesap hatalarından kaçınmanızı sağlar.

## Temel fikir

**Hangi nakit akışları?** Yalnızca yatırım yapılırsa ortaya çıkacak ek nakit akışları: yatırım tutarı, kurulum, ek işletme sermayesi, tasarruflar veya ek katkı payı, bakım giderleri, ömür sonundaki hurda değeri. Daha önce harcanmış etüt maliyetleri gibi batık maliyetler hesaba girmez. Şirket genel giderlerinden pay ayrılmaz; yatırım bunları değiştirmiyorsa.

**Üç ölçü:**

- **Net bugünkü değer (NBD):** Sermaye maliyetiyle iskonto edilmiş nakit akışlarının toplamı. Karar ölçüsü olarak en güvenilir olanıdır.
- **İç verim oranı (İVO):** Sermaye maliyetiyle karşılaştırılır.
- **Geri ödeme süresi:** Yatırımın kaç yılda geri döneceği. Graham ve Harvey (2001), finans yöneticilerinin NBD ve İVO'nun yanında geri ödeme süresini de yaygın olarak kullandığını raporladı. Pratiktir, ama paranın zaman değerini ve geri ödeme sonrasındaki nakdi dikkate almaz.

**Enflasyon tutarlılığı:** Yüksek enflasyonda iskonto oranı nominal ise, işçilik ve kira tasarrufları da yıllar içinde nominal olarak artar. Tasarrufları sabit yazıp nominal oranla iskonto etmek, iyi yatırımları reddetmenize yol açar.

### Tipik distribütör ve üretici yatırımları

- **Depo otomasyonu ve raf sistemleri:** Getirisi işçilik tasarrufu, hata azalması ve kapasite artışıdır. Tasarrufun gerçekleşmesi, çalışan sayısının fiilen azalmasına veya artan hacmin ek işe alım olmadan karşılanmasına bağlıdır.
- **Araç filosu:** Satın alma ile kiralama veya dış kaynak kullanımı karşılaştırılır.
- **Yeni şube veya depo:** Ek satış, rota kısalması ve teslimat hizmeti iyileşmesi; ama ek sabit giderler ve işletme sermayesi ihtiyacı da hesaba katılmalıdır.
- **Üretim hattı:** Kapasite, verimlilik ve kalite artışı; bakım ve enerji maliyetleri.

### Sık unutulan kalemler

- **İşletme sermayesi:** Yeni bir depo veya ürün hattı ek stok ve alacak gerektirir. Bu, başta nakit çıkışı, proje sonunda ise geri dönüştür.
- **Vergi etkisi:** Amortismanın vergi matrahını düşürmesi ve varsa yatırım teşvikleri.
- **Kalıntı değer:** Projenin sonunda varlıkların satış değeri.
- **Fırsat maliyeti:** Kullanılan mevcut arsa veya depo alanının başka bir kullanımdan vazgeçilmesi.

Yatırım sonrası, gerçekleşen nakit akışlarını planla karşılaştırın. Bu geri bildirim, gelecekteki yatırım tahminlerinin kalitesini artırır.

## Bir örnek

> **Örnek (temsili rakamlar):** Yatırım tutarı, tasarruf, enflasyon ve iskonto oranları varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b3.py` ile yapılmıştır.

Bir distribütör 15.000.000 TL'lik depo otomasyonuyla yılda 6.000.000 TL işçilik ve fire tasarrufu bekliyor. Ekonomik ömür 5 yıl, sermaye maliyeti (nominal) %30.

- Geri ödeme süresi **2,5 yıl**; ilk bakışta cazip.
- Tasarruf sabit yazılırsa NBD **−386.581 TL**, İVO %28,6. Yatırım reddedilir.
- Ama tasarruflar işçilik maliyetiyle yılda %25 artarsa (nominal oranla tutarlı yazım), NBD **6.368.747 TL**, İVO %47,5. Yatırım değer yaratır.
- Ekonomik ömür 5 değil 3 yıl olursa (sabit tasarrufla) NBD −4.103.323 TL.

Kararı, yatırımın matematiğinden çok tasarruf ve ömür varsayımları belirliyor.

## Sık yapılan hatalar

- Nominal iskonto oranını sabit (enflasyonsuz) tasarruflarla kullanmak.
- Ek işletme sermayesini ve ömür sonu hurda değerini unutmak.
- Batık maliyetleri ya da dağıtılmış genel giderleri hesaba katmak.
- Tedarikçinin verdiği tasarruf rakamlarını doğrulamadan kullanmak.
- Yatırımdan sonra gerçekleşen tasarrufu ölçmemek.

## Pratikte nasıl uygulanır?

- [ ] Yatırım teklifleri için standart bir şablon kullanın: nakit akışları, varsayımlar, NBD, İVO, geri ödeme.
- [ ] Nakit akışlarının nominal mi reel mi olduğunu ve iskonto oranıyla tutarlılığını kontrol edin.
- [ ] Tasarruf, ömür ve yatırım tutarı için duyarlılık analizi ekleyin.
- [ ] Belirli bir tutarın üzerindeki yatırımlar için yönetim onay sınırları belirleyin.
- [ ] Yatırımdan 12 ay sonra gerçekleşen sonuçları tahminle karşılaştırın.

## Daha fazlası

- OpenStax (2026). *Principles of Finance*. https://openstax.org/books/principles-finance/pages/1-why-it-matters
- Graham, J. R.; Harvey, C. R. (2001). *The theory and practice of corporate finance: evidence from the field*. https://doi.org/10.1016/S0304-405X(01)00044-7
