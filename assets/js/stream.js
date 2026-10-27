/* Project physical gala snapshots into a rotatable 3D scene. */
(async () => {
  const hero = document.querySelector('.stream-hero');
  const canvas = document.getElementById('stream-canvas');
  if (!hero || !canvas) return;
  const context = canvas.getContext('2d', { alpha: false });
  if (!context) return;
  const status = hero.querySelector('.stream-load-status');
  const controls = hero.querySelector('.stream-controls');
  const play = document.getElementById('stream-play');
  const view = document.getElementById('stream-view');
  const reset = document.getElementById('stream-reset');
  const slider = document.getElementById('stream-timeline');
  const output = document.getElementById('stream-time');
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
  const views = [[-.9, .98], [-.9, .38], [0, 1.49]];
  let yaw = views[0][0], tilt = views[0][1], viewIndex = 0;
  let width = 1, height = 1, scale = 1, cx = 0, cy = 0, dpr = 1;
  let age = 1500, playing = !reducedMotion.matches, visible = true;
  let lastTime = null, raf = null, backgroundDirty = true, lastPaint = 0;
  let model, positions, particles, frames, stride;
  const background = document.createElement('canvas');
  const backdrop = background.getContext('2d', { alpha: false });
  let seed = 20261027;
  const random = () => { seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0; return seed / 4294967296; };
  const normal = () => Math.sqrt(-2 * Math.log(Math.max(random(), 1e-10))) * Math.cos(2 * Math.PI * random());
  const galaxy = [];
  // The luminous disk and bulge are schematic. Only stream coordinates are data.
  for (let i = 0; i < 14500; i++) {
    let r;
    do { r = -2.9 * Math.log(Math.max(random() * random(), 1e-10)); } while (r > 17 || r < .25);
    const inArm = r > 3.5 && random() < .72;
    const angle = inArm
      ? Math.floor(random() * 4) * Math.PI / 2 + Math.log(r / 3.5) / Math.tan(.235) + normal() * .105
      : random() * 2 * Math.PI;
    galaxy.push({ x: r * Math.cos(angle), y: r * Math.sin(angle), z: normal() * (.07 + r * .008), r,
      alpha: .18 + random() * .48, size: .35 + random() * .65,
      color: inArm && r > 4 ? [151, 177, 214] : [225, 204, 172] });
  }
  for (let i = 0; i < 3000; i++) {
    const x = normal() * 1.65, y = normal() * .8;
    galaxy.push({ x: x * .9 - y * .435, y: x * .435 + y * .9, z: normal() * .55,
      r: Math.hypot(x, y), alpha: .18 + random() * .3, size: .3 + random() * .55, color: [242, 211, 165] });
  }
  const coreStars = Array.from({ length: 100 }, () => {
    const radius = Math.min(.075, .015 / Math.sqrt(Math.max(random(), .001) ** (-2 / 3) - 1));
    const z = random() * 2 - 1, angle = random() * Math.PI * 2;
    return [radius * Math.sqrt(1 - z * z) * Math.cos(angle), radius * Math.sqrt(1 - z * z) * Math.sin(angle), radius * z];
  });
  const fieldStars = Array.from({ length: 240 }, () => [random(), random(), .25 + random() * .5, .1 + random() * .3]);
  const projection = (x, y, z) => {
    const a = Math.cos(yaw) * x - Math.sin(yaw) * y;
    const b = Math.sin(yaw) * x + Math.cos(yaw) * y;
    return [cx + a * scale, cy - (Math.cos(tilt) * b - Math.sin(tilt) * z) * scale,
      Math.sin(tilt) * b + Math.cos(tilt) * z];
  };
  const glow = (ctx, x, y, radius, rgb, opacity) => {
    const gradient = ctx.createRadialGradient(x, y, 0, x, y, radius);
    gradient.addColorStop(0, `rgba(${rgb},${opacity})`);
    gradient.addColorStop(.3, `rgba(${rgb},${opacity * .25})`);
    gradient.addColorStop(1, `rgba(${rgb},0)`);
    ctx.fillStyle = gradient; ctx.fillRect(x - radius, y - radius, radius * 2, radius * 2);
  };
  const makeBackground = () => {
    backdrop.setTransform(dpr, 0, 0, dpr, 0, 0);
    backdrop.fillStyle = '#080d18'; backdrop.fillRect(0, 0, width, height);
    for (const [x, y, radius, alpha] of fieldStars) {
      backdrop.fillStyle = `rgba(192,206,229,${alpha})`;
      backdrop.beginPath(); backdrop.arc(x * width, y * height, radius, 0, Math.PI * 2); backdrop.fill();
    }
    // Diffuse light, with the same projected disk geometry as the stars.
    backdrop.save(); backdrop.translate(cx, cy);
    backdrop.rotate(-yaw * .03); backdrop.scale(1, Math.max(.12, Math.cos(tilt)));
    glow(backdrop, 0, 0, 17 * scale, '127,145,177', .13);
    glow(backdrop, 0, 0, 4.5 * scale, '244,207,148', .25);
    backdrop.restore();
    const sorted = galaxy.map(star => ({ star, point: projection(star.x, star.y, star.z) })).sort((a, b) => a.point[2] - b.point[2]);
    for (const { star, point } of sorted) {
      const [x, y] = point;
      if (x < 0 || x > width || y < 0 || y > height) continue;
      const resolution = width < 600 ? .72 : 1;
      backdrop.fillStyle = `rgba(${star.color.join(',')},${star.alpha})`;
      backdrop.fillRect(x, y, Math.max(.45, star.size * resolution), Math.max(.45, star.size * resolution));
    }
    backgroundDirty = false;
  };
  const resize = () => {
    width = hero.clientWidth; height = hero.clientHeight;
    dpr = Math.min(devicePixelRatio || 1, 1.5);
    canvas.width = background.width = Math.round(width * dpr);
    canvas.height = background.height = Math.round(height * dpr);
    scale = Math.min(width / (width < 600 ? 47 : 50), height / 36);
    cx = width * (width < 600 ? .5 : .55); cy = height * (width < 600 ? .44 : .52);
    backgroundDirty = true; requestFrame();
  };
  const setPlayLabel = () => {
    play.textContent = age >= model.durationMyr ? 'Replay' : playing ? 'Pause' : 'Play';
    play.setAttribute('aria-label', age >= model.durationMyr ? 'Replay stream formation' : playing ? 'Pause stream animation' : 'Play stream animation');
  };
  const render = () => {
    if (!model) return;
    if (backgroundDirty) makeBackground();
    context.setTransform(dpr, 0, 0, dpr, 0, 0);
    context.drawImage(background, 0, 0, width, height);
    const frame = Math.min(frames - 1, age / model.frameStepMyr);
    const first = Math.floor(frame), second = Math.min(first + 1, frames - 1), mix = frame - first;
    const firstOffset = first * stride, secondOffset = second * stride;
    const sample = index => {
      const base = firstOffset + index * 3, next = secondOffset + index * 3;
      if (positions[base] === -32768) return null;
      return [0, 1, 2].map(axis => (positions[base + axis] * (1 - mix) + positions[next + axis] * mix) * model.scaleKpc);
    };
    const core = sample(0), projectedCore = projection(...core);
    // Position-space density is not thickened. The sub-pixel stellar markers are
    // a display convention, not physical radii or an artificial ribbon width.
    const streamPoints = [];
    for (let i = 1; i < particles; i++) {
      if (age < model.releaseMyr[i]) continue;
      const p = sample(i); if (!p) continue;
      const point = projection(...p);
      streamPoints.push({ point, tail: model.tail[i], fresh: Math.min(1, (age - model.releaseMyr[i]) / 12) });
    }
    streamPoints.sort((a, b) => a.point[2] - b.point[2]);
    for (const { point: [x, y, depth], tail, fresh } of streamPoints) {
      if (x < 0 || x > width || y < 0 || y > height) continue;
      // Mild disk extinction only when a distant stream star projects onto it.
      const r = Math.hypot((x - cx) / scale, (y - cy) / (scale * Math.max(.1, Math.cos(tilt))));
      const alpha = (depth < -2 && r < 13 ? .32 : .8) * fresh;
      context.fillStyle = tail === 'l' ? `rgba(173,210,255,${alpha})` : `rgba(241,207,154,${alpha})`;
      const radius = width < 600 ? .85 : 1.05;
      context.beginPath(); context.arc(x, y, radius, 0, Math.PI * 2); context.fill();
    }
    context.fillStyle = 'rgba(247,242,224,.3)';
    for (const delta of coreStars) {
      const [x, y] = projection(core[0] + delta[0], core[1] + delta[1], core[2] + delta[2]);
      context.fillRect(x, y, .65, .65);
    }
    const [px, py] = projectedCore;
    const labelDirection = px > width - 115 ? -1 : 1;
    context.strokeStyle = 'rgba(218,229,245,.65)'; context.lineWidth = .75;
    context.beginPath(); context.moveTo(px + labelDirection * 6, py - 4); context.lineTo(px + labelDirection * 20, py - 18); context.lineTo(px + labelDirection * 90, py - 18); context.stroke();
    context.fillStyle = '#dce6f6'; context.font = '11px -apple-system, BlinkMacSystemFont, sans-serif';
    context.textAlign = labelDirection === 1 ? 'left' : 'right';
    context.fillText('Progenitor', px + labelDirection * 25, py - 24);
    context.textAlign = 'left';
    // A physical scale bar reinforces that the galaxy and tails share one scale.
    const bar = 5 * scale, barX = Math.max(24, width * .08), barY = height * (width < 600 ? .63 : .72);
    context.strokeStyle = 'rgba(154,173,202,.55)'; context.beginPath();context.moveTo(barX, barY);context.lineTo(barX + bar, barY);context.stroke();
    context.fillStyle = '#8f9fb6';context.font = '10px -apple-system, BlinkMacSystemFont, sans-serif';context.fillText('5 kpc',barX,barY - 8);
    slider.value = String(Math.round(age)); output.textContent = `${(age / 1000).toFixed(2)} Gyr`;
    canvas.dataset.modelTimeMyr = String(Math.round(age));
  };
  function requestFrame() { if (!raf && model && visible && !document.hidden) raf = requestAnimationFrame(tick); }
  function tick(time) {
    raf = null;
    if (!visible || document.hidden) { lastTime = null; return; }
    const elapsed = lastTime === null ? 0 : Math.min(100, time - lastTime);
    lastTime = time;
    if (playing) age = Math.min(model.durationMyr, age + elapsed * .015);
    if (time - lastPaint >= 32 || !playing) { render(); lastPaint = time; }
    if (age >= model.durationMyr) { playing = false; setPlayLabel(); }
    if (playing) requestFrame();
  }
  try {
    const [metaResponse, binaryResponse] = await Promise.all([fetch(hero.dataset.streamModel), fetch(hero.dataset.streamBinary)]);
    if (!metaResponse.ok || !binaryResponse.ok) throw new Error('Model unavailable');
    model = await metaResponse.json();
    let buffer = await binaryResponse.arrayBuffer();
    const header = new Uint8Array(buffer, 0, 2);
    if (header[0] === 0x1f && header[1] === 0x8b) {
      buffer = await new Response(new Blob([buffer]).stream().pipeThrough(new DecompressionStream('gzip'))).arrayBuffer();
    }
    positions = new Int16Array(buffer); particles = model.particleCount; frames = model.frameCount; stride = particles * 3;
    if (positions.length !== frames * stride) throw new Error('Invalid snapshot dimensions');
    controls.hidden = false; status.textContent = 'Leading tail: blue · Trailing tail: amber';
    canvas.dataset.modelReady = 'true'; slider.max = String(model.durationMyr);
    setPlayLabel(); resize();
    new ResizeObserver(resize).observe(hero);
    new IntersectionObserver(entries => { visible = entries[0].isIntersecting; lastTime = null; if (visible) requestFrame(); }, { threshold: .01 }).observe(hero);
    document.addEventListener('visibilitychange', () => { lastTime = null; if (!document.hidden) requestFrame(); });
    play.addEventListener('click', () => { if (age >= model.durationMyr) age = 0; playing = !playing; lastTime = null;setPlayLabel();requestFrame(); });
    slider.addEventListener('input', () => { age = Number(slider.value);playing = false;setPlayLabel();requestFrame(); });
    view.addEventListener('click', () => { viewIndex = (viewIndex + 1) % views.length;[yaw, tilt] = views[viewIndex];backgroundDirty = true;requestFrame(); });
    reset.addEventListener('click', () => { viewIndex = 0;[yaw, tilt] = views[0];backgroundDirty = true;requestFrame(); });
    let drag = null;
    canvas.addEventListener('pointerdown', event => { drag = { x: event.clientX, y: event.clientY, yaw, tilt };canvas.setPointerCapture(event.pointerId); });
    canvas.addEventListener('pointermove', event => {
      if (!drag) return;
      yaw = drag.yaw + (event.clientX - drag.x) * .005;
      tilt = Math.min(1.5, Math.max(.12, drag.tilt + (event.clientY - drag.y) * .004));
      backgroundDirty = true;requestFrame();
    });
    const release = () => { drag = null; };
    canvas.addEventListener('pointerup', release);canvas.addEventListener('pointercancel', release);
    reducedMotion.addEventListener('change', event => { if (event.matches) { playing = false;setPlayLabel();requestFrame(); } });
  } catch (error) {
    canvas.hidden = true; controls.hidden = true; status.textContent = 'Static model view';
    console.warn('Stream preview:', error.message);
  }
})();
