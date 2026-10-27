# Current plan

## Objective

Automatically loop the opening stellar-stream animation from the end back to 0 Gyr, and write Skills as complete first-person paragraphs.

## Milestones

- [x] Recover synchronized repository context.
- [x] Restart active playback at zero while preserving 48 Myr/s speed, pause and time controls.
- [x] Replace Skills fragments with first-person prose and simplify its layout.
- [x] Validate production output and browser endpoint/pause behavior.
- [x] Publish and verify the live update (1d4c307).

## Outstanding issues

- No implementation blocker. Preserve four content sections, the single-row GIF gallery, small avatar, footer, contact data, search identity and publication status.
- Existing Google query/sitemap follow-ups are separate from this revision.

## Validation criteria

- Playing through the endpoint restarts at zero and continues automatically; pause and scrubbing still work.
- Skills contains normal first-person paragraphs and remains readable without overflow.
- Production-safe Jekyll build, JS syntax and focused browser checks pass.
- Verified deployment is recorded in git history and WORKLOG.

## Next recommended steps

1. Continue user-directed refinements from the canonical checkout.
