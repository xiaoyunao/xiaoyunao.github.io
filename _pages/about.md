---
permalink: /
layout: home
title: "Yun-Ao Xiao"
seo_title: "Yun-Ao Xiao (Yunao Xiao) | Astronomy"
excerpt: "Yun-Ao Xiao (Yunao Xiao, 肖云奥, xiaoyunao), astronomy PhD student at NAOC. Research on stellar streams, Galactic archaeology, astrometry, and active asteroids."
author_profile: false
last_modified_at: 2026-10-27
redirect_from: 
  - /about/
  - /about.html
---

<section class="hero shell" aria-labelledby="intro-title">
<div class="hero-copy">
<p class="eyebrow">Astronomy · Galactic archaeology · Time-domain surveys</p>
<h1 id="intro-title">Yun-Ao Xiao.</h1>
<p class="hero-tagline">A moving sky.<br>A universe of questions.</p>
<p class="hero-description">PhD student at NAOC, exploring the Milky Way and the small bodies of our Solar System.</p>
<div class="button-row"><a class="button" href="#research">Explore my research</a><a class="text-link" href="{{ '/publications/' | relative_url }}">Publications <span aria-hidden="true">↗</span></a></div>
<div class="identity-line"><span lang="zh">肖云奥</span><span>Beijing, China</span></div>
</div>
<figure class="hero-portrait"><img src="{{ '/images/cartoon_selfie.png' | relative_url }}" alt="Illustrated portrait of Yun-Ao Xiao with telescopes and an observatory" width="1254" height="1254" fetchpriority="high"></figure>
</section>
<section class="about-strip shell" aria-labelledby="about-heading">
<div><p class="eyebrow">A little about me</p><h2 id="about-heading">Curiosity, calibrated.</h2></div>
<div>
<p>My name is Yun-Ao Xiao (肖云奥), a PhD student in <a href="http://groups.bao.ac.cn/wsgp/">WSGP</a> group, <a href="http://www.nao.cas.cn/">NAOC</a>. I’m working under the guidance of Prof. <a href="http://www.bao.ac.cn/nrc/zg/202208/t20220830_6506002.html">Hu Zou</a>, studying stellar streams, dwarf galaxies, and the Milky Way dark matter halo, alongside the development of asteroid survey and data-processing methods.</p>
</div>
</section>
<section class="section research-intro" id="research" aria-labelledby="research-heading">
<div class="shell">
<div class="section-heading"><p class="eyebrow">My research</p><h2 id="research-heading">From stellar streams<br>to small worlds.</h2><p>I use wide-field imaging, astrometry, and spectroscopy to study how galaxies assemble and how objects move across the sky. My work connects Galactic archaeology with the development of survey methods and data pipelines, from tracing faint stellar structures in the Milky Way to identifying and measuring asteroids in time-domain observations.</p></div>
<article class="research-feature">
<div class="stream-layout"><div><p class="eyebrow">01 / Galactic archaeology</p><h3>The Milky Way,<br>in motion.</h3><p>Stellar streams are a record of our Galaxy's past — and a way to map its invisible dark matter halo.</p></div><img class="stream-visual" src="{{ '/images/stellar-stream.svg' | relative_url }}" alt="" aria-hidden="true" width="520" height="320" loading="lazy"></div>
<div class="full-copy">
<p>Stellar streams preserve the history of disrupted star clusters and dwarf galaxies, while their orbits trace the Milky Way’s gravitational field. I combine deep imaging, Gaia astrometry, and DESI spectroscopy to identify stream members and study their spatial, kinematic, and chemical properties. A particular focus is <strong>Palomar 5</strong>, where I use clustering methods and dynamical models to investigate the stream and constrain the structure of the Galactic dark matter halo. I am also interested in dwarf galaxies and faint tidal substructures around nearby galaxies.</p>
</div>
</article>
</div>
</section>
<section class="astrometry" aria-labelledby="astrometry-heading">
<div class="shell astrometry-grid">
<div class="astrometry-copy"><span class="research-index">02 / Survey astrometry</span><h3 id="astrometry-heading">Faint stars.<br>Measurable motion.</h3><div>
<p>Measuring the motions of faint stars opens a window onto the distant Galactic halo. In my <a href="https://doi.org/10.3847/1538-3881/adb72c">SDSS–DESI proper-motion study</a>, I combined imaging observations separated by roughly 13 years, using galaxies to establish a stable reference frame. The resulting catalog extends proper-motion measurements to approximately <em>r</em> = 23 over 12,589 square degrees, complementing Gaia at faint magnitudes. I use these measurements together with photometric and spectroscopic information to explore halo substructures and improve the selection of distant stellar populations.</p>
</div><div class="research-stats"><div><strong>~13 years</strong><span>Imaging baseline</span></div><div><strong>12,589 deg²</strong><span>Survey footprint</span></div></div></div>
<figure class="science-figure"><a href="{{ '/images/proper_motion.png' | relative_url }}"><img src="{{ '/images/proper_motion.png' | relative_url }}" alt="Sky maps of proper-motion offsets and uncertainties in the SDSS–DESI catalog" loading="lazy" width="1202" height="746"></a><figcaption>Proper-motion offsets and uncertainties across the SDSS–DESI footprint. <a href="https://doi.org/10.3847/1538-3881/adb72c">Xiao et al., The Astronomical Journal (2025) ↗</a></figcaption></figure>
</div>
</section>
<section class="asteroids shell" aria-labelledby="asteroid-heading">
<div class="asteroid-heading"><div><span class="research-index">03 / Asteroids & time-domain science</span><h3 id="asteroid-heading">Small bodies.<br>Unexpected activity.</h3></div><img class="orbit-visual" src="{{ '/images/asteroid-orbits.svg' | relative_url }}" alt="" aria-hidden="true" width="280" height="180" loading="lazy"></div>
<div class="two-column-copy"><div>
<p>I study small Solar System bodies through wide-field, time-domain observations, with a particular interest in <strong>monitoring active asteroids</strong>. Repeated imaging can reveal unexpected brightening, faint comae or dust tails, and the onset, fading, or recurrence of activity. By combining calibrated light curves with image morphology and orbital context, I aim to distinguish dust-related activity from rotational variability, changing viewing geometry, and measurement artifacts.</p>
</div><div>
<p>A key scientific goal is to understand the mechanisms that drive asteroid mass loss, including ice sublimation, impacts, and rotational instability. Monitoring activity over time and across orbital passages can help distinguish these processes and constrain dust production, activity timescales, and the survival of volatile material. These studies connect individual objects to broader questions about the physical evolution of small bodies, the asteroid–comet connection, and the distribution of water-bearing material in the Solar System.</p>

<p>To support this science, I develop survey and processing workflows for <strong>SMT and GOTTA</strong>, including adaptive scheduling, matching detections to known asteroids using predicted positions, and extracting reliable photometry of moving and trailed sources. My <a href="https://github.com/xiaoyunao/ASAS">adaptive asteroid survey scheduler</a> connects observing cadence and field selection with visibility constraints and survey coverage, supporting repeated monitoring and timely follow-up of candidate activity.</p>
</div></div>
<div class="research-note">
<p>Across these projects, I focus on careful calibration, reproducible analysis, and practical pipelines that connect large survey datasets to astrophysical questions. My collaborative work also includes CSST data-processing methods and DESI studies of galaxies and active galactic nuclei.</p>
</div>
</section>
<section class="section observing-section" aria-labelledby="observing-heading">
<div class="shell observing-grid">
<div><p class="eyebrow">From the observatory</p><h2 class="section-title" id="observing-heading">Under the<br>Chilean sky.</h2><p>Observing at Cerro Tololo.<br>Connecting survey science with the night sky.</p></div>
<div><span class="status-label">Observing visit completed</span><h3 class="observing-title">Blanco 4 m · DECam · IBIS</h3><div>
<p>I have completed an observing visit to the <strong><a href="https://noirlab.edu/public/images/noirlab2513a/">Víctor M. Blanco 4-meter Telescope</a></strong> at Cerro Tololo Inter-American Observatory in Chile, observing with <strong>DECam for the <a href="https://arxiv.org/abs/2509.26467">Intermediate-Band Imaging Survey (IBIS)</a></strong>.</p>

<p>My observing experience also includes telescopes across China and the 200-inch Hale Telescope (<a href="https://sites.astro.caltech.edu/palomar/about/telescopes/hale.html">P200</a>); I have worked with data from the <a href="https://noirlab.edu/public/programs/kitt-peak-national-observatory/bok-telescope/">UArizona Bok 2.3-meter Telescope</a>.</p>
</div></div>
</div>
</section>
<section class="section shell skills-grid" aria-labelledby="skills-heading">
<div class="skills-heading"><p class="eyebrow">Tools & practice</p><h2 class="section-title" id="skills-heading">From photons<br>to understanding.</h2><p class="skills-tags">Python / Linux / NERSC<br>Java / HTML / LaTeX<br>AI-assisted coding & agent workflows</p></div>
<div>
<details class="detail-row" open><summary>Scientific software & computing</summary><div>
<p>I work primarily in <strong>Python</strong> for scientific analysis, visualization, and pipeline development, and also use <strong>Java</strong>, <strong>HTML</strong>, and <strong>LaTeX</strong> for software development, web content, and scientific writing. I routinely work in Linux environments and use high-performance computing resources, including <strong>NERSC</strong>, to process large survey datasets and run computationally intensive analyses.</p>
</div></details>
<details class="detail-row"><summary>AI-assisted research workflows</summary><div>
<p>I incorporate <strong>AI-assisted coding and agent-based workflows</strong> into my research software practice, using them to support task planning, code development and debugging, literature organization, documentation, and repetitive data-processing tasks. My experience includes connecting agents to command-line tools and existing analysis pipelines, while reviewing generated code and checking numerical outputs against tests and scientific expectations.</p>
</div></details>
<details class="detail-row"><summary>Imaging & data-processing pipelines</summary><div>
<p>I contribute to data-processing and photometric pipeline development for the <a href="http://groups.bao.ac.cn/csst/ktjj/">Chinese Space Station Telescope (CSST)</a>, the <a href="http://www.swifar.ynu.edu.cn/info/1015/1073.htm">Multi-channel Photometric Survey Telescope (Mephisto)</a>, and the 60–90 cm Schmidt telescope. This work spans image calibration, source measurement, catalog matching, and quality assessment, with an emphasis on reproducible workflows for large imaging datasets.</p>
</div></details>
<details class="detail-row"><summary>Instrumentation & detector development</summary><div>
<p>During my undergraduate studies, I participated in the development and testing of imaging detectors for the Cherenkov telescopes of the <a href="http://english.ihep.cas.cn/lhaaso/">Large High Altitude Air Shower Observatory (LHAASO)</a>, gaining experience in instrumentation for high-energy astronomy and cosmic-ray research.</p>
</div></details>
</div>
</section>
<section class="section collaboration-section" aria-labelledby="collaboration-heading">
<div class="shell collaboration-grid"><div><p class="eyebrow">Working together</p><h2 class="section-title" id="collaboration-heading">A wider view.<br>A shared effort.</h2></div><div class="collaboration-copy">
<p>I participate in the <a href="https://www.desi.lbl.gov/">Dark Energy Spectroscopic Instrument (DESI)</a> collaboration through observations and the analysis of survey data. Within the <a href="https://desi.lbl.gov/trac/wiki/MilkyWayWG">Milky Way Survey Working Group (MWS)</a>, my interests center on stellar streams and Galactic structure, combining spectroscopy with imaging and astrometry to study stellar populations and the Milky Way’s gravitational potential.</p>

<p>Our group is also actively participating in <strong><a href="https://arxiv.org/abs/2209.03585">DESI-2 (DESI-II)</a></strong> and the <strong><a href="https://arxiv.org/abs/2509.26467">Intermediate-Band Imaging Survey (IBIS)</a></strong>. IBIS uses medium-band imaging with DECam on the Blanco telescope to help select high-redshift galaxies, including Lyman-alpha emitters and Lyman-break galaxies, for spectroscopic studies. This imaging effort supports DESI-2’s extension to higher redshift and connects survey observations and target selection to studies of large-scale structure and cosmic evolution.</p>

<p>Through these collaborations, I bring together experience in observing, imaging and spectroscopic data processing, and scientific analysis, linking my work on Galactic archaeology with broader survey science.</p>
</div></div>
</section>
<section class="section shell" aria-labelledby="papers-heading">
<div class="section-header-row"><div><p class="eyebrow">Selected work</p><h2 id="papers-heading">Ideas into papers.</h2></div><a class="text-link" href="{{ '/publications/' | relative_url }}">All publications <span aria-hidden="true">↗</span></a></div>
  {% assign selected_papers = site.publications | where: 'role', 'first-author' | sort: 'date' | reverse %}
  {% for paper in selected_papers %}
<article class="selected-paper"><div class="paper-meta"><span class="paper-status">{% if paper.status == 'preprint' %}Preprint{% else %}Published{% endif %}</span><time datetime="{{ paper.date | date: '%Y-%m-%d' }}">{{ paper.date | date: '%Y' }}</time></div><div><h3><a href="{{ paper.url | relative_url }}">{{ paper.title }}</a></h3><p>{{ paper.venue }}</p></div><a class="paper-arrow" href="{{ paper.paperurl }}" aria-label="Read {{ paper.title | escape }}"><span aria-hidden="true">↗</span></a></article>
  {% endfor %}
</section>
