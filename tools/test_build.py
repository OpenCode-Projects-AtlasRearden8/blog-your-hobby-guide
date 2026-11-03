#!/usr/bin/env python3
"""Smoke tests for the blog builder — standard library unittest, no installs.

    python3 tools/test_build.py
"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build


class TestMarkdown(unittest.TestCase):
    def test_heading_levels(self):
        html_text = build.md_to_html("# Title\n\n## Section")
        self.assertIn("<h2>Title</h2>", html_text)
        self.assertIn("<h3>Section</h3>", html_text)

    def test_paragraphs_split_on_blank_lines(self):
        html_text = build.md_to_html("one\n\ntwo")
        self.assertEqual(html_text.count("<p>"), 2)

    def test_bold_italic_code(self):
        html_text = build.md_to_html("**b** *i* `c`")
        self.assertIn("<strong>b</strong>", html_text)
        self.assertIn("<em>i</em>", html_text)
        self.assertIn("<code>c</code>", html_text)

    def test_link_escapes_href(self):
        html_text = build.md_to_html('[x](http://e.com/a?b=1&c=2)')
        self.assertIn('href="http://e.com/a?b=1&amp;c=2"', html_text)
        self.assertIn("<a href=", html_text)

    def test_lists(self):
        html_text = build.md_to_html("- one\n- two\n\n1. a\n2. b")
        self.assertIn("<ul>", html_text)
        self.assertIn("<ol>", html_text)
        self.assertEqual(html_text.count("<li>"), 4)

    def test_fenced_code_escapes_html(self):
        html_text = build.md_to_html("```\n<div>&hi</div>\n```")
        self.assertIn("&lt;div&gt;&amp;hi&lt;/div&gt;", html_text)

    def test_blockquote(self):
        html_text = build.md_to_html("> quoted")
        self.assertIn("<blockquote>", html_text)
        self.assertIn("<p>quoted</p>", html_text)

    def test_image_with_alt(self):
        html_text = build.md_to_html("![cool cat](../img/cat.jpg)")
        self.assertIn('<img src="../img/cat.jpg" alt="cool cat">', html_text)

    def test_inline_html_in_text_is_escaped_by_code_only(self):
        html_text = build.md_to_html("use `1 < 2` safely")
        self.assertIn("<code>1 &lt; 2</code>", html_text)


class TestFrontMatter(unittest.TestCase):
    def test_split_meta_and_body(self):
        meta, body = build.split_front_matter("Title: Hello\nDate: 2026-11-01\n\nBody here")
        self.assertEqual(meta["title"], "Hello")
        self.assertEqual(meta["date"], "2026-11-01")
        self.assertEqual(body.strip(), "Body here")

    def test_no_meta(self):
        meta, body = build.split_front_matter("Just words")
        self.assertEqual(meta, {})
        self.assertEqual(body.strip(), "Just words")

    def test_colon_in_body_stays(self):
        meta, body = build.split_front_matter("Note: keep\n\nA: B in body")
        self.assertEqual(meta["note"], "keep")
        self.assertIn("A: B in body", body)


class TestBuildPipeline(unittest.TestCase):
    def _write(self, path, text):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def test_full_build_in_temp_dir(self):
        with tempfile.TemporaryDirectory() as tmp:
            old = (build.ROOT, build.SITE, build.POSTS_SRC, build.PAGES_SRC,
                   build.POSTS_OUT, build.IMG_SRC, build.IMG_OUT, build.CONTENT)
            try:
                root = Path(tmp)
                build.ROOT = root
                build.SITE = root / "site"
                build.CONTENT = root / "content"
                build.POSTS_SRC = root / "content" / "posts"
                build.PAGES_SRC = root / "content" / "pages"
                build.IMG_SRC = root / "content" / "img"
                build.POSTS_OUT = build.SITE / "posts"
                build.IMG_OUT = build.SITE / "img"

                self._write(build.POSTS_SRC / "2026-11-01-hello.md",
                            "Title: Hello\nDate: 2026-11-01\n\n# Hi\n\nA **bold** post.\n")
                self._write(build.POSTS_SRC / "_draft.md",
                            "Title: Secret\nDate: 2026-11-02\n\nshould not appear\n")
                self._write(build.POSTS_SRC / "2026-11-03-second.md",
                            "Title: Second\nDate: 2026-11-03\n\nOlder body text.\n")
                self._write(build.PAGES_SRC / "about.md", "Title: About\n\nWho I am.\n")
                self._write(build.IMG_SRC / "pic.txt", "fake img")
                self._write(build.SITE / "styles.css", "body{}\n")

                posts = build.collect_posts()
                # drafts (leading underscore) are excluded; newest first
                self.assertEqual([p["slug"] for p in posts],
                                 ["2026-11-03-second", "2026-11-01-hello"])

                build.SITE.mkdir(exist_ok=True)
                build.build_posts(posts)
                build.build_pages()
                build.build_index(posts)
                build.build_posts_archive(posts)
                build.build_images()

                index = (build.SITE / "index.html").read_text(encoding="utf-8")
                self.assertIn('href="posts/2026-11-03-second.html"', index)
                self.assertIn("2026-11-01-hello.html", index)  # both listed
                self.assertNotIn("Secret", index)              # draft hidden

                post = (build.POSTS_OUT / "2026-11-01-hello.html").read_text(encoding="utf-8")
                self.assertIn("<title>Hello", post)
                self.assertIn("<strong>bold</strong>", post)
                self.assertIn("2026-11-01", post)

                self.assertTrue((build.SITE / "about.html").exists())
                self.assertTrue((build.POSTS_OUT / "index.html").exists())
                self.assertTrue((build.IMG_OUT / "pic.txt").exists())
            finally:
                (build.ROOT, build.SITE, build.POSTS_SRC, build.PAGES_SRC,
                 build.POSTS_OUT, build.IMG_SRC, build.IMG_OUT, build.CONTENT) = old


if __name__ == "__main__":
    unittest.main(verbosity=2)
