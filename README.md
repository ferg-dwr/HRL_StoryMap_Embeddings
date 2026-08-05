# HRL StoryMap — Vocabulary Definitions

Inline definition cards for the Healthy Rivers and Landscapes StoryMap. One page per
word, hosted on GitHub Pages, embedded into StoryMaps as iframes.

## Add or change a word

1. Edit `terms.json`
2. `python3 build.py`
3. Commit and push — Pages redeploys automatically

`docs/` is generated. Don't hand-edit it.

### Fields

| Field | Notes |
|---|---|
| `word` | The headword |
| `say` | Pronunciation respelling, e.g. `ee-KAH-luh-jee` — CAPS on the stressed syllable |
| `pos` | Part of speech |
| `def` | Definition, elementary reading level |

The JSON key becomes the URL slug: `"tule"` → `/words/tule.html`

### Secondary terms inside a definition

Use `[[word|pronunciation]]` anywhere in `def` and it renders bold blue with an
italic respelling:

    "Scientists who study ecology are called [[ecologists|ee-KAH-luh-jists]]."

## One-time GitHub Pages setup

1. Create a repo (public — Pages requires it on free plans)
2. Push this folder
3. Settings → Pages → Source: *Deploy from a branch*, Branch: `main`, Folder: `/docs`

Live at `https://<user>.github.io/<repo>/words/<slug>.html`

## Embedding in ArcGIS StoryMaps

**Embed block** — paste the URL. The card centers itself vertically and horizontally in
whatever space it's given, so err on the tall side; extra space around the card is
invisible.

| Definition length | Height |
|---|---|
| 2-3 lines | 200px |
| 4-5 lines | 250px |
| 6+ lines (ecology, salmon, restoration) | 300px |
| Index page | 280px |

Text reflows longer on narrow screens, so add ~60px of headroom and check on mobile.
Too short clips the card; too tall just adds empty space.

**Or link the word** — select the bold term in the StoryMaps text, add a link, paste
the URL. Opens in a new tab and doesn't interrupt the scroll.

## Notes

- `.nojekyll` is required, or GitHub skips some files
- Fonts load from Google Fonts (Open Sans, to match the StoryMaps default theme). If
  agency policy blocks external CDNs, self-host and edit `FONTS` in `build.py`
- The small speaker icon uses the browser's built-in speech synthesis. No audio files,
  no API keys. It hides itself where unsupported
- Background is transparent so it inherits the StoryMaps panel color