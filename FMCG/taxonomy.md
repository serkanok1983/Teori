# Kategori ağacı (taxonomy) — v0.1

Üç üst grup, 33 kategori. Kategori, kartın konusunu belirtir (hangi müfredattan geldiğini değil). Kartın `category` alanı aşağıdaki **slug** sütunundan biri olmalıdır. Bu tablo `scripts/validate.py` tarafından okunur; biçimini bozmayın.

Üst gruplar:
- **Ticari Yönetim** — satış, dağıtım, bayi, fiyat, perakende (ağırlıkla FMCG müfredatı)
- **Ekonomi ve Finans** — enflasyon, nakit, finansal tablolar, vergi (ağırlıkla ECO müfredatı)
- **İş Sistemleri ve Dijitalleşme** — ERP, saha satış yazılımı, e-belge, veri (ağırlıkla EA müfredatı)

| slug | Türkçe ad | üst grup | açıklama |
|---|---|---|---|
| sektor-ve-kanal | Sektör ve Kanal Yapısı | Ticari Yönetim | Hızlı tüketim sektörü, değer zinciri, marjlar, kanal aktörleri, Türkiye pazarı |
| ticari-finans | Ticari Finans ve Kârlılık | Ticari Yönetim | Kâr-zarar, brütten nete, katkı payı, başabaş, sapma analizi |
| tuketici-ve-marka | Tüketici, Alışveriş ve Marka | Ticari Yönetim | Satın alma davranışı, marka büyümesi, pazar araştırması |
| strateji-ve-portfoy | Strateji ve Ürün Portföyü | Ticari Yönetim | Konumlandırma, portföy, yeni ürün, SKU sadeleştirme |
| fiyatlama-ve-promosyon | Fiyatlama ve Promosyon | Ticari Yönetim | Fiyat esnekliği, fiyat-ambalaj mimarisi, promosyon getirisi, enflasyonda fiyat |
| dagitim-modeli | Dağıtım Modeli (Pazara Erişim) | Ticari Yönetim | Kanallar, nokta evreni, hizmet maliyeti, direkt/dolaylı dağıtım |
| bayi-yonetimi | Bayi (Distribütör) Yönetimi | Ticari Yönetim | Bayi kâr-zararı, yatırım getirisi, tahsilat, bayi seçimi ve geliştirme |
| saha-satis-ekibi | Saha Satış Ekibi Yönetimi | Ticari Yönetim | Satış formatları, ekip büyüklüğü, bölge ve rota, KPI, prim, koçluk |
| satis-teknikleri | Satış Teknikleri ve Müzakere | Ticari Yönetim | Satış yöntemleri, itiraz, kapanış, müzakere, satış tahmini |
| perakende-uygulama | Mağazada Uygulama ve Perakende | Ticari Yönetim | Raf, planogram, stoksuzluk, mükemmel mağaza, trade marketing |
| kilit-musteri-ve-kategori | Zincir Marketler ve Kategori Yönetimi | Ticari Yönetim | Kilit müşteri yönetimi, ticari şartlar, kategori yönetimi, ortak iş planı |
| tedarik-zinciri-ve-stok | Tedarik Zinciri ve Stok | Ticari Yönetim | Talep tahmini, stok politikası, kamçı etkisi, S&OP, soğuk zincir |
| liderlik-ve-degisim | Liderlik, Değişim ve Uyum | Ticari Yönetim | Satış liderliği, dijital dönüşüm, etik, rekabet hukuku, sürdürülebilirlik |
| ekonomi-temelleri | İşletmeler için Ekonomi | Ekonomi ve Finans | Arz-talep, fırsat maliyeti, fiyat farklılaştırma, oyun teorisi, davranışsal ekonomi |
| makroekonomi-ve-enflasyon | Enflasyon, Faiz ve Kur | Ekonomi ve Finans | Enflasyon ölçümü, reel faiz, TCMB politikası, kur, kriz dersleri |
| finansal-tablolar | Muhasebe ve Finansal Tablolar | Ekonomi ve Finans | Çift taraflı kayıt, bilanço, gelir tablosu, nakit akış, enflasyon muhasebesi |
| finansal-analiz | Finansal Analiz, Nakit ve Kredi | Ekonomi ve Finans | Oranlar, işletme sermayesi, nakit dönüşüm süresi, müşteri kredisi, nakit yönetimi |
| kurumsal-finans | Yatırım ve Finansman Kararları | Ekonomi ve Finans | Paranın zaman değeri, NBD/İVO, kredi, değerleme, yüksek enflasyonda finans |
| maliyet-ve-butce | Maliyet, Bütçe ve Performans | Ekonomi ve Finans | Maliyetleme, faaliyet tabanlı maliyet, bütçe, yuvarlanan tahmin, karne |
| vergi-ve-mevzuat | Vergi ve Mevzuat | Ekonomi ve Finans | Türk vergi sistemi, KDV, ÖTV, kurumlar vergisi, SGK, bordro |
| finansal-piyasalar-ve-risk | Banka, Sigorta ve Risk | Ekonomi ve Finans | Bankalarla çalışma, kur riskinden korunma, sigorta, risk yönetimi |
| veri-ve-istatistik | Veriyle Karar Verme | Ekonomi ve Finans | Tanımlayıcı istatistik, örnekleme, test-kontrol, korelasyon, mevsimsellik |
| is-sistemleri-temelleri | İş Yazılımlarının Temelleri | İş Sistemleri ve Dijitalleşme | Kurumsal sistem nedir, bulut/SaaS, uygulama portföyü, benimseme |
| surec-yonetimi | Süreç Yönetimi | İş Sistemleri ve Dijitalleşme | Süreç tanımı, süreç haritası, döngü süresi, süreç madenciliği, onay akışları |
| veri-yonetimi | Ana Veri ve Raporlama | İş Sistemleri ve Dijitalleşme | Ana veri, veri kalitesi, barkod/GS1, raporlama, gösterge panoları |
| entegrasyon | Sistem Entegrasyonu | İş Sistemleri ve Dijitalleşme | Neden zor, EDI, API, saha satış–ERP entegrasyonu |
| erp | ERP | İş Sistemleri ve Dijitalleşme | ERP nedir, siparişten tahsilata, satın almadan ödemeye, stok, hesap planı |
| saha-satis-ve-dms | Saha Satış, CRM ve Bayi Sistemleri | İş Sistemleri ve Dijitalleşme | SFA, DMS, sıcak satış/ön satış, fiyat motoru, promosyon yönetimi, B2B sipariş |
| tedarik-ve-depo-sistemleri | Depo, Sevkiyat ve Planlama Sistemleri | İş Sistemleri ve Dijitalleşme | WMS, TMS, rota planlama, talep planlama, izlenebilirlik |
| e-belge-ve-odeme | e-Belge, Ödeme ve Tahsilat Sistemleri | İş Sistemleri ve Dijitalleşme | e-fatura, e-irsaliye, e-arşiv, e-defter, ödeme sistemleri, DBS, Findeks |
| yazilim-secimi-ve-proje | Yazılım Seçimi ve Proje Yönetimi | İş Sistemleri ve Dijitalleşme | Al/yap kararı, toplam sahip olma maliyeti, tedarikçi seçimi, devreye alma |
| bt-yonetisimi-ve-guvenlik | BT Yönetişimi, Güvenlik ve KVKK | İş Sistemleri ve Dijitalleşme | Yetkiler, iç kontrol, yedekleme, KVKK, belge saklama |
| yapay-zeka-ve-otomasyon | Yapay Zekâ ve Otomasyon | İş Sistemleri ve Dijitalleşme | Düşük kodlu araçlar, RPA, üretken yapay zekâ, tahmin ve öneri modelleri |

## Önerilen etiketler (tags)

`marj`, `fiyatlama`, `kar-orani`, `kdv`, `enflasyon`, `nakit`, `isletme-sermayesi`, `tahsilat`, `vade`, `stok`, `bayi`, `zincir-market`, `geleneksel-kanal`, `saha-satis`, `rota`, `kpi`, `prim`, `promosyon`, `erp`, `sfa`, `dms`, `wms`, `e-fatura`, `e-irsaliye`, `muhasebe`, `vergi`, `mevzuat`, `veri-kalitesi`, `entegrasyon`, `kvkk`, `butce`, `raporlama`.

## Rol filtresi için gruplar (uygulamada kolay seçim)

- **Sahipler:** uretici-sahibi, bayi-sahibi
- **Üst yönetim:** uretici-yonetici, bayi-yonetici, satis-direktoru
- **Satış yönetimi:** satis-direktoru, satis-muduru, bolge-muduru, satis-sefi
- **Saha:** saha-satis-temsilcisi
- **Destek fonksiyonları:** finans-muduru, depo-lojistik-muduru, it-yoneticisi
