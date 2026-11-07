---
id: kb-ea-4-1-what-is-a-process
title: "İş süreci nedir? Departman yerine süreç gözüyle bakmak"
summary: "İş sürecini müşteriden başlayıp müşteride biten uçtan uca bir iş akışı olarak tanımlar; departmanlar arası el değiştirmelerin neden zaman ve hata ürettiğini, yeniden tasarımın neden yazılımdan önce geldiğini anlatır."
course: ea
category: surec-yonetimi
tags: [surec, siparis, verimlilik, organizasyon]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, it-yoneticisi]
level: temel
source_lessons: [EA-4.1]
reading_minutes: 2
key_points:
  - "İş süreci, bir müşteri ya da iç kullanıcı için sonuç üreten ve birden çok birimi kesen faaliyetler zinciridir."
  - "Departman yapısı işi böler; süreç bakışı işi uçtan uca birleştirir."
  - "Gecikmelerin çoğu iş yapılırken değil, iş bir masadan diğerine geçerken oluşur."
  - "Kötü bir süreci otomatikleştirmek, hatayı daha hızlı üretmek demektir."
glossary_terms: [is-sureci, siparisten-tahsilata]
related: [kb-ea-4-2-bpm-lifecycle, kb-ea-4-3-process-maps-bpmn, kb-ea-4-6-process-analysis-cycle-time, kb-ea-20-2-order-to-cash]
sources:
  - title: "Reengineering Work: Don't Automate, Obliterate"
    authors: "Hammer, M."
    year: 1990
    type: article
    verified: false
    note: "Harvard Business Review; DOI yok."
  - title: "Reengineering the Corporation"
    authors: "Hammer, M.; Champy, J."
    year: 1993
    type: book
    verified: false
  - title: "Process Innovation: Reengineering Work through Information Technology"
    authors: "Davenport, T. H."
    year: 1993
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

Bir müşteri "siparişim neden üç günde geldi?" diye sorduğunda satış "depoya ilettik", depo "onay geç geldi", muhasebe "limit kontrolü bekliyordu" der. Her birim kendi işini zamanında yapmıştır ama müşteri yine geç kalmıştır. Bu kart, işi departmanlara göre değil **iş süreci** (*business process*) olarak görmenizi sağlar. Yazılım seçmeden ya da bir aksaklığı çözmeden önce bu bakış açısı gerekir.

## Temel fikir

İş süreci, bir müşteri ya da iç kullanıcı için değer üreten, belirli bir tetikleyiciyle başlayıp belirli bir sonuçla biten faaliyetler zinciridir. Örnekler: siparişten tahsilata, satın almadan ödemeye, iade süreci, yeni müşteri açılışı.

Fonksiyonel (departman) yapıda her birim kendi verimliliğine bakar. Süreç ise birimleri keser. Sorun, iş bir birimden diğerine geçerken çıkar:

- İş bir kuyruğa girer ve beklemeye başlar.
- Bilgi aktarılırken eksilir ya da yanlış yazılır.
- Kimse uçtan uca süreden sorumlu değildir.

Hammer (1990), bu durumda var olan işi otomatikleştirmek yerine gereksiz adımları kaldırmayı savundu. Davenport (1993) da teknolojiyi süreci yeniden tasarlamanın aracı olarak gördü. Bugün bu fikirler daha ölçülü uygulanıyor: Radikal yeniden tasarım yerine, adım adım iyileştirme ve ölçüm. Ancak temel ders aynı: Önce süreci düzeltin, sonra otomatikleştirin.

Her sürecin bir **süreç sahibi** olmalıdır: uçtan uca süreden ve sonuçtan sorumlu, birimler arası yetkisi olan bir yönetici.

### Süreç sahipliği

Süreç gözüyle bakmanın pratik sonucu, her uçtan uca süreç için bir sahip belirlemektir. Süreç sahibi, departmanlar arasındaki devir noktalarındaki sorunları çözmekten ve sürecin göstergelerinden sorumludur.

## Bir örnek

> **Örnek (temsili rakamlar):** Süreler gerçek değildir; hesaplar `scripts/cards_numbers_ea_b1.py` ile yapılmıştır.

Bir bayide büyük bir siparişin yolu: temsilci → satış şefi (iskonto onayı) → muhasebe (limit kontrolü) → satış müdürü (limit aşımı onayı) → sevkiyat planlama → depo → faturalama. Bu, **6 el değiştirme** demek.

- Her el değiştirmede iş ortalama 3 saat bekliyor: 6 × 3 = **18,0 saat** bekleme.
- Bütün adımların gerçek iş süresi (dokunma süresi) toplam 40 dakika. Toplam sürenin yalnızca 40 ÷ (18 × 60 + 40) = **%3,6**'sı iş, gerisi bekleme.

Yeniden tasarım: Limit içindeki ve iskonto politikasına uyan siparişler sistemde otomatik onaylanıyor; limit kontrolü sipariş anında yapılıyor. El değiştirme sayısı 3'e iniyor ve bekleme **9,0 saat**e düşüyor. Burada fark yaratan yazılım değil, onay kuralının değişmesidir; yazılım yalnızca bu kuralı uygular.

## Sık yapılan hatalar

- Süreci departman sınırında bitirmek; "bizim kısmımız tamam" demek.
- Bekleme süresini ölçmeyip yalnızca iş süresine bakmak.
- Mevcut süreci olduğu gibi yeni sisteme taşımak.
- Süreç sahibi atamamak ya da bu rolü yetkisi olmayan birine vermek.

## Pratikte nasıl uygulanır?

- [ ] En çok şikâyet aldığınız bir süreci seçin ve başlangıç–bitiş noktasını tanımlayın.
- [ ] Süreçteki el değiştirmeleri sayın; her birinde ortalama bekleme süresini ölçün.
- [ ] Her onay adımı için "bu kontrol neyi önlüyor, kural ile yapılabilir mi?" diye sorun.
- [ ] Süreç için bir sahip atayın ve uçtan uca süreyi onun hedefine koyun.
- [ ] Yazılım değişikliğinden önce süreç değişikliğini kâğıt üzerinde netleştirin.

## Daha fazlası

- Hammer (1990), "Reengineering Work: Don't Automate, Obliterate", *Harvard Business Review* (DOI yok; doğrulanmadı).
- Hammer ve Champy (1993), *Reengineering the Corporation* (kitap; doğrulanmadı).
- Davenport (1993), *Process Innovation* (kitap; doğrulanmadı).
