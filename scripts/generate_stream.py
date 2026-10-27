"""Generate the homepage's physical, three-dimensional tidal-stream trajectories.

Run in the optional environment documented in docs/STREAM_MODEL.md. The web page
only plays the exported snapshots; it never needs the Python dependencies.
"""
from pathlib import Path
import gzip
import json
import argparse

import astropy.coordinates as coord
import astropy.units as u
from astropy.constants import G
import gala
import gala.dynamics as gd
import gala.potential as gp
from gala.dynamics import mockstream as ms
from gala.units import galactic
import h5py
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def generate(duration=3000, n_particles=2):
    if duration <= 0 or duration % 5:
        raise ValueError('Duration must be a positive multiple of the 5 Myr snapshot interval')
    local = ROOT / '.local/stream-model'
    output = ROOT / 'assets/data'
    local.mkdir(parents=True, exist_ok=True)
    output.mkdir(parents=True, exist_ok=True)

    # A fixed, spherical baseline, deliberately independent of the paper's fit.
    radius = 8.2 * u.kpc
    bulge = gp.HernquistPotential(m=3.4e10*u.Msun, c=.7*u.kpc, units=galactic)
    disk = gp.MiyamotoNagaiPotential(m=1e11*u.Msun, a=6.5*u.kpc, b=.26*u.kpc, units=galactic)
    baryons = gp.CCompositePotential(bulge=bulge, disk=disk)
    baryonic_v2 = baryons.circular_velocity([radius.value, 0, 0]*u.kpc)[0]**2
    x = (radius/(20*u.kpc)).value
    halo_mass = (((232*u.km/u.s)**2-baryonic_v2)*radius/(G*(np.log1p(x)-x/(1+x)))).to(u.Msun)
    potential = gp.CCompositePotential(bulge=bulge, disk=disk, halo=gp.NFWPotential(m=halo_mass, r_s=20*u.kpc, units=galactic))
    hamiltonian = gp.Hamiltonian(potential)
    coord.galactocentric_frame_defaults.set('v4.0')
    pal5 = coord.SkyCoord(ra=229.018*u.deg, dec=-.124*u.deg,
                         distance=20.6*u.kpc, pm_ra_cosdec=-2.754*u.mas/u.yr,
                         pm_dec=-2.643*u.mas/u.yr, radial_velocity=-58.61*u.km/u.s)
    present = gd.PhaseSpacePosition(pal5.transform_to(coord.Galactocentric()).data)
    mass = 2e4*u.Msun
    scale = 15*u.pc
    cluster = gp.PlummerPotential(m=mass, b=scale, units=galactic)
    df = ms.FardalStreamDF(gala_modified=True, random_state=np.random.RandomState(20261027))
    generator = ms.MockStreamGenerator(df, hamiltonian, progenitor_potential=cluster)
    snapshots = local/'snapshots.h5'
    stream, _ = generator.run(present, mass, dt=-1*u.Myr, n_steps=duration,
                              release_every=8, n_particles=n_particles,
                              output_every=5, output_filename=str(snapshots),
                              overwrite=True, progress=False,
                              Integrator_kwargs={'atol':1e-10, 'rtol':1e-10})
    with h5py.File(snapshots) as handle:
        positions = handle['stream/pos'][:].transpose(1, 2, 0)
        core = handle['nbody/pos'][:, :, 0].T
        core_velocity = handle['nbody/vel'][:, :, 0].T
        times = handle['stream/time'][:]
    release_time = stream.release_time.to_value(u.Myr)
    active = times[:, None] >= release_time[None, :] - 1e-8
    assert np.isfinite(positions[active]).all()
    assert np.isfinite(core).all()

    # 2 pc quantization preserves the physical width and avoids inflated ribbons.
    # The core is index zero in every frame. Unreleased particles use a sentinel.
    spatial_scale = .002
    combined = np.concatenate((core[:, None, :], positions), axis=1)
    live = np.column_stack((np.ones(len(times), dtype=bool), active))
    assert np.abs(combined[live]).max()/spatial_scale < 32767
    quantized = np.full(combined.shape, -32768, dtype='<i2')
    quantized[live] = np.rint(combined[live]/spatial_scale).astype('<i2')
    data = quantized.tobytes(order='C')
    with gzip.GzipFile(filename=str(output/'tidal-stream.bin.gz'), mode='wb', mtime=0) as handle:
        handle.write(data)

    phase = gd.PhaseSpacePosition(pos=core.T*u.kpc, vel=core_velocity.T*u.kpc/u.Myr)
    energy = hamiltonian.energy(phase).value
    energy_drift = float(np.ptp(energy)/abs(np.median(energy)))
    assert energy_drift < 1e-6, energy_drift
    quantization_error = float(np.abs(combined[live]-quantized[live]*spatial_scale).max())
    assert quantization_error <= spatial_scale/2 + 1e-10
    assert np.all(np.diff(live.sum(axis=1)) >= 0)
    metadata = {
        'format':'little-endian int16, frame/particle/xyz; core first; -32768 = unreleased',
        'scaleKpc':spatial_scale, 'frameCount':len(times), 'particleCount':combined.shape[1],
        'frameStepMyr':5, 'durationMyr':duration,
        'tail':['core']+stream.lead_trail.tolist(),
        'releaseMyr':[0]+np.rint(release_time-times[0]).astype(int).tolist(),
        'galaVersion':gala.__version__, 'seed':20261027,
        'model':'Fixed Hernquist bulge + Miyamoto-Nagai disk + spherical NFW halo; Vc(8.2 kpc)=232 km/s',
        'progenitorMassMsun':mass.value, 'plummerScalePc':scale.value,
        'haloMassMsun':halo_mass.value,
        'validation':{'coreRelativeEnergyDrift':energy_drift, 'maximumQuantizationErrorKpc':quantization_error, 'particlesInEachTail':int(len(release_time)/2)},
    }
    (output/'tidal-stream.json').write_text(json.dumps(metadata, separators=(',', ':'))+'\n')
    np.savez_compressed(local/'diagnostics.npz', positions=positions, core=core, times=times, active=active)
    make_diagnostic(positions, core, local, duration)
    print(json.dumps({'frames':len(times), 'particles':combined.shape[1], 'gzBytes':(output/'tidal-stream.bin.gz').stat().st_size, **metadata['validation']}, indent=2))


def make_diagnostic(positions, core, local, duration):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(11, 5), layout='constrained')
    ax = fig.add_subplot(121, projection='3d')
    p = positions[-1]
    ax.scatter(*p.T, s=.5, alpha=.5, color='#4f83bb')
    ax.scatter(*core[-1], s=20, color='#d49d48', label='Progenitor')
    ax.plot(*core.T, color='#9aa0a6', lw=.5, alpha=.6, label='Core orbit')
    ax.set(xlabel='x [kpc]', ylabel='y [kpc]', zlabel='z [kpc]', title=f'Gala tidal stream at {duration/1000:g} Gyr')
    ax.set_box_aspect((1,1,1));ax.legend(fontsize=8)
    ax2 = fig.add_subplot(122)
    ax2.scatter(p[:,0], p[:,2], s=.8, alpha=.4, color='#4f83bb')
    ax2.scatter(*core[-1,[0,2]], s=25, color='#d49d48')
    ax2.set(xlabel='x [kpc]', ylabel='z [kpc]', title='Physical positions; equal spatial scale')
    ax2.set_aspect('equal');fig.savefig(local/'stream-diagnostic.png', dpi=160)
    plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--duration', type=int, default=3000)
    parser.add_argument('--particles-per-tail', type=int, default=2)
    args = parser.parse_args()
    generate(args.duration, args.particles_per_tail)
