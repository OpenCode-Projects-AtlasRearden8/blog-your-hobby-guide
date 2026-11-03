# Chapter 8 — Hiding Costs: What Must Cost Money and What Never Should

The promise of this manual is a zero-dollar blog. Here is the honest
version: what is genuinely free forever, what is free *now* and might
tempt you later, and the few places hobby bloggers get talked into
paying for things they do not need.

## 8.1 The free-forever core

| Thing                     | Cost | Notes                                        |
|---------------------------|------|----------------------------------------------|
| GitHub account / Pages    | $0   | Static hosting for public repos, free.       |
| Git                       | $0   | The version control doing all the history.   |
| Python 3                  | $0   | Runs the builder and checker.                |
| Markdown files            | $0   | Any editor; nothing to buy or license.       |
| Bandwidth at hobby scale  | $0   | GitHub's limit: about 100 GB/month.          |
| Images (your phone)       | $0   | Chapter 6.                                   |
| HTTP instead of HTTPS     | —    | GitHub Pages gives you HTTPS free.           |

For nearly every hobby blog ever started, this list is *all* of the
stack. The monthly bill is genuinely $0.00.

## 8.2 "Free now" things that quietly want money

Watch your step on these; none is bad, all have a billing cliff:

- **Cloud AI assistants.** Free tiers exist; power use pushes toward
  subscriptions. Chapter 5: local models or sparing use keep it $0.
- **Comment systems / analytics SaaS.** Heavy free tiers, then $9–19
  monthly — and your readers' data flows to a third party. The hobby-
  scale alternative: a `mailto:` contact line and no analytics.
- **Website builders.** Marketing says "free"; the free tier shows
  *their* ads, hides *your* pages behind a subdomain, and blocks
  exporting. Static files are the keystone escape hatch.
- **Stock photos.** Plenty of free, properly licensed sources exist
  (Chapter 6). Subscribe only if a bankroller forces it.

## 8.3 The two places spending real money is defensible

1. **A custom domain, ~$12/year.** `yourblog.com` instead of
   `you.github.io`. Worth it if: you might print it, use it in email,
   or care how the blog looks on a résumé. GitHub Pages supports it
   free — you pay only the domain itself. Register at any honest
   registrar; avoid "free first year, then $40" offers.
2. **A one-time equipment upgrade** (better camera, better light).That
   improves the hobby itself, which is the point of everything here.

Everything else a paid service could sell you, SQLite-tight simplicity
already covers.

## 8.4 Costs people forget — the hidden balance sheet

Not dollars, but the same accounting:

- **Attention.** Every widget and feed is a distraction tax. A page of
  HTML has none.
- **Maintenance.** Fewer moving parts = fewer updates. Static wins.
- **Migration risk.** Files in a folder move anywhere, forever. Data
  behind a free-tier service can be hostage later.
- **Trust.** No ads, no trackers = readers who stay. Trust is the only
  currency a hobby blog deals in.

## 8.5 If it must scale someday

Fine — the hobby solution survives industrialization: the Markdown
posts remain; the static site remains; you point any better host at
the same `site/` folder. Nothing in this manual locks you in. That is
the quiet superpower of building with files from day one.

## 8.6 A final, unhurried word

Free is not the same as cheap. This stack costs nothing and asks for
nothing but one post a week. If you ever feel pressure to "monetize,"
reread Chapter 1 — the blog is the hobby's story, and its price tag is
part of the charm.
