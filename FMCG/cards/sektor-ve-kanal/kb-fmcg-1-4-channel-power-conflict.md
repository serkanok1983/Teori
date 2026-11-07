---
id: kb-fmcg-1-4-channel-power-conflict
title: "Kanal gücü ve çatışma: Zincirle pazarlıkta kim kime bağımlı?"
summary: "Kanalda güç, tarafların birbirine ne kadar bağımlı olduğundan doğar. Bu kart bağımlılığı karşılıklı ölçmeyi, çatışmanın türlerini ve bir listeden çıkarma tehdidinin gerçek maliyetini hesaplamayı gösterir."
course: fmcg
category: sektor-ve-kanal
tags: [zincir-market, rekabet, pazarlik, bayi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: orta
source_lessons: [FMCG-1.4]
reading_minutes: 3
key_points:
  - "Güç, karşı tarafın size olan bağımlılığından gelir; bağımlılık iki yönlü ölçülmelidir."
  - "Zincirin sizin satışınızdaki payı ile sizin zincirin kategorisindeki payınız çoğu zaman çok farklıdır."
  - "Listeden çıkma tehdidini, kaybedilen katkı ve geri kazanılabilecek satış üzerinden TL olarak hesaplayın."
  - "Çatışmanın kaynağı genellikle hedef, alan (bölge, müşteri) ya da algı farkıdır; her birinin çözümü ayrıdır."
glossary_terms: [kanal-gucu, kanal-catismasi, katki-payi]
related: [kb-fmcg-1-3-channel-actors, kb-fmcg-10-4-negotiating-with-chains, kb-fmcg-13-14-negotiation-structure, kb-fmcg-10-2-trade-terms, kb-fmcg-1-2-scale-and-concentration]
sources:
  - title: "Marketing Channels"
    authors: "Coughlan, A. T.; Anderson, E.; Stern, L. W.; El-Ansary, A. I."
    year: 2006
    type: book
    verified: false
    note: "Kitap; baskı yılı kontrol edilmedi."
  - title: "Rekabet Kurumu"
    authors: "Rekabet Kurumu"
    year: 2026
    type: web
    url: "https://www.rekabet.gov.tr/"
    verified: true
    checked_on: 2026-10-28
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Ulusal bir zincir ek iskonto istediğinde ya da bir bayi bölge dışına satış yaptığında, kimin ne kadar güçlü olduğunu bilmek doğru tepkiyi belirler. Bu kart gücü duygudan değil rakamdan okumayı öğretir. Yıllık zincir görüşmeleri, bayi bölge anlaşmazlıkları ve kanal politikası kararları için temel çerçevedir.

## Temel fikir

**Güç, bağımlılıktan gelir.** Kanal literatüründe (Coughlan ve ark.) A'nın B üzerindeki gücü, B'nin A'ya ne kadar bağımlı olduğuyla açıklanır. Bağımlılık iki şeyle artar: karşı tarafın size sağladığı değerin büyüklüğü ve bu değerin yerine koyulmasının zorluğu.

Bunu iki yönlü ölçmek gerekir:

- **Sizin zincire bağımlılığınız:** Toplam satışınızın yüzde kaçı bu zincirden geçiyor? Kaybederseniz bu satışın ne kadarını başka mağazalarda geri kazanırsınız?
- **Zincirin size bağımlılığı:** Kategorisinin yüzde kaçını sizin ürünleriniz oluşturuyor? Markanızı bulamayan müşteri mağaza değiştirir mi?

Büyük bir zincirle çalışan orta ölçekli üreticide bu iki oran genellikle çok dengesizdir. Bu dengesizlik, ek iskonto taleplerinin ve sözleşme şartlarının kaynağıdır.

**Gücün kaynakları.** Ödül (prim, raf alanı), yaptırım (listeden çıkarma), uzmanlık (kategori bilgisi, veri), meşruiyet (sözleşme, mevzuat) ve ilişki. Uzun vadede uzmanlık ve ilişki, yaptırımdan daha kalıcı sonuç verir.

**Çatışmanın türleri.**

- **Hedef çatışması:** Üretici hacim ister, zincir kategori kârı ister.
- **Alan çatışması:** Bayi bölge dışına satar, toptancı bayinin müşterisine girer, üretici bayinin müşterisine doğrudan gider.
- **Algı çatışması:** Taraflar aynı veriye farklı bakar, örneğin stoksuzluğun nedeni konusunda.

Her çatışma kötü değildir. Açıkça konuşulan çatışma, süreçleri iyileştirebilir. Zararlı olan, ölçülmeyen ve sürekli tekrarlanan çatışmadır.

> **Dikkat:** Güçlü tarafın baskısı bazı durumlarda rekabet hukuku veya haksız ticari uygulama kurallarına takılabilir. Şüpheli bir talep karşısında hukuk danışmanınıza başvurun.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek bir firmaya ait değildir; hesaplar `scripts/cards_numbers_fmcg_b1.py` ile yapılmıştır.

Bir üretici yılda 40.000.000 TL'lik ürünü bir zincire satıyor; katkı payı oranı %30. Zincir yıllık görüşmede ek %2 iskonto istiyor ve vermezse bazı ürünleri listeden çıkaracağını söylüyor.

- Zincirden gelen yıllık katkı: 40.000.000 × 0,30 = **12.000.000 TL**
- Ek %2 iskontonun maliyeti: 40.000.000 × 0,02 = **800.000 TL**
- Listeden tamamen çıkarılma, hiç geri kazanım yoksa: **12.000.000 TL** katkı kaybı.
- Müşterilerin %40'ı ürünü başka mağazadan almaya devam ederse: kayıp **7.200.000 TL**.

İlk bakışta iskontoyu vermek kârlı görünür. Ama soru yalnızca bu yılın 800.000 TL'si değildir. İskonto kalıcı mı olacak? Karşılığında raf, teşhir ya da hacim taahhüdü alınabilir mi? Zincirin size bağımlılığı ne kadar? Hesabı bu sorularla birlikte masaya götürmek pazarlık gücünüzü artırır.

## Sık yapılan hatalar

- Bağımlılığı tek yönlü görmek; zincirin size olan ihtiyacını hiç hesaplamamak.
- Listeden çıkarma tehdidinin maliyetini geri kazanım oranı olmadan hesaplamak.
- Karşılık almadan iskonto vermek ve iskontonun sonraki yıllara taşınmasına izin vermek.
- Bayi bölge çatışmalarını kural yazmadan, her seferinde ayrı pazarlıkla çözmeye çalışmak.
- Yaptırım gücüne fazla güvenip uzmanlık ve veri gücünü ihmal etmek.

## Pratikte nasıl uygulanır?

- [ ] İlk 10 müşteriniz için iki yönlü bağımlılık tablosu hazırlayın: sizin satışınızdaki payları ve sizin onların kategorisindeki payınız.
- [ ] Her büyük müşteri için listeden çıkarılma senaryosunu %0 ve gerçekçi bir geri kazanım oranıyla TL olarak hesaplayın.
- [ ] Ek iskonto taleplerine karşılık isteyeceğiniz unsurları (raf, teşhir, hacim, ödeme süresi) önceden listeleyin.
- [ ] Bayi bölgeleri, müşteri sahipliği ve bölge dışı satış kurallarını yazılı hâle getirin.
- [ ] Çatışma kayıtlarını (konu, taraf, çözüm süresi) tutun ve çeyrekte bir gözden geçirin.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın.

## Daha fazlası

- Coughlan, A. T.; Anderson, E.; Stern, L. W.; El-Ansary, A. I. (2006). *Marketing Channels.* (kaynak doğrulanmadı)
- Rekabet Kurumu (2026). *Rekabet Kurumu.* https://www.rekabet.gov.tr/
