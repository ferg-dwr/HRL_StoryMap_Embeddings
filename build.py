#!/usr/bin/env python3
"""
Build the HRL StoryMap vocabulary definition pages.

    python3 build.py

Reads  terms.json
Writes docs/            <- point GitHub Pages here
       docs/def.css
       docs/index.html
       docs/words/<slug>.html
"""

import json
import html
import re
import shutil
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "docs"
WORDS = OUT / "words"

SITE_SUB = "Healthy Rivers and Landscapes"

# ---------------------------------------------------------------- css

CSS = """/* HRL vocabulary definitions — sized to sit inside StoryMaps body text */
:root{
  --ink:#1B1B1B;
  --term:#1C5BC4;
  --muted:#5A5A5A;
  --body:"Open Sans","Noto Sans","Helvetica Neue",Arial,system-ui,sans-serif;
}
*{box-sizing:border-box;}
html,body{margin:0;padding:0;background:transparent;}
body{
  font-family:var(--body);
  color:var(--ink);
  font-size:16px;
  line-height:1.55;
  padding:2px 2px 6px;
  -webkit-font-smoothing:antialiased;
}

.entry{max-width:660px;margin:0;}

.term{font-weight:700;color:var(--term);}
.say{font-style:italic;color:var(--ink);}
.pos{font-style:italic;color:var(--muted);}

.headline{margin:0 0 2px;font-size:16px;line-height:1.5;}
.def{margin:0;}

/* inline secondary terms inside the definition */
.def .term{font-weight:700;}

.speak{
  display:inline-flex;align-items:center;justify-content:center;
  width:20px;height:20px;padding:0;margin-left:4px;
  vertical-align:-4px;
  color:var(--term);background:none;border:none;border-radius:50%;
  cursor:pointer;opacity:.6;transition:opacity .15s,background .15s;
}
.speak:hover{opacity:1;background:rgba(28,91,196,.1);}
.speak.is-playing{opacity:1;background:rgba(28,91,196,.18);}
.speak svg{width:13px;height:13px;}

/* index page */
.index-head{font-size:17px;font-weight:700;margin:0 0 2px;}
.index-sub{font-size:14px;color:var(--muted);margin:0 0 12px;}
.chips{display:flex;flex-wrap:wrap;gap:6px;}
.chip{
  display:inline-block;font-size:14px;padding:3px 11px;
  border:1px solid #D6DDE8;border-radius:999px;
  color:var(--term);text-decoration:none;background:#fff;
  transition:background .15s,color .15s,border-color .15s;
}
.chip:hover{background:var(--term);border-color:var(--term);color:#fff;}

:focus-visible{outline:2px solid var(--term);outline-offset:2px;}
@media (prefers-reduced-motion:reduce){*{transition:none!important;}}
@media (max-width:420px){body{font-size:15px;}}
"""

# ---------------------------------------------------------------- templates

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?'
    'family=Open+Sans:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">'
)

SPEAK_SVG = (
    '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.7" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M7 3 4 6H2v4h2l3 3V3Z"/><path d="M10.5 5.5a3.5 3.5 0 0 1 0 5"/></svg>'
)

SPEAK_JS = """
<script>
(function(){
  var btns=document.querySelectorAll('.speak');
  if(!('speechSynthesis' in window)){
    btns.forEach(function(b){b.style.display='none';});
    return;
  }
  btns.forEach(function(b){
    b.addEventListener('click',function(){
      window.speechSynthesis.cancel();
      var u=new SpeechSynthesisUtterance(b.dataset.word);
      u.rate=0.82; u.lang='en-US';
      b.classList.add('is-playing');
      u.onend=u.onerror=function(){b.classList.remove('is-playing');};
      window.speechSynthesis.speak(u);
    });
  });
})();
</script>
"""

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{fonts}
<link rel="stylesheet" href="{css}">
</head>
<body>
{content}
{scripts}
</body>
</html>
"""


def e(s):
    return html.escape(str(s), quote=True)


def speak_btn(word):
    return (
        f'<button class="speak" type="button" data-word="{e(word)}" '
        f'aria-label="Hear {e(word)} spoken aloud">{SPEAK_SVG}</button>'
    )


INLINE = re.compile(r"\[\[([^\]|]+)\|([^\]]+)\]\]")


def render_def(text):
    """Turn [[word|pronunciation]] into a bold term plus italic respelling."""
    def sub(m):
        word, say = m.group(1), m.group(2)
        return (
            f'<strong class="term">{e(word)}</strong> '
            f'<em class="say">(say it: {e(say)})</em>'
        )
    return INLINE.sub(sub, e(text)).replace("[[", "").replace("]]", "")


def entry_html(t):
    return f"""<div class="entry">
  <p class="headline"><strong class="term">{e(t['word'])}</strong>
    <em class="say">(say it: {e(t['say'])})</em>{speak_btn(t['word'])}
    &mdash; <em class="pos">{e(t['pos'])}</em></p>
  <p class="def">{render_def(t['def'])}</p>
</div>"""


def build():
    terms = json.loads((HERE / "terms.json").read_text(encoding="utf-8"))

    if OUT.exists():
        shutil.rmtree(OUT)
    WORDS.mkdir(parents=True)

    (OUT / "def.css").write_text(CSS, encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    for slug, t in terms.items():
        (WORDS / f"{slug}.html").write_text(
            PAGE.format(
                title=f"{t['word']} — {SITE_SUB}",
                desc=e(re.sub(r"\[\[([^\]|]+)\|[^\]]+\]\]", r"\1", t["def"])[:150]),
                fonts=FONTS,
                css="../def.css",
                content=entry_html(t),
                scripts=SPEAK_JS,
            ),
            encoding="utf-8",
        )

    chips = "\n    ".join(
        f'<a class="chip" href="words/{slug}.html">{e(t["word"])}</a>'
        for slug, t in terms.items()
    )
    index = f"""<div class="entry">
  <p class="index-head">Words in this story</p>
  <p class="index-sub">Tap a word to see what it means and how to say it.</p>
  <div class="chips">
    {chips}
  </div>
</div>"""

    (OUT / "index.html").write_text(
        PAGE.format(
            title=f"Word list — {SITE_SUB}",
            desc="Vocabulary from the Healthy Rivers and Landscapes StoryMap.",
            fonts=FONTS,
            css="def.css",
            content=index,
            scripts="",
        ),
        encoding="utf-8",
    )

    print(f"built {len(terms)} definition pages + index -> {OUT}/")


if __name__ == "__main__":
    build()
