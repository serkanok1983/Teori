---
id: kb-ea-4-2-bpm-lifecycle
title: "Süreç iyileştirme döngüsü: Belirle, keşfet, analiz et, yeniden tasarla, izle"
summary: "İş süreçlerini bir kerelik projeyle değil, tanımlama, keşif, analiz, yeniden tasarım, uygulama ve izleme adımlarından oluşan bir döngüyle yönetmeyi; ortalama yerine medyan ve eşik aşımıyla izlemeyi anlatır."
course: ea
category: surec-yonetimi
tags: [surec, bpm, kpi, iade, verimlilik]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, it-yoneticisi]
level: orta
source_lessons: [EA-4.2]
reading_minutes: 3
key_points:
  - "Süreç yönetimi altı adımlı bir döngüdür: belirleme, keşif, analiz, yeniden tasarım, uygulama, izleme."
  - "Önce hangi süreçlerin önemli olduğu belirlenir; her süreç aynı ilgiyi hak etmez."
  - "Keşif, sürecin kâğıttaki halini değil gerçekte nasıl yürüdüğünü ortaya çıkarır."
  - "İzleme için ortalamanın yanında medyan ve eşik aşan vaka sayısı kullanılmalıdır."
  - "İzleme sonuçları döngüyü yeniden başlatır; süreç iyileştirme bitmez."
glossary_terms: [bpm, is-sureci]
related: [kb-ea-4-1-what-is-a-process, kb-ea-4-3-process-maps-bpmn, kb-ea-4-6-process-analysis-cycle-time, kb-ea-4-7-process-mining]
sources:
  - title: "Fundamentals of Business Process Management"
    authors: "Dumas, M.; La Rosa, M.; Mendling, J.; Reijers, H. A."
    year: 2018
    type: book
    verified: false
    note: "2. baskı yılı yayımlamadan önce kontrol edilmeli."
time_sensitive: false
valid_as_of: null
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Firmalar süreçlerini genellikle bir kriz ya da yeni yazılım projesiyle ele alır, sonra unutur. Bu kart, süreçleri sürekli bir döngüyle yönetmeyi sağlayan **iş süreci yönetimi** (BPM, *business process management*) yaklaşımını anlatır. Hangi sürece öncelik vereceğinize, iyileşmeyi nasıl ölçeceğinize ve ne zaman yeniden ele alacağınıza karar verirken işe yarar.

## Temel fikir

Dumas ve arkadaşlarının ders kitabında anlatılan döngü altı adımdan oluşur:

1. **Belirleme:** Firmanın süreçleri listelenir ve önceliklendirilir. Ölçüt: stratejik önem, sorunun büyüklüğü ve iyileştirmenin mümkün olması.
2. **Keşif:** Süreç gerçekte nasıl yürüyorsa öyle belgelenir. Çalışanlarla görüşme, iş başında gözlem ve sistem kayıtları kullanılır.
3. **Analiz:** Sorunlar ve nedenleri bulunur; süre, maliyet, hata gibi ölçülerle sayısallaştırılır.
4. **Yeniden tasarım:** Sorunları gideren yeni süreç tasarlanır; alternatifler karşılaştırılır.
5. **Uygulama:** Hem organizasyon (görev, yetki, eğitim) hem de sistem (yazılım ayarı, iş akışı) tarafında değişiklik yapılır.
6. **İzleme:** Yeni süreç ölçülür. Sapma ya da yeni sorun çıkınca döngü yeniden başlar.

Bu döngünün üzerinde bir **süreç mimarisi** durur: firmanın ana süreçlerinin (ör. satış, tedarik, finans) ve bunların alt süreçlerinin haritası. Mimari, hangi sürecin kime ait olduğunu ve birbirine nasıl bağlandığını gösterir.

İzleme için doğru ölçüyü seçmek önemlidir. Süreç süreleri genellikle çarpık dağılır: Birkaç uzun vaka ortalamayı yukarı çeker. Bu yüzden ortalamanın yanında **medyanı** ve belirlenen bir eşiği aşan vaka sayısını da izleyin.

### Döngüyü sürdürmek

Süreç iyileştirmenin en zor kısmı, döngünün tek bir projeyle bitmemesini sağlamaktır. Bunun için her temel sürecin bir sahibi, birkaç izleme göstergesi ve düzenli gözden geçirme takvimi olmalıdır. Göstergeler hedeften saptığında, döngü yeniden keşif ve analiz aşamasına döner. Dumas ve arkadaşları, izleme aşamasının bir sonraki iyileştirme döngüsünü besleyen aşama olduğunu vurgular.

## Bir örnek

> **Örnek (temsili rakamlar):** Vakalar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b1.py` ile yapılmıştır.

Bir bayi, iade edilen mal için müşteriye iade faturası ya da fiyat farkı belgesinin geç düzenlenmesinden şikâyet alıyor. Süreç "belirleme" adımında öncelikli seçiliyor. Keşifte, iade belgesinin depo kabulünden sonra muhasebeye kâğıtla gittiği ve haftada bir toplu işlendiği görülüyor. Yeniden tasarımda depo kabulü sistemde yapılıyor ve muhasebeye otomatik görev düşüyor.

İade kabulünden belge düzenlenmesine kadar geçen gün, 12'şer vakalık örneklerle:

| Ölçü | Önce | Sonra |
|---|---|---|
| Ortalama | 5,7 gün | 2,0 gün |
| Medyan | 5,0 gün | 2,0 gün |
| 5 günü aşan vaka | 5 / 12 | 0 / 12 |

"Önce" örneğinde 12 günlük tek bir vaka ortalamayı medyanın üstüne çekiyor. "5 günü aşan vaka" ölçüsü, müşterinin hissettiği sorunu en doğrudan gösteren ölçü olarak izleme panosuna alınıyor.

## Sık yapılan hatalar

- Belirleme adımını atlayıp en gürültülü şikâyetin peşinden gitmek.
- Keşfi yalnızca prosedür dokümanından yapmak; gerçek uygulamayı görmemek.
- Yeniden tasarımı yalnızca yazılım ayarı olarak uygulamak; görev ve yetkiyi değiştirmemek.
- İzlemeyi yalnızca ortalamayla yapmak.
- Proje bitince izlemeyi bırakmak.

## Pratikte nasıl uygulanır?

- [ ] Firmanızın 8–12 ana sürecini listeleyin ve her birine bir sahip atayın.
- [ ] Her yıl önem ve sorun büyüklüğüne göre 2–3 süreci iyileştirme için seçin.
- [ ] Keşif için sürecin içindeki kişilerle konuşun ve sistem kayıtlarına bakın.
- [ ] Her süreç için bir süre ölçüsü (medyan) ve bir eşik ölçüsü (X günü aşan vaka) belirleyin.
- [ ] Değişikliği yaptıktan sonra en az üç ay ölçün; sonucu süreç sahibiyle gözden geçirin.

## Daha fazlası

- Dumas, La Rosa, Mendling ve Reijers, *Fundamentals of Business Process Management* (kitap; baskı yılı doğrulanmadı).
