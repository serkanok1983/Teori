---
id: kb-ea-8-2-data-quality-field
title: "Veri kalitesi: Saha ve ERP verisinde neyi, nasıl ölçersiniz?"
summary: "Veri kalitesini doğruluk, tamlık, tutarlılık ve güncellik gibi boyutlarla tanımlamayı; saha satış ve ERP verisinde ölçülebilir kalite kuralları yazmayı ve hataları kaynağında düzeltmeyi anlatır."
course: ea
category: veri-yonetimi
tags: [veri-kalitesi, ana-veri, saha-satis, kpi]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, it-yoneticisi]
level: temel
source_lessons: [EA-8.2]
reading_minutes: 3
key_points:
  - "Veri kalitesi 'kullanıma uygunluk'tur: Aynı veri bir iş için yeterli, diğeri için yetersiz olabilir."
  - "Wang ve Strong veri kalitesini içsel, bağlamsal, gösterimsel ve erişilebilirlik boyutlarıyla ele alır."
  - "Her boyut için ölçülebilir bir kural yazılır: örneğin 'telefon alanı boş olmamalı'."
  - "Hataların çoğu girişte oluşur; düzeltme kaynağında yapılmazsa tekrar eder."
  - "Kalite oranlarını bölge ve temsilci bazında göstermek, sahiplenmeyi artırır."
glossary_terms: [veri-kalitesi, ana-veri]
related: [kb-ea-8-1-master-data-governance, kb-ea-8-3-mdm-matching-duplicates, kb-ea-26-2-field-data-outlet-visit, kb-ea-9-6-bi-dashboards-kpis]
sources:
  - title: "Beyond accuracy: What data quality means to data consumers"
    authors: "Wang, R. Y.; Strong, D. M."
    year: 1996
    type: article
    doi: "10.1080/07421222.1996.11518099"
    url: "https://doi.org/10.1080/07421222.1996.11518099"
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

Rota planlaması yanlış konumlar yüzünden saçmalıyorsa, kampanya SMS'leri boş telefon alanları yüzünden gitmiyorsa ya da kanal raporları "kanal tipi: boş" satırıyla doluysa sorun yazılımda değil veridedir. Bu kart, **veri kalitesini** (*data quality*) ölçülebilir hale getirmenizi sağlar.

## Temel fikir

Wang ve Strong (1996), veri kullanıcılarına sorarak veri kalitesinin yalnızca doğruluktan ibaret olmadığını gösterdi. Dört ana grup tanımladılar:

- **İçsel kalite:** Doğruluk, güvenilirlik.
- **Bağlamsal kalite:** Tamlık, güncellik, işe uygunluk.
- **Gösterimsel kalite:** Anlaşılır ve tutarlı biçim.
- **Erişilebilirlik:** Gereken kişinin veriye ulaşabilmesi ve güvenliği.

Yönetici için pratik boyutlar şunlardır: **tamlık** (alan dolu mu?), **geçerlilik** (biçim doğru mu?), **doğruluk** (gerçeği yansıtıyor mu?), **tutarlılık** (iki sistemde aynı mı?), **güncellik** (ne zaman güncellendi?), **teklik** (mükerrer var mı?).

Her boyut için bir kural yazılır ve oranı ölçülür. Saha verisinde tipik kök nedenler: zorunlu olmayan alanlar, zaman baskısı altındaki temsilci, serbest metin alanları, konumun dükkân yerine yolda alınması.

### Veri kalitesi programını başlatmak

Veri kalitesi, tek seferlik bir temizlikle değil, düzenli ölçüm ve sorumlulukla iyileşir. Küçük ve somut bir başlangıç için şu adımlar önerilir:

- **Önemli alanları seçin:** Tüm alanları ölçmeye çalışmak yerine, iş sonuçlarını doğrudan etkileyen alanlardan başlayın: müşteri vergi numarası, adres ve konum, ürün barkodu, birim dönüşümleri, fiyat ve kredi limiti.
- **Kuralları yazın:** Her alan için geçerlilik kuralını tanımlayın. Örneğin vergi numarası doğru uzunlukta mı, konum bilgisi bölge sınırları içinde mi, barkod kontrol hanesi doğru mu?
- **Ölçün ve yayınlayın:** Kurallara uymayan kayıt oranını düzenli olarak ölçün ve veri sahiplerine bir pano ile gösterin.
- **Kökeni bulun:** Hatalı kayıtların hangi kanaldan ve hangi süreçten geldiğini belirleyin. Saha uygulamasındaki bir ekranın zorunlu alan eksikliği, binlerce hatalı kaydın kaynağı olabilir.
- **Kaynakta önleyin:** Tespit edilen hata türleri için giriş ekranlarına doğrulama ekleyin.

**Saha verisinin özelliği.** Saha ekiplerinin girdiği veriler, zaman baskısı altında ve mobil cihazdan girilir. Açılır listeler, barkod okutma, konumun otomatik alınması ve fotoğrafla belgeleme, serbest metin girişine göre çok daha güvenilir veri sağlar. Wang ve Strong'un vurguladığı gibi, kalite, verinin kullanıcısının bakış açısından tanımlanmalıdır; bu nedenle ölçütleri raporların kullanıcılarıyla birlikte belirlemek gerekir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b2.py` ile yapılmıştır.

5.000 noktalı bir müşteri listesinde kalite kontrolü:

| Kural | Hatalı kayıt | Oran |
|---|---|---|
| Telefon boş olmamalı (tamlık) | 600 | %12,0 |
| Kanal tipi boş olmamalı (tamlık) | 410 | %8,2 |
| Konum, adresin 500 m yakınında olmalı (doğruluk) | 250 | %5,0 |
| Vergi numarası 10 hane olmalı (geçerlilik) | 90 | %1,8 |

Firma önce kaynağı düzeltiyor: Saha uygulamasında telefon ve kanal tipi zorunlu hale geliyor, kanal tipi serbest metin yerine listeden seçiliyor ve konum yalnızca ziyaret sırasında alınıyor. Mevcut hatalı kayıtlar bölgelere dağıtılıp üç ayda temizleniyor ve oranlar aylık bölge raporuna ekleniyor.

## Sık yapılan hatalar

- Veri temizliğini bir kerelik proje yapıp kaynaktaki nedeni düzeltmemek.
- "Kaliteli veri" hedefini ölçülebilir kurala çevirmemek.
- Her alanı zorunlu yapmak; temsilci rastgele değer girmeye başlar.
- Kalite oranını yalnızca BT'nin görmesi.

## Pratikte nasıl uygulanır?

- [ ] İşiniz için en kritik 10 alanı seçin ve her biri için bir kalite kuralı yazın.
- [ ] Kuralları aylık çalıştırıp oranları bölge ve temsilci bazında raporlayın.
- [ ] Serbest metin alanlarını mümkün olduğunca listeden seçime çevirin.
- [ ] Kaynağında düzeltilebilen hataları sistem doğrulamasıyla engelleyin.
- [ ] Hedef oranı belirleyin (ör. tamlık %98) ve yöneticilerin hedefine bağlayın.

## Daha fazlası

- Wang ve Strong (1996), *Journal of Management Information Systems*. https://doi.org/10.1080/07421222.1996.11518099
