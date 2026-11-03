#!/usr/bin/env python3
"""Build the static blog from content/ into site/.

Local-first and dependency-free: Python 3 standard library only.

Usage:
    python3 tools/build.py            rebuild the whole site
    python3 tools/build.py --quiet    same, but less chatter
"""

import html
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
POSTS_SRC = CONTENT / "posts"
PAGES_SRC = CONTENT / "pages"
IMG_SRC = CONTENT / "img"
SITE = ROOT / "site"
POSTS_OUT = SITE / "posts"
IMG_OUT = SITE / "img"

SITE_NAME = "Hobby Blog Example"
FOOTER = "Made by hand. A GitHub Pages example blog for the manual in docs/."


# ---------------------------------------------------------------------------
# Tiny Markdown-ish converter (headings, lists, quotes, emphasis, links,
# images, code, paragraphs). Deliberately small and readable.


def inline(text):
    """Inline Markdown: code, links, images, bold, italic."""
    text = re.sub(r"`([^`]+)`",
                  lambda m: "<code>%s</code>" % html.escape(m.group(1), quote=False),
                  text)
    text = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)",
                  lambda m: '<img src="%s" alt="%s">' % (
                      html.escape(m.group(2), quote=False), html.escape(m.group(1), quote=False)),
                  text)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
                  lambda m: '<a href="%s">%s</a>' % (
                      html.escape(m.group(2), quote=False), m.group(1)),
                  text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    return text


def md_to_html(text):
    """Convert a small, common subset of Markdown to HTML."""
    out = []
    in_code = False
    code_lines = []
    list_open = None  # "ul" or "ol"
    in_quote = False
    para = []

    def flush_para():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    def flush_list():
        nonlocal list_open
        if list_open:
            out.append("</%s>" % list_open)
            list_open = None

    def flush_quote():
        nonlocal in_quote
        if in_quote:
            out.append("</blockquote>")
            in_quote = False

    for raw in text.splitlines():
        line = raw.rstrip()

        if line.strip().startswith("```"):          # fenced code
            flush_para(); flush_list(); flush_quote()
            if in_code:
                body = html.escape("\n".join(code_lines), quote=False)
                out.append("<pre><code>" + body + "</code></pre>")
                code_lines = []
            in_code = not in_code
            continue
        if in_code:
            code_lines.append(raw)
            continue

        m = re.match(r"^(#{1,4})\s+(.*)$", line)    # headings: # -> <h2>
        if m:
            flush_para(); flush_list(); flush_quote()
            level = len(m.group(1)) + 1
            out.append("<h%d>%s</h%d>" % (level, inline(m.group(2)), level))
            continue

        if line.startswith("> "):                   # blockquote
            flush_para(); flush_list()
            if not in_quote:
                out.append("<blockquote>")
                in_quote = True
            out.append("<p>%s</p>" % inline(line[2:]))
            continue
        flush_quote()

        m_ul = re.match(r"^[-*]\s+(.*)$", line)     # lists
        m_ol = re.match(r"^\d+\.\s+(.*)$", line)
        kind = "ul" if m_ul else ("ol" if m_ol else None)
        if kind:
            flush_para()
            if list_open != kind:
                flush_list()
                out.append("<%s>" % kind)
                list_open = kind
            out.append("<li>%s</li>" % inline((m_ul or m_ol).group(1)))
            continue
        flush_list()

        if not line.strip():                        # blank line
            flush_para()
            continue

        para.append(line.strip())

    if in_code and code_lines:
        body = html.escape("\n".join(code_lines), quote=False)
        out.append("<pre><code>" + body + "</code></pre>")
    flush_para(); flush_list(); flush_quote()
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Front matter + page assembly


def split_front_matter(text):
    """Split 'Key: value' header lines from the Markdown body."""
    meta = {}
    lines = text.splitlines()
    i = 0
    while i < len(lines) and ":" in lines[i]:
        key, _, value = lines[i].partition(":")
        if not re.fullmatch(r"[A-Za-z][A-Za-z ]*", key):
            break
        meta[key.strip().lower()] = value.strip()
        i += 1
    while i < len(lines) and not lines[i].strip():
        i += 1
    return meta, "\n".join(lines[i:])


def style_link_for(section):
    prefix = "../" if section else ""
    return '<link rel="stylesheet" href="%sstyles.css">' % prefix


def nav_for(section):
    prefix = "../" if section else ""
    posts_link = './' if section else "posts/"
    return (
        '<nav><a href="%sindex.html">Home</a> · '
        '<a href="%sabout.html">About</a> · '
        '<a href="%s">Posts</a></nav>' % (prefix, prefix, posts_link)
    )


def wrap_page(title, body, section=""):
    """Wrap rendered Markdown in the site template."""
    return (
        "<!DOCTYPE html>\n"
        '<html lang="en">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        "<title>%s — %s</title>\n"
        "%s\n</head>\n<body>\n%s\n<main>\n%s\n</main>\n"
        "<footer>%s</footer>\n</body>\n</html>\n"
        % (
            html.escape(title, quote=False), html.escape(SITE_NAME, quote=False),
            style_link_for(section), nav_for(section), body,
            html.escape(FOOTER, quote=False),
        )
    )


def render_markdown_page(md_path, section=""):
    text = md_path.read_text(encoding="utf-8")
    meta, body_md = split_front_matter(text)
    title = meta.get("title") or md_path.stem.replace("-", " ").title()
    body = md_to_html(body_md)
    if section == "posts/":
        date = meta.get("date", "")
        if date:
            body = '<p class="meta">%s</p>\n%s' % (html.escape(date, quote=False), body)
    return title, wrap_page(title, body, section)


def collect_posts():
    """Read every dated post, newest-first list."""
    posts = []
    if POSTS_SRC.is_dir():
        for md_path in sorted(POSTS_SRC.glob("*.md")):
            if md_path.name.startswith("_"):
                continue  # underscores are drafts/templates, never built
            text = md_path.read_text(encoding="utf-8")
            meta, body_md = split_front_matter(text)
            posts.append({
                "slug": md_path.stem,
                "title": meta.get("title") or md_path.stem.replace("-", " ").title(),
                "date": meta.get("date", ""),
                "body": body_md,
            })
    return sorted(posts, key=lambda p: p["date"], reverse=True)


# ---------------------------------------------------------------------------
# Build steps


def build_posts(posts):
    POSTS_OUT.mkdir(parents=True, exist_ok=True)
    written = []
    for p in posts:
        body_html = md_to_html(p["body"])
        page = wrap_page(
            p["title"],
            '<p class="meta">%s</p>\n%s' % (html.escape(p["date"], quote=False), body_html),
            section="posts/",
        )
        out = POSTS_OUT / (p["slug"] + ".html")
        out.write_text(page, encoding="utf-8")
        written.append(out)
    return written


def build_index(posts):
    items = [
        '<li><a href="posts/%s.html">%s</a> <span class="meta">%s</span></li>'
        % (html.escape(p["slug"], quote=False), html.escape(p["title"], quote=False),
           html.escape(p["date"], quote=False))
        for p in posts
    ]
    body = (
        "<h1>%s</h1>\n<p>A tiny blog about a hobby, built on GitHub Pages. "
        "Read the manual in <code>docs/</code> to build one like it.</p>\n"
        "<h2>Posts</h2>\n<ul>\n%s\n</ul>\n"
        % (html.escape(SITE_NAME, quote=False), "\n".join(items))
    )
    (SITE / "index.html").write_text(wrap_page(SITE_NAME, body), encoding="utf-8")


def build_posts_archive(posts):
    items = [
        '<li><a href="%s.html">%s</a> <span class="meta">%s</span></li>'
        % (html.escape(p["slug"], quote=False), html.escape(p["title"], quote=False),
           html.escape(p["date"], quote=False))
        for p in posts
    ]
    body = ("<h1>Every post</h1>\n<ul>\n%s\n</ul>\n" % "\n".join(items))
    out = POSTS_OUT / "index.html"
    out.write_text(wrap_page("Every post", body, section="posts/"), encoding="utf-8")


def build_pages():
    written = []
    if PAGES_SRC.is_dir():
        for md_path in sorted(PAGES_SRC.glob("*.md")):
            title, page = render_markdown_page(md_path)
            out = SITE / (md_path.stem + ".html")
            out.write_text(page, encoding="utf-8")
            written.append(out)
    return written


def build_images():
    if IMG_OUT.exists():
        shutil.rmtree(IMG_OUT)
    if IMG_SRC.is_dir():
        shutil.copytree(IMG_SRC, IMG_OUT)


def main(argv):
    quiet = "--quiet" in argv
    SITE.mkdir(exist_ok=True)

    posts = collect_posts()
    written = build_posts(posts)
    written += build_pages()
    build_index(posts)
    build_posts_archive(posts)
    build_images()

    for src in (SITE / "styles.css", SITE / "robots.txt", SITE / "favicon.ico"):
        if not src.exists():
            print("NOTE: missing static file: %s" % src.relative_to(ROOT))

    if not quiet:
        print("Built %d posts, %s." % (
            len(written),
            ", ".join(str(p.relative_to(SITE)) for p in written[-2:]) or "no pages",
        ))
        print("Site is ready in site/ — preview with:")
        print("    python3 -m http.server 8000 --directory site")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
