---
id: kb-fmcg-11-4-safety-stock
title: "Güvenlik stoku: Belirsizliğe karşı ne kadar stok tutmalı?"
summary: "Güvenlik stoku, talep ve tedarik süresindeki belirsizliğe karşı tutulan ek stoktur. Bu kart güvenlik stokunun hesabını, hizmet seviyesi ile stok arasındaki ilişkiyi, tedarik süresinin etkisini ve ürün gruplarına göre farklı hedefler koymayı anlatır."
course: fmcg
category: tedarik-zinciri-ve-stok
tags: [tedarik-zinciri, stok, planlama]
roles: [bayi-sahibi, bayi-yonetici, depo-lojistik-muduru]
level: orta
source_lessons: [FMCG-11.4]
reading_minutes: 3
key_points:
  - "Güvenlik stoku = hizmet katsayısı × tedarik süresi boyunca talebin standart sapması."
  - "Hizmet seviyesi yükseldikçe gereken güvenlik stoku hızla artar; %99'dan %99,9'a çıkmak çok pahalıdır."
  - "Tedarik süresini kısaltmak, güvenlik stokunu karekökü oranında azaltır."
  - "Ürünler satış hızına ve önemine göre gruplanmalı, her grup için ayrı hizmet seviyesi hedefi konmalıdır."
  - "Tahmin hatası ölçülüyorsa, güvenlik stoku hesabında talebin değil tahmin hatasının dağılımı kullanılmalıdır."
glossary_terms: [guvenlik-stoku, yeniden-siparis-noktasi, tahmin-hatasi, siparis-karsilama-orani, raf-bulunurlugu]
related: [kb-fmcg-11-3-eoq-reorder-point, kb-fmcg-11-2-demand-forecasting, kb-fmcg-9-4-osa-out-of-stock, kb-fmcg-11-1-supply-chain-basics, kb-fmcg-11-7-warehouse-transport-network]
sources:
  - title: "Inventory and Production Management in Supply Chains"
    authors: "Silver, E. A.; Pyke, D. F.; Thomas, D. J."
    year: 2017
    type: book
    doi: "10.1201/9781315374406"
    verified: true
    checked_on: 2026-10-28
    note: "DOI Crossref kaydında başlık ve yazar eşleşti; baskı yılı karttakinden farklı olabilir."
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

Talep her gün aynı değildir, tedarik de her zaman zamanında gelmez. Güvenlik stoku (*safety stock*) olmadan, talebin beklenenden yüksek olduğu her dönemde stoksuzluk yaşanır. Çok fazla güvenlik stoku ise sermaye ve depo alanı bağlar. Bu kart, ne kadar güvenlik stoku tutacağınızı hesaplamanızı ve bu kararı hizmet hedefine bağlamanızı sağlar.

## Temel fikir

**Temel formül.** Talebin normal dağıldığı ve tedarik süresinin sabit olduğu varsayımıyla:

- Tedarik süresi boyunca talebin standart sapması = günlük talebin standart sapması × √(tedarik süresi)
- Güvenlik stoku = z × tedarik süresi boyunca standart sapma

Burada z, istenen hizmet seviyesine karşılık gelen katsayıdır. Silver, Pyke ve Thomas gibi kaynaklarda bu formülün farklı hizmet tanımları ve tedarik süresi değişkenliği için uyarlamaları anlatılır.

**Hizmet seviyesi tanımı.** Burada kullanılan hizmet seviyesi, bir tedarik döngüsünde stoksuzluk yaşanmama olasılığıdır (*cycle service level*). Sipariş karşılama oranı gibi diğer tanımlar farklı hesaplar gerektirir. Hangi tanımı kullandığınızı açıkça belirtin.

**Azalan getiri.** Hizmet seviyesi yükseldikçe z katsayısı hızla artar. %95'ten %99'a çıkmak güvenlik stokunu yaklaşık %41 artırır; %99,9 için ise çok daha fazlası gerekir.

**Tedarik süresinin etkisi.** Güvenlik stoku, tedarik süresinin karekökü ile orantılıdır. Tedarik süresini iki katına çıkarmak güvenlik stokunu yaklaşık %41 artırır. Tersine, tedarik süresini kısaltmak stoku azaltmanın etkili yollarından biridir.

**Tahmin hatasıyla hesap.** Talep tahmini yapılıyorsa, belirsizlik talebin kendisinden değil tahmin hatasından gelir. Bu durumda formülde talebin standart sapması yerine tahmin hatasının standart sapması kullanılmalıdır. Daha iyi tahmin, doğrudan daha az güvenlik stoku demektir.

**Ürün grupları.** Bütün ürünlere aynı hizmet seviyesini uygulamak pahalıdır. Hızlı dönen ve stratejik ürünler için yüksek, yavaş dönen ürünler için daha düşük hedefler koymak, toplam stoku azaltırken ana ürünlerde bulunurluğu korur.

## Bir örnek

> **Örnek (temsili rakamlar):** Günlük talebin standart sapması ve tedarik süresi varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b6.py` ile yapılmıştır.

Bir ürünün günlük talebinin standart sapması **12** koli, tedarik süresi **5** gün. Tedarik süresi boyunca standart sapma: 12 × √5 ≈ **26,8** koli.

| Hizmet seviyesi | z | Güvenlik stoku (koli) |
|---|---|---|
| %90 | 1,282 | 34,4 |
| %95 | 1,645 | 44,1 |
| %98 | 2,054 | 55,1 |
| %99 | 2,326 | 62,4 |
| %99,9 | 3,090 | 82,9 |

%95'ten %99,9'a çıkmak güvenlik stokunu neredeyse iki katına çıkarıyor. Tedarik süresi 5 günden 10 güne uzarsa, %95 hizmet için güvenlik stoku **44,1**'den **62,4** koliye çıkıyor; bu, %99 hizmet seviyesinin 5 günlük tedarik süresiyle gerektirdiği stokla aynı. Yani tedarik süresini kısa tutmak, aynı stokla daha yüksek hizmet sağlar.

## Sık yapılan hatalar

- **Güvenlik stokunu "iki haftalık satış" gibi sabit kurallarla belirlemek.** Talep dalgalanması ve tedarik süresi ürüne göre çok farklıdır.
- **Bütün ürünler için %99 hedeflemek.** Yavaş dönen ürünlerde bu, büyük ve gereksiz stok demektir.
- **Tedarik süresinin değişkenliğini yok saymak.** Tedarikçi gecikmeleri ek güvenlik stoku gerektirir.
- **Promosyon dönemlerini aynı hesapla yönetmek.** Promosyonlar ayrıca planlanmalıdır.
- **Parametreleri güncellememek.** Talep yapısı değiştikçe güvenlik stoku da değişmelidir.

## Pratikte nasıl uygulanır?

- [ ] Ürünleri satış hızına ve önemine göre üç-dört gruba ayırın.
- [ ] Her grup için hizmet seviyesi hedefi belirleyin.
- [ ] Her ürün için tahmin hatasının ya da talebin standart sapmasını ölçün.
- [ ] Güvenlik stokunu formülle hesaplayın ve yeniden sipariş noktasına ekleyin.
- [ ] Tedarik süresini kısaltma fırsatlarını (sipariş sıklığı, tedarikçiyle iş birliği) araştırın.
- [ ] Her üç ayda bir gerçekleşen hizmet seviyesini hedefle karşılaştırın.

## Daha fazlası

- Silver, E. A.; Pyke, D. F.; Thomas, D. J. (2017). *Inventory and Production Management in Supply Chains.*
- Chopra, S.; Meindl, P. (2016). *Supply Chain Management: Strategy, Planning, and Operation.* (kaynak doğrulanmadı)
