# Chapter 3 — The Markdown Workflow

Markdown is plain text with light punctuation that a converter turns
into HTML. It was designed to be readable *as text*. This chapter gives
you the workflow: the format, the filenames, the loop.

## 3.1 The 20% of Markdown you need

```markdown
# A top heading (usually just the post title)

A paragraph. Blank lines separate paragraphs. **Bold** and *italic*
live in asterisks. A [link](https://example.org) brackets-then-parens.

## A section heading

- A bullet list item
- Another one

1. A numbered list item

> A blockquote, for quoting a book or game text

`inline code` and:

    indented code blocks

an HTML comment <!-- like this --> is invisible in output.
```

That is essentially it. You can write years of posts without learning
more. Markdown's design goal was that the source looks fine as-is — so
even *without* conversion, your files are readable.

## 3.2 The headers at the top of each post

Keep it boring. First lines of the file, one key per line:

```markdown
Title: My First Post
Date: 2026-11-01
```

`Title` becomes the page heading and the entry in the index; `Date`
becomes the sort key and the visible date. Optional extras you can add
later, but the builder in this repo only needs those two.

## 3.3 Filenames are your URLs

Pattern, locked in from day one:

```
YYYY-MM-DD-short-slug.md    →  /posts/2026-11-02-short-slug.html
```

- Lowercase, hyphens for spaces, no punctuation.
- The date prefix sorts posts chronologically in any folder listing —
  free archive organization, forever.
- Never rename a published file: the URL is the address other people
  may have linked to.

## 3.4 The daily loop

```
1. cp content/posts/_template.md content/posts/2026-11-03-new-idea.md
2. Write in your editor of choice.
3. python3 tools/build.py
4. python3 -m http.server 8000 --directory site   # preview
5. Read your own post as a stranger would.
6. python3 tools/check.py                          # links, index, polish
7. git add -A && git commit -m "post: new idea"
```

Steps 3–6 take under a minute and catch 95% of blog embarrassment:
broken links, typos in headers, a post missing from the index.

## 3.5 Drafts: the underscore trick

Any file starting with `_` is skipped by the builder. So
`content/posts/_drafts/my-fuzzy-idea.md` exists locally, is fully
editable, and never appears on the site. When it is ready, drop the
underscore, rename with a date, and rebuild.

## 3.6 Editing tools

Any text editor works: Notepad, TextEdit (in plain-text mode), VS Code,
or `nano` from the terminal. If you later want a preview-as-you-type,
editors have Markdown modes — but do not let tool shopping postpone
post one. `nano` is sufficient for a hobby blog; this manual's own
Markdown was drafted in plain editors.

## 3.7 A few professional touches, for free

- **Short paragraphs.** One idea per paragraph, 2–4 sentences.
- **One idea per post.** Splitting a big post into two is the cheapest
  way to double your archive.
- **Front-load the payoff.** First paragraph should state what the
  reader gets and why you are the one delivering it.
- **End with a next step** — a question to think about, a link to the
  previous post, or "why not try it this weekend?"

## 3.8 When Markdown is not enough

Occasionally a post wants a table, an image with a caption, or a video
embed. Markdown lets you drop raw HTML inline when needed. Use it
sparingly: the virtue of the whole system is that it stays as readable
as a text file.
