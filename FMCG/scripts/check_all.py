#!/usr/bin/env python3
"""OMURGA KB full QA check. Usage: python3 scripts/check_all.py  (or scripts/check-all.sh)
Writes reports/QA-REPORT.md (auto section) and exits 1 on any error."""
import os, re, glob, subprocess, sys, collections, statistics, yaml, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
errs = []
v = subprocess.run([sys.executable, "scripts/validate.py"], capture_output=True, text=True)
vsum = v.stdout.strip().splitlines()[-1]
if v.returncode: errs.append("validator: " + vsum)
cards = {}
for f in sorted(glob.glob("cards/*/*.md")):
    t = open(f, encoding="utf-8").read(); m = re.match(r"^---\n(.*?)\n---\n(.*)$", t, re.S)
    d = yaml.safe_load(m.group(1)); d["_f"] = f; d["_words"] = len(re.findall(r"\w+", m.group(2)))
    if d["id"] in cards: errs.append(f"duplicate id {d['id']}")
    cards[d["id"]] = d
gl = {}
for h, y in re.findall(r"^## (.+?)\n+```yaml\n(.*?)```", open("glossary/terms.md", encoding="utf-8").read(), re.S | re.M):
    g = yaml.safe_load(y)
    if g["id"] in gl: errs.append(f"duplicate glossary id {g['id']}")
    gl[g["id"]] = g
dangling = [(c, r) for c, d in cards.items() for r in d.get("related") or [] if r not in cards]
self_rel = [c for c, d in cards.items() if c in (d.get("related") or [])]
missing_terms = [(c, g) for c, d in cards.items() for g in d.get("glossary_terms") or [] if g not in gl]
gl_bad_cards = [(k, c) for k, g in gl.items() for c in g.get("cards") or [] if c not in cards]
gl_bad_see = [(k, s) for k, g in gl.items() for s in g.get("see_also") or [] if s not in gl]
for lst, name in [(dangling, "dangling related"), (missing_terms, "missing glossary term"), (gl_bad_cards, "glossary cards→missing card"), (gl_bad_see, "glossary see_also→missing term")]:
    errs += [f"{name}: {a} → {b}" for a, b in lst]
newfiles = glob.glob("glossary/terms-*-new.md")
if newfiles: errs.append(f"unmerged glossary files: {newfiles}")
C = lambda k: collections.Counter(x for d in cards.values() for x in (d[k] if isinstance(d[k], list) else [d[k]]))
words = sorted(d["_words"] for d in cards.values())
def pct(p): return words[min(len(words) - 1, int(p * len(words)))]
bins = collections.Counter(min(b, 1400) // 100 * 100 for b in words)
ts = sorted((d["id"], str(d.get("valid_as_of"))) for d in cards.values() if d.get("time_sensitive"))
unv = collections.defaultdict(list)
for d in cards.values():
    for s in d["sources"]:
        if s.get("verified") is not True: unv[f"{s['title']} ({s.get('authors')}, {s.get('year')}, {s.get('type')})"].append(d["id"])
thin = sorted((d["_words"], d["id"]) for d in cards.values() if d["_words"] < 450)
o = ["<!-- AUTO:START (scripts/check_all.py) -->", f"## Otomatik kontrol sonuçları ({datetime.date.today()})", "",
     f"- Validator: `{vsum}`", f"- Kart: {len(cards)} · benzersiz id: {len(set(cards))} · sözlük terimi: {len(gl)}",
     f"- Kırık `related`: {len(dangling)} · kendine `related`: {len(self_rel)} · eksik sözlük terimi: {len(missing_terms)} · sözlükte olmayan kart: {len(gl_bad_cards)} · kırık `see_also`: {len(gl_bad_see)}",
     f"- **Sonuç: {'GEÇTİ (0 hata)' if not errs else 'HATA: ' + str(len(errs))}**", ""]
for e in errs: o.append(f"  - ERROR {e}")
for k, title in [("course", "Kurs"), ("category", "Kategori"), ("roles", "Rol"), ("level", "Seviye"), ("status", "Durum")]:
    o += ["", f"### {title} bazında kart sayısı", "", f"| {k} | kart |", "|---|---|"] + [f"| {a} | {b} |" for a, b in sorted(C(k).items())]
o += ["", "### Kelime sayısı dağılımı (gövde)", "", f"min {words[0]} · p10 {pct(.1)} · medyan {int(statistics.median(words))} · ort. {int(statistics.mean(words))} · p90 {pct(.9)} · max {words[-1]}", "", "| aralık | kart |", "|---|---|"]
o += [f"| {b}–{b+99} | {n} |" for b, n in sorted(bins.items())]
o += ["", f"Kısa kartlar (<450 kelime): {len(thin)}"] + [f"- {i} ({w})" for w, i in thin]
o += ["", f"### time_sensitive: true kartlar ({len(ts)})", "", "| id | valid_as_of |", "|---|---|"] + [f"| {a} | {b} |" for a, b in ts]
o += ["", f"### verified:false kaynaklar ({len(unv)} benzersiz kaynak, {sum(map(len, unv.values()))} atıf, {len({c for v in unv.values() for c in v})} kart)", ""]
o += [f"- {k} — {len(v)} kart: {', '.join(sorted(v))}" for k, v in sorted(unv.items())]
o.append("<!-- AUTO:END -->")
auto = "\n".join(o) + "\n"
rp = "reports/QA-REPORT.md"
old = open(rp, encoding="utf-8").read() if os.path.exists(rp) else "# QA-REPORT — OMURGA Bilgi Bankası v1.0\n\n<!-- AUTO:START --><!-- AUTO:END -->\n"
new = re.sub(r"<!-- AUTO:START.*?<!-- AUTO:END -->\n?", lambda _: auto, old, flags=re.S)
os.makedirs("reports", exist_ok=True); open(rp, "w", encoding="utf-8").write(new)
print(vsum); print(f"{len(cards)} cards, {len(gl)} terms, {len(errs)} errors, {len(unv)} unverified sources, {len(ts)} time-sensitive, {len(thin)} thin")
sys.exit(1 if errs else 0)
