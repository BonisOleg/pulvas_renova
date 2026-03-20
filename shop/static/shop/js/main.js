'use strict';

/* ── Color swatch picker ─────────────────── */
function initColorSwatches() {
  const swatches = document.querySelectorAll('.swatch');
  if (!swatches.length) return;

  const colorNameDisplay = document.getElementById('color-name-display');
  const colorImages = document.querySelectorAll('[data-color-id]');

  swatches.forEach(btn => {
    if (btn.dataset.hex) btn.style.backgroundColor = btn.dataset.hex;
  });

  swatches.forEach(btn => {
    btn.addEventListener('click', () => {
      const id = btn.dataset.colorId;
      const name = btn.dataset.colorName;

      swatches.forEach(s => {
        s.classList.remove('is-active');
        s.setAttribute('aria-checked', 'false');
      });
      btn.classList.add('is-active');
      btn.setAttribute('aria-checked', 'true');

      if (colorNameDisplay) colorNameDisplay.textContent = name;

      colorImages.forEach(img => {
        if (img.tagName === 'IMG') {
          img.classList.toggle('is-hidden', img.dataset.colorId !== id);
        }
      });
    });
  });
}

/* ── Fixed background gallery ────────────────── */
function initBgGallery() {
  const pictures = document.querySelectorAll('#bg-layer .bg-img');
  const sections = Array.from(document.querySelectorAll('section[data-bg]'));
  if (!pictures.length || !sections.length) return;

  const ratios = new Map(sections.map(s => [s, 0]));
  let activeIdx = -1;

  function activate(idx) {
    if (idx === activeIdx) return;

    const incoming = pictures[idx];
    if (!incoming) return;

    pictures.forEach(p => {
      if (p.classList.contains('bg-img--active')) {
        p.classList.remove('bg-img--active');
        p.classList.add('bg-img--prev');
      }
    });

    incoming.classList.remove('bg-img--prev');
    incoming.classList.add('bg-img--active');
    activeIdx = idx;

    incoming.addEventListener('transitionend', () => {
      pictures.forEach(p => {
        if (p !== incoming) p.classList.remove('bg-img--prev');
      });
    }, { once: true });
  }

  function pickBest() {
    let best = sections[0];
    let bestRatio = -1;
    for (const s of sections) {
      const r = ratios.get(s);
      if (r > bestRatio) { bestRatio = r; best = s; }
    }
    activate(Number(best.dataset.bg));
  }

  const thresholds = Array.from({ length: 21 }, (_, i) => i / 20);
  const observer = new IntersectionObserver(entries => {
    entries.forEach(e => ratios.set(e.target, e.intersectionRatio));
    pickBest();
  }, { threshold: thresholds });

  sections.forEach(s => observer.observe(s));
}

/* ── Smooth scroll via data-scroll-to attr ── */
function initScrollButtons() {
  document.querySelectorAll('[data-scroll-to]').forEach(el => {
    el.addEventListener('click', () => {
      const target = document.getElementById(el.dataset.scrollTo);
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });
}

/* ── Init ─────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  initScrollButtons();
  initColorSwatches();
  initBgGallery();
});
