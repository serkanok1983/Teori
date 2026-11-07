---
id: kb-fmcg-11-6-sop-ibp
title: "Satış ve operasyon planlaması (S&OP) ve entegre iş planlaması"
summary: "Satış ve operasyon planlaması, talep, arz ve finans planlarını aylık bir döngüde tek bir plana bağlar. Bu kart döngünün adımlarını, entegre iş planlamasına geçişi, kurumsal kaynak planlama sistemindeki karşılığını ve arz açığı kararlarının nasıl verileceğini anlatır."
course: fmcg
category: tedarik-zinciri-ve-stok
tags: [tedarik-zinciri, planlama, yonetim]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, depo-lojistik-muduru]
level: ileri
source_lessons: [FMCG-11.6, EA-29.4]
reading_minutes: 3
key_points:
  - "S&OP, satış, pazarlama, tedarik zinciri ve finansın aylık bir döngüde tek bir plan üzerinde anlaşmasıdır."
  - "Tipik döngü: veri toplama, talep planı, arz planı, uzlaşma toplantısı ve yönetim toplantısı."
  - "Entegre iş planlaması, aynı süreci finansal planlar ve stratejiyle daha sıkı bağlar."
  - "Arz açığı kararları, ek maliyet ile kurtarılan katkı karşılaştırılarak verilmelidir."
  - "Kurumsal kaynak planlama sistemi süreci destekler, ama kararları veren insanlardır."
glossary_terms: [satis-ve-operasyon-planlamasi, tahmin-hatasi, guvenlik-stoku, katki-payi, erp]
related: [kb-fmcg-11-2-demand-forecasting, kb-fmcg-11-1-supply-chain-basics, kb-fmcg-11-5-bullwhip-effect, kb-fmcg-10-7-joint-business-planning, kb-fmcg-13-16-sales-forecasting]
sources:
  - title: "Supply Chain Management: Strategy, Planning, and Operation"
    authors: "Chopra, S.; Meindl, P."
    year: 2016
    type: book
    verified: false
    note: "Kitap; baskı yılı kontrol edilmedi."
  - title: "ASCM CSCP — Certified Supply Chain Professional"
    authors: "ASCM"
    year: 2026
    type: web
    url: "https://www.ascm.org/learning-development/certifications-credentials/cscp/"
    verified: true
    checked_on: 2026-10-28
    note: "HTTP 200; başlık etiketi okunamadı."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Satış ekibi büyük bir promosyon planlar, ama üretim bundan son anda haberdar olur. Pazarlama yeni ürün lansmanı yapar, ama ambalaj tedarikçisi hazır değildir. Satış ve operasyon planlaması (*sales and operations planning*, S&OP), bu kopukluğu gidermek için kullanılan aylık karar sürecidir. Bu kart, süreci kurmanızı ve bir arz açığında nasıl karar vereceğinizi anlatır.

## Temel fikir

**Tipik aylık döngü.** Chopra ve Meindl ile ASCM'nin mesleki kaynakları, süreci benzer adımlarla anlatır:

1. **Veri toplama:** Geçen ayın gerçekleşen satışı, stok, tahmin hatası.
2. **Talep planı:** İstatistiksel tahmin, satış ve pazarlama bilgisi (promosyon, listeleme, lansman) ile birleştirilir.
3. **Arz planı:** Üretim, tedarik ve depo kapasitesi talep planıyla karşılaştırılır; açıklar ve fazlalar belirlenir.
4. **Uzlaşma toplantısı:** Satış, pazarlama, tedarik zinciri ve finans, açıkları çözmek için seçenekleri değerlendirir.
5. **Yönetim toplantısı:** Üst yönetim, çözülemeyen konularda karar verir ve tek bir planı onaylar.

**Entegre iş planlaması** (*integrated business planning*). S&OP'nin gelişmiş bir biçimi olarak anlatılır. Aynı süreci adet planlarından finansal planlara ve stratejik hedeflere bağlar; böylece yönetim, hacim kararlarının ciro ve kârlılık etkisini aynı toplantıda görür.

**Kurumsal kaynak planlama sistemi.** S&OP süreci, kurumsal kaynak planlama (ERP) sistemindeki talep planlama, ana üretim planlaması ve malzeme ihtiyaç planlaması modülleriyle desteklenir. Sistemin işi verileri bir araya getirmek ve senaryoları hesaplamaktır. Ancak sistem tek başına bir S&OP süreci değildir: Toplantılar yapılmaz, kararlar alınmaz ve sorumluluklar belirlenmezse, en iyi sistem bile kopukluğu gidermez.

**Arz açığı kararları.** Talep kapasiteyi aştığında seçenekler şunlardır: fazla mesai, dış üretim, stoktan karşılama, müşteri önceliklendirme ya da satış kaybını kabul etmek. Her seçeneğin maliyeti, kurtardığı katkıyla karşılaştırılmalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Açık miktarı, katkı ve fazla mesai maliyeti varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b6.py` ile yapılmıştır.

Bayram öncesi ayda talep planı, üretim kapasitesini **10.000** koli aşıyor. Koli başına katkı 40 TL; açık karşılanmazsa kayıp katkı **400.000 TL**.

Seçenek: fazla mesaiyle **6.000** koli ek üretim, koli başına **15 TL** ek maliyet.

- Fazla mesai maliyeti: 6.000 × 15 = **90.000 TL**
- Kurtarılan katkı: 6.000 × 40 = **240.000 TL**
- Net kazanç: **150.000 TL**
- Kalan açık: **4.000** koli, kalan kayıp katkı **160.000 TL**

Fazla mesai açıkça kârlı. Kalan 4.000 koli için uzlaşma toplantısında başka seçenekler değerlendirilir: Hangi müşteriler ve kanallar önceliklendirilecek, promosyon bir hafta ertelenebilir mi, güvenlik stoku geçici olarak kullanılabilir mi? Bu kararlar satış, tedarik zinciri ve finans tarafından birlikte verilmelidir.

## Sık yapılan hatalar

- **S&OP'yi bir tahmin toplantısına indirgemek.** Amaç tahmin değil, kararlardır.
- **Finansı sürece katmamak.** Adet planları ile bütçe arasında fark kalır.
- **Satış hedefini talep planı olarak kullanmak.** Hedef bir istektir, talep planı ise bir beklentidir.
- **Sistemi kurmak, süreci kurmamak.** ERP yazılımı, toplantı ve karar disiplini olmadan işe yaramaz.
- **Arz açığını yalnızca maliyetle değerlendirmek.** Kurtarılan katkı da hesaba katılmalıdır.

## Pratikte nasıl uygulanır?

- [ ] Aylık bir S&OP takvimi belirleyin ve her adımın sahibini atayın.
- [ ] Talep planını istatistiksel tahmin ve satış bilgisiyle birlikte hazırlayın.
- [ ] Arz planında açık ve fazlaları adet ve TL olarak gösterin.
- [ ] Uzlaşma toplantısında her seçeneğin maliyetini ve kurtardığı katkıyı karşılaştırın.
- [ ] Yönetim toplantısında tek bir planı onaylayın ve kararları kaydedin.
- [ ] Tahmin hatası ve plan uyumunu her ay ölçün.

## Daha fazlası

- Chopra, S.; Meindl, P. (2016). *Supply Chain Management: Strategy, Planning, and Operation.* (kaynak doğrulanmadı)
- ASCM (2026). *ASCM CSCP — Certified Supply Chain Professional.* https://www.ascm.org/learning-development/certifications-credentials/cscp/
