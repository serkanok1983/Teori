# OMURGA Bilgi Bankası — İçerik Paketi v1.0

Bu paket, OMURGA-Saha uygulamasının bilgi bankası için **288 taslak kartı** (FMCG 97, Ekonomi 85, İşletme Mimarisi 106), 477 terimlik sözlüğü, şemayı, yazım kurallarını, ders haritasını ve kontrol betiklerini içerir. Claude Code'a verilecek entegrasyon talimatı `INTEGRATION-BRIEF.md` dosyasındadır.

## İçerik
| Dosya / klasör | Açıklama |
|---|---|
| `INTEGRATION-BRIEF.md` | Claude Code için entegrasyon ve birleştirme (merge) talimatı (İngilizce) |
| `SCHEMA.md` | Kart alanları ve gövde yapısı |
| `STYLE-GUIDE.md` | Türkçe yazım kuralları (sayı/para biçimi dahil) |
| `taxonomy.md` | 33 kategori, 3 üst grup, roller, önerilen etiketler |
| `map/LESSON-MAP.md`, `map/LESSON-MAP.csv` | 570 dersin hangi karta dönüştüğü |
| `map/PLANNED-CARDS.csv`, `map/planned_card_ids.txt` | 288 kartın listesi |
| `cards/<kategori>/<id>.md` | 288 kart, hepsi `status: draft` |
| `glossary/terms.md` | Birleştirilmiş sözlük (477 terim, Türkçe alfabetik) |
| `glossary/_merged/` | Birleştirilen eski `terms-*-new.md` dosyaları ve `MERGE-LOG.md` (yeniden adlandırma ve birleştirme kaydı). Yalnızca arşivdir; içe aktarılmaz. |
| `reports/QA-REPORT.md` | Kalite raporu (otomatik bölüm + Türkçe kalite geçişi kaydı) |
| `reports/REVIEW-NEEDED.md` | Mali müşavir/avukat incelemesi gereken kartlar ve doğrulanamayan kaynaklar |
| `reference/` | Üç müfredatın kopyası (kaynak ders listesi) |
| `scripts/` | Doğrulayıcı, toplu kontrol, harita üreticisi ve örnek rakam betikleri (`cards_numbers_*.py` + `.out`) |

Kartların düzenlenebilir aslı `cards/` altındaki Markdown dosyalarıdır. Eski çalışma kopyaları (`scripts/eco_src_backup`) pakete alınmamıştır.

## Kontrol
```bash
pip install pyyaml
bash scripts/check-all.sh       # doğrulayıcı + tutarlılık kontrolleri → reports/QA-REPORT.md
python3 scripts/validate.py     # yalnızca doğrulayıcı
```
Beklenen sonuç: 288 kart, 0 hata. Uyarılar yalnızca `verified: false` kaynaklardır.

Örnek rakamlar betiklerle üretilmiştir; `python3 scripts/cards_numbers_eco_b1.py` gibi çalıştırıp çıktıyı aynı adlı `.out` dosyasıyla karşılaştırabilirsiniz.

## Yayın akışı
Tüm kartlar `status: draft`. Serkan incelemeden sonra `reviewed`, ardından `published` yapar. Yalnızca `published` kartlar son kullanıcıya gösterilir. Doğrulanmamış kaynağı olan kart `published` olamaz (STYLE-GUIDE). `time_sensitive: true` olan 47 kartta `valid_as_of` tarihi gösterilir.
