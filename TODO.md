# Website Handoff Notes

## Current State

- Site is a Jekyll GitHub Pages repo for `https://gauravsinghlab.github.io`.
- The site is currently being fine-tuned locally before republishing.
- The layout has been restyled after `https://sumeetpalsingh.github.io/`: compact academic navigation, centered homepage title, text-first sections, simple image row, and restrained styling.
- Generated/stock imagery was removed.
- The landing page now uses `images/Yeast_hetrogeneitybig.png` as the first image.
- Local preview works through `.\preview.ps1` at `http://127.0.0.1:4000/`.

## Useful Files

- `_config.yml`: site title, description, email, profile links, and GitHub Pages URL.
- `index.md`: homepage content and image row.
- `assets/css/styles.css`: main visual layout.
- `_data/research.yml`: homepage/research theme data.
- `_data/gallery.yml`: gallery image list.
- `images/`: real lab image assets.
- `tools/preview.py`: lightweight local preview builder/server.

## Next Good Tasks

- Replace placeholder member entries in `_data/members.yml`.
- Add real publication citations in `_data/publications.yml`.
- Update `research.md` with the lab's actual research directions.
- Decide whether the homepage image row should show one large image or three equal thumbnails.
- Confirm whether TIFF files should stay in Git or be converted to web PNG/JPG copies only.

## Prompt For New Codex Session

```text
Read the repo and continue from the latest commit. Use TODO.md as the handoff note. We are fine-tuning the research group website locally before republishing.
```
