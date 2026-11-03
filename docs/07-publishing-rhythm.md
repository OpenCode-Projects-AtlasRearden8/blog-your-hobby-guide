# Chapter 7 — A Weekly Publishing Rhythm You Can Keep

Chapter 4 gave you the habit; this chapter gives the calendar around
it. One post per week, forever — here's how that actually sounds in a
life that already has a job, a family, laundry, and a hobby the blog is
*about*.

## 7.1 Why weekly is the ceiling, not the floor

- It is sustainable. Daily requires content, weekly requires a pulse.
- It trains readers' expectations: same day, same place.
- Weekly archives grow to 50 posts a year — an enormous, honest body of
  work. Most hobby blogs stop at 4 or 5 posts, ever.

If weekly ever feels heavy, drop to fortnightly. Never hourly, never
"when inspired."

## 7.2 The five-shapes-any-post menu

Rotate through these five; rotation kills "what do I write" dead:

1. **Log.** "This week I did X, here's what I learned." Capture-file
   fuel. Short.
2. **How-to.** "How I do Y (with my constraints)." The workhorse; ever
   useful to strangers a year from now.
3. **Failure report.** "I tried Z; it went badly." Unexpectedly,
   these are the most-loved posts on any blog.
4. **Question.** "Why does M do that? I don't know yet." Nest post:
   the answer. Two birds.
5. **Link + why.** "Found a great page; here's my take." Ten minutes,
   and generous — link out freely.

Type 1 and 4 can be written on an empty evening; never let the weekly
rule punch you into type-2 ambitiousness every single time.

## 7.3 The batching day

Once a week — same slot, e.g., Sunday mornings, coffee included — run
one 45-minute session that contains the whole machine:

| Minutes | Task                                                  |
|---------|-------------------------------------------------------|
| 5       | Skim `ideas.md`, pick next week's post (write stub).  |
| 20      | Draft or edit one post (Chapter 4's 10+20+10 shape).   |
| 10      | Process any photos waiting (Chapter 6).               |
| 10      | `build.py`, `check.py`, preview, commit, (push).      |

Forty-five minutes, once. Everything else is just filing notes during
the week, ten seconds at a time.

## 7.4 Backup rhythm: the double-3-2-1, hobby edition

`git` already gives you history for free. Add two micro-habits:

- Every publish: `git add -A && git commit -m "post: <title>"`.
- Monthly: copy the whole folder to a USB stick or a second machine.
  `cp -r blog-folder /backup/2026-11-01/` — done. Your site is a
  folder; backing it up is literally one command.

## 7.5 The archive feeds the calendar

Every 4–6 weeks, scroll your own posts. Most likely things happen:

- Two posts secretly form a series → announce it, add "Part 1/2" links.
- You wrote "I should test that" three times → it wants to be a post.
- Year one ends → write a "what this blog is now" post. Readers love
  these; so does your future self.

## 7.6 Publishing to GitHub Pages, the once-per-moment part

After the local rhythm is solid (give yourself 4 weeks offline-first),
attach it to the world:

```bash
git remote add origin https://github.com/you/you.github.io.git
git push -u origin main
```

Then in the repo: *Settings → Pages → Deploy from branch: main, /
(root)*. Every `git push` from now on republishes, usually inside a
minute. The rhythm does not change — commit becomes commit + push.

This repo never pushes anywhere on your behalf. Publishing is a button
you press, in a terminal you type into. That is as it should be.
