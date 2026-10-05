# Current plan

## Objective

Maintain the personal homepage exclusively from `/Users/island/Desktop/personal_page`. Current milestone: improve Google search visibility and connect Google Search Console using the existing free GitHub Pages address.

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
- [x] Publish the education/research-profile iteration and verify live content (2026-10-05, `374b8f7`).
- [ ] Incorporate any additional text, figures, or papers supplied by the user.
- [x] Push the authorized refresh and verify GitHub Pages deployment (2026-10-05, content commit `232f451`).

- [x] Add search descriptions, a descriptive homepage title, and linked Person identity metadata.
- [x] Exclude template examples from publication and clean the sitemaps.
- [x] Validate production metadata, real content records, and removal of sample output.
- [x] Deploy the search-visibility update (`c18d544`, verified GitHub Pages build).
- [x] Obtain the user's Google Search Console HTML verification tag from the logged-in account.
- [ ] Publish the verification tag and verify ownership.
- [ ] Submit sitemap.xml and inspect/request homepage indexing in Search Console.

## Outstanding issues

- Palomar 5 remains a preprint in the checked public sources; a newer private status requires user input.
- Public-record completeness is verified against ORCID and both arXiv name variants, not any private manuscript list.
- Google sign-in and token retrieval completed; verification and sitemap submission await token deployment.
- Unused template sections are now excluded from the public build, with sources retained. Replace sample content before enabling them.
- The preview uses the existing GitHub Pages dependency stack; optional Faraday/GitHub metadata warnings do not prevent building.

## Validation criteria

- Avatar loads without cropping; My Research includes asteroid observations and pipeline work.
- Published and preprint records remain distinct, with verified authorship, unique IDs, and working generated detail pages.
- Publication figures load and fit narrow screens; maintenance files are excluded from site output.
- Jekyll build and git whitespace checks pass; website changes are saved in a local milestone commit.

## Next recommended steps

1. Complete the verification-tag deployment.
2. Add the Google verification token when supplied; deploy, verify ownership, submit sitemap.xml, and inspect homepage indexing. See docs/SEARCH_VISIBILITY.md.
3. Continue content maintenance only from this checkout. No paid domain or server is planned.
