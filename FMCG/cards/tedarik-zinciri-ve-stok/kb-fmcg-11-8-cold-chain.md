---
id: kb-fmcg-11-8-cold-chain
title: "Soğuk zincir: Sıcaklığa duyarlı ürünlerde dağıtım"
summary: "Süt ürünleri, şarküteri, dondurma ve dondurulmuş gıdalar gibi ürünler, üretimden rafa kadar belirli sıcaklık aralığında tutulmalıdır. Bu kart soğuk zincirin halkalarını, en sık kırılma noktalarını, izleme yatırımının ekonomisini ve kalan raf ömrünün satışa etkisini anlatır."
course: fmcg
category: tedarik-zinciri-ve-stok
tags: [tedarik-zinciri, lojistik, kalite]
roles: [depo-lojistik-muduru]
level: orta
source_lessons: [FMCG-11.8]
reading_minutes: 4
key_points:
  - "Soğuk zincir, ancak en zayıf halkası kadar güçlüdür; kırılmalar çoğu zaman yükleme, boşaltma ve mağaza arka deposunda olur."
  - "Sıcaklık sapması, ürün görünüşte sağlam olsa bile kalite ve gıda güvenliği riskini artırabilir."
  - "Sürekli sıcaklık izleme, beklenen kayıp ve iade maliyetiyle karşılaştırılarak değerlendirilmelidir."
  - "Zincirde geçen her gün, mağazada satış için kalan raf ömrünü kısaltır."
  - "Son kullanma tarihi yönetimi için ilk giren ilk çıkar yerine son kullanma tarihi önce çıkar kuralı uygulanır."
glossary_terms: [soguk-zincir, dagitim-merkezi, hizmet-maliyeti, raf-bulunurlugu]
related: [kb-fmcg-11-7-warehouse-transport-network, kb-fmcg-11-1-supply-chain-basics, kb-fmcg-6-3-cost-to-serve, kb-fmcg-9-4-osa-out-of-stock, kb-fmcg-7-1-distributor-pnl]
sources:
  - title: "Supply Chain Management: Strategy, Planning, and Operation"
    authors: "Chopra, S.; Meindl, P."
    year: 2016
    type: book
    verified: false
    note: "Kitap; baskı yılı kontrol edilmedi."
  - title: "ECR Community"
    authors: "ECR Community"
    year: 2026
    type: web
    url: "https://www.ecr-community.org/"
    verified: true
    checked_on: 2026-10-28
    note: "URL HTTP 200 ile açıldı, başlık/kurum eşleşti (2026-10-28)."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28

---

## Ne işe yarar?

Bir yoğurt kolisi fabrikadan doğru sıcaklıkta çıkar, ama aktarma deposunda bir saat rampada bekler, dağıtım aracının soğutucusu kapı açık kaldığı için ısınır, mağazanın arka deposunda dolap dolu olduğu için zeminde kalır. Sonuçta raf ömrü kısalır, şişkin ambalaj iadeleri gelir ve tüketici şikâyet eder. Bu kart, soğuk zincirin (*cold chain*) nerede kırıldığını, bunu nasıl ölçeceğinizi ve önleme yatırımının ekonomisini değerlendirmenizi sağlar.

## Temel fikir

**Halkalar.** Tipik bir hızlı tüketim soğuk zinciri şu halkalardan oluşur: fabrika soğuk deposu, ana taşıma, dağıtım merkezi ya da dağıtıcı deposu, dağıtım aracı, mağaza arka deposu ve satış dolabı. Ürün her halkada ve özellikle halkalar arasındaki geçişlerde risk altındadır.

**Sıcaklık sınıfları.** Ürünler genellikle soğutulmuş (örneğin süt ürünleri, şarküteri) ve dondurulmuş (dondurma, dondurulmuş gıda) olarak iki ana sınıfta yönetilir. Her ürünün saklama koşulu etiketinde ve ürün şartnamesinde yazar; hedef aralıklar ürün ve mevzuata göre değişir, bu nedenle her ürün için kalite biriminin belirlediği aralığı esas alın.

**Sık kırılma noktaları.**

- Yükleme ve boşaltmada rampada bekleme
- Çok noktaya teslimat yapan araçlarda kapının sık açılması
- Ön soğutma yapılmadan araca yükleme
- Mağaza arka deposunda yetersiz dolap kapasitesi
- Satış dolaplarının aşırı doldurulması ya da kapaklarının açık bırakılması

**İzleme.** Araç ve depolarda sürekli sıcaklık kaydı yapan cihazlar, sapmanın nerede ve ne kadar sürdüğünü gösterir. Kayıt olmadan, bir iade ya da şikâyetin kaynağını bulmak çoğu zaman imkânsızdır.

**Kalan raf ömrü.** Kısa raf ömürlü ürünlerde, zincirde geçen her gün mağazada satış için kalan süreyi azaltır. Perakendeciler genellikle teslimatta belirli bir kalan raf ömrü oranı ister. Bu nedenle soğuk zincir, yalnızca bir kalite konusu değil, aynı zamanda bir satış ve fire konusudur.

**Stok sırası.** Soğuk zincirde stok, ilk giren ilk çıkar kuralı yerine son kullanma tarihi en yakın olan önce çıkar kuralıyla yönetilmelidir. Aksi hâlde farklı partilerin karışması fireyi artırır.

## Bir örnek

> **Örnek (temsili rakamlar):** Sevkiyat değeri, sapma olasılıkları, izleme maliyeti ve raf ömrü varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b7.py` ile yapılmıştır.

Bir üretici, her biri **500.000 TL** değerinde yılda **400** soğuk sevkiyat yapıyor. Geçmiş kayıtlara göre sevkiyatların yaklaşık **%2**'sinde ürünün imha ya da iadesini gerektiren bir sıcaklık sapması yaşanıyor.

- Sevkiyat başına beklenen kayıp: 500.000 × %2 = **10.000 TL**
- Sürekli izleme ve uyarı sistemiyle sapma olasılığının **%0,5**'e inmesi bekleniyor; beklenen kayıp **2.500 TL**.
- İzleme maliyeti sevkiyat başına **1.500 TL**.
- Sevkiyat başına net kazanç: 10.000 − 2.500 − 1.500 = **6.000 TL**; yılda **2.400.000 TL**.

Ayrıca **10** günlük raf ömrü olan bir üründe zincirde **4** gün geçerse, mağazaya ürünün raf ömrünün yalnızca **6** günü, yani **%60**'ı kalır. Zinciri bir gün kısaltmak, mağazadaki satış süresini belirgin biçimde uzatır.

Bu hesap, sapma olasılığının gerçekten bu ölçüde azalacağı varsayımına dayanır. İlk aşamada izlemeyi pilot bir bölgede deneyip gerçek sapma oranını ölçmek, varsayımı doğrulamanın en güvenilir yoludur.

## Sık yapılan hatalar

- **Yalnızca fabrika çıkışını kontrol etmek.** Kırılmaların çoğu sonraki halkalarda olur.
- **Sıcaklık kaydını yalnızca şikâyet gelince okumak.** Kayıtlar düzenli olarak incelenmeli ve sapmalar raporlanmalıdır.
- **Mağaza dolap kapasitesini sipariş miktarıyla birlikte planlamamak.** Fazla teslimat, ürünün dolap dışında kalmasına yol açar.
- **Kalan raf ömrünü izlememek.** Zincir uzadıkça perakendeci kabul şartları karşılanamaz.
- **Soğuk zincir maliyetini müşteri kârlılığına yansıtmamak.** Küçük ve uzak noktalara soğuk teslimat pahalıdır.

## Pratikte nasıl uygulanır?

- [ ] Soğuk zincirinizin bütün halkalarını ve geçiş noktalarını bir akış şemasında gösterin.
- [ ] Araç ve depolarda sürekli sıcaklık kaydı başlatın; önce pilot bir bölgede deneyin.
- [ ] Sapma oranını, imha ve iade maliyetini aylık olarak raporlayın.
- [ ] Zincirde geçen gün sayısını ve teslimatta kalan raf ömrünü ölçün.
- [ ] Depo ve mağazalarda son kullanma tarihi önce çıkar kuralını uygulayın.
- [ ] Soğuk teslimatın hizmet maliyetini müşteri kârlılığı hesabına ekleyin.

## Daha fazlası

- Chopra, S.; Meindl, P. (2016). *Supply Chain Management: Strategy, Planning, and Operation.* (kaynak doğrulanmadı)
- ECR Community (2026). *ECR Community.* https://www.ecr-community.org/
