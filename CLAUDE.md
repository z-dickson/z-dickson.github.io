# Project: Zachary P. Dickson — academic website

Personal academic website, live at **https://z-dickson.github.io**.

## Handoff context (read this first)

In July 2026 this site was **migrated from Quarto to the al-folio Jekyll theme**
(based on the template at `github.com/el-chinosauro/el-chinosauro.github.io`, which
is itself a fork of `alshedivat/al-folio`). All prior content was ported over. The
old Quarto site is preserved on the **`quarto-backup`** branch if anything needs to
be referenced or recovered.

If you're Claude Code picking this up on a fresh machine: just
`git clone https://github.com/z-dickson/z-dickson.github.io` (or `git pull`). The
repo is self-contained; there is no local/remote history mismatch anymore (that was
resolved during the migration).

## Tech stack

- **Jekyll + al-folio** (Ruby). Content is Markdown/Liquid; publications are BibTeX.
- **No local Ruby needed to deploy** — GitHub Actions builds and deploys on push.
- Local preview: **native Ruby on the Ubuntu machine** (set up July 2026, see below),
  **Docker** on the Mac (system Ruby there is too old).

## Deployment (how the site goes live)

1. Push to `master` → the **"Deploy site"** GitHub Actions workflow
   (`.github/workflows/deploy.yml`) builds the Jekyll site and pushes the built
   output to the **`gh-pages`** branch.
2. GitHub Pages serves from `gh-pages` (Settings → Pages → source = `gh-pages`, "legacy" build).

**Known gotcha:** GitHub's own "pages build and deployment" step occasionally fails
with a transient `Deployment failed, try again later.` This is a GitHub-side error,
not a content problem — just **re-run the failed "pages build and deployment" run**
and the live site updates. The already-live site is unaffected while it retries.

## Local preview — native Ruby (Ubuntu machine, preferred there)

Set up July 2026 on the Ubuntu 24.04 machine (Ruby 3.2.3 + ruby-dev +
build-essential + imagemagick, all via apt). Gems are installed **outside the
Dropbox-synced repo** at `~/.local/share/mysite-gems` (via `.bundle/config`,
which is gitignored) so gem files don't churn Dropbox sync.

```bash
bin/serve            # = bundle exec jekyll serve --livereload
```

Open **http://localhost:4000**. Edits to content rebuild automatically and the
browser live-reloads; only `_config.yml` changes need a server restart. Build
takes ~5s.

First-time setup on a new Linux machine (and the `mini_racer` gotcha) is
documented in the comments at the top of `bin/serve`. In short: `mini_racer`
fails to link on Debian/Ubuntu because the `libv8-node` gem ships its static lib
under `x86_64-linux` while the linker looks under `x86_64-linux-gnu` — a symlink
between the two fixes it.

## Local preview with Docker (the Mac)

On the Mac (Apple Silicon), use **Docker Desktop** instead:

```bash
cd <repo>
docker compose up        # uses docker-compose.yml (prebuilt amirpourmand/al-folio image)
```

Then open **http://localhost:8080** (note: port **8080**, not the Jekyll default 4000).
Live-reload runs on port 35729. Stop with Ctrl-C, or `docker compose down`.

- `docker-compose.yml` mounts the repo into the container and sets
  `JEKYLL_ENV=development`. No Ruby/Jekyll install required on the host.
- First run pulls the image (a few minutes); later runs are fast.

## Where content lives (editing map)

| What | File(s) |
|------|---------|
| Homepage bio, profile photo, social links | `_pages/about.md` |
| Published papers | `_bibliography/papers.bib` |
| Under review / working papers | `_bibliography/working.bib` |
| Teaching (courses, PhD workshops) | `_pages/teaching.md` |
| Invited talks + slide links | `_pages/talks.md` |
| Language models & datasets | `_pages/data.md` (permalink `/data/`) |
| CV summary + PDF link | `_pages/cv.md` + `_data/cv.yml` (PDF: `assets/pdf/dickson_CV.pdf`) |
| Homepage news feed | add a file in `_news/` (see existing ones) |
| Site name, email, URL, social handles | `_config.yml` |
| Coauthor auto-links | `_data/coauthors.yml` |
| Journal/venue badges (colors, URLs) | `_data/venues.yml` |
| PDFs / slide decks / images | `assets/pdf/`, `assets/html/`, `assets/img/` |

## Publications system (al-folio BibTeX conventions)

Publications render from the `.bib` files via jekyll-scholar. Useful per-entry fields
(defined in `_config.yml` `filtered_bibtex_keywords`):

- `abbr` — venue badge; must match a key in `_data/venues.yml` (e.g. `APSR`, `CPS`,
  `PolComm`, `PoP`, `JEPP`, `LancetPH`).
- `preview` — thumbnail; a filename in `assets/img/publication_preview/` OR a full URL.
- `html` → "HTML" button (article link), `pdf` → "PDF" (file in `assets/pdf/` or URL),
  `supp` → "Supp", `code` → "Code", `slides`/`website` → their buttons.
- `bibtex_show={true}` → "Bib" popover. `abstract` → "Abs" popover.
- `note` — rendered as raw HTML on its own line (used here for **"Covered in:"** media
  coverage and replication/pre-analysis links, since those have no dedicated buttons).
- `doi` — enables altmetric/dimensions/scholar badges.
- Author self-highlighting: entries use `author={Dickson, Zachary P. and ...}` and
  `_config.yml` `scholar.first_name/last_name` are set to match so the author's name
  is emphasized. Grouping is by `year`, descending. `max_author_limit: 3` collapses
  long author lists (e.g. the Lancet consortium paper) — click "N more authors" to expand.

Use **UTF-8 directly** for accented author names (e.g. `Klüver`, `Đorđe`), not LaTeX
macros — jekyll-scholar handles Unicode and it avoids build edge cases.

## CI checks (all must stay green)

Three workflows run on push/PR: `deploy` (build), `check` (prettier), `link-checker`
(lychee).

- **Prettier** (`prettier 3.1.1` + `@shopify/prettier-plugin-liquid 1.4.0`, config in
  `.prettierrc`) checks `.md/.yml/.html/.liquid/.scss/.js/.json`. To format after edits
  you need Node: `npm install` then `npx prettier . --write`.
- **Link checker** (lychee) checks links in `.md`/`.html`. `.lycheeignore` excludes
  third-party links embedded in the imported slide decks (paywalled/rate-limited/moved),
  author-local build paths, and `localhost` preview URLs (this file is scanned too, so
  any localhost link outside `.lycheeignore` would fail CI).
- The imported reveal.js/Quarto slide decks in **`assets/html/`** are treated as vendored
  artifacts — ignored by BOTH prettier (`.prettierignore`) and lychee. Don't lint them.

## Branches

- `master` — source of truth; deploys to the live site.
- `gh-pages` — built output, managed automatically by Actions (don't edit by hand).
- `quarto-backup` — the previous Quarto site, kept for reference/recovery.

## Optional TODOs / notes

- `_data/cv.yml` is a concise summary; the authoritative CV is the PDF
  (`assets/pdf/dickson_CV.pdf`). Expand the YAML if a richer on-page CV is wanted.
- `orcid_id` in `_config.yml` is blank — fill in if desired (enables an ORCID icon).
- No banner images are used (the template's default `sicilia.jpeg` was removed). Add
  `banner_image:` to a page's front matter + an image in `assets/img/` to reintroduce.
- This file is excluded from the built site (`_config.yml` `exclude`) and from prettier.
