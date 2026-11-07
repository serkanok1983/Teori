---
id: kb-fmcg-11-7-warehouse-transport-network
title: "Depo ve taşıma ağı: Kaç dağıtım merkezi, nerede?"
summary: "Dağıtım merkezlerinin sayısı ve yeri, depo, taşıma ve stok maliyetleri ile hizmet süresi arasında bir denge kurar. Bu kart bu dengeyi, stok havuzlamasının etkisini ve hızlı tüketimde ağ kararlarının nasıl değerlendirileceğini anlatır."
course: fmcg
category: tedarik-zinciri-ve-stok
tags: [tedarik-zinciri, lojistik, maliyet]
roles: [depo-lojistik-muduru]
level: orta
source_lessons: [FMCG-11.7]
reading_minutes: 3
key_points:
  - "Dağıtım merkezi sayısı arttıkça depo maliyeti ve güvenlik stoku artar, son kilometre taşıma maliyeti ve teslim süresi azalır."
  - "Güvenlik stoku, kabaca dağıtım merkezi sayısının karekökü ile orantılı olarak artar."
  - "Toplam maliyet, depo, taşıma ve stok maliyetlerinin toplamıdır; tek bir kalemle karar verilmemelidir."
  - "Hizmet süresi hedefi, özellikle zincir ve geleneksel kanal için ağ kararını belirleyebilir."
  - "Çapraz sevkiyat ve doğrudan mağaza teslimatı, ağ tasarımında alternatif modellerdir."
glossary_terms: [dagitim-merkezi, guvenlik-stoku, hizmet-maliyeti, stok-gun-sayisi]
related: [kb-fmcg-11-1-supply-chain-basics, kb-fmcg-11-4-safety-stock, kb-fmcg-11-8-cold-chain, kb-fmcg-7-1-distributor-pnl, kb-fmcg-10-1-key-account-management]
sources:
  - title: "Supply Chain Management: Strategy, Planning, and Operation"
    authors: "Chopra, S.; Meindl, P."
    year: 2016
    type: book
    verified: false
    note: "Kitap; baskı yılı kontrol edilmedi."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Bir üretici tüm Türkiye'ye tek bir merkez depodan mı hizmet vermeli, yoksa bölgesel depolar mı açmalı? Bu karar yıllarca sürecek maliyetleri ve müşterilere ne kadar hızlı teslimat yapılabileceğini belirler. Bu kart, ağ kararlarının temel ödünleşimlerini ve bunları nasıl hesaplayacağınızı anlatır.

## Temel fikir

**Temel ödünleşimler.** Chopra ve Meindl, ağ tasarımını birkaç maliyet kalemi ile hizmet arasındaki bir denge olarak anlatır. Dağıtım merkezi (*distribution center*) sayısı arttıkça:

- **Depo maliyeti artar:** Her depo kira, personel ve sistem gerektirir.
- **Ana taşıma maliyeti artar:** Fabrikadan depolara daha fazla sevkiyat gerekir, ama bunlar genellikle tam araçla yapılır.
- **Son kilometre taşıma maliyeti azalır:** Depolar müşterilere yaklaşır, dağıtım mesafeleri kısalır.
- **Teslim süresi kısalır:** Müşterilere daha hızlı hizmet verilir.
- **Güvenlik stoku artar:** Stok birden fazla depoya bölündüğünde, her depo kendi belirsizliğine karşı stok tutar.

**Stok havuzlaması.** Talep dalgalanmaları depolar arasında birbirinden bağımsızsa, toplam güvenlik stoku kabaca depo sayısının karekökü ile artar. Tek depoda havuzlanan stok, farklı bölgelerdeki dalgalanmaların birbirini kısmen dengelemesinden yararlanır. Bu kural bir yaklaşımdır; bölgeler arasında talep ilişkisi varsa etki farklı olur.

**Hizmet süresi.** Zincir depoları belirli teslim pencereleri ister; geleneksel kanalda dağıtıcı ya da doğrudan satış modeli farklı sıklıklar gerektirir. Bazen hizmet süresi hedefi, maliyet hesabından bağımsız olarak ağ kararını belirler.

**Alternatif modeller.**

- **Çapraz sevkiyat** (*cross-docking*): Ürünler depoda stoklanmadan doğrudan araçlar arasında aktarılır.
- **Doğrudan mağaza teslimatı:** Büyük hacimli müşterilere depoyu atlayarak teslimat.
- **Dış kaynaklı lojistik:** Depolama ve taşımanın üçüncü taraf lojistik firmalarına verilmesi; sabit maliyeti değişkene çevirir.

## Bir örnek

> **Örnek (temsili rakamlar):** Maliyetler ve stok değerleri varsayımdır; güvenlik stoku iki depoda √2 oranında artırılmıştır, stok tutma maliyeti stok değerinin %30'u alınmıştır; hesaplar `scripts/cards_numbers_fmcg_b6.py` ile yapılmıştır.

Bir üretici, tek ve iki dağıtım merkezli ağları karşılaştırıyor (yıllık TL):

| Kalem | 1 dağıtım merkezi | 2 dağıtım merkezi |
|---|---|---|
| Depo maliyeti | 6.000.000 | 9.000.000 |
| Taşıma maliyeti | 14.000.000 | 10.000.000 |
| Güvenlik stoku değeri | 1.000.000 | 1.414.214 |
| Stok tutma maliyeti | 300.000 | 424.264 |
| **Toplam yıllık maliyet** | **20.300.000** | **19.424.264** |

İki depolu ağ, depo ve stok maliyetlerinin artmasına rağmen taşıma tasarrufu sayesinde yılda yaklaşık 876 bin TL daha ucuz. Üstelik teslim süresi kısalıyor. Ancak fark toplam maliyetin yalnızca yaklaşık %4'ü; taşıma maliyeti varsayımında küçük bir değişiklik sonucu tersine çevirebilir. Bu nedenle karar, farklı yakıt ve hacim senaryolarıyla test edilmelidir.

## Sık yapılan hatalar

- **Yalnızca depo kirasına bakmak.** Taşıma ve stok maliyetleri genellikle daha büyüktür.
- **Stok havuzlamasını hesaba katmamak.** Depo sayısını artırmak toplam stoku artırır.
- **Tek bir senaryoyla karar vermek.** Yakıt fiyatı ve hacim değiştikçe sonuç değişir.
- **Hizmet hedefini sonradan düşünmek.** Müşteri teslim gereksinimleri baştan belirlenmelidir.
- **Mevcut ağı sorgulamamak.** Kanal yapısı değiştikçe (indirim marketleri, e-ticaret) ağ da gözden geçirilmelidir.

## Pratikte nasıl uygulanır?

- [ ] Mevcut ağınızın depo, taşıma ve stok maliyetlerini ayrı ayrı hesaplayın.
- [ ] Müşteri gruplarına göre hizmet süresi hedeflerini belirleyin.
- [ ] Alternatif ağ seçeneklerinin toplam maliyetini hesaplayın.
- [ ] Sonuçları yakıt, hacim ve kira senaryolarıyla test edin.
- [ ] Çapraz sevkiyat ve dış kaynaklı lojistik seçeneklerini de karşılaştırmaya dahil edin.

## Daha fazlası

- Chopra, S.; Meindl, P. (2016). *Supply Chain Management: Strategy, Planning, and Operation.* (kaynak doğrulanmadı)
