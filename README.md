# GS Research Group Website

Jekyll GitHub Pages website for the Gaurav Singh Lab at SNIoE.

## Edit Content

- `index.md`: homepage
- `research.md`: research themes and methods
- `members.md`: group members and alumni page shell
- `publications.md`: selected publications page shell
- `news.md`: group updates page shell
- `gallery.md`: lab/gallery highlights page shell
- `contact.md`: address, email, and openings
- `_config.yml`: site title, navigation, email, links, and base URL settings
- `_includes/header.html`: shared navigation
- `_includes/footer.html`: shared footer
- `_layouts/default.html`: shared page layout
- `_layouts/post.html`: news post layout
- `_data/publications.yml`: editable publications data
- `_data/research.yml`: editable research themes
- `_data/methods.yml`: editable methods
- `_data/gallery.yml`: editable gallery entries
- `_posts/`: news posts
- `assets/css/styles.css`: site styling
- `images/brand/`: header logo and brand assets
- `images/home/`: homepage hero and slideshow images
- `images/gallery/`: gallery-specific web images if needed
- `images/raw/`: original source images such as TIFFs
- `_data/brand.yml`: brand/logo image paths
- `_data/homepage.yml`: homepage slideshow image list

Keep lab text, contact details, member information, and publication records verified before publishing. The homepage hero text currently sits on top of the image in a left-aligned overlay panel.

Image organization:

- Keep the header logo path in `_data/brand.yml`.
- Keep homepage slideshow images in `_data/homepage.yml`.
- Use descriptive lowercase hyphenated filenames inside purpose-based folders under `images/`.
- Treat `images/raw/` as source material, not direct web-facing assets.

## Preview Locally

This repo includes a lightweight local preview helper that does not require Ruby:

```powershell
.\preview.ps1
```

Then open:

```text
http://127.0.0.1:4000/
```

If you change content or CSS, rerun `.\preview.ps1` or the preview builder so the served site reflects the latest files.

If Ruby is installed, the full Jekyll preview also works:

```powershell
bundle install
bundle exec jekyll serve
```

Then open the local URL Jekyll prints, usually `http://127.0.0.1:4000/`.

## Publish On GitHub Pages

1. Push these files to a GitHub repository.
2. In GitHub, open `Settings` -> `Pages`.
3. Set `Source` to `Deploy from a branch`.
4. Select the branch that contains this site, usually `main`, and the root folder `/`.
5. Save. GitHub will publish the site at the Pages URL shown in the settings.

GitHub Pages will build the Jekyll site automatically.

## Working Across Computers

Use GitHub as the source of truth. Before switching computers:

```powershell
git status
git add .
git commit -m "Describe current website changes"
git push
```

On another computer:

```powershell
git clone https://github.com/gauravsinghlab/gauravsinghlab.github.io.git
```

or, if already cloned:

```powershell
git pull
```

Then open a new Codex session and say:

```text
Read the repo and continue from the latest commit. Use TODO.md as the handoff note.
```
