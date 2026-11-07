---
id: kb-ea-39-4-ai-assistants-on-company-data
title: "Şirket verisi üzerinde yapay zekâ asistanları"
summary: "Büyük dil modellerinin ERP ve CRM verisine bağlanmasını; erişimle zenginleştirilmiş üretim (RAG), araç kullanımı, yetki kontrolü, uydurma (halüsinasyon) riski ve değerlendirme yöntemlerini anlatır."
course: ea
category: yapay-zeka-ve-otomasyon
tags: [yapay-zeka, rag, llm, yetki, degerlendirme]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, it-yoneticisi]
level: orta
source_lessons: [EA-39.4]
reading_minutes: 2
key_points:
  - "RAG, modelin cevap üretmeden önce ilgili belgeleri veya kayıtları getirip bunlara dayanarak yanıt vermesidir."
  - "Araç kullanımı, modelin sorgu veya işlem için tanımlı sistem fonksiyonlarını çağırmasıdır."
  - "Asistan, kullanıcının sistemdeki yetkisinden fazlasını görmemelidir."
  - "Dil modelleri akıcı ama yanlış içerik üretebilir; buna halüsinasyon denir."
  - "Asistan, gerçek sorulardan oluşan bir test setiyle düzenli ölçülmelidir."
glossary_terms: [rag, halusinasyon]
related: [kb-ea-39-3-genai-at-work, kb-ea-15-2-user-roles-permissions, kb-ea-39-5-ml-forecast-recommendation]
sources:
  - title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    authors: "Lewis, P. vd."
    year: 2020
    type: web
    url: "https://arxiv.org/abs/2005.11401"
    verified: true
    checked_on: 2026-10-28
    note: "URL HTTP 200 ile açıldı, başlık/kurum eşleşti (2026-10-28)."
  - title: "Survey of Hallucination in Natural Language Generation"
    authors: "Ji, Z.; Lee, N.; Frieske, R.; Yu, T."
    year: 2023
    type: article
    doi: "10.1145/3571730"
    url: "https://doi.org/10.1145/3571730"
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

"Geçen ay bölgemde en çok düşen bayi hangisi?" sorusunu bir asistana sormak caziptir. Ancak yanlış cevap veya yetkisiz veri gösterimi ciddi sorun yaratır. Bu kart, böyle bir asistanın nasıl güvenli kurulacağını anlatır.

## Temel fikir

**RAG (erişimle zenginleştirilmiş üretim):** Lewis ve arkadaşlarının tanımladığı yaklaşımda model, cevap vermeden önce bir arama adımıyla ilgili belgeleri getirir ve yanıtı bunlara dayandırır. Şirket içi prosedürler ve belgeler için yaygın bir yöntemdir.

**Araç kullanımı:** Sayısal sorular için model, belge aramak yerine tanımlı bir rapor veya sorgu fonksiyonunu çağırır. Sonuç sistemden gelir; model yalnızca açıklar.

**Yetki:** Asistan, soran kullanıcının kimliğiyle çalışmalı ve ERP/CRM'deki rol yetkileri aynen uygulanmalıdır.

**Halüsinasyon:** Ji ve arkadaşlarının derlemesi, dil modellerinin kaynağa dayanmayan içerik üretebildiğini ve bunun farklı türlerini inceler. Kaynak göstermek ve "bilmiyorum" diyebilmek bu riski azaltır ama sıfırlamaz.

**Değerlendirme:** Gerçek kullanıcı sorularından oluşan, doğru cevabı bilinen bir test seti hazırlanır; her değişiklikten sonra çalıştırılır.

### Kurulum adımları ve yönetim soruları

Şirket verisi üzerinde bir asistan kurarken, teknik seçimlerden önce yönetim kararlarının netleşmesi gerekir:

- **Kapsam:** Asistan hangi soruları cevaplayacak, hangilerini kesinlikle cevaplamayacak? Örneğin prosedür ve ürün bilgisi sorularına cevap verirken, personel ücretleri gibi hassas konuları kapsam dışında bırakmak.
- **Veri kaynakları:** Hangi belgeler ve sistemler bağlanacak? Güncel olmayan veya çelişkili belgeler, asistanın yanlış ama ikna edici cevaplar vermesine yol açar. Belge sahipliği ve güncelleme sorumluluğu belirlenmelidir.
- **İşlem yetkisi:** Asistan yalnızca okuyacak mı, yoksa sipariş açmak, kayıt güncellemek gibi işlemler de yapacak mı? İşlem yapan asistanlarda her adımın kullanıcı onayından geçmesi ve kayıt altına alınması gerekir.
- **Kayıt ve denetim:** Kim, ne sordu, asistan hangi kaynaklara dayanarak ne cevap verdi? Bu kayıtlar hem hata analizi hem de kişisel veri uyumu için gereklidir.
- **Dış hizmet kullanımı:** Model bir bulut hizmeti üzerinden çalışıyorsa, verinin nerede işlendiği ve saklandığı, sözleşme ve kişisel veri mevzuatı açısından değerlendirilmelidir.

**Değerlendirme seti nasıl hazırlanır?** Kullanıcılardan gerçek soruları toplayın; her biri için doğru cevabı ve dayandığı kaynağı bir uzman yazsın. Set, kolay sorular kadar zor ve tuzaklı soruları da içermelidir: cevabı olmayan sorular, yetki dışı sorular ve birden çok kaynağın birleştirilmesini gerektiren sorular. Asistanın "bu konuda bilgim yok" diyebilmesi de başarı olarak sayılmalıdır.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b8.py` ile yapılmıştır.

Bir ekip, satış asistanını 50 soruluk bir test setiyle ölçüyor; 44 cevap doğru: **%88,0**. Yanlışların çoğu sayısal sorularda çıkıyor. Ekip bu soruları belge aramasından rapor fonksiyonu çağrısına yönlendiriyor ve testi yeniden çalıştırıyor.

## Sık yapılan hatalar

- Asistana tüm veriyi tek bir servis hesabıyla açmak.
- Sayısal soruları modelin "tahminine" bırakmak.
- Cevaplarda kaynak göstermemek.
- Test seti olmadan canlıya almak.

## Pratikte nasıl uygulanır?

- [ ] Kullanım senaryolarını ve yasak alanları yazın.
- [ ] Kullanıcı yetkilerinin asistanda da uygulandığını test edin.
- [ ] Sayısal sorular için onaylı rapor fonksiyonları tanımlayın.
- [ ] Test seti hazırlayın ve her değişiklikte çalıştırın.
- [ ] Cevaplarda kaynak bağlantısı gösterin.

## Daha fazlası

- Lewis ve arkadaşları (2020), RAG makalesi, arXiv.
- Ji ve arkadaşları (2023), doğal dil üretiminde halüsinasyon derlemesi, ACM Computing Surveys.
