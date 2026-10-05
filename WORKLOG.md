# Work log

## 2026-10-05

### Publish education and research-profile update

- Goal: push the user's approved second content iteration.
- Commands: git status/fetch/ahead-behind check; direct HTTPS git push; GitHub Pages builds API; live homepage and Education HTTP checks.
- Result: content commit `374b8f7` pushed to main; GitHub Pages reports built with no error at 2026-10-05T03:26:09Z.
- Validation: live homepage contains AI-assisted coding, DESI-2, active-asteroid monitoring, and Blanco; live Education contains September 2025 onward and the completed 2022–2025 master's dates. Branch synchronized after the content push.
- Files changed afterward: WORKLOG.md and PLAN.md record the completed deployment; both are excluded from site output.
- Remaining issues: none for this deployment. Next: continue refinements from this checkout when requested.

### Update education, skills, collaboration, and asteroid science

- Goal: update PhD education, add Blanco observing plans and language/AI/agent experience, describe DESI-2/IBIS participation, and strengthen the asteroid science narrative.
- Files changed: `_education/01.md`, `_education/02.md`, new `_education/03.md`, `_pages/education.md`, `_pages/about.md`, CHANGELOG.md, PLAN.md, and source notes in docs/PROFILE_SOURCES.md.
- Education: public ORCID confirms B.S. 2018-09 to 2022-07, M.S. 2022-09 to 2025-07, Ph.D. starting 2025-09 with no end date. Retained UCAS naming from the existing site and explicitly added NAOC as research institution. Preserved undergraduate minor, advisor, and thesis information.
- Content: named Python, Java, HTML and LaTeX; added AI-assisted coding/agent workflows; Blanco visit remains upcoming. DESI-2 and IBIS participation follows the user's statement, with primary-source links. Added active-asteroid monitoring goals, photometric/morphological diagnostics, mass-loss mechanisms, and volatile/physical-evolution motivation without claiming discoveries.
- Rendering fix: the generic archive include used empty title links and excerpt-only education content; education now renders complete records with working detail links and explicit descending start-year order. Removed malformed unclosed strong tags from original entries.
- Commands: git status/branch/fetch/history; ORCID educations API; primary-source web lookup; Jekyll safe build with development config; Python assertions on rendered text, education chronology and links; git diff --check; browser inspection of Education and homepage.
- Validation: build passed; requested terms and DESI-2/IBIS URLs render; all three education dates and ordering match ORCID; education detail links are non-empty; visual inspection passed.
- Remaining: no implementation blockers. This iteration is local and not yet pushed; earlier deployment remains online.
- Next: review current local preview and publish this iteration when requested.

### Publish homepage refresh

- Goal: push the approved homepage refresh to GitHub and verify deployment.
- Commands: git status/fetch/history; git push origin main; transport retries; final successful push with per-command `http.proxy=` and HTTP/1.1; GitHub Pages builds API; HTTP checks of live homepage and publications.
- Result: `main` advanced from `d133858` to `232f451`, preserving both local commits. GitHub Pages reports this exact content commit as built, with no build error (2026-10-05T03:04:44Z).
- Validation: live homepage includes cartoon_selfie.png and asteroid research; live publications page includes 10 journal articles, 9 co-authored papers, and arXiv:2607.19162. Local branch synchronized with origin after the content push.
- Transport findings: proxy-routed Git upload repeatedly timed out; direct HTTPS succeeded. No permanent Git/network settings changed. Prepared API fallback performed only a read: it detected the already-updated branch and exited without mutation.
- Files changed afterward: AGENTS.md, PLAN.md, WORKLOG.md record publishing authorization and verified deployment; these documents are excluded from website output.
- Remaining issues: none for this deployment. Next: continue homepage refinements from this canonical checkout when requested.

## 2026-10-04

### Refresh avatar, research, and publications

- Goal: replace avatar, rewrite My Research including asteroid work, complete public co-authored publications, and verify template extension/image support.
- Changed: `_config.yml`, `_pages/about.md`, `_pages/publications.md`, new `_publications/*.md` and publication include/styles, `_layouts/single.html`, avatar/style, `.gitignore`, README and continuity docs. Migrated the three outdated `_submits` records into `_publications`.
- Research: three themes—stellar streams/halo (Palomar 5), deep SDSS–DESI astrometry, and SMT/GOTTA asteroid scheduling/matching/photometry. Removed the stale “1st-year” qualifier. Used the existing public homepage, published proper-motion study, ASAS and GOTTA repository descriptions; no unpublished numerical results added.
- Bibliography: public ORCID contains 10 journal papers (one first-author, nine co-authored); arXiv author-name variants recover those 10 and one additional first-author Palomar 5 preprint. Added DOI/arXiv links, full author lists, concise summaries, and explicit preprint status. See docs/PUBLICATION_SOURCES.md.
- Avatar: exact byte copy of user-provided cartoon_selfie.PNG to images/cartoon_selfie.png; rounded-square CSS preserves the whole illustration. Publication figures now render; reused existing proper_motion.png.
- Commands: git fetch/status/history; ORCID public API, arXiv API, Crossref/publisher lookup; Homebrew Ruby 3.3 install; BUNDLE_PATH=.local/bundle bundle install; bundle exec jekyll build; jekyll serve with development config; Python metadata/output checks; git diff --check.
- Setup/debugging: Homebrew dependency install hit a bottle-metadata error; Ruby itself installed successfully and OpenSSL loaded. Initial build caught an undefined new Sass variable; replaced it with the template's existing text-color variable. Used arXiv English author names for CSST distortion paper because publisher metadata interleaves Chinese name components.
- Validation: Jekyll production and development builds passed; all 10 ORCID DOIs match, 11 arXiv IDs are unique, authorship and generated detail pages verified. Avatar SHA-256 matches supplied original. Maintenance files absent from generated output. Browser verified loaded images, 11 entries, expandable authors, desktop avatar, and no horizontal overflow at 1440px or 390px on the publications page.
- Remaining: user may supply additional non-public papers or updated Palomar 5 status. Existing unrelated template pages/placeholders remain for a later requested review. No push/deployment performed.
- Next: review local homepage/publications preview and refine text or add user-selected scientific figures; publish only when requested.

### Establish canonical workspace

- Goal: locate the existing personal homepage and establish its canonical local workspace.
- Found: `xiaoyunao/xiaoyunao.github.io`, an existing Jekyll/academicpages website.
- Workspace: `/Users/island/Desktop/personal_page`; cloned directly into the previously empty directory.
- Commands: `gh repo list xiaoyunao`, `gh repo clone xiaoyunao/xiaoyunao.github.io .`, `git status --short --branch`, `git branch --show-current`, `git fetch --all --prune`, `git log --oneline --decorate --graph -n 15 --all`, `git rev-list --left-right --count HEAD...@{upstream}`, `git remote -v`.
- Findings: branch `main` tracks `origin/main`; both pointed to `d133858` after cloning; existing README contains template instructions; no existing WORKLOG.md, PLAN.md, or repository AGENTS.md.
- Files added: `AGENTS.md`, `WORKLOG.md`, `PLAN.md` for workspace continuity. Existing website files remain untouched.
- Validation: clone and fetch succeeded; ahead/behind count was `0 0`; original checkout was clean. Documentation reviewed with `git diff --cached --check`; website build deferred because no website changes were requested.
- Remaining: no setup blockers; local dependency installation and website build have not been attempted.
- Next: await the user's homepage change request; perform all future maintenance from this checkout. Record setup in a local documentation commit; do not push or deploy during this task.
