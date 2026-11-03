#!/usr/bin/env python3
"""Check site/ for the mistakes that embarrass hobby bloggers.

Runs these checks, all local, all fast:
  1. Every internal href/src in site/*.html resolves to a real file.
  2. site/index.html links every post; no draft (_*) files leaked out.
  3. Each post page has a title, a date, and no empty paragraphs.
  4. External links all use https.

Usage:
    python3 tools/check.py          after python3 tools/build.py
Exits nonzero on any failure.
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"

problems = []


def fail(msg):
    problems.append(msg)


def link_targets(html_text):
    p = HTMLParser()
    attrs = []
    p.handle_starttag = lambda tag, at: attrs.extend(
        (tag, v) for k, v in at if k in ("href", "src") and v
    )
    p.handle_startendtag = p.handle_starttag
    p.feed(html_text)
    return attrs


def check_links():
    pages = sorted(SITE.rglob("*.html"))
    if not pages:
        fail("no built pages found in site/")
        return
    for page in pages:
        text = page.read_text(encoding="utf-8")
        for tag, target in link_targets(text):
            parsed = urlparse(target)
            if parsed.scheme in ("http", "https"):
                if parsed.scheme == "http":
                    fail('%s: external link uses http (want https): %s'
                         % (page.relative_to(SITE), target))
                continue
            if parsed.scheme or target.startswith(("#", "mailto:", "data:")):
                continue
            clean = unquote(target.split("#")[0]).rstrip("/")
            resolved = (page.parent / clean).resolve()
            if resolved.is_dir():
                resolved = resolved / "index.html"
            if not resolved.exists():
                fail('%s: broken link "%s" (from %s)'
                     % (page.relative_to(SITE), target, page.name))


def check_index_and_drafts():
    index = SITE / "index.html"
    if not index.exists():
        fail("site/index.html missing — run tools/build.py")
        return
    text = index.read_text(encoding="utf-8")
    posts_dir = SITE / "posts"
    post_pages = sorted(p for p in posts_dir.glob("*.html")
                        if p.name != "index.html")
    for post in post_pages:
        if 'href="posts/%s"' % post.name not in text:
            fail("index.html does not link post: %s" % post.name)
    for leaked in SITE.rglob("_*"):
        fail("draft file leaked into site/: %s" % leaked.relative_to(SITE))
    if not (SITE / "styles.css").exists():
        fail("site/styles.css missing")


def check_post_quality():
    for post in sorted((SITE / "posts").glob("*.html")):
        if post.name == "index.html":
            continue
        text = post.read_text(encoding="utf-8")
        if "<title>" not in text:
            fail("%s: missing <title>" % post.name)
        if 'class="meta"' not in text:
            fail("%s: no date line (meta paragraph)" % post.name)
        if re.search(r"<p>\s*</p>", text):
            fail("%s: contains an empty paragraph" % post.name)
        for img in re.findall(r'<img src="[^"]*" alt=""', text):
            fail("%s: image without alt text" % post.name)


def main(argv):
    if not SITE.is_dir():
        print("site/ does not exist yet. Run: python3 tools/build.py")
        return 1
    check_links()
    check_index_and_drafts()
    check_post_quality()

    if problems:
        print("FAILED — %d problem(s):" % len(problems))
        for p in problems:
            print("  -", p)
        return 1
    print("OK — links, index, drafts, post quality: all good.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
