---
id: kb-ea-30-4-barcodes-traceability
title: "Barkod, GS1 standartları ve izlenebilirlik"
summary: "GTIN, SSCC ve GS1-128 gibi GS1 standartlarını, parti ve son kullanma tarihinin barkodla izlenmesini ve bir geri çağırmada etkilenen ürünlerin ve müşterilerin nasıl hızla bulunacağını anlatır."
course: ea
category: tedarik-ve-depo-sistemleri
tags: [barkod, gs1, gtin, sscc, izlenebilirlik]
roles: [depo-lojistik-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-30.4]
reading_minutes: 2
key_points:
  - "GTIN, bir ürünün dünya genelinde tekil kimliğidir ve barkodda taşınır."
  - "SSCC, bir palet veya lojistik birimin tekil numarasıdır."
  - "GS1-128 gibi barkodlar parti ve son kullanma tarihini de taşıyabilir."
  - "İzlenebilirlik, bir partinin nereden geldiğini ve nereye gittiğini bulabilmektir."
  - "Geri çağırma hızı, parti bilgisinin her harekette okutulmasına bağlıdır."
glossary_terms: [gtin, sscc, izlenebilirlik]
related: [kb-ea-30-3-wms-what-it-does, kb-ea-32-2-food-safety-traceability, kb-ea-37-2-e-irsaliye-practice]
sources:
  - title: "GS1 Türkiye"
    authors: "GS1 Türkiye"
    year: 2026
    type: web
    url: "https://www.gs1tr.org/"
    verified: false
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Bir ürün partisinde sorun çıktığında şirketin ilk sorusu şudur: "Bu parti hangi müşterilere gitti?" Yanıtı saatler içinde verebilmek, barkod ve parti takibinin doğru kurulmasına bağlıdır.

## Temel fikir

**GS1 standartları.** GS1, dünya genelinde kullanılan ürün ve lojistik numaralandırma standartlarını yönetir. Türkiye'de GS1 Türkiye üyelik ve numara tahsisini yürütür.

- **GTIN:** Ürünün (ör. bir şişe, bir koli) tekil numarası. Perakendedeki barkodlar bu numarayı taşır.
- **SSCC:** Palet gibi lojistik birimlerin tekil numarası. Sevkiyat etiketinde bulunur.
- **GS1-128 ve GS1 DataMatrix:** GTIN'in yanında parti numarası, son kullanma tarihi gibi ek bilgileri taşıyabilen barkod türleri.

**İzlenebilirlik.**

- **Geriye doğru:** Bir partinin hangi hammadde ve tedarikçiden geldiği.
- **İleriye doğru:** Bir partinin hangi müşterilere sevk edildiği.

İleriye doğru izlenebilirlik için sevkiyatta parti numarasının okutulması ve irsaliyeye yazılması gerekir.

### İzlenebilirliği sistemde kurmak

Barkod standardını kullanmak tek başına izlenebilirlik sağlamaz; verinin süreç boyunca kaydedilmesi gerekir. Uygulamada dikkat edilecek noktalar şunlardır:

- **Ana veri:** Her ürün için GTIN, ambalaj hiyerarşisi (adet, koli, palet) ve ağırlık bilgisi ERP'de doğru tanımlanmalıdır. Koli ve adet için aynı numaranın kullanılması, depoda yanlış miktar okunmasına yol açar.
- **Mal kabulde okutma:** Tedarikçiden gelen paletin SSCC'si okutulduğunda, içerdiği ürün ve partiler sisteme tek seferde alınabilir. Bunun için tedarikçinin sevk bildirimini elektronik göndermesi gerekir.
- **Sevkiyatta okutma:** İleriye doğru izlenebilirlik, hangi partinin hangi müşteriye gittiğinin kaydedilmesine bağlıdır. Yalnızca ürün kodu okutulup parti atlanırsa geri çağırmada tüm müşterilere ulaşmak gerekir.
- **Etiket kalitesi:** Okunamayan etiketler elle girişe, elle giriş de hataya yol açar. Etiket basım ve yapıştırma standartları belirlenmelidir.

**Test edin.** İzlenebilirliğin gerçekten çalıştığını görmenin en iyi yolu, rastgele seçilen bir parti için geriye ve ileriye doğru izleme tatbikatı yapmaktır. Tatbikatın ne kadar sürdüğü ve hangi kayıtların eksik çıktığı, iyileştirme listesinin başlangıç noktasıdır.

### Tedarikçilerle uyum

İzlenebilirlik zinciri, tedarikçilerin parti bilgisini doğru etiketlemesine bağlıdır. Tedarikçi sözleşmelerine etiketleme gereksinimleri eklenmelidir.

**Palet ve koli etiketi.** Sevkiyat birimleri için GS1 standartlarında seri sevkiyat kap kodu (SSCC) kullanılır. Bu kod, paletin içindeki ürünleri, partileri ve miktarları elektronik irsaliye veya sevk bildirimiyle eşleştirir; alıcı paleti tek okutmayla kabul edebilir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b7.py` ile yapılmıştır.

Bir üretici 1 parti üründe etiket hatası tespit ediyor. Depo sistemi, partinin 36 palete dağıldığını ve SSCC numaralarıyla 48 noktaya sevk edildiğini dakikalar içinde listeliyor. Saha ekibi yalnızca bu noktalara gidiyor; tüm ürünleri toplatmaya gerek kalmıyor.

## Sık yapılan hatalar

- Parti bilgisini yalnızca üretimde tutup sevkiyatta okutmamak.
- Firma içi kodları GTIN yerine kullanmak.
- Palet etiketlerini elle yazmak.
- Geri çağırma tatbikatı yapmamak.
- Koli ve adet için aynı barkodu kullanmak.
- Etiket kalitesini kontrol etmeyip elle girişe mahkûm olmak.

## Pratikte nasıl uygulanır?

- [ ] Ürünlerinizin GTIN'lerinin ve ana verisinin doğru olduğunu kontrol edin.
- [ ] Sevkiyatta parti okutmayı zorunlu yapın.
- [ ] Palet etiketlerini SSCC ile sistemden basın.
- [ ] Yılda bir geri çağırma tatbikatı yapın.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın.

## Daha fazlası

- GS1 Türkiye (doğrulanmadı): https://www.gs1tr.org/
