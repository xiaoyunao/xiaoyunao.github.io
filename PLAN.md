# Current plan

## Objective

Maintain the personal homepage exclusively from `/Users/island/Desktop/personal_page`. Current milestone: education, programming/observing/AI skills, DESI-2/IBIS participation, and active-asteroid science.

## Milestones

- [x] Clone and establish the canonical workspace.
- [x] Replace the avatar with the supplied illustration, preserving the full image.
- [x] Rewrite My Research around streams/halo, astrometry, and asteroid survey methods.
- [x] Verify and add all 10 journal articles in public ORCID, plus the Palomar 5 arXiv preprint.
- [x] Support publication figures and expandable author lists.
- [x] Build locally and check rendered pages and responsive layout.
- [x] Update education dates and add the PhD entry from ORCID.
- [x] Add explicit languages, AI/agent experience, upcoming Blanco observing, DESI-2/IBIS links, and active-asteroid science goals.
- [x] Build and inspect the updated Education and homepage.
- [ ] Publish this new iteration when requested.
- [ ] Incorporate any additional text, figures, or papers supplied by the user.
- [x] Push the authorized refresh and verify GitHub Pages deployment (2026-10-05, content commit `232f451`).

## Outstanding issues

- Palomar 5 remains a preprint in the checked public sources; a newer private status requires user input.
- Public-record completeness is verified against ORCID and both arXiv name variants, not any private manuscript list.
- Other template sections (including CV and blog/portfolio examples) still contain sample content; review before exposing new navigation items.
- The preview uses the existing GitHub Pages dependency stack; optional Faraday/GitHub metadata warnings do not prevent building.

## Validation criteria

- Avatar loads without cropping; My Research includes asteroid observations and pipeline work.
- Published and preprint records remain distinct, with verified authorship, unique IDs, and working generated detail pages.
- Publication figures load and fit narrow screens; maintenance files are excluded from site output.
- Jekyll build and git whitespace checks pass; website changes are saved in a local milestone commit.

## Next recommended steps

1. Review the latest local homepage and Education at http://127.0.0.1:4000/; this iteration has not yet been pushed.
2. Incorporate additional papers or publication-status corrections if provided.
3. Add selected science figures or new sections as requested; the template supports both.
4. Before future changes, recover Git state and read WORKLOG.md and this plan.
