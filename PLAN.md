# Current plan

## Objective

Expand the homepage animation to six physical stellar streams: three globular-cluster masses and three dwarf-galaxy masses on distinct orbits. Use one shared leading-tail color and one shared trailing-tail color, while preserving 0 Gyr start, 48 Myr/s and automatic looping.

## Milestones

- [x] Recover synchronized repository context and inspect the current generator/renderer.
- [x] Generate six Gala streams with varied masses, sizes and orbital initial conditions.
- [x] Extend the renderer to multiple progenitors with common tail colors and a clear composition.
- [x] Validate numerical exports, browser controls, desktop/mobile visuals and static poster.
- [x] Publish and verify live HTML, data and renderer (80f73a3).

## Outstanding issues

- Preserve the four detailed Skills items, the single-row GIF gallery, other content sections and the footer.
- An existing untracked .DS_Store belongs to local filesystem state; leave it uncommitted.

## Validation criteria

- Three clusters and three dwarf galaxies have distinct masses and orbital parameters, physical finite coordinates, correct release/tail membership, bounded quantization error and stable core energy.
- Shared leading/trailing colors apply to all six streams; viewing/time controls and automatic loops work.
- Visual layout and runtime remain usable at desktop and mobile widths; no browser errors.
- Production-safe build, JS/Python syntax, updated model documentation and deployment verification pass.

## Next recommended steps

1. Finish the multi-stream visual revision in the canonical checkout.
