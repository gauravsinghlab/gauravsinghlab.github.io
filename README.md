# GS Research Group Website

Jekyll GitHub Pages website for a research group.

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
- `_data/members.yml`: editable member data
- `_data/publications.yml`: editable publications data
- `_data/research.yml`: editable research themes
- `_data/methods.yml`: editable methods
- `_data/gallery.yml`: editable gallery entries
- `_posts/`: news posts
- `assets/css/styles.css`: site styling
- `images/`: lab image assets used by the homepage and gallery

Replace placeholder names, emails, addresses, publications, and group text with verified information before publishing.

## Preview Locally

This repo includes a lightweight local preview helper that does not require Ruby:

```powershell
.\preview.ps1
```

Then open:

```text
http://127.0.0.1:4000/
```

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
