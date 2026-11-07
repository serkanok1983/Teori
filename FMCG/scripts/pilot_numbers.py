#!/usr/bin/env python3
"""Computes every number used in the 3 pilot cards. Output is pasted into the cards; re-run to check."""
from decimal import Decimal as D, ROUND_HALF_UP
q = lambda x, p="0.01": x.quantize(D(p), ROUND_HALF_UP)
def tl(x, p="0.01"):
    s = f"{q(x,p):,.{len(p.split('.')[1]) if '.' in p else 0}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")
pct = lambda x, p="0.01": tl(x*100, p)
print("== CARD 1: margin vs markup")
for m in [D("0.25"), D("0.12")]:
    print(f"margin {pct(m)}% -> markup {pct(m/(1-m))}%")
k = D("0.25"); print(f"markup 25% -> margin {pct(k/(1+k))}%")
C = D("100"); print("cost 100: wrong (x1.25) =", tl(C*D("1.25")), "margin of that =", pct((C*D("1.25")-C)/(C*D("1.25"))),"%; right (/0.75) =", tl(C/D("0.75")))
c, Pm, md, mr, t = D("20"), D("30"), D("0.12"), D("0.25"), D("0.20")
Pd = Pm/(1-md); Pr = Pd/(1-mr); Ps = Pr*(1+t)
print("Pd", tl(Pd), "dist gp", tl(Pd-Pm)); print("Pr", tl(Pr), "ret gp", tl(Pr-Pd)); print("Ps", tl(Ps), "KDV", tl(Ps-Pr))
print("mfr margin", pct((Pm-c)/Pm), "%")
for name, v in [("cost", c), ("mfr", Pm-c), ("dist", Pd-Pm), ("ret", Pr-Pd)]: print(name, tl(v), pct(v/Pr, "0.1"), "%")
print("sum check", tl(q(c)+q(Pm-c)+q(Pd-Pm)+q(Pr-Pd)), "vs Pr", tl(Pr))
print("== CARD 2: cash conversion cycle")
S, COGS, AR, INV, AP = D(120_000_000), D(105_000_000), D(14_000_000), D(9_000_000), D(11_000_000)
dso, dio, dpo = AR/S*365, INV/COGS*365, AP/COGS*365
print("DSO", tl(dso,"0.1"), "DIO", tl(dio,"0.1"), "DPO", tl(dpo,"0.1"), "CCC", tl(q(dso,"0.1")+q(dio,"0.1")-q(dpo,"0.1"),"0.1"), "(unrounded", tl(dso+dio-dpo,"0.1"),")")
nwc = AR+INV-AP; r = D("0.45"); gp = S-COGS
print("NWC", tl(nwc,"1"), "fin cost", tl(nwc*r,"1"), "gross profit", tl(gp,"1"), "share", pct(nwc*r/gp,"0.1"),"%")
daily = S/365; print("daily sales", tl(daily,"1"), "10 days DSO frees", tl(daily*10,"1"), "annual saving", tl(daily*10*r,"1"))
# inflation: 30-day receivable, 3% monthly inflation -> real value lost
for m_inf in [D("0.03")]:
    print("1.000.000 TL receivable 60 days at 3%/month real value", tl(D(1_000_000)/(1+m_inf)**2,"1"), "loss", tl(D(1_000_000)-D(1_000_000)/(1+m_inf)**2,"1"))
print("== CARD 3: order to cash")
cases, per, price, disc, kdv, unit_cost = 40, 12, D("30"), D("0.05"), D("0.20"), D("26")
ordered = cases*per; delivered_cases = 38; units = delivered_cases*per
gross = units*price; d = gross*disc; net = gross-d; vat = net*kdv; tot = net+vat; cogs = units*unit_cost
print("ordered units", ordered, "delivered units", units)
print("gross", tl(gross), "discount", tl(d), "net", tl(net), "KDV", tl(vat), "invoice total", tl(tot), "COGS", tl(cogs), "gross profit", tl(net-cogs), "gp%", pct((net-cogs)/net,"0.1"))
print("ordered value net if full", tl(ordered*price*(1-disc)), "lost sales net", tl((ordered-units)*price*(1-disc)))
print("fill rate", pct(D(units)/D(ordered),"0.1"),"%")
print("== extra checks")
print("card1 lost per unit", tl(C/D("0.75") - C*D("1.25")))
print("card3 journal debits", tl(tot + d), "credits", tl(gross + vat))
print("card3 unit net price", tl(price*(1-disc)), "short units", ordered-units)
