# Current plan

## Objective

Polish the opening galaxy/stream animation and research media in the canonical homepage checkout, following the user's latest 2026-10-27 feedback. Use concise factual copy, a zero-time opening, stronger galaxy imagery, Palomar 5 Figure 5 and the four supplied Desktop GIFs.

## Milestones

- [x] Recover synchronized repository context.
- [x] Generate and integrate the new galaxy texture and simplified scene graphics/controls.
- [x] Change playback to start at 0 Gyr and run at 24 Myr/s; update the static opening frame.
- [x] Remove defensive explanations and manuscript/figure-number captions.
- [x] Extract Palomar 5 Figure 5 and embed all four Desktop observation GIFs.
- [x] Validate GIF frame identity/timing and continuous looping, plus zero-time/texture/browser checks.
- [x] Complete final mobile/rendered-site checks.
- [x] Commit/push and verify GitHub Pages deployment and live assets (a8764c5; versioned assets c38cb50).

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
