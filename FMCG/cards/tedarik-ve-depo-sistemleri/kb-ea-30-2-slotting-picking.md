---
id: kb-ea-30-2-slotting-picking
title: "Yerleşim (slotting) ve toplama yöntemleri"
summary: "Depoda ürünlerin hangi lokasyona konacağını belirleyen yerleşim mantığını, ABC analizine göre yerleşimi ve tekli, toplu ve bölgesel toplama yöntemlerinin ne zaman kullanıldığını anlatır."
course: ea
category: tedarik-ve-depo-sistemleri
tags: [slotting, toplama, abc-analizi, depo-yerlesimi]
roles: [depo-lojistik-muduru]
level: orta
source_lessons: [EA-30.2]
reading_minutes: 2
key_points:
  - "Yerleşim, hızlı dönen ürünleri toplama noktasına en yakın ve en erişilebilir lokasyona koymaktır."
  - "ABC analizi ürünleri hareket sıklığına göre sınıflar."
  - "Tekli toplamada her sipariş ayrı, toplu toplamada birden fazla sipariş birlikte toplanır."
  - "Bölgesel toplamada her çalışan bir bölgeden sorumludur."
  - "Yerleşim talep değiştikçe düzenli güncellenmelidir."
glossary_terms: [slotting, abc-analizi, toplu-toplama]
related: [kb-ea-30-1-warehouse-operations-kpis, kb-ea-30-3-wms-what-it-does, kb-ea-30-4-barcodes-traceability]
sources:
  - title: "Warehouse Management"
    authors: "Richards, G."
    year: 2021
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

Toplayıcının zamanının büyük kısmı yürümekle geçer. Ürünlerin doğru yere konması ve doğru toplama yönteminin seçilmesi, ek yatırım olmadan verimliliği artırmanın en kolay yoludur.

## Temel fikir

**Yerleşim (slotting).** Hangi ürünün hangi lokasyonda duracağına karar verme işidir. Temel kurallar:

- Hızlı dönen ürünler sevk alanına yakın ve bel hizasındaki raflara.
- Ağır ürünler alt raflara.
- Birlikte sipariş edilen ürünler yan yana.

**ABC analizi.** Ürünler toplama sıklığına göre sınıflanır: A (en sık), B, C. Genellikle az sayıda ürün, toplamaların büyük bölümünü oluşturur.

### Hangi toplama yöntemi ne zaman?

Toplama yöntemi seçimi, depo yerleşimi kadar önemlidir. Yaygın yöntemler ve uygun oldukları durumlar şöyledir:

- **Sipariş bazlı (tekli) toplama:** Bir çalışan bir siparişi baştan sona toplar. Az sayıda büyük sipariş için basit ve hatası az bir yöntemdir; ancak çok sayıda küçük siparişte yürüme mesafesi hızla artar.
- **Toplu toplama:** Birkaç sipariş birlikte toplanır, sonra ayrıştırılır. Bakkal ve küçük market gibi çok sayıda küçük siparişin olduğu dağıtımda yürüme mesafesini belirgin biçimde azaltır; ayrıştırma adımında kontrol gerekir.
- **Bölge toplama:** Her çalışan deponun bir bölgesinden sorumludur; sipariş bölgeden bölgeye geçer. Büyük depolarda ve ürün çeşitliliği yüksek olduğunda etkilidir.
- **Dalga toplama:** Siparişler araç veya sevk saatine göre gruplanarak belirli zaman dilimlerinde toplamaya bırakılır. Dağıtım rotalarıyla uyumlu çalışmayı sağlar.

**Yerleşimin bakımı.** Ürünlerin hareket sıklığı mevsime, promosyona ve yeni ürün girişine göre değişir. Bu nedenle yerleşim bir kez yapılıp bırakılmamalı; hızlı hareket eden ürünler dönemsel olarak gözden geçirilmeli, ağır ürünler alt raflarda ve sevkiyat alanına yakın tutulmalıdır. Birlikte satılan ürünlerin yan yana konması da toplama süresini kısaltır.

### Lokasyon kodu ve toplama rotası

Yerleşimin işe yaraması için her lokasyonun okunaklı ve mantıklı bir kodu olmalıdır; örneğin koridor, raf, kat ve göz sırasıyla. Toplama listesi bu kodlara göre sıralandığında toplayıcı depoda tek yönde ilerler, geri dönüşler ve boşuna yürüme azalır. Depo yönetim sistemi kullanılıyorsa listeyi rota sırasına göre kendisi üretir; kullanılmıyorsa ERP'deki lokasyon alanı ve basit bir sıralama kuralı da belirgin iyileşme sağlar. Yerleşim değiştiğinde lokasyon kayıtlarının aynı gün güncellenmesi gerekir; aksi halde sistemdeki yer ile raftaki ürün birbirini tutmaz ve toplayıcı ürünü aramaya başlar.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b7.py` ile yapılmıştır.

Bir depoda satır başı ortalama toplama süresi 2,0 dakika. ABC analiziyle A ürünleri sevk alanına taşındıktan sonra süre 1,4 dakikaya iniyor: **%30,0** azalma. Günde 3.000 satır toplandığında bu, günde **30,0** işçilik saati demek.

## Sık yapılan hatalar

- Ürünleri geliş sırasına göre rafa koymak.
- Yerleşimi bir kez yapıp yıllarca güncellememek.
- Yeni ürünleri boş bulunan ilk rafa koymak.
- Hızlı hareket eden ürünleri sevkiyat alanından uzak, üst raflara yerleştirmek.
- Benzer ambalajlı ürünleri yan yana koyup karışıklığa zemin hazırlamak.
- Promosyon dönemlerinde değişen hareket hızını yerleşime yansıtmamak.
- Toplama yöntemini sipariş profiline bakmadan, alışkanlıkla seçmek.

## Pratikte nasıl uygulanır?

- [ ] Son üç ayın toplama verisinden ABC analizi yapın.
- [ ] A ürünlerini en erişilebilir lokasyonlara taşıyın.
- [ ] Sipariş profilinize göre toplama yöntemini seçin.
- [ ] Yerleşimi mevsim başlarında gözden geçirin.

## Daha fazlası

- Richards, *Warehouse Management* (kitap; doğrulanmadı).
