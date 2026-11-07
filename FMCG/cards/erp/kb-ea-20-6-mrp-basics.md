---
id: kb-ea-20-6-mrp-basics
title: "MRP temelleri: Ürün ağacı, net ihtiyaç ve üretim planı"
summary: "Malzeme ihtiyaç planlamasının (MRP) mantığını; ana üretim planı, ürün ağacı, brüt ve net ihtiyaç, tedarik süresi ve parti büyüklüğü kavramlarını ve MRP çıktısının satın alma ile üretim emirlerine nasıl dönüştüğünü anlatır."
course: ea
category: erp
tags: [erp, mrp, uretim-planlama, urun-agaci, satin-alma]
roles: [uretici-sahibi, uretici-yonetici, depo-lojistik-muduru, it-yoneticisi]
level: orta
source_lessons: [EA-20.6, EA-20.7]
reading_minutes: 3
key_points:
  - "MRP, ana üretim planından ve ürün ağacından malzeme ihtiyacını hesaplar."
  - "Net ihtiyaç = brüt ihtiyaç − eldeki stok − yoldaki siparişler."
  - "Tedarik süresi geriye sayılarak siparişin ne zaman verilmesi gerektiği bulunur."
  - "Parti büyüklüğü kuralı sipariş miktarını yuvarlar."
  - "MRP'nin kalitesi; ürün ağacı, stok ve tedarik süresi verilerinin doğruluğuna bağlıdır."
glossary_terms: [mrp, urun-agaci, ana-uretim-plani, tedarik-suresi]
related: [kb-ea-20-5-inventory-in-erp, kb-ea-20-3-procure-to-pay, kb-ea-34-1-purchasing-supplier-management, kb-ea-20-1-what-erp-does]
sources:
  - title: "Orlicky's Material Requirements Planning"
    authors: "Orlicky, J."
    year: 1975
    type: book
    verified: false
  - title: "Manufacturing Planning and Control for Supply Chain Management"
    authors: "Vollmann, T. E.; Berry, W. L.; Whybark, D. C.; Jacobs, F. R."
    year: 2005
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

Üretimde ya hammadde eksik kalır ya da depo gereksiz malzemeyle dolar. **Malzeme ihtiyaç planlaması** (MRP), "neyi, ne kadar, ne zaman almalıyım?" sorusunu sistematik olarak yanıtlar.

## Temel fikir

Orlicky'nin tanımladığı ve Vollmann ve arkadaşlarının ayrıntılandırdığı MRP mantığı üç girdiye dayanır:

1. **Ana üretim planı:** Hangi bitmiş üründen hangi hafta kaç adet üretileceği.
2. **Ürün ağacı:** Bir bitmiş ürünün hangi yarı mamul ve hammaddelerden, hangi miktarlarda oluştuğu.
3. **Stok ve açık siparişler:** Eldeki stok ve yolda olan satın alma siparişleri.

Hesap adımları:

- **Brüt ihtiyaç:** Üretim miktarı × ürün ağacındaki kullanım miktarı.
- **Net ihtiyaç:** Brüt ihtiyaç − eldeki stok − yoldaki siparişler.
- **Parti büyüklüğü:** Net ihtiyaç, tedarikçinin minimum veya katlı sipariş kuralına göre yuvarlanır.
- **Zaman kaydırma:** İhtiyaç tarihinden tedarik süresi kadar geriye gidilerek sipariş tarihi bulunur.

MRP'nin çıktısı **planlı sipariş** önerileridir. Planlama ekibi bunları satın alma siparişine (dış temin) veya üretim emrine (iç üretim) dönüştürür.

**Kapasite kontrolü:** Klasik MRP, kapasitenin sınırsız olduğunu varsayar. Bu nedenle üretim planının makine ve iş gücü kapasitesiyle ayrıca kontrol edilmesi gerekir.

### MRP'nin güvenilir çalışması için ön koşullar

MRP, verilen verilerle mekanik olarak hesap yapar; verilerdeki hatalar doğrudan yanlış planlara dönüşür. Vollmann ve arkadaşlarının vurguladığı gibi, sistemin başarısı büyük ölçüde veri doğruluğuna bağlıdır. Başlıca ön koşullar şunlardır:

- **Doğru ürün ağacı:** Her mamulün hangi bileşenlerden ve hangi miktarlarda oluştuğu doğru tanımlanmalıdır. Mühendislik değişiklikleri, yürürlük tarihleriyle birlikte ürün ağacına yansıtılmalıdır.
- **Doğru stok:** MRP, eldeki stoğu düşerek net ihtiyacı hesaplar. Stok kayıtlarındaki hatalar, ya gereksiz satın almaya ya da malzeme eksikliğine yol açar.
- **Gerçekçi tedarik süreleri:** Tedarik ve üretim süreleri, gerçekleşen verilere göre güncellenmelidir.
- **Güvenilir ana üretim planı:** MRP'nin girdisi olan ana üretim planı, kapasite ve talep açısından gerçekçi olmalıdır. Sürekli değişen bir plan, sistemin sürekli yeni öneriler üretmesine ve planlayıcıların sisteme güvenini kaybetmesine yol açar.

**Planlayıcının iş listesi.** MRP, öne çekme, erteleme ve iptal gibi önerilerde bulunur. Planlayıcılar, tüm önerileri tek tek incelemek yerine, en kritik istisnalara odaklanmalıdır.

**Dağıtım şirketleri için not.** Üretim yapmayan dağıtım şirketlerinde de benzer mantık, paketleme veya karışık koli hazırlama gibi işlemlerde ve dağıtım ihtiyaç planlamasında kullanılır. Orlicky'nin temel fikri, bağımlı talebin tahmin edilmesi değil hesaplanması gerektiğidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b4.py` ile yapılmıştır.

Bir gıda üreticisi 10. haftada 1.000 koli ürün üretecek. Her koli 2 adet ambalaj kullanıyor.

- Brüt ihtiyaç: 1.000 × 2 = **2.000** ambalaj
- Eldeki stok 600, yoldaki sipariş 400
- Net ihtiyaç: **1.000** ambalaj
- Tedarikçi 500'lük partilerle satıyor: sipariş **1.000** adet
- Tedarik süresi 2 hafta: sipariş **8. haftada** verilmeli

Ürün ağacında ambalaj kullanımı yanlışlıkla 1 adet girilseydi, MRP 1.000 ambalaj eksik hesaplayacak ve üretim 10. haftada duracaktı.

## Sık yapılan hatalar

- Ürün ağacını güncellemeden reçete değiştirmek.
- Temin sürelerini tedarikçinin gerçek performansıyla güncellememek.
- MRP önerilerini kontrol etmeden toplu olarak siparişe dönüştürmek.
- Kapasiteyi kontrol etmeden ana üretim planını kesinleştirmek.

## Pratikte nasıl uygulanır?

- [ ] En çok kullanılan 20 ürünün ürün ağacını üretimle birlikte doğrulayın.
- [ ] Kritik malzemelerin temin sürelerini son siparişlere göre güncelleyin.
- [ ] MRP'yi haftalık çalıştırın ve istisna mesajlarını gözden geçirin.
- [ ] Ana üretim planını kapasiteyle karşılaştıran basit bir kontrol ekleyin.

## Daha fazlası

- Orlicky, *Material Requirements Planning* (kitap; doğrulanmadı).
- Vollmann ve ark., *Manufacturing Planning and Control for Supply Chain Management* (kitap; doğrulanmadı).
