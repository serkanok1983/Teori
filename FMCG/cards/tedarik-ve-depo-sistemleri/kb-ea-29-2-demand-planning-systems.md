---
id: kb-ea-29-2-demand-planning-systems
title: "Talep planlama sistemleri: İstatistiksel tahmin, mutabakat ve tahmin katma değeri"
summary: "Talep planlama yazılımlarının istatistiksel tahmin, satış ekibi girdisi ve uzlaşma sürecini nasıl birleştirdiğini; tahmin doğruluğunu ve her adımın katma değerini (FVA) ölçmeyi anlatır."
course: ea
category: tedarik-ve-depo-sistemleri
tags: [talep-planlama, tahmin, mape, fva, s-op]
roles: [satis-direktoru, satis-muduru, bolge-muduru, satis-sefi, depo-lojistik-muduru]
level: orta
source_lessons: [EA-29.2]
reading_minutes: 2
key_points:
  - "Talep planlama, istatistiksel tahmin ile pazar bilgisini birleştiren düzenli bir süreçtir."
  - "Tahmin doğruluğu genellikle ortalama mutlak yüzde hata (MAPE) gibi ölçülerle izlenir."
  - "Tahmin katma değeri (FVA), her adımın hatayı basit bir yönteme göre azaltıp azaltmadığını ölçer."
  - "Satış ekibinin müdahalesi her zaman tahmini iyileştirmez; ölçülmelidir."
  - "Talep bilgisinin paylaşılması tedarik zincirindeki dalgalanmayı azaltır."
glossary_terms: [talep-planlama, mape, tahmin-katma-degeri]
related: [kb-ea-26-6-dms-secondary-sales, kb-ea-29-3-drp-inventory-planning, kb-ea-39-5-ml-forecast-recommendation, kb-ea-27-2-tpm-promotion-settlement]
sources:
  - title: "Information Distortion in a Supply Chain: The Bullwhip Effect"
    authors: "Lee, H.; Padmanabhan, V.; Whang, S."
    year: 1997
    type: article
    doi: "10.1287/mnsc.43.4.546"
    url: "https://doi.org/10.1287/mnsc.43.4.546"
    verified: true
    checked_on: 2026-10-28
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Üretim, satın alma ve depo kararları talep tahminine dayanır. Tahmin Excel'de ve kişilere bağlı yapıldığında hem hata büyür hem de kimse hatanın nereden geldiğini bilemez. Bu kart, talep planlama sistemlerinin temel mantığını anlatır.

## Temel fikir

**Süreç adımları:**

1. **İstatistiksel tahmin:** Geçmiş satış verisinden, mevsimsellik ve trend dikkate alınarak sistemin ürettiği tahmin.
2. **Pazar girdisi:** Satış ve pazarlama ekiplerinin kampanya, yeni müşteri, liste değişikliği gibi bilgileri eklemesi.
3. **Uzlaşma (konsensüs):** Satış, pazarlama, tedarik ve finansın tek bir rakamda anlaşması. Çoğu şirkette bu, satış ve operasyon planlama (S&OP) toplantısında yapılır.

**Doğruluğu ölçmek.** Yaygın ölçü **MAPE**'dir: tahmin ile gerçekleşen arasındaki farkın gerçekleşene oranının ortalaması. Düşük olması iyidir.

**Tahmin katma değeri (FVA).** Her adımın hatası, en basit yöntemle (ör. "geçen ayın satışı kadar") karşılaştırılır. Bir adım hatayı düşürüyorsa değer katar; artırıyorsa o adım sorgulanmalıdır.

**Veri paylaşımı.** Lee, Padmanabhan ve Whang (1997), tedarik zincirinde her halkanın yalnızca bir sonraki halkanın siparişine bakmasının dalgalanmayı büyüttüğünü gösterir. Distribütörün ikincil satış verisinin talep planlamaya girmesi bu nedenle önemlidir.

### Talep planlama sürecini kurmak

Talep planlama bir yazılım değil, düzenli tekrarlanan bir yönetim sürecidir. Sistem bu süreci destekler; ancak sürecin kendisi tanımlanmadan alınan araçlar genellikle beklenen faydayı sağlamaz.

- **Planlama seviyesi:** Tahmin hangi düzeyde yapılacak: ürün ve depo mu, marka ve bölge mi? Çok ayrıntılı seviye gürültülü, çok toplu seviye ise uygulanamaz sonuç verir. Genellikle toplu seviyede yapılan tahmin, oranlarla ayrıntıya dağıtılır.
- **Planlama ufku ve donmuş bölge:** Yakın dönemde üretim ve tedarik kararları alınmış olduğundan tahmin değişiklikleri sınırlı etkiye sahiptir. Hangi dönemin değiştirilemeyeceği önceden belirlenmelidir.
- **Talep sinyalleri:** Satış verisinin yanında promosyon takvimi, fiyat değişiklikleri, yeni ürün girişleri ve yeni nokta açılışları sisteme girdi olarak verilmelidir. Bu bilgiler satış ve pazarlama ekiplerinden düzenli olarak toplanmalıdır.
- **Stoksuzluk düzeltmesi:** Stok olmadığı için satılamayan dönemler, gerçek talebi düşük gösterir. Bu dönemler düzeltilmeden yapılan tahminler, stoksuzluğu kendi kendini besleyen bir döngüye çevirir.

**Rollerin ayrılması.** İstatistiksel tahmini hazırlayan planlama ekibi ile ticari bilgiyi ekleyen satış ekibinin katkıları ayrı ayrı kaydedilmelidir. Böylece tahmin katma değeri analiziyle hangi müdahalenin doğruluğu artırdığı, hangisinin bozduğu görülebilir. Tahmin hatası kaçınılmazdır; önemli olan hatayı ölçmek ve güvenlik stoğunu buna göre planlamaktır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b6.py` ile yapılmıştır.

Bir ürün grubunda basit yöntemin MAPE'si %30, istatistiksel tahminin %22, uzlaşılmış tahminin %25. İstatistiksel tahminin FVA'sı **+8** puan; değer katıyor. Uzlaşma adımının FVA'sı **−3** puan; satış ekibinin eklemeleri hatayı artırıyor. Şirket, ekip girdilerini yalnızca belgelenmiş kampanya ve liste değişiklikleriyle sınırlıyor.

## Sık yapılan hatalar

- Tahmini hedefle karıştırmak.
- Tahmin doğruluğunu hiç ölçmemek.
- Her manuel müdahaleyi iyileştirme saymak.
- Talep planlamaya distribütör verisini almamak.

## Pratikte nasıl uygulanır?

- [ ] Tahmin seviyesini (ürün, kanal, ay) belirleyin.
- [ ] Her adımın tahminini ayrı kaydedin.
- [ ] MAPE ve FVA'yı aylık raporlayın.
- [ ] Değer katmayan adımları sadeleştirin.

## Daha fazlası

- Lee, Padmanabhan ve Whang (1997), *Management Science*. https://doi.org/10.1287/mnsc.43.4.546
