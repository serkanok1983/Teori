---
id: kb-eco-31-5-agency-governance-family-firm
title: "Aile şirketinde vekâlet sorunları ve kurumsal yönetim"
summary: "Aile şirketlerinde ortaklar, aile üyeleri ve profesyonel yöneticiler arasındaki çıkar çatışmalarını, ilişkili taraf işlemlerinin azınlık ortaklara maliyetini ve yönetim kurulu, iç denetim ve yazılı kurallarla bu sorunları azaltmayı anlatır."
course: eco
category: kurumsal-finans
tags: [kurumsal-yonetim, aile-sirketi, vekalet-sorunu]
roles: [uretici-sahibi, bayi-sahibi]
level: orta
source_lessons: [ECO-31.5]
reading_minutes: 3
key_points:
  - "Vekâlet sorunu, karar verenin çıkarı ile şirketin ya da diğer ortakların çıkarı ayrıştığında ortaya çıkar."
  - "Aile şirketlerinde asıl çatışma çoğu zaman yönetici ile ortak değil, kontrol eden aile ile diğer ortaklar arasındadır."
  - "Piyasa koşullarının dışındaki ilişkili taraf işlemleri, değeri sessizce bir ortaktan diğerine aktarır."
  - "Yazılı kurallar, bağımsız gözetim ve şeffaf raporlama vekâlet maliyetini düşürür."
glossary_terms: [vekalet-maliyeti, iliskili-taraf-islemi, asil-vekil-sorunu]
related: [kb-eco-12-3-principal-agent, kb-eco-54-3-governance-sustainability-reporting, kb-eco-31-8-mergers-acquisitions, kb-eco-33-7-reading-annual-report]
sources:
  - title: "Theory of the firm: Managerial behavior, agency costs and ownership structure"
    authors: "Jensen, M. C.; Meckling, W. H."
    year: 1976
    type: article
    doi: "10.1016/0304-405X(76)90026-X"
    url: "https://doi.org/10.1016/0304-405X(76)90026-X"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Financial Economics 3(4)."
  - title: "Corporate Ownership Around the World"
    authors: "La Porta, R.; Lopez-de-Silanes, F.; Shleifer, A."
    year: 1999
    type: article
    doi: "10.1111/0022-1082.00115"
    url: "https://doi.org/10.1111/0022-1082.00115"
    verified: true
    checked_on: 2026-10-28
    note: "Journal of Finance 54(2). Aile kontrolündeki şirketlerin yaygınlığı."
  - title: "6102 sayılı Türk Ticaret Kanunu"
    authors: "T.C. Resmî Gazete / Mevzuat Bilgi Sistemi"
    year: 2011
    type: law
    url: "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6102.pdf"
    verified: true
    checked_on: 2026-10-28
    note: "Mevzuat Bilgi Sistemi resmî PDF metni açıldı, kanun adı ve numarası eşleşti (2026-10-28)."
  - title: "Sermaye Piyasası Kurulu (resmî site)"
    authors: "SPK"
    year: 2026
    type: web
    url: "https://www.spk.gov.tr"
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

Türkiye'de dağıtım ve üretim şirketlerinin önemli bir kısmı aile şirketidir. Kuşak değişimi, yeni bir ortak, profesyonel genel müdür ya da banka kredisi gibi durumlarda yönetim kuralları önem kazanır. Bu kart, çıkar çatışmalarını tanımanızı ve bunları azaltacak pratik düzenlemeleri kurmanızı sağlar.

## Temel fikir

Jensen ve Meckling (1976), şirket yöneticisi ile sahipleri arasındaki çıkar farkının yarattığı kayıpları **vekâlet maliyeti** olarak tanımladı: izleme maliyetleri, güvence maliyetleri ve kalan verim kaybı.

Aile şirketlerinde sorun üç biçimde görülür:

1. **Ortak – profesyonel yönetici:** Yönetici kısa vadeli ciro hedefine, ortaklar uzun vadeli değere odaklanabilir.
2. **Kontrol eden aile – azınlık ortaklar:** La Porta ve diğerleri (1999), dünyanın pek çok ülkesinde şirketlerin kontrol eden aileler tarafından yönetildiğini ve asıl çatışmanın kontrol eden ortak ile azınlık ortaklar arasında olduğunu gösterdi.
3. **Aile üyeleri arasında:** Şirkette çalışan ve çalışmayan aile üyelerinin kâr dağıtımı, maaş ve yatırım beklentileri farklı olabilir.

**İlişkili taraf işlemleri** (aile üyelerine ait şirketlerden mal, hizmet ya da kira alımı) piyasa koşullarındaysa sorun değildir. Piyasa fiyatının üzerindeyse, kayıp tüm ortaklara yansır, kazanç ise yalnızca bir tarafa gider. Türk Ticaret Kanunu bu tür işlemler ve yönetim kurulu üyelerinin şirketle işlem yapması konusunda düzenlemeler içerir; halka açık şirketler ayrıca SPK kurumsal yönetim kurallarına tabidir. Somut uygulama için hukuk danışmanınıza başvurun.

## Bir örnek

> **Örnek (temsili rakamlar):** Alım tutarı, fiyat farkı ve ortaklık payları varsayımsaldır. Hesaplar `scripts/cards_numbers_eco_b3.py` ile yapılmıştır.

Bir distribütör yılda 20.000.000 TL'lik nakliye hizmetini, kontrol eden ailenin bir üyesine ait şirketten alıyor. Fiyatlar piyasanın %10 üzerinde.

- Şirketin yıllık fazladan maliyeti: **2.000.000 TL**.
- Şirkette %40 payı olan azınlık ortakların bu maliyetten payı: **800.000 TL**.

Kontrol eden aile, kaybın kendi payına düşen kısmını nakliye şirketinin kârıyla fazlasıyla geri kazanıyor. Azınlık ortak ise yalnızca kaybı taşıyor. Fiyatların yılda bir piyasa teklifleriyle karşılaştırılması ve işlemin yönetim kurulunda açıkça onaylanması bu sorunu büyük ölçüde önler.

## Sık yapılan hatalar

- İlişkili taraf işlemlerini kayıt dışı ya da belgesiz yürütmek.
- Aile üyelerinin şirketteki rollerini ve ücretlerini yazılı kurallara bağlamamak.
- Profesyonel yöneticiye yalnızca ciro bazlı prim vermek.
- Yönetim kurulunu yalnızca aile üyelerinden oluşturup bağımsız görüşe yer vermemek.
- Kâr dağıtımı politikasını belirsiz bırakmak.
- Ortaklar arasındaki anlaşmazlıklar için önceden bir çözüm ve hisse devri mekanizması kurmamak.

## Pratikte nasıl uygulanır?

- [ ] Tüm ilişkili taraf işlemlerini listeleyin ve yılda bir piyasa fiyatlarıyla karşılaştırın.
- [ ] Yönetim kuruluna en az bir bağımsız ve deneyimli üye ekleyin.
- [ ] Profesyonel yöneticilerin primini kârlılık, nakit ve sermaye getirisine bağlayın.
- [ ] Kurumsal yönetim düzenlemelerini hukuk danışmanınız ve mali müşavirinizle birlikte hazırlayın.
- [ ] Aile anayasası veya ortaklar sözleşmesiyle görev, ücret, kâr dağıtımı ve hisse devri kurallarını yazılı hâle getirin.

## Daha fazlası

- Jensen, M. C.; Meckling, W. H. (1976). *Theory of the firm: Managerial behavior, agency costs and ownership structure*. https://doi.org/10.1016/0304-405X(76)90026-X
- La Porta, R.; Lopez-de-Silanes, F.; Shleifer, A. (1999). *Corporate Ownership Around the World*. https://doi.org/10.1111/0022-1082.00115
- T.C. Resmî Gazete / Mevzuat Bilgi Sistemi (2011). *6102 sayılı Türk Ticaret Kanunu*. https://www.mevzuat.gov.tr/MevzuatMetin/1.5.6102.pdf
- SPK (2026). *Sermaye Piyasası Kurulu (resmî site)*. https://www.spk.gov.tr
