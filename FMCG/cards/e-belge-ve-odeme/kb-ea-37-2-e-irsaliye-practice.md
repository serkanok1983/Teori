---
id: kb-ea-37-2-e-irsaliye-practice
title: "E-irsaliye uygulamada"
summary: "E-irsaliyenin sevkiyat sürecindeki yerini, araç ve plaka gibi verilerin doğruluğunu, irsaliye yanıtını ve fatura ile eşleştirmeyi uygulama odaklı anlatır."
course: ea
category: e-belge-ve-odeme
tags: [e-irsaliye, sevkiyat, lojistik, ubl-tr, eslestirme]
roles: [finans-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-37.2]
reading_minutes: 2
key_points:
  - "E-irsaliye, malın sevkiyatı sırasında düzenlenen elektronik sevk belgesidir."
  - "Araç, sürücü ve teslim adresi gibi alanların doğruluğu sahadaki sorunları azaltır."
  - "Alıcı, irsaliye yanıtıyla teslim aldığı miktarı bildirebilir."
  - "İrsaliye ile fatura arasındaki eşleştirme ERP'de izlenmelidir."
  - "Düzenleme zamanı ve zorunluluk kapsamı güncel mevzuatla kontrol edilmelidir."
glossary_terms: [e-irsaliye, irsaliye-yaniti]
related: [kb-ea-37-1-e-document-map, kb-ea-37-2-e-fatura-scenarios, kb-ea-31-1-tms-fleet-telematics, kb-ea-30-3-wms-what-it-does]
sources:
  - title: "e-İrsaliye kılavuzları"
    authors: "GİB"
    year: 2026
    type: web
    url: "https://ebelge.gib.gov.tr/"
    verified: false
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Dağıtımda irsaliye her gün yüzlerce kez kesilir. Elektronik ortamdaki küçük bir veri hatası, aracın yolda bekletilmesine veya müşterinin teslimi kabul etmemesine yol açabilir. Bu kart, e-irsaliyeyi depo ve sevkiyat süreciyle birlikte ele alır.

## Temel fikir

**Süreçteki yeri:** Sipariş → toplama → yükleme → **e-irsaliye** → yolculuk → teslim → fatura.

**Kritik alanlar:**

- Sevk tarihi ve saati
- Araç plakası ve sürücü bilgisi
- Teslim adresi
- Ürün, miktar ve birim

**İrsaliye yanıtı:** Alıcı, teslim aldığı miktarı ve varsa eksik veya fazlalığı elektronik yanıtla bildirebilir. Bu yanıt, fatura öncesinde farkları yakalamak için değerlidir.

**Eşleştirme:** ERP'de her faturanın hangi irsaliyelere dayandığı izlenmelidir; irsaliyesi faturalanmamış sevkiyatlar düzenli raporlanmalıdır.

**Sistem bağlantısı:** Depo sistemi yüklemeyi, taşıma sistemi aracı belirler; e-irsaliye bu iki kaynaktan otomatik beslenmelidir.

### Sahadaki tipik durumlar

E-irsaliye uygulamasında sorunların çoğu, sevkiyatın planlandığı gibi gitmediği durumlarda ortaya çıkar. Bu durumlar için önceden kural belirlemek, sahadaki aracın beklemesini önler:

- **Araç değişikliği:** Yükleme sonrası arıza veya planlama değişikliği nedeniyle araç değişirse, belgedeki araç bilgisinin nasıl güncelleneceği belirlenmelidir.
- **Kısmi teslim:** Müşteri ürünlerin bir kısmını kabul etmezse, irsaliye yanıtı ve iade kaydı nasıl işlenecek? Faturaya teslim edilen miktar mı, sevk edilen miktar mı yansıyacak?
- **Araçtan satış:** Araç stoğundan satış yapılan modelde, depodan araca çıkış ile araçtan müşteriye teslim farklı belge akışları gerektirebilir.
- **Bağlantı sorunu:** Sahada internet bağlantısı olmadığında belgenin nasıl düzenleneceği ve sonradan iletileceği önceden planlanmalıdır.

**Rol dağılımı.** Depo, sevkiyat planlama ve muhasebe birimleri e-irsaliyenin farklı parçalarından sorumludur. Hangi alanı kimin girdiği ve hatayı kimin düzelteceği yazılı değilse, sorunlar birimler arasında el değiştirir.

**İzleme.** Günlük olarak düzenlenen, iletilen, yanıt alınan ve hata alan belge sayıları bir panoda izlenmelidir. Bu basit görünüm, sorunların müşteri şikâyetine dönüşmeden yakalanmasını sağlar.

### Depo ekibiyle uygulama

E-irsaliye süreci, sevkiyat saatlerinde depo ekibinin hızını doğrudan etkiler. Belge oluşturma adımının yükleme planıyla uyumlu çalışması gerekir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b8.py` ile yapılmıştır.

Bir dağıtıcı ayda 900 e-irsaliye düzenliyor; 27'sinde plaka bilgisi yanlış. Hata oranı **%3,0**. Plaka elle yazıldığı için hata oluşuyor. Şirket plakayı taşıma sisteminden otomatik çekince bu hata türü ortadan kalkıyor.

## Sık yapılan hatalar

- Araç ve sürücü bilgisini elle girmek.
- İrsaliye yanıtlarını okumamak.
- İrsaliye–fatura eşleşmesini izlememek.
- Sevkiyat değişince irsaliyeyi güncellemeyi unutmak.
- Araç değişikliği ve kısmi teslim için önceden kural belirlememek.
- Hata düzeltme sorumluluğunu birimler arasında belirsiz bırakmak.
- Günlük belge durumunu izleyen bir pano kurmamak.

## Pratikte nasıl uygulanır?

- [ ] Plaka ve sürücü bilgisini taşıma sisteminden otomatik besleyin.
- [ ] İrsaliye yanıtlarını bir iş kuyruğuna düşürün.
- [ ] Faturalanmamış irsaliye raporunu haftalık inceleyin.
- [ ] Hata ve iptal usullerini mali müşavirinizle yazılı hâle getirin.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın. Kapsam, düzenleme zamanı ve hata düzeltme usullerini mutlaka mali müşavirinizle teyit edin.

## Daha fazlası

- GİB e-Belge portalı, e-İrsaliye kılavuzları (doğrulanmadı).
