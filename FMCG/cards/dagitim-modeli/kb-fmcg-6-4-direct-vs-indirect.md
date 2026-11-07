---
id: kb-fmcg-6-4-direct-vs-indirect
title: "Doğrudan mı, dağıtıcı üzerinden mi? Kanal kararının hesabı"
summary: "Bir bölgeye kendi araç ve ekibinizle mi gideceğinizi, yoksa bir dağıtıcıyla mı çalışacağınızı belirleyen temel hesap, sabit maliyetler ile dağıtıcı marjı arasındaki dengedir. Bu kart başabaş hacmini ve kararın maliyet dışındaki boyutlarını anlatır."
course: fmcg
category: dagitim-modeli
tags: [dagitim, maliyet, strateji]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru]
level: orta
source_lessons: [FMCG-6.4]
reading_minutes: 3
key_points:
  - "Doğrudan dağıtımın yüksek sabit, düşük değişken maliyeti vardır; dağıtıcı modeli ise neredeyse tamamen değişkendir."
  - "İki model arasındaki başabaş satış, doğrudan modelin sabit maliyetinin, dağıtıcı marjı ile doğrudan değişken maliyet farkına bölünmesiyle bulunur."
  - "Başabaşın altındaki hacimlerde dağıtıcı, üstündekilerde doğrudan model genellikle daha ucuzdur."
  - "Kontrol, pazar bilgisi, işletme sermayesi ve risk de kararın parçasıdır."
glossary_terms: [dogrudan-dagitim, sabit-maliyet, degisken-maliyet, bayi]
related: [kb-fmcg-6-3-cost-to-serve, kb-fmcg-6-8-rtm-design-case, kb-fmcg-7-1-distributor-pnl, kb-fmcg-7-4-distributor-selection-kpis, kb-fmcg-1-3-channel-actors]
sources:
  - title: "Marketing Channels"
    authors: "Coughlan, A. T.; Anderson, E.; Stern, L. W.; El-Ansary, A. I."
    year: 2006
    type: book
    verified: false
    note: "Kitap; baskı yılı kontrol edilmedi."
  - title: "The Economic Institutions of Capitalism"
    authors: "Williamson, O. E."
    year: 1985
    type: book
    verified: false
    note: "Kitap; künye kontrol edilmedi."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Bir bölgede satışlar büyüdüğünde "Artık kendimiz dağıtsak mı?" sorusu, satışlar küçüldüğünde "Bu bölgeyi bir dağıtıcıya mı bıraksak?" sorusu gelir. Bu kart, kararın maliyet tarafını basit bir başabaş hesabıyla, diğer tarafını da bir kontrol listesiyle ele alır.

## Temel fikir

**İki model.**

- **Doğrudan dağıtım** (*direct distribution*): Depo, araç, sürücü, satış temsilcisi ve tahsilat sizde. Maliyetin büyük kısmı sabittir; satış artarken toplam maliyet yavaş artar.
- **Dağıtıcı modeli:** Dağıtıcı bu işlevleri üstlenir ve karşılığında satış üzerinden bir marj alır. Maliyet neredeyse tamamen değişkendir.

**Başabaş.** Doğrudan modelin sabit maliyeti F, değişken maliyet oranı v, dağıtıcı marjı d ise iki modelin maliyeti, satış S = F / (d − v) olduğunda eşitlenir. Bu hacmin altında dağıtıcı, üstünde doğrudan model daha ucuzdur.

**Maliyet dışındaki etkenler.** Coughlan ve arkadaşları, kanal tasarımında hangi işlevi kimin daha verimli yaptığına bakmayı önerir. Williamson (1985), işlem maliyetleri yaklaşımıyla bir işi içeride yapmak ile piyasadan almak arasındaki seçimi, varlığa özgü yatırımlar, belirsizlik ve fırsatçılık riski üzerinden açıklar. Pratikte bakılacaklar:

- **Kontrol:** Raf, fiyat ve ziyaret kalitesi üzerinde ne kadar söz sahibisiniz?
- **Pazar bilgisi:** Nokta bazında veriye doğrudan ulaşabiliyor musunuz?
- **İşletme sermayesi:** Doğrudan modelde stok ve alacak sizin bilançonuzdadır.
- **Risk:** Tahsilat riski ve çalışan yönetimi sizde mi?
- **Ölçek ve kapsam:** Dağıtıcı başka üreticilerin ürünlerini de taşıyarak maliyeti paylaştırabilir.

**Geçişi planlamak.** Doğrudan modele geçiş ya da dağıtıcıya devretme kararı verildiğinde geçiş süreci ayrıca planlanmalıdır. Doğrudan modele geçerken depo, araç, personel ve sistem yatırımları sonuçlar gelmeden önce yapılır; bu nedenle ilk dönemde kârlılık düşebilir. Dağıtıcıya devrederken ise mevcut müşteri ilişkilerinin, alacakların ve fiyat listelerinin nasıl aktarılacağı netleştirilmelidir. Her iki durumda da geçiş sırasında noktalarda stoksuzluk ve hizmet kesintisi riski yüksektir. Bu nedenle geçişi önce bir bölgede deneyip sonuçları ölçmek, sonra yaygınlaştırmak daha güvenlidir. Dağıtıcıyla mevcut sözleşmenin fesih koşulları da önceden hukuk danışmanıyla kontrol edilmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Maliyetler ve marj varsayımdır; hesaplar `scripts/cards_numbers_fmcg_b3.py` ile yapılmıştır.

Bir bölgede doğrudan dağıtımın yıllık sabit maliyeti 3.000.000 TL, değişken maliyeti satışın %4'ü. Dağıtıcı %10 marjla çalışıyor.

- Başabaş satış: 3.000.000 / (0,10 − 0,04) = **50.000.000 TL**

| Yıllık satış | Doğrudan maliyet | Dağıtıcı maliyeti |
|---|---|---|
| 30.000.000 TL | 4.200.000 TL | 3.000.000 TL |
| 50.000.000 TL | 5.000.000 TL | 5.000.000 TL |
| 80.000.000 TL | 6.200.000 TL | 8.000.000 TL |

30 milyon TL'lik bir bölgede dağıtıcı 1,2 milyon TL daha ucuz. 80 milyon TL'de doğrudan model 1,8 milyon TL tasarruf sağlıyor. Ancak doğrudan modele geçince alacak ve stok bilançonuza gelir; bu sermayenin maliyetini de hesaba katın.

## Sık yapılan hatalar

- **Yalnızca dağıtıcı marjına bakmak.** Dağıtıcının üstlendiği tahsilat, stok ve risk işlevlerinin maliyeti doğrudan modelde size geçer.
- **Geçiş maliyetini unutmak.** Depo kurulumu, ekip alımı ve dağıtıcıyla sözleşme sonu maliyetleri ilk yılı ağırlaştırır.
- **Tek bir model seçmek.** Büyük şehirlerde doğrudan, küçük bölgelerde dağıtıcı modeli birlikte kullanılabilir.

## Pratikte nasıl uygulanır?

- [ ] Her bölge için doğrudan modelin sabit ve değişken maliyetlerini çıkarın.
- [ ] Başabaş satışı hesaplayın ve bölgenin bugünkü ve üç yıl sonraki satışıyla karşılaştırın.
- [ ] Ek işletme sermayesini ve onun maliyetini ekleyin.
- [ ] Kontrol, bilgi ve risk başlıklarını puanlayıp maliyet hesabıyla birlikte değerlendirin.
- [ ] Geçiş kararı verirseniz bir bölgede pilot uygulamayla başlayın.

## Daha fazlası

- Coughlan, A. T.; Anderson, E.; Stern, L. W.; El-Ansary, A. I. (2006). *Marketing Channels.* (kaynak doğrulanmadı)
- Williamson, O. E. (1985). *The Economic Institutions of Capitalism.* (kaynak doğrulanmadı)
