# Yeni terimler (ea)

EA kartları için yeni terimler; terms.md ile birleştirilecek.

## Kurumsal bilgi sistemi

```yaml
id: kurumsal-bilgi-sistemi
term: "Kurumsal bilgi sistemi"
en: "enterprise system"
definition: "Bir firmanın birden çok biriminin işlerini ortak veri ve kurallarla yürüten yazılım ve süreçler bütünü."
see_also: [erp, sfa]
cards: [kb-ea-1-1-what-is-an-enterprise-system]
```

## Geçiş maliyeti

```yaml
id: gecis-maliyeti
term: "Geçiş maliyeti"
en: "switching cost"
definition: "Bir yazılım ya da tedarikçiden başkasına geçerken katlanılan para, zaman, veri taşıma ve eğitim maliyeti."
see_also: [saas]
cards: [kb-ea-1-5-software-vendor-economics-lockin]
```

## SaaS (hizmet olarak yazılım)

```yaml
id: saas
term: "SaaS (hizmet olarak yazılım)"
en: "software as a service"
definition: "Yazılımın tedarikçinin sunucularında çalıştığı ve abonelikle kullanıldığı model."
see_also: [gecis-maliyeti]
cards: [kb-ea-1-5-software-vendor-economics-lockin, kb-ea-16-1-cloud-saas-basics]
```

## Teknoloji kabul modeli

```yaml
id: teknoloji-kabul-modeli
term: "Teknoloji kabul modeli"
en: "technology acceptance model (TAM)"
definition: "Kullanıcıların bir sistemi algılanan fayda ve kullanım kolaylığına göre benimsediğini öne süren model."
see_also: []
cards: [kb-ea-2-2-user-adoption]
```

## İş süreci

```yaml
id: is-sureci
term: "İş süreci"
en: "business process"
definition: "Bir tetikleyiciyle başlayıp müşteri ya da iç kullanıcı için sonuç üreten, birimler arası faaliyetler zinciri."
see_also: [bpm, siparisten-tahsilata]
cards: [kb-ea-3-2-it-plus-process-complementarity, kb-ea-4-1-what-is-a-process, kb-ea-4-2-bpm-lifecycle, kb-ea-4-3-process-maps-bpmn]
```

## Net bugünkü değer (NBD)

```yaml
id: net-bugunku-deger
term: "Net bugünkü değer (NBD)"
en: "net present value (NPV)"
definition: "Gelecekteki net nakit akışlarının iskonto edilerek bugüne indirgenmiş toplamından yatırımın düşülmesiyle bulunan değer."
see_also: [toplam-sahip-olma-maliyeti]
cards: [kb-ea-17-2-total-cost-of-ownership, kb-ea-3-6-it-business-case]
```

## Toplam sahip olma maliyeti

```yaml
id: toplam-sahip-olma-maliyeti
term: "Toplam sahip olma maliyeti"
en: "total cost of ownership (TCO)"
definition: "Bir sistemin satın alma, kurulum, işletme ve çıkış maliyetlerinin ömrü boyunca toplamı."
see_also: [net-bugunku-deger]
cards: [kb-ea-17-1-build-buy-configure, kb-ea-17-2-total-cost-of-ownership, kb-ea-3-6-it-business-case]
```

## İş süreci yönetimi (BPM)

```yaml
id: bpm
term: "İş süreci yönetimi (BPM)"
en: "business process management"
definition: "Süreçleri belirleme, keşif, analiz, yeniden tasarım, uygulama ve izleme döngüsüyle yönetme yaklaşımı."
see_also: [is-sureci, bpmn]
cards: [kb-ea-4-2-bpm-lifecycle]
```

## BPMN

```yaml
id: bpmn
term: "BPMN"
en: "Business Process Model and Notation"
definition: "Süreç haritaları için olay, faaliyet, karar noktası ve kulvar gibi öğeler tanımlayan standart gösterim."
see_also: [bpm]
cards: [kb-ea-4-3-process-maps-bpmn]
```

## Döngü süresi

```yaml
id: dongu-suresi
term: "Döngü süresi"
en: "cycle time"
definition: "Bir işin süreçte başlangıçtan bitişe kadar geçirdiği toplam süre."
see_also: [akis-verimliligi, little-yasasi]
cards: [kb-ea-4-6-process-analysis-cycle-time]
```

## Akış verimliliği

```yaml
id: akis-verimliligi
term: "Akış verimliliği"
en: "flow efficiency"
definition: "Gerçek iş süresinin toplam döngü süresine oranı."
see_also: [dongu-suresi]
cards: [kb-ea-4-6-process-analysis-cycle-time]
```

## Little yasası

```yaml
id: little-yasasi
term: "Little yasası"
en: "Little's law"
definition: "Dengedeki bir süreçte bekleyen iş sayısının, çıkış hızı ile döngü süresinin çarpımına eşit olması."
see_also: [dongu-suresi]
cards: [kb-ea-4-6-process-analysis-cycle-time]
```

## Süreç madenciliği

```yaml
id: surec-madenciligi
term: "Süreç madenciliği"
en: "process mining"
definition: "Sistem olay kayıtlarından sürecin gerçek akışını, varyantlarını ve sürelerini çıkaran yöntem."
see_also: [olay-gunlugu]
cards: [kb-ea-4-7-process-mining]
```

## Olay günlüğü

```yaml
id: olay-gunlugu
term: "Olay günlüğü"
en: "event log"
definition: "Vaka, faaliyet ve zaman damgası içeren sistem kayıtları."
see_also: [surec-madenciligi]
cards: [kb-ea-4-7-process-mining]
```

## İş akışı

```yaml
id: is-akisi
term: "İş akışı"
en: "workflow"
definition: "Bir talebi kurallara göre onaylayıcılara yönlendiren, süre takip eden ve kayıt tutan otomasyon."
see_also: [gorevler-ayriligi]
cards: [kb-ea-4-9-workflow-approvals]
```

## Görevler ayrılığı

```yaml
id: gorevler-ayriligi
term: "Görevler ayrılığı"
en: "segregation of duties (SoD)"
definition: "Bir işlemin başlatılması, onaylanması ve kaydedilmesinin farklı kişilerce yapılması ilkesi."
see_also: [is-akisi]
cards: [kb-ea-15-2-user-roles-permissions, kb-ea-6-4-internal-controls-sod, kb-ea-20-3-procure-to-pay, kb-ea-4-9-workflow-approvals]
```

## Uygulama portföyü

```yaml
id: uygulama-portfoyu
term: "Uygulama portföyü"
en: "application portfolio"
definition: "Firmanın kullandığı tüm uygulamaların iş yetenekleriyle eşlenmiş ve değerlendirilmiş listesi."
see_also: [erp]
cards: [kb-ea-5-4-application-portfolio]
```

## Entegrasyon

```yaml
id: entegrasyon
term: "Entegrasyon"
en: "integration"
definition: "Farklı uygulamaların veri ve işlemleri otomatik paylaşacak şekilde birbirine bağlanması."
see_also: [erp]
cards: [kb-ea-10-1-why-integration-is-hard, kb-ea-11-6-apis-for-managers, kb-ea-5-5-erp-core-vs-best-of-breed]
```

## BT yönetişimi

```yaml
id: bt-yonetisimi
term: "BT yönetişimi"
en: "IT governance"
definition: "Teknoloji kararlarını kimin, hangi bilgiyle verdiğini ve hesap verebilirliği belirleyen düzen."
see_also: []
cards: [kb-ea-6-1-it-governance-decision-rights]
```

## Hizmet seviyesi anlaşması (SLA)

```yaml
id: sla
term: "Hizmet seviyesi anlaşması (SLA)"
en: "service level agreement"
definition: "Bir hizmetin erişilebilirlik, yanıt ve çözüm sürelerini ölçülebilir biçimde tanımlayan anlaşma."
see_also: []
cards: [kb-ea-6-2-it-service-sla, kb-ea-25-5-customer-service-cases, kb-ea-17-4-vendor-selection-rfp, kb-ea-19-3-working-with-it-partners]
```

## Bilgi güvenliği

```yaml
id: bilgi-guvenligi
term: "Bilgi güvenliği"
en: "information security"
definition: "Bilginin gizliliğini, bütünlüğünü ve erişilebilirliğini koruma."
see_also: []
cards: [kb-ea-6-3-information-security-basics]
```

## Ana veri

```yaml
id: ana-veri
term: "Ana veri"
en: "master data"
definition: "Müşteri, ürün, tedarikçi gibi işlemlerde tekrar kullanılan temel kayıtlar."
see_also: [veri-yonetisimi, mdm]
cards: [kb-ea-10-1-why-integration-is-hard, kb-ea-8-1-master-data-governance, kb-ea-8-2-data-quality-field, kb-ea-8-3-mdm-matching-duplicates, kb-ea-8-4-gs1-barcodes-pim]
```

## Veri yönetişimi

```yaml
id: veri-yonetisimi
term: "Veri yönetişimi"
en: "data governance"
definition: "Veriyle ilgili kararları kimin verdiğini ve hangi kuralların geçerli olduğunu belirleyen düzen."
see_also: [ana-veri]
cards: [kb-ea-8-1-master-data-governance]
```

## Veri kalitesi

```yaml
id: veri-kalitesi
term: "Veri kalitesi"
en: "data quality"
definition: "Verinin doğruluk, tamlık, tutarlılık ve güncellik bakımından kullanıma uygunluğu."
see_also: [ana-veri]
cards: [kb-ea-8-2-data-quality-field]
```

## Ana veri yönetimi (MDM)

```yaml
id: mdm
term: "Ana veri yönetimi (MDM)"
en: "master data management"
definition: "Ana verinin tek, temiz ve tutarlı tutulması için süreç ve sistemler."
see_also: [ana-veri]
cards: [kb-ea-8-3-mdm-matching-duplicates]
```

## GTIN

```yaml
id: gtin
term: "GTIN"
en: "Global Trade Item Number"
definition: "Ticari ürünleri küresel olarak tanımlayan GS1 numarası."
see_also: []
cards: [kb-ea-11-4-edi-with-chains, kb-ea-30-4-barcodes-traceability, kb-ea-8-4-gs1-barcodes-pim]
```

## Veri ambarı

```yaml
id: veri-ambari
term: "Veri ambarı"
en: "data warehouse"
definition: "Farklı kaynaklardan verileri tarihçesiyle toplayıp analiz için düzenleyen ayrı veritabanı."
see_also: []
cards: [kb-ea-9-1-reporting-vs-transaction-systems, kb-ea-9-2-sell-in-sell-out-reporting]
```

## Sell-in

```yaml
id: sell-in
term: "Sell-in"
en: "sell-in"
definition: "Üreticinin dağıtıcıya yaptığı satış."
see_also: [sell-out]
cards: [kb-ea-9-2-sell-in-sell-out-reporting]
```

## Sell-out

```yaml
id: sell-out
term: "Sell-out"
en: "sell-out"
definition: "Dağıtıcının noktalara ya da perakendecinin tüketiciye yaptığı satış."
see_also: [sell-in]
cards: [kb-ea-9-2-sell-in-sell-out-reporting]
```

## KPI (temel performans göstergesi)

```yaml
id: kpi
term: "KPI (temel performans göstergesi)"
en: "key performance indicator"
definition: "Bir hedefe ilerlemeyi ölçen, tanımı ve sahibi belli gösterge."
see_also: []
cards: [kb-ea-9-6-bi-dashboards-kpis]
```

## İş zekâsı

```yaml
id: is-zekasi
term: "İş zekâsı"
en: "business intelligence (BI)"
definition: "Veriyi rapor, pano ve analizle karar desteğine dönüştüren araç ve süreçler."
see_also: [kpi, veri-ambari]
cards: [kb-ea-9-6-bi-dashboards-kpis]
```

## Elektronik veri değişimi (EDI)

```yaml
id: edi
term: "Elektronik veri değişimi (EDI)"
en: "Electronic data interchange"
definition: "Firmalar arasında sipariş, sevk bildirimi ve fatura gibi belgelerin standart biçimde, sistemden sisteme otomatik alışverişi."
see_also: [entegrasyon, gtin]
cards: [kb-ea-11-4-edi-with-chains]
```

## e-Arşiv Fatura

```yaml
id: e-arsiv-fatura
term: "e-Arşiv Fatura"
en: "e-Archive invoice"
definition: "e-Fatura sistemine kayıtlı olmayan alıcılara elektronik ortamda düzenlenen fatura."
see_also: [e-fatura]
cards: [kb-ea-37-1-e-document-map, kb-ea-26-5-van-sales-presales]
```

## e-Defter

```yaml
id: e-defter
term: "e-Defter"
en: "e-Ledger"
definition: "Yasal defterlerin elektronik ortamda tutulması ve beratlarının alınması."
see_also: [e-fatura]
cards: [kb-ea-37-1-e-document-map]
```

## API (uygulama programlama arayüzü)

```yaml
id: api
term: "API (uygulama programlama arayüzü)"
en: "Application programming interface"
definition: "Bir sistemin diğer sistemlere hangi veriyi hangi kurallarla sunduğunu tanımlayan programlanabilir arayüz."
see_also: [entegrasyon, webhook]
cards: [kb-ea-11-6-apis-for-managers]
```

## Webhook

```yaml
id: webhook
term: "Webhook"
en: "Webhook"
definition: "Bir olay gerçekleştiğinde bir sistemin diğerine kendiliğinden bildirim göndermesi."
see_also: [api]
cards: [kb-ea-11-6-apis-for-managers]
```

## RPO (kurtarma noktası hedefi)

```yaml
id: rpo
term: "RPO (kurtarma noktası hedefi)"
en: "Recovery point objective"
definition: "Bir kesintide göze alınabilecek en fazla veri kaybı süresi."
see_also: [rto]
cards: [kb-ea-14-4-backup-disaster-recovery]
```

## RTO (kurtarma süresi hedefi)

```yaml
id: rto
term: "RTO (kurtarma süresi hedefi)"
en: "Recovery time objective"
definition: "Bir kesintiden sonra sistemin en geç yeniden çalışır hale gelmesi gereken süre."
see_also: [rpo]
cards: [kb-ea-14-4-backup-disaster-recovery]
```

## Rol tabanlı erişim denetimi (RBAC)

```yaml
id: rbac
term: "Rol tabanlı erişim denetimi (RBAC)"
en: "Role-based access control"
definition: "Yetkilerin kişilere değil rollere verildiği, kişilere rol atandığı erişim yönetimi."
see_also: [en-az-yetki, gorevler-ayriligi]
cards: [kb-ea-15-2-user-roles-permissions]
```

## En az yetki ilkesi

```yaml
id: en-az-yetki
term: "En az yetki ilkesi"
en: "Principle of least privilege"
definition: "Her kullanıcının yalnızca işini yapmaya yetecek kadar erişime sahip olması."
see_also: [rbac]
cards: [kb-ea-15-2-user-roles-permissions]
```

## KVKK

```yaml
id: kvkk
term: "KVKK"
en: "Turkish Personal Data Protection Law"
definition: "6698 sayılı Kişisel Verilerin Korunması Kanunu ve bu kanunla kurulan kurum."
see_also: [acik-riza, aydinlatma-yukumlulugu]
cards: [kb-ea-15-5-kvkk-basics, kb-ea-25-4-consent-iys-marketing]
```

## Açık rıza

```yaml
id: acik-riza
term: "Açık rıza"
en: "Explicit consent"
definition: "Belirli bir konuya ilişkin, bilgilendirilmeye dayanan ve özgür iradeyle açıklanan onay."
see_also: [kvkk]
cards: [kb-ea-15-5-kvkk-basics, kb-ea-25-4-consent-iys-marketing]
```

## Aydınlatma yükümlülüğü

```yaml
id: aydinlatma-yukumlulugu
term: "Aydınlatma yükümlülüğü"
en: "Duty to inform"
definition: "Kişisel veri işlenirken veri sahibine kimin, hangi amaçla, hangi veriyi işlediğinin bildirilmesi."
see_also: [kvkk]
cards: [kb-ea-15-5-kvkk-basics]
```

## Bulut bilişim

```yaml
id: bulut-bilisim
term: "Bulut bilişim"
en: "Cloud computing"
definition: "Ağ üzerinden, ihtiyaç anında, paylaşılan ve ölçülen bilişim kaynaklarının kullanılması."
see_also: [saas]
cards: [kb-ea-16-5-cloud-cost-data-residency, kb-ea-16-1-cloud-saas-basics]
```

## FinOps

```yaml
id: finops
term: "FinOps"
en: "FinOps"
definition: "Bulut maliyetini finans, BT ve iş birimlerinin birlikte görünür kılıp yönettiği disiplin."
see_also: [bulut-bilisim]
cards: [kb-ea-16-5-cloud-cost-data-residency]
```

## Veri konumu

```yaml
id: veri-konumu
term: "Veri konumu"
en: "Data residency"
definition: "Verinin fiziksel olarak hangi ülke veya bölgede saklandığı."
see_also: [kvkk, bulut-bilisim]
cards: [kb-ea-16-5-cloud-cost-data-residency]
```

## Uyum–boşluk analizi

```yaml
id: uyum-bosluk-analizi
term: "Uyum–boşluk analizi"
en: "Fit-gap analysis"
definition: "Süreç adımlarının bir yazılım paketince standart olarak karşılanıp karşılanmadığının tek tek işaretlenmesi."
see_also: [ozellestirme-borcu]
cards: [kb-ea-17-1-build-buy-configure, kb-ea-18-5-implementation-methodology]
```

## Özelleştirme borcu

```yaml
id: ozellestirme-borcu
term: "Özelleştirme borcu"
en: "Customisation debt"
definition: "Paket yazılıma yapılan özelleştirmelerin sürüm yükseltmelerinde yarattığı ek test ve bakım yükü."
see_also: [uyum-bosluk-analizi]
cards: [kb-ea-17-1-build-buy-configure]
```

## Kullanıcı hikâyesi

```yaml
id: kullanici-hikayesi
term: "Kullanıcı hikâyesi"
en: "User story"
definition: "Bir ihtiyacın “rol, amaç, istek” kalıbında kısa anlatımı."
see_also: [kabul-kriteri]
cards: [kb-ea-17-3-writing-requirements]
```

## Kabul kriteri

```yaml
id: kabul-kriteri
term: "Kabul kriteri"
en: "Acceptance criterion"
definition: "Bir ihtiyacın karşılanıp karşılanmadığını ölçülebilir biçimde gösteren koşul."
see_also: [kullanici-hikayesi]
cards: [kb-ea-17-3-writing-requirements]
```

## MoSCoW önceliklendirmesi

```yaml
id: moscow
term: "MoSCoW önceliklendirmesi"
en: "MoSCoW prioritisation"
definition: "İhtiyaçları olmazsa olmaz, olmalı, olabilir ve bu sefer değil olarak ayıran yöntem."
see_also: [kabul-kriteri]
cards: [kb-ea-17-3-writing-requirements]
```

## Teklife çağrı dokümanı (RFP)

```yaml
id: rfp
term: "Teklife çağrı dokümanı (RFP)"
en: "Request for proposal"
definition: "Tedarikçilerden ihtiyaçlara göre yapılandırılmış çözüm ve fiyat teklifi istemek için hazırlanan doküman."
see_also: [kritik-basari-faktoru]
cards: [kb-ea-17-4-vendor-selection-rfp]
```

## Kritik başarı faktörü

```yaml
id: kritik-basari-faktoru
term: "Kritik başarı faktörü"
en: "Critical success factor"
definition: "Bir projenin veya seçimin başarılı sayılması için mutlaka karşılanması gereken koşul."
see_also: [rfp]
cards: [kb-ea-18-3-why-erp-projects-fail]
```

## Canlıya geçiş

```yaml
id: canliya-gecis
term: "Canlıya geçiş"
en: "Go-live"
definition: "Yeni sistemin gerçek işlemler için kullanılmaya başlandığı an ve bu ana hazırlık süreci."
see_also: [veri-tasima]
cards: [kb-ea-18-4-post-go-live-dip, kb-ea-18-5-implementation-methodology]
```

## Veri taşıma

```yaml
id: veri-tasima
term: "Veri taşıma"
en: "Data migration"
definition: "Eski sistemdeki ana veri ve açık bakiyelerin temizlenip yeni sisteme aktarılması."
see_also: [acilis-bakiyesi, mutabakat]
cards: [kb-ea-18-6-data-migration-opening-balances]
```

## Açılış bakiyesi

```yaml
id: acilis-bakiyesi
term: "Açılış bakiyesi"
en: "Opening balance"
definition: "Yeni sistemde canlıya geçiş tarihi itibarıyla girilen stok, cari ve hesap bakiyeleri."
see_also: [veri-tasima]
cards: [kb-ea-18-6-data-migration-opening-balances]
```

## Mutabakat

```yaml
id: mutabakat
term: "Mutabakat"
en: "Reconciliation"
definition: "İki kaynak arasındaki bakiye veya kayıtların karşılaştırılıp farkların açıklanması."
see_also: [acilis-bakiyesi]
cards: [kb-ea-20-4-record-to-report-close, kb-ea-18-6-data-migration-opening-balances]
```

## Kilit kullanıcı

```yaml
id: kilit-kullanici
term: "Kilit kullanıcı"
en: "Key user"
definition: "Kendi bölümünde yeni sistemi en iyi bilen, test eden ve diğer kullanıcıları eğiten kişi."
see_also: [degisim-yonetimi]
cards: [kb-ea-18-7-change-management-training]
```

## Değişim yönetimi

```yaml
id: degisim-yonetimi
term: "Değişim yönetimi"
en: "Change management"
definition: "İnsanların yeni süreç ve sistemi benimsemesi için yapılan iletişim, eğitim ve destek çalışmaları."
see_also: [kilit-kullanici]
cards: [kb-ea-18-7-change-management-training]
```

## Kazanılmış değer

```yaml
id: kazanilmis-deger
term: "Kazanılmış değer"
en: "Earned value"
definition: "Tamamlanan işin planlanan bütçe üzerinden değeri; maliyet ve takvim performansını ölçmekte kullanılır."
see_also: [risk-kaydi]
cards: [kb-ea-19-1-project-management-basics]
```

## Risk kaydı

```yaml
id: risk-kaydi
term: "Risk kaydı"
en: "Risk register"
definition: "Proje risklerinin olasılık, etki, sahip ve önlemleriyle tutulduğu liste."
see_also: [kazanilmis-deger]
cards: [kb-ea-19-1-project-management-basics]
```

## Uygulama yönetim hizmeti (AMS)

```yaml
id: ams
term: "Uygulama yönetim hizmeti (AMS)"
en: "Application management services"
definition: "Bir yazılımın bakım, hata çözümü ve küçük geliştirmelerinin dış bir firmaya sözleşmeyle verilmesi."
see_also: [sla]
cards: [kb-ea-19-3-working-with-it-partners]
```

## Organizasyon yapısı (ERP)

```yaml
id: organizasyon-yapisi
term: "Organizasyon yapısı (ERP)"
en: "Organizational structure"
definition: "ERP'de şirket, tesis, depo, satış organizasyonu gibi raporlama ve yetkiyi belirleyen birimler."
see_also: [erp]
cards: [kb-ea-20-1-what-erp-does]
```

## Üçlü eşleştirme

```yaml
id: uclu-eslestirme
term: "Üçlü eşleştirme"
en: "Three-way match"
definition: "Satın alma siparişi, mal kabul ve faturanın miktar ve fiyatta karşılaştırılması."
see_also: [satinalma-siparisi, gorevler-ayriligi]
cards: [kb-ea-20-3-procure-to-pay]
```

## Satın alma siparişi

```yaml
id: satinalma-siparisi
term: "Satın alma siparişi"
en: "Purchase order"
definition: "Tedarikçiye verilen, ürün, miktar, fiyat ve teslim koşullarını içeren onaylı sipariş belgesi."
see_also: [uclu-eslestirme]
cards: [kb-ea-20-3-procure-to-pay]
```

## Genel muhasebe

```yaml
id: genel-muhasebe
term: "Genel muhasebe"
en: "General ledger"
definition: "Tüm mali hareketlerin hesap planına göre toplandığı ana defter."
see_also: [ay-sonu-kapanisi]
cards: [kb-ea-20-4-record-to-report-close, kb-ea-22-1-chart-of-accounts-tekduzen]
```

## Ay sonu kapanışı

```yaml
id: ay-sonu-kapanisi
term: "Ay sonu kapanışı"
en: "Month-end close"
definition: "Dönem kayıtlarının tamamlanıp mutabakat, tahakkuk ve değerlemeyle raporlamaya hazır hale getirilmesi."
see_also: [genel-muhasebe, mutabakat]
cards: [kb-ea-20-4-record-to-report-close]
```

## Hareketli ortalama maliyet

```yaml
id: hareketli-ortalama-maliyet
term: "Hareketli ortalama maliyet"
en: "Moving average cost"
definition: "Her girişten sonra toplam stok değerinin toplam miktara bölünmesiyle güncellenen birim maliyet."
see_also: [standart-maliyet]
cards: [kb-ea-20-5-inventory-in-erp]
```

## Standart maliyet

```yaml
id: standart-maliyet
term: "Standart maliyet"
en: "Standard cost"
definition: "Dönem başında belirlenen sabit birim maliyet; gerçek maliyetle fark ayrı hesapta izlenir."
see_also: [hareketli-ortalama-maliyet]
cards: [kb-ea-20-5-inventory-in-erp]
```

## Hareket tipi

```yaml
id: hareket-tipi
term: "Hareket tipi"
en: "Movement type"
definition: "ERP'de bir stok hareketinin türünü ve muhasebe etkisini belirleyen kod."
see_also: [hareketli-ortalama-maliyet]
cards: [kb-ea-20-5-inventory-in-erp]
```

## Malzeme ihtiyaç planlaması (MRP)

```yaml
id: mrp
term: "Malzeme ihtiyaç planlaması (MRP)"
en: "Material requirements planning"
definition: "Üretim planı, ürün ağacı ve stoktan malzeme ihtiyacını ve sipariş zamanını hesaplayan yöntem."
see_also: [urun-agaci, ana-uretim-plani, temin-suresi]
cards: [kb-ea-20-6-mrp-basics]
```

## Ürün ağacı

```yaml
id: urun-agaci
term: "Ürün ağacı"
en: "Bill of materials"
definition: "Bir ürünün hangi bileşenlerden hangi miktarlarda oluştuğunu gösteren yapı."
see_also: [mrp]
cards: [kb-ea-20-6-mrp-basics]
```

## Ana üretim planı

```yaml
id: ana-uretim-plani
term: "Ana üretim planı"
en: "Master production schedule"
definition: "Hangi bitmiş üründen hangi dönemde ne kadar üretileceğini gösteren plan."
see_also: [mrp]
cards: [kb-ea-20-6-mrp-basics]
```

## Temin süresi

```yaml
id: temin-suresi
term: "Temin süresi"
en: "Lead time"
definition: "Siparişin verilmesinden malzemenin kullanıma hazır olmasına kadar geçen süre."
see_also: [mrp]
cards: [kb-ea-20-6-mrp-basics]
```

## Yerelleştirme (ERP)

```yaml
id: yerellestirme
term: "Yerelleştirme (ERP)"
en: "Localisation"
definition: "Bir yazılımın ülkenin hesap planı, vergi, e-belge ve bordro mevzuatına uyarlanması."
see_also: [erp]
cards: [kb-ea-21-3-erp-market-turkey]
```

## Tekdüzen hesap planı

```yaml
id: tekduzen-hesap-plani
term: "Tekdüzen hesap planı"
en: "Turkish uniform chart of accounts"
definition: "Türkiye'de bilanço esasına göre defter tutan işletmelerin kullandığı standart hesap planı."
see_also: [hesap-eslestirme]
cards: [kb-ea-22-1-chart-of-accounts-tekduzen]
```

## Hesap eşleştirme

```yaml
id: hesap-eslestirme
term: "Hesap eşleştirme"
en: "Account determination"
definition: "ERP'de bir işlem tipinin hangi muhasebe hesaplarına kaydedileceğini belirleyen kurallar."
see_also: [tekduzen-hesap-plani, genel-muhasebe]
cards: [kb-ea-22-1-chart-of-accounts-tekduzen]
```

## Kur farkı

```yaml
id: kur-farki
term: "Kur farkı"
en: "Exchange rate difference"
definition: "Dövizli bir işlemin kayıt ve ödeme ya da değerleme tarihleri arasındaki kur değişiminden doğan fark."
see_also: [kur-riski]
cards: [kb-ea-22-2-multi-currency-inflation-adjust-in-erp]
```

## Paralel defter

```yaml
id: paralel-defter
term: "Paralel defter"
en: "Parallel ledger"
definition: "Aynı işlemlerin farklı muhasebe kurallarına veya para birimlerine göre ayrı defterlerde tutulması."
see_also: [enflasyon-duzeltmesi]
cards: [kb-ea-22-2-multi-currency-inflation-adjust-in-erp]
```

## Enflasyon düzeltmesi

```yaml
id: enflasyon-duzeltmesi
term: "Enflasyon düzeltmesi"
en: "Inflation adjustment"
definition: "Parasal olmayan kalemlerin fiyat endeksiyle yeniden ifade edilerek mali tabloların enflasyon etkisinden arındırılması."
see_also: [paralel-defter]
cards: [kb-ea-22-2-multi-currency-inflation-adjust-in-erp]
```

## Konsolidasyon

```yaml
id: konsolidasyon
term: "Konsolidasyon"
en: "Consolidation"
definition: "Grup şirketlerinin mali tablolarının tek bir ekonomik birim gibi birleştirilmesi."
see_also: [sirketler-arasi-eliminasyon]
cards: [kb-ea-22-3-consolidation-close-systems]
```

## Şirketler arası eliminasyon

```yaml
id: sirketler-arasi-eliminasyon
term: "Şirketler arası eliminasyon"
en: "Intercompany elimination"
definition: "Konsolidasyonda grup içi satış, alacak–borç ve gerçekleşmemiş kârın çıkarılması."
see_also: [konsolidasyon]
cards: [kb-ea-22-3-consolidation-close-systems]
```

## Bütçe payı

```yaml
id: butce-payi
term: "Bütçe payı"
en: "Budgetary slack"
definition: "Yöneticilerin hedefi kolay tutturmak için bütçeye bilinçli olarak koyduğu pay."
see_also: [yonetim-kontrolu]
cards: [kb-ea-23-1-budgeting-purposes-games]
```

## Yönetim kontrolü

```yaml
id: yonetim-kontrolu
term: "Yönetim kontrolü"
en: "Management control"
definition: "Yöneticilerin stratejiyi uygulamak için planlama, ölçme ve yönlendirme araçlarını kullanması."
see_also: [butce-payi, dengeli-karne]
cards: [kb-ea-23-1-budgeting-purposes-games]
```

## Kayan tahmin

```yaml
id: kayan-tahmin
term: "Kayan tahmin"
en: "Rolling forecast"
definition: "Her dönem güncellenen ve hep aynı uzunlukta bir geleceği kapsayan tahmin."
see_also: [surucu-bazli-planlama]
cards: [kb-ea-23-2-rolling-forecast-driver-based]
```

## Sürücü bazlı planlama

```yaml
id: surucu-bazli-planlama
term: "Sürücü bazlı planlama"
en: "Driver-based planning"
definition: "Sonuçların hacim, fiyat, verimlilik gibi birkaç temel sürücüden hesaplandığı planlama yöntemi."
see_also: [kayan-tahmin]
cards: [kb-ea-23-2-rolling-forecast-driver-based]
```

## Sıfır tabanlı bütçe

```yaml
id: sifir-tabanli-butce
term: "Sıfır tabanlı bütçe"
en: "Zero-based budgeting"
definition: "Her gider kaleminin geçen yıla bakılmadan sıfırdan gerekçelendirildiği bütçe yöntemi."
see_also: [kayan-tahmin]
cards: [kb-ea-23-2-rolling-forecast-driver-based]
```

## Dengeli karne

```yaml
id: dengeli-karne
term: "Dengeli karne"
en: "Balanced scorecard"
definition: "Performansı finansal, müşteri, iç süreç ve öğrenme boyutlarında izleyen yönetim aracı."
see_also: [strateji-haritasi, okr]
cards: [kb-ea-23-3-balanced-scorecard-okr]
```

## Strateji haritası

```yaml
id: strateji-haritasi
term: "Strateji haritası"
en: "Strategy map"
definition: "Stratejik hedefler arasındaki neden–sonuç ilişkilerini gösteren şema."
see_also: [dengeli-karne]
cards: [kb-ea-23-3-balanced-scorecard-okr]
```

## Hedefler ve anahtar sonuçlar (OKR)

```yaml
id: okr
term: "Hedefler ve anahtar sonuçlar (OKR)"
en: "Objectives and key results"
definition: "İddialı bir hedef ve onu ölçen birkaç anahtar sonuçla kısa döngülerde çalışan hedef belirleme yöntemi."
see_also: [dengeli-karne]
cards: [kb-ea-23-3-balanced-scorecard-okr]
```

## Nakit pozisyonu

```yaml
id: nakit-pozisyonu
term: "Nakit pozisyonu"
en: "Cash position"
definition: "Belirli bir anda tüm banka ve kasa bakiyeleri ile günün beklenen giriş–çıkışlarının toplam görünümü."
see_also: [nakit-akis-tahmini]
cards: [kb-ea-24-1-treasury-cash-forecasting]
```

## Nakit akış tahmini

```yaml
id: nakit-akis-tahmini
term: "Nakit akış tahmini"
en: "Cash flow forecast"
definition: "Gelecek dönemlerdeki nakit giriş ve çıkışlarının dönem dönem tahmini."
see_also: [nakit-pozisyonu, nakit-donusum-suresi]
cards: [kb-ea-24-1-treasury-cash-forecasting]
```

## Kur riski

```yaml
id: kur-riski
term: "Kur riski"
en: "Foreign exchange risk"
definition: "Döviz kurlarındaki değişimin dövizli alacak, borç ve nakit akışlarının değerini etkileme riski."
see_also: [kur-farki]
cards: [kb-ea-24-1-treasury-cash-forecasting]
```

## Hesap ekstresi

```yaml
id: hesap-ekstresi
term: "Hesap ekstresi"
en: "Bank statement"
definition: "Banka hesabındaki hareketlerin dönemsel dökümü; ERP'ye standart biçimlerle aktarılabilir."
see_also: [otomatik-eslestirme, iso-20022]
cards: [kb-ea-24-2-bank-statement-integration]
```

## ISO 20022

```yaml
id: iso-20022
term: "ISO 20022"
en: "ISO 20022"
definition: "Ödeme, ekstre ve diğer finansal mesajlar için XML tabanlı uluslararası standart."
see_also: [hesap-ekstresi]
cards: [kb-ea-24-2-bank-statement-integration]
```

## Otomatik eşleştirme

```yaml
id: otomatik-eslestirme
term: "Otomatik eşleştirme"
en: "Automatic matching"
definition: "Banka hareketlerinin kurallarla ilgili müşteri, tedarikçi ve faturalara otomatik bağlanması."
see_also: [hesap-ekstresi]
cards: [kb-ea-24-2-bank-statement-integration]
```

## Kredi limiti

```yaml
id: kredi-limiti
term: "Kredi limiti"
en: "Credit limit"
definition: "Bir müşteriye vadeli satışta izin verilen azami açık risk tutarı."
see_also: [dbs, kademeli-hatirlatma]
cards: [kb-ea-24-3-credit-limits-collections-systems]
```

## Doğrudan borçlandırma sistemi (DBS)

```yaml
id: dbs
term: "Doğrudan borçlandırma sistemi (DBS)"
en: "Direct debit system"
definition: "Bayinin bankasının tanımlı limit dahilinde tedarikçiye vadesinde ödeme yapmayı taahhüt ettiği tahsilat yöntemi."
see_also: [kredi-limiti]
cards: [kb-ea-24-3-credit-limits-collections-systems]
```

## Kademeli hatırlatma

```yaml
id: kademeli-hatirlatma
term: "Kademeli hatırlatma"
en: "Dunning"
definition: "Vadesi geçen alacaklar için adım adım artan hatırlatma ve yaptırım süreci."
see_also: [kredi-limiti]
cards: [kb-ea-24-3-credit-limits-collections-systems]
```

## Müşteri ilişkileri yönetimi (CRM)

```yaml
id: crm
term: "Müşteri ilişkileri yönetimi (CRM)"
en: "Customer relationship management"
definition: "Müşterilerle ilişkiyi kârlı ve uzun vadeli yönetmeye yönelik strateji ve bunu destekleyen sistemler."
see_also: [operasyonel-crm, analitik-crm]
cards: [kb-ea-25-1-crm-basics]
```

## Operasyonel CRM

```yaml
id: operasyonel-crm
term: "Operasyonel CRM"
en: "Operational CRM"
definition: "Ziyaret, fırsat, teklif ve talep gibi günlük müşteri işlerini destekleyen CRM bileşeni."
see_also: [crm]
cards: [kb-ea-25-1-crm-basics]
```

## Analitik CRM

```yaml
id: analitik-crm
term: "Analitik CRM"
en: "Analytical CRM"
definition: "Müşteri verisinden segmentasyon, kayıp riski ve fırsat analizi üreten CRM bileşeni."
see_also: [crm]
cards: [kb-ea-25-1-crm-basics]
```

## Müşteri yaşam boyu değeri (CLV)

```yaml
id: musteri-yasam-boyu-degeri
term: "Müşteri yaşam boyu değeri (CLV)"
en: "Customer lifetime value"
definition: "Bir müşterinin gelecekte getireceği marjların bugünkü değeri."
see_also: [elde-tutma-orani]
cards: [kb-ea-25-2-customer-lifetime-value]
```

## Elde tutma oranı

```yaml
id: elde-tutma-orani
term: "Elde tutma oranı"
en: "Retention rate"
definition: "Bir dönemin müşterilerinden sonraki dönemde de alım yapanların oranı."
see_also: [musteri-yasam-boyu-degeri]
cards: [kb-ea-25-2-customer-lifetime-value]
```

## İleti Yönetim Sistemi (İYS)

```yaml
id: iys
term: "İleti Yönetim Sistemi (İYS)"
en: "Message management system"
definition: "Ticari elektronik ileti onay ve retlerinin kaydedildiği ulusal sistem."
see_also: [ticari-elektronik-ileti, kvkk]
cards: [kb-ea-25-4-consent-iys-marketing]
```

## Ticari elektronik ileti

```yaml
id: ticari-elektronik-ileti
term: "Ticari elektronik ileti"
en: "Commercial electronic message"
definition: "Mal ve hizmet tanıtımı amacıyla SMS, e-posta veya arama gibi elektronik yollarla gönderilen ileti."
see_also: [iys]
cards: [kb-ea-25-4-consent-iys-marketing]
```

## Pazarlama otomasyonu

```yaml
id: pazarlama-otomasyonu
term: "Pazarlama otomasyonu"
en: "Marketing automation"
definition: "Kampanyaların segment ve tetikleyicilere göre otomatik yürütülmesini sağlayan sistemler."
see_also: [crm, iys]
cards: [kb-ea-25-4-consent-iys-marketing]
```

## Talep kaydı

```yaml
id: talep-kaydi
term: "Talep kaydı"
en: "Case / ticket"
definition: "Bir müşteri sorusu, şikâyeti veya isteğinin sorumlu, öncelik ve durumla izlendiği kayıt."
see_also: [ilk-temasta-cozum, sla]
cards: [kb-ea-25-5-customer-service-cases]
```

## İlk temasta çözüm

```yaml
id: ilk-temasta-cozum
term: "İlk temasta çözüm"
en: "First contact resolution"
definition: "Talebin müşterinin ilk temasında, ek aktarım veya geri dönüş gerekmeden çözülmesi."
see_also: [talep-kaydi]
cards: [kb-ea-25-5-customer-service-cases]
```

## Rut planı

```yaml
id: rut-plani
term: "Rut planı"
en: "Route plan"
definition: "Satış temsilcisinin hangi noktayı hangi gün ve sıklıkta ziyaret edeceğini gösteren plan."
see_also: [sfa]
cards: [kb-ea-26-1-retail-execution-sfa]
```

## Mükemmel mağaza

```yaml
id: mukemmel-magaza
term: "Mükemmel mağaza"
en: "Perfect store"
definition: "Bir noktada bulunması beklenen ürün, raf, fiyat ve teşhir standartlarının puanlanarak izlenmesi."
see_also: [sfa]
cards: [kb-ea-26-1-retail-execution-sfa]
```

## Nokta ana verisi

```yaml
id: nokta-ana-verisi
term: "Nokta ana verisi"
en: "Outlet master data"
definition: "Satış noktalarının kod, adres, konum, kanal ve sınıf gibi temel bilgileri."
see_also: [rut-plani]
cards: [kb-ea-26-2-field-data-outlet-visit]
```

## Konumla giriş

```yaml
id: konumla-giris
term: "Konumla giriş"
en: "Geo-fenced check-in"
definition: "Ziyaret kaydının cihaz konumunun noktaya belirli bir mesafede olmasıyla doğrulanması."
see_also: [nokta-ana-verisi]
cards: [kb-ea-26-2-field-data-outlet-visit]
```

## Çevrimdışı öncelikli

```yaml
id: cevrimdisi-oncelikli
term: "Çevrimdışı öncelikli"
en: "Offline-first"
definition: "Uygulamanın bağlantı olmadan da çalışacak şekilde tasarlanması; veri sonra eşitlenir."
see_also: [senkronizasyon]
cards: [kb-ea-26-3-offline-mode-for-managers]
```

## Senkronizasyon

```yaml
id: senkronizasyon
term: "Senkronizasyon"
en: "Synchronisation"
definition: "Cihazdaki veri ile merkezi sistem arasındaki karşılıklı veri eşitleme."
see_also: [veri-cakismasi]
cards: [kb-ea-26-3-offline-mode-for-managers]
```

## Veri çakışması

```yaml
id: veri-cakismasi
term: "Veri çakışması"
en: "Data conflict"
definition: "Aynı kaydın iki yerde farklı değiştirilmesi sonucu eşitlemede ortaya çıkan uyuşmazlık."
see_also: [senkronizasyon]
cards: [kb-ea-26-3-offline-mode-for-managers]
```

## Araçlı satış

```yaml
id: aracli-satis
term: "Araçlı satış"
en: "Van sales"
definition: "Satış, teslimat, fatura ve tahsilatın aynı ziyarette araçtaki stoktan yapıldığı model."
see_also: [on-satis, gun-sonu-mutabakati]
cards: [kb-ea-26-5-van-sales-presales]
```

## Ön satış

```yaml
id: on-satis
term: "Ön satış"
en: "Pre-sales"
definition: "Siparişin ziyarette alınıp teslimatın sonradan yapıldığı satış modeli."
see_also: [aracli-satis]
cards: [kb-ea-26-5-van-sales-presales]
```

## Gün sonu mutabakatı

```yaml
id: gun-sonu-mutabakati
term: "Gün sonu mutabakatı"
en: "End-of-day reconciliation"
definition: "Gün sonunda stok ve kasanın sayılarak sistem kayıtlarıyla karşılaştırılması."
see_also: [aracli-satis, z-raporu]
cards: [kb-ea-26-5-van-sales-presales]
```

## Distribütör yönetim sistemi (DMS)

```yaml
id: dms
term: "Distribütör yönetim sistemi (DMS)"
en: "Distributor management system"
definition: "Distribütörün satış, stok ve tahsilat işlerini yürüten ve üreticiyle veri paylaşan sistem."
see_also: [ikincil-satis]
cards: [kb-ea-26-6-dms-secondary-sales]
```

## İkincil satış

```yaml
id: ikincil-satis
term: "İkincil satış"
en: "Secondary sales / sell-out"
definition: "Distribütörden perakende noktalarına yapılan satış."
see_also: [birincil-satis, dms]
cards: [kb-ea-26-6-dms-secondary-sales]
```

## Birincil satış

```yaml
id: birincil-satis
term: "Birincil satış"
en: "Primary sales / sell-in"
definition: "Üreticiden distribütöre yapılan satış."
see_also: [ikincil-satis]
cards: [kb-ea-26-6-dms-secondary-sales]
```

## Koşul tekniği

```yaml
id: kosul-teknigi
term: "Koşul tekniği"
en: "Condition technique"
definition: "Fiyat ve iskontoların koşul kayıtları olarak tanımlanıp bir şemada sırayla uygulandığı yöntem."
see_also: [erisim-sirasi]
cards: [kb-ea-27-1-pricing-engine-conditions]
```

## Erişim sırası

```yaml
id: erisim-sirasi
term: "Erişim sırası"
en: "Access sequence"
definition: "Sistemin bir koşul kaydını hangi anahtarlarla ve hangi öncelikle arayacağını belirleyen sıra."
see_also: [kosul-teknigi]
cards: [kb-ea-27-1-pricing-engine-conditions]
```

## Fiyat şelalesi

```yaml
id: fiyat-selalesi
term: "Fiyat şelalesi"
en: "Price waterfall"
definition: "Liste fiyatından tüm indirimler düşülerek cebe kalan fiyata ulaşan döküm."
see_also: [cep-fiyati]
cards: [kb-ea-27-1-pricing-engine-conditions]
```

## Cebe kalan fiyat

```yaml
id: cep-fiyati
term: "Cebe kalan fiyat"
en: "Pocket price"
definition: "Fatura dışı indirimler dahil tüm indirimlerden sonra satıcıya kalan fiyat."
see_also: [fiyat-selalesi]
cards: [kb-ea-27-1-pricing-engine-conditions]
```

## Ticari promosyon yönetimi (TPM)

```yaml
id: tpm
term: "Ticari promosyon yönetimi (TPM)"
en: "Trade promotion management"
definition: "Promosyonların planlama, bütçe, tahakkuk, mahsuplaşma ve değerlendirmesini yöneten sistem ve süreç."
see_also: [promosyon-tahakkuku, mahsuplasma]
cards: [kb-ea-27-2-tpm-promotion-settlement]
```

## Promosyon tahakkuku

```yaml
id: promosyon-tahakkuku
term: "Promosyon tahakkuku"
en: "Promotion accrual"
definition: "Promosyon maliyetinin satış gerçekleştikçe fatura beklenmeden gider olarak kaydedilmesi."
see_also: [tpm]
cards: [kb-ea-27-2-tpm-promotion-settlement]
```

## Mahsuplaşma (promosyon)

```yaml
id: mahsuplasma
term: "Mahsuplaşma (promosyon)"
en: "Claim settlement"
definition: "Müşterinin promosyon talebinin tahakkukla karşılaştırılıp kapatılması."
see_also: [tpm]
cards: [kb-ea-27-2-tpm-promotion-settlement]
```

## Sipariş yönetimi

```yaml
id: siparis-yonetimi
term: "Sipariş yönetimi"
en: "Order management"
definition: "Farklı kanallardan gelen siparişlerin kontrol, rezervasyon, tahsis ve sevk sürecinin yönetimi."
see_also: [satilabilir-stok]
cards: [kb-ea-28-1-order-management]
```

## Satılabilir stok (ATP)

```yaml
id: satilabilir-stok
term: "Satılabilir stok (ATP)"
en: "Available to promise"
definition: "Eldeki stoktan rezerve edilmiş miktar düşülerek bulunan, yeni siparişe söz verilebilecek miktar."
see_also: [stok-rezervasyonu]
cards: [kb-ea-28-1-order-management]
```

## Stok rezervasyonu

```yaml
id: stok-rezervasyonu
term: "Stok rezervasyonu"
en: "Stock reservation"
definition: "Onaylanan sipariş için stoğun ayrılarak başka siparişlere kapatılması."
see_also: [satilabilir-stok]
cards: [kb-ea-28-1-order-management]
```

## B2B sipariş portalı

```yaml
id: b2b-portal
term: "B2B sipariş portalı"
en: "B2B ordering portal"
definition: "Bayi ve noktaların sipariş, fatura ve ödeme işlerini kendileri yaptığı web veya mobil kanal."
see_also: [self-servis]
cards: [kb-ea-28-2-b2b-ordering-portals]
```

## Self servis

```yaml
id: self-servis
term: "Self servis"
en: "Self-service"
definition: "Müşterinin işlemini temsilci aracılığı olmadan kendisinin yapması."
see_also: [b2b-portal]
cards: [kb-ea-28-2-b2b-ordering-portals]
```

## Ödeme kaydedici cihaz (ÖKC)

```yaml
id: okc
term: "Ödeme kaydedici cihaz (ÖKC)"
en: "Fiscal cash register"
definition: "Perakende satışlarda mali belge üreten ve kayıtları mali hafızada tutan yeni nesil yazar kasa."
see_also: [z-raporu, kasa-yazilimi]
cards: [kb-ea-28-3-pos-okc]
```

## Z raporu

```yaml
id: z-raporu
term: "Z raporu"
en: "Z report"
definition: "ÖKC'den gün sonunda alınan, günün mali satış toplamlarını gösteren rapor."
see_also: [okc]
cards: [kb-ea-28-3-pos-okc]
```

## Kasa yazılımı

```yaml
id: kasa-yazilimi
term: "Kasa yazılımı"
en: "POS software"
definition: "Mağazada ürün, fiyat, kampanya ve satış ekranını yöneten yazılım."
see_also: [okc]
cards: [kb-ea-28-3-pos-okc]
```

## Sanal POS

```yaml
id: sanal-pos
term: "Sanal POS"
en: "Virtual POS"
definition: "İnternet veya uzaktan kartla ödeme almayı sağlayan banka ya da ödeme kuruluşu altyapısı."
see_also: [valor, pci-dss]
cards: [kb-ea-28-4-card-virtual-pos]
```

## Valör

```yaml
id: valor
term: "Valör"
en: "Value date"
definition: "Bir tahsilatın hesaba geçerek kullanılabilir hale geldiği tarih."
see_also: [sanal-pos]
cards: [kb-ea-28-4-card-virtual-pos]
```

## PCI DSS

```yaml
id: pci-dss
term: "PCI DSS"
en: "Payment Card Industry Data Security Standard"
definition: "Kart verisini işleyen sistemler için PCI Güvenlik Standartları Konseyi'nin güvenlik standardı."
see_also: [sanal-pos]
cards: [kb-ea-28-4-card-virtual-pos]
```

## Talep planlama

```yaml
id: talep-planlama
term: "Talep planlama"
en: "Demand planning"
definition: "İstatistiksel tahmin ile pazar bilgisini birleştirerek uzlaşılmış talep rakamı üreten süreç."
see_also: [mape, tahmin-katma-degeri]
cards: [kb-ea-29-2-demand-planning-systems]
```

## MAPE

```yaml
id: mape
term: "MAPE"
en: "Mean absolute percentage error"
definition: "Tahmin ile gerçekleşen arasındaki mutlak farkın gerçekleşene oranının ortalaması."
see_also: [talep-planlama]
cards: [kb-ea-29-2-demand-planning-systems]
```

## Tahmin katma değeri (FVA)

```yaml
id: tahmin-katma-degeri
term: "Tahmin katma değeri (FVA)"
en: "Forecast value added"
definition: "Bir tahmin adımının hatayı basit bir yönteme göre ne kadar azalttığını gösteren ölçü."
see_also: [mape]
cards: [kb-ea-29-2-demand-planning-systems]
```

## Dağıtım ihtiyaç planlaması (DRP)

```yaml
id: drp
term: "Dağıtım ihtiyaç planlaması (DRP)"
en: "Distribution requirements planning"
definition: "Depolar için talep, stok ve planlı girişlerden ikmal ihtiyacını zamana yayarak hesaplayan yöntem."
see_also: [emniyet-stogu, tedarik-suresi]
cards: [kb-ea-29-3-drp-inventory-planning]
```

## Emniyet stoğu

```yaml
id: emniyet-stogu
term: "Emniyet stoğu"
en: "Safety stock"
definition: "Talep ve tedarik belirsizliğine karşı tutulan ek stok."
see_also: [drp]
cards: [kb-ea-29-3-drp-inventory-planning]
```

## Tedarik süresi

```yaml
id: tedarik-suresi
term: "Tedarik süresi"
en: "Lead time"
definition: "Sipariş verilmesi ile malın teslim alınması arasındaki süre."
see_also: [drp]
cards: [kb-ea-29-3-drp-inventory-planning]
```

## Toplama doğruluğu

```yaml
id: toplama-dogrulugu
term: "Toplama doğruluğu"
en: "Picking accuracy"
definition: "Hatasız toplanan sipariş satırlarının toplam satırlara oranı."
see_also: [zamaninda-sevk]
cards: [kb-ea-30-1-warehouse-operations-kpis]
```

## Zamanında sevk

```yaml
id: zamaninda-sevk
term: "Zamanında sevk"
en: "On-time shipment"
definition: "Söz verilen zamanda depodan çıkan siparişlerin oranı."
see_also: [toplama-dogrulugu]
cards: [kb-ea-30-1-warehouse-operations-kpis]
```

## Yerleşim (slotting)

```yaml
id: slotting
term: "Yerleşim (slotting)"
en: "Slotting"
definition: "Ürünlerin depoda hangi lokasyonda duracağının hareket sıklığına göre belirlenmesi."
see_also: [abc-analizi]
cards: [kb-ea-30-2-slotting-picking]
```

## ABC analizi

```yaml
id: abc-analizi
term: "ABC analizi"
en: "ABC analysis"
definition: "Ürünlerin önem veya hareket sıklığına göre A, B ve C gruplarına ayrılması."
see_also: [slotting]
cards: [kb-ea-30-2-slotting-picking]
```

## Toplu toplama

```yaml
id: toplu-toplama
term: "Toplu toplama"
en: "Batch picking"
definition: "Birden fazla siparişin birlikte toplanıp sonra ayrıştırılması."
see_also: [slotting]
cards: [kb-ea-30-2-slotting-picking]
```

## Depo yönetim sistemi (WMS)

```yaml
id: wms
term: "Depo yönetim sistemi (WMS)"
en: "Warehouse management system"
definition: "Depo içindeki lokasyon bazlı stok ve görevleri yöneten sistem."
see_also: [el-terminali, dalga-planlama]
cards: [kb-ea-30-3-wms-what-it-does]
```

## El terminali

```yaml
id: el-terminali
term: "El terminali"
en: "Handheld terminal"
definition: "Depo çalışanlarının barkod okutup görev aldığı taşınabilir cihaz."
see_also: [wms]
cards: [kb-ea-30-3-wms-what-it-does]
```

## Dalga planlama

```yaml
id: dalga-planlama
term: "Dalga planlama"
en: "Wave planning"
definition: "Siparişlerin sevk saati ve araca göre gruplanarak toplamaya bırakılması."
see_also: [wms]
cards: [kb-ea-30-3-wms-what-it-does]
```

## SSCC

```yaml
id: sscc
term: "SSCC"
en: "Serial Shipping Container Code"
definition: "Palet gibi lojistik birimlerin GS1 standardındaki tekil numarası."
see_also: [gtin]
cards: [kb-ea-30-4-barcodes-traceability]
```

## İzlenebilirlik

```yaml
id: izlenebilirlik
term: "İzlenebilirlik"
en: "Traceability"
definition: "Bir partinin nereden geldiğinin ve nereye gittiğinin kayıtlarla gösterilebilmesi."
see_also: [parti-takibi, geri-cagirma]
cards: [kb-ea-30-4-barcodes-traceability, kb-ea-32-2-food-safety-traceability]
```

## Taşıma yönetim sistemi (TMS)

```yaml
id: tms
term: "Taşıma yönetim sistemi (TMS)"
en: "Transportation management system"
definition: "Sevkiyatların araçlara atanmasını, maliyetini ve teslimat durumunu yöneten sistem."
see_also: [telematik]
cards: [kb-ea-31-1-tms-fleet-telematics]
```

## Telematik

```yaml
id: telematik
term: "Telematik"
en: "Telematics"
definition: "Araçtan konum, hız, yakıt ve motor verisinin uzaktan toplanması."
see_also: [tms]
cards: [kb-ea-31-1-tms-fleet-telematics]
```

## Elektronik teslimat kanıtı

```yaml
id: teslimat-kaniti
term: "Elektronik teslimat kanıtı"
en: "Electronic proof of delivery"
definition: "Teslimatın zamanını, yerini ve alıcısını elektronik olarak kayda geçiren kayıt."
see_also: [tms]
cards: [kb-ea-31-1-tms-fleet-telematics]
```

## Rota optimizasyonu

```yaml
id: rota-optimizasyonu
term: "Rota optimizasyonu"
en: "Route optimisation"
definition: "Kısıtlar altında toplam mesafe veya süreyi azaltan rotanın hesaplanması."
see_also: [zaman-penceresi]
cards: [kb-ea-31-3-route-planning-sales-vs-delivery]
```

## Zaman penceresi

```yaml
id: zaman-penceresi
term: "Zaman penceresi"
en: "Time window"
definition: "Müşterinin teslimat kabul ettiği saat aralığı."
see_also: [rota-optimizasyonu]
cards: [kb-ea-31-3-route-planning-sales-vs-delivery]
```

## Üretim yürütme sistemi (MES)

```yaml
id: mes
term: "Üretim yürütme sistemi (MES)"
en: "Manufacturing execution system"
definition: "Üretim hattındaki gerçekleşmeyi anlık izleyen ve ERP ile bağlantılı çalışan sistem."
see_also: [oee]
cards: [kb-ea-32-1-mes-oee]
```

## Toplam ekipman etkinliği (OEE)

```yaml
id: oee
term: "Toplam ekipman etkinliği (OEE)"
en: "Overall equipment effectiveness"
definition: "Kullanılabilirlik, performans ve kalite oranlarının çarpımıyla bulunan verimlilik göstergesi."
see_also: [mes]
cards: [kb-ea-32-1-mes-oee]
```

## Geri çağırma

```yaml
id: geri-cagirma
term: "Geri çağırma"
en: "Product recall"
definition: "Sorunlu ürünün piyasadan ve müşterilerden toplanması süreci."
see_also: [izlenebilirlik]
cards: [kb-ea-32-2-food-safety-traceability]
```

## Parti takibi

```yaml
id: parti-takibi
term: "Parti takibi"
en: "Lot tracking"
definition: "Ürünlerin üretim partisi numarasıyla tüm hareketlerde izlenmesi."
see_also: [izlenebilirlik]
cards: [kb-ea-32-2-food-safety-traceability]
```

## Planlı bakım

```yaml
id: planli-bakim
term: "Planlı bakım"
en: "Preventive maintenance"
definition: "Arıza beklenmeden takvime veya kullanıma göre yapılan bakım."
see_also: [mtbf, mttr]
cards: [kb-ea-32-4-asset-maintenance]
```

## MTBF

```yaml
id: mtbf
term: "MTBF"
en: "Mean time between failures"
definition: "Arızalar arasındaki ortalama çalışma süresi."
see_also: [mttr]
cards: [kb-ea-32-4-asset-maintenance]
```

## MTTR

```yaml
id: mttr
term: "MTTR"
en: "Mean time to repair"
definition: "Bir arızanın ortalama onarım süresi."
see_also: [mtbf]
cards: [kb-ea-32-4-asset-maintenance]
```

## Personel ana verisi

```yaml
id: personel-ana-verisi
term: "Personel ana verisi"
en: "Employee master data"
definition: "Çalışanın kimlik, pozisyon, departman ve ücret gibi temel bilgileri."
see_also: [puantaj]
cards: [kb-ea-33-1-hr-systems]
```

## Puantaj

```yaml
id: puantaj
term: "Puantaj"
en: "Time and attendance"
definition: "Çalışanların devam, izin ve fazla mesai kayıtları."
see_also: [personel-ana-verisi]
cards: [kb-ea-33-1-hr-systems]
```

## Brüt ücret

```yaml
id: brut-ucret
term: "Brüt ücret"
en: "Gross pay"
definition: "Kesintilerden önceki ücret tutarı."
see_also: [net-ucret]
cards: [kb-ea-33-2-payroll-basics]
```

## Net ücret

```yaml
id: net-ucret
term: "Net ücret"
en: "Net pay"
definition: "Kesintiler düşüldükten sonra çalışana ödenen tutar."
see_also: [brut-ucret]
cards: [kb-ea-33-2-payroll-basics]
```

## Bordro parametresi

```yaml
id: bordro-parametresi
term: "Bordro parametresi"
en: "Payroll parameter"
definition: "Bordro hesabında kullanılan ve mevzuatla değişen oran, tavan ve istisna değerleri."
see_also: [brut-ucret]
cards: [kb-ea-33-2-payroll-basics]
```

## Prim planı

```yaml
id: prim-plani
term: "Prim planı"
en: "Incentive plan"
definition: "Satış primini belirleyen ölçü, ağırlık, hedef ve ödeme eğrisinin bütünü."
see_also: [odeme-egrisi]
cards: [kb-ea-33-3-incentive-compensation-systems]
```

## Ödeme eğrisi

```yaml
id: odeme-egrisi
term: "Ödeme eğrisi"
en: "Payout curve"
definition: "Hedef gerçekleşme oranına göre ödenecek primi gösteren kural."
see_also: [prim-plani]
cards: [kb-ea-33-3-incentive-compensation-systems]
```

## Satın alma talebi

```yaml
id: satin-alma-talebi
term: "Satın alma talebi"
en: "Purchase requisition"
definition: "Bir birimin ihtiyacını satın almaya ilettiği iç belge."
see_also: [tedarikci-performansi]
cards: [kb-ea-34-1-purchasing-supplier-management]
```

## Tedarikçi performansı

```yaml
id: tedarikci-performansi
term: "Tedarikçi performansı"
en: "Supplier performance"
definition: "Tedarikçinin teslim, kalite ve fiyat uyumu gibi kriterlerle ölçülmesi."
see_also: [satin-alma-talebi]
cards: [kb-ea-34-1-purchasing-supplier-management]
```

## Saklama süresi

```yaml
id: saklama-suresi
term: "Saklama süresi"
en: "Retention period"
definition: "Bir belge türünün mevzuat veya politika gereği saklanması gereken süre."
see_also: [imha-politikasi]
cards: [kb-ea-35-1-document-archive-retention]
```

## Üst veri

```yaml
id: ust-veri
term: "Üst veri"
en: "Metadata"
definition: "Bir belgeyi tanımlayan tür, tarih, karşı taraf gibi bilgiler."
see_also: [saklama-suresi]
cards: [kb-ea-35-1-document-archive-retention]
```

## İmha politikası

```yaml
id: imha-politikasi
term: "İmha politikası"
en: "Disposal policy"
definition: "Süresi dolan belge ve kişisel verilerin nasıl ve kimin onayıyla yok edileceğini belirleyen kurallar."
see_also: [saklama-suresi]
cards: [kb-ea-35-1-document-archive-retention]
```

## Güvenli elektronik imza

```yaml
id: guvenli-elektronik-imza
term: "Güvenli elektronik imza"
en: "qualified electronic signature"
definition: "Nitelikli sertifikaya dayanan ve kişiye bağlı elektronik imza."
see_also: [mali-muhur, kep]
cards: [kb-ea-35-2-e-signature-kep-seal]
```

## Mali mühür

```yaml
id: mali-muhur
term: "Mali mühür"
en: "fiscal seal"
definition: "Vergi mükellefi kuruma ait, e-belgeleri kurum adına imzalamakta kullanılan elektronik sertifika."
see_also: [guvenli-elektronik-imza]
cards: [kb-ea-35-2-e-signature-kep-seal, kb-ea-37-2-e-fatura-scenarios]
```

## Kayıtlı elektronik posta (KEP)

```yaml
id: kep
term: "Kayıtlı elektronik posta (KEP)"
en: "registered electronic mail"
definition: "Gönderim ve teslimi ispat edilebilir biçimde kayda alan elektronik posta hizmeti."
see_also: [guvenli-elektronik-imza]
cards: [kb-ea-35-2-e-signature-kep-seal]
```

## UBL-TR

```yaml
id: ubl-tr
term: "UBL-TR"
en: "UBL-TR"
definition: "E-belgelerde kullanılan, uluslararası UBL standardının Türkiye uyarlaması olan XML biçimi."
see_also: [ettn]
cards: [kb-ea-37-2-e-fatura-scenarios]
```

## ETTN

```yaml
id: ettn
term: "ETTN"
en: "unique invoice identifier"
definition: "Her e-belgeye verilen tekil kimlik numarası (UUID)."
see_also: [ubl-tr]
cards: [kb-ea-37-2-e-fatura-scenarios]
```

## Ticari fatura senaryosu

```yaml
id: ticari-fatura
term: "Ticari fatura senaryosu"
en: "commercial invoice profile"
definition: "Alıcının e-faturaya sistem üzerinden kabul veya red yanıtı verebildiği senaryo."
see_also: [ubl-tr]
cards: [kb-ea-37-2-e-fatura-scenarios]
```

## İrsaliye yanıtı

```yaml
id: irsaliye-yaniti
term: "İrsaliye yanıtı"
en: "despatch advice response"
definition: "Alıcının e-irsaliyedeki malları teslim alma durumunu bildiren elektronik yanıt."
see_also: [e-irsaliye]
cards: [kb-ea-37-2-e-irsaliye-practice]
```

## Özel entegratör

```yaml
id: ozel-entegrator
term: "Özel entegratör"
en: "authorised e-document integrator"
definition: "E-belgeleri işletmeler adına ileten yetkili hizmet sağlayıcı."
see_also: [idempotency]
cards: [kb-ea-37-3-e-document-integration-routes, kb-ea-40-4-integrating-sfa-with-erp]
```

## Tekrarlanabilirlik (idempotency)

```yaml
id: idempotency
term: "Tekrarlanabilirlik (idempotency)"
en: "idempotency"
definition: "Aynı isteğin birden çok kez gönderilmesinin tek seferlik etkiyle sonuçlanması."
see_also: [ozel-entegrator]
cards: [kb-ea-37-3-e-document-integration-routes]
```

## Berat

```yaml
id: berat
term: "Berat"
en: "e-ledger receipt"
definition: "E-defterin teslim edildiğini gösteren onay dosyası."
see_also: [e-defter]
cards: [kb-ea-37-4-e-defter-e-arsiv]
```

## FAST

```yaml
id: fast
term: "FAST"
en: "instant payment system"
definition: "TCMB'nin işlettiği, günün her saati anlık para transferi sağlayan sistem."
see_also: [eft]
cards: [kb-ea-38-1-payment-systems-tr]
```

## EFT

```yaml
id: eft
term: "EFT"
en: "electronic funds transfer"
definition: "Bankalar arası elektronik fon transferi sistemi."
see_also: [fast]
cards: [kb-ea-38-1-payment-systems-tr]
```

## TR Karekod

```yaml
id: tr-karekod
term: "TR Karekod"
en: "TR QR code"
definition: "Karekodla ödeme için Türkiye'de kullanılan ortak standart."
see_also: [fast]
cards: [kb-ea-38-1-payment-systems-tr]
```

## Kredi bürosu

```yaml
id: kredi-burosu
term: "Kredi bürosu"
en: "credit bureau"
definition: "Finans kuruluşlarının kredi ve risk verilerini paylaştığı kuruluş."
see_also: [risk-raporu]
cards: [kb-ea-38-3-findeks-credit-bureau]
```

## Risk raporu

```yaml
id: risk-raporu
term: "Risk raporu"
en: "credit report"
definition: "Bir kişi veya firmanın kredi ve ödeme geçmişini özetleyen rapor."
see_also: [kredi-burosu]
cards: [kb-ea-38-3-findeks-credit-bureau]
```

## Adaptör

```yaml
id: adaptor
term: "Adaptör"
en: "adapter"
definition: "Ortak veri modelini belirli bir sistemin yapısına çeviren entegrasyon bileşeni."
see_also: [alan-eslestirme]
cards: [kb-ea-40-4-integrating-sfa-with-erp]
```

## Alan eşleştirme

```yaml
id: alan-eslestirme
term: "Alan eşleştirme"
en: "field mapping"
definition: "İki sistemdeki alanların birbirine nasıl karşılık geldiğini tanımlayan kurallar."
see_also: [adaptor]
cards: [kb-ea-40-4-integrating-sfa-with-erp]
```

## Uygulama haritası

```yaml
id: uygulama-haritasi
term: "Uygulama haritası"
en: "application landscape"
definition: "Bir şirketin yeteneklerini, sistemlerini ve aralarındaki arayüzleri gösteren görünüm."
see_also: [adaptor]
cards: [kb-ea-41-1-case-distributor-app-landscape]
```

## Low-code platform

```yaml
id: low-code
term: "Low-code platform"
en: "low-code platform"
definition: "Görsel araçlarla az kod yazarak uygulama geliştirmeyi sağlayan platform."
see_also: [vatandas-gelistirici]
cards: [kb-ea-39-1-low-code]
```

## Vatandaş geliştirici

```yaml
id: vatandas-gelistirici
term: "Vatandaş geliştirici"
en: "citizen developer"
definition: "BT birimi dışından olup low-code araçlarla çözüm geliştiren çalışan."
see_also: [low-code]
cards: [kb-ea-39-1-low-code]
```

## Robotik süreç otomasyonu (RPA)

```yaml
id: rpa
term: "Robotik süreç otomasyonu (RPA)"
en: "robotic process automation"
definition: "Kullanıcı arayüzü üzerindeki kural tabanlı işleri yazılım robotlarıyla otomatikleştirme."
see_also: [yazilim-robotu]
cards: [kb-ea-39-2-rpa]
```

## Yazılım robotu

```yaml
id: yazilim-robotu
term: "Yazılım robotu"
en: "software bot"
definition: "İnsanın ekran üzerindeki adımlarını kurallara göre tekrarlayan program."
see_also: [rpa]
cards: [kb-ea-39-2-rpa]
```

## Üretken yapay zekâ

```yaml
id: uretken-yapay-zeka
term: "Üretken yapay zekâ"
en: "generative AI"
definition: "Metin, görüntü veya kod gibi yeni içerik üretebilen yapay zekâ modelleri."
see_also: [rag]
cards: [kb-ea-39-3-genai-at-work]
```

## Maruziyet (yapay zekâ)

```yaml
id: maruziyet
term: "Maruziyet (yapay zekâ)"
en: "AI exposure"
definition: "Bir mesleğin görevlerinin yapay zekâdan etkilenebilecek payı."
see_also: [uretken-yapay-zeka]
cards: [kb-ea-39-3-genai-at-work]
```

## Erişimle zenginleştirilmiş üretim (RAG)

```yaml
id: rag
term: "Erişimle zenginleştirilmiş üretim (RAG)"
en: "retrieval-augmented generation"
definition: "Dil modelinin cevap üretmeden önce ilgili belgeleri getirip yanıtını bunlara dayandırması."
see_also: [halusinasyon]
cards: [kb-ea-39-4-ai-assistants-on-company-data]
```

## Halüsinasyon

```yaml
id: halusinasyon
term: "Halüsinasyon"
en: "hallucination"
definition: "Dil modelinin kaynağa dayanmayan, akıcı ama yanlış içerik üretmesi."
see_also: [rag]
cards: [kb-ea-39-4-ai-assistants-on-company-data]
```

## Sonraki en iyi aksiyon

```yaml
id: sonraki-en-iyi-aksiyon
term: "Sonraki en iyi aksiyon"
en: "next best action"
definition: "Kullanıcıya bir sonraki adım için veri tabanlı öneri sunan yöntem."
see_also: [mlops]
cards: [kb-ea-39-5-ml-forecast-recommendation]
```

## MLOps

```yaml
id: mlops
term: "MLOps"
en: "MLOps"
definition: "Makine öğrenmesi modellerinin eğitim, yayın, izleme ve yenilenme süreçlerinin yönetimi."
see_also: [anormallik-tespiti]
cards: [kb-ea-39-5-ml-forecast-recommendation]
```

## Anormallik tespiti

```yaml
id: anormallik-tespiti
term: "Anormallik tespiti"
en: "anomaly detection"
definition: "Olağan örüntüden belirgin biçimde sapan kayıtların otomatik işaretlenmesi."
see_also: [mlops]
cards: [kb-ea-39-5-ml-forecast-recommendation]
```

## Canlıya geçiş (cutover)

```yaml
id: cutover
term: "Canlıya geçiş (cutover)"
en: "cutover"
definition: "Eski sistemin kapatılıp yeni sistemin kullanıma açıldığı planlı geçiş dönemi."
see_also: [geri-donus-plani]
cards: [kb-ea-41-5-cutover-plan]
```

## Geri dönüş planı

```yaml
id: geri-donus-plani
term: "Geri dönüş planı"
en: "rollback plan"
definition: "Canlıya geçiş başarısız olursa eski sisteme hangi koşulda ve nasıl dönüleceğini belirleyen plan."
see_also: [cutover]
cards: [kb-ea-41-5-cutover-plan]
```
