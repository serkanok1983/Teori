# Güvenilir, Ölçeklenebilir ve Sürdürülebilir Uygulamalar

> İnternet o kadar iyi yapıldı ki çoğu kişi onu insan yapımından ziyade Pasifik Okyanusu gibi bir doğal kaynak olarak görüyor. En son ne zaman bu ölçekte bir teknoloji bu kadar hatasızdı?
> *Alan Kay, Dr Dobb's Journal'le mülakat (2012)*

Bugün çoğu uygulama *işlem-yoğun*dan ziyade *veri-yoğun*dur. Ham işlemci gücü artık bu uygulamalar için sınırlayıcı olmaktan çıkmıştır - işlenen verinin miktarı, karmaşıklığı ve hangi hızda değiştiği daha önemlidir.

Veri-yoğun bir uygulama tipik olarak yaygın ihtiyaç duyulan işlevleri sağlayan standart yapı taşlarından inşa edilir. Mesela çoğu uygulamanın,

* kendisi veya başka bir uygulama daha sonra erişebilsin diye veri depolamak (*veritabanları*)
* okumaları hızlandırmak için pahalı bir işlemin sonucunu hatırlamak (*önbellekler*)
* kullanıcılara arama ve filtreleme sağlamak (*arama indeksleri*)
* asenkron ele alınmak üzere başka bir prosese mesaj göndermek (*stream processing*)
* büyük miktarda birikmiş veriyi düzenli olarak işlemek (*batch processing*) gibi ihtiyaçları vardır.
