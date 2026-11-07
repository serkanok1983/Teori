---
id: kb-fmcg-7-5-distributor-development
title: "Dağıtıcı geliştirme: Ortak bir iş planıyla büyümek"
summary: "Dağıtıcıyı değiştirmek pahalı ve risklidir; çoğu zaman mevcut dağıtıcıyı geliştirmek daha iyi sonuç verir. Bu kart ortak bir iş planı kurmayı, kapsama ve verimlilik hedefleri koymayı ve desteği sonuca bağlamayı anlatır."
course: fmcg
category: bayi-yonetimi
tags: [dagitim, strateji, saha-satis]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, satis-muduru, bolge-muduru, satis-sefi]
level: orta
source_lessons: [FMCG-7.5]
reading_minutes: 3
key_points:
  - "Dağıtıcı geliştirme, üretici ile dağıtıcının ortak hedefler, ortak veri ve düzenli gözden geçirmelerle çalışmasıdır."
  - "Ortak iş planı satış hedefinin yanında kapsama, ziyaret kalitesi, stok ve tahsilat hedeflerini de içermelidir."
  - "Üretici desteği, dağıtıcının yatırımını ve ek maliyetini karşılayacak, ama sonuca bağlı biçimde kurgulanmalıdır."
  - "Planın dağıtıcı için de kârlı olması gerekir; aksi hâlde uygulanmaz."
glossary_terms: [bayi, kanal-catismasi, sayisal-dagitim]
related: [kb-fmcg-7-4-distributor-selection-kpis, kb-fmcg-7-1-distributor-pnl, kb-fmcg-7-2-distributor-roi, kb-fmcg-10-7-joint-business-planning, kb-fmcg-12-7-case-distributor-turnaround]
sources:
  - title: "Marketing Channels"
    authors: "Coughlan, A. T.; Anderson, E.; Stern, L. W.; El-Ansary, A. I."
    year: 2006
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

Dağıtıcıyla ilişki çoğu zaman aylık hedef baskısına dönüşür: Üretici daha fazla satış ister, dağıtıcı daha fazla destek. Bu kart, ilişkiyi ortak bir iş planına dönüştürmenizi ve büyümeyi iki taraf için de kârlı kılmanızı sağlar.

## Temel fikir

**Ortak iş planı.** Yılda bir hazırlanan ve üç ayda bir gözden geçirilen bir plandır. Şunları içerir:

- **Satış hedefi:** Kategori ve ürün bazında.
- **Kapsama hedefi:** Aktif nokta sayısı ve hedef nokta tiplerinde sayısal dağıtım.
- **Ziyaret kalitesi:** Ziyaret başına kalem sayısı, rafta bulunurluk, mükemmel mağaza puanı.
- **Operasyon:** Sipariş karşılama oranı, stok günü, teslimat süresi.
- **Finans:** Alacak tahsil süresi, gecikmiş alacak oranı.
- **Kaynaklar:** Dağıtıcının ekleyeceği temsilci, araç ya da sistem; üreticinin vereceği destek.

**Kanal ilişkisi.** Coughlan ve arkadaşları, kanal üyeleri arasında çatışmanın kaçınılmaz olduğunu ve iş birliği mekanizmalarıyla yönetilebileceğini anlatır. Ortak hedefler, paylaşılan veri ve düzenli toplantılar bu mekanizmaların başında gelir.

**Destek ve sonuç.** Üreticinin desteği (kapsama primi, temsilci desteği, sistem yatırımı) dağıtıcının ek maliyetini karşılamalı, ama sonuca bağlanmalıdır. Koşulsuz destek zamanla hak hâline gelir.

**Dağıtıcının kârı.** Plan, dağıtıcının kâr-zarar tablosunda da anlamlı olmalıdır. Ek nokta ve ziyaret maliyetini karşılamayan bir büyüme planı kâğıt üzerinde kalır.

**Geliştirme alanlarını belirlemek.** Ortak iş planındaki geliştirme hedefleri, dağıtıcının performans göstergelerinden çıkarılmalıdır. Sayısal dağıtım düşükse kapsama ve yeni nokta açma; sipariş başına satır sayısı düşükse ürün çeşidi ve satış becerisi; alacak gün sayısı yüksekse kredi ve tahsilat; stoksuzluk sıksa sipariş ve depo yönetimi öne çıkar. Her alan için ölçülebilir bir hedef, bir sorumlu ve üreticinin sağlayacağı destek (eğitim, sistem, saha ekibi, prim) yazılmalıdır. Üç aylık gözden geçirmelerde hem dağıtıcının hem üreticinin taahhütlerini yerine getirip getirmediği konuşulmalıdır; tek taraflı bir değerlendirme ilişkiye zarar verir.

## Bir örnek

> **Örnek (temsili rakamlar):** Nokta sayıları, sipariş tutarı ve marj varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b4.py` ile yapılmıştır.

Dağıtıcı bugün 1.800 aktif noktaya hizmet veriyor. Ortak planda hedef bir yılda 2.200 nokta. Yeni noktaların ortalama aylık sipariş tutarı 1.500 TL.

- Ek yıllık satış: 400 × 1.500 × 12 = **7.200.000 TL**
- Dağıtıcının ek brüt marjı (%9): **648.000 TL**

Dağıtıcı bu noktalar için bir temsilci ve bir araç eklemek zorundaysa ve bunların yıllık maliyeti 648.000 TL'ye yakınsa, büyüme dağıtıcıya kâr bırakmaz. Üretici ilk yıl için bu noktalara özel bir kapsama primi önerir. Prim, ancak yeni noktaların en az üç ay düzenli sipariş vermesi şartıyla ödenecektir.

## Sık yapılan hatalar

- **Yalnızca satış hedefi koymak.** Satış, kapsama ve verimlilik olmadan sürdürülemez.
- **Dağıtıcının maliyetini hesaba katmamak.** Plan dağıtıcı için kârsızsa uygulanmaz.
- **Koşulsuz destek.** Sonuca bağlanmayan destek davranış değiştirmez.
- **Gözden geçirmeyi atlamak.** Yıllık plan, üç ayda bir bakılmazsa unutulur.

## Pratikte nasıl uygulanır?

- [ ] Her ana dağıtıcıyla yıllık ortak iş planı hazırlayın.
- [ ] Hedefleri satış, kapsama, kalite, operasyon ve finans başlıklarında belirleyin.
- [ ] Her hedefin dağıtıcıya maliyetini ve gelirini birlikte hesaplayın.
- [ ] Desteği ölçülebilir sonuçlara bağlayın ve ödeme koşullarını yazın.
- [ ] Üç ayda bir ortak toplantıda verileri birlikte gözden geçirin.

## Daha fazlası

- Coughlan, A. T.; Anderson, E.; Stern, L. W.; El-Ansary, A. I. (2006). *Marketing Channels.* (kaynak doğrulanmadı)
