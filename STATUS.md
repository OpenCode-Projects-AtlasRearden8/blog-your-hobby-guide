# STATUS

Last verified: 2026-11-03 (all commands below re-run green).

## What was built

**Manual: Start a Hobby Blog on GitHub Pages for Free** — a complete,
local-first manual plus a working example blog, in one repository.

- `docs/` — the manual itself: index + 8 chapters (picking a niche,
  static-blog anatomy, the Markdown workflow, writing habits that
  stick, light AI drafting help with disclosure, photos, a weekly
  publishing rhythm, hiding costs) + a plain-English glossary appendix.
- `content/` — Markdown sources for the example blog (`posts/` with a
  date-slug template and three example posts, `pages/about.md`,
  `img/` for images).
- `site/` — the generated static blog: `index.html` (post list,
  newest first), `posts/` (each post + its own archive index),
  `about.html`, one page of `styles.css`, `robots.txt`, and a
  hand-built `favicon.ico`. It is both the deliverable example and the
  test vehicle for a GitHub Pages-style site.
- `tools/build.py` — dependency-free (Python 3 stdlib only) builder:
  converts Markdown posts/pages to HTML, skips `_`-prefixed drafts,
  copies `content/img/` to `site/img/`, writes index/archive pages.
- `tools/check.py` — site linter: resolves every internal link,
  requires index to link every post, forbids leaked drafts, checks
  titles/dates/alt text/https.
- `tools/test_build.py` — 13 unittest smoke tests (std lib only)
  covering the Markdown converter, front-matter parsing, and a full
  build in a temp directory, including draft exclusion and ordering.
- `tools/verify.sh` — one command that runs tests + build + checks.
- `README.md`, MIT `LICENSE` (Copyright (c) 2026 Asdale Dynamics, LLC).

## How to run it

```bash
sh tools/verify.sh                              # tests + build + checks
python3 tools/build.py                          # rebuild site/ from content/
python3 -m http.server 8000 --directory site    # preview at localhost:8000
python3 tools/check.py                          # link/quality checks
python3 tools/test_build.py                     # tests only
```

Requirements: Python 3 (no pip installs, no accounts, no keys).

## Verification results

- `sh tools/verify.sh` → 13/13 tests pass; build completes;
  `check.py` reports "OK — links, index, drafts, post quality: all good."
- Local HTTP smoke test: `python3 -m http.server` + curl returned
  HTTP 200 for `/`, one post page, `styles.css`, and `favicon.ico`.
- Render sanity: `##` sections correctly render as `<h3>` beneath each
  post's `<h1>` title; no cross-post content leakage.
- Draft safety: `_template.md` and any `_*` draft is never built or
  linked; checker fails if one ever leaks into `site/`.
- Secret scan (grep for key/token/password patterns) over docs,
  content, site, tools, README: clean. No personal data in files.

## Known gaps (deliberate, hobby-scale)

- The Markdown converter covers the common subset (headings, lists,
  quotes, fenced code, bold/italic/links/images); tables and footnotes
  are not supported — the manual suggests raw HTML for those cases.
- No publication automation: pushing to GitHub Pages is documented in
  Chapter 7 but intentionally left as a manual act; this repo never
  pushes or hosts anything itself.
- No comments, search, or analytics — by design (privacy + zero cost).
- Example images folder is empty by design (no stock assets bundled);
  Chapter 6 explains how to add your own with alt text.
- `site/` is regenerated; edits there are overwritten by the next
  build. Edit `content/` instead. (This is also stated in the docs.)
