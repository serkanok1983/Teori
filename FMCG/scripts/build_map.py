#!/usr/bin/env python3
"""Build map/LESSON-MAP.csv and map/LESSON-MAP.md from the three curricula + scripts/lesson_decisions.txt.
Usage: python3 scripts/build_map.py   (run from package root)"""
import csv, re, collections, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
CUR = {"fmcg": ROOT/"reference/FMCG-CURRICULUM.md", "eco": ROOT/"reference/ECO-CURRICULUM.md", "ea": ROOT/"reference/EA-CURRICULUM.md"}
EXPECT = {"fmcg": 109, "eco": 266, "ea": 195}
ROLE = {"A": ["uretici-sahibi","uretici-yonetici","bayi-sahibi","bayi-yonetici","satis-direktoru"],
        "O": ["uretici-sahibi","bayi-sahibi"], "U": ["uretici-sahibi","uretici-yonetici"],
        "B": ["bayi-sahibi","bayi-yonetici"], "S": ["satis-direktoru","satis-muduru","bolge-muduru","satis-sefi"],
        "F": ["saha-satis-temsilcisi"], "M": ["finans-muduru"], "L": ["depo-lojistik-muduru"], "I": ["it-yoneticisi"]}
ROLE_ORDER = ["uretici-sahibi","uretici-yonetici","bayi-sahibi","bayi-yonetici","satis-direktoru","satis-muduru",
              "bolge-muduru","satis-sefi","saha-satis-temsilcisi","finans-muduru","depo-lojistik-muduru","it-yoneticisi"]
LEVEL = {"t": "temel", "o": "orta", "i": "ileri"}

def parse(course, path):
    rows, unit = [], None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^### Unit (\d+) — (.+)$", line)
        if m: unit = (int(m.group(1)), m.group(2).strip()); continue
        m = re.match(r"^\|\s*((?:FMCG|ECO|EA)-\d+\.\d+)\s*\|(.*)$", line)
        if m:
            cells = [c.strip() for c in m.group(2).split("|")]
            title = cells[1] if course == "ea" else cells[0]
            rows.append(dict(lesson_id=m.group(1), course=course, unit=f"{unit[0]} — {unit[1]}", title=title))
    return rows

def card_id(lid, slug):
    c, n = lid.split("-"); u, k = n.split(".")
    return f"kb-{c.lower()}-{u}-{k}-{slug}"

lessons = []
for c, p in CUR.items():
    r = parse(c, p); assert len(r) == EXPECT[c], (c, len(r)); lessons += r
assert len(lessons) == 570 and len({l["lesson_id"] for l in lessons}) == 570

dec = {}
for line in (ROOT/"scripts/lesson_decisions.txt").read_text(encoding="utf-8").splitlines():
    if not line.strip() or line.startswith("#"): continue
    p = line.split("|"); p += [""]*(7-len(p))
    assert p[0] not in dec, p[0]; dec[p[0]] = p
assert set(dec) == {l["lesson_id"] for l in lessons}, set(dec) ^ {l["lesson_id"] for l in lessons}

FIT = {"d": "direct", "a": "adapt", "s": "split", "x": "skip-learner-only"}
cards = collections.OrderedDict()   # card_id -> dict
out = []
for l in lessons:
    lid, fit, roles, lvl, cat, slugs, notes = dec[l["lesson_id"]]
    row = dict(l, kb_fit="", target_roles="", target_level="", proposed_card_ids="", proposed_category="", notes=notes.strip())
    if fit.startswith("m:"):
        tgt = fit[2:]; t = dec[tgt]; assert t[1] in "das" and not t[1].startswith("m"), (lid, tgt)
        fit_s, roles, lvl, cat, slugs = f"merge-with:{tgt}", t[2], t[3], t[4], t[5].split("+")[0]
        ids = [card_id(tgt, slugs)]
    elif fit == "x":
        fit_s, ids = FIT["x"], []
    else:
        assert fit in "das" and roles and lvl in LEVEL and cat and slugs, lid
        fit_s = FIT[fit]; sl = slugs.split("+"); assert (len(sl) > 1) == (fit == "s"), lid
        ids = [card_id(lid, s) for s in sl]
    if ids:
        rl = sorted({r for ch in roles for r in ROLE[ch]}, key=ROLE_ORDER.index)
        row.update(target_roles=";".join(rl), target_level=LEVEL[lvl], proposed_card_ids=";".join(ids), proposed_category=cat)
        for cid in ids:
            cd = cards.setdefault(cid, dict(id=cid, course=l["course"] if not fit.startswith("m:") else fit[2:].split("-")[0].lower(),
                                            category=cat, level=LEVEL[lvl], roles=rl, lessons=[]))
            cd["lessons"].append(lid)
    row["kb_fit"] = fit_s; out.append(row)

cols = ["lesson_id","course","unit","title","kb_fit","target_roles","target_level","proposed_card_ids","proposed_category","notes"]
with open(ROOT/"map/LESSON-MAP.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(out)
with open(ROOT/"map/PLANNED-CARDS.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["card_id","course","category","level","roles","source_lessons"])
    for c in cards.values(): w.writerow([c["id"], c["course"], c["category"], c["level"], ";".join(c["roles"]), ";".join(c["lessons"])])

# ---- summary
fitk = lambda r: r["kb_fit"].split(":")[0]
md = ["# LESSON-MAP — özet (otomatik üretildi: scripts/build_map.py)", "",
      f"Toplam ders: **{len(out)}** (FMCG {EXPECT['fmcg']}, ECO {EXPECT['eco']}, EA {EXPECT['ea']}; sayımlar script ile doğrulandı).",
      f"Planlanan kart sayısı: **{len(cards)}**.", "",
      "Tam satır satır sınıflandırma: `LESSON-MAP.csv`. Planlanan kart listesi: `PLANNED-CARDS.csv`.", "",
      "## Ders kararları ve kart sayısı (kurs bazında)", "", "| Kurs | Ders | direct | adapt | split | merge-with | skip-learner-only | Kart |", "|---|---|---|---|---|---|---|---|"]
for c in ["fmcg","eco","ea"]:
    rs = [r for r in out if r["course"] == c]; cnt = collections.Counter(fitk(r) for r in rs)
    nc = sum(1 for cd in cards.values() if cd["course"] == c)
    md.append(f"| {c.upper()} | {len(rs)} | {cnt['direct']} | {cnt['adapt']} | {cnt['split']} | {cnt['merge-with']} | {cnt['skip-learner-only']} | {nc} |")
cnt = collections.Counter(fitk(r) for r in out)
md.append(f"| **Toplam** | {len(out)} | {cnt['direct']} | {cnt['adapt']} | {cnt['split']} | {cnt['merge-with']} | {cnt['skip-learner-only']} | **{len(cards)}** |")
md += ["", "Not: Kartın kursu, birleştirmede hedef dersin kursudur (ör. FMCG-2.5 → ECO-38.2 kartına katıldığı için ECO sayılır).", "",
       "## Ünite bazında", "", "| Kurs | Ünite | Ders | Kartta kullanılan | Atlanan | Bu üniteden doğan kart |", "|---|---|---|---|---|---|"]
for c in ["fmcg","eco","ea"]:
    units = collections.OrderedDict()
    for r in out:
        if r["course"] == c: units.setdefault(r["unit"], []).append(r)
    for u, rs in units.items():
        sk = sum(1 for r in rs if fitk(r) == "skip-learner-only")
        own = {cid for r in rs if fitk(r) in ("direct","adapt","split") for cid in r["proposed_card_ids"].split(";")}
        md.append(f"| {c.upper()} | {u} | {len(rs)} | {len(rs)-sk} | {sk} | {len(own)} |")
md += ["", "## Rol bazında (kartın hedef rolleri arasında bu rol olan kart sayısı)", "", "| Rol | Kart |", "|---|---|"]
for r in ROLE_ORDER: md.append(f"| {r} | {sum(1 for cd in cards.values() if r in cd['roles'])} |")
md += ["", "## Seviye ve kategori", "", "| Seviye | Kart |", "|---|---|"]
for lv in ["temel","orta","ileri"]: md.append(f"| {lv} | {sum(1 for cd in cards.values() if cd['level']==lv)} |")
md += ["", "| Kategori | Kart |", "|---|---|"]
for k, v in sorted(collections.Counter(cd["category"] for cd in cards.values()).items()): md.append(f"| {k} | {v} |")
md += ["", "## Sınıflandırma ilkeleri", "",
       "- Bilgi bankası, FMCG üreticisi ve bayisinin sahip/yöneticilerine, satış yönetimine, finans, depo-lojistik ve BT yöneticilerine hizmet eder.",
       "- `skip-learner-only`: saf teori/ispat (tüketici teorisi aksiyomları, genel denge, DSGE, büyüme modelleri), ekonometri iç işleyişi, portföy/varlık fiyatlama, türev fiyatlama, kamu maliyesi kuramı, yazılım mimarisi iç detayları (DDD, CQRS, Kubernetes, mesajlaşma desenleri), OMURGA'yı inşa edenlere özel EA-40.x dersleri, öğrenci kapstonları.",
       "- Bir satış direktörü, bayi sahibi veya finans müdürünün kullanabileceği her şey tutuldu; teorik dersler pratik bir karta katıldı (ör. ajans teorisi → prim sistemi kartı).",
       "- EA'nın iş tarafı (ERP/SFA/DMS/WMS seçimi, süreç, veri kalitesi, entegrasyon, e-fatura/e-irsaliye pratiği, bütçe sistemleri) dahil; teknik iç konular ya atlandı ya `it-yoneticisi` rolüne yönelik sade bir karta dönüştürüldü.",
       "- Mevzuat/vergi/oran içeren kartlar `notes` sütununda `valid_as_of` ile işaretlendi.", ""]
(ROOT/"map/LESSON-MAP.md").write_text("\n".join(md), encoding="utf-8")
(ROOT/"map/planned_card_ids.txt").write_text("\n".join(cards) + "\n", encoding="utf-8")
print(f"lessons={len(out)} cards={len(cards)}", {c: sum(1 for cd in cards.values() if cd['course']==c) for c in ['fmcg','eco','ea']}, dict(cnt))
