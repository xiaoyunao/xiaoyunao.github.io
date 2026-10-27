# Current plan

## Objective

Apply the latest 2026-10-27 layout/playback adjustment: four smaller observation GIFs on one row and double the current stream speed to 48 Myr/s. Preserve the existing visual design and content.

## Milestones

- [x] Recover synchronized repository context.
- [x] Generate and integrate the new galaxy texture and simplified scene graphics/controls.
- [x] Change playback to start at 0 Gyr and run at 48 Myr/s; update the static opening frame.
- [x] Remove defensive explanations and manuscript/figure-number captions.
- [x] Extract Palomar 5 Figure 5 and embed all four Desktop observation GIFs in a compact single row.
- [x] Validate GIF frame identity/timing and continuous looping, plus zero-time/texture/browser checks.
- [x] Complete final mobile/rendered-site checks.
- [ ] Commit/push and verify the latest single-row/speed update on GitHub Pages.

## Outstanding issues

- No implementation blocker. Preserve the established four-section structure, small avatar, existing footer, contact data, search identity and publication status.
- Existing Google query/sitemap follow-ups are separate from this visual revision.

## Validation criteria

- Opening state is 0.00 Gyr; playback, view/reset and time controls work at the new speed.
- New galaxy texture loads; interface is readable on desktop and mobile without overflow.
- Public copy has no rejected explanatory/caption phrases. Pal5 uses Figure 5 with all panels preserved.
- Four native GIFs load and loop continuously, retaining original frame pixels and timing.
- Production-safe Jekyll build, JS/Python syntax, links/assets/anchors, metadata/contact and unchanged publication/footer checks pass.
- Milestone and verified deployment recorded in git history and WORKLOG.

## Next recommended steps

1. Continue user-directed visual edits from this checkout with concise academic copy and direct image captions.
