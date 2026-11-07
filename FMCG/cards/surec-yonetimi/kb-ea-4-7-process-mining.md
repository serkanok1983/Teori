---
id: kb-ea-4-7-process-mining
title: "Süreç madenciliği: ERP kayıtlarından gerçek süreci çıkarmak"
summary: "ERP ve saha uygulamasının tuttuğu olay kayıtlarından sürecin gerçekte nasıl işlediğini, hangi varyantların oluştuğunu ve nerede zaman kaybedildiğini bulmayı küçük bir SQL örneğiyle anlatır."
course: ea
category: surec-yonetimi
tags: [surec, surec-madenciligi, erp, siparis, raporlama, sql]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, it-yoneticisi]
level: ileri
source_lessons: [EA-4.7, EA-4.8]
reading_minutes: 3
key_points:
  - "Süreç madenciliği, sistemlerin tuttuğu olay kayıtlarından sürecin gerçek akışını çıkarır."
  - "Bir olay kaydı için üç alan yeterlidir: vaka numarası, faaliyet adı ve zaman damgası."
  - "Aynı süreç gerçekte birçok farklı yoldan (varyant) yürür; en sık varyant ile istisnalar ayrı incelenir."
  - "Uygunluk kontrolü, gerçek akışı olması gereken süreçle karşılaştırır ve atlanan kontrolleri bulur."
  - "Sonuç, veri kalitesine bağlıdır; eksik ya da yanlış zaman damgası yanlış süreç gösterir."
glossary_terms: [surec-madenciligi, olay-gunlugu, siparisten-tahsilata]
related: [kb-ea-4-2-bpm-lifecycle, kb-ea-4-6-process-analysis-cycle-time, kb-ea-20-2-order-to-cash, kb-ea-6-4-internal-controls-sod, kb-ea-8-2-data-quality-field]
sources:
  - title: "Workflow mining: discovering process models from event logs"
    authors: "van der Aalst, W.; Weijters, T.; Maruster, L."
    year: 2004
    type: article
    doi: "10.1109/TKDE.2004.47"
    url: "https://doi.org/10.1109/TKDE.2004.47"
    verified: true
    checked_on: 2026-10-28
  - title: "Process Mining (processmining.org)"
    authors: "IEEE Task Force on Process Mining / van der Aalst, W."
    year: 2026
    type: web
    url: "https://www.processmining.org/"
    verified: true
    checked_on: 2026-10-28
  - title: "Process Mining: Data Science in Action"
    authors: "van der Aalst, W."
    year: 2016
    type: book
    verified: false
    note: "2. baskı."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Süreç haritası, sürecin nasıl yürümesi gerektiğini gösterir. ERP'deki kayıtlar ise nasıl yürüdüğünü. **Süreç madenciliği** (*process mining*), bu kayıtlardan gerçek akışı otomatik çıkarır: Hangi siparişler onaysız sevk edilmiş, hangileri iki kez faturalanmış, nerede günlerce beklenmiş? Bu kart, yöneticinin bu yöntemden ne isteyeceğini ve küçük bir veri setiyle nasıl başlanacağını anlatır.

## Temel fikir

Her işlem sistemi, kaydı kimin ne zaman oluşturduğunu tutar. Bu kayıtlar bir araya getirilince **olay günlüğü** (*event log*) olur. Her satırda üç zorunlu alan bulunur:

- **Vaka:** Sürecin izlediği nesne (sipariş numarası).
- **Faaliyet:** Ne oldu (sipariş girildi, onaylandı, sevk edildi, faturalandı).
- **Zaman:** Ne zaman oldu.

Van der Aalst, Weijters ve Maruster (2004), bu tür kayıtlardan süreç modelinin otomatik çıkarılabileceğini gösterdi. Bugün üç kullanım öne çıkar:

1. **Keşif:** Olay günlüğünden süreç haritasını çıkarmak; sık izlenen yolları ve istisnaları görmek.
2. **Uygunluk kontrolü:** Gerçek akışı olması gereken modelle karşılaştırmak. Örneğin "kredi limiti aşan sipariş onaysız sevk edilmiş mi?"
3. **Zenginleştirme:** Haritaya süre, maliyet ya da kişi bilgisini eklemek; darboğazları bulmak.

ERP verisinde bir zorluk vardır: Bir sipariş birden çok sevkiyata, bir fatura birden çok siparişe bağlanabilir. Tek vaka numarasına indirgemek bilgi kaybettirir. Yeni yaklaşımlar bu yüzden birden çok nesneyi birlikte izleyen olay günlükleri kullanır.

## Bir örnek

> **Örnek (temsili rakamlar):** Olay günlüğü uydurmadır; sorgular `scripts/cards_numbers_ea_b1.py` içinde SQLite ile gerçekten çalıştırılmış, çıktı aynen aktarılmıştır.

Beş siparişin olay günlüğü `olay(vaka, aktivite, zaman)` tablosunda. Önce varyantları, yani her siparişin izlediği faaliyet sırasını sayıyoruz:

```sql
select varyant, count(*) vaka_sayisi from (
  select vaka, group_concat(aktivite,' > ') varyant
  from (select * from olay order by vaka, zaman) group by vaka)
group by varyant order by vaka_sayisi desc;
```

| Varyant | Vaka |
|---|---|
| Sipariş > Onay > Sevk > Fatura | 3 |
| Sipariş > Sevk > Fatura > Fatura | 1 |
| Sipariş > Sevk > Fatura | 1 |

Sonra her vakanın baştan sona süresini saat olarak:

```sql
select vaka, round((julianday(max(zaman))-julianday(min(zaman)))*24,1) saat
from olay group by vaka order by saat desc;
```

| Vaka | Saat |
|---|---|
| S5 | 70,5 |
| S3 | 46,3 |
| S1 | 23,2 |
| S4 | 22,1 |
| S2 | 6,1 |

Okuma: İki sipariş onay adımını atlamış (S2 ve S5). S5 ayrıca iki kez faturalanmış ve en uzun süren vaka. S3'te onay tek başına bir günden fazla sürmüş. Gerçek bir ERP'de aynı sorgular on binlerce siparişte çalışır; ilk bakılacak yer, onaysız ve tekrar faturalı varyantlardır.

> **Not:** Buradaki SQL, yöntemi göstermek içindir. Ticari süreç madenciliği araçları bu işi görsel olarak yapar; önemli olan doğru olay günlüğünü hazırlamaktır.

## Sık yapılan hatalar

- Zaman damgası olmayan ya da yalnızca tarih (saat yok) tutan alanlarla analiz yapmak.
- Faaliyet adlarını farklı sistemlerde farklı yazmak; aynı adımı iki ayrı faaliyet gibi göstermek.
- Bir faturanın birden çok siparişe bağlandığı durumları göz ardı etmek.
- En sık varyantı "doğru süreç" sanmak; sık olan her zaman doğru değildir.
- Sonucu kişileri suçlamak için kullanmak; çalışanlar kayıt girmeyi bırakır.

## Pratikte nasıl uygulanır?

- [ ] BT'den seçtiğiniz süreç için vaka–faaliyet–zaman üçlüsünü içeren bir dışa aktarım isteyin.
- [ ] Faaliyet adlarını sadeleştirip tek listede birleştirin.
- [ ] Önce varyant sayımını yapın; ilk beş varyantı ve onay atlayan vakaları inceleyin.
- [ ] Uygunluk kontrolü için 2–3 kural yazın (ör. "limit aşan sipariş onaysız sevk edilemez").
- [ ] Bulguları süreç sahibiyle paylaşın ve iyileştirme döngüsüne alın.

## Daha fazlası

- van der Aalst, Weijters ve Maruster (2004), *IEEE Transactions on Knowledge and Data Engineering*. https://doi.org/10.1109/TKDE.2004.47
- processmining.org. https://www.processmining.org/
- van der Aalst, *Process Mining: Data Science in Action* (kitap; doğrulanmadı).
