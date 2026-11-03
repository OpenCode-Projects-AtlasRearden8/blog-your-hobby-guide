# Chapter 6 — Photos Without Pain or Cost

Photographs make hobby blogs feel alive, and they come with three real
questions: where do you get them, how do you make them load fast, and
how do you stay out of legal trouble. All three have calm, free answers.

## 6.1 The three sources, in order of preference

1. **Your own photos.** Best: real, unique, and yours. A phone camera
   is entirely sufficient; light in a window beats any editing.
2. **License-safe free sources.** Wikimedia Commons, Unsplash, Pexels,
   Pixabay — free to use, but *check the license text on the actual
   photo's page* and credit as the license requires ("Photo: Jane Doe /
   Wikimedia Commons" under the image is plenty).
3. **Sparingly, decorative CSS.** A color band, a border, an emoji in
   the post metadata: sometimes the answer is no photograph at all.

Never take images from Google Images search. That is how hobby blogs
accidentally commit copyright infringement.

## 6.2 Make them small without a service

Photos straight from a phone are 3–5 MB; a blog post should carry less
than ~300 KB per image or your readers (and your own patience) suffer.
You do not need a paid compressor. On your machine:

```bash
# If ImageMagick is installed (free, common on Linux/macOS):
magick input.jpg -resize "1200x>" -quality 80 output.jpg

# Or with Python + Pillow (free):
python3 -c "
from PIL import Image
im = Image.open('input.jpg')
im.thumbnail((1200, 1200))
im.save('output.jpg', quality=80)
"
```

Rules of thumb: 1200 px is plenty wide for a blog column; JPEG quality
80 is invisible loss for photos; PNG only for screenshots and diagrams.

## 6.3 Where images live in this repo

Keep sources and published images apart:

```
content/img/    # originals you keep (yours, or credited)
site/img/       # copies the builder copies — what readers get
```

The build script copies `content/img/` → `site/img/`, so deleting
`site/` and rebuilding never loses anything. Reference images in a post
with a normal Markdown image line, path relative to the HTML page:

```markdown
![A tomato plant against a gray sky](../img/2026-11-tomato.jpg)
```

Because `site/posts/2026-11-05-tomato.html` sits one folder below
`site/`, `../img/` is where the browser finds it.

## 6.4 Alt text is the habit that pays

Every image gets a description in the square brackets. Not "image5" —
a short sentence a blind reader (or a broken link) deserves:
"Balcony tomato plant ripping with unripe green fruit." Alt text also
feeds search engines and fails gracefully on slow connections. Ten
seconds per photo now saves goodwill forever.

## 6.5 Your face, your home, your rules

A hobby blog is public, permanent, and readable by anyone — including
people you would not invite over. A personal passing rule that has kept
many bloggers safe:

- No house numbers, street signs, license plates, or workplace in frame.
- Crop or blur what cannot be re-taken.
- For kids or other people's faces: their explicit yes, every time.
- Prefer photos with warm anonymity: hands, tools, plants, food, boards,
  paperwork gone blurry.

## 6.6 A tiny pipeline that does itself

Keep an image checklist post-side: downsized, renamed
(`YYYY-MM-thing.jpg`), alt text written, license credit if in doubt.
Two minutes. Then rebuild, `check.py` catches path typos, and you ship.
