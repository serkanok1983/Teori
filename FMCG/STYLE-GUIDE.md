# Yazım Kılavuzu (STYLE-GUIDE) — OMURGA Bilgi Bankası

Bu kılavuz, `cards/` altındaki her kartın dilini ve içeriğini belirler. Yapısal kurallar `SCHEMA.md` dosyasındadır.

## 1. Dil ve ton
- Doğal, sade ve profesyonel Türkçe yazın. Metin çeviri gibi okunmamalı.
- Okura "siz" diye hitap edin. Emir kipini ölçülü kullanın ("kontrol edin", "izleyin").
- Paragraflar kısa olsun: en fazla 3–4 cümle. Bir cümle tek bir fikir taşısın.
- Akademik dolgu kullanmayın ("literatürde görüldüğü üzere", "bu bağlamda belirtmek gerekir ki" gibi).
- Okur yöneticidir; teoriden önce "bu bana ne kazandırır" sorusunu cevaplayın.

## 2. Terimler
- Yabancı terimi ilk kullanımda parantez içinde ve italik verin: **nakit dönüşüm süresi** (*cash conversion cycle*). Sonra yalnızca Türkçesini kullanın.
- Yerleşik kısaltmalar (ERP, KDV, SFA) kullanılabilir; ilk kullanımda açılımı verilir.
- Kartta geçen her önemli terim `glossary/terms.md` dosyasında bulunmalı ve `glossary_terms` alanında listelenmelidir.

## 3. Sayılar ve birimler
- Türk biçimi: binlik ayırıcı nokta, ondalık virgül: **7.260,00 TL**, **%33,33**, **42,6 gün**.
- Para birimi rakamdan sonra: `1.140,00 TL`. Yüzde işareti önde: `%5`.
- Kuruş kuralı: Birim fiyat ve küçük tutarlarda iki ondalık yazılır (`28,50 TL`, `4.440,00 TL`). Büyük toplamlar ve temsili bütçe rakamları tam sayıya yuvarlanabilir (`7.901.370 TL`). Aynı tablo içinde tek biçim kullanılır.
- Eksi işareti olarak tire değil `−` (U+2212) kullanılır: `−300.000 TL`, `−%6,4`.
- Örnekteki her rakam bir betikle (ör. `scripts/pilot_numbers.py`) hesaplanmış ve kontrol edilmiş olmalıdır. Elle hesap yapılan rakam yayımlanmaz.
- Örnek rakamları her zaman `> **Örnek (temsili rakamlar):**` etiketiyle başlar; gerçek firma verisi gibi sunulmaz.

## 4. Role göre yazım
- `roles` alanındaki rollere göre örnek seçin: bayi sahibi için kâr ve nakit, saha temsilcisi için müşteri ziyareti, finans müdürü için kayıt ve kontrol.
- "Pratikte nasıl uygulanır?" bölümü uygulanabilir bir kontrol listesi olmalıdır (`- [ ]`).

## 5. Kaynaklar ve telif
- Kaynak, metin içinde yazar adı ve yılıyla anılır: "Richards ve Laughlin (1980)".
- Telifli kaynaktan birebir alıntı yapılmaz; fikir kendi cümlelerimizle anlatılır. Kitaplardan tablo, şekil ya da uzun pasaj kopyalanmaz.
- Olgu uydurulmaz. Doğrulanamayan bir bilgi ya kaldırılır ya da kaynağı `verified: false` olarak işaretlenir. Doğrulanmamış kaynağı olan kart `published` olamaz.
- DOI varsa yazılır ve doi.org / Crossref üzerinden kontrol edilir.

## 6. Mevzuat, vergi ve oranlar
- Vergi oranı, e-belge kapsamı, faiz, kur gibi zamanla değişen her bilgi içeren kartta `time_sensitive: true` ve `valid_as_of: YYYY-AA-GG` zorunludur.
- Böyle kartların sonunda şu not bulunur:
  > **Mevzuat notu:** Bu karttaki bilgiler [tarih] tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın.
- Örnekte kullanılan oranlar (ör. KDV %20) "örnek oran" diye etiketlenir.

## 7. Uzunluk
- Hedef 500–900 kelime (yaklaşık 3–5 dakika). `reading_minutes` = kelime ÷ 200, ±2 tolerans (tablolu kartlarda üst sınıra yakın değer verilebilir).

## 8. Kontrol listesi (yayımlamadan önce)
- [ ] `python3 scripts/validate.py` hata vermiyor.
- [ ] Rakamlar betikle doğrulandı.
- [ ] Tüm kaynaklar `verified: true`.
- [ ] Bir alan uzmanı kartı okudu (`status: reviewed`), ardından `published` yapıldı.
