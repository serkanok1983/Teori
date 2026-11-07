# FMCG batch 6 temsili rakamlar (10-x, 11-1..11-7). Tüm girdiler varsayımdır.
import math, random, statistics as st
def tr(x, d=0):
    s = f"{x:,.{d}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")

print("== 10-1 müşteri kâr-zarar")
liste=20_000_000; fa=0.10; inv=liste*(1-fa)
prim=inv*0.04; listeleme=300_000; promo=900_000
netnet=inv-prim-listeleme-promo
smm=liste*0.45; brut=netnet-smm
lojistik=netnet*0.03; kam=600_000; vade=inv*0.40*60/365
katki=brut-lojistik-kam-vade
for k,v in [("liste",liste),("fatura",inv),("ciro primi",prim),("netnet",netnet),("smm",smm),("brüt",brut),("lojistik",lojistik),("kam",kam),("vade maliyeti",vade),("müşteri katkısı",katki)]:
    print(k, tr(v))
print("katkı/liste %", tr(katki/liste*100,1), "katkı/netnet %", tr(katki/netnet*100,1))

print("== 10-2 fiyat şelalesi (birim 100 TL liste)")
L=100; f=L*0.92; cp=f*0.04; pr=f*0.03; nn=f-cp-pr; vd=f*0.40*60/365; cep=nn-vd
print("fatura",tr(f,2),"ciro primi",tr(cp,2),"promosyon",tr(pr,2),"netnet",tr(nn,2),"vade",tr(vd,2),"cep",tr(cep,2))
print("toplam fark %", tr((L-cep),2))
print("vade 60->90 ek maliyet", tr(f*0.40*30/365,2))

print("== 10-4 koşullu prim")
s=18_000_000; ask=s*0.02
g=0.08; ext=s*g; katk=ext*0.30; primg=s*(1+g)*0.02
print("koşulsuz +2 puan maliyet", tr(ask), "büyüme", tr(ext), "ek katkı", tr(katk), "koşullu prim maliyeti", tr(primg), "net", tr(katk-primg))
g2=0.05; ext2=s*g2; print("büyüme %5 ise hedef tutmaz, prim 0; ek katkı", tr(ext2*0.30))
# eşik: büyüme g için katkı s*g*0.30 >= s*(1+g)*0.02  => g >= 0.02/(0.28)
print("başabaş büyüme %", tr(0.02/0.28*100,1))

print("== 10-6 yeni ürün kanibalizasyon")
yeni=40_000; kan=0.60; net=yeni*(1-kan)
print("yeni ürün aylık satış", tr(yeni), "kanibalizasyon %60", tr(yeni*kan), "net kategori artışı", tr(net))
print("kategori 5.000.000 içinde büyüme %", tr(net/5_000_000*100,2))

print("== 10-7 ortak iş planı")
base=18_000_000; inits={"dağıtım":0.03,"promosyon":0.02,"yeni ürün":0.025}
tot=0
for k,v in inits.items(): print(k, tr(base*v)); tot+=base*v
print("toplam", tr(tot), "%", tr(tot/base*100,1), "katkı %30", tr(tot*0.30), "yatırım 200.000 net", tr(tot*0.30-200_000))

print("== 11-1 nakit dönüşüm")
dio,dso,dpo=45,60,40; ccc=dio+dso-dpo; sales=120_000_000
print("NDS", ccc, "günlük satış", tr(sales/365), "bağlı sermaye (satış bazlı yaklaşık)", tr(sales/365*ccc))
print("stok 45->35 gün serbest kalan (satış bazlı)", tr(sales/365*10))

print("== 11-2 tahmin")
a=[100,120,90,110,130,105]; fc=[110,110,100,100,120,115]
ape=[abs(x-y)/x for x,y in zip(a,fc)]
print("MAPE %", tr(sum(ape)/len(ape)*100,1), "bias toplam", sum(y-x for x,y in zip(a,fc)), "WAPE %", tr(sum(abs(x-y) for x,y in zip(a,fc))/sum(a)*100,1))
naive=a[:-1]; ape2=[abs(x-y)/x for x,y in zip(a[1:],naive)]
print("naif (geçen hafta) MAPE % (5 hafta)", tr(sum(ape2)/len(ape2)*100,1))
ape1=[abs(x-y)/x for x,y in zip(a[1:],fc[1:])]
print("aynı 5 haftada tahmin MAPE %", tr(sum(ape1)/len(ape1)*100,1))

print("== 11-3 EOQ")
D=12000; S=600; c=200; h=0.25; H=c*h
eoq=math.sqrt(2*D*S/H); print("EOQ", tr(eoq,1))
for q in [200,537,1000,2000]:
    tc=D/q*S+q/2*H; print("Q",q,"sipariş",tr(D/q*S),"tutma",tr(q/2*H),"toplam",tr(tc))
d=D/300; LT=5; print("günlük",tr(d),"ROP (güvenlik stoku hariç)", tr(d*LT), "ss 44 ile", tr(d*LT+44))

print("== 11-4 güvenlik stoku")
sd=12; LT=5; sL=sd*math.sqrt(LT); print("sigma_L", tr(sL,1))
for sl,z in [(90,1.282),(95,1.645),(98,2.054),(99,2.326),(99.9,3.090)]:
    print(sl, z, tr(z*sL,1))
print("tedarik süresi 5->10 gün, %95", tr(1.645*sd*math.sqrt(10),1))

print("== 11-5 kamçı etkisi simülasyonu")
random.seed(7)
T=200; dem=[max(0,random.gauss(100,10)) for _ in range(T)]
def tier(orders_in, L=2, n=4):
    out=[]; hist=[]
    inv_pos=None
    for t,x in enumerate(orders_in):
        hist.append(x)
        f=sum(hist[-n:])/len(hist[-n:])
        target=f*(L+1)
        prev=getattr(tier,'_p',None)
        out.append(x)  # placeholder
    return out
# standart sipariş-yukarı politikası: sipariş_t = talep_t + (S_t - S_{t-1}), S_t=(L+1)*MA_n
def order_up_to(d, L=2, n=4):
    S=[]; o=[]
    for t in range(len(d)):
        w=d[max(0,t-n+1):t+1]; S.append((L+1)*sum(w)/len(w))
        o.append(max(0, d[t]+(S[t]-S[t-1] if t>0 else 0)))
    return o
r=order_up_to(dem); w=order_up_to(r); f=order_up_to(w)
sd0=st.pstdev(dem[10:]);
for name,s in [("tüketici",dem),("perakendeci",r),("dağıtıcı",w),("fabrika",f)]:
    print(name, "ort", tr(st.mean(s[10:]),1), "std", tr(st.pstdev(s[10:]),1), "oran", tr(st.pstdev(s[10:])/sd0,1))

print("== 11-6 S&OP")
dp=100_000; cap=90_000; gap=dp-cap; k=40; ot=6_000; otc=15
print("açık", tr(gap), "kayıp katkı", tr(gap*k), "fazla mesai maliyeti", tr(ot*otc), "kurtarılan katkı", tr(ot*k), "net", tr(ot*k-ot*otc), "kalan açık", tr(gap-ot), "kalan kayıp", tr((gap-ot)*k))

print("== 11-7 ağ")
ss1=1_000_000; ss2=ss1*math.sqrt(2); car=0.30
for name,dep,nak,ss in [("1 merkez",6_000_000,14_000_000,ss1),("2 bölge",9_000_000,10_000_000,ss2)]:
    print(name,"depo",tr(dep),"nakliye",tr(nak),"güvenlik stoku",tr(ss),"taşıma",tr(ss*car),"toplam",tr(dep+nak+ss*car))
