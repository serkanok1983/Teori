# Sözlük (Glossary)

OMURGA Bilgi Bankası sözlüğü — 477 terim, Türkçe alfabetik sırada. Her terim bir H2 başlık ve bir `yaml` bloğundan oluşur; `id` değeri kartların `glossary_terms` alanında kullanılır. Tanımlar kısa tutulur; ayrıntı ilgili kartlardadır. (v1.0: FMCG, Ekonomi ve İşletme Mimarisi terimleri birleştirildi; birleştirme kaydı `glossary/_merged/MERGE-LOG.md`.)

## A/B testi

```yaml
id: ab-testi
term: "A/B testi"
en: "A/B test"
definition: "Kullanıcıların rastgele iki gruba ayrılıp yalnızca birinin değişikliği gördüğü, farkın etkisini ölçen kontrollü deney."
see_also: [kontrol-grubu, p-degeri]
cards: [kb-eco-47-4-ab-testing-significance]
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

## Açık rıza

```yaml
id: acik-riza
term: "Açık rıza"
en: "Explicit consent"
definition: "Belirli bir konuya ilişkin, bilgilendirilmeye dayanan ve özgür iradeyle açıklanan onay."
see_also: [kvkk]
cards: [kb-ea-15-5-kvkk-basics, kb-ea-25-4-consent-iys-marketing]
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

## Adaptör

```yaml
id: adaptor
term: "Adaptör"
en: "adapter"
definition: "Ortak veri modelini belirli bir sistemin yapısına çeviren entegrasyon bileşeni."
see_also: [alan-eslestirme]
cards: [kb-ea-40-4-integrating-sfa-with-erp]
```

## Ağırlıklı dağıtım

```yaml
id: agirlikli-dagitim
term: "Ağırlıklı dağıtım"
en: "weighted distribution"
definition: "Ürünü bulunduran satış noktalarının, kategorinin toplam satışı içindeki payı."
see_also: [sayisal-dagitim]
cards: [kb-fmcg-12-6-case-brand-growth-plan, kb-fmcg-13-9-prospecting-account-segmentation, kb-fmcg-3-4-mental-physical-availability, kb-fmcg-4-7-launch-forecasting]
```

## Ağırlıklı ortalama maliyet

```yaml
id: agirlikli-ortalama-maliyet
term: "Ağırlıklı ortalama maliyet"
en: "weighted average cost"
definition: "Satılan malın ve dönem sonu stoğun, alımların miktarla ağırlıklandırılmış ortalama birim maliyetiyle değerlendiği yöntem."
see_also: [fifo]
cards: [kb-eco-34-1-inventory-valuation]
```

## Ağırlıklı ortalama sermaye maliyeti (AOSM)

```yaml
id: aosm
term: "Ağırlıklı ortalama sermaye maliyeti (AOSM)"
en: "weighted average cost of capital, WACC"
definition: "Özkaynak maliyeti ile vergi sonrası borç maliyetinin, sermaye yapısındaki paylarıyla ağırlıklandırılmış ortalaması."
see_also: [ozkaynak-maliyeti, yatirilan-sermaye-getirisi]
cards: [kb-eco-31-2-cost-of-capital]
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

## Alacak tahsil süresi

```yaml
id: alacak-tahsil-suresi
term: "Alacak tahsil süresi"
en: "days sales outstanding (DSO)"
definition: "Ticari alacakların ortalama kaç günde tahsil edildiğini gösteren gösterge; alacak bakiyesi / net satış × gün sayısı."
see_also: [alacak-yaslandirma, nakit-donusum-suresi]
cards: [kb-eco-33-7-reading-annual-report, kb-eco-38-2-cash-conversion-cycle, kb-eco-55-1-case-distributor-credit-decision, kb-fmcg-11-1-supply-chain-basics, kb-fmcg-12-7-case-distributor-turnaround, kb-fmcg-7-3-credit-collections-dso]
```

## Alacak yaşlandırma

```yaml
id: alacak-yaslandirma
term: "Alacak yaşlandırma"
en: "receivables aging"
definition: "Ticari alacakların vadesinden bu yana geçen süreye göre gruplara ayrılarak izlenmesi."
see_also: [beklenen-kredi-zarari]
cards: [kb-eco-34-2-receivables-doubtful-debts]
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

## Alım sıklığı

```yaml
id: alim-sikligi
term: "Alım sıklığı"
en: "Purchase frequency"
definition: "Markayı alan hanelerin belirli bir dönemde ortalama kaç kez satın aldığı."
see_also: [penetrasyon]
cards: [kb-fmcg-12-6-case-brand-growth-plan, kb-fmcg-3-2-repeat-buying-patterns]
```

## Alışveriş yolculuğu

```yaml
id: alisveris-yolculugu
term: "Alışveriş yolculuğu"
en: "path to purchase"
definition: "Alıcının bir ürünü bilmekten satın almaya ve tekrar almaya kadar geçtiği adımlar."
see_also: [donusum-orani]
cards: [kb-fmcg-3-7-shopper-path-to-purchase]
```

## Amortisman

```yaml
id: amortisman
term: "Amortisman"
en: "depreciation"
definition: "Maddi duran varlığın maliyetinin faydalı ömrü boyunca gider olarak dağıtılması; nakit çıkışı değildir."
see_also: [faydali-omur]
cards: [kb-eco-34-3-fixed-assets-depreciation]
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

## Ana veri

```yaml
id: ana-veri
term: "Ana veri"
en: "master data"
definition: "Müşteri, ürün, tedarikçi gibi işlemlerde tekrar kullanılan temel kayıtlar."
see_also: [mdm, veri-yonetisimi]
cards: [kb-ea-10-1-why-integration-is-hard, kb-ea-8-1-master-data-governance, kb-ea-8-2-data-quality-field, kb-ea-8-3-mdm-matching-duplicates, kb-ea-8-4-gs1-barcodes-pim]
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

## Analitik CRM

```yaml
id: analitik-crm
term: "Analitik CRM"
en: "Analytical CRM"
definition: "Müşteri verisinden segmentasyon, kayıp riski ve fırsat analizi üreten CRM bileşeni."
see_also: [crm]
cards: [kb-ea-25-1-crm-basics]
```

## anlaşmaya en iyi alternatif

```yaml
id: batna
term: "anlaşmaya en iyi alternatif"
en: "best alternative to a negotiated agreement (BATNA)"
definition: "Bir müzakerede anlaşma sağlanamazsa tarafın başvurabileceği en iyi seçenek; kabul edilebilecek en kötü anlaşmanın sınırını belirler."
see_also: [anlasma-alani]
cards: [kb-fmcg-13-14-negotiation-structure]
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

## API (uygulama programlama arayüzü)

```yaml
id: api
term: "API (uygulama programlama arayüzü)"
en: "Application programming interface"
definition: "Bir sistemin diğer sistemlere hangi veriyi hangi kurallarla sunduğunu tanımlayan programlanabilir arayüz."
see_also: [entegrasyon, webhook]
cards: [kb-ea-11-6-apis-for-managers]
```

## Araçtan satış

```yaml
id: aractan-satis
term: "Araçtan satış"
en: "van selling"
definition: "Satış, teslimat ve çoğu zaman tahsilatın aynı ziyarette, ürün yüklü araçla yapıldığı saha satış biçimi."
see_also: [gun-sonu-mutabakati, on-satis]
cards: [kb-ea-26-5-van-sales-presales, kb-fmcg-8-1-selling-formats]
```

## Arka marj

```yaml
id: arka-marj
term: "Arka marj"
en: "back margin"
definition: "Perakendecinin alış fiyatı dışında üreticiden aldığı prim, ücret ve destekler."
see_also: [ciro-primi, ticari-harcama]
cards: [kb-fmcg-9-1-retailer-economics]
```

## Artan oranlı tarife

```yaml
id: artan-oranli-tarife
term: "Artan oranlı tarife"
en: "progressive tax schedule"
definition: "Gelirin dilimlere ayrıldığı ve üst dilimlere daha yüksek oran uygulandığı vergi tarifesi; her oran yalnızca kendi dilimindeki tutara uygulanır."
see_also: [marjinal-vergi-orani]
cards: [kb-eco-42-1-tax-basics-average-marginal]
```

## Artımsal hacim

```yaml
id: artimsal-hacim
term: "Artımsal hacim"
en: "incremental volume"
definition: "Bir faaliyetin baz satışın üstüne getirdiği ek satış hacmi."
see_also: [baz-satis]
cards: [kb-fmcg-12-3-analytics-for-decisions, kb-fmcg-13-5-retail-buyer-decisions, kb-fmcg-5-4-promotion-economics, kb-fmcg-5-5-trade-spend-roi, kb-fmcg-9-6-trade-marketing, kb-fmcg-9-7-retail-media]
```

## Arz şoku

```yaml
id: arz-soku
term: "Arz şoku"
en: "supply shock"
definition: "Talepten bağımsız olarak üretim maliyetlerini veya arz miktarını aniden değiştiren olay."
see_also: []
cards: [kb-eco-19-3-supply-shocks-cost-inflation]
```

## Asıl–vekil sorunu

```yaml
id: asil-vekil-sorunu
term: "Asıl–vekil sorunu"
en: "principal–agent problem"
definition: "İşi yaptıran taraf (asıl) ile işi yapan tarafın (vekil) çıkarları farklı olduğunda ve vekilin davranışı tam izlenemediğinde ortaya çıkan verim kaybı."
see_also: []
cards: [kb-eco-12-3-principal-agent, kb-eco-31-5-agency-governance-family-firm]
```

## Aşama-kapı süreci

```yaml
id: asama-kapi
term: "Aşama-kapı süreci"
en: "stage-gate"
definition: "Yeni ürün projesini aşamalara bölen ve her aşama sonunda devam ya da dur kararı veren yönetim süreci."
see_also: []
cards: [kb-fmcg-4-5-stage-gate-innovation]
```

## Aşırı güven

```yaml
id: asiri-guven
term: "Aşırı güven"
en: "overconfidence"
definition: "Kişinin kendi tahmin ve bilgisinin doğruluğunu olduğundan yüksek görmesi."
see_also: []
cards: [kb-eco-13-1-heuristics-biases]
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

## Aydınlatma yükümlülüğü

```yaml
id: aydinlatma-yukumlulugu
term: "Aydınlatma yükümlülüğü"
en: "Duty to inform"
definition: "Kişisel veri işlenirken veri sahibine kimin, hangi amaçla, hangi veriyi işlediğinin bildirilmesi."
see_also: [kvkk]
cards: [kb-ea-15-5-kvkk-basics]
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

## Bağımsız denetim

```yaml
id: bagimsiz-denetim
term: "Bağımsız denetim"
en: "statutory audit"
definition: "Finansal tabloların, yetkili bağımsız denetçi tarafından ilgili raporlama çerçevesine uygunluk açısından incelenip görüş bildirilmesi."
see_also: [tfrs]
cards: [kb-eco-35-1-reporting-regimes-tr]
```

## Başabaş noktası

```yaml
id: basabas-noktasi
term: "Başabaş noktası"
en: "Break-even point"
definition: "Toplam katkı payının sabit giderlere eşit olduğu, kârın sıfır olduğu satış hacmi."
see_also: [katki-payi, sabit-maliyet]
cards: [kb-fmcg-2-3-contribution-breakeven]
```

## Batık maliyet

```yaml
id: batik-maliyet
term: "Batık maliyet"
en: "sunk cost"
definition: "Geçmişte yapılmış ve hangi seçenek seçilirse seçilsin geri alınamayan harcama; karara girmez."
see_also: [firsat-maliyeti]
cards: [kb-eco-1-1-opportunity-cost-sunk-cost, kb-eco-39-5-relevant-costs-decisions, kb-eco-5-5-economies-of-scale-sunk-costs]
```

## Bayi (distribütör)

```yaml
id: bayi
term: "Bayi (distribütör)"
en: "Distributor"
definition: "Üreticiden alıp belirli bir bölgedeki perakende noktalara satan, stok, teslimat, kredi ve satış işlevlerini üstlenen bağımsız işletme."
see_also: [kanal-islevleri, toptanci]
cards: [kb-fmcg-1-3-channel-actors, kb-fmcg-12-7-case-distributor-turnaround, kb-fmcg-6-4-direct-vs-indirect, kb-fmcg-7-1-distributor-pnl, kb-fmcg-7-4-distributor-selection-kpis, kb-fmcg-7-5-distributor-development]
```

## Baz etkisi

```yaml
id: baz-etkisi
term: "Baz etkisi"
en: "base effect"
definition: "Yıllık değişim oranının, bir yıl önceki aynı dönemin olağan dışı düşük veya yüksek değerinden etkilenmesi."
see_also: []
cards: [kb-eco-14-2-inflation-measurement-tufe-ufe]
```

## Baz satış

```yaml
id: baz-satis
term: "Baz satış"
en: "baseline sales"
definition: "Promosyon ya da özel bir faaliyet olmasaydı gerçekleşecek tahmini satış."
see_also: [artimsal-hacim]
cards: [kb-fmcg-11-2-demand-forecasting, kb-fmcg-12-3-analytics-for-decisions, kb-fmcg-13-16-sales-forecasting, kb-fmcg-5-4-promotion-economics]
```

## Beklenen kayıp

```yaml
id: beklenen-kayip
term: "Beklenen kayıp"
en: "expected loss"
definition: "Bir kaybın olasılığı ile tutarının çarpımı."
see_also: []
cards: [kb-eco-4-2-risk-aversion-insurance]
```

## Beklenen kredi zararı

```yaml
id: beklenen-kredi-zarari
term: "Beklenen kredi zararı"
en: "expected credit loss"
definition: "Alacaklarda gelecekte oluşması beklenen tahsil edilememe zararının, gerçekleşmeden önce tahmin edilerek karşılık ayrılması yaklaşımı (TFRS 9)."
see_also: [supheli-alacak]
cards: [kb-eco-34-2-receivables-doubtful-debts, kb-eco-37-3-customer-credit-analysis, kb-eco-55-1-case-distributor-credit-decision]
```

## Belirlilik katsayısı (R²)

```yaml
id: belirlilik-katsayisi
term: "Belirlilik katsayısı (R²)"
en: "coefficient of determination"
definition: "Bağımlı değişkendeki değişimin regresyon modeliyle açıklanan payı."
see_also: [regresyon]
cards: [kb-eco-47-5-correlation-regression-basics]
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

## Bilanço

```yaml
id: bilanco
term: "Bilanço"
en: "balance sheet"
definition: "Belirli bir tarihte şirketin varlıklarını, borçlarını ve özkaynağını gösteren finansal tablo."
see_also: [gelir-tablosu]
cards: [kb-eco-33-5-balance-sheet]
```

## Bilgi asimetrisi

```yaml
id: bilgi-asimetrisi
term: "Bilgi asimetrisi"
en: "information asymmetry"
definition: "İşlemin bir tarafının diğerinden daha fazla bilgiye sahip olması."
see_also: [ters-secim]
cards: [kb-eco-12-1-adverse-selection-credit, kb-eco-12-3-principal-agent]
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

## Birim fiyat

```yaml
id: birim-fiyat
term: "Birim fiyat"
en: "unit price"
definition: "Ürünün kilogram, litre ya da adet gibi standart bir birim başına fiyatı."
see_also: [fiyat-paket-mimarisi]
cards: [kb-fmcg-13-7-behavioural-economics-selling, kb-fmcg-5-3-price-pack-architecture]
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

## BOBİ FRS

```yaml
id: bobi-frs
term: "BOBİ FRS"
en: "Turkish financial reporting standard for large and medium-sized entities"
definition: "Bağımsız denetime tabi olup TFRS uygulamak zorunda olmayan büyük ve orta boy işletmeler için KGK'nın yayımladığı finansal raporlama standardı."
see_also: [tfrs]
cards: [kb-eco-35-1-reporting-regimes-tr]
```

## Borç ödeme süresi

```yaml
id: borc-odeme-suresi
term: "Borç ödeme süresi"
en: "days payables outstanding (DPO)"
definition: "Tedarikçi borçlarının ortalama kaç günde ödendiği."
see_also: [nakit-donusum-suresi]
cards: [kb-eco-38-2-cash-conversion-cycle, kb-fmcg-11-1-supply-chain-basics]
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

## BPMN

```yaml
id: bpmn
term: "BPMN"
en: "Business Process Model and Notation"
definition: "Süreç haritaları için olay, faaliyet, karar noktası ve kulvar gibi öğeler tanımlayan standart gösterim."
see_also: [bpm]
cards: [kb-ea-4-3-process-maps-bpmn]
```

## Brüt kâr

```yaml
id: brut-kar
term: "Brüt kâr"
en: "gross profit"
definition: "Net satışlardan satışların maliyetinin düşülmesiyle bulunan kâr."
see_also: [faaliyet-kari]
cards: [kb-eco-33-4-income-statement, kb-eco-38-1-distributor-financial-statements]
```

## Brüt ücret

```yaml
id: brut-ucret
term: "Brüt ücret"
en: "Gross pay"
definition: "Kesintilerden önceki ücret tutarı."
see_also: [net-ucret]
cards: [kb-ea-33-2-payroll-basics, kb-eco-43-2-income-tax-withholding, kb-eco-44-3-sgk-employer-costs]
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

## Bulut bilişim

```yaml
id: bulut-bilisim
term: "Bulut bilişim"
en: "Cloud computing"
definition: "Ağ üzerinden, ihtiyaç anında, paylaşılan ve ölçülen bilişim kaynaklarının kullanılması."
see_also: [saas]
cards: [kb-ea-16-1-cloud-saas-basics, kb-ea-16-5-cloud-cost-data-residency]
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

## Canlıya geçiş

```yaml
id: canliya-gecis
term: "Canlıya geçiş"
en: "Go-live"
definition: "Yeni sistemin gerçek işlemler için kullanılmaya başlandığı an ve bu ana hazırlık süreci."
see_also: [geri-donus-plani, veri-tasima]
cards: [kb-ea-18-4-post-go-live-dip, kb-ea-18-5-implementation-methodology, kb-ea-41-5-cutover-plan]
```

## Cari oran

```yaml
id: cari-oran
term: "Cari oran"
en: "current ratio"
definition: "Dönen varlıkların kısa vadeli yabancı kaynaklara oranı; kısa vadeli ödeme gücünün kaba göstergesi."
see_also: [bilanco]
cards: [kb-eco-33-5-balance-sheet]
```

## Cep fiyatı

```yaml
id: cep-fiyati
term: "Cep fiyatı"
en: "Pocket price"
definition: "Tüm fatura altı ve fatura dışı indirimler ile sabit ücretler düşüldükten sonra satıcıya kalan birim fiyat."
see_also: [fiyat-selalesi]
cards: [kb-ea-27-1-pricing-engine-conditions, kb-fmcg-10-2-trade-terms, kb-fmcg-2-2-gross-to-net]
```

## Ciro primi

```yaml
id: ciro-primi
term: "Ciro primi"
en: "Volume / turnover rebate"
definition: "Müşteriye belirli bir dönemdeki satın alma tutarına bağlı olarak dönem sonunda ödenen prim."
see_also: [ticari-harcama]
cards: [kb-fmcg-10-1-key-account-management, kb-fmcg-10-2-trade-terms, kb-fmcg-10-4-negotiating-with-chains, kb-fmcg-13-14-negotiation-structure, kb-fmcg-2-2-gross-to-net, kb-fmcg-5-5-trade-spend-roi, kb-fmcg-9-1-retailer-economics]
```

## CR4 (dört firma yoğunlaşma oranı)

```yaml
id: cr4
term: "CR4 (dört firma yoğunlaşma oranı)"
en: "Four-firm concentration ratio"
definition: "Pazardaki en büyük dört firmanın pazar paylarının toplamı."
see_also: [hhi]
cards: [kb-fmcg-1-2-scale-and-concentration]
```

## Çapalama

```yaml
id: capalama
term: "Çapalama"
en: "Anchoring"
definition: "İlk görülen bir rakamın sonraki tahmin veya değerlendirmeleri o rakama doğru çekmesi."
see_also: [kayiptan-kacinma]
cards: [kb-eco-13-1-heuristics-biases, kb-fmcg-13-14-negotiation-structure, kb-fmcg-13-7-behavioural-economics-selling, kb-fmcg-3-1-consumer-decisions]
```

## Çapraz fiyat esnekliği

```yaml
id: capraz-fiyat-esnekligi
term: "Çapraz fiyat esnekliği"
en: "cross-price elasticity"
definition: "Bir ürünün fiyatındaki yüzde değişime karşı başka bir ürünün hacmindeki yüzde değişim."
see_also: []
cards: [kb-fmcg-5-1-price-elasticity]
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

## Çift marjinalleşme

```yaml
id: cift-marjinallesme
term: "Çift marjinalleşme"
en: "double marginalization"
definition: "Zincirdeki her halkanın kendi marjını ayrı ayrı eklemesiyle raf fiyatının gereğinden yükselmesi."
see_also: [marj]
cards: [kb-eco-8-2-vertical-restraints, kb-fmcg-1-1-margin-stack, kb-fmcg-1-1-margin-vs-markup, kb-fmcg-1-3-channel-actors]
```

## Çift taraflı kayıt

```yaml
id: cift-tarafli-kayit
term: "Çift taraflı kayıt"
en: "double-entry bookkeeping"
definition: "Her işlemin en az iki hesabı eşit tutarda, biri borç biri alacak tarafında etkilediği kayıt sistemi."
see_also: [bilanco]
cards: [kb-eco-33-2-double-entry-basics]
```

## Çifte risk

```yaml
id: cifte-risk
term: "Çifte risk"
en: "Double jeopardy"
definition: "Küçük markaların hem daha az alıcıya sahip olması hem de bu alıcıların markayı biraz daha seyrek alması kalıbı."
see_also: [alim-sikligi, penetrasyon]
cards: [kb-fmcg-3-2-repeat-buying-patterns]
```

## çözüm satışı

```yaml
id: cozum-satisi
term: "çözüm satışı"
en: "solution selling"
definition: "Ürün özelliklerini anlatmak yerine müşterinin sorununu ve ihtiyacını sorularla ortaya çıkarıp ona göre bir çözüm öneren satış yaklaşımı."
see_also: [satin-alma-merkezi]
cards: [kb-fmcg-13-11-objections-closing-upsell, kb-fmcg-13-12-adaptive-selling, kb-fmcg-13-2-spin-solution-selling, kb-fmcg-13-3-challenger-meddic-sandler, kb-fmcg-13-6-persuasion-science]
```

## Dağıtım ihtiyaç planlaması (DRP)

```yaml
id: drp
term: "Dağıtım ihtiyaç planlaması (DRP)"
en: "Distribution requirements planning"
definition: "Depolar için talep, stok ve planlı girişlerden ikmal ihtiyacını zamana yayarak hesaplayan yöntem."
see_also: [guvenlik-stoku, tedarik-suresi]
cards: [kb-ea-29-3-drp-inventory-planning]
```

## dağıtım merkezi

```yaml
id: dagitim-merkezi
term: "dağıtım merkezi"
en: "distribution centre"
definition: "Ürünlerin toplanıp depolandığı, siparişlere göre hazırlanıp noktalara ya da alt depolara sevk edildiği tesis."
see_also: [guvenlik-stoku]
cards: [kb-fmcg-11-7-warehouse-transport-network, kb-fmcg-11-8-cold-chain]
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

## Damga vergisi

```yaml
id: damga-vergisi
term: "Damga vergisi"
en: "stamp duty"
definition: "Sözleşme ve kanunda sayılan diğer kâğıtlar üzerinden alınan vergi; 488 sayılı Kanun ile düzenlenir."
see_also: [otv]
cards: [kb-eco-43-1-turkish-tax-system-overview, kb-eco-43-5-otv-stamp-duty]
```

## Deflatör

```yaml
id: deflator
term: "Deflatör"
en: "deflator"
definition: "Nominal büyüklüğü reel büyüklüğe çevirmek için kullanılan fiyat endeksi."
see_also: [gsyh]
cards: [kb-eco-14-1-gdp-real-nominal]
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

## Değişken maliyet

```yaml
id: degisken-maliyet
term: "Değişken maliyet"
en: "Variable cost"
definition: "Satış ya da üretim hacmiyle doğru orantılı olarak artan maliyet; hammadde, ambalaj, adet başı nakliye gibi."
see_also: [katki-payi, sabit-maliyet]
cards: [kb-fmcg-1-2-scale-and-concentration, kb-fmcg-2-3-contribution-breakeven, kb-fmcg-6-4-direct-vs-indirect]
```

## Değişken ücret

```yaml
id: degisken-ucret
term: "Değişken ücret"
en: "variable pay"
definition: "Satış çalışanının ücretinin, hedef gerçekleşmesine ya da başka performans ölçütlerine bağlı olarak değişen kısmı."
see_also: [hizlandirici]
cards: [kb-fmcg-8-12-salesperson-motivation, kb-fmcg-8-8-incentive-compensation]
```

## Deneme-tekrar modeli

```yaml
id: deneme-tekrar
term: "Deneme-tekrar modeli"
en: "trial-repeat model"
definition: "Yeni ürün hacmini, ürünü ilk kez alanlar ve tekrar alanlar üzerinden tahmin eden yaklaşım."
see_also: [penetrasyon]
cards: [kb-fmcg-4-7-launch-forecasting]
```

## Dengeli karne

```yaml
id: dengeli-karne
term: "Dengeli karne"
en: "Balanced scorecard"
definition: "Performansı finansal, müşteri, iç süreç ve öğrenme boyutlarında izleyen yönetim aracı."
see_also: [okr, strateji-haritasi]
cards: [kb-ea-23-3-balanced-scorecard-okr]
```

## Depo yönetim sistemi (WMS)

```yaml
id: wms
term: "Depo yönetim sistemi (WMS)"
en: "Warehouse management system"
definition: "Depo içindeki lokasyon bazlı stok ve görevleri yöneten sistem."
see_also: [dalga-planlama, el-terminali]
cards: [kb-ea-30-3-wms-what-it-does]
```

## Devlet tahvili

```yaml
id: devlet-tahvili
term: "Devlet tahvili"
en: "government bond"
definition: "Hazinenin bir yıldan uzun vadeli borçlanma aracı."
see_also: [hazine-bonosu, kupon]
cards: [kb-eco-25-6-bond-types-treasury-instruments]
```

## Devreden KDV

```yaml
id: devreden-kdv
term: "Devreden KDV"
en: "VAT carried forward"
definition: "Bir dönemde indirilecek KDV'nin hesaplanan KDV'yi aşan ve sonraki dönemlere aktarılan kısmı."
see_also: [indirilecek-kdv]
cards: [kb-eco-43-4-kdv-vat]
```

## Dışsallık

```yaml
id: dissallik
term: "Dışsallık"
en: "externality"
definition: "Bir faaliyetin, fiyata yansımadan üçüncü kişilere yüklediği maliyet veya sağladığı fayda."
see_also: [karbon-fiyatlamasi]
cards: [kb-eco-40-4-environmental-taxes-cbam]
```

## Dikey kısıt

```yaml
id: dikey-kisit
term: "Dikey kısıt"
en: "vertical restraint"
definition: "Tedarik zincirinin farklı basamaklarındaki firmalar arasındaki sözleşmede birinin diğerinin ticari serbestliğini sınırlaması."
see_also: [cift-marjinallesme, yeniden-satis-fiyati]
cards: [kb-eco-8-2-vertical-restraints]
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

## Doğrudan borçlandırma sistemi (DBS)

```yaml
id: dbs
term: "Doğrudan borçlandırma sistemi (DBS)"
en: "Direct debit system"
definition: "Bayinin bankasının tanımlı limit dahilinde tedarikçiye vadesinde ödeme yapmayı taahhüt ettiği tahsilat yöntemi."
see_also: [kredi-limiti]
cards: [kb-ea-24-3-credit-limits-collections-systems, kb-eco-38-3-distributor-credit-risk-dbs, kb-eco-50-3-working-with-banks]
```

## Doğrudan dağıtım

```yaml
id: dogrudan-dagitim
term: "Doğrudan dağıtım"
en: "direct distribution"
definition: "Üreticinin satış, teslimat ve tahsilatı aracı olmadan kendi kaynaklarıyla yapması."
see_also: [bayi, pazara-giris-modeli]
cards: [kb-fmcg-6-4-direct-vs-indirect, kb-fmcg-6-8-rtm-design-case]
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

## Dönüşüm oranı

```yaml
id: donusum-orani
term: "Dönüşüm oranı"
en: "conversion rate"
definition: "Bir adımı geçenlerin, önceki adımı geçenlere oranı."
see_also: [alisveris-yolculugu]
cards: [kb-fmcg-13-8-sales-funnel-math, kb-fmcg-3-7-shopper-path-to-purchase]
```

## Döviz pozisyonu

```yaml
id: doviz-pozisyonu
term: "Döviz pozisyonu"
en: "FX position"
definition: "Döviz cinsinden varlıklar ile döviz cinsinden yükümlülükler arasındaki fark."
see_also: [kur-riski]
cards: [kb-eco-23-2-currency-crises-business]
```

## DuPont analizi

```yaml
id: dupont-analizi
term: "DuPont analizi"
en: "DuPont analysis"
definition: "Özkaynak kârlılığını net kâr marjı, varlık devir hızı ve finansal kaldıraç bileşenlerine ayıran analiz."
see_also: [ozkaynak-karliligi, varlik-devir-hizi]
cards: [kb-eco-36-5-dupont]
```

## Durum tespiti

```yaml
id: durum-tespiti
term: "Durum tespiti"
en: "due diligence"
definition: "Satın alma öncesinde hedef şirketin finansal, vergi, hukuki ve ticari durumunun ayrıntılı incelenmesi."
see_also: [sinerji]
cards: [kb-eco-31-8-mergers-acquisitions]
```

## Duyarlılık analizi

```yaml
id: duyarlilik-analizi
term: "Duyarlılık analizi"
en: "sensitivity analysis"
definition: "Tek bir varsayım değiştirilip diğerleri sabit tutularak sonucun ne kadar değiştiğinin ölçülmesi."
see_also: [senaryo-analizi]
cards: [kb-eco-31-10-scenario-sensitivity]
```

## e-Arşiv Fatura

```yaml
id: e-arsiv-fatura
term: "e-Arşiv Fatura"
en: "e-Archive invoice"
definition: "e-Fatura sistemine kayıtlı olmayan alıcılara elektronik ortamda düzenlenen fatura."
see_also: [e-fatura]
cards: [kb-ea-26-5-van-sales-presales, kb-ea-37-1-e-document-map, kb-ea-37-4-e-defter-e-arsiv]
```

## e-Defter

```yaml
id: e-defter
term: "e-Defter"
en: "e-Ledger"
definition: "Yasal defterlerin elektronik ortamda tutulması ve beratlarının alınması."
see_also: [e-fatura]
cards: [kb-ea-37-1-e-document-map, kb-ea-37-4-e-defter-e-arsiv]
```

## e-Fatura

```yaml
id: e-fatura
term: "e-Fatura"
en: "e-invoice"
definition: "Faturanın elektronik ortamda düzenlenip GİB sistemi üzerinden alıcıya iletildiği belge türü; kapsamı mevzuata göre değişir."
see_also: [e-irsaliye]
cards: [kb-ea-20-2-order-to-cash, kb-ea-37-1-e-document-map, kb-fmcg-13-17-turkish-trade-practice]
```

## e-İrsaliye

```yaml
id: e-irsaliye
term: "e-İrsaliye"
en: "e-dispatch note"
definition: "Sevk irsaliyesinin elektronik ortamda düzenlenip iletilen hali; kapsamı mevzuata göre değişir."
see_also: [e-fatura]
cards: [kb-ea-20-2-order-to-cash, kb-ea-37-1-e-document-map, kb-ea-37-2-e-irsaliye-practice, kb-fmcg-13-17-turkish-trade-practice]
```

## Efektif faiz

```yaml
id: efektif-faiz
term: "Efektif faiz"
en: "effective interest rate"
definition: "Faiz, masraf ve diğer kredi maliyetlerinin tümünü içeren yıllık bileşik maliyet oranı."
see_also: [reel-faiz]
cards: [kb-eco-25-2-loans-real-vs-nominal, kb-eco-50-3-working-with-banks]
```

## Efektif vergi oranı

```yaml
id: efektif-vergi-orani
term: "Efektif vergi oranı"
en: "effective tax rate"
definition: "Hesaplanan verginin muhasebe kârına oranı; kanuni orandan kalıcı farklar nedeniyle ayrışabilir."
see_also: [kkeg]
cards: [kb-eco-43-3-corporate-tax]
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

## ekonomik sipariş miktarı

```yaml
id: ekonomik-siparis-miktari
term: "ekonomik sipariş miktarı"
en: "economic order quantity"
definition: "Sipariş verme ve stok tutma maliyetlerinin toplamını en aza indiren sipariş büyüklüğü."
see_also: [yeniden-siparis-noktasi]
cards: [kb-fmcg-11-3-eoq-reorder-point]
```

## Eksik sigorta

```yaml
id: eksik-sigorta
term: "Eksik sigorta"
en: "underinsurance"
definition: "Sigorta bedelinin sigorta değerinin altında olması; aksi kararlaştırılmadıkça tazminat, bedelin değere oranında azalır."
see_also: [sigorta-bedeli]
cards: [kb-eco-52-1-business-insurance]
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

## Elde tutma oranı

```yaml
id: elde-tutma-orani
term: "Elde tutma oranı"
en: "Retention rate"
definition: "Bir dönemin müşterilerinden sonraki dönemde de alım yapanların oranı."
see_also: [musteri-yasam-boyu-degeri]
cards: [kb-ea-25-2-customer-lifetime-value]
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

## Elektronik veri değişimi (EDI)

```yaml
id: edi
term: "Elektronik veri değişimi (EDI)"
en: "Electronic data interchange"
definition: "Firmalar arasında sipariş, sevk bildirimi ve fatura gibi belgelerin standart biçimde, sistemden sisteme otomatik alışverişi."
see_also: [entegrasyon, gtin]
cards: [kb-ea-11-4-edi-with-chains]
```

## Emisyon yoğunluğu

```yaml
id: emisyon-yogunlugu
term: "Emisyon yoğunluğu"
en: "emission intensity"
definition: "Birim ürün veya birim ciro başına sera gazı emisyonu."
see_also: [kapsam-1-2-emisyon, skdm]
cards: [kb-eco-40-4-environmental-taxes-cbam]
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

## Enflasyon beklentisi

```yaml
id: enflasyon-beklentisi
term: "Enflasyon beklentisi"
en: "inflation expectations"
definition: "Piyasa katılımcılarının gelecekteki enflasyon oranına ilişkin tahmini."
see_also: [reel-faiz]
cards: [kb-eco-21-1-monetary-policy-tcmb]
```

## Enflasyon düzeltmesi

```yaml
id: enflasyon-duzeltmesi
term: "Enflasyon düzeltmesi"
en: "Inflation adjustment"
definition: "Parasal olmayan kalemlerin fiyat endeksiyle yeniden ifade edilerek mali tabloların enflasyon etkisinden arındırılması."
see_also: [paralel-defter]
cards: [kb-ea-22-2-multi-currency-inflation-adjust-in-erp, kb-eco-35-2-inflation-accounting]
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

## Erişim sırası

```yaml
id: erisim-sirasi
term: "Erişim sırası"
en: "Access sequence"
definition: "Sistemin bir koşul kaydını hangi anahtarlarla ve hangi öncelikle arayacağını belirleyen sıra."
see_also: [kosul-teknigi]
cards: [kb-ea-27-1-pricing-engine-conditions]
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

## ERP (kurumsal kaynak planlama)

```yaml
id: erp
term: "ERP (kurumsal kaynak planlama)"
en: "enterprise resource planning"
definition: "Satış, stok, satın alma ve muhasebeyi ortak bir veritabanında birleştiren iş yazılımı."
see_also: [sfa]
cards: [kb-ea-1-1-what-is-an-enterprise-system, kb-ea-18-3-why-erp-projects-fail, kb-ea-18-4-post-go-live-dip, kb-ea-20-1-what-erp-does, kb-ea-20-2-order-to-cash, kb-ea-21-3-erp-market-turkey, kb-ea-3-2-it-plus-process-complementarity, kb-ea-5-4-application-portfolio, kb-ea-5-5-erp-core-vs-best-of-breed, kb-ea-6-4-internal-controls-sod, kb-ea-9-1-reporting-vs-transaction-systems, kb-fmcg-11-6-sop-ibp, kb-fmcg-12-2-change-digital-transformation, kb-fmcg-8-10-sfa-data-driven-selling]
```

## Esnek bütçe

```yaml
id: esnek-butce
term: "Esnek bütçe"
en: "flexible budget"
definition: "Gerçekleşen faaliyet hacmine göre yeniden hesaplanan bütçe; maliyet karşılaştırmalarında hacim etkisini ayıklar."
see_also: [maliyet-sapmasi]
cards: [kb-eco-39-4-budgeting-standard-costs]
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

## Faaliyet kaldıracı

```yaml
id: faaliyet-kaldiraci
term: "Faaliyet kaldıracı"
en: "Operating leverage"
definition: "Sabit giderler nedeniyle faaliyet kârının satış hacmindeki değişime oransal olarak daha güçlü tepki vermesi."
see_also: [basabas-noktasi]
cards: [kb-fmcg-12-7-case-distributor-turnaround, kb-fmcg-2-3-contribution-breakeven]
```

## Faaliyet kârı

```yaml
id: faaliyet-kari
term: "Faaliyet kârı"
en: "operating profit"
definition: "Brüt kârdan faaliyet giderlerinin düşülmesiyle bulunan, finansman ve vergi öncesi kâr."
see_also: [brut-kar, favok]
cards: [kb-eco-33-4-income-statement]
```

## Faaliyet raporu

```yaml
id: faaliyet-raporu
term: "Faaliyet raporu"
en: "annual report"
definition: "Şirket yönetiminin yıllık faaliyetleri, riskleri ve finansal durumu hakkında hazırladığı rapor."
see_also: [bilanco]
cards: [kb-eco-33-7-reading-annual-report]
```

## Faaliyet tabanlı maliyetleme

```yaml
id: faaliyet-tabanli-maliyetleme
term: "Faaliyet tabanlı maliyetleme"
en: "activity-based costing (ABC)"
definition: "Genel giderleri önce faaliyetlere, sonra maliyet sürücülerine göre ürün veya müşterilere dağıtan maliyet yöntemi."
see_also: [hizmet-maliyeti, maliyet-surucusu]
cards: [kb-eco-39-2-product-costing, kb-eco-39-3-abc-customer-profitability]
```

## Faiz karşılama oranı

```yaml
id: faiz-karsilama-orani
term: "Faiz karşılama oranı"
en: "interest coverage ratio"
definition: "Faaliyet kârının faiz giderine oranı; şirketin faizini kaç kez karşılayabildiğini gösterir."
see_also: [finansal-kaldirac]
cards: [kb-eco-31-4-debt-vs-equity, kb-eco-36-4-ratios-profitability-leverage]
```

## Fark-içinde-fark

```yaml
id: fark-icinde-fark
term: "Fark-içinde-fark"
en: "difference-in-differences"
definition: "Uygulama grubundaki değişimden kontrol grubundaki değişimi çıkararak uygulamanın etkisini tahmin eden yöntem."
see_also: [kontrol-grubu, paralel-egilim]
cards: [kb-eco-48-7-test-vs-control-did]
```

## Farklılaşma

```yaml
id: farklilasma
term: "Farklılaşma"
en: "differentiation"
definition: "Tüketicinin değer verdiği ve fazladan ödemeye razı olduğu bir fark sunarak rekabet etme stratejisi."
see_also: [fiyat-primi, maliyet-liderligi]
cards: [kb-fmcg-4-3-competitive-strategy]
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

## FAVÖK

```yaml
id: favok
term: "FAVÖK"
en: "EBITDA"
definition: "Faiz, vergi, amortisman ve itfa öncesi kâr."
see_also: [firma-degeri]
cards: [kb-eco-26-4-business-valuation-basics, kb-eco-33-4-income-statement, kb-eco-34-5-leases-ifrs16]
```

## Faydalı ömür

```yaml
id: faydali-omur
term: "Faydalı ömür"
en: "useful life"
definition: "Bir duran varlığın işletmede kullanılması beklenen süre; amortismanın dağıtıldığı dönem."
see_also: [amortisman]
cards: [kb-eco-34-3-fixed-assets-depreciation]
```

## Fırsat maliyeti

```yaml
id: firsat-maliyeti
term: "Fırsat maliyeti"
en: "opportunity cost"
definition: "Bir seçenek için vazgeçilen en iyi alternatifin değeri."
see_also: [batik-maliyet]
cards: [kb-eco-1-1-opportunity-cost-sunk-cost, kb-eco-39-5-relevant-costs-decisions]
```

## Finansal kaldıraç

```yaml
id: finansal-kaldirac
term: "Finansal kaldıraç"
en: "financial leverage"
definition: "Varlıkların bir kısmının borçla finanse edilmesi ve bunun özkaynak getirisi ile riskine etkisi."
see_also: [faiz-karsilama-orani]
cards: [kb-eco-31-4-debt-vs-equity, kb-eco-36-5-dupont]
```

## Finansal sıkıntı

```yaml
id: finansal-sikinti
term: "Finansal sıkıntı"
en: "financial distress"
definition: "Bir şirketin borçlarını vadesinde ödemekte zorlandığı ve iflas riskinin arttığı durum."
see_also: [z-skoru]
cards: [kb-eco-37-4-distress-signals-z-score]
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

## Firma değeri

```yaml
id: firma-degeri
term: "Firma değeri"
en: "enterprise value"
definition: "Şirket faaliyetlerinin tümünün değeri; özkaynak değeri ile net borcun toplamı."
see_also: [favok]
cards: [kb-eco-26-4-business-valuation-basics, kb-eco-31-8-mergers-acquisitions]
```

## Fisher denklemi

```yaml
id: fisher-denklemi
term: "Fisher denklemi"
en: "Fisher equation"
definition: "Nominal faiz, reel faiz ve beklenen enflasyon arasındaki ilişki: (1 + i) = (1 + r) × (1 + πᵉ)."
see_also: [reel-faiz]
cards: [kb-eco-18-3-real-vs-nominal-interest-fisher]
```

## Fiyat farklılaştırma

```yaml
id: fiyat-farklilastirma
term: "Fiyat farklılaştırma"
en: "price discrimination"
definition: "Aynı ürünü maliyet farkıyla açıklanamayan farklı fiyatlardan farklı müşterilere satmak."
see_also: [marj]
cards: [kb-eco-6-4-price-discrimination]
```

## Fiyat-hacim-karma analizi

```yaml
id: fiyat-hacim-karma-analizi
term: "Fiyat-hacim-karma analizi"
en: "Price-volume-mix analysis"
definition: "Gelir veya kâr farkını hacim, ürün karması, fiyat ve maliyet etkilerine ayıran analiz."
see_also: [katki-payi]
cards: [kb-fmcg-2-6-price-volume-mix-variance, kb-fmcg-5-7-rgm-system]
```

## Fiyat-paket mimarisi

```yaml
id: fiyat-paket-mimarisi
term: "Fiyat-paket mimarisi"
en: "price pack architecture"
definition: "Ambalaj boyutlarını, fiyat noktalarını ve kanalları birlikte planlama."
see_also: [birim-fiyat]
cards: [kb-fmcg-5-3-price-pack-architecture]
```

## Fiyat primi

```yaml
id: fiyat-primi
term: "Fiyat primi"
en: "price premium"
definition: "Bir markanın rakip ya da mağaza markasına göre aldığı yüzde fiyat farkı."
see_also: [magaza-markali-urun, marka-degeri]
cards: [kb-fmcg-3-5-brand-equity, kb-fmcg-9-2-formats-private-label]
```

## Fiyat şelalesi

```yaml
id: fiyat-selalesi
term: "Fiyat şelalesi"
en: "Price waterfall"
definition: "Liste fiyatından başlayarak her indirim ve desteği sırayla düşüp cep fiyatına ulaşan gösterim."
see_also: [cep-fiyati, ticari-harcama]
cards: [kb-ea-27-1-pricing-engine-conditions, kb-fmcg-10-1-key-account-management, kb-fmcg-10-2-trade-terms, kb-fmcg-2-2-gross-to-net]
```

## Fiziksel bulunurluk

```yaml
id: fiziksel-bulunurluk
term: "Fiziksel bulunurluk"
en: "physical availability"
definition: "Ürünün satın alma anında bulunabilmesi, görülebilmesi ve kolayca satın alınabilmesi."
see_also: [raf-bulunurlugu, sayisal-dagitim, zihinsel-bulunurluk]
cards: [kb-fmcg-12-6-case-brand-growth-plan, kb-fmcg-3-4-mental-physical-availability]
```

## Geçici vergi

```yaml
id: gecici-vergi
term: "Geçici vergi"
en: "advance tax payment"
definition: "Yıl içindeki dönem kârları üzerinden peşin ödenen ve yıllık gelir veya kurumlar vergisinden mahsup edilen vergi."
see_also: [kurumlar-vergisi]
cards: [kb-eco-43-3-corporate-tax]
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

## Gelir büyüme yönetimi

```yaml
id: gelir-buyume-yonetimi
term: "Gelir büyüme yönetimi"
en: "revenue growth management"
definition: "Fiyat, paket, karma, promosyon ve ticari koşulları net gelir ve kâr için birlikte yönetme yaklaşımı."
see_also: [fiyat-paket-mimarisi, ticari-harcama]
cards: [kb-fmcg-5-7-rgm-system]
```

## Gelir tablosu

```yaml
id: gelir-tablosu
term: "Gelir tablosu"
en: "income statement"
definition: "Bir dönemdeki satışları, maliyetleri, giderleri ve kârı gösteren finansal tablo."
see_also: [bilanco]
cards: [kb-eco-33-4-income-statement]
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

## Genel üretim gideri

```yaml
id: genel-uretim-gideri
term: "Genel üretim gideri"
en: "manufacturing overhead"
definition: "Ürüne doğrudan izlenemeyen, birden fazla ürüne ortak üretim giderleri; bakım, kurulum ve kalite kontrol gibi."
see_also: [faaliyet-tabanli-maliyetleme]
cards: [kb-eco-39-2-product-costing]
```

## genişletilmiş üretici sorumluluğu

```yaml
id: uretici-sorumlulugu
term: "genişletilmiş üretici sorumluluğu"
en: "extended producer responsibility"
definition: "Ürünü piyasaya süren işletmenin, ürünün ve ambalajının kullanım sonrası toplanması ve geri kazanımından mali ya da operasyonel olarak sorumlu tutulması ilkesi."
see_also: []
cards: [kb-fmcg-12-4-sustainability-regulation]
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

## Geri dönüş planı

```yaml
id: geri-donus-plani
term: "Geri dönüş planı"
en: "rollback plan"
definition: "Canlıya geçiş başarısız olursa eski sisteme hangi koşulda ve nasıl dönüleceğini belirleyen plan."
see_also: [canliya-gecis]
cards: [kb-ea-41-5-cutover-plan]
```

## Geri ödeme süresi

```yaml
id: geri-odeme-suresi
term: "Geri ödeme süresi"
en: "Payback period"
definition: "Bir yatırımın kendi nakit akışlarıyla kendini geri ödemesi için geçen süre."
see_also: [net-bugunku-deger]
cards: [kb-eco-31-1-capital-budgeting, kb-fmcg-2-4-roi-roce-npv, kb-fmcg-6-6-horeca]
```

## Gider tahakkuku

```yaml
id: gider-tahakkuku
term: "Gider tahakkuku"
en: "accrued expense"
definition: "Döneme ait olduğu hâlde henüz ödenmemiş ya da faturası gelmemiş bir giderin tahmini tutarla kaydedilmesi."
see_also: [tahakkuk-esasi]
cards: [kb-eco-33-3-accruals-period-close]
```

## Görevler ayrılığı

```yaml
id: gorevler-ayriligi
term: "Görevler ayrılığı"
en: "segregation of duties (SoD)"
definition: "Bir işlemin başlatılması, onaylanması ve kaydedilmesinin farklı kişilerce yapılması ilkesi."
see_also: [is-akisi]
cards: [kb-ea-15-2-user-roles-permissions, kb-ea-20-3-procure-to-pay, kb-ea-4-9-workflow-approvals, kb-ea-6-4-internal-controls-sod]
```

## GSYH

```yaml
id: gsyh
term: "GSYH"
en: "gross domestic product"
definition: "Bir ülkede belirli bir dönemde üretilen nihai mal ve hizmetlerin piyasa değeri."
see_also: [deflator]
cards: [kb-eco-14-1-gdp-real-nominal]
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

## Gün sonu mutabakatı

```yaml
id: gun-sonu-mutabakati
term: "Gün sonu mutabakatı"
en: "End-of-day reconciliation"
definition: "Gün sonunda stok ve kasanın sayılarak sistem kayıtlarıyla karşılaştırılması."
see_also: [aractan-satis, z-raporu]
cards: [kb-ea-26-5-van-sales-presales]
```

## Güven aralığı

```yaml
id: guven-araligi
term: "Güven aralığı"
en: "confidence interval"
definition: "Bir tahminin etrafında, belirli bir güven düzeyiyle gerçek değeri kapsaması beklenen aralık."
see_also: [hata-payi, standart-hata]
cards: [kb-eco-47-3-sampling-confidence]
```

## Güvenli elektronik imza

```yaml
id: guvenli-elektronik-imza
term: "Güvenli elektronik imza"
en: "qualified electronic signature"
definition: "Nitelikli sertifikaya dayanan ve kişiye bağlı elektronik imza."
see_also: [kep, mali-muhur]
cards: [kb-ea-35-2-e-signature-kep-seal]
```

## Güvenlik stoku (emniyet stoğu)

```yaml
id: guvenlik-stoku
term: "Güvenlik stoku (emniyet stoğu)"
en: "safety stock"
definition: "Talep ve tedarik süresindeki belirsizliğe karşı, beklenen tüketimin üzerinde tutulan ek stok."
see_also: [drp, tahmin-hatasi, yeniden-siparis-noktasi]
cards: [kb-ea-29-3-drp-inventory-planning, kb-fmcg-11-2-demand-forecasting, kb-fmcg-11-3-eoq-reorder-point, kb-fmcg-11-4-safety-stock, kb-fmcg-11-5-bullwhip-effect, kb-fmcg-11-6-sop-ibp, kb-fmcg-11-7-warehouse-transport-network]
```

## Haksız ticari uygulama

```yaml
id: haksiz-ticari-uygulama
term: "Haksız ticari uygulama"
en: "Unfair trading practice"
definition: "6585 sayılı Kanun'un tedarikçiye karşı yasakladığı uygulamalar; karşılıksız ücret, istenmeyen kampanya maliyeti yükleme, tek taraflı şart değişikliği gibi."
see_also: [zincir-magaza]
cards: [kb-fmcg-1-5-turkish-fmcg-landscape, kb-fmcg-10-2-trade-terms, kb-fmcg-12-5-ethics-compliance-trade]
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

## Hareket tipi

```yaml
id: hareket-tipi
term: "Hareket tipi"
en: "Movement type"
definition: "ERP'de bir stok hareketinin türünü ve muhasebe etkisini belirleyen kod."
see_also: [hareketli-ortalama-maliyet]
cards: [kb-ea-20-5-inventory-in-erp]
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

## Hasılat

```yaml
id: hasilat
term: "Hasılat"
en: "revenue"
definition: "Mal ve hizmet satışından elde edilen, KDV hariç gelir."
see_also: [net-satis]
cards: [kb-eco-33-2-double-entry-basics]
```

## Hata payı

```yaml
id: hata-payi
term: "Hata payı"
en: "margin of error"
definition: "Güven aralığının yarı genişliği; örneklem tahmininin belirsizliğinin ölçüsü."
see_also: [guven-araligi]
cards: [kb-eco-47-3-sampling-confidence]
```

## Hazine bonosu

```yaml
id: hazine-bonosu
term: "Hazine bonosu"
en: "treasury bill"
definition: "Hazinenin bir yıldan kısa vadeli, genellikle iskontolu satılan borçlanma aracı."
see_also: [devlet-tahvili]
cards: [kb-eco-25-6-bond-types-treasury-instruments]
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

## Herfindahl-Hirschman Endeksi (HHI)

```yaml
id: hhi
term: "Herfindahl-Hirschman Endeksi (HHI)"
en: "Herfindahl-Hirschman Index"
definition: "Bir pazardaki tüm firmaların yüzde cinsinden pazar paylarının karelerinin toplamı; 0 ile 10.000 arasında değişen yoğunlaşma ölçüsü."
see_also: [cr4]
cards: [kb-fmcg-1-2-scale-and-concentration]
```

## Hesap ekstresi

```yaml
id: hesap-ekstresi
term: "Hesap ekstresi"
en: "Bank statement"
definition: "Banka hesabındaki hareketlerin dönemsel dökümü; ERP'ye standart biçimlerle aktarılabilir."
see_also: [iso-20022, otomatik-eslestirme]
cards: [kb-ea-24-2-bank-statement-integration]
```

## Hesap eşleştirme

```yaml
id: hesap-eslestirme
term: "Hesap eşleştirme"
en: "Account determination"
definition: "ERP'de bir işlem tipinin hangi muhasebe hesaplarına kaydedileceğini belirleyen kurallar."
see_also: [genel-muhasebe, tekduzen-hesap-plani]
cards: [kb-ea-22-1-chart-of-accounts-tekduzen]
```

## Hızlandırıcı

```yaml
id: hizlandirici
term: "Hızlandırıcı"
en: "accelerator"
definition: "Prim planında hedefin üstündeki her gerçekleşme puanının, hedefin altındakinden daha yüksek oranda ödüllendirilmesi."
see_also: [degisken-ucret]
cards: [kb-fmcg-8-12-salesperson-motivation, kb-fmcg-8-8-incentive-compensation]
```

## Hızlı ticaret

```yaml
id: hizli-ticaret
term: "Hızlı ticaret"
en: "quick commerce"
definition: "Şehir içi küçük depolardan dakikalar içinde teslimat yapan çevrim içi satış modeli."
see_also: [sepet-buyuklugu]
cards: [kb-fmcg-6-7-e-grocery-quick-commerce]
```

## Hizmet maliyeti

```yaml
id: hizmet-maliyeti
term: "Hizmet maliyeti"
en: "Cost-to-serve"
definition: "Bir müşteriye ya da satış noktasına satış yapmanın ziyaret, sipariş işleme, teslimat, vade ve tahsilat dahil toplam maliyeti."
see_also: [marj, minimum-siparis-buyuklugu]
cards: [kb-eco-39-3-abc-customer-profitability, kb-eco-7-5-auctions-tenders, kb-fmcg-1-1-margin-stack, kb-fmcg-10-1-key-account-management, kb-fmcg-11-7-warehouse-transport-network, kb-fmcg-11-8-cold-chain, kb-fmcg-12-7-case-distributor-turnaround, kb-fmcg-13-4-b2b-buying-behaviour, kb-fmcg-6-3-cost-to-serve, kb-fmcg-6-8-rtm-design-case, kb-fmcg-7-1-distributor-pnl]
```

## Hizmet seviyesi anlaşması (SLA)

```yaml
id: sla
term: "Hizmet seviyesi anlaşması (SLA)"
en: "service level agreement"
definition: "Bir hizmetin erişilebilirlik, yanıt ve çözüm sürelerini ölçülebilir biçimde tanımlayan anlaşma."
see_also: []
cards: [kb-ea-17-4-vendor-selection-rfp, kb-ea-19-3-working-with-it-partners, kb-ea-25-5-customer-service-cases, kb-ea-6-2-it-service-sla]
```

## Horeca

```yaml
id: horeca
term: "Horeca"
en: "hotel, restaurant, café"
definition: "Ürünün evde değil dışarıda tüketildiği otel, restoran, kafe ve benzeri noktalardan oluşan kanal."
see_also: []
cards: [kb-fmcg-6-6-horeca]
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

## İç verim oranı

```yaml
id: ic-verim-orani
term: "İç verim oranı"
en: "internal rate of return, IRR"
definition: "Bir yatırımın nakit akışlarının net bugünkü değerini sıfır yapan iskonto oranı."
see_also: [iskonto-orani, net-bugunku-deger]
cards: [kb-eco-25-1-time-value-npv-irr, kb-eco-31-1-capital-budgeting]
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

## İleti Yönetim Sistemi (İYS)

```yaml
id: iys
term: "İleti Yönetim Sistemi (İYS)"
en: "Message management system"
definition: "Ticari elektronik ileti onay ve retlerinin kaydedildiği ulusal sistem."
see_also: [kvkk, ticari-elektronik-ileti]
cards: [kb-ea-25-4-consent-iys-marketing]
```

## İlgili maliyet

```yaml
id: ilgili-maliyet
term: "İlgili maliyet"
en: "relevant cost"
definition: "Bir kararla birlikte değişen, gelecekte katlanılacak maliyet; batık maliyetler ve değişmeyen sabit giderler dahil değildir."
see_also: [batik-maliyet, firsat-maliyeti]
cards: [kb-eco-39-5-relevant-costs-decisions]
```

## İlişkili taraf işlemi

```yaml
id: iliskili-taraf-islemi
term: "İlişkili taraf işlemi"
en: "related-party transaction"
definition: "Şirketin ortakları, yöneticileri veya onlara bağlı kişi ve şirketlerle yaptığı işlem."
see_also: [vekalet-maliyeti]
cards: [kb-eco-31-5-agency-governance-family-firm, kb-eco-33-7-reading-annual-report, kb-eco-36-7-earnings-quality-red-flags]
```

## İlk giren ilk çıkar (FIFO)

```yaml
id: fifo
term: "İlk giren ilk çıkar (FIFO)"
en: "first in, first out"
definition: "Satılan malın en eski alımların maliyetiyle hesaplandığı stok maliyet yöntemi."
see_also: [agirlikli-ortalama-maliyet]
cards: [kb-eco-34-1-inventory-valuation]
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

## İmha politikası

```yaml
id: imha-politikasi
term: "İmha politikası"
en: "Disposal policy"
definition: "Süresi dolan belge ve kişisel verilerin nasıl ve kimin onayıyla yok edileceğini belirleyen kurallar."
see_also: [saklama-suresi]
cards: [kb-ea-35-1-document-archive-retention]
```

## İndirilecek KDV

```yaml
id: indirilecek-kdv
term: "İndirilecek KDV"
en: "input VAT"
definition: "Alış ve gider faturalarında ödenen ve hesaplanan KDV'den indirilebilen KDV."
see_also: [devreden-kdv]
cards: [kb-eco-43-4-kdv-vat]
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

## İskonto oranı

```yaml
id: iskonto-orani
term: "İskonto oranı"
en: "discount rate"
definition: "Gelecekteki nakit akışlarını bugünkü değere çevirmek için kullanılan getiri oranı."
see_also: [net-bugunku-deger]
cards: [kb-eco-25-1-time-value-npv-irr]
```

## İstatistiksel anlamlılık

```yaml
id: istatistiksel-anlamlilik
term: "İstatistiksel anlamlılık"
en: "statistical significance"
definition: "Gözlenen farkın şansla açıklanamayacak kadar büyük olması; genellikle p-değerinin önceden belirlenen eşiğin altında kalmasıyla ifade edilir."
see_also: [p-degeri]
cards: [kb-eco-47-4-ab-testing-significance]
```

## İstatistiksel güç

```yaml
id: istatistiksel-guc
term: "İstatistiksel güç"
en: "statistical power"
definition: "Gerçekte var olan bir etkiyi testin yakalama olasılığı."
see_also: [ab-testi]
cards: [kb-eco-47-4-ab-testing-significance]
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

## İş süreci

```yaml
id: is-sureci
term: "İş süreci"
en: "business process"
definition: "Bir tetikleyiciyle başlayıp müşteri ya da iç kullanıcı için sonuç üreten, birimler arası faaliyetler zinciri."
see_also: [bpm, siparisten-tahsilata]
cards: [kb-ea-3-2-it-plus-process-complementarity, kb-ea-4-1-what-is-a-process, kb-ea-4-2-bpm-lifecycle, kb-ea-4-3-process-maps-bpmn]
```

## İş süreci yönetimi (BPM)

```yaml
id: bpm
term: "İş süreci yönetimi (BPM)"
en: "business process management"
definition: "Süreçleri belirleme, keşif, analiz, yeniden tasarım, uygulama ve izleme döngüsüyle yönetme yaklaşımı."
see_also: [bpmn, is-sureci]
cards: [kb-ea-4-2-bpm-lifecycle]
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

## işbirlikçi planlama, tahmin ve yenileme

```yaml
id: isbirlikci-planlama
term: "işbirlikçi planlama, tahmin ve yenileme"
en: "collaborative planning, forecasting and replenishment (CPFR)"
definition: "Tedarikçi ile perakendecinin ortak bir tahmin ve yenileme planı üzerinde anlaşıp sapmaları birlikte yönettiği süreç."
see_also: [ortak-is-plani, tedarikci-yonetimli-stok]
cards: [kb-fmcg-11-9-vmi-cpfr]
```

## İşletme sermayesi (net)

```yaml
id: isletme-sermayesi
term: "İşletme sermayesi (net)"
en: "net working capital"
definition: "Ticari alacaklar ve stoklar toplamından ticari borçların düşülmesiyle bulunan, faaliyete bağlanmış para."
see_also: [nakit-donusum-suresi]
cards: [kb-eco-31-9-three-statement-model, kb-eco-33-5-balance-sheet, kb-eco-33-6-cash-flow-statement, kb-eco-36-6-cash-flow-vs-profit, kb-eco-38-2-cash-conversion-cycle, kb-eco-50-4-tcmb-policy-rate-credit, kb-fmcg-11-1-supply-chain-basics, kb-fmcg-2-4-roi-roce-npv, kb-fmcg-7-2-distributor-roi, kb-fmcg-7-3-credit-collections-dso]
```

## İşveren maliyeti

```yaml
id: isveren-maliyeti
term: "İşveren maliyeti"
en: "total employer cost"
definition: "Brüt ücrete işveren primleri ve ek ödemeler eklenerek bulunan toplam personel maliyeti."
see_also: []
cards: [kb-eco-44-3-sgk-employer-costs, kb-eco-9-2-minimum-wage-labour-costs]
```

## İzlenebilirlik

```yaml
id: izlenebilirlik
term: "İzlenebilirlik"
en: "Traceability"
definition: "Bir partinin nereden geldiğinin ve nereye gittiğinin kayıtlarla gösterilebilmesi."
see_also: [geri-cagirma, parti-takibi]
cards: [kb-ea-30-4-barcodes-traceability, kb-ea-32-2-food-safety-traceability]
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

## Kademeli hatırlatma

```yaml
id: kademeli-hatirlatma
term: "Kademeli hatırlatma"
en: "Dunning"
definition: "Vadesi geçen alacaklar için adım adım artan hatırlatma ve yaptırım süreci."
see_also: [kredi-limiti]
cards: [kb-ea-24-3-credit-limits-collections-systems]
```

## kamçı etkisi

```yaml
id: kamci-etkisi
term: "kamçı etkisi"
en: "bullwhip effect"
definition: "Tüketici talebindeki küçük dalgalanmaların, tedarik zincirinde yukarı doğru çıkıldıkça siparişlerde giderek büyüyen dalgalanmalara dönüşmesi."
see_also: [satis-ve-operasyon-planlamasi, tahmin-hatasi]
cards: [kb-fmcg-11-5-bullwhip-effect, kb-fmcg-11-9-vmi-cpfr]
```

## Kanal çatışması

```yaml
id: kanal-catismasi
term: "Kanal çatışması"
en: "Channel conflict"
definition: "Kanal üyeleri arasında hedef, alan (bölge, müşteri) ya da algı farkından doğan anlaşmazlık."
see_also: [kanal-gucu]
cards: [kb-fmcg-1-4-channel-power-conflict, kb-fmcg-7-5-distributor-development]
```

## Kanal gücü

```yaml
id: kanal-gucu
term: "Kanal gücü"
en: "Channel power"
definition: "Bir kanal üyesinin diğerinin kararlarını etkileyebilme kapasitesi; büyük ölçüde karşı tarafın ona bağımlılığından doğar."
see_also: [kanal-catismasi]
cards: [kb-fmcg-1-4-channel-power-conflict, kb-fmcg-10-4-negotiating-with-chains, kb-fmcg-12-5-ethics-compliance-trade, kb-fmcg-4-3-competitive-strategy]
```

## Kanal işlevleri

```yaml
id: kanal-islevleri
term: "Kanal işlevleri"
en: "Channel functions"
definition: "Ürünün tüketiciye ulaşması için birinin üstlenmesi gereken işler: stok tutma, bölme, kredi, taşıma, satış, raf düzeni ve bilgi toplama."
see_also: [bayi, toptanci]
cards: [kb-fmcg-1-3-channel-actors, kb-fmcg-6-1-rtm-channels-formats, kb-fmcg-6-5-wholesale-cash-carry]
```

## Kanunen kabul edilmeyen gider (KKEG)

```yaml
id: kkeg
term: "Kanunen kabul edilmeyen gider (KKEG)"
en: "non-deductible expense"
definition: "Muhasebede gider yazılan ancak vergi matrahının hesabında indirilemeyen tutarlar."
see_also: [kurumlar-vergisi]
cards: [kb-eco-43-3-corporate-tax]
```

## Kapsam 1 ve kapsam 2 emisyonları

```yaml
id: kapsam-1-2-emisyon
term: "Kapsam 1 ve kapsam 2 emisyonları"
en: "scope 1 and scope 2 emissions"
definition: "Kapsam 1, şirketin kendi kaynaklarından doğrudan emisyon; kapsam 2, satın alınan elektrik ve ısıdan kaynaklanan dolaylı emisyondur."
see_also: [emisyon-yogunlugu]
cards: [kb-eco-54-3-governance-sustainability-reporting]
```

## Kapsam ekonomisi

```yaml
id: kapsam-ekonomisi
term: "Kapsam ekonomisi"
en: "economies of scope"
definition: "Birden fazla ürünü aynı kaynakla üretmenin veya dağıtmanın ayrı ayrı yapmaktan ucuz olması."
see_also: [olcek-ekonomisi]
cards: [kb-eco-5-5-economies-of-scale-sunk-costs]
```

## Karbon fiyatlaması

```yaml
id: karbon-fiyatlamasi
term: "Karbon fiyatlaması"
en: "carbon pricing"
definition: "Sera gazı emisyonuna vergi veya emisyon ticareti yoluyla bir fiyat biçilmesi."
see_also: [dissallik, skdm]
cards: [kb-eco-40-4-environmental-taxes-cbam]
```

## Karşılık

```yaml
id: karsilik
term: "Karşılık"
en: "provision"
definition: "Zamanı veya tutarı belirsiz olan, ödenmesi muhtemel bir yükümlülük için tahmini tutarla ayrılan borç kaydı."
see_also: [kosullu-borc]
cards: [kb-eco-34-7-provisions-severance]
```

## Kartel

```yaml
id: kartel
term: "Kartel"
en: "cartel"
definition: "Rakiplerin fiyat, miktar, bölge veya müşteri konusunda anlaşması; rekabet hukukunda yasaktır."
see_also: [oligopol]
cards: [kb-eco-7-7-oligopoly-collusion]
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

## kategori yönetimi

```yaml
id: kategori-yonetimi
term: "kategori yönetimi"
en: "category management"
definition: "Perakendeci ile tedarikçinin bir ürün kategorisini, tek tek markalar yerine kategorinin toplam satış ve kârını büyütecek biçimde birlikte yönetmesi."
see_also: [kilit-musteri-yonetimi, planogram]
cards: [kb-fmcg-10-6-category-management, kb-fmcg-10-7-joint-business-planning, kb-fmcg-13-2-strategic-selling, kb-fmcg-13-5-retail-buyer-decisions]
```

## Katkı payı

```yaml
id: katki-payi
term: "Katkı payı"
en: "Contribution margin"
definition: "Satış gelirinden değişken maliyetler düşüldükten sonra sabit giderleri karşılamaya ve kâra kalan tutar."
see_also: [basabas-noktasi, degisken-maliyet]
cards: [kb-eco-39-5-relevant-costs-decisions, kb-fmcg-1-4-channel-power-conflict, kb-fmcg-11-6-sop-ibp, kb-fmcg-13-4-b2b-buying-behaviour, kb-fmcg-13-5-retail-buyer-decisions, kb-fmcg-2-1-fmcg-pnl, kb-fmcg-2-3-contribution-breakeven, kb-fmcg-2-6-price-volume-mix-variance, kb-fmcg-4-4-portfolio-management, kb-fmcg-4-6-sku-rationalisation, kb-fmcg-5-1-price-elasticity, kb-fmcg-5-4-promotion-economics, kb-fmcg-5-6-pricing-in-high-inflation, kb-fmcg-6-6-horeca, kb-fmcg-7-1-distributor-pnl, kb-fmcg-8-4-sales-force-sizing, kb-fmcg-8-8-incentive-compensation]
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

## Kayıptan kaçınma

```yaml
id: kayiptan-kacinma
term: "Kayıptan kaçınma"
en: "Loss aversion"
definition: "Bir kaybın, aynı büyüklükteki bir kazançtan daha güçlü hissedilmesi eğilimi."
see_also: [capalama]
cards: [kb-eco-13-1-heuristics-biases, kb-fmcg-13-6-persuasion-science, kb-fmcg-13-7-behavioural-economics-selling, kb-fmcg-3-1-consumer-decisions]
```

## Kayıt dışı ekonomi

```yaml
id: kayit-disi-ekonomi
term: "Kayıt dışı ekonomi"
en: "informal economy"
definition: "Vergi ve sosyal güvenlik kayıtlarına yansıtılmayan ekonomik faaliyetler."
see_also: [vergi-uyumu]
cards: [kb-eco-42-8-informality-tax-compliance]
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

## Kazananın laneti

```yaml
id: kazananin-laneti
term: "Kazananın laneti"
en: "winner's curse"
definition: "İhaleyi kazananın, değeri veya maliyeti en iyimser tahmin eden taraf olması ve bu yüzden zarar etme eğilimi."
see_also: []
cards: [kb-eco-7-5-auctions-tenders]
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

## Kâr kalitesi

```yaml
id: kar-kalitesi
term: "Kâr kalitesi"
en: "earnings quality"
definition: "Raporlanan kârın nakde dönüşme ve gelecekte süreklilik gösterme derecesi."
see_also: [tahakkuk-orani]
cards: [kb-eco-36-7-earnings-quality-red-flags]
```

## KDV (Katma Değer Vergisi)

```yaml
id: kdv
term: "KDV (Katma Değer Vergisi)"
en: "value added tax (VAT)"
definition: "Mal ve hizmet teslimlerinde satış bedeli üzerinden hesaplanan, nihai tüketicinin yüklendiği vergi."
see_also: []
cards: [kb-eco-33-2-double-entry-basics, kb-eco-43-1-turkish-tax-system-overview, kb-eco-43-4-kdv-vat, kb-eco-43-5-otv-stamp-duty, kb-fmcg-1-1-margin-vs-markup, kb-fmcg-13-17-turkish-trade-practice]
```

## Kıdem tazminatı

```yaml
id: kidem-tazminati
term: "Kıdem tazminatı"
en: "severance pay"
definition: "Belirli koşullarla işten ayrılan çalışana, hizmet süresine bağlı olarak ödenen yasal tazminat."
see_also: [karsilik]
cards: [kb-eco-34-7-provisions-severance, kb-eco-44-3-sgk-employer-costs]
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

## kilit müşteri yönetimi

```yaml
id: kilit-musteri-yonetimi
term: "kilit müşteri yönetimi"
en: "key account management"
definition: "Satışın ve stratejik önemin yoğunlaştığı büyük müşterilerin, özel ekip, müşteri bazlı plan ve müşteri kâr-zararıyla yönetilmesi."
see_also: [kategori-yonetimi, ortak-is-plani]
cards: [kb-fmcg-10-1-key-account-management, kb-fmcg-10-4-negotiating-with-chains, kb-fmcg-10-7-joint-business-planning, kb-fmcg-12-4-sustainability-regulation, kb-fmcg-13-13-relationship-selling-trust, kb-fmcg-13-2-strategic-selling, kb-fmcg-13-3-challenger-meddic-sandler]
```

## Kira yükümlülüğü

```yaml
id: kira-yukumlulugu
term: "Kira yükümlülüğü"
en: "lease liability"
definition: "TFRS 16'da kiracının gelecekteki kira ödemelerinin bugünkü değeriyle kaydettiği borç."
see_also: [kullanim-hakki-varligi]
cards: [kb-eco-34-5-leases-ifrs16]
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

## Kontrol grubu

```yaml
id: kontrol-grubu
term: "Kontrol grubu"
en: "control group"
definition: "Bir deney veya analizde uygulamaya maruz kalmayan ve karşılaştırma için kullanılan grup."
see_also: [ab-testi, fark-icinde-fark]
cards: [kb-eco-48-7-test-vs-control-did]
```

## kontrollü deney

```yaml
id: kontrollu-deney
term: "kontrollü deney"
en: "controlled experiment"
definition: "Bir uygulamanın etkisini, uygulamanın yapıldığı test grubunu benzer bir kontrol grubuyla karşılaştırarak ölçme yöntemi."
see_also: [artimsal-hacim]
cards: [kb-fmcg-12-3-analytics-for-decisions]
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

## Konumlandırma

```yaml
id: konumlandirma
term: "Konumlandırma"
en: "positioning"
definition: "Hedef segmentin zihninde markanın rakiplere göre neyi temsil ettiğini belirleme."
see_also: [segmentasyon]
cards: [kb-fmcg-4-2-segmentation-positioning]
```

## Korelasyon

```yaml
id: korelasyon
term: "Korelasyon"
en: "correlation"
definition: "İki değişkenin doğrusal birlikte hareketinin yönü ve gücü; −1 ile +1 arasında ölçülür."
see_also: [regresyon]
cards: [kb-eco-47-5-correlation-regression-basics]
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

## Koşullu borç

```yaml
id: kosullu-borc
term: "Koşullu borç"
en: "contingent liability"
definition: "Gerçekleşmesi belirsiz gelecek olaylara bağlı olan ya da ödenmesi muhtemel olmayan, bu nedenle karşılık ayrılmayıp dipnotta açıklanan yükümlülük."
see_also: [karsilik]
cards: [kb-eco-34-7-provisions-severance]
```

## koşullu prim

```yaml
id: kosullu-prim
term: "koşullu prim"
en: "conditional rebate"
definition: "Yalnızca önceden belirlenmiş bir hedef (örneğin büyüme ya da bulunurluk) gerçekleştiğinde ödenen ticari prim."
see_also: [ciro-primi, ortak-is-plani]
cards: [kb-fmcg-10-2-trade-terms, kb-fmcg-10-4-negotiating-with-chains, kb-fmcg-10-7-joint-business-planning, kb-fmcg-13-14-negotiation-structure]
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

## Kredi bürosu

```yaml
id: kredi-burosu
term: "Kredi bürosu"
en: "credit bureau"
definition: "Finans kuruluşlarının kredi ve risk verilerini paylaştığı kuruluş."
see_also: [risk-raporu]
cards: [kb-ea-38-3-findeks-credit-bureau]
```

## Kredi limiti

```yaml
id: kredi-limiti
term: "Kredi limiti"
en: "Credit limit"
definition: "Bir müşteriye vadeli satışta izin verilen azami açık risk tutarı."
see_also: [dbs, kademeli-hatirlatma]
cards: [kb-ea-24-3-credit-limits-collections-systems, kb-eco-37-3-customer-credit-analysis, kb-eco-38-3-distributor-credit-risk-dbs, kb-eco-50-3-working-with-banks]
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

## Kullanıcı hikâyesi

```yaml
id: kullanici-hikayesi
term: "Kullanıcı hikâyesi"
en: "User story"
definition: "Bir ihtiyacın “rol, amaç, istek” kalıbında kısa anlatımı."
see_also: [kabul-kriteri]
cards: [kb-ea-17-3-writing-requirements]
```

## Kullanılan sermayenin getirisi (ROCE)

```yaml
id: roce
term: "Kullanılan sermayenin getirisi (ROCE)"
en: "Return on capital employed"
definition: "Faaliyet kârının, işletmede kullanılan duran varlıklar ve işletme sermayesi toplamına oranı."
see_also: [isletme-sermayesi, yatirimin-getirisi]
cards: [kb-eco-36-4-ratios-profitability-leverage, kb-eco-38-1-distributor-financial-statements, kb-fmcg-2-4-roi-roce-npv, kb-fmcg-7-2-distributor-roi]
```

## Kullanım hakkı varlığı

```yaml
id: kullanim-hakki-varligi
term: "Kullanım hakkı varlığı"
en: "right-of-use asset"
definition: "TFRS 16'da kiracının kiralanan varlığı kullanma hakkını temsil eden ve amortismana tabi tutulan varlık."
see_also: [kira-yukumlulugu]
cards: [kb-eco-34-5-leases-ifrs16]
```

## Kupon

```yaml
id: kupon
term: "Kupon"
en: "coupon"
definition: "Tahvil sahibine belirli dönemlerde ödenen faiz."
see_also: [devlet-tahvili]
cards: [kb-eco-25-6-bond-types-treasury-instruments]
```

## Kur farkı

```yaml
id: kur-farki
term: "Kur farkı"
en: "Exchange rate difference"
definition: "Dövizli bir işlemin kayıt ve ödeme ya da değerleme tarihleri arasındaki kur değişiminden doğan fark."
see_also: [kur-riski]
cards: [kb-ea-22-2-multi-currency-inflation-adjust-in-erp, kb-eco-34-8-fx-transactions]
```

## Kur riski

```yaml
id: kur-riski
term: "Kur riski"
en: "Foreign exchange risk"
definition: "Döviz kurlarındaki değişimin dövizli alacak, borç ve nakit akışlarının değerini etkileme riski."
see_also: [kur-farki]
cards: [kb-ea-24-1-treasury-cash-forecasting, kb-eco-23-2-currency-crises-business, kb-eco-25-2-loans-real-vs-nominal, kb-eco-30-1-forwards-fx-hedging, kb-eco-32-3-risk-management-stress-test, kb-eco-34-8-fx-transactions]
```

## Kurumlar vergisi

```yaml
id: kurumlar-vergisi
term: "Kurumlar vergisi"
en: "corporate income tax"
definition: "Sermaye şirketleri ve diğer kurumların kazancı üzerinden alınan vergi; 5520 sayılı Kanun ile düzenlenir."
see_also: [gecici-vergi, kkeg]
cards: [kb-eco-43-1-turkish-tax-system-overview, kb-eco-43-3-corporate-tax]
```

## Kurumsal bilgi sistemi

```yaml
id: kurumsal-bilgi-sistemi
term: "Kurumsal bilgi sistemi"
en: "enterprise system"
definition: "Bir firmanın birden çok biriminin işlerini ortak veri ve kurallarla yürüten yazılım ve süreçler bütünü."
see_also: [erp, sfa]
cards: [kb-ea-1-1-what-is-an-enterprise-system]
```

## Kurumsal yönetim

```yaml
id: kurumsal-yonetim
term: "Kurumsal yönetim"
en: "corporate governance"
definition: "Şirketin ortakları, yönetimi ve paydaşları arasındaki ilişkiyi; karar alma, denetim ve hesap verme düzenini belirleyen kurallar."
see_also: [vekalet-maliyeti]
cards: [kb-eco-54-3-governance-sustainability-reporting]
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

## Likidite tamponu

```yaml
id: likidite-tamponu
term: "Likidite tamponu"
en: "liquidity buffer"
definition: "Beklenmedik nakit açığını karşılamak için tutulan nakit ve kullanılabilir taahhütlü kredi limiti."
see_also: []
cards: [kb-eco-24-3-turkey-crises-lessons, kb-eco-32-3-risk-management-stress-test]
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

## Low-code platform

```yaml
id: low-code
term: "Low-code platform"
en: "low-code platform"
definition: "Görsel araçlarla az kod yazarak uygulama geliştirmeyi sağlayan platform."
see_also: [vatandas-gelistirici]
cards: [kb-ea-39-1-low-code]
```

## Mağaza markalı ürün

```yaml
id: magaza-markali-urun
term: "Mağaza markalı ürün"
en: "Private label / store brand"
definition: "Perakendecinin kendi markasıyla sattığı, çoğunlukla bir üreticiye fason ürettirilen ürün."
see_also: [zincir-magaza]
cards: [kb-fmcg-1-5-turkish-fmcg-landscape, kb-fmcg-3-5-brand-equity, kb-fmcg-9-2-formats-private-label]
```

## Mahkûmlar ikilemi

```yaml
id: mahkumlar-ikilemi
term: "Mahkûmlar ikilemi"
en: "prisoner's dilemma"
definition: "Her tarafın tek başına en iyi hamlesinin, toplamda herkes için daha kötü sonuç doğurduğu durum."
see_also: [nash-dengesi]
cards: [kb-eco-7-1-game-theory-for-managers]
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

## Mali mühür

```yaml
id: mali-muhur
term: "Mali mühür"
en: "fiscal seal"
definition: "Vergi mükellefi kuruma ait, e-belgeleri kurum adına imzalamakta kullanılan elektronik sertifika."
see_also: [guvenli-elektronik-imza]
cards: [kb-ea-35-2-e-signature-kep-seal, kb-ea-37-2-e-fatura-scenarios]
```

## Maliyet liderliği

```yaml
id: maliyet-liderligi
term: "Maliyet liderliği"
en: "cost leadership"
definition: "Sektördeki en düşük maliyetli üretici olarak rekabet avantajı kurma stratejisi."
see_also: [farklilasma]
cards: [kb-fmcg-4-3-competitive-strategy]
```

## Maliyet sapması

```yaml
id: maliyet-sapmasi
term: "Maliyet sapması"
en: "cost variance"
definition: "Gerçekleşen maliyet ile standart maliyet arasındaki fark; fiyat ve miktar sapmalarına ayrılabilir."
see_also: [esnek-butce]
cards: [kb-eco-39-4-budgeting-standard-costs]
```

## Maliyet sürücüsü

```yaml
id: maliyet-surucusu
term: "Maliyet sürücüsü"
en: "cost driver"
definition: "Bir faaliyetin maliyetini doğuran ölçülebilir etken; kurulum sayısı, sipariş sayısı veya teslimat sayısı gibi."
see_also: [faaliyet-tabanli-maliyetleme]
cards: [kb-eco-39-2-product-costing, kb-eco-39-3-abc-customer-profitability]
```

## Maliyet üzerine ekleme oranı

```yaml
id: maliyet-uzerine-ekleme-orani
term: "Maliyet üzerine ekleme oranı"
en: "markup"
definition: "Satış fiyatı ile maliyet arasındaki farkın maliyete oranı."
see_also: [marj]
cards: [kb-fmcg-1-1-margin-vs-markup]
```

## Malzeme ihtiyaç planlaması (MRP)

```yaml
id: mrp
term: "Malzeme ihtiyaç planlaması (MRP)"
en: "Material requirements planning"
definition: "Üretim planı, ürün ağacı ve stoktan malzeme ihtiyacını ve sipariş zamanını hesaplayan yöntem."
see_also: [ana-uretim-plani, tedarik-suresi, urun-agaci]
cards: [kb-ea-20-6-mrp-basics]
```

## MAPE

```yaml
id: mape
term: "MAPE"
en: "Mean absolute percentage error"
definition: "Tahmin ile gerçekleşen arasındaki mutlak farkın gerçekleşene oranının ortalaması."
see_also: [talep-planlama, tahmin-hatasi]
cards: [kb-ea-29-2-demand-planning-systems]
```

## Marj (kâr marjı)

```yaml
id: marj
term: "Marj (kâr marjı)"
en: "margin"
definition: "Satış fiyatı ile maliyet arasındaki farkın satış fiyatına oranı."
see_also: [maliyet-uzerine-ekleme-orani]
cards: [kb-eco-19-3-supply-shocks-cost-inflation, kb-eco-6-4-price-discrimination, kb-fmcg-1-1-margin-stack, kb-fmcg-1-1-margin-vs-markup]
```

## Marjinal vergi oranı

```yaml
id: marjinal-vergi-orani
term: "Marjinal vergi oranı"
en: "marginal tax rate"
definition: "Bir sonraki 1 birim gelire uygulanan vergi oranı."
see_also: [ortalama-vergi-orani]
cards: [kb-eco-42-1-tax-basics-average-marginal]
```

## Marka değeri

```yaml
id: marka-degeri
term: "Marka değeri"
en: "brand equity"
definition: "Marka bilgisinin, tüketicinin markanın pazarlama faaliyetlerine verdiği tepkide yarattığı fark."
see_also: [fiyat-primi]
cards: [kb-fmcg-3-5-brand-equity, kb-fmcg-9-2-formats-private-label]
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

## Medyan

```yaml
id: medyan
term: "Medyan"
en: "median"
definition: "Sıralanmış verinin ortasındaki değer; uç değerlerden etkilenmez."
see_also: [ortalama]
cards: [kb-eco-47-1-descriptive-statistics]
```

## Mevsimsel endeks

```yaml
id: mevsimsel-endeks
term: "Mevsimsel endeks"
en: "seasonal index"
definition: "Bir dönemin (ör. ayın) değerinin yıllık ortalamaya göre tipik oranı."
see_also: [mevsimsellik]
cards: [kb-eco-49-1-time-series-seasonality]
```

## Mevsimsellik

```yaml
id: mevsimsellik
term: "Mevsimsellik"
en: "seasonality"
definition: "Bir zaman serisinde her yıl aynı dönemlerde tekrarlanan dalgalanma."
see_also: [mevsimsel-endeks, zaman-serisi]
cards: [kb-eco-49-1-time-series-seasonality]
```

## Minimum sipariş büyüklüğü

```yaml
id: minimum-siparis-buyuklugu
term: "Minimum sipariş büyüklüğü"
en: "Minimum order quantity / drop size"
definition: "Teslimat ve hizmet maliyetini karşılamak için kabul edilen en küçük sipariş tutarı ya da koli sayısı."
see_also: [hizmet-maliyeti]
cards: [kb-fmcg-1-1-margin-stack, kb-fmcg-11-3-eoq-reorder-point, kb-fmcg-6-3-cost-to-serve]
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

## MoSCoW önceliklendirmesi

```yaml
id: moscow
term: "MoSCoW önceliklendirmesi"
en: "MoSCoW prioritisation"
definition: "İhtiyaçları olmazsa olmaz, olmalı, olabilir ve bu sefer değil olarak ayıran yöntem."
see_also: [kabul-kriteri]
cards: [kb-ea-17-3-writing-requirements]
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

## Muafiyet

```yaml
id: muafiyet
term: "Muafiyet"
en: "deductible"
definition: "Sigortalı bir hasarın, sigortacının ödemeye başlamadan önce sigortalının üstlendiği kısmı."
see_also: [beklenen-kayip]
cards: [kb-eco-4-2-risk-aversion-insurance, kb-eco-52-1-business-insurance]
```

## Mutabakat

```yaml
id: mutabakat
term: "Mutabakat"
en: "Reconciliation"
definition: "İki kaynak arasındaki bakiye veya kayıtların karşılaştırılıp farkların açıklanması."
see_also: [acilis-bakiyesi]
cards: [kb-ea-18-6-data-migration-opening-balances, kb-ea-20-4-record-to-report-close]
```

## Mükemmel mağaza

```yaml
id: mukemmel-magaza
term: "Mükemmel mağaza"
en: "perfect store"
definition: "Bir noktada bulunurluk, raf, fiyat ve teşhir için tanımlanmış hedef standartlar ve bunlara göre hesaplanan puan."
see_also: [raf-payi, sfa, zorunlu-urun-listesi]
cards: [kb-ea-26-1-retail-execution-sfa, kb-fmcg-9-5-perfect-store]
```

## Müşteri ilişkileri yönetimi (CRM)

```yaml
id: crm
term: "Müşteri ilişkileri yönetimi (CRM)"
en: "Customer relationship management"
definition: "Müşterilerle ilişkiyi kârlı ve uzun vadeli yönetmeye yönelik strateji ve bunu destekleyen sistemler."
see_also: [analitik-crm, operasyonel-crm]
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

## Nakit akış tablosu

```yaml
id: nakit-akis-tablosu
term: "Nakit akış tablosu"
en: "cash flow statement"
definition: "Bir dönemdeki nakit giriş ve çıkışlarını işletme, yatırım ve finansman faaliyetleri olarak gösteren tablo."
see_also: [serbest-nakit-akisi]
cards: [kb-eco-33-6-cash-flow-statement]
```

## Nakit akış tahmini

```yaml
id: nakit-akis-tahmini
term: "Nakit akış tahmini"
en: "Cash flow forecast"
definition: "Gelecek dönemlerdeki nakit giriş ve çıkışlarının dönem dönem tahmini."
see_also: [nakit-donusum-suresi, nakit-pozisyonu]
cards: [kb-ea-24-1-treasury-cash-forecasting]
```

## Nakit dönüşüm süresi

```yaml
id: nakit-donusum-suresi
term: "Nakit dönüşüm süresi"
en: "cash conversion cycle (CCC)"
definition: "Tedarikçiye ödeme ile müşteriden tahsilat arasında paranın işletmede bağlı kaldığı gün sayısı: alacak tahsil süresi + stok gün sayısı − borç ödeme süresi."
see_also: [alacak-tahsil-suresi, borc-odeme-suresi, isletme-sermayesi, stok-gun-sayisi]
cards: [kb-eco-36-6-cash-flow-vs-profit, kb-eco-38-1-distributor-financial-statements, kb-eco-38-2-cash-conversion-cycle, kb-fmcg-11-1-supply-chain-basics, kb-fmcg-12-7-case-distributor-turnaround]
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

## Nakit-ve-taşı

```yaml
id: nakit-ve-tasi
term: "Nakit-ve-taşı"
en: "cash and carry"
definition: "Perakendeci ve işletmelerin ürünü kendisinin seçip ödediği ve taşıdığı toptan satış formatı."
see_also: [toptanci]
cards: [kb-fmcg-13-17-turkish-trade-practice, kb-fmcg-6-5-wholesale-cash-carry]
```

## Nash dengesi

```yaml
id: nash-dengesi
term: "Nash dengesi"
en: "Nash equilibrium"
definition: "Diğerlerinin hamlesi verildiğinde hiçbir tarafın kendi hamlesini değiştirmek istemediği durum."
see_also: [mahkumlar-ikilemi]
cards: [kb-eco-7-1-game-theory-for-managers, kb-eco-7-7-oligopoly-collusion]
```

## Net borç

```yaml
id: net-borc
term: "Net borç"
en: "net debt"
definition: "Finansal borçlardan nakit ve nakit benzerlerinin düşülmesiyle bulunan tutar."
see_also: [bilanco]
cards: [kb-eco-33-5-balance-sheet, kb-eco-36-4-ratios-profitability-leverage]
```

## Net bugünkü değer (NBD)

```yaml
id: net-bugunku-deger
term: "Net bugünkü değer (NBD)"
en: "Net present value (NPV)"
definition: "Bir yatırımın gelecekteki nakit akışlarının sermaye maliyetiyle bugüne indirgenmiş toplamından yatırım tutarının çıkarılmasıyla bulunan değer."
see_also: [geri-odeme-suresi, toplam-sahip-olma-maliyeti]
cards: [kb-ea-17-2-total-cost-of-ownership, kb-ea-3-6-it-business-case, kb-eco-25-1-time-value-npv-irr, kb-eco-31-1-capital-budgeting, kb-fmcg-2-4-roi-roce-npv]
```

## Net gerçekleşebilir değer

```yaml
id: net-gerceklesebilir-deger
term: "Net gerçekleşebilir değer"
en: "net realisable value"
definition: "Stoğun tahmini satış fiyatından satış için gereken tahmini maliyetlerin düşülmesiyle bulunan değer."
see_also: [fifo]
cards: [kb-eco-34-1-inventory-valuation]
```

## Net parasal pozisyon

```yaml
id: net-parasal-pozisyon
term: "Net parasal pozisyon"
en: "net monetary position"
definition: "Parasal varlıklar ile parasal borçlar arasındaki fark; enflasyonda satın alma gücü kazancı veya kaybını belirler."
see_also: [parasal-kalem]
cards: [kb-eco-35-2-inflation-accounting]
```

## Net satış

```yaml
id: net-satis
term: "Net satış"
en: "Net sales / net revenue"
definition: "Brüt satıştan iskonto, prim ve diğer ticari indirimler düşüldükten sonra kalan satış geliri."
see_also: [fiyat-selalesi, ticari-harcama]
cards: [kb-eco-33-4-income-statement, kb-fmcg-2-1-fmcg-pnl, kb-fmcg-2-2-gross-to-net, kb-fmcg-2-6-price-volume-mix-variance, kb-fmcg-5-6-pricing-in-high-inflation]
```

## Net ücret

```yaml
id: net-ucret
term: "Net ücret"
en: "Net pay"
definition: "Kesintiler düşüldükten sonra çalışana ödenen tutar."
see_also: [brut-ucret]
cards: [kb-ea-33-2-payroll-basics, kb-eco-43-2-income-tax-withholding, kb-eco-44-3-sgk-employer-costs]
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

## Nokta evreni

```yaml
id: nokta-evreni
term: "Nokta evreni"
en: "outlet universe"
definition: "Bir bölgede kategoriyi satan ya da satabilecek bütün satış noktalarının listesi."
see_also: [sayisal-dagitim, ziyaret-sikligi]
cards: [kb-fmcg-13-8-sales-funnel-math, kb-fmcg-13-9-prospecting-account-segmentation, kb-fmcg-6-2-outlet-universe-segmentation, kb-fmcg-8-13-sales-analytics, kb-fmcg-8-4-sales-force-sizing, kb-fmcg-8-5-territory-routing]
```

## Nominal kur

```yaml
id: nominal-kur
term: "Nominal kur"
en: "nominal exchange rate"
definition: "Bir birim yabancı paranın yerli para karşılığı."
see_also: [reel-kur]
cards: [kb-eco-22-1-exchange-rates-real-nominal]
```

## olası anlaşma alanı

```yaml
id: anlasma-alani
term: "olası anlaşma alanı"
en: "zone of possible agreement (ZOPA)"
definition: "Tarafların kabul edebileceği sınırlar arasında kalan, anlaşmanın mümkün olduğu aralık."
see_also: [batna]
cards: [kb-fmcg-13-14-negotiation-structure]
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

## Oligopol

```yaml
id: oligopol
term: "Oligopol"
en: "oligopoly"
definition: "Az sayıda firmanın pazarın büyük kısmını tuttuğu ve kararlarının birbirini etkilediği yapı."
see_also: [kartel]
cards: [kb-eco-7-7-oligopoly-collusion]
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

## Organizasyon yapısı (ERP)

```yaml
id: organizasyon-yapisi
term: "Organizasyon yapısı (ERP)"
en: "Organizational structure"
definition: "ERP'de şirket, tesis, depo, satış organizasyonu gibi raporlama ve yetkiyi belirleyen birimler."
see_also: [erp]
cards: [kb-ea-20-1-what-erp-does]
```

## ortak iş planı

```yaml
id: ortak-is-plani
term: "ortak iş planı"
en: "joint business plan"
definition: "Üretici ile müşterinin bir dönem için büyüme hedeflerini, girişimleri, yatırımları ve ölçütleri birlikte belirlediği yazılı plan."
see_also: [kilit-musteri-yonetimi, kosullu-prim]
cards: [kb-fmcg-10-7-joint-business-planning, kb-fmcg-11-9-vmi-cpfr, kb-fmcg-13-13-relationship-selling-trust]
```

## Ortalama (aritmetik)

```yaml
id: ortalama
term: "Ortalama (aritmetik)"
en: "mean"
definition: "Değerlerin toplamının değer sayısına bölümü; uç değerlere duyarlıdır."
see_also: [medyan]
cards: [kb-eco-47-1-descriptive-statistics]
```

## Ortalama vergi oranı

```yaml
id: ortalama-vergi-orani
term: "Ortalama vergi oranı"
en: "average tax rate"
definition: "Toplam verginin toplam gelire oranı."
see_also: [marjinal-vergi-orani]
cards: [kb-eco-42-1-tax-basics-average-marginal]
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

## Ödeme eğrisi

```yaml
id: odeme-egrisi
term: "Ödeme eğrisi"
en: "Payout curve"
definition: "Hedef gerçekleşme oranına göre ödenecek primi gösteren kural."
see_also: [prim-plani]
cards: [kb-ea-33-3-incentive-compensation-systems]
```

## Ödeme kaydedici cihaz (ÖKC)

```yaml
id: okc
term: "Ödeme kaydedici cihaz (ÖKC)"
en: "Fiscal cash register"
definition: "Perakende satışlarda mali belge üreten ve kayıtları mali hafızada tutan yeni nesil yazar kasa."
see_also: [kasa-yazilimi, z-raporu]
cards: [kb-ea-28-3-pos-okc]
```

## Ölçek ekonomisi

```yaml
id: olcek-ekonomisi
term: "Ölçek ekonomisi"
en: "Economies of scale"
definition: "Hacim arttıkça sabit maliyetlerin daha çok birime yayılması sonucu birim maliyetin düşmesi."
see_also: [sabit-maliyet]
cards: [kb-eco-5-5-economies-of-scale-sunk-costs, kb-fmcg-1-2-scale-and-concentration]
```

## Ön satış

```yaml
id: on-satis
term: "Ön satış"
en: "pre-selling"
definition: "Temsilcinin siparişi ziyarette alıp teslimatın sonradan ayrı bir araçla yapıldığı saha satış biçimi."
see_also: [aractan-satis]
cards: [kb-ea-26-5-van-sales-presales, kb-fmcg-8-1-selling-formats]
```

## Örneklem

```yaml
id: orneklem
term: "Örneklem"
en: "sample"
definition: "İncelenen kitlenin, hakkında çıkarım yapmak için seçilen alt kümesi."
see_also: [standart-hata]
cards: [kb-eco-47-3-sampling-confidence]
```

## Örneklem hatası

```yaml
id: orneklem-hatasi
term: "Örneklem hatası"
en: "sampling error"
definition: "Bir sonucun tüm kitle yerine bir örnekleme dayanması nedeniyle gerçek değerden sapabileceği aralık."
see_also: []
cards: [kb-fmcg-12-3-analytics-for-decisions, kb-fmcg-3-8-market-research-toolkit]
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

## Özel tüketim vergisi (ÖTV)

```yaml
id: otv
term: "Özel tüketim vergisi (ÖTV)"
en: "special consumption tax"
definition: "4760 sayılı Kanun ekindeki listelerde yer alan mallardan genellikle tek aşamada alınan vergi; KDV matrahına dahildir."
see_also: [damga-vergisi]
cards: [kb-eco-43-1-turkish-tax-system-overview, kb-eco-43-5-otv-stamp-duty]
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

## Özkaynak kârlılığı

```yaml
id: ozkaynak-karliligi
term: "Özkaynak kârlılığı"
en: "return on equity (ROE)"
definition: "Net kârın özkaynağa oranı; ortakların yatırdığı sermayenin getirisi."
see_also: [dupont-analizi]
cards: [kb-eco-36-4-ratios-profitability-leverage, kb-eco-36-5-dupont]
```

## Özkaynak maliyeti

```yaml
id: ozkaynak-maliyeti
term: "Özkaynak maliyeti"
en: "cost of equity"
definition: "Ortakların, şirkete koydukları sermaye için aynı riskteki alternatiflere göre bekledikleri getiri."
see_also: [aosm]
cards: [kb-eco-31-2-cost-of-capital]
```

## p-değeri

```yaml
id: p-degeri
term: "p-değeri"
en: "p-value"
definition: "Gerçekte etki yokken, gözlenen kadar veya daha uç bir sonucun şans eseri ortaya çıkma olasılığı."
see_also: [istatistiksel-anlamlilik]
cards: [kb-eco-47-4-ab-testing-significance]
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

## Paralel eğilim varsayımı

```yaml
id: paralel-egilim
term: "Paralel eğilim varsayımı"
en: "parallel trends assumption"
definition: "Uygulama olmasaydı uygulama ve kontrol gruplarının benzer eğilimi izleyeceği varsayımı."
see_also: [fark-icinde-fark]
cards: [kb-eco-48-7-test-vs-control-did]
```

## Parasal kalem

```yaml
id: parasal-kalem
term: "Parasal kalem"
en: "monetary item"
definition: "Nakit ile sabit veya belirlenebilir tutarda para olarak tahsil edilecek ya da ödenecek varlık ve borçlar."
see_also: [net-parasal-pozisyon]
cards: [kb-eco-35-2-inflation-accounting]
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

## Pazara giriş modeli

```yaml
id: pazara-giris-modeli
term: "Pazara giriş modeli"
en: "route to market"
definition: "Ürünün tüketiciye hangi kanallardan, hangi aracılarla ve hangi hizmet düzeyiyle ulaştığının tasarımı."
see_also: [dogrudan-dagitim, kanal-islevleri]
cards: [kb-fmcg-6-1-rtm-channels-formats, kb-fmcg-6-8-rtm-design-case, kb-fmcg-8-1-selling-formats]
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

## PCI DSS

```yaml
id: pci-dss
term: "PCI DSS"
en: "Payment Card Industry Data Security Standard"
definition: "Kart verisini işleyen sistemler için PCI Güvenlik Standartları Konseyi'nin güvenlik standardı."
see_also: [sanal-pos]
cards: [kb-ea-28-4-card-virtual-pos]
```

## Penetrasyon

```yaml
id: penetrasyon
term: "Penetrasyon"
en: "Penetration"
definition: "Belirli bir dönemde bir markayı veya kategoriyi en az bir kez satın alan hanelerin oranı."
see_also: [alim-sikligi, cifte-risk]
cards: [kb-fmcg-12-6-case-brand-growth-plan, kb-fmcg-3-2-repeat-buying-patterns, kb-fmcg-3-4-mental-physical-availability, kb-fmcg-3-8-market-research-toolkit, kb-fmcg-4-7-launch-forecasting]
```

## Perakende medya

```yaml
id: perakende-medya
term: "Perakende medya"
en: "retail media"
definition: "Perakendecinin kendi web sitesi, uygulaması ve mağazalarındaki reklam alanlarını, müşteri verisini kullanarak markalara satması."
see_also: [artimsal-hacim]
cards: [kb-fmcg-9-7-retail-media]
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

## Pişmanlık

```yaml
id: pismanlik
term: "Pişmanlık"
en: "voluntary disclosure"
definition: "Vergi hatasının idare tespit etmeden kendiliğinden bildirilmesi; kanundaki şartlar sağlanırsa vergi ziyaı cezası kesilmez."
see_also: [vergi-ziyai-cezasi]
cards: [kb-eco-43-6-tax-procedure-inspection]
```

## Piyasa dengesi

```yaml
id: piyasa-dengesi
term: "Piyasa dengesi"
en: "market equilibrium"
definition: "Talep edilen ve arz edilen miktarın eşitlendiği fiyat ve miktar."
see_also: [talep-esnekligi]
cards: [kb-eco-1-3-supply-demand, kb-eco-1-5-price-controls-tax-incidence]
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

## Planogram

```yaml
id: planogram
term: "Planogram"
en: "planogram"
definition: "Ürünlerin rafta hangi yerde ve kaç yüzle duracağını gösteren yerleşim planı."
see_also: [raf-payi]
cards: [kb-fmcg-10-6-category-management, kb-fmcg-9-3-shelf-space-planogram, kb-fmcg-9-5-perfect-store]
```

## Politika faizi

```yaml
id: politika-faizi
term: "Politika faizi"
en: "policy rate"
definition: "Merkez bankasının para politikasını yürütürken temel aldığı kısa vadeli faiz oranı."
see_also: [reel-faiz]
cards: [kb-eco-21-1-monetary-policy-tcmb, kb-eco-50-4-tcmb-policy-rate-credit]
```

## Portföy

```yaml
id: portfoy
term: "Portföy"
en: "portfolio"
definition: "Firmanın sattığı ürün, marka ve ambalaj seçeneklerinin bütünü."
see_also: [sku-sadelestirme]
cards: [kb-fmcg-4-4-portfolio-management]
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

## Prim teşviki

```yaml
id: prim-tesviki
term: "Prim teşviki"
en: "social security contribution incentive"
definition: "Belirli şartları sağlayan işverenlerin sosyal güvenlik primlerinde sağlanan indirim veya destek."
see_also: [isveren-maliyeti]
cards: [kb-eco-44-3-sgk-employer-costs]
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

## Puantaj

```yaml
id: puantaj
term: "Puantaj"
en: "Time and attendance"
definition: "Çalışanların devam, izin ve fazla mesai kayıtları."
see_also: [personel-ana-verisi]
cards: [kb-ea-33-1-hr-systems]
```

## Raf bulunurluğu

```yaml
id: raf-bulunurlugu
term: "Raf bulunurluğu"
en: "On-shelf availability (OSA)"
definition: "Ürünün tüketicinin aradığı anda rafta satılabilir hâlde bulunma oranı."
see_also: [siparis-karsilama-orani]
cards: [kb-fmcg-11-4-safety-stock, kb-fmcg-11-8-cold-chain, kb-fmcg-12-4-sustainability-regulation, kb-fmcg-13-2-spin-solution-selling, kb-fmcg-3-1-consumer-decisions, kb-fmcg-3-7-shopper-path-to-purchase, kb-fmcg-9-3-shelf-space-planogram, kb-fmcg-9-4-osa-out-of-stock, kb-fmcg-9-5-perfect-store]
```

## Raf payı

```yaml
id: raf-payi
term: "Raf payı"
en: "share of shelf"
definition: "Bir markanın ya da üreticinin kategori rafındaki yüz veya uzunluk payı."
see_also: [planogram]
cards: [kb-fmcg-10-6-category-management, kb-fmcg-13-5-retail-buyer-decisions, kb-fmcg-9-3-shelf-space-planogram, kb-fmcg-9-5-perfect-store]
```

## Reel büyüme

```yaml
id: reel-buyume
term: "Reel büyüme"
en: "real growth"
definition: "Fiyat artışının etkisinden arındırılmış büyüme; (1 + nominal) / (1 + enflasyon) − 1 ile hesaplanır."
see_also: [cagr]
cards: [kb-eco-14-1-gdp-real-nominal, kb-eco-2-5-growth-rates-and-logs, kb-eco-33-7-reading-annual-report, kb-eco-49-1-time-series-seasonality]
```

## Reel faiz

```yaml
id: reel-faiz
term: "Reel faiz"
en: "real interest rate"
definition: "Nominal faizin enflasyondan arındırılmış hâli; (1 + nominal faiz) / (1 + enflasyon) − 1."
see_also: [fisher-denklemi]
cards: [kb-eco-18-3-real-vs-nominal-interest-fisher, kb-eco-21-1-monetary-policy-tcmb, kb-eco-25-2-loans-real-vs-nominal, kb-eco-32-4-finance-in-high-inflation]
```

## Reel kur

```yaml
id: reel-kur
term: "Reel kur"
en: "real exchange rate"
definition: "Nominal kurun iki ülkenin fiyat düzeyleriyle düzeltilmiş hâli; göreli fiyat rekabetini gösterir."
see_also: [nominal-kur]
cards: [kb-eco-22-1-exchange-rates-real-nominal]
```

## Regresyon

```yaml
id: regresyon
term: "Regresyon"
en: "regression"
definition: "Bir değişkenin bir veya daha fazla değişkenle ilişkisini denklemle tahmin eden istatistiksel yöntem."
see_also: [belirlilik-katsayisi, korelasyon]
cards: [kb-eco-47-5-correlation-regression-basics]
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

## Risk raporu

```yaml
id: risk-raporu
term: "Risk raporu"
en: "credit report"
definition: "Bir kişi veya firmanın kredi ve ödeme geçmişini özetleyen rapor."
see_also: [kredi-burosu]
cards: [kb-ea-38-3-findeks-credit-bureau]
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

## Rol tabanlı erişim denetimi (RBAC)

```yaml
id: rbac
term: "Rol tabanlı erişim denetimi (RBAC)"
en: "Role-based access control"
definition: "Yetkilerin kişilere değil rollere verildiği, kişilere rol atandığı erişim yönetimi."
see_also: [en-az-yetki, gorevler-ayriligi]
cards: [kb-ea-15-2-user-roles-permissions]
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

## Rut planı

```yaml
id: rut-plani
term: "Rut planı"
en: "Route plan"
definition: "Satış temsilcisinin hangi noktayı hangi gün ve sıklıkta ziyaret edeceğini gösteren plan."
see_also: [sfa]
cards: [kb-ea-26-1-retail-execution-sfa]
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

## Sabit maliyet

```yaml
id: sabit-maliyet
term: "Sabit maliyet"
en: "Fixed cost"
definition: "Belirli bir dönemde ve kapasite aralığında satış hacminden bağımsız olarak oluşan maliyet; kira, maaş, amortisman gibi."
see_also: [degisken-maliyet, olcek-ekonomisi]
cards: [kb-eco-5-5-economies-of-scale-sunk-costs, kb-fmcg-1-2-scale-and-concentration, kb-fmcg-2-1-fmcg-pnl, kb-fmcg-2-3-contribution-breakeven, kb-fmcg-6-4-direct-vs-indirect]
```

## Saha satış otomasyonu

```yaml
id: sfa
term: "Saha satış otomasyonu"
en: "sales force automation (SFA)"
definition: "Saha temsilcisinin ziyaret, sipariş ve tahsilat işlerini mobil cihazdan yürüttüğü uygulama."
see_also: [erp]
cards: [kb-ea-1-1-what-is-an-enterprise-system, kb-ea-2-2-user-adoption, kb-ea-20-2-order-to-cash, kb-ea-26-1-retail-execution-sfa, kb-fmcg-12-1-leading-sales-orgs, kb-fmcg-12-2-change-digital-transformation, kb-fmcg-8-10-sfa-data-driven-selling, kb-fmcg-8-13-sales-analytics]
```

## Sahte veya muhteviyatı itibarıyla yanıltıcı belge

```yaml
id: sahte-belge
term: "Sahte veya muhteviyatı itibarıyla yanıltıcı belge"
en: "fictitious invoice"
definition: "Gerçek bir işleme dayanmayan veya işlemi gerçeğe aykırı gösteren belge; Vergi Usul Kanunu'nda ağır yaptırımlara bağlanmıştır."
see_also: [vergi-uyumu]
cards: [kb-eco-42-8-informality-tax-compliance]
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

## Sanal POS

```yaml
id: sanal-pos
term: "Sanal POS"
en: "Virtual POS"
definition: "İnternet veya uzaktan kartla ödeme almayı sağlayan banka ya da ödeme kuruluşu altyapısı."
see_also: [pci-dss, valor]
cards: [kb-ea-28-4-card-virtual-pos]
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

## satın alma merkezi

```yaml
id: satin-alma-merkezi
term: "satın alma merkezi"
en: "buying centre"
definition: "Bir kurumsal satın alma kararını etkileyen ya da veren kişilerin tamamı; kullanıcı, etkileyici, karar verici, onaylayıcı ve kapı bekçisi gibi rolleri kapsar."
see_also: [cozum-satisi]
cards: [kb-fmcg-13-2-strategic-selling, kb-fmcg-13-3-challenger-meddic-sandler, kb-fmcg-13-4-b2b-buying-behaviour]
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

## Satın alma talebi

```yaml
id: satin-alma-talebi
term: "Satın alma talebi"
en: "Purchase requisition"
definition: "Bir birimin ihtiyacını satın almaya ilettiği iç belge."
see_also: [tedarikci-performansi]
cards: [kb-ea-34-1-purchasing-supplier-management]
```

## satış hunisi

```yaml
id: satis-hunisi
term: "satış hunisi"
en: "sales funnel"
definition: "Potansiyel müşterilerin ilk temastan siparişe kadar geçtiği aşamalar ve her aşamadaki dönüşüm oranları."
see_also: [donusum-orani]
cards: [kb-fmcg-13-16-sales-forecasting, kb-fmcg-13-8-sales-funnel-math]
```

## satış ve operasyon planlaması

```yaml
id: satis-ve-operasyon-planlamasi
term: "satış ve operasyon planlaması"
en: "sales and operations planning"
definition: "Talep, arz ve finans planlarını düzenli bir aylık döngüde tek bir mutabık plana bağlayan yönetim süreci; kapsamı genişletilmiş hâline bütünleşik iş planlaması denir."
see_also: [kamci-etkisi, tahmin-hatasi]
cards: [kb-fmcg-11-2-demand-forecasting, kb-fmcg-11-6-sop-ibp, kb-fmcg-13-16-sales-forecasting]
```

## Sayısal dağıtım

```yaml
id: sayisal-dagitim
term: "Sayısal dağıtım"
en: "numeric distribution"
definition: "Ürünü bulunduran satış noktalarının, kategoriyi satan tüm noktalara oranı."
see_also: [agirlikli-dagitim]
cards: [kb-fmcg-12-6-case-brand-growth-plan, kb-fmcg-13-9-prospecting-account-segmentation, kb-fmcg-3-4-mental-physical-availability, kb-fmcg-6-2-outlet-universe-segmentation, kb-fmcg-7-5-distributor-development, kb-fmcg-8-10-sfa-data-driven-selling, kb-fmcg-8-13-sales-analytics, kb-fmcg-8-7-sales-kpi-design]
```

## Segmentasyon

```yaml
id: segmentasyon
term: "Segmentasyon"
en: "segmentation"
definition: "Pazarı ihtiyaçları ve tepkileri birbirine benzeyen alıcı gruplarına ayırma."
see_also: [konumlandirma]
cards: [kb-fmcg-13-9-prospecting-account-segmentation, kb-fmcg-4-2-segmentation-positioning]
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

## Senaryo analizi

```yaml
id: senaryo-analizi
term: "Senaryo analizi"
en: "scenario analysis"
definition: "Birlikte gerçekleşmesi beklenen varsayım değişikliklerinin tutarlı setler hâlinde sonuca etkisinin incelenmesi."
see_also: [duyarlilik-analizi]
cards: [kb-eco-31-10-scenario-sensitivity]
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

## Sepet büyüklüğü

```yaml
id: sepet-buyuklugu
term: "Sepet büyüklüğü"
en: "basket size"
definition: "Bir alışverişte ya da siparişte satın alınan ürünlerin toplam tutarı ya da adedi."
see_also: []
cards: [kb-fmcg-13-11-objections-closing-upsell, kb-fmcg-6-7-e-grocery-quick-commerce, kb-fmcg-8-2-structured-sales-call, kb-fmcg-8-3-salesperson-performance-drivers, kb-fmcg-8-9-coaching]
```

## Serbest nakit akışı

```yaml
id: serbest-nakit-akisi
term: "Serbest nakit akışı"
en: "free cash flow"
definition: "Faaliyetlerden elde edilen nakitten yatırım harcamaları düşüldükten sonra kalan nakit."
see_also: [isletme-sermayesi]
cards: [kb-eco-26-4-business-valuation-basics, kb-eco-31-9-three-statement-model, kb-eco-33-6-cash-flow-statement, kb-eco-36-6-cash-flow-vs-profit]
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

## Sınırda Karbon Düzenleme Mekanizması (SKDM)

```yaml
id: skdm
term: "Sınırda Karbon Düzenleme Mekanizması (SKDM)"
en: "Carbon Border Adjustment Mechanism (CBAM)"
definition: "AB'nin, kapsamdaki ürünlerin ithalatında gömülü emisyon için sertifika alınmasını öngören düzenlemesi."
see_also: [karbon-fiyatlamasi]
cards: [kb-eco-40-4-environmental-taxes-cbam]
```

## Sigorta bedeli

```yaml
id: sigorta-bedeli
term: "Sigorta bedeli"
en: "sum insured"
definition: "Poliçede belirtilen ve sigortacının sorumluluğunun üst sınırını oluşturan tutar."
see_also: [eksik-sigorta]
cards: [kb-eco-52-1-business-insurance]
```

## Sinerji

```yaml
id: sinerji
term: "Sinerji"
en: "synergy"
definition: "İki işletmenin birleşmesiyle, ayrı ayrı elde edebileceklerinin toplamını aşan ek değer."
see_also: [durum-tespiti]
cards: [kb-eco-31-8-mergers-acquisitions]
```

## Sinyal

```yaml
id: sinyal
term: "Sinyal"
en: "signalling"
definition: "Bilgili tarafın kendi kalitesini, taklidi pahalı bir adımla karşı tarafa göstermesi."
see_also: [ters-secim]
cards: [kb-eco-12-1-adverse-selection-credit]
```

## Sipariş karşılama oranı

```yaml
id: siparis-karsilama-orani
term: "Sipariş karşılama oranı"
en: "fill rate"
definition: "Sevk edilen miktarın sipariş edilen miktara oranı."
see_also: [siparisten-tahsilata]
cards: [kb-ea-20-2-order-to-cash, kb-fmcg-11-1-supply-chain-basics, kb-fmcg-11-4-safety-stock, kb-fmcg-7-4-distributor-selection-kpis, kb-fmcg-9-4-osa-out-of-stock]
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

## Siparişten tahsilata

```yaml
id: siparisten-tahsilata
term: "Siparişten tahsilata"
en: "order-to-cash (O2C)"
definition: "Müşteri siparişinden sevkiyat, faturalama ve tahsilata kadar uzanan uçtan uca satış süreci."
see_also: [erp]
cards: [kb-ea-20-2-order-to-cash, kb-ea-4-1-what-is-a-process, kb-ea-4-7-process-mining, kb-fmcg-12-2-change-digital-transformation]
```

## SKU sadeleştirme

```yaml
id: sku-sadelestirme
term: "SKU sadeleştirme"
en: "SKU rationalisation"
definition: "Düşük katkılı ürünleri portföyden çıkararak karmaşıklık maliyetini azaltma."
see_also: [portfoy, talep-transferi]
cards: [kb-fmcg-12-7-case-distributor-turnaround, kb-fmcg-4-6-sku-rationalisation]
```

## soğuk zincir

```yaml
id: soguk-zincir
term: "soğuk zincir"
en: "cold chain"
definition: "Sıcaklığa duyarlı ürünlerin üretimden tüketiciye kadar belirlenmiş sıcaklık aralığında tutulmasını sağlayan depolama, taşıma ve izleme sistemi."
see_also: [dagitim-merkezi]
cards: [kb-fmcg-11-8-cold-chain]
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

## SSCC

```yaml
id: sscc
term: "SSCC"
en: "Serial Shipping Container Code"
definition: "Palet gibi lojistik birimlerin GS1 standardındaki tekil numarası."
see_also: [gtin]
cards: [kb-ea-30-4-barcodes-traceability]
```

## Standart hata

```yaml
id: standart-hata
term: "Standart hata"
en: "standard error"
definition: "Bir örneklem tahmininin, tekrarlanan örneklemlerde ne kadar değişeceğinin ölçüsü."
see_also: [guven-araligi]
cards: [kb-eco-47-3-sampling-confidence]
```

## Standart maliyet

```yaml
id: standart-maliyet
term: "Standart maliyet"
en: "Standard cost"
definition: "Dönem başında belirlenen sabit birim maliyet; gerçek maliyetle fark ayrı hesapta izlenir."
see_also: [hareketli-ortalama-maliyet]
cards: [kb-ea-20-5-inventory-in-erp, kb-eco-39-4-budgeting-standard-costs]
```

## Standart sapma

```yaml
id: standart-sapma
term: "Standart sapma"
en: "standard deviation"
definition: "Değerlerin ortalamadan tipik uzaklığının ölçüsü."
see_also: [ortalama]
cards: [kb-eco-47-1-descriptive-statistics]
```

## Stok gün sayısı

```yaml
id: stok-gun-sayisi
term: "Stok gün sayısı"
en: "days inventory outstanding (DIO)"
definition: "Stokların ortalama kaç günlük satış maliyetine yettiği."
see_also: [nakit-donusum-suresi]
cards: [kb-eco-38-2-cash-conversion-cycle, kb-fmcg-11-1-supply-chain-basics, kb-fmcg-11-3-eoq-reorder-point, kb-fmcg-11-7-warehouse-transport-network, kb-fmcg-11-9-vmi-cpfr, kb-fmcg-7-4-distributor-selection-kpis, kb-fmcg-9-1-retailer-economics]
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

## Stok yatırımının brüt kâr getirisi (GMROI)

```yaml
id: gmroi
term: "Stok yatırımının brüt kâr getirisi (GMROI)"
en: "gross margin return on inventory investment"
definition: "Bir ürün ya da kategorinin brüt kârının, maliyet üzerinden ortalama stok değerine oranı."
see_also: [roce]
cards: [kb-fmcg-9-1-retailer-economics]
```

## Stoksuzluk

```yaml
id: stoksuzluk
term: "Stoksuzluk"
en: "out-of-stock (OOS)"
definition: "Tüketicinin almak istediği ürünü rafta bulamaması durumu."
see_also: [raf-bulunurlugu]
cards: [kb-fmcg-11-9-vmi-cpfr, kb-fmcg-13-2-spin-solution-selling, kb-fmcg-9-4-osa-out-of-stock]
```

## Stopaj (vergi tevkifatı)

```yaml
id: stopaj
term: "Stopaj (vergi tevkifatı)"
en: "withholding tax"
definition: "Ödemeyi yapanın, karşı tarafın vergisini ödeme sırasında kesip beyan ettiği ve ödediği vergi."
see_also: [brut-ucret]
cards: [kb-eco-43-1-turkish-tax-system-overview, kb-eco-43-2-income-tax-withholding]
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

## Stres testi

```yaml
id: stres-testi
term: "Stres testi"
en: "stress test"
definition: "Olası en kötü ama gerçekçi koşulların birlikte gerçekleştiği varsayımıyla şirketin dayanıklılığının ölçülmesi."
see_also: [senaryo-analizi]
cards: [kb-eco-32-3-risk-management-stress-test]
```

## Sürdürülebilirlik raporlaması

```yaml
id: surdurulebilirlik-raporlamasi
term: "Sürdürülebilirlik raporlaması"
en: "sustainability reporting"
definition: "Şirketin iklim ve diğer sürdürülebilirlik konularındaki risk, fırsat ve performansını açıklayan raporlama."
see_also: [tsrs]
cards: [kb-eco-54-3-governance-sustainability-reporting]
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

## Sürücü bazlı planlama

```yaml
id: surucu-bazli-planlama
term: "Sürücü bazlı planlama"
en: "Driver-based planning"
definition: "Sonuçların hacim, fiyat, verimlilik gibi birkaç temel sürücüden hesaplandığı planlama yöntemi."
see_also: [kayan-tahmin]
cards: [kb-ea-23-2-rolling-forecast-driver-based]
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

## Şüpheli alacak

```yaml
id: supheli-alacak
term: "Şüpheli alacak"
en: "doubtful receivable"
definition: "Tahsil edilememe riski yüksek olan ve karşılık ayrılan ticari alacak; vergi açısından kabulü belirli koşullara bağlıdır."
see_also: [beklenen-kredi-zarari]
cards: [kb-eco-34-2-receivables-doubtful-debts]
```

## Tahakkuk esası

```yaml
id: tahakkuk-esasi
term: "Tahakkuk esası"
en: "accrual basis"
definition: "Gelir ve giderlerin nakit hareketinin tarihine değil, ait oldukları döneme kaydedilmesi ilkesi."
see_also: [gider-tahakkuku]
cards: [kb-eco-33-3-accruals-period-close]
```

## Tahakkuk oranı

```yaml
id: tahakkuk-orani
term: "Tahakkuk oranı"
en: "accruals ratio"
definition: "Net kâr ile işletme nakit akışı arasındaki farkın ortalama toplam varlıklara oranı."
see_also: [kar-kalitesi]
cards: [kb-eco-36-7-earnings-quality-red-flags]
```

## tahmin hatası

```yaml
id: tahmin-hatasi
term: "tahmin hatası"
en: "forecast error"
definition: "Gerçekleşen talep ile tahmin arasındaki fark; genellikle ortalama mutlak yüzde hata ve sapma (bias) ile ölçülür."
see_also: [guvenlik-stoku, satis-ve-operasyon-planlamasi, mape]
cards: [kb-fmcg-11-2-demand-forecasting, kb-fmcg-11-4-safety-stock, kb-fmcg-11-5-bullwhip-effect, kb-fmcg-11-6-sop-ibp, kb-fmcg-13-16-sales-forecasting]
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

## Talep esnekliği (fiyat)

```yaml
id: talep-esnekligi
term: "Talep esnekliği (fiyat)"
en: "price elasticity of demand"
definition: "Fiyattaki yüzde değişime karşılık talep edilen miktardaki yüzde değişim."
see_also: [piyasa-dengesi]
cards: [kb-eco-1-3-supply-demand, kb-eco-1-5-price-controls-tax-incidence]
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

## Talep planlama

```yaml
id: talep-planlama
term: "Talep planlama"
en: "Demand planning"
definition: "İstatistiksel tahmin ile pazar bilgisini birleştirerek uzlaşılmış talep rakamı üreten süreç."
see_also: [mape, tahmin-katma-degeri]
cards: [kb-ea-29-2-demand-planning-systems]
```

## Talep transferi

```yaml
id: talep-transferi
term: "Talep transferi"
en: "demand transfer"
definition: "Bir ürün çıkarıldığında ya da bulunamadığında alıcıların aynı firmanın başka ürününe geçen oranı."
see_also: [sku-sadelestirme]
cards: [kb-fmcg-10-6-category-management, kb-fmcg-13-5-retail-buyer-decisions, kb-fmcg-4-6-sku-rationalisation]
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

## Tedarik süresi

```yaml
id: tedarik-suresi
term: "Tedarik süresi"
en: "Lead time"
definition: "Siparişin verilmesinden malzemenin kullanıma hazır olmasına kadar geçen süre."
see_also: [drp, mrp]
cards: [kb-ea-20-6-mrp-basics, kb-ea-29-3-drp-inventory-planning]
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

## tedarikçi yönetimli stok

```yaml
id: tedarikci-yonetimli-stok
term: "tedarikçi yönetimli stok"
en: "vendor-managed inventory"
definition: "Müşterinin stok seviyesini ve yenileme siparişlerini, paylaşılan satış ve stok verisine dayanarak tedarikçinin yönettiği model."
see_also: [isbirlikci-planlama, kamci-etkisi]
cards: [kb-fmcg-11-9-vmi-cpfr]
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

## Teklife çağrı dokümanı (RFP)

```yaml
id: rfp
term: "Teklife çağrı dokümanı (RFP)"
en: "Request for proposal"
definition: "Tedarikçilerden ihtiyaçlara göre yapılandırılmış çözüm ve fiyat teklifi istemek için hazırlanan doküman."
see_also: [kritik-basari-faktoru]
cards: [kb-ea-17-4-vendor-selection-rfp]
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

## Tekrarlanabilirlik (idempotency)

```yaml
id: idempotency
term: "Tekrarlanabilirlik (idempotency)"
en: "idempotency"
definition: "Aynı isteğin birden çok kez gönderilmesinin tek seferlik etkiyle sonuçlanması."
see_also: [ozel-entegrator]
cards: [kb-ea-37-3-e-document-integration-routes]
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

## Temerrüt olasılığı

```yaml
id: temerrut-olasiligi
term: "Temerrüt olasılığı"
en: "probability of default"
definition: "Bir borçlunun belirli bir süre içinde borcunu ödeyememe olasılığı."
see_also: [beklenen-kredi-zarari]
cards: [kb-eco-37-3-customer-credit-analysis, kb-eco-55-1-case-distributor-credit-decision]
```

## Teminat mektubu

```yaml
id: teminat-mektubu
term: "Teminat mektubu"
en: "letter of guarantee"
definition: "Bankanın, müşterisinin yükümlülüğünü yerine getirmemesi hâlinde belirli bir tutarı lehdara ödemeyi taahhüt ettiği belge."
see_also: [dbs]
cards: [kb-eco-38-3-distributor-credit-risk-dbs, kb-eco-50-3-working-with-banks]
```

## Ters seçim

```yaml
id: ters-secim
term: "Ters seçim"
en: "adverse selection"
definition: "Bilgi farkı nedeniyle sunulan koşulların orantısız biçimde riskli tarafları çekmesi."
see_also: [bilgi-asimetrisi, sinyal]
cards: [kb-eco-12-1-adverse-selection-credit]
```

## TFRS

```yaml
id: tfrs
term: "TFRS"
en: "Turkish Financial Reporting Standards"
definition: "Uluslararası Finansal Raporlama Standartlarıyla uyumlu olarak KGK tarafından yayımlanan standartlar seti."
see_also: [bobi-frs]
cards: [kb-eco-35-1-reporting-regimes-tr]
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

## Ticari fatura senaryosu

```yaml
id: ticari-fatura
term: "Ticari fatura senaryosu"
en: "commercial invoice profile"
definition: "Alıcının e-faturaya sistem üzerinden kabul veya red yanıtı verebildiği senaryo."
see_also: [ubl-tr]
cards: [kb-ea-37-2-e-fatura-scenarios]
```

## Ticari harcama

```yaml
id: ticari-harcama
term: "Ticari harcama"
en: "trade spend"
definition: "Üreticinin perakendeci veya bayiye verdiği fatura altı iskonto, ciro primi, promosyon desteği ve listeleme bedeli gibi tüm ticari ödemeler."
see_also: [ciro-primi, fiyat-selalesi, net-satis]
cards: [kb-fmcg-10-2-trade-terms, kb-fmcg-12-5-ethics-compliance-trade, kb-fmcg-13-14-negotiation-structure, kb-fmcg-13-7-behavioural-economics-selling, kb-fmcg-2-1-fmcg-pnl, kb-fmcg-2-2-gross-to-net, kb-fmcg-5-5-trade-spend-roi, kb-fmcg-5-7-rgm-system, kb-fmcg-9-6-trade-marketing, kb-fmcg-9-7-retail-media]
```

## Ticari promosyon yönetimi (TPM)

```yaml
id: tpm
term: "Ticari promosyon yönetimi (TPM)"
en: "Trade promotion management"
definition: "Promosyonların planlama, bütçe, tahakkuk, mahsuplaşma ve değerlendirmesini yöneten sistem ve süreç."
see_also: [mahsuplasma, promosyon-tahakkuku]
cards: [kb-ea-27-2-tpm-promotion-settlement]
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

## Toplam sahip olma maliyeti

```yaml
id: toplam-sahip-olma-maliyeti
term: "Toplam sahip olma maliyeti"
en: "total cost of ownership (TCO)"
definition: "Bir sistemin satın alma, kurulum, işletme ve çıkış maliyetlerinin ömrü boyunca toplamı."
see_also: [net-bugunku-deger]
cards: [kb-ea-17-1-build-buy-configure, kb-ea-17-2-total-cost-of-ownership, kb-ea-3-6-it-business-case]
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

## Toplu toplama

```yaml
id: toplu-toplama
term: "Toplu toplama"
en: "Batch picking"
definition: "Birden fazla siparişin birlikte toplanıp sonra ayrıştırılması."
see_also: [slotting]
cards: [kb-ea-30-2-slotting-picking]
```

## Toptancı

```yaml
id: toptanci
term: "Toptancı"
en: "Wholesaler"
definition: "Ürünü toplu alıp çoğunlukla küçük perakendecilere ve işletmelere satan, genellikle kendi deposundan ya da al-götür modeliyle çalışan aracı."
see_also: [bayi]
cards: [kb-fmcg-1-3-channel-actors, kb-fmcg-6-5-wholesale-cash-carry]
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

## trade marketing

```yaml
id: trade-marketing
term: "trade marketing"
en: "trade marketing"
definition: "Marka stratejisini kanal ve mağaza düzeyinde teşhir, promosyon, malzeme ve aktivasyon programlarına dönüştüren ve bu yatırımların getirisini izleyen işlev."
see_also: [mukemmel-magaza, ticari-harcama]
cards: [kb-fmcg-9-6-trade-marketing]
```

## TSRS

```yaml
id: tsrs
term: "TSRS"
en: "Turkish Sustainability Reporting Standards"
definition: "ISSB standartlarıyla uyumlu olarak Kamu Gözetimi Kurumu tarafından yayımlanan sürdürülebilirlik raporlama standartları."
see_also: [surdurulebilirlik-raporlamasi]
cards: [kb-eco-54-3-governance-sustainability-reporting]
```

## TÜFE

```yaml
id: tufe
term: "TÜFE"
en: "consumer price index"
definition: "Hanehalkının satın aldığı mal ve hizmet sepetinin fiyat değişimini ölçen endeks."
see_also: [ufe]
cards: [kb-eco-14-2-inflation-measurement-tufe-ufe]
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

## Uç değer

```yaml
id: uc-deger
term: "Uç değer"
en: "outlier"
definition: "Veri setindeki diğer değerlerden belirgin biçimde farklı gözlem."
see_also: [medyan]
cards: [kb-eco-47-1-descriptive-statistics]
```

## uyarlamalı satış

```yaml
id: uyarlamali-satis
term: "uyarlamalı satış"
en: "adaptive selling"
definition: "Satış temsilcisinin yaklaşımını, görüşme sırasında edindiği bilgiye ve karşısındaki kişinin özelliklerine göre değiştirmesi."
see_also: [cozum-satisi]
cards: [kb-fmcg-13-12-adaptive-selling]
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

## Uygulama portföyü

```yaml
id: uygulama-portfoyu
term: "Uygulama portföyü"
en: "application portfolio"
definition: "Firmanın kullandığı tüm uygulamaların iş yetenekleriyle eşlenmiş ve değerlendirilmiş listesi."
see_also: [erp]
cards: [kb-ea-5-4-application-portfolio]
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

## Uyum–boşluk analizi

```yaml
id: uyum-bosluk-analizi
term: "Uyum–boşluk analizi"
en: "Fit-gap analysis"
definition: "Süreç adımlarının bir yazılım paketince standart olarak karşılanıp karşılanmadığının tek tek işaretlenmesi."
see_also: [ozellestirme-borcu]
cards: [kb-ea-17-1-build-buy-configure, kb-ea-18-5-implementation-methodology]
```

## uyum programı

```yaml
id: uyum-programi
term: "uyum programı"
en: "compliance programme"
definition: "Bir işletmenin rekabet, ticaret ve etik kurallarına uyumu sağlamak için oluşturduğu politika, eğitim, onay ve denetim mekanizmaları bütünü."
see_also: [haksiz-ticari-uygulama]
cards: [kb-fmcg-12-5-ethics-compliance-trade]
```

## Üçlü eşleştirme

```yaml
id: uclu-eslestirme
term: "Üçlü eşleştirme"
en: "Three-way match"
definition: "Satın alma siparişi, mal kabul ve faturanın miktar ve fiyatta karşılaştırılması."
see_also: [gorevler-ayriligi, satinalma-siparisi]
cards: [kb-ea-20-3-procure-to-pay]
```

## ÜFE

```yaml
id: ufe
term: "ÜFE"
en: "producer price index"
definition: "Üreticilerin yurt içinde sattığı ürünlerin fiyat değişimini ölçen endeks."
see_also: [tufe]
cards: [kb-eco-14-2-inflation-measurement-tufe-ufe]
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

## Üretken yapay zekâ

```yaml
id: uretken-yapay-zeka
term: "Üretken yapay zekâ"
en: "generative AI"
definition: "Metin, görüntü veya kod gibi yeni içerik üretebilen yapay zekâ modelleri."
see_also: [rag]
cards: [kb-ea-39-3-genai-at-work]
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

## Üst veri

```yaml
id: ust-veri
term: "Üst veri"
en: "Metadata"
definition: "Bir belgeyi tanımlayan tür, tarih, karşı taraf gibi bilgiler."
see_also: [saklama-suresi]
cards: [kb-ea-35-1-document-archive-retention]
```

## Vade

```yaml
id: vade
term: "Vade"
en: "Payment term"
definition: "Satış veya teslim ile ödeme arasında taraflarca kabul edilen süre."
see_also: [alacak-tahsil-suresi]
cards: [kb-eco-32-4-finance-in-high-inflation, kb-fmcg-1-5-turkish-fmcg-landscape, kb-fmcg-10-1-key-account-management, kb-fmcg-10-2-trade-terms, kb-fmcg-10-4-negotiating-with-chains, kb-fmcg-13-17-turkish-trade-practice, kb-fmcg-13-4-b2b-buying-behaviour, kb-fmcg-7-2-distributor-roi, kb-fmcg-7-3-credit-collections-dso]
```

## Vadeli kur

```yaml
id: vadeli-kur
term: "Vadeli kur"
en: "forward exchange rate"
definition: "Gelecekteki bir tarihte döviz alım veya satımı için bugünden belirlenen kur; spot kur ve faiz farkından türetilir."
see_also: [kur-riski]
cards: [kb-eco-30-1-forwards-fx-hedging, kb-eco-34-8-fx-transactions]
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

## Varlık devir hızı

```yaml
id: varlik-devir-hizi
term: "Varlık devir hızı"
en: "asset turnover"
definition: "Net satışların toplam varlıklara oranı; her 1 TL varlıkla yapılan satış."
see_also: [dupont-analizi]
cards: [kb-eco-36-5-dupont]
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

## Vekâlet maliyeti

```yaml
id: vekalet-maliyeti
term: "Vekâlet maliyeti"
en: "agency cost"
definition: "Karar veren ile adına karar verilen tarafın çıkarlarının ayrışmasından doğan izleme, güvence ve verim kaybı maliyetleri."
see_also: [asil-vekil-sorunu]
cards: [kb-eco-31-5-agency-governance-family-firm]
```

## Vergi incelemesi

```yaml
id: vergi-incelemesi
term: "Vergi incelemesi"
en: "tax audit"
definition: "Yetkili inceleme elemanlarının defter, belge ve kayıtları inceleyerek ödenmesi gereken verginin doğruluğunu araştırması."
see_also: [vergi-ziyai-cezasi]
cards: [kb-eco-43-6-tax-procedure-inspection]
```

## Vergi uyumu

```yaml
id: vergi-uyumu
term: "Vergi uyumu"
en: "tax compliance"
definition: "Mükellefin vergi yükümlülüklerini kanuna uygun ve süresinde yerine getirmesi."
see_also: [kayit-disi-ekonomi]
cards: [kb-eco-42-8-informality-tax-compliance]
```

## Vergi yansıması

```yaml
id: vergi-yansimasi
term: "Vergi yansıması"
en: "tax incidence"
definition: "Bir verginin ekonomik yükünün alıcı ve satıcı arasında fiilen nasıl paylaşıldığı."
see_also: [talep-esnekligi]
cards: [kb-eco-1-5-price-controls-tax-incidence]
```

## Vergi ziyaı cezası

```yaml
id: vergi-ziyai-cezasi
term: "Vergi ziyaı cezası"
en: "tax loss penalty"
definition: "Verginin eksik veya geç tahakkuk ettirilmesi hâlinde, kaybedilen vergi üzerinden kesilen ceza."
see_also: [pismanlik]
cards: [kb-eco-43-6-tax-procedure-inspection]
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

## Veri çakışması

```yaml
id: veri-cakismasi
term: "Veri çakışması"
en: "Data conflict"
definition: "Aynı kaydın iki yerde farklı değiştirilmesi sonucu eşitlemede ortaya çıkan uyuşmazlık."
see_also: [senkronizasyon]
cards: [kb-ea-26-3-offline-mode-for-managers]
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

## Veri konumu

```yaml
id: veri-konumu
term: "Veri konumu"
en: "Data residency"
definition: "Verinin fiziksel olarak hangi ülke veya bölgede saklandığı."
see_also: [bulut-bilisim, kvkk]
cards: [kb-ea-16-5-cloud-cost-data-residency]
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

## Veri yönetişimi

```yaml
id: veri-yonetisimi
term: "Veri yönetişimi"
en: "data governance"
definition: "Veriyle ilgili kararları kimin verdiğini ve hangi kuralların geçerli olduğunu belirleyen düzen."
see_also: [ana-veri]
cards: [kb-ea-8-1-master-data-governance]
```

## Yatırılan sermayenin getirisi

```yaml
id: yatirilan-sermaye-getirisi
term: "Yatırılan sermayenin getirisi"
en: "return on invested capital, ROIC"
definition: "Vergi sonrası faaliyet kârının, faaliyetlerde kullanılan sermayeye (işletme sermayesi ve duran varlıklar) oranı."
see_also: [aosm]
cards: [kb-eco-31-2-cost-of-capital]
```

## Yatırımın getirisi (ROI)

```yaml
id: yatirimin-getirisi
term: "Yatırımın getirisi (ROI)"
en: "Return on investment"
definition: "Bir yatırımdan elde edilen net kazancın yatırım tutarına oranı; basit hâli paranın zaman değerini dikkate almaz."
see_also: [net-bugunku-deger]
cards: [kb-fmcg-2-4-roi-roce-npv]
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

## Yeniden satış fiyatının belirlenmesi

```yaml
id: yeniden-satis-fiyati
term: "Yeniden satış fiyatının belirlenmesi"
en: "resale price maintenance (RPM)"
definition: "Üreticinin bayinin satış fiyatını sabitlemesi, alt veya üst sınır koyması ya da tavsiye etmesi."
see_also: [dikey-kisit]
cards: [kb-eco-8-2-vertical-restraints]
```

## yeniden sipariş noktası

```yaml
id: yeniden-siparis-noktasi
term: "yeniden sipariş noktası"
en: "reorder point"
definition: "Stok bu seviyeye indiğinde yeni sipariş verilmesi gereken miktar; tedarik süresi boyunca beklenen talep ile güvenlik stokunun toplamı."
see_also: [ekonomik-siparis-miktari, guvenlik-stoku]
cards: [kb-fmcg-11-3-eoq-reorder-point, kb-fmcg-11-4-safety-stock]
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

## Yerine koyma maliyeti

```yaml
id: yerine-koyma-maliyeti
term: "Yerine koyma maliyeti"
en: "replacement cost"
definition: "Bir stok kalemini ya da varlığı bugünkü fiyatlarla yeniden edinmenin maliyeti."
see_also: [net-gerceklesebilir-deger]
cards: [kb-eco-32-4-finance-in-high-inflation, kb-eco-34-3-fixed-assets-depreciation]
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

## Yıllık ortalama bileşik büyüme (CAGR)

```yaml
id: cagr
term: "Yıllık ortalama bileşik büyüme (CAGR)"
en: "compound annual growth rate"
definition: "Çok yıllık bir dönemde her yıl aynı oranda büyünseydi gerekecek sabit yıllık oran."
see_also: [reel-buyume]
cards: [kb-eco-2-5-growth-rates-and-logs]
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

## Z raporu

```yaml
id: z-raporu
term: "Z raporu"
en: "Z report"
definition: "ÖKC'den gün sonunda alınan, günün mali satış toplamlarını gösteren rapor."
see_also: [okc]
cards: [kb-ea-28-3-pos-okc]
```

## Z-skoru

```yaml
id: z-skoru
term: "Z-skoru"
en: "Z-score"
definition: "Birkaç finansal oranı ağırlıklandırarak şirketin iflas riskini sınıflandıran skor; ilk olarak Altman (1968) tarafından geliştirildi."
see_also: [finansal-sikinti]
cards: [kb-eco-37-4-distress-signals-z-score]
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

## Zaman serisi

```yaml
id: zaman-serisi
term: "Zaman serisi"
en: "time series"
definition: "Düzenli zaman aralıklarıyla gözlenen değerler dizisi."
see_also: [mevsimsellik]
cards: [kb-eco-49-1-time-series-seasonality]
```

## Zamanaşımı

```yaml
id: zamanasimi
term: "Zamanaşımı"
en: "statute of limitations"
definition: "Kanunda öngörülen süre geçtikten sonra verginin tarh edilememesi veya tahsil edilememesi."
see_also: [vergi-incelemesi]
cards: [kb-eco-43-6-tax-procedure-inspection]
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

## Zihinsel bulunurluk

```yaml
id: zihinsel-bulunurluk
term: "Zihinsel bulunurluk"
en: "mental availability"
definition: "Bir satın alma durumunda markanın tüketicinin aklına gelme kolaylığı ve olasılığı."
see_also: [fiziksel-bulunurluk, penetrasyon]
cards: [kb-fmcg-12-6-case-brand-growth-plan, kb-fmcg-3-4-mental-physical-availability]
```

## Zincir mağaza

```yaml
id: zincir-magaza
term: "Zincir mağaza"
en: "Chain store"
definition: "6585 sayılı Kanun'a göre aynı unvan veya marka altında belirli şube sayısı ve mağaza büyüklüğü koşullarını sağlayan perakende işletme."
see_also: [haksiz-ticari-uygulama]
cards: [kb-fmcg-1-5-turkish-fmcg-landscape, kb-fmcg-13-17-turkish-trade-practice, kb-fmcg-13-2-strategic-selling, kb-fmcg-6-1-rtm-channels-formats, kb-fmcg-9-2-formats-private-label]
```

## Ziyaret sıklığı

```yaml
id: ziyaret-sikligi
term: "Ziyaret sıklığı"
en: "call frequency"
definition: "Bir satış noktasının belirli bir dönemde kaç kez ziyaret edildiği."
see_also: [nokta-evreni]
cards: [kb-fmcg-12-1-leading-sales-orgs, kb-fmcg-13-12-adaptive-selling, kb-fmcg-13-13-relationship-selling-trust, kb-fmcg-13-2-spin-solution-selling, kb-fmcg-13-8-sales-funnel-math, kb-fmcg-13-9-prospecting-account-segmentation, kb-fmcg-6-2-outlet-universe-segmentation, kb-fmcg-8-1-selling-formats, kb-fmcg-8-2-structured-sales-call, kb-fmcg-8-3-salesperson-performance-drivers, kb-fmcg-8-4-sales-force-sizing, kb-fmcg-8-5-territory-routing, kb-fmcg-8-6-sales-org-span-of-control, kb-fmcg-8-7-sales-kpi-design, kb-fmcg-8-9-coaching]
```

## Zorunlu ürün listesi

```yaml
id: zorunlu-urun-listesi
term: "Zorunlu ürün listesi"
en: "must-stock list"
definition: "Belirli bir nokta tipinde her zaman bulunması istenen ürünlerin listesi."
see_also: [mukemmel-magaza, sayisal-dagitim]
cards: [kb-fmcg-13-11-objections-closing-upsell, kb-fmcg-8-10-sfa-data-driven-selling, kb-fmcg-9-5-perfect-store]
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
