---
id: kb-eco-18-3-real-vs-nominal-interest-fisher
title: "Reel ve nominal faiz: Borç gerçekte ne kadara mal oluyor?"
summary: "Nominal faizden enflasyon beklentisini ayırarak reel faizi hesaplamayı, tedarikçi vade farkının yıllık maliyetini ve negatif reel faizin borçlanma ve stok kararlarına etkisini anlatır."
course: eco
category: makroekonomi-ve-enflasyon
tags: [faiz, enflasyon, finansman]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, finans-muduru]
level: temel
source_lessons: [ECO-18.3]
reading_minutes: 3
key_points:
  - "Reel faiz, nominal faizin beklenen enflasyondan arındırılmış hâlidir: (1 + nominal) / (1 + enflasyon) − 1."
  - "Yüksek enflasyonda basit çıkarma (nominal − enflasyon) reel faizi olduğundan yüksek gösterir."
  - "Aylık vade farkı yıllığa bileşik olarak çevrilmeli ve enflasyonla karşılaştırılmalıdır."
  - "Reel faiz negatifken borçlanmak cazip görünür; ama beklenti değişirse risk hızla büyür."
glossary_terms: [reel-faiz, fisher-denklemi]
related: [kb-eco-50-4-tcmb-policy-rate-credit, kb-eco-25-2-loans-real-vs-nominal, kb-eco-2-5-growth-rates-and-logs, kb-eco-32-4-finance-in-high-inflation]
sources:
  - title: "The Theory of Interest"
    authors: "Fisher, I."
    year: 1930
    type: book
    verified: true
    checked_on: 2026-10-28
  - title: "The Economy 2.0"
    authors: "CORE Econ"
    year: 2026
    type: web
    url: "https://www.core-econ.org/the-economy/"
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

Bankanın teklif ettiği %50 faiz pahalı mı, ucuz mu? Tedarikçinin aylık %4 vade farkı mı daha kötü, banka kredisi mi? Bu sorulara cevap, nominal faizi enflasyonla birlikte okumaktan geçer. Bu kart, borçlanma ve vade kararlarında reel maliyeti hesaplamanızı sağlar.

## Temel fikir

**Nominal faiz**, sözleşmede yazan orandır. **Reel faiz** (*real interest rate*), bu oranın enflasyondan arındırılmış hâlidir; yani borç verenin satın alma gücü olarak ne kazandığını, borçlunun gerçekte ne ödediğini gösterir.

**Fisher denklemi** (*Fisher equation*), Irving Fisher'ın (1930) faiz teorisine dayanır:

(1 + nominal faiz) = (1 + reel faiz) × (1 + beklenen enflasyon)

Buradan reel faiz = (1 + nominal) / (1 + enflasyon) − 1. Düşük enflasyonda nominal faizden enflasyonu çıkarmak yeterli bir yaklaşımdır; yüksek enflasyonda bu yaklaşım ciddi hata verir.

İki pratik not:

- Karar anında bilinen **beklenen** enflasyondur; gerçekleşen enflasyon sonradan öğrenilir. Beklenti yanılırsa borçlu ya da borç veren beklenmedik şekilde kazanır veya kaybeder.
- Kıyas yaparken aynı dönem uzunluğunu kullanın: aylık oranları bileşik olarak yıllığa çevirin.

### İşletme kararlarında reel faiz

- **Borçlanma:** Reel faiz negatifken borçlanmak, borcun reel değerinin erimesi nedeniyle cazip görünür. Ancak bu avantaj, satış fiyatlarınızın enflasyonla birlikte artabilmesine bağlıdır. Fiyatlarınızı artıramıyorsanız reel faiz düşük olsa bile borcu ödemek zorlaşabilir.
- **Nakit tutmak:** TL nakdi faiz getirmeyen hesaplarda tutmak, reel olarak değer kaybetmek demektir. Kısa vadeli nakit fazlası için getiri ve likiditeyi birlikte değerlendirin.
- **Vade farkı:** Müşteriye uyguladığınız vade farkının reel karşılığına bakın. Vade farkı enflasyonun altındaysa, müşteriye reel bir indirim vermiş olursunuz.
- **Yatırım:** Yatırım projelerinde reel nakit akışlarını reel iskonto oranıyla, nominal nakit akışlarını nominal iskonto oranıyla değerlendirin.

### Beklenen enflasyonu nereden bulursunuz?

TCMB'nin yayımladığı piyasa katılımcıları anketi, enflasyon raporları ve piyasada işlem gören TÜFE'ye endeksli tahvillerle normal tahvillerin getiri farkı, beklenti hakkında fikir verir. Kendi sektörünüzdeki maliyet artışları ise genel enflasyondan farklı olabilir; kendi kararlarınız için sektörünüzün maliyet enflasyonunu da izleyin.

## Bir örnek

> **Örnek (temsili rakamlar):** Faiz ve enflasyon oranları örnek amaçlıdır; güncel veriyi temsil etmez. Hesaplar `scripts/cards_numbers_eco_b2.py` ile yapılmıştır.

**Banka kredisi.** Nominal faiz %50, beklenen enflasyon %40.

- Reel faiz = 1,50 / 1,40 − 1 = **%7,14**.
- Basit çıkarma %10 verir; gerçek maliyeti abartır.

**Tedarikçi vade farkı.** Aylık %4 vade farkı yıllık bileşik **%60,1** eder. Aynı enflasyon beklentisiyle reel maliyeti **%14,4**. Bu örnekte vade farkı, banka kredisinden pahalıdır; peşin ödeyip krediyle finanse etmek daha ucuz olabilir.

**Negatif reel faiz.** Nominal faiz %45, beklenen enflasyon %55 ise reel faiz **−%6,5**. Borçlanıp stoğa ya da sabit kıymete yatırım yapmak cazip görünür. Ancak enflasyon beklentisi düşer veya faiz aniden yükselirse aynı borç pahalılaşır.

## Sık yapılan hatalar

- Kredi tekliflerini yalnızca nominal faize göre karşılaştırmak; masrafları ve vadeyi göz ardı etmek.
- Aylık vade farkını 12 ile çarparak yıllığa çevirmek.
- Geçmiş enflasyonu, beklenen enflasyon yerine kullanmak.
- Negatif reel faizin süreceğini varsayarak kısa vadeli krediyle uzun vadeli yatırım finanse etmek.
- Müşteriye uygulanan vade farkını reel olarak hesaplamamak; enflasyonun altında vade farkıyla müşteriyi finanse etmek.

## Pratikte nasıl uygulanır?

- [ ] Tüm finansman seçeneklerini (banka kredisi, tedarikçi vadesi, faktoring, DBS) aynı tabloda yıllık bileşik ve reel olarak karşılaştırın.
- [ ] Enflasyon beklentisi için tek bir kaynak belirleyin (ör. TCMB Piyasa Katılımcıları Anketi) ve tutarlı kullanın.
- [ ] Müşterilerinize uyguladığınız vade farkının reel olarak pozitif olup olmadığını kontrol edin.
- [ ] Değişken faizli borçlarda faiz artışı senaryosunu nakit planına ekleyin.
- [ ] Uzun vadeli yatırımları mümkünse vadesi uyumlu kaynakla finanse edin.

## Daha fazlası

- Fisher, I. (1930). *The Theory of Interest*.
- CORE Econ (2026). *The Economy 2.0*. https://www.core-econ.org/the-economy/
