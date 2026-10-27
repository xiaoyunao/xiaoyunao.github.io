(() => {
  const toggle = document.querySelector('.menu-toggle');
  const links = document.querySelector('.navigation-links');
  if (!toggle || !links) return;
  toggle.hidden = false;
  document.documentElement.classList.add('navigation-ready');
  const closeMenu = () => {
    toggle.setAttribute('aria-expanded', 'false');
    links.classList.remove('is-open');
  };
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(open));
    links.classList.toggle('is-open', open);
  });
  links.addEventListener('click', event => {
    if (event.target.closest('a')) closeMenu();
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      closeMenu();
      toggle.focus();
    }
  });
  document.addEventListener('click', event => {
    if (!event.target.closest('.site-nav')) closeMenu();
  });
  window.matchMedia('(min-width: 900px)').addEventListener('change', closeMenu);
})();
