# Manual: Start a Hobby Blog on GitHub Pages for Free

A complete, tested, local-first manual for starting a hobby blog with
Markdown, a tiny build script, and GitHub Pages — plus a working
example blog in this very repo. No accounts beyond GitHub, no secrets,
no personal data, no monthly bill.

Written by **Asdale Dynamics, LLC** in the plain-English, friend-to-friend
style of *The Massive AI Manual* by Dylan Asdale. Licensed MIT — see
[LICENSE](LICENSE).

## What is in here

| Folder            | What it is                                             |
|-------------------|--------------------------------------------------------|
| `docs/`           | The manual: 8 chapters + glossary. Start at [docs/index.md](docs/index.md). |
| `site/`           | A small static blog that actually works. Open `site/index.html` in a browser. |
| `content/`        | The Markdown sources the site is built from (the format you will write in). |
| `tools/`          | A dependency-free builder, checker, and tests. Python 3 standard library only. |

## Quick start (all commands are tested)

```bash
sh tools/verify.sh                                  # run tests, build, checks
python3 tools/build.py                              # rebuild the site
python3 -m http.server 8000 --directory site        # preview locally
# open http://localhost:8000/
python3 tools/check.py                              # check links & quality
```

Then follow the manual: chapter by chapter, until you publish your own
first post. Chapter 7 explains the one point where a GitHub account and
a `git push` enter the picture — publishing stays a deliberate act that
you perform.

## Chapters

1. Picking a niche that survives contact with reality
2. Anatomy of a static blog
3. The Markdown workflow
4. Writing habits that stick
5. Light AI drafting help — with disclosure
6. Photos without pain or cost
7. A weekly publishing rhythm you can keep
8. Hiding costs: what must cost money and what never should

Plus a plain-English glossary appendix.

## The example blog is itself the demo

The site in `site/` is built from `content/` by `tools/build.py`. Edit a
Markdown file in `content/posts/`, rebuild, and refresh — that is the
entire writing loop, visible in one repository. It works completely
offline; hosting is only mentioned at the end.

## Contributing and reuse

MIT licensed. Fork it, rename everything, repurpose it for your niche.
Adaptations welcome: new chapters, a nicer builder, accessibility
improvements. Keep it dependency-free and local-first, please.

## Credits & license

Created by **Asdale Dynamics, LLC**. Code and text are released under
the MIT License (see `LICENSE`). Copyright (c) 2026 Asdale Dynamics, LLC.
