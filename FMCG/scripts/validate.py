#!/usr/bin/env python3
"""OMURGA KB card validator. Usage: python3 scripts/validate.py [card paths...]
Default: validates every cards/**/*.md. Exit 1 if any ERROR."""
import sys, re, csv, datetime, glob, os
try:
    import yaml
except ImportError:
    sys.exit("PyYAML gerekli: pip install pyyaml")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)
ROLES = {"uretici-sahibi","uretici-yonetici","bayi-sahibi","bayi-yonetici","satis-direktoru","satis-muduru","bolge-muduru","satis-sefi","saha-satis-temsilcisi","finans-muduru","depo-lojistik-muduru","it-yoneticisi"}
LEVELS = {"temel","orta","ileri"}; STATUS = {"draft","reviewed","published"}; COURSES = {"fmcg","eco","ea"}
REQ = ["id","title","summary","course","category","tags","roles","level","source_lessons","reading_minutes","key_points","glossary_terms","related","sources","time_sensitive","status","language","version","updated"]
HEADINGS = ["Ne işe yarar?","Temel fikir","Bir örnek","Sık yapılan hatalar","Pratikte nasıl uygulanır?","Daha fazlası"]
ID_RE = re.compile(r"^kb-(fmcg|eco|ea)-\d+-\d+-[a-z0-9]+(-[a-z0-9]+)*$")
cats = set(re.findall(r"^\|\s*([a-z0-9-]+)\s*\|", open(P("taxonomy.md"), encoding="utf-8").read(), re.M)) - {"slug"}
lessons = {r["lesson_id"] for r in csv.DictReader(open(P("map/LESSON-MAP.csv"), encoding="utf-8"))}
planned = set(open(P("map/planned_card_ids.txt")).read().split())
gloss = set(re.findall(r"^id:\s*([a-z0-9-]+)", open(P("glossary/terms.md"), encoding="utf-8").read(), re.M))
files = sys.argv[1:] or sorted(glob.glob(P("cards/**/*.md"), recursive=True))
errs = warns = 0; seen = {}
def date_ok(v):
    if isinstance(v, datetime.date): return True
    try: datetime.date.fromisoformat(str(v)); return True
    except ValueError: return False
for f in files:
    rel = os.path.relpath(os.path.abspath(f), ROOT); E=[]; W=[]
    txt = open(f, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", txt, re.S)
    if not m: print(f"ERROR {rel}: frontmatter yok"); errs+=1; continue
    try: d = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e: print(f"ERROR {rel}: YAML: {e}"); errs+=1; continue
    body = m.group(2)
    for k in REQ:
        if k not in d: E.append(f"eksik alan: {k}")
    cid = d.get("id","")
    if not ID_RE.match(str(cid)): E.append(f"id biçimi hatalı: {cid}")
    if cid in seen: E.append(f"tekrarlanan id ({seen[cid]})")
    seen[cid]=rel
    if os.path.basename(f) != f"{cid}.md": E.append("dosya adı id ile aynı değil")
    if d.get("course") not in COURSES: E.append("course geçersiz")
    elif not str(cid).startswith(f"kb-{d['course']}-"): E.append("id course ile uyuşmuyor")
    c = d.get("category")
    if c not in cats: E.append(f"category taxonomy'de yok: {c}")
    if os.path.basename(os.path.dirname(f)) != c: E.append("klasör category ile aynı değil")
    for r in d.get("roles") or []:
        if r not in ROLES: E.append(f"bilinmeyen rol: {r}")
    if not d.get("roles"): E.append("roles boş")
    if d.get("level") not in LEVELS: E.append("level geçersiz")
    st = d.get("status")
    if st not in STATUS: E.append("status geçersiz")
    if d.get("language") != "tr": E.append("language 'tr' olmalı")
    if str(d.get("version")) != d.get("version"): E.append("version tırnaklı string olmalı")
    for l in d.get("source_lessons") or []:
        if l not in lessons: E.append(f"source_lessons LESSON-MAP'te yok: {l}")
    if not d.get("source_lessons"): E.append("source_lessons boş")
    if cid not in planned: W.append("id PLANNED-CARDS listesinde yok (yeni kart mı?)")
    kp = d.get("key_points") or []
    if not 3 <= len(kp) <= 6: E.append(f"key_points 3-6 olmalı ({len(kp)})")
    for g in d.get("glossary_terms") or []:
        if g not in gloss: E.append(f"glossary terimi yok: {g}")
    for r in d.get("related") or []:
        if r not in planned: E.append(f"related bilinmeyen id: {r}")
        elif not glob.glob(P("cards","*",f"{r}.md")): W.append(f"related henüz yazılmadı (planlı): {r}")
    if not date_ok(d.get("updated")): E.append("updated tarih değil")
    if d.get("time_sensitive") is True:
        if not date_ok(d.get("valid_as_of")): E.append("time_sensitive=true ama valid_as_of yok/hatalı")
        if "Mevzuat notu" not in body: E.append("time_sensitive kartta mevzuat notu yok")
    elif d.get("time_sensitive") is not False: E.append("time_sensitive true/false olmalı")
    srcs = d.get("sources") or []
    if not srcs: E.append("sources boş")
    for s in srcs:
        for k in ("title","authors","year","type","verified"):
            if k not in s: E.append(f"kaynakta eksik: {k} ({s.get('title')})")
        if s.get("verified") is True and not date_ok(s.get("checked_on")): E.append(f"verified kaynakta checked_on yok: {s.get('title')}")
        if s.get("verified") is not True:
            (E if st=="published" else W).append(f"doğrulanmamış kaynak: {s.get('title')}")
    hs = re.findall(r"^## (.+?)\s*$", body, re.M)
    if hs != HEADINGS: E.append(f"H2 başlıkları şemaya uymuyor: {hs}")
    if "> **Örnek (temsili rakamlar):**" not in body: E.append("örnek etiketi yok")
    words = len(re.findall(r"\w+", body)); est = max(1, round(words/200)); rm = d.get("reading_minutes")
    if not isinstance(rm,int) or not 1<=rm<=20: E.append("reading_minutes 1-20 tamsayı olmalı")
    elif abs(rm-est) > 2: E.append(f"reading_minutes {rm}, tahmin {est} ({words} kelime)")
    for e in E: print(f"ERROR {rel}: {e}")
    for w in W: print(f"WARN  {rel}: {w}")
    print(f"{'FAIL' if E else 'OK  '} {rel} ({words} kelime, ~{est} dk)")
    errs+=len(E); warns+=len(W)
print(f"\n{len(files)} kart, {errs} hata, {warns} uyarı")
sys.exit(1 if errs else 0)
