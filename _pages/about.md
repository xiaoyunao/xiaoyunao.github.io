---
permalink: /
layout: home
title: "Yun-Ao Xiao"
seo_title: "Yun-Ao Xiao (Yunao Xiao) | Astronomy"
excerpt: "Yun-Ao Xiao (Yunao Xiao, 肖云奥, xiaoyunao), astronomy PhD student at NAOC. Galactic science, stellar streams, astrometry, time-domain surveys, and asteroids."
author_profile: false
last_modified_at: 2026-10-27
redirect_from:
  - /about/
  - /about.html
---

<section class="stream-hero" aria-labelledby="intro-title" data-stream-model="{{ '/assets/data/tidal-stream.json' | relative_url }}" data-galaxy-texture="{{ '/images/milky-way-disk.png' | relative_url }}" data-stream-binary="{{ '/assets/data/tidal-stream.bin.gz' | relative_url }}">
<canvas id="stream-canvas" aria-label="Three-dimensional model of a star cluster and its tidal stream orbiting the Milky Way. Use the view and playback controls below."></canvas>
<div class="hero-profile shell">
<img class="profile-avatar" src="{{ '/images/cartoon_selfie.png' | relative_url }}" alt="Illustrated portrait of Yun-Ao Xiao" width="1254" height="1254">
<div><h1 id="intro-title">Yun-Ao Xiao</h1><p>肖云奥 · PhD student in Astrophysics<br>National Astronomical Observatories, Chinese Academy of Sciences</p></div>
</div>
<div class="stream-caption shell">
<div><p class="stream-caption-title">Stellar-stream dynamics</p><p>Drag to rotate the view.</p><span class="stream-load-status" role="status">Static preview</span></div>
<div class="stream-controls" hidden>
<div class="playback-row"><button type="button" id="stream-play" aria-label="Pause stream animation">Pause</button><button type="button" id="stream-view" aria-label="Change viewing angle">View</button><button type="button" id="stream-reset" aria-label="Reset viewing angle">Reset</button><output id="stream-time" for="stream-timeline">0.00 Gyr</output></div>
<label class="timeline-label sr-only" for="stream-timeline">Time since first stellar release</label><input id="stream-timeline" type="range" min="0" max="3000" step="1" value="0" aria-label="Time since first stellar release, in million years">
</div>
</div>
</section>

<div class="profile-introduction shell">
<p>I am an astronomy PhD student in the <a href="http://groups.bao.ac.cn/wsgp/">WSGP group</a> at <a href="http://www.nao.cas.cn/">NAOC</a>, supervised by Prof. <a href="http://www.bao.ac.cn/nrc/zg/202208/t20220830_6506002.html">Hu Zou</a>. My research combines wide-field imaging, astrometry and spectroscopy to study the Milky Way, alongside the development of time-domain surveys and moving-object analysis.</p>
<nav class="research-index-nav" aria-label="Research and experience"><a href="#research">Galactic science</a><a href="#time-domain">Time-domain & asteroid science</a><a href="#observing">Observing & DESI</a><a href="#skills">Skills</a></nav>
</div>

<section class="research-section shell" id="research" aria-labelledby="galactic-heading">
<header class="research-section-heading"><span class="section-number">01</span><h2 id="galactic-heading">Galactic science</h2></header>
<div class="research-row">
<div class="research-copy"><h3>Stellar streams and the Galactic halo</h3><p>I study how stellar streams trace the assembly and gravitational potential of the Milky Way. My work on <strong>Palomar 5</strong> combines deep DESI Legacy Surveys imaging, photometric member selection, distance information and corrections for spatially varying survey depth.</p><p>I measure the stream track and cross-stream width, and compare the observed morphology with dynamical stream models to investigate the inner Galactic halo. I also work with Gaia astrometry and DESI spectroscopy to connect stream morphology with stellar kinematics and populations, and am interested in dwarf galaxies and tidal structures around nearby galaxies.</p></div>
<figure class="research-figure"><a href="{{ '/images/research/pal5-structure.png' | relative_url }}"><img src="{{ '/images/research/pal5-structure.png' | relative_url }}" alt="Stellar density, track, width and star counts along the Palomar 5 stream" width="1356" height="1293" loading="lazy"></a><figcaption>The structure of the Palomar 5 stellar stream.</figcaption></figure>
</div>
<div class="research-row">
<div class="research-copy"><h3>Deep proper motions</h3><p>My <a href="https://doi.org/10.3847/1538-3881/adb72c">SDSS–DESI proper-motion work</a> uses imaging separated by roughly 13 years, with galaxies providing a stable reference frame. The catalog extends to approximately <em>r</em> = 23 over 12,589 square degrees, complementing Gaia at faint magnitudes.</p><p>I use these measurements with photometric and spectroscopic information to identify distant stellar populations and study substructures in the Galactic halo.</p><a class="text-link" href="{{ '/publications/' | relative_url }}">Publications <span aria-hidden="true">↗</span></a></div>
<figure class="research-figure"><a href="{{ '/images/proper_motion.png' | relative_url }}"><img src="{{ '/images/proper_motion.png' | relative_url }}" alt="Sky maps of proper-motion offsets and uncertainties across the SDSS–DESI footprint" width="1202" height="746" loading="lazy"></a><figcaption>Proper-motion offsets and uncertainties across the SDSS–DESI survey footprint. <a href="https://doi.org/10.3847/1538-3881/adb72c">Xiao et al., The Astronomical Journal (2025).</a></figcaption></figure>
</div>
</section>

<section class="research-section shell" id="time-domain" aria-labelledby="asteroid-heading">
<header class="research-section-heading"><span class="section-number">02</span><h2 id="asteroid-heading">Time-domain & asteroid science</h2></header>
<p class="section-introduction">I develop observing and analysis workflows for the Xinglong 60/90 cm Schmidt telescope's SHARP survey and the GOTTA Prototype. My work covers survey planning, known- and unidentified-object searches, trail detection, astrometry and time-series photometry.</p>
<div class="method-grid">
<div><h3>Survey planning</h3><p>Dynamic field selection and repeat-visit scheduling account for target visibility, lunar geometry, accumulated sky coverage and follow-up needs. The <a href="https://github.com/xiaoyunao/ASAS">survey scheduler</a> is one part of this observing and processing system.</p></div>
<div><h3>Known-object recovery</h3><p>I match calibrated image catalogs to predicted asteroid positions, reject stationary-source contamination, and combine detections with orbital and observing geometry to evaluate the recovered sample and measurement quality.</p></div>
<div><h3>Searches for unidentified moving sources</h3><p>I search repeated observations for objects moving against the background stars, connect their detections into trajectories, and use follow-up observations to establish their identities and orbits.</p></div>
<div><h3>Trails and physical characterization</h3><p>I develop methods to detect and measure trailed sources, accounting for their motion during an exposure. Calibrated light curves and period analysis support studies of asteroid rotation and the monitoring of possible activity.</p></div>
</div>
<div class="paper-figure-grid">
<figure class="research-figure"><a href="{{ '/images/research/gotta-known-asteroids.png' | relative_url }}"><img src="{{ '/images/research/gotta-known-asteroids.png' | relative_url }}" alt="A GOTTA Prototype exposure with recovered asteroids marked and four corresponding image cutouts" width="1221" height="612" loading="lazy"></a><figcaption>Asteroids observed by the GOTTA Prototype.</figcaption></figure>
<figure class="research-figure"><a href="{{ '/images/research/gotta-lightcurves.png' | relative_url }}"><img src="{{ '/images/research/gotta-lightcurves.png' | relative_url }}" alt="Two asteroid rotation light curves" width="1284" height="495" loading="lazy"></a><figcaption>Asteroid rotation light curves.</figcaption></figure>
</div>
<div class="asteroid-gallery" aria-label="Asteroids moving across successive exposures">
<figure><img src="{{ '/images/research/asteroid-01.gif' | relative_url }}" alt="Moving object in successive observations, sequence 1" width="485" height="485" loading="lazy"></figure>
<figure><img src="{{ '/images/research/asteroid-02.gif' | relative_url }}" alt="Moving object in successive observations, sequence 2" width="485" height="485" loading="lazy"></figure>
<figure><img src="{{ '/images/research/asteroid-03.gif' | relative_url }}" alt="Moving object in successive observations, sequence 3" width="485" height="485" loading="lazy"></figure>
<figure><img src="{{ '/images/research/asteroid-04.gif' | relative_url }}" alt="Moving object in successive observations, sequence 4" width="485" height="485" loading="lazy"></figure>
</div>
<p class="gallery-caption">Moving objects in successive observations.</p>
<div class="research-text-columns"><div><h3>Jupiter Trojan monitoring</h3><p>We are preparing a monitoring program for <strong>Jupiter Trojans</strong>, using repeated photometry to study rotation periods and light-curve amplitudes. Current preparation focuses on observing windows, cadence, cross-night photometric consistency and period ambiguities.</p></div><div><h3>Time-domain applications</h3><p>The repeated imaging also supports the development of calibrated light curves and image-subtraction analyses for variable and transient sources. For active asteroids, I am interested in combining photometric changes, image morphology and orbital context to investigate the onset and evolution of activity.</p></div></div>
</section>

<section class="research-section shell" id="observing" aria-labelledby="observing-heading">
<header class="research-section-heading"><span class="section-number">03</span><h2 id="observing-heading">Observing experience & DESI collaboration</h2></header>
<div class="research-text-columns"><div><h3>Observations and survey data</h3><p>My observing experience includes telescopes in China, the 200-inch Hale Telescope (<a href="https://sites.astro.caltech.edu/palomar/about/telescopes/hale.html">P200</a>), and the <a href="https://noirlab.edu/public/images/noirlab2513a/">Víctor M. Blanco 4-meter Telescope</a> at Cerro Tololo in Chile, where I observed with DECam for the <a href="https://arxiv.org/abs/2509.26467">Intermediate-Band Imaging Survey (IBIS)</a>. I have also worked with data from the <a href="https://noirlab.edu/public/programs/kitt-peak-national-observatory/bok-telescope/">Bok 2.3-meter Telescope</a>.</p><p>I contribute to imaging and photometric pipelines for <a href="http://groups.bao.ac.cn/csst/ktjj/">CSST</a>, <a href="http://www.swifar.ynu.edu.cn/info/1015/1073.htm">Mephisto</a> and the Xinglong 60/90 cm Schmidt telescope, including calibration, source measurement, catalog matching and quality assessment.</p></div><div><h3>DESI, DESI-2 and IBIS</h3><p>I participate in the <a href="https://www.desi.lbl.gov/">DESI collaboration</a> through observations and survey-data analysis. Within the Milky Way Survey Working Group, my interests include stellar streams and Galactic structure, combining spectroscopy with imaging and astrometry.</p><p>Our group also participates in <a href="https://arxiv.org/abs/2209.03585">DESI-2</a> and <a href="https://arxiv.org/abs/2509.26467">IBIS</a>. IBIS medium-band DECam imaging supports the selection of high-redshift galaxies for spectroscopic studies. My collaborative work also includes DESI galaxy and active-galactic-nucleus studies.</p></div></div>
</section>

<section class="research-section shell" id="skills" aria-labelledby="skills-heading">
<header class="research-section-heading"><span class="section-number">04</span><h2 id="skills-heading">Skills</h2></header>
<div class="skill-list">
<article class="skill-item"><h3>Scientific computing</h3><p>I work primarily in Python for scientific analysis, visualization and pipeline development, from exploring individual observations to processing large survey catalogs. I routinely work in Linux environments and use NERSC for large datasets and computationally intensive analyses. I also use Java for software development, HTML for web content and LaTeX for scientific writing, bringing these tools together to develop research software and present its results.</p></article>
<article class="skill-item"><h3>Survey pipelines</h3><p>I develop imaging and photometric pipelines for CSST, Mephisto and the Xinglong 60/90 cm Schmidt telescope, covering image calibration, astrometry, source measurement, catalog matching and quality assessment. For SHARP and GOTTA, I work across survey scheduling, known-object matching, searches for unidentified moving sources, and the detection and measurement of trailed objects. I connect these processing stages to calibrated light curves, period analysis and the scientific interpretation of repeated observations.</p></article>
<article class="skill-item"><h3>AI-assisted development</h3><p>I incorporate AI coding tools and agents into my research software workflow, using them to develop task plans, implement and debug code, organize literature and maintain documentation. I connect agents to command-line tools and existing analysis pipelines so they can work through tasks within the computing environments I already use. I also use these workflows to automate repetitive processing and support the continued development and maintenance of my research projects.</p></article>
<article class="skill-item"><h3>Instrumentation</h3><p>I participated in the development and testing of imaging detectors for the Cherenkov telescopes of <a href="http://english.ihep.cas.cn/lhaaso/">LHAASO</a> during my undergraduate studies, gaining experience in instrumentation for high-energy astronomy and cosmic-ray research. I also have hands-on observing experience with optical telescopes in China, the 200-inch Hale Telescope and Blanco/DECam. These experiences connect my work on detectors and observations with the calibration, measurement and analysis of astronomical data.</p></article>
</div>
</section>
