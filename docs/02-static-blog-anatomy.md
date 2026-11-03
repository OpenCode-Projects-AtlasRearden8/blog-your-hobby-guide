# Chapter 2 — Anatomy of a Static Blog

A static blog is a folder of files. That is the whole architecture.
Understanding the folder is understanding the blog. This chapter is the
map; the `site/` directory in this repo is a miniature of the map you
can open in a browser right now.

## 2.1 The moving parts

A minimal static blog has five kinds of parts:

```
my-blog/
├── content/          # Markdown sources (what YOU write)
│   └── posts/
│       └── 2026-11-01-first-post.md
├── site/             # Generated HTML (what READERS see)
│   ├── index.html
│   ├── styles.css
│   ├── about.html
│   └── posts/
│       └── 2026-11-01-first-post.html
├── tools/            # The little scripts that turn 1 into 2
│   ├── build.py
│   └── check.py
└── README.md
```

Two folders, one conversion step. When someone visits your page, GitHub
Pages serves `site/` — nothing more exotic than that. No database, no
server-side code, no plugins to update.

## 2.2 What each piece is actually for

- **The source folder (`content/`).** Markdown files you edit. Their
  filenames become URLs, so dates keep posts sorted: `YYYY-MM-DD-slug.md`.
  Each file starts with a tiny header (title, date) in plain lines —
  see Chapter 3.
- **The output folder (`site/`).** Only what a browser needs: HTML,
  one stylesheet, and any images. This folder is a *build artifact* —
  regenerating it should always be safe.
- **The generator (`tools/build.py`).** A few dozen lines that read the
  Markdown, render it to HTML, wrap it in a template, and drop it in
  `site/posts/`. The one in this repo uses only the Python standard
  library, so it runs anywhere Python does, with nothing to install.
- **The checker (`tools/check.py`).** Follows every internal link in the
  finished site and fails loudly if a file is missing. This is how you
  "test" a static site.
- **The stylesheet (`styles.css`).** One file. Small. No framework,
  because hobby blogs do not need one, and a framework you can mentally
  audit is a cost not a feature.

## 2.3 How GitHub Pages fits in

GitHub Pages is a free static file host attached to any repository.
There are two modes:

- **User site:** repo named `yourname.github.io`, live at the root URL.
- **Project site:** any repo named anything, live at
  `yourname.github.io/repo-name/`.

Both are created by pushing a repository to GitHub (account required —
that is the one account in this whole manual) and turning on Pages in
the repo's *Settings → Pages* panel, choosing the branch and folder.
The first deploy takes a minute; afterwards every push redeploys.

**Local-first habit:** never test on the live URL. Preview locally:

```
python3 tools/build.py
python3 -m http.server 8000 --directory site
```

Then open `http://localhost:8000/`. What you see is exactly what ships.

## 2.4 Files that pay rent

These small, boring files carry disproportionate weight:

- `index.html` — the front door; a list of posts newest first.
- `about.html` — a friendly two-paragraph "why this blog exists." It is
  the most-visited page on most hobby blogs.
- `styles.css` — consistent look without rebuilding anything.
- `favicon.ico` — a tiny image; browsers request it automatically and a
  404 in the console looks unpolished.
- `robots.txt` — two lines that politely tell search engines what you
  do and do not want indexed.

## 2.5 Why static wins for a hobby

- **Durability.** HTML files from 1996 still render. There is no
  dependency graph to rot.
- **Portability.** Your backup *is* your folder. Copy it to a USB stick
  and you are fully backed up.
- **Cost.** Static hosting is free at hobby scale (Chapter 8).
- **Speed.** Nothing to install, nothing to break, deploys in seconds.
- **Privacy.** No comments section collecting emails, no analytics
  pinging home. Your readers' data stays where it belongs: nowhere.

The tradeoff is interactive features — no comments, no search-as-a-service.
Chapter 7 shows a mailto: contact line is the hobby-scale answer.

## 2.6 Your turn

Open `site/index.html` in this repo in a browser. Everything you see —
the front page, the posts, the stylesheet — was produced from `content/`
by `tools/build.py`. Change a word in `content/posts/`, rebuild, refresh.
You now understand the entire system.
