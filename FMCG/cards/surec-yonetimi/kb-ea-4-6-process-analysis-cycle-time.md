---
id: kb-ea-4-6-process-analysis-cycle-time
title: "Süreç analizi: Döngü süresi, akış verimliliği ve Little yasası"
summary: "Bir sürecin neden yavaş olduğunu üç basit ölçüyle analiz etmeyi anlatır: döngü süresi, akış verimliliği ve süreçteki iş sayısı ile süre arasındaki bağı kuran Little yasası; vaka başı maliyetle birlikte."
course: ea
category: surec-yonetimi
tags: [surec, verimlilik, kpi, siparis, maliyet]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, depo-lojistik-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-4.6]
reading_minutes: 2
key_points:
  - "Döngü süresi, bir işin süreçte başlangıçtan bitişe geçirdiği toplam süredir."
  - "Akış verimliliği, bu sürenin ne kadarının gerçek iş, ne kadarının bekleme olduğunu gösterir."
  - "Little yasası: süreçteki iş sayısı = günlük çıkış × döngü süresi."
  - "Bekleyen iş yığınını azaltmak, çıkışı değiştirmeden döngü süresini kısaltır."
  - "Vaka başı maliyet, süreç iyileştirmesinin parasal karşılığını gösterir."
glossary_terms: [dongu-suresi, akis-verimliligi, little-yasasi]
related: [kb-ea-4-1-what-is-a-process, kb-ea-4-2-bpm-lifecycle, kb-ea-4-7-process-mining, kb-ea-30-1-warehouse-operations-kpis]
sources:
  - title: "Fundamentals of Business Process Management"
    authors: "Dumas, M.; La Rosa, M.; Mendling, J.; Reijers, H. A."
    year: 2018
    type: book
    verified: false
  - title: "Factory Physics"
    authors: "Hopp, W. J.; Spearman, M. L."
    year: 2008
    type: book
    verified: false
    note: "Little yasası ve kuyruk etkileri; baskı yılı kontrol edilmeli."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

"Siparişler çok geç işleniyor, iki kişi daha alalım" kararı çoğu zaman yanlış teşhise dayanır. Bu kart, bir sürecin yavaşlığını üç ölçüyle ayrıştırmanızı sağlar: **döngü süresi** (*cycle time*), **akış verimliliği** (*flow efficiency*) ve **Little yasası** (*Little's law*). Böylece sorunun kapasitede mi, yoksa bekleyen iş yığınında mı olduğunu görürsünüz.

## Temel fikir

- **Döngü süresi:** Bir vakanın (sipariş, iade, cari açılış) sürece girdiği andan çıktığı ana kadar geçen süre.
- **Dokunma süresi:** Vakaya gerçekten çalışılan süre.
- **Akış verimliliği** = dokunma süresi ÷ döngü süresi. Ofis süreçlerinde bu oran çoğu zaman çok düşüktür; vakalar zamanlarının çoğunu sırada bekleyerek geçirir.
- **Little yasası:** Uzun dönemde dengedeki bir süreçte, süreçteki ortalama iş sayısı (WIP, *work in process*) = ortalama çıkış hızı × ortalama döngü süresi. Bunu ters çevirirseniz: döngü süresi = WIP ÷ çıkış hızı.

Little yasasının pratik sonucu şudur: Çıkış hızını (kapasiteyi) değiştirmeden, süreçte bekleyen iş sayısını azaltırsanız döngü süresi kısalır. Biriken işi eritmek, yeni işi daha hızlı sürece sokmaktan çoğu zaman daha etkilidir.

**Vaka başı maliyet**, sürecin personel maliyetinin işlenen vaka sayısına bölünmesidir. İyileştirmenin parasal karşılığını göstermek için kullanılır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b1.py` ile yapılmıştır.

Bir bayinin sipariş işleme ekibi günde ortalama 80 sipariş tamamlıyor. Bir siparişin girişten sevke hazır olmaya kadar ortalama döngü süresi 2,5 gün.

- Little yasasına göre süreçteki ortalama sipariş sayısı: 80 × 2,5 = **200**.
- Bir siparişe gerçekte harcanan süre 35 dakika. Takvim süresiyle (2,5 × 24 saat) akış verimliliği: 35 ÷ 3.600 = **%0,97**. Yalnızca 8 saatlik iş günleri sayılsa bile 35 ÷ (2,5 × 480) = **%2,9**.

Yani sipariş zamanının %97'den fazlasını bekleyerek geçiriyor. İki kişi eklemek yerine ekip, siparişleri günde iki kez toplu işlemek yerine geldikçe işlemeye ve eksik bilgili siparişleri sahada düzelttirmeye karar veriyor. Süreçteki sipariş sayısı 100'e inerse, aynı günlük 80 çıkışla döngü süresi 100 ÷ 80 = **1,25 gün** olur.

Vaka başı maliyet: 4 kişilik ekip, kişi başı aylık 52.000 TL maliyet, 22 iş günü ve günde 80 sipariş ile (4 × 52.000) ÷ 22 ÷ 80 = **118,18 TL**.

## Sık yapılan hatalar

- Yavaşlığı otomatik olarak kapasite eksikliği saymak.
- Bekleme süresini ölçmeyip yalnızca iş süresini kronometreyle tutmak.
- Ortalama döngü süresine bakıp uzun kuyruğu (çok gecikmiş vakaları) görmemek.
- Little yasasını dengede olmayan, hızla büyüyen bir kuyrukta birebir uygulamak.
- Vaka başı maliyeti hesaplamadan "verimlilik arttı" demek.

## Pratikte nasıl uygulanır?

- [ ] Seçtiğiniz süreç için günlük tamamlanan vaka sayısını ve ortalama döngü süresini sistem kayıtlarından çıkarın.
- [ ] Little yasasıyla süreçte bekleyen vaka sayısını hesaplayın; gerçek sayımla karşılaştırın.
- [ ] Bir hafta boyunca birkaç vakanın dokunma süresini ölçüp akış verimliliğini bulun.
- [ ] Bekleyen işi azaltan kuralları deneyin: toplu işlem yerine sürekli akış, eksik veriyi kaynağında düzeltme.
- [ ] Vaka başı maliyeti değişiklikten önce ve sonra raporlayın.

## Daha fazlası

- Dumas ve diğerleri, *Fundamentals of Business Process Management* (kitap; doğrulanmadı).
- Hopp ve Spearman, *Factory Physics* (kitap; doğrulanmadı).
