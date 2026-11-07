# SCHEMA — Bilgi Bankası kartı (makale) şeması — v0.1

Bu dosya, paketteki her kartın (makalenin) biçimini tanımlar. Bir kart = tek bir Markdown dosyası = YAML frontmatter + gövde.
Şema bilerek küçük ve kararlı tutuldu; içe aktarıcı (importer) yalnızca buradaki alanlara güvenmelidir.
Makineyle doğrulama: `python3 scripts/validate.py` (PyYAML gerekir: `pip install pyyaml`).

## 1. Dosya adı ve konum

- Yol: `cards/<category>/<id>.md` — `<category>` taxonomy.md'deki kategori kısa adıdır (slug), dosya adı kartın `id`'sidir.
- Kodlama UTF-8, satır sonu LF. Türkçe karakterler (ç ğ ı İ ö ş ü â) olduğu gibi yazılır; HTML entity kullanılmaz.

## 2. Frontmatter alanları

| Alan | Tür | Zorunlu | Kural |
|---|---|---|---|
| `id` | string | evet | Kalıcı anahtar. Biçim: `kb-<course>-<ünite>-<ders>-<ingilizce-slug>`; regex `^kb-(fmcg\|eco\|ea)-\d+-\d+-[a-z0-9]+(-[a-z0-9]+)*$`. Asla değiştirilmez, yeniden kullanılmaz. Örnek: `kb-fmcg-1-1-margin-vs-markup`. Birleştirilmiş kartlarda numara, birincil dersten gelir. |
| `title` | string | evet | Türkçe başlık, en çok 90 karakter. |
| `summary` | string | evet | 1–2 cümle, en çok 300 karakter; listelerde ve arama sonuçlarında görünür. |
| `course` | enum | evet | `fmcg` \| `eco` \| `ea` (birincil dersin kursu). |
| `category` | string | evet | taxonomy.md'deki kategori slug'larından biri; dosyanın bulunduğu klasörle aynı olmalı. |
| `tags` | list[string] | evet (≥1) | Küçük harf, ASCII, tire ile: `marj`, `fiyatlama`. Serbest ama taxonomy.md'deki önerilen etiketler tercih edilir. |
| `roles` | list[enum] | evet (≥1) | Sabit sözlük (aşağıda). |
| `level` | enum | evet | `temel` \| `orta` \| `ileri`. |
| `source_lessons` | list[string] | evet (≥1) | Müfredat ders kimlikleri: `FMCG-1.1`, `ECO-38.2`, `EA-20.2`. Hepsi `map/LESSON-MAP.csv` içinde bulunmalı. |
| `reading_minutes` | int | evet | 1–20. Gövdedeki kelime sayısı ÷ 200, yukarı yuvarlanmış (doğrulayıcı ±2 dk tolerans uygular). |
| `key_points` | list[string] | evet (3–6) | Kartın özü; her madde tek cümle. Uygulama bunu "Akılda kalsın" kutusu olarak gösterebilir. |
| `glossary_terms` | list[string] | hayır | `glossary/terms.md` içindeki terim `id`'leri. |
| `related` | list[string] | hayır | Diğer kart `id`'leri. Her biri ya pakette mevcut ya da `map/planned_card_ids.txt` içinde planlı olmalı. |
| `sources` | list[object] | evet (≥1) | Bkz. §4. |
| `time_sensitive` | bool | evet | Vergi oranı, mevzuat, faiz, kur, piyasa yapısı gibi zamanla eskiyen bilgi içeriyorsa `true`. |
| `valid_as_of` | date \| null | koşullu | `YYYY-MM-DD`. `time_sensitive: true` ise zorunlu; içerikteki zamana bağlı bilginin doğrulandığı tarih. |
| `status` | enum | evet | `draft` \| `reviewed` \| `published`. Uygulamada yalnızca `published` görünür. |
| `language` | enum | evet | Şimdilik yalnızca `tr`. |
| `version` | string | evet | Kartın sürümü, SemVer-benzeri `MAJOR.MINOR` (ör. `0.1`). İçerik anlamı değişirse MINOR, yapı değişirse MAJOR artar. |
| `updated` | date | evet | Kartın son değiştirildiği tarih, `YYYY-MM-DD`. |

Bilinmeyen alan eklenmez; gerekiyorsa önce bu şema sürümü artırılır.

## 3. Rol sözlüğü (sabit)

| Değer | Görünen ad (TR) |
|---|---|
| `uretici-sahibi` | Üretici firma sahibi / ortağı |
| `uretici-yonetici` | Üretici firma yöneticisi (genel müdür, pazarlama, ticari) |
| `bayi-sahibi` | Bayi / distribütör sahibi |
| `bayi-yonetici` | Bayi / distribütör yöneticisi |
| `satis-direktoru` | Satış direktörü |
| `satis-muduru` | Satış müdürü |
| `bolge-muduru` | Bölge müdürü |
| `satis-sefi` | Satış şefi |
| `saha-satis-temsilcisi` | Saha satış temsilcisi |
| `finans-muduru` | Finans müdürü / mali işler |
| `depo-lojistik-muduru` | Depo ve lojistik müdürü |
| `it-yoneticisi` | BT (bilgi teknolojileri) yöneticisi |

## 4. `sources` nesnesi

```yaml
sources:
  - title: "Vertical Integration and Antitrust Policy"   # zorunlu
    authors: "Spengler, J. J."                            # zorunlu (kurum adı da olabilir)
    year: 1950                                            # zorunlu (int) — web sayfasında yayın yılı yoksa erişim yılı
    type: article                                         # article | book | web | law | standard | dataset
    doi: "10.1086/256964"                                 # article için varsa
    url: "https://doi.org/10.1086/256964"                 # web/law/dataset için zorunlu
    verified: true                                        # zorunlu bool: DOI Crossref'te ya da URL HTTP 200 ile açılıp başlık eşleştiyse true
    checked_on: 2026-10-28                                # verified: true ise zorunlu
    note: "Çift marjinalleşme sonucu"                     # isteğe bağlı
```
`verified: false` olan kaynaklı kart `published` olamaz (doğrulayıcı hata verir); `reviewed` olabilir.

## 5. Gövde yapısı

Başlıklar tam olarak bu sırayla ve bu adlarla (H2) yazılır; içe aktarıcı bölümleri bunlara göre tanıyabilir:

1. `## Ne işe yarar?` — 2–4 cümlelik kısa özet: bu bilgi okuyucunun hangi kararında, hangi işinde işe yarar.
2. `## Temel fikir` — Kavram, tanım, formül (düz metin; isteğe bağlı KaTeX, bkz. STYLE-GUIDE §6), neden önemli olduğu.
3. `## Bir örnek` — Sayısal, adım adım çözülmüş örnek. Her adım gösterilir. Gerçek veri değilse başlığın altında ilk satır şu etiketi taşır: `> **Örnek (temsili rakamlar):** …`. Tüm sayılar bir script ile hesaplanır (pilotlar için `scripts/pilot_numbers.py`).
4. `## Sık yapılan hatalar` — Madde listesi, 3–6 madde.
5. `## Pratikte nasıl uygulanır?` — Kontrol listesi (`- [ ]`), rol odaklı, 4–8 madde.
6. `## Daha fazlası` — Kaynaklar: yazar, yıl, başlık ve bağlantı; ilgili kartlar `related` üzerinden uygulamada ayrıca listelenir.

İsteğe bağlı bloklar:
- Uyarı kutusu (callout): `> **Dikkat:** …` / `> **Mevzuat notu:** …` / `> **İpucu:** …` — düz blockquote; uygulama bunları kutu olarak çizebilir, çizmese de okunur.
- `time_sensitive: true` olan kartlarda gövdenin sonunda (Daha fazlası'ndan önce) şu not zorunludur:
  `> **Mevzuat notu:** Bu karttaki oran ve kurallar <valid_as_of> tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın.`

Uzunluk: gövde 450–1.100 kelime (ileri seviye kartta 1.400'e kadar). Tablo kullanılabilir (GFM).

## 6. Sözlük (glossary) biçimi

Tek dosya: `glossary/terms.md`. Her terim bir H2 başlığı + hemen altında bir ```yaml bloğu:

```yaml
id: marj                    # kalıcı, ASCII, tireli
term: Marj                  # Türkçe görünen ad
en: margin                  # İngilizce karşılık
definition: "Satış fiyatı ile maliyet arasındaki farkın satış fiyatına oranı."
see_also: [maliyet-uzerine-ekleme-orani]
cards: [kb-fmcg-1-1-margin-vs-markup]
```
Kartlardaki `glossary_terms` bu `id`'lere işaret eder.

## 7. Kategori ağacı

`taxonomy.md` içindeki tablo makine tarafından okunur (`| slug | Türkçe ad | üst grup | açıklama |`). Kartın `category` alanı yalnızca bu slug'lardan biri olabilir.

## 8. Tam örnek frontmatter

```yaml
---
id: kb-fmcg-1-1-margin-vs-markup
title: "Marj mı, maliyet üzerine ekleme mi? Fiyatı doğru kurmak"
summary: "..."
course: fmcg
category: sektor-ve-kanal
tags: [marj, fiyatlama, kar-orani]
roles: [bayi-sahibi, satis-muduru]
level: temel
source_lessons: [FMCG-1.1]
reading_minutes: 6
key_points: ["...", "...", "..."]
glossary_terms: [marj]
related: [kb-fmcg-1-1-margin-stack]
sources: [...]
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---
```
