---
id: kb-eco-14-2-inflation-measurement-tufe-ufe
title: "Enflasyonu ölçmek: TÜFE, Yİ-ÜFE ve kendi maliyet enflasyonunuz"
summary: "Tüketici ve üretici fiyat endekslerinin neyi ölçtüğünü, baz etkisini ve bir distribütörün ya da üreticinin kendi maliyet sepetine göre enflasyon hesaplamasını anlatır."
course: eco
category: makroekonomi-ve-enflasyon
tags: [enflasyon, maliyet, fiyatlama]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, finans-muduru]
level: temel
source_lessons: [ECO-3.7, ECO-14.2]
reading_minutes: 3
key_points:
  - "TÜFE hanehalkının tükettiği sepetin, Yİ-ÜFE üreticilerin sattığı malların fiyat değişimini ölçer."
  - "Şirketin kendi maliyet artışı, resmî endekslerden belirgin şekilde farklı olabilir."
  - "Kendi maliyet sepetinizi ağırlıklarla kurarak gerçek maliyet enflasyonunuzu hesaplayın."
  - "Yıllık enflasyon, geçen yılın aynı dönemindeki yüksek ya da düşük aylık artışların çıkmasıyla değişir (baz etkisi)."
  - "Sözleşmelerde hangi endeksin, hangi tarihteki değerinin kullanılacağını açıkça yazın."
glossary_terms: [tufe, ufe, baz-etkisi]
related: [kb-eco-2-5-growth-rates-and-logs, kb-eco-19-3-supply-shocks-cost-inflation, kb-eco-32-4-finance-in-high-inflation, kb-fmcg-5-6-pricing-in-high-inflation]
sources:
  - title: "Türkiye İstatistik Kurumu (resmî site)"
    authors: "TÜİK"
    year: 2026
    type: web
    url: "https://www.tuik.gov.tr"
    verified: true
    checked_on: 2026-10-28
  - title: "Enflasyon Verileri — Tüketici Fiyatları"
    authors: "TCMB"
    year: 2026
    type: web
    url: "https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Istatistikler/Enflasyon+Verileri"
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

Kira, maaş, nakliye ve tedarik sözleşmeleri çoğu zaman bir enflasyon endeksine bağlanır. Fiyat artışı pazarlıklarında da "enflasyon şu kadar" cümlesi kullanılır. Bu kart, hangi endeksin neyi ölçtüğünü ve şirketiniz için anlamlı olan maliyet enflasyonunu nasıl hesaplayacağınızı anlatır.

## Temel fikir

- **TÜFE (Tüketici Fiyat Endeksi)**: Hanehalklarının satın aldığı mal ve hizmetlerden oluşan bir sepetin fiyat değişimini ölçer. Sepet ağırlıkları hane harcama anketlerine dayanır ve dönemsel olarak güncellenir.
- **Yİ-ÜFE (Yurt İçi Üretici Fiyat Endeksi)**: Üreticilerin yurt içinde sattığı malların, vergiler hariç üretici fiyatlarındaki değişimi ölçer. Hammadde ve enerji fiyatlarındaki değişim burada daha erken görülür.
- **Çekirdek göstergeler**: Enerji, gıda gibi oynak kalemlerin dışarıda bırakıldığı endekslerdir; ana eğilimi görmek için kullanılır.

Türkiye'de bu endeksleri TÜİK aylık olarak yayımlar; TCMB de enflasyon verilerini ve analizlerini paylaşır.

**Kendi maliyet enflasyonunuz:** Bir distribütörün gider yapısı (personel, akaryakıt, kira, araç bakım) TÜFE sepetinden çok farklıdır. Kendi gider kalemlerinizi ağırlıklandırarak hesapladığınız maliyet artışı, fiyat ve marj görüşmelerinde daha savunulabilir bir dayanaktır.

**Baz etkisi** (*base effect*): Yıllık enflasyon son 12 ayın aylık artışlarının bileşkesidir. Geçen yılın aynı ayında çok yüksek bir aylık artış varsa, o ay hesaptan çıktığında yıllık oran düşer; bu, fiyatların düştüğü anlamına gelmez.

## Bir örnek

> **Örnek (temsili rakamlar):** Ağırlıklar, artış oranları ve endeks değerleri varsayımsaldır; gerçek TÜFE veya Yİ-ÜFE verisi değildir. Hesaplar `scripts/cards_numbers_eco_b2.py` ile yapılmıştır.

Bir distribütörün faaliyet gideri sepeti:

| Kalem | Ağırlık | Yıllık artış | Katkı (puan) |
|---|---|---|---|
| Personel | %40 | %50 | 20,0 |
| Akaryakıt | %25 | %30 | 7,5 |
| Kira | %20 | %60 | 12,0 |
| Diğer | %15 | %40 | 6,0 |

Kendi maliyet enflasyonu **%45,5**. Aynı dönemde örnek TÜFE %40, örnek Yİ-ÜFE %35 olsun. Distribütörün maliyeti TÜFE'nin 5,5 puan üstünde artmış. Üreticiyle marj görüşmesinde bu tablo, "enflasyon kadar artış" önerisinden daha güçlü bir argümandır.

**Baz etkisi:** On bir ay boyunca aylık %3, son ayda %8 artış olan bir yılda yıllık oran %49,5. Ertesi yıl her ay %3 artış olursa yıllık oran %42,6'ya iner; aylık fiyat artış hızı değişmediği hâlde yıllık rakam düşmüştür.

## Sık yapılan hatalar

- Her maliyet kalemini TÜFE ile güncellemek; kendi gider yapınızı yansıtmamak.
- Yıllık enflasyondaki düşüşü fiyat artışlarının durduğu şeklinde yorumlamak.
- Sözleşmelerde endeksi, ayı ve hesaplama yöntemini (yıllık mı, 12 aylık ortalama mı) belirtmemek.
- Yİ-ÜFE'deki artışı izlememek; bu artış birkaç ay sonra alış fiyatlarınıza yansıyabilir.
- Endeks değerlerini ikincil kaynaklardan almak; resmî kaynaktan doğrulamamak.
- Sözleşmelerde endeks türünü (TÜFE, ÜFE, ilgili alt endeks) ve hangi ayın verisinin kullanılacağını belirtmemek.

## Pratikte nasıl uygulanır?

- [ ] Kendi faaliyet gider sepetinizi ağırlıklarıyla tanımlayın; artışını üç ayda bir hesaplayın.
- [ ] Yİ-ÜFE ve ilgili alt kalemlerini (gıda, kimya, ambalaj) aylık izleyin; alış fiyatı artışlarını önceden tahmin edin.
- [ ] Endekse bağlı sözleşmelerde endeks adı, referans ayı ve formülü açıkça yazın.
- [ ] Fiyat görüşmelerinde kendi maliyet enflasyonu tablonuzu kullanın.
- [ ] Endeks verilerini TÜİK ve TCMB'nin resmî yayınlarından alın.
- [ ] Kendi maliyet sepetinize en yakın alt endeksleri belirleyin ve fiyat güncellemelerinde bunları referans alın.

## Daha fazlası

- TÜİK (2026). *Türkiye İstatistik Kurumu (resmî site)*. https://www.tuik.gov.tr
- TCMB (2026). *Enflasyon Verileri — Tüketici Fiyatları*. https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Istatistikler/Enflasyon+Verileri
- CORE Econ (2026). *The Economy 2.0*. https://www.core-econ.org/the-economy/
