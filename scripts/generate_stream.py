"""Generate the homepage's six physical, three-dimensional tidal streams.

Run in the optional environment documented in docs/STREAM_MODEL.md. The website
plays the exported Gala snapshots without any Python runtime.
"""
from pathlib import Path
import argparse
import gzip
import json

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
SEED = 20261027
FRAME_STEP = 10
RELEASE_EVERY = 12
PROFILES = [
    dict(id='gc-1', kind='cluster', label='Globular cluster', mass=2e4, scale_pc=15,
         radius=13, node=20, inclination=35, speed_fraction=.82),
    dict(id='gc-2', kind='cluster', label='Globular cluster', mass=1e5, scale_pc=25,
         radius=18, node=145, inclination=70, speed_fraction=.75),
    dict(id='gc-3', kind='cluster', label='Globular cluster', mass=5e5, scale_pc=45,
         radius=23, node=260, inclination=115, speed_fraction=.9),
    dict(id='dwarf-1', kind='dwarf', label='Dwarf galaxy', mass=1e7, scale_pc=250,
         radius=19, node=95, inclination=50, speed_fraction=.72),
    dict(id='dwarf-2', kind='dwarf', label='Dwarf galaxy', mass=5e7, scale_pc=450,
         radius=24, node=210, inclination=90, speed_fraction=.68),
    dict(id='dwarf-3', kind='dwarf', label='Dwarf galaxy', mass=2e8, scale_pc=700,
         radius=27, node=315, inclination=140, speed_fraction=.78),
]


def milky_way():
    radius = 8.2 * u.kpc
    bulge = gp.HernquistPotential(m=3.4e10*u.Msun, c=.7*u.kpc, units=galactic)
    disk = gp.MiyamotoNagaiPotential(m=1e11*u.Msun, a=6.5*u.kpc, b=.26*u.kpc, units=galactic)
    baryons = gp.CCompositePotential(bulge=bulge, disk=disk)
    baryonic_v2 = baryons.circular_velocity([radius.value, 0, 0]*u.kpc)[0]**2
    x = (radius/(20*u.kpc)).value
    halo_mass = (((232*u.km/u.s)**2-baryonic_v2)*radius/(G*(np.log1p(x)-x/(1+x)))).to(u.Msun)
    potential = gp.CCompositePotential(
        bulge=bulge, disk=disk,
        halo=gp.NFWPotential(m=halo_mass, r_s=20*u.kpc, units=galactic))
    return gp.Hamiltonian(potential), halo_mass.to_value(u.Msun)


def initial_state(profile, hamiltonian):
    node, tilt = np.deg2rad([profile['node'], profile['inclination']])
    position = profile['radius'] * np.array([np.cos(node), np.sin(node), 0.])
    direction = np.array([-np.sin(node)*np.cos(tilt), np.cos(node)*np.cos(tilt), np.sin(tilt)])
    circular_speed = hamiltonian.potential.circular_velocity(position*u.kpc).to_value(u.km/u.s)[0]
    velocity = direction * circular_speed * profile['speed_fraction']
    return gd.PhaseSpacePosition(pos=position*u.kpc, vel=velocity*u.km/u.s)


def integrate_profile(profile, index, duration, n_particles, local, hamiltonian):
    mass = profile['mass']*u.Msun
    progenitor = gp.PlummerPotential(m=mass, b=profile['scale_pc']*u.pc, units=galactic)
    df = ms.FardalStreamDF(gala_modified=True, random_state=np.random.RandomState(SEED + index))
    generator = ms.MockStreamGenerator(df, hamiltonian, progenitor_potential=progenitor)
    initial = initial_state(profile, hamiltonian)
    snapshots = local/f"{profile['id']}.h5"
    per_tail = n_particles * (2 if profile['kind'] == 'dwarf' else 1)
    stream, _ = generator.run(
        initial, mass, dt=1*u.Myr, n_steps=duration,
        release_every=RELEASE_EVERY, n_particles=per_tail,
        output_every=FRAME_STEP, output_filename=str(snapshots),
        overwrite=True, progress=False,
        Integrator_kwargs={'atol':1e-10, 'rtol':1e-10})
    with h5py.File(snapshots) as handle:
        positions = handle['stream/pos'][:].transpose(1, 2, 0)
        core = handle['nbody/pos'][:, :, 0].T
        velocity = handle['nbody/vel'][:, :, 0].T
        times = handle['stream/time'][:]
    release_time = stream.release_time.to_value(u.Myr)
    active = times[:, None] >= release_time[None, :] - 1e-8
    combined = np.concatenate((core[:, None, :], positions), axis=1)
    live = np.column_stack((np.ones(len(times), dtype=bool), active))
    assert np.isfinite(combined[live]).all()
    assert np.all(np.diff(live.sum(axis=1)) >= 0)
    phase = gd.PhaseSpacePosition(pos=core.T*u.kpc, vel=velocity.T*u.kpc/u.Myr)
    energy = hamiltonian.energy(phase).value
    energy_drift = float(np.ptp(energy)/abs(np.median(energy)))
    assert energy_drift < 1e-6, (profile['id'], energy_drift)
    counts = {tail:int(np.sum(stream.lead_trail == tail)) for tail in ['l', 't']}
    assert counts['l'] == counts['t'] and counts['l'] > 0
    radii = np.linalg.norm(core, axis=1)
    info = {
        'id':profile['id'], 'kind':profile['kind'], 'label':profile['label'],
        'massMsun':profile['mass'], 'plummerScalePc':profile['scale_pc'],
        'seed':SEED + index,
        'orbit':{'initialPositionKpc':initial.xyz.to_value(u.kpc).tolist(),
                 'initialVelocityKms':initial.v_xyz.to_value(u.km/u.s).tolist(),
                 'initialInclinationDeg':profile['inclination'], 'nodeDeg':profile['node'],
                 'speedFraction':profile['speed_fraction'],
                 'minimumRadiusKpc':float(radii.min()), 'maximumRadiusKpc':float(radii.max())},
        'validation':{'coreRelativeEnergyDrift':energy_drift, 'particlesPerTail':counts['l']},
    }
    print(json.dumps({'id':profile['id'], 'particles':combined.shape[1], **info['validation']}), flush=True)
    return combined, live, times, ['core']+stream.lead_trail.tolist(), [0]+np.rint(release_time).astype(int).tolist(), info


def generate(duration=3000, n_particles=1, output=None):
    if duration <= 0 or duration % FRAME_STEP or n_particles < 1:
        raise ValueError('Duration must be a positive multiple of 10 Myr; particles must be positive')
    local = ROOT / '.local/stream-model/population'
    output = Path(output) if output else ROOT / 'assets/data'
    local.mkdir(parents=True, exist_ok=True)
    output.mkdir(parents=True, exist_ok=True)
    hamiltonian, halo_mass = milky_way()
    all_positions, all_live, tails, releases, streams = [], [], [], [], []
    offset = 0
    for index, profile in enumerate(PROFILES):
        combined, live, times, tail, release, info = integrate_profile(
            profile, index, duration, n_particles, local, hamiltonian)
        info.update(coreIndex=offset, particleStart=offset+1, particleCount=combined.shape[1]-1)
        offset += combined.shape[1]
        all_positions.append(combined)
        all_live.append(live)
        tails.extend(tail)
        releases.extend(release)
        streams.append(info)
    combined = np.concatenate(all_positions, axis=1)
    live = np.concatenate(all_live, axis=1)
    # Keep sub-parsec precision where possible, while reserving -32768 for unborn stars.
    maximum = float(np.abs(combined[live]).max())
    spatial_scale = max(.002, np.ceil(maximum/32000/.001)*.001)
    quantized = np.full(combined.shape, -32768, dtype='<i2')
    quantized[live] = np.rint(combined[live]/spatial_scale).astype('<i2')
    assert maximum/spatial_scale < 32767
    quantization_error = float(np.abs(combined[live]-quantized[live]*spatial_scale).max())
    assert quantization_error <= spatial_scale/2 + 1e-10
    assert len(tails) == len(releases) == combined.shape[1]
    with gzip.GzipFile(filename=str(output/'tidal-stream.bin.gz'), mode='wb', mtime=0) as handle:
        handle.write(quantized.tobytes(order='C'))
    metadata = {
        'schemaVersion':2,
        'format':'little-endian int16, frame/particle/xyz; each stream core then tails; -32768 = unreleased',
        'scaleKpc':spatial_scale, 'frameCount':len(times), 'particleCount':combined.shape[1],
        'frameStepMyr':FRAME_STEP, 'durationMyr':duration, 'releaseEveryMyr':RELEASE_EVERY,
        'tail':tails, 'releaseMyr':releases, 'streams':streams,
        'colors':{'leading':'#add2ff', 'trailing':'#f1cf9a'},
        'galaVersion':gala.__version__, 'seed':SEED,
        'model':'Fixed Hernquist bulge + Miyamoto-Nagai disk + spherical NFW halo; Vc(8.2 kpc)=232 km/s',
        'haloMassMsun':halo_mass,
        'validation':{'maximumQuantizationErrorKpc':quantization_error,
                      'maximumCoordinateKpc':maximum,
                      'maximumCoreRelativeEnergyDrift':max(s['validation']['coreRelativeEnergyDrift'] for s in streams)},
    }
    (output/'tidal-stream.json').write_text(json.dumps(metadata, separators=(',', ':'))+'\n')
    np.savez_compressed(local/'diagnostics.npz', positions=combined.astype('f4'), times=times, active=live,
                        coreIndices=np.array([s['coreIndex'] for s in streams]))
    make_diagnostic(combined, streams, local, duration)
    print(json.dumps({'streams':len(streams), 'frames':len(times), 'particles':combined.shape[1],
                      'gzBytes':(output/'tidal-stream.bin.gz').stat().st_size, **metadata['validation']}, indent=2))


def make_diagnostic(positions, streams, local, duration):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(13, 8), layout='constrained')
    for i, stream in enumerate(streams):
        ax = fig.add_subplot(2, 3, i+1, projection='3d')
        start, count, core_index = stream['particleStart'], stream['particleCount'], stream['coreIndex']
        p = positions[-1, start:start+count]
        ax.scatter(*p.T, s=.4, alpha=.5, color='#4f83bb')
        ax.scatter(*positions[-1, core_index], s=15, color='#c79443')
        ax.plot(*positions[:, core_index].T, color='#8e959f', lw=.5, alpha=.65)
        mass = stream['massMsun']
        ax.set(xlabel='x [kpc]', ylabel='y [kpc]', zlabel='z [kpc]',
               title=f"{stream['id']}: {mass:g} Msun, {duration/1000:g} Gyr")
        ax.set(xlim=(-32,32), ylim=(-32,32), zlim=(-32,32))
        ax.set_box_aspect((1,1,1))
    fig.savefig(local/'streams-diagnostic.png', dpi=145)
    plt.close(fig)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--duration', type=int, default=3000)
    parser.add_argument('--particles-per-tail', type=int, default=1)
    parser.add_argument('--output-directory', type=Path)
    args = parser.parse_args()
    generate(args.duration, args.particles_per_tail, args.output_directory)
