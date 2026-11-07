---
id: kb-ea-16-1-cloud-saas-basics
title: "Bulut ve SaaS temelleri: Kiralamak mı, kurmak mı?"
summary: "Bulut bilişimin temel özelliklerini, SaaS, PaaS ve IaaS modellerini ve kendi sunucunuzda kurulu yazılımla abonelik modeli arasındaki sorumluluk, maliyet ve bağımlılık farklarını anlatır."
course: ea
category: is-sistemleri-temelleri
tags: [bulut, saas, altyapi, maliyet]
roles: [uretici-sahibi, uretici-yonetici, bayi-sahibi, bayi-yonetici, satis-direktoru, it-yoneticisi]
level: temel
source_lessons: [EA-16.1]
reading_minutes: 3
key_points:
  - "Bulut; talep üzerine, ağ üzerinden, paylaşılan ve ölçülen kaynak kullanımıdır."
  - "SaaS'ta yazılımı, PaaS'ta platformu, IaaS'ta altyapıyı kiralarsınız."
  - "Abonelikte ilk yatırım düşüktür ama maliyet kullanıcı sayısıyla her yıl tekrar eder."
  - "Sorumluluk paylaşılır: Veri, kullanıcılar ve yetkiler her zaman sizin sorumluluğunuzdadır."
  - "Sözleşmede veri iadesi, yedekleme, hizmet seviyesi ve fiyat artışı maddeleri aranmalıdır."
glossary_terms: [saas, bulut-bilisim]
related: [kb-ea-16-5-cloud-cost-data-residency, kb-ea-17-2-total-cost-of-ownership, kb-ea-6-2-it-service-sla, kb-ea-14-4-backup-disaster-recovery]
sources:
  - title: "The NIST Definition of Cloud Computing (SP 800-145)"
    authors: "Mell, P.; Grance, T."
    year: 2011
    type: standard
    doi: "10.6028/NIST.SP.800-145"
    url: "https://doi.org/10.6028/NIST.SP.800-145"
    verified: true
    checked_on: 2026-10-28
  - title: "A view of cloud computing"
    authors: "Armbrust, M.; Fox, A.; Griffith, R. ve ark."
    year: 2010
    type: article
    doi: "10.1145/1721654.1721672"
    url: "https://doi.org/10.1145/1721654.1721672"
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

Yeni bir ERP, CRM ya da saha satış uygulaması seçerken ilk sorulardan biri "bulutta mı, kendi sunucumuzda mı?" olur. Bu kart, kararı verirken kullanacağınız kavramları ve sözleşmede bakmanız gerekenleri özetler.

## Temel fikir

NIST'in tanımına (SP 800-145) göre **bulut bilişim**in beş özelliği vardır: ihtiyaç anında self-servis kullanım, ağ üzerinden erişim, paylaşılan kaynak havuzu, hızlı ölçeklenme ve ölçülen kullanım. Üç hizmet modeli:

| Model | Ne kiralarsınız | Örnek kullanım |
|---|---|---|
| **SaaS** | Hazır yazılımı | Bulut ERP, CRM, e-posta |
| **PaaS** | Uygulama geliştirme ve çalıştırma platformunu | Kendi saha uygulamanızı geliştirmek |
| **IaaS** | Sanal sunucu, depolama, ağ | Mevcut ERP'yi buluttaki sunucuya taşımak |

Armbrust ve arkadaşları (2010), bulutun ekonomik avantajını sermaye harcamasının kullanım kadar ödenen gidere dönüşmesi ve kapasitenin ihtiyaca göre artırılıp azaltılabilmesi olarak açıklar. Bunun karşılığında bazı riskler gelir: tedarikçiye bağımlılık, verinin başka bir yerde tutulması ve tekrar eden maliyet.

Sorumluluk paylaşılır. SaaS'ta sunucu, yazılım güncellemesi ve altyapı yedeği tedarikçidedir. Kullanıcıların kim olduğu, yetkileri, verinin doğruluğu ve verinin dışarı alınabilmesi ise her zaman sizin sorumluluğunuzdadır.

### SaaS sözleşmesinde dikkat edilecek konular

Bulut hizmetine geçişte teknik özellikler kadar sözleşme koşulları da önemlidir. Hizmet sözleşmesinde şu konular açıkça yer almalıdır:

- **Hizmet seviyesi:** Taahhüt edilen erişilebilirlik oranı, planlı bakım pencereleri, destek saatleri ve olaylara müdahale süreleri. Taahhüdün karşılanmaması hâlinde uygulanacak yaptırımlar da yazılı olmalıdır.
- **Veri sahipliği ve konumu:** Verinin sahibinin şirketiniz olduğu, verinin hangi ülkelerde işlendiği ve saklandığı belirtilmelidir. Kişisel veri mevzuatı açısından yurt dışına veri aktarımı ayrıca değerlendirilmelidir.
- **Yedekleme ve geri yükleme:** Sağlayıcının yedekleme sıklığı, saklama süresi ve sizin talebiniz üzerine geri yükleme yapılıp yapılmadığı sorulmalıdır.
- **Çıkış ve veri teslimi:** Sözleşme sona erdiğinde verilerin hangi formatta ve ne sürede teslim edileceği, ardından nasıl silineceği tanımlanmalıdır.
- **Fiyat değişiklikleri:** Abonelik ücretlerinin artış koşulları ve kullanıcı sayısındaki değişikliklerin fiyata etkisi açık olmalıdır.
- **Güvenlik belgeleri:** Sağlayıcının bağımsız güvenlik denetim raporları ve belgeleri talep edilmelidir.

**Paylaşılan sorumluluk.** Bulut modelinde güvenlik sorumluluğu sağlayıcı ile müşteri arasında paylaşılır. SaaS'ta altyapı ve uygulama sağlayıcının sorumluluğundadır; ancak kullanıcı hesapları, yetkiler ve verinin doğru kullanımı şirketinizin sorumluluğunda kalır. Mell ve Grance'in tanımındaki hizmet modelleri, bu sorumluluk paylaşımını anlamak için iyi bir başlangıç noktasıdır.

**Bağlantı.** Bulut uygulamaları internet bağlantısına bağımlıdır; şube ve depoların yedek bağlantı ihtiyacı değerlendirilmelidir.

## Bir örnek

> **Örnek (temsili rakamlar):** Rakamlar gerçek değildir; hesaplar `scripts/cards_numbers_ea_b3.py` ile yapılmıştır.

Bir bayi, 40 kullanıcılı bir bulut ERP teklifi alıyor. Kullanıcı başı aylık ücret 1.500 TL:

- Aylık maliyet **60.000 TL**, yıllık **720.000 TL**.
- İki yıl içinde kullanıcı sayısının %25 artarak 50'ye çıkması bekleniyor. O zaman yıllık maliyet **900.000 TL** olacak.

Bayi teklifleri yalnızca ilk yıl maliyetiyle değil, beş yıllık toplam sahip olma maliyetiyle karşılaştırmaya karar veriyor. Sözleşmeye yıllık fiyat artışı için üst sınır, sözleşme bittiğinde verinin standart biçimde iade edilmesi ve yedekleme koşulları maddelerini ekletiyor.

## Sık yapılan hatalar

- Bulutun her zaman daha ucuz olduğunu varsaymak.
- Yedeklemenin tedarikçinin işi olduğunu düşünüp sözleşmeyi kontrol etmemek.
- Çıkış planı yapmamak: Veri hangi biçimde ve ne kadar sürede geri alınır?
- Pasif kullanıcı lisanslarını yıllarca ödemeye devam etmek.

## Pratikte nasıl uygulanır?

- [ ] Hangi modeli (SaaS, PaaS, IaaS) değerlendirdiğinizi netleştirin.
- [ ] Beş yıllık maliyeti kullanıcı artışı ve fiyat artışıyla birlikte hesaplayın.
- [ ] Sözleşmede hizmet seviyesi, yedekleme, veri konumu, veri iadesi ve fiyat artışı maddelerini arayın.
- [ ] Lisansları üç ayda bir gerçek kullanıma göre gözden geçirin.

## Daha fazlası

- NIST SP 800-145: https://doi.org/10.6028/NIST.SP.800-145
- Armbrust ve ark. (2010), *Communications of the ACM*. https://doi.org/10.1145/1721654.1721672
