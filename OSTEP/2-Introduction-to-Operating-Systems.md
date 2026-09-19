# İşletim Sistemlerine Giriş

İşletim sistemleri dersi alıyorsanız, bir bilgisayar programı yürütüldüğünde neler olduğunu az çok biliyorsunuzdur. Aksi halde, bu kitap size zor gelecektir ve belki okumayı bırakıp gerekli önşart dersini almanız mantıklı olabilir.

Peki bir program yürütüldüğünde neler olur?

Bir program çalışırken çok basit bir şeyi yapar: talimatları yerine getirir. Saniyede milyonlarca (hatta milyarlarca) kez işlemci bellekten bir talimatı alır (*fetch*), çözümler (*decode*, yani ne olduğunu anlar) ve yürütür (*execute*, yani belirtilen işi yapar, iki sayıyı toplamak, belleğe erişmek, bir koşulu kontrol etmek, bir fonksiyona atlamak gibi). Bu talimatla işi bittiğinde, işlemci sonraki talimata geçer ve bu program bitene kadar böyle devam eder. ^[Elbette, modern işlemciler programlar daha hızlı çalışsın diye aslında çok sayıda değişik ve ürkütücü şeyler yaparlar, bir seferde birden fazla talimat yürütmek, sıradan bağımsız talimat tamamlamak gibi. Ancak burada bunlarla ilgilenmiyoruz, çoğu programda varsaydığımız basit modeli ele alıyoruz: talimatlar görünüşe göre bir bir ve arka arkaya, sırayla yürütülürler.]

Böylece **Von Neumann** modeli bilgisayarın temelini tanımlamış olduk. ^[Von Neumann bilgisayar sistemlerinin ilk öncülerindendi. Oyun teorisi ve atom bombasında da öncü çalışmalar yapmıştır.] Basit görünüyor, değil mi? Ancak bu derste şunu göreceğiz: bir program çalışırken, aynı zamanda her biri sistemi **kullanımı kolay** hale getirmek amacını taşıyan bir sürü işlem yürütülür.

Program çalıştırmayı kolay hale getirmek (hatta aynı anda birden fazla program çalıştırabilmenizi sağlamak), programların belleği paylaşmalarına izin vermek, programlara cihazlarla etkileşim imkanı sunmak gibi sorumlulukları olan bir yazılım gövdesi vardır. Bu yazılım gövdesine, sistemin kolay kullanılır bir şekilde doğru ve etkin çalışmasını sağlamakla görevli olduğu için **işletim sistemi (OS)** denir. ^[İlk zamanlar işletim sistemi için **süpervizör** ve **ana kontrol programı** gibi isimler düşünülmüştü.]

>MESELENİN ÖZÜ: KAYNAKLARI SANALLAŞTIRMAK
>Bu kitapta cevaplayacağımız bir merkezi soru oldukça basit: işletim sistemi kaynakları nasıl sanallaştırıyor? Bu meselemizin özüdür. İşletim sisteminin bunu *neden* yaptığı değil soru, bu açıktır, sistemi daha kullanımı kolay hale getirmek için. Dolayısıyla, biz işin *nasılına* odaklanacağız: işletim sistemi tarafından sanallaştırmayı elde etmek için hangi mekanizmalar ve politikalar kuruluyor? İşletim sistemi bunu nasıl bu kadar etkin bir biçimde yapabiliyor? Ne donanım desteği gerekiyor?

İşletim sisteminin bu görevi başarmak için ilk başvurduğu yol, **sanallaştırma** adı verilen bir genel tekniktir. Bu teknikte, işletim sistemi işlemci, bellek veya disk gibi bir **fiziksel** kaynağı alır ve kendisinin daha genel, güçlü ve kullanımı kolay bir **sanal** formuna dönüştürür. Bu nedenle, bazen işletim sisteminden **sanal makine** diye bahsederiz.
