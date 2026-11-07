---
id: kb-fmcg-11-9-vmi-cpfr
title: "Tedarikçi yönetimli stok ve işbirlikçi planlama (VMI ve CPFR)"
summary: "Tedarikçi yönetimli stokta müşterinin stok seviyesini tedarikçi yönetir; işbirlikçi planlamada ise iki taraf ortak bir tahmin ve yenileme planı üzerinde anlaşır. Bu kart iki modeli, gereken veri ve güveni, faydaların nasıl hesaplanacağını ve sık karşılaşılan sorunları anlatır."
course: fmcg
category: tedarik-zinciri-ve-stok
tags: [tedarik-zinciri, kilit-musteri, planlama]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, depo-lojistik-muduru]
level: ileri
source_lessons: [FMCG-11.9]
reading_minutes: 3
key_points:
  - "Tedarikçi yönetimli stokta tedarikçi, müşterinin satış ve stok verisine bakarak siparişleri kendisi oluşturur."
  - "İşbirlikçi planlama, ortak bir tahmin ve yenileme planı ile sapmaların birlikte yönetilmesine dayanır."
  - "Her iki model de kamçı etkisini azaltmayı, stoku düşürmeyi ve raf bulunurluğunu artırmayı hedefler."
  - "Başarı için düzenli veri paylaşımı, açık hizmet hedefleri ve sorumlulukları tanımlayan bir sözleşme gerekir."
  - "Faydalar, stok günü ve stoksuzluk oranındaki değişimle ölçülmeli ve taraflar arasında paylaşılmalıdır."
glossary_terms: [tedarikci-yonetimli-stok, isbirlikci-planlama, kamci-etkisi, stok-gun-sayisi, stoksuzluk, ortak-is-plani]
related: [kb-fmcg-11-5-bullwhip-effect, kb-fmcg-10-7-joint-business-planning, kb-fmcg-11-2-demand-forecasting, kb-fmcg-9-4-osa-out-of-stock, kb-fmcg-10-1-key-account-management]
sources:
  - title: "ECR Community"
    authors: "ECR Community"
    year: 2026
    type: web
    url: "https://www.ecr-community.org/"
    verified: true
    checked_on: 2026-10-28
    note: "URL HTTP 200 ile açıldı, başlık/kurum eşleşti (2026-10-28)."
  - title: "Information Distortion in a Supply Chain: The Bullwhip Effect"
    authors: "Lee, H. L.; Padmanabhan, V.; Whang, S."
    year: 1997
    type: article
    doi: "10.1287/mnsc.43.4.546"
    url: "https://doi.org/10.1287/mnsc.43.4.546"
    verified: true
    checked_on: 2026-10-28
    note: "Management Science 43(4), 546–558."
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

Zincir deposu siparişlerini kendi verdiğinde, üretici siparişin ne zaman ve ne kadar geleceğini çoğu zaman önceden bilmez. Sonuç, kamçı etkisi, fazla stok ve stoksuzluğun bir arada görülmesidir. Tedarikçi yönetimli stok (*vendor-managed inventory*, VMI) ve işbirlikçi planlama (*collaborative planning, forecasting and replenishment*, CPFR), bu kopukluğu gidermek için geliştirilmiş iki modeldir. Bu kart, hangisinin ne zaman uygun olduğunu ve faydasını nasıl hesaplayacağınızı anlatır.

## Temel fikir

**Tedarikçi yönetimli stok.** Müşteri, depo ya da mağaza düzeyindeki satış ve stok verisini tedarikçiyle düzenli olarak paylaşır. Tedarikçi, üzerinde anlaşılan stok aralığı ve hizmet hedefine göre yenileme siparişlerini kendisi oluşturur. Müşteri sipariş işinden kurtulur; tedarikçi ise talebi daha erken görür ve üretimini daha düzgün planlar.

**İşbirlikçi planlama.** Bu modelde taraflar bir adım daha ileri gider. Ortak bir iş planı üzerinde anlaşır, promosyon ve lansman takvimini paylaşır, ortak bir satış tahmini oluşturur ve bu tahminden sipariş planı türetir. Tahmin ile gerçekleşme arasındaki sapmalar belirlenmiş eşikleri aşınca iki taraf birlikte çözüm arar. ECR gibi sektör girişimleri bu süreçleri ve iyi uygulama örneklerini yayımlamaktadır.

**Neden işe yarar?** Lee, Padmanabhan ve Whang'ın kamçı etkisi çalışması, talep bilgisinin paylaşılmasını ve sipariş kararlarının koordinasyonunu dalgalanmayı azaltmanın temel yolları arasında sayar. Tedarikçi yönetimli stok ve işbirlikçi planlama bu önerilerin uygulamadaki karşılıklarıdır.

**Ön koşullar.**

- Düzenli ve doğru veri paylaşımı (satış, stok, açık siparişler)
- Ortak hizmet hedefi ve stok aralığı tanımı
- Sorumlulukları, sapma eşiklerini ve fazla stok durumunu düzenleyen bir sözleşme
- Her iki tarafta da süreci sahiplenen kişiler
- Güven: Tarafların veriyi pazarlıkta birbirine karşı kullanmaması

**Sınırlar.** Bu modeller, verisi olmayan ya da çok sayıda küçük noktadan oluşan geleneksel kanalda uygulanması zordur. En çok, merkezi depoyla çalışan büyük zincirlerde ve dağıtıcı depolarında anlamlıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Satış, stok günleri, stoksuzluk oranları ve kayıp satış payı varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b7.py` ile yapılmıştır.

Bir üreticinin bir zincire yıllık satışı **50.000.000 TL**. Tedarikçi yönetimli stoka geçmeden önce zincir deposunda stok **30** gün, mağazalarda stoksuzluk oranı **%6**.

Bir yıllık uygulamadan sonra:

- Stok **20** güne iniyor; satış bazlı yaklaşık hesapla **1.369.863 TL** sermaye serbest kalıyor. Bu fayda öncelikle zincirin.
- Stoksuzluk **%3**'e iniyor. Stoksuzluk anında kaybedilen satışın yarısının başka bir zamana ya da ürüne kaymadan tamamen kaybolduğu varsayılırsa, kurtarılan satış yılda **750.000 TL**. Bu fayda her iki tarafın.

Bu rakamlar, modelin her iki tarafa da somut fayda sağladığını gösteriyor. Ortak iş planında bu faydaların ölçülmesi ve paylaşılması (örneğin ek raf alanı ya da promosyon katkısı olarak) karşılıklı güveni güçlendirir.

## Sık yapılan hatalar

- **Veri paylaşımını tek seferlik bir proje olarak görmek.** Veri düzenli ve zamanında gelmezse model çöker.
- **Hizmet hedefini tanımlamamak.** Taraflar başarıyı farklı ölçer.
- **Tedarikçi yönetimli stoku stok yükleme aracı olarak kullanmak.** Bu, güveni hızla yok eder.
- **Promosyonları ortak plana dahil etmemek.** Plan dışı promosyonlar tahmini bozar.
- **Faydaları ölçmemek.** Ölçülmeyen fayda, sonraki pazarlıkta değer görmez.

## Pratikte nasıl uygulanır?

- [ ] Merkezi depoyla çalışan ve veri paylaşmaya istekli bir müşteriyle pilot başlatın.
- [ ] Stok aralığı, hizmet hedefi ve sapma eşiklerini yazılı olarak tanımlayın.
- [ ] Günlük ya da haftalık veri paylaşımını otomatikleştirin.
- [ ] Promosyon ve lansman takvimini ortak planlama sürecine ekleyin.
- [ ] Stok günü, stoksuzluk ve tahmin hatasını başlangıçta ve her çeyrekte ölçün.
- [ ] Sonuçları ortak iş planı toplantılarında birlikte değerlendirin.

## Daha fazlası

- ECR Community (2026). *ECR Community.* https://www.ecr-community.org/
- Lee, H. L.; Padmanabhan, V.; Whang, S. (1997). *Information Distortion in a Supply Chain: The Bullwhip Effect.* Management Science 43(4), 546–558. https://doi.org/10.1287/mnsc.43.4.546
- Chopra, S.; Meindl, P. (2016). *Supply Chain Management: Strategy, Planning, and Operation.* (kaynak doğrulanmadı)
