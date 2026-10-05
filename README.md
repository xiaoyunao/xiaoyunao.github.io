# Yun-Ao Xiao's academic homepage

Source for https://xiaoyunao.github.io, built with Jekyll and the academicpages template.
The canonical editing workspace is `/Users/island/Desktop/personal_page`.

## Local preview

This checkout was validated with Ruby 3.3 and the `github-pages` Gemfile dependencies.
On this Mac, Ruby is installed at `/opt/homebrew/opt/ruby@3.3/bin`; gems are kept locally in `.local/bundle`.
The generated `Gemfile.lock` is local and ignored, matching the repository's unpinned GitHub Pages dependency setup.

```sh
cd /Users/island/Desktop/personal_page
export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"
export BUNDLE_PATH=".local/bundle"
bundle install
bundle exec jekyll build
bundle exec jekyll serve --config _config.yml,_config.dev.yml --host 127.0.0.1
```

Open http://127.0.0.1:4000. Restart the preview after changing `_config.yml`.
On another machine, install a compatible Ruby and Bundler first and omit the Mac-specific PATH line.

## Editing guide

- `_pages/about.md`: biography and My Research (Markdown with optional HTML figures).
- `_config.yml`: site identity, author profile, and avatar filename.
- `_publications/*.md`: one paper per file, with verified authors, status, dates, journal information, and links.
- `_pages/publications.md` and `_includes/publication-entry.html`: publication groups and list presentation.
- `_data/navigation.yml`: visible menu entries. Unused template pages and sample posts are excluded from the published site in `_config.yml`; replace placeholders and remove the corresponding exclusion before enabling them.
- `images/`: avatar and research/publication illustrations.
- `docs/PUBLICATION_SOURCES.md`: publication audit and source links.
- `WORKLOG.md`, `PLAN.md`, and git history: project continuity.

For a publication illustration, set `image`, `image_alt`, and `image_caption` in the paper's front matter; the list renders it automatically. Add a figure to the paper body if it should also appear on its detail page. Research text can embed a figure directly:

```html
<figure>
  <img src="{{ '/images/proper_motion.png' | relative_url }}" alt="Description of the scientific figure" loading="lazy">
  <figcaption>Caption and source.</figcaption>
</figure>
```

Publication records use `status: published` or `status: preprint`, and `role: first-author` or `role: co-author`. Dates for journal articles follow issue dates for consistent sorting; the website displays years. New papers require authorship and status verification. Maintenance docs and local tooling are excluded from site output.

## Search visibility

- The homepage uses `seo_title` for its browser/search title while keeping its visible heading. Page `description` or `excerpt` supplies the description tag; `_includes/seo.html` renders metadata and Person profile links.
- `jekyll-sitemap` generates `/sitemap.xml` and `/robots.txt`. Only actual content should be published; template sources remain in Git and are explicitly excluded in `_config.yml`.
- Google Search Console setup and indexing checks: [docs/SEARCH_VISIBILITY.md](docs/SEARCH_VISIBILITY.md).

## Original template documentation

A Github Pages template for academic websites. This was forked (then detached) by [Stuart Geiger](https://github.com/staeiou) from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/), which is © 2016 Michael Rose and released under the MIT License. See LICENSE.md.

I think I've got things running smoothly and fixed some major bugs, but feel free to file issues or make pull requests if you want to improve the generic template / theme.

### Note: if you are using this repo and now get a notification about a security vulnerability, delete the Gemfile.lock file. 

# Instructions

1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section
1. (Optional) Use the Jupyter notebooks or python scripts in the `markdown_generator` folder to generate markdown files for publications and talks from a TSV file.

See more info at https://academicpages.github.io/

## To run locally (not on GitHub Pages, to serve on your own computer)

1. Clone the repository and made updates as detailed above
1. Make sure you have ruby-dev, bundler, and nodejs installed: `sudo apt install ruby-dev ruby-bundler nodejs`
1. Run `bundle clean` to clean up the directory (no need to run `--force`)
1. Run `bundle install` to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.
1. Run `bundle exec jekyll liveserve` to generate the HTML and serve it from `localhost:4000` the local server will automatically rebuild and refresh the pages on change.

# Changelog -- bugfixes and enhancements

There is one logistical issue with a ready-to-fork template theme like academic pages that makes it a little tricky to get bug fixes and updates to the core theme. If you fork this repository, customize it, then pull again, you'll probably get merge conflicts. If you want to save your various .yml configuration files and markdown files, you can delete the repository and fork it again. Or you can manually patch. 

To support this, all changes to the underlying code appear as a closed issue with the tag 'code change' -- get the list [here](https://github.com/academicpages/academicpages.github.io/issues?q=is%3Aclosed%20is%3Aissue%20label%3A%22code%20change%22%20). Each issue thread includes a comment linking to the single commit or a diff across multiple commits, so those with forked repositories can easily identify what they need to patch.
