# Appendix — A Plain-English Glossary

Jargon, decoded like a friend would.

**Repository ("repo").** A folder that git keeps versions of. Your blog
is one.

**Git.** Software that remembers every saved change to your folder.
Undo, forever, at any size.

**GitHub.** A website that hosts git repositories (the one account this
manual requires). Not the same thing as git.

**GitHub Pages.** GitHub's free static-file host. It shows a repo's
HTML files to the world.

**Static site.** A website that is just files — no database, no server
code running per visitor. Fast, durable, free to host.

**Markdown.** Plain text with simple punctuation (like `*this*` for
*italic*) that a small program converts to HTML.

**HTML.** The file format web browsers display. `<h1>` means "big
heading," `<a href=...>` means "link," and so on.

**CSS.** The file(s) that say how HTML should look: colors, fonts,
spacing. Ours is one page: `styles.css`.

**Build.** The step that turns sources (Markdown) into outputs (HTML).
Ours: `python3 tools/build.py`.

**URL / link.** The address of a page, e.g. `https://you.github.io/posts/…`.

**Local.** On *your* machine rather than on the internet. Local-first
means test on your machine, then publish deliberately.

**Slug.** The short, lowercase, hyphenated name in a URL, like
`my-first-post` in `/posts/2026-11-01-my-first-post.html`.

**Draft.** A post that exists but is not published. Here: filenames
starting with `_` are skipped by the builder.

**Alt text.** A written description of an image, for screen readers
and broken connections.

**LLM (Large Language Model).** The kind of AI behind chat assistants
— good at rewriting and outlining, unreliable about facts.

**Ollama.** Free software that runs small LLMs on your own machine.
No account, no data sent anywhere.

**MCP (Model Context Protocol).** An open way for AI tools to connect
to data and actions. Not needed for this blog — noted here because
guides about it live alongside this manual.

**Commit.** A saved, labeled snapshot in git; the habit's heartbeat.
Pushing means sending commits to GitHub (publishing, or just backup).

**404.** "Page not found." `tools/check.py` hunts these before readers do.

**MIT License.** A short permission note in this repo's `LICENSE`
file: reuse this freely; no warranty.
