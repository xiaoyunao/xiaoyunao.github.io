# Homepage tidal-stream population

The homepage projects six physical Galactocentric streams computed with Gala: three globular-cluster progenitors and three dwarf-galaxy progenitors. JavaScript interpolates the exported particle snapshots in physical time and projects all six through the same rotatable three-dimensional view.

## Reproduce

```sh
cd /Users/island/Desktop/personal_page
python3 -m venv .local/stream-venv
.local/stream-venv/bin/python -m pip install -r scripts/requirements-stream.txt
.local/stream-venv/bin/python -m py_compile scripts/generate_stream.py
.local/stream-venv/bin/python scripts/generate_stream.py
```

For a short integration into an ignored output directory:

```sh
.local/stream-venv/bin/python scripts/generate_stream.py --duration 120 --output-directory .local/stream-smoke
```

The existing Mac environment uses the bundled Python 3.12 with system site packages. These dependencies are optional offline tools; GitHub Pages serves the exported data and ordinary JavaScript.

## Potential and initial conditions

The common external potential contains a Hernquist bulge (3.4e10 solar masses, 0.7 kpc), a Miyamoto–Nagai disk (1e11 solar masses, a=6.5 kpc, b=0.26 kpc) and a spherical NFW halo with scale radius 20 kpc. The halo mass gives a total circular speed of 232 km/s at 8.2 kpc.

| ID | Type | Mass (solar masses) | Plummer b (pc) | Initial radius (kpc) | Initial inclination | Node | Speed / local circular speed | Core radius range (kpc) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| gc-1 | Globular cluster | 20,000 | 15 | 13 | 35° | 20° | 0.82 | 7.85–13.13 |
| gc-2 | Globular cluster | 100,000 | 25 | 18 | 70° | 145° | 0.75 | 8.17–18.38 |
| gc-3 | Globular cluster | 500,000 | 45 | 23 | 115° | 260° | 0.90 | 17.35–23.31 |
| dwarf-1 | Dwarf galaxy | 10,000,000 | 250 | 19 | 50° | 95° | 0.72 | 8.55–19.23 |
| dwarf-2 | Dwarf galaxy | 50,000,000 | 450 | 24 | 90° | 210° | 0.68 | 9.28–24.35 |
| dwarf-3 | Dwarf galaxy | 200,000,000 | 700 | 27 | 140° | 315° | 0.78 | 15.35–27.14 |

Each initial position lies at the tabulated radius and node in the Galactic plane. Its tangential velocity is tilted by the inclination and scaled relative to the local circular speed; all Cartesian positions and velocities are recorded in JSON. These produce varied orbital radii, inclinations, directions and eccentricities.

Each stream is integrated separately in the common Milky Way potential with its own fixed-mass Plummer progenitor potential. Gala's modified Fardal particle-release distribution is seeded deterministically (20261027 through 20261032). Released tracers feel their progenitor and the Galactic potential. Progenitor mass is constant; stream self-gravity and interactions between the six systems are omitted.

## Sampling and rendering

- Integrate forward from 0 to 3000 Myr with 1 Myr steps, DOPRI853 tolerances 1e-10 and snapshots every 10 Myr.
- Release particles every 12 Myr: one per tail for each cluster, two per tail for each dwarf galaxy. Final population: 4,518 tail tracers and six cores, 301 frames.
- All leading tails use `#add2ff`; all trailing tails use `#f1cf9a`. The renderer uses tail membership directly, independent of the progenitor.
- Core stellar markers sample each progenitor's Plummer scale, with a small screen-space center marker and glow. Stream widths come from particle positions. Desktop labels show type and mass; mobile preserves the common tail legend and omits the small individual labels.
- Playback starts at 0 Gyr and advances at 48 Myr per wall-clock second. The full interval takes 62.5 seconds and automatically loops back to zero.
- The same view transform projects particles and the generated galaxy texture `images/milky-way-disk.png`. Texture source and prompt: [GALAXY_ASSET.md](GALAXY_ASSET.md).
- Offscreen/hidden tabs pause scheduling; reduced-motion preferences, manual pause, time scrubbing, view presets and pointer rotation remain supported.

## Data format and validation

`assets/data/tidal-stream.json` uses schema version 2. Each entry in `streams` identifies a core index and a contiguous tail-particle range, plus mass, scale, initial conditions, random seed and validation results. The flattened `tail` and `releaseMyr` arrays index the same particles as the binary data.

`assets/data/tidal-stream.bin.gz` contains little-endian int16 coordinates in frame/particle/xyz order; -32768 marks unreleased particles. Each stream's core precedes its particles. This export uses a 0.003 kpc unit and has at most 1.5 pc rounding error per component. Compressed size: 3,843,030 bytes.

Generation checks active-coordinate finiteness, monotonic release counts, equal counts in the two tails, index consistency, quantization bounds and core relative energy drift below 1e-6. The maximum measured energy drift is 2.60e-9. The short 120 Myr six-stream integration also passes these checks.

Local scientific outputs live in `.local/stream-model/population/`: six HDF5 snapshot files, `diagnostics.npz` and `streams-diagnostic.png`. The diagnostic shows each system separately with equal spatial scales. `images/stream-poster.jpg` captures the same six-core renderer at exactly 0 Gyr using a temporary local capture page removed by the final production build.

## References

- [Gala mock-stream methods](https://gala.adrian.pw/en/latest/dynamics/mockstreams.html)
- [MockStreamGenerator snapshot API](https://gala.adrian.pw/en/latest/api/gala.dynamics.mockstream.MockStreamGenerator.html)
