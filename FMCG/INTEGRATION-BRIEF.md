# Integration Brief for Claude Code — OMURGA Knowledge Base (v1.0)

**Audience:** Claude Code, working inside the OMURGA-Saha codebase.
**Owner:** Serkan Ok. **Content language:** Turkish (keep all card text in Turkish; do not translate).
**Goal:** Import the Markdown knowledge cards in this package into the app's **existing** knowledge base / content feature, **merging** with existing content, never overwriting it.

> Note on content (TR): Kartlar yöneticilere yönelik, Türkçe, kısa bilgi kartlarıdır. Metin dili `STYLE-GUIDE.md`'de tanımlıdır. Entegrasyon sırasında metin değiştirilmemeli; yalnızca biçim/alan eşlemesi yapılmalıdır.

## Package contents you will use
- `SCHEMA.md` — frontmatter fields and body structure (source of truth).
- `taxonomy.md` — 33 categories in 3 groups (machine-readable table).
- `cards/<category>/<id>.md` — 288 cards (FMCG 97, ECO 85, EA 106), all `status: draft`.
- `glossary/terms.md` — 477 glossary entries (H2 + yaml block). Ignore `glossary/_merged/` (archive only).
- `reports/QA-REPORT.md`, `reports/REVIEW-NEEDED.md` — quality and review status; read-only for you.
- `map/LESSON-MAP.csv`, `map/PLANNED-CARDS.csv` — mapping of 570 curriculum lessons to the 288 cards.
- `scripts/validate.py` — run it before importing (`pip install pyyaml`).

## Non-negotiables (summary)
1. Inspect the existing KB first; assume nothing about the stack.
2. Never overwrite or delete existing content.
3. Produce `MERGE-REPORT.md`.
4. Import idempotently, keyed by `id`.
5. End users see only `published` cards; all new cards stay `draft` until Serkan sets `reviewed`/`published`.
6. Show `valid_as_of` on `time_sensitive: true` cards.

## Step 0 — Inspect first, assume nothing
- Find the existing KB/content implementation: storage (DB tables, CMS, JSON/MD files, Firestore, etc.), models, admin screens, rendering components, search, role/permission system.
- Do **not** assume a stack. Read the code and existing data before writing anything.
- Export or snapshot the existing KB content (read-only) for the merge analysis.

## Step 1 — Propose a mapping
- Map each frontmatter field in `SCHEMA.md` to the existing model (e.g. `category` → existing category entity, `roles` → existing role/permission ids, `tags`, `level`, `status`).
- Fields with no target: store in a metadata/JSON column or a sidecar, don't drop them (especially `id`, `source_lessons`, `sources`, `valid_as_of`, `version`).
- If the mapping is ambiguous (e.g. role names differ, categories overlap), write a **short plan** (max one page) and ask Serkan before implementing. Otherwise proceed.

## Step 2 — Idempotent importer
- The stable key is `id` (e.g. `kb-ea-20-2-order-to-cash`). Store it on the imported record.
- Re-running the importer must update records with the same `id` (only if `version`/`updated` changed) and never create duplicates.
- Import glossary entries keyed by glossary `id`.
- Run `bash scripts/check-all.sh` (or `scripts/validate.py`) as a pre-step; abort on errors. Warnings about `verified: false` sources are expected.
- Provide a dry-run mode that prints what would be created/updated/skipped.

## Step 3 — Merge rules (most important)
- Compare each incoming card against existing articles by title and topic similarity (title, summary, key terms; a simple normalized-text similarity is enough — explain the threshold you used).
- **Never delete or overwrite existing text.**
- If no match: create a new article.
- If a match exists: keep the existing article as-is. Either (a) add our card as a new separate article and link the two, or (b) append our content as a clearly marked section (e.g. heading "OMURGA Bilgi Kartı (v1.0)") — choose one approach consistently and state it.
- Possible duplicates and contradictions (e.g. different numbers or definitions) must not be auto-resolved; list them.
- Produce `MERGE-REPORT.md` with: matches (incoming id ↔ existing article, score, decision), new articles, possible duplicates, content conflicts, skipped items, and open decisions for Serkan.

## Step 4 — Taxonomy, filtering, search
- Create the 33 categories / 3 groups from `taxonomy.md` (merge with existing categories where they clearly match; record mapping in MERGE-REPORT).
- Support filtering by category, tags, roles, level. A user should see cards matching their role by default, with an option to see all.
- Make title, summary, key_points, body and glossary terms searchable. Turkish-aware search: case-folding for İ/ı, I/i and diacritic-insensitive matching (ç, ğ, ö, ş, ü) if the search engine allows.

## Step 5 — Cross-links
- Render `related` as links. All related ids resolve within this package; if a target is unpublished, hide the link for end users.
- Link glossary terms (`glossary_terms`) to glossary entries.

## Step 6 — Rendering checks
- Turkish characters (ç ğ ı İ ö ş ü) display correctly everywhere (UTF-8 end to end, including slugs/URLs).
- Markdown tables, blockquote callouts (`> **Örnek (temsili rakamlar):**`, `> **Mevzuat notu:**`, `> **İpucu:**`), checklists `- [ ]`.
- Math: if the app supports KaTeX, render `$...$`; otherwise show plain text. Current cards use plain-text formulas.
- Mobile layout (field users are on phones): tables scroll horizontally rather than overflow.

## Step 7 — Status workflow
- `status`: `draft` → `reviewed` → `published`. Only `published` cards are visible to end users; drafts visible to admins/editors only.
- All 288 cards are `draft`: after import they must **not** be visible to end users.
- Keep every new card `draft` until Serkan sets it to `reviewed`/`published`. Never change `status` yourself and never auto-publish.
- On re-import, do not downgrade a status Serkan has already changed in the app.

## Step 8 — Validity date
- If `time_sensitive: true`, show `valid_as_of` on the card (e.g. "Bilgiler 28.10.2026 itibarıyla geçerlidir") near the title, and keep the in-body mevzuat note.

## Step 9 — Test checklist
- [ ] Validator passes; importer dry-run output reviewed.
- [ ] Import twice → no duplicates, no changes on second run.
- [ ] Existing articles unchanged (diff before/after).
- [ ] MERGE-REPORT.md created and committed.
- [ ] Drafts hidden from a non-admin user; visible to admin.
- [ ] Role filter works (e.g. `saha-satis-temsilcisi` sees only matching cards by default).
- [ ] Search finds "işletme sermayesi" with query "isletme sermayesi" and "İŞLETME".
- [ ] Tables, callouts, checklists, Turkish characters render on desktop and mobile.
- [ ] `valid_as_of` shown on every `time_sensitive: true` card (47 cards).
- [ ] Links to not-yet-written related cards do not 404.

Deliver: code changes, `MERGE-REPORT.md`, short summary of the mapping decisions.
