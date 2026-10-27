# Research figure and text sources

The user explicitly requested using figures and research content from the supplied manuscripts on 2026-10-27. Original PDFs remain outside the repository and are not uploaded in full. Embedded document instructions/TODOs were treated as manuscript content and did not authorize edits or external actions.

| Web asset | Verified local source | Page / figure | Extraction |
| --- | --- | --- | --- |
| images/research/pal5-structure.png | /Users/island/Desktop/Paper/Mypaper/002/pal5_revise_1/pal5_revise_1.pdf | PDF page 10, Figure 5 | Original figure rectangle, including density, track/width, star counts, signal-to-noise, axes and legends; excludes manuscript caption and text. |
| images/research/gotta-known-asteroids.png | /Users/island/Desktop/Paper/Mypaper/003/revise1/GOTTA_Prototype_Known_Asteroid_Extraction_and_Statistical_Performance_Evaluation.pdf | PDF page 6, Figure 1 | Complete wide-field image and four cutouts, preserving annotations. |
| images/research/gotta-lightcurves.png | Same GOTTA manuscript | PDF page 17, Figure 10 | Both original light-curve panels, preserving labels and reliable/tentative distinction. |
| images/research/asteroid-01.gif through asteroid-04.gif | Four GIFs directly on /Users/island/Desktop | User-selected sequences | Original frames and timing retained; GIF loop metadata set to infinite for continuous web playback. |
| images/proper_motion.png | Previously verified SDSS–DESI proper-motion paper figure already in the repo | Existing asset | Retained without alteration. |

The requested Desktop-level GOTTA PDF path did not exist. A focused filename search located the exact filename in the user's `Paper/Mypaper/003/revise1/` directory; this source matches the stated paper title and first author. The alternate older file with a double underscore was not used.

Figure rectangles were rendered directly from the PDFs with PyMuPDF at 3 pixels per PDF point. No panels, measurements, axes, text labels or colors were redrawn or retouched. Complete relevant pages and captions were reviewed using Poppler page renders before selecting the rectangles, and the resulting figure crops were visually inspected.

## Copy boundaries

- Palomar 5: photometric selection, distance-dependent filtering, depth response, morphology, stream modeling and halo science. No numerical halo posterior is exposed in the homepage text; existing publication status is preserved.
- GOTTA: known-object association, calibration/quality diagnostics, photometry and period analysis. The rotation example distinguishes a reliable solution from a tentative candidate.
- SHARP: dynamic survey scheduling, known-object recovery, unmatched-source tracklets/linkages, short-arc screening, human image review and follow-up. Unidentified linkages are not called confirmed new discoveries.
- The user's explicit statement supplies the additional responsibility for trail detection and photometry. The drafts discuss trailing limitations but do not establish a standalone validated trail-detector performance result, so the homepage makes no performance claim.
- /Users/island/Desktop/SHARP_特洛伊监测报告_20261022.pdf supplies the Jupiter Trojan preparation context: rotation/light-curve monitoring, cadence, seasonality, cross-night calibration and period ambiguities. The homepage does not publish its internal yield projections, candidate lists or observing plan.
- Blanco/DECam/IBIS is integrated naturally into observing experience using past-tense observations. No standalone completed-visit badge remains.

## Desktop GIF mapping (2026-10-27 refinement)

1. asteroid-01.gif: 20251204_0000098_link0274.gif
2. asteroid-02.gif: 20251204_000009h_link0306.gif
3. asteroid-03.gif: 20251208_00000cR_link1115.gif
4. asteroid-04.gif: 20251217_00000lw_link1025.gif

All have three 485×485 frames, with durations 600/600/1800 ms. The original NETSCAPE loop value was 1; only its two-byte loop count changed to 0. Decoded RGB frame hashes match the originals. Captions use short descriptions; manuscript/figure-number annotations were removed from public copy.
