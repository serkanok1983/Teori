---
id: kb-ea-15-5-kvkk-basics
title: "KVKK temelleri: Satış ve dağıtım verisinde kişisel veri"
summary: "6698 sayılı Kişisel Verilerin Korunması Kanunu'nun satış, dağıtım ve CRM sistemlerinde ne anlama geldiğini; aydınlatma, açık rıza, saklama süresi, veri güvenliği, ihlal bildirimi ve yurt dışına aktarım başlıklarını anlatır."
course: ea
category: bt-yonetisimi-ve-guvenlik
tags: [kvkk, kisisel-veri, mevzuat, crm, guvenlik]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, it-yoneticisi]
level: temel
source_lessons: [EA-15.5]
reading_minutes: 3
key_points:
  - "Bakkal sahibinin adı, telefonu, konum verisi ve temsilci GPS kayıtları kişisel veridir."
  - "Her işleme faaliyetinin bir hukuki sebebi olmalı; açık rıza bu sebeplerden yalnızca biridir."
  - "Veri sahibine hangi veriyi neden işlediğinizi anlatan aydınlatma metni verilmelidir."
  - "Veriler amaç için gereken süre kadar saklanmalı, sonra silinmeli veya anonim hale getirilmelidir."
  - "Veri ihlali, yurt dışına aktarım ve kayıt yükümlülükleri için güncel Kurul kararlarına bakılmalıdır."
glossary_terms: [kvkk, acik-riza, aydinlatma-yukumlulugu]
related: [kb-ea-15-2-user-roles-permissions, kb-ea-25-4-consent-iys-marketing, kb-ea-16-5-cloud-cost-data-residency, kb-ea-8-1-master-data-governance]
sources:
  - title: "6698 sayılı Kişisel Verilerin Korunması Kanunu"
    authors: "T.C. Cumhurbaşkanlığı Mevzuat Bilgi Sistemi"
    year: 2016
    type: law
    url: "https://www.mevzuat.gov.tr/"
    verified: true
    checked_on: 2026-10-28
  - title: "Kişisel Verileri Koruma Kurumu"
    authors: "KVKK"
    year: 2026
    type: web
    url: "https://www.kvkk.gov.tr/"
    verified: true
    checked_on: 2026-10-28
time_sensitive: true
valid_as_of: 2026-10-28
status: draft
language: tr
version: "0.1"
updated: 2026-10-28
---

## Ne işe yarar?

Satış ve dağıtım sistemleri kişisel veriyle doludur: bakkal sahibinin adı ve cep telefonu, teslimat adresleri, saha temsilcisinin gün boyu konumu, sadakat programı üyeleri. Bu kart, **KVKK**'nın bu sistemlerde hangi soruları doğurduğunu yönetici diliyle özetler. Hukuki görüş yerine geçmez.

## Temel fikir

6698 sayılı Kanun, kimliği belirli ya da belirlenebilir gerçek kişiye ait her bilgiyi kişisel veri sayar. Tüzel kişi bilgisi (firma unvanı, vergi numarası) kapsam dışıdır; ancak şahıs işletmesinde ad ve telefon kişisel veridir.

Temel başlıklar:

- **Hukuki sebep:** Kanun, sözleşmenin ifası, hukuki yükümlülük, meşru menfaat gibi işleme şartlarını sayar. **Açık rıza** bu şartlardan biridir; her şey için rıza toplamak hem gereksiz hem de rıza geri alındığında sorun yaratır.
- **Aydınlatma yükümlülüğü:** Veri sahibine kimin, hangi amaçla, hangi veriyi işlediği ve kime aktardığı anlatılır.
- **Ölçülülük ve saklama:** Amaç için gereken veri toplanır, gereken süre saklanır, sonra silinir veya anonim hale getirilir.
- **Veri güvenliği:** Yetki yönetimi, kayıt tutma ve şifreleme gibi teknik ve idari tedbirler alınır.
- **İhlal bildirimi:** Veri ihlalinde Kurul'a ve ilgili kişilere bildirim yapılır; süre ve yöntem Kurul kararlarıyla belirlenmiştir.
- **Yurt dışına aktarım:** Yurt dışındaki bir bulut hizmetine veri göndermek aktarım sayılabilir; bu kurallar 2024'te değiştirilmiştir.
- **Sicile kayıt (VERBİS):** Kayıt yükümlülüğü ve istisnalar Kurul kararlarıyla belirlenir.

### Kişisel veri envanterinden başlamak

Uyum çalışmalarının pratik başlangıç noktası, kişisel veri envanteridir. Her süreç için hangi kişisel verilerin, hangi amaçla, hangi hukuki sebebe dayanarak işlendiği, kimlerle paylaşıldığı ve ne kadar süre saklandığı bir tabloda toplanmalıdır. Satış ve dağıtım şirketlerinde bu tablo; müşteri yetkilileri, şahıs işletmesi sahipleri, sürücüler, saha çalışanları ve tüketici şikâyetleri gibi kategorileri içerir. Envanter, aydınlatma metinlerinin, saklama politikasının ve erişim yetkilerinin tutarlı olmasını sağlar. Hukuki değerlendirmeler ve güncel yükümlülükler için hukuk danışmanınıza başvurmanız önerilir.

## Bir örnek

> **Örnek (temsili rakamlar):** Bu örnekte hesap gerektiren rakam yoktur; senaryo temsilidir.

Bir bayi, saha uygulamasıyla temsilcilerinin konumunu izliyor ve CRM'de bakkal sahiplerinin cep telefonlarını tutuyor. Yaptığı gözden geçirmede şunları buluyor:

- Konum verisi mesai dışında da toplanıyor. Uygulama yalnızca mesai saatinde konum alacak şekilde ayarlanıyor ve temsilcilere aydınlatma metni veriliyor.
- Kampanya SMS'leri için ayrıca ticari elektronik ileti izni gerekiyor; bu, KVKK'dan ayrı bir yükümlülük.
- Beş yıl önce çalışmayı bırakan müşterilerin kişisel verileri hâlâ duruyor. Saklama süreleri belirleniyor ve periyodik imha planı yapılıyor.
- CRM tedarikçisinin sunucularının nerede olduğu sözleşmeden kontrol ediliyor.

## Sık yapılan hatalar

- Her işlem için açık rıza istemek ya da rızayı sözleşmenin şartı yapmak.
- Excel ile e-postada müşteri listesi dolaştırmak.
- Eski verileri "belki lazım olur" diye silmemek.
- Bulut sağlayıcısının veriyi nerede tuttuğunu bilmemek.

## Pratikte nasıl uygulanır?

- [ ] Satış, dağıtım ve CRM sistemlerindeki kişisel veri alanlarını listeleyin.
- [ ] Her biri için amacı, hukuki sebebi ve saklama süresini yazın.
- [ ] Müşteri, temsilci ve sürücüler için aydınlatma metinlerini hazırlayın.
- [ ] Yetkileri en az yetki ilkesine göre daraltın.
- [ ] İhlal durumunda kimin ne yapacağını yazılı hale getirin.

> **Mevzuat notu:** Bu karttaki oran ve kurallar 2026-10-28 tarihi itibarıyla derlenmiştir. Mevzuat güncel olmayabilir; uygulamadan önce mali müşavirinize veya danışmanınıza doğrulatın. KVKK uygulaması için bir avukattan görüş alınmalıdır.

## Daha fazlası

- 6698 sayılı Kanun: https://www.mevzuat.gov.tr/
- Kişisel Verileri Koruma Kurumu, rehberler ve Kurul kararları: https://www.kvkk.gov.tr/
