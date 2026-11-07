---
id: kb-ea-31-1-tms-fleet-telematics
title: "Taşıma yönetimi (TMS), filo ve telematik"
summary: "Sevkiyat planlama, araç ve sürücü yönetimi, teslimat kanıtı ve araç takip (telematik) verisinin yakıt, rölanti ve sürüş davranışı için nasıl kullanıldığını anlatır."
course: ea
category: tedarik-ve-depo-sistemleri
tags: [tms, filo, telematik, teslimat, yakit]
roles: [bayi-sahibi, bayi-yonetici, depo-lojistik-muduru]
level: orta
source_lessons: [EA-31.1]
reading_minutes: 2
key_points:
  - "TMS, siparişleri araçlara ve seferlere atar, taşıma maliyetini ve teslimat durumunu izler."
  - "Telematik, araçtan konum, hız, yakıt ve motor verisi toplar."
  - "Elektronik teslimat kanıtı, teslimatın zamanını, yerini ve alıcıyı kayda geçirir."
  - "Yakıt tüketimi ve rölanti süresi telematik verisiyle izlenebilir."
  - "Sürücü verisi kişisel veri olduğundan kullanım amacı açıkça belirlenmelidir."
glossary_terms: [tms, telematik, teslimat-kaniti]
related: [kb-ea-31-3-route-planning-sales-vs-delivery, kb-ea-30-1-warehouse-operations-kpis, kb-ea-26-5-van-sales-presales]
sources:
  - title: "Global Logistics and Supply Chain Management"
    authors: "Mangan, J.; Lalwani, C."
    year: 2016
    type: book
    verified: false
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Kendi filosuyla dağıtım yapan bir firmada nakliye, depo kadar büyük bir maliyet kalemidir. Bu kart, taşıma yönetim sistemlerinin (TMS) ve araç takip verisinin nasıl kullanılacağını anlatır.

## Temel fikir

**TMS ne yapar?**

- Sevk edilecek siparişleri araçlara ve seferlere atar.
- Araç kapasitesini (ağırlık, hacim, palet) kontrol eder.
- Kendi filo ve nakliye firması maliyetlerini izler.
- Teslimat durumunu ve gecikmeleri raporlar.

**Telematik.** Araçlara takılan cihazlar konum, hız, yakıt seviyesi, motor çalışma süresi ve sert fren gibi verileri gönderir. Bu veriyle:

- Planlanan ve gerçekleşen rota karşılaştırılır,
- 100 km'de yakıt tüketimi ve rölantide geçen süre izlenir,
- Bakım zamanı kilometreye göre planlanır.

**Elektronik teslimat kanıtı.** Sürücü, teslimatta mobil cihazdan alıcı adı, imza veya fotoğraf alır; kayıt zaman ve konumla birlikte merkeze düşer. İtirazlarda kanıt hazırdır.

**Kişisel veri.** Sürücüye bağlanabilen konum ve sürüş verisi kişisel veridir. Hangi amaçla toplandığı, kimlerin göreceği ve ne kadar saklanacağı belirlenmeli ve sürücülere bildirilmelidir.

### TMS'yi değerlendirirken sorulacak sorular

Taşıma yönetim sistemi seçerken veya mevcut sistemi gözden geçirirken aşağıdaki sorular yol gösterir:

- **Kendi filonuz mu, nakliye firması mı?** Kendi aracınız varsa rota, sürücü ve araç maliyeti yönetimi; dış nakliyede ise teklif karşılaştırma, navlun faturası kontrolü ve taşıyıcı performansı öne çıkar.
- **ERP ve depo sistemiyle bağlantı:** Siparişler TMS'ye otomatik gelmeli, araç atanınca depo yüklemeyi bu sıraya göre planlamalı, e-irsaliye araç bilgisini TMS'den almalıdır.
- **Teslimat kanıtı:** Sürücünün mobil cihazla teslim zamanını, konumunu ve alıcı onayını kaydetmesi, müşteri itirazlarını hızla çözmeyi sağlar.
- **Maliyet görünürlüğü:** Rota, araç veya müşteri bazında taşıma maliyeti hesaplanabiliyor mu? Bu bilgi, hizmet maliyeti analizinin temel girdisidir.

**Telematik verisinin kullanımı.** Konum ve hız verisi, rota uyumu ve güvenli sürüş için değerlidir; yakıt ve motor verisi ise bakım planlamasını destekler. Ancak bu veriler çalışanla ilgili kişisel veri niteliği taşıyabileceğinden, hangi amaçla toplandığı çalışanlara açıkça bildirilmeli ve erişim sınırlandırılmalıdır.

**Kademeli başlangıç.** Tüm özellikleri aynı anda açmak yerine, önce araç takibi ve teslimat kanıtıyla başlayıp rota optimizasyonunu sonra eklemek, sahadaki benimsemeyi kolaylaştırır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b7.py` ile yapılmıştır.

Bir filo bir ayda 42.000 km yol yapıyor ve 11.760 litre yakıt tüketiyor: 100 km'de **28,0** litre. Telematik verisi, araçların ayda toplam 180 saat rölantide beklediğini gösteriyor. Saatte 2 litre varsayımıyla bu **360** litre yakıt demek. Bekleme noktalarında motor kapatma kuralı getiriliyor.

## Sık yapılan hatalar

- Telematik verisini toplayıp hiç raporlamamak.
- Sürücüleri bilgilendirmeden takip etmek.
- Teslimat kanıtını kâğıt irsaliyeye bırakmak.
- Nakliye maliyetini müşteri kârlılığına yansıtmamak.
- Telematik verisinin amacını çalışanlara açıklamadan toplamak.
- TMS'yi ERP ve depo sistemine bağlamadan ayrı bir ada olarak işletmek.

## Pratikte nasıl uygulanır?

- [ ] Araç başına aylık km, yakıt ve rölanti raporu kurun.
- [ ] Elektronik teslimat kanıtına geçin.
- [ ] Sürücü verisinin kullanım amacını yazılı belirleyin.
- [ ] Sefer başı maliyeti müşteri ve bölge bazında hesaplayın.

## Daha fazlası

- Mangan ve Lalwani, *Global Logistics and Supply Chain Management* (kitap; doğrulanmadı).
