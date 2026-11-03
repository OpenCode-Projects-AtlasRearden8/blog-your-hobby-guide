# Chapter 5 — Light AI Drafting Help, With Disclosure

AI can help a hobby blogger the way a helpful colleague can: it sits
with you, it speeds up the blank page, it suggests a smoother sentence.
But there is one rule above all others in this chapter: **tell your
readers.** Trust is the entire business model of a hobby blog — and the
loss is invisible until it is gone.

## 5.1 A working disclosure line

Put this before or after any post AI helped with — or, simplest, on
your about page once:

> Some posts on this blog are drafted with AI assistance and then
> reviewed, edited, and verified by me before publishing. Anything
> factual that is wrong is my error, and I fix things when spotted.

That is honest, plain-English, and calm. It costs one paragraph and
buys the peace of mind to actually use the tools.

## 5.2 Where AI helps at hobby scale

- **Beating the blank page.** "Here are notes for a post, turn them
  into a rough draft I will edit" is the single most useful prompt.
  The outline from `ideas.md` becomes 80% of a post in a minute.
- **Titles and structure.** Ask for five title options and a suggested
  paragraph order.
- **Plain-English rewrites.** Of a clunky paragraph you wrote.
- **Summarizing your own archive.** "Here are my last five posts,
  list recurring themes" helps you spot a series.

## 5.3 Where AI must not be trusted

- **Facts about your niche.** Game mechanics, plant hardiness, chess
  openings, model numbers, dates. AI hallucinates fluently and
  confidently. Verify against a primary source — the manual, the seed
  packet, the database — or leave it out.
- **Your voice.** Its default tone is a beige beige-ing. You write
  about *your* hobby; keep your opinions, your typos' character, your
  weird asides. If a paragraph does not sound like you, rewrite it.
- **Your experiences.** Never outsource the actual content of "what
  happened when I tried it." That is the whole value.

The rule of thumb: **AI may sit in the passenger seat but you keep
hands on the wheel. Your one-of-a-kind material is the trip itself.**

## 5.4 A local-first, no-account way to try it

If you want to experiment without sending text to a cloud service, run
a small model on your own machine:

```
# Example: Ollama, free and local; download the model once
ollama pull llama3.2:3b
ollama run llama3.2:3b "Rewrite these blog notes as a friendly
first-draft: [paste notes]"
```

Tradeoffs, honestly: local models are slower and less talented than the
cloud ones, and want a few GB of RAM. The upside: no account, no
subscription, your notes never leave the machine. Start there; if the
quality is not enough, a cloud assistant with a clear disclosure line
is the pragmatic next step.

## 5.5 The one-minute self-audit

Before publishing an AI-assisted post, ask:

- [ ] Every factual claim either verified by me or removed.
- [ ] It sounds like me, or I paid it that compliment already.
- [ ] Something in it only I could have written.
- [ ] The disclosure line covers it.
- [ ] I would be comfortable if a reader asked, "parts written by AI?"
      and I answered with this post.

Five checks, one minute, complete trust.
