'use strict';

/* ── Utils ─────────────────────────────── */
function debounce(fn, delay) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

function getCsrfToken() {
  const el = document.querySelector('[name=csrfmiddlewaretoken]');
  return el ? el.value : '';
}

function closeAll() {
  document.querySelectorAll('.np-dropdown').forEach(d => (d.innerHTML = ''));
}

/* ── Color swatch picker ─────────────────── */
function initColorSwatches() {
  const swatches = document.querySelectorAll('.swatch');
  if (!swatches.length) return;

  const heroImg = document.getElementById('hero-shoe-img');
  const colorNameDisplay = document.getElementById('color-name-display');
  const colorImages = document.querySelectorAll('[data-color-id]');

  swatches.forEach(btn => {
    btn.addEventListener('click', () => {
      const id = btn.dataset.colorId;
      const name = btn.dataset.colorName;
      const imgSrc = btn.dataset.colorImg;

      swatches.forEach(s => {
        s.classList.remove('is-active');
        s.setAttribute('aria-checked', 'false');
      });
      btn.classList.add('is-active');
      btn.setAttribute('aria-checked', 'true');

      if (colorNameDisplay) colorNameDisplay.textContent = name;
      if (heroImg) heroImg.src = imgSrc;

      colorImages.forEach(img => {
        img.classList.toggle('is-hidden', img.dataset.colorId !== id);
      });

      syncFormColor(id, name, btn.style.backgroundColor);
    });
  });

  // Set initial color in form
  const first = swatches[0];
  if (first) {
    syncFormColor(first.dataset.colorId, first.dataset.colorName, first.style.backgroundColor);
  }
}

function syncFormColor(id, name, hex) {
  const hiddenInput = document.getElementById('id_shoe_color');
  const dotEl = document.getElementById('form-color-dot');
  const nameEl = document.getElementById('form-color-name-text');

  if (hiddenInput) hiddenInput.value = id;
  if (dotEl) dotEl.style.background = hex;
  if (nameEl) nameEl.textContent = name;
}

/* ── Size buttons ─────────────────────────── */
function initSizeButtons() {
  const sizeBtns = document.querySelectorAll('.size-btn');
  const hiddenInput = document.getElementById('size-hidden-input');
  if (!sizeBtns.length) return;

  sizeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      sizeBtns.forEach(b => b.classList.remove('is-selected'));
      btn.classList.add('is-selected');
      if (hiddenInput) hiddenInput.value = btn.dataset.size;
    });
  });
}

/* ── Nova Poshta city autocomplete ─────────── */
function initCityAutocomplete() {
  const cityInput = document.getElementById('city-input');
  const cityRefInput = document.getElementById('city-ref');
  const cityDropdown = document.getElementById('city-dropdown');

  if (!cityInput || !cityDropdown) return;

  const fetchCities = debounce(async (query) => {
    if (query.length < 2) {
      cityDropdown.innerHTML = '';
      return;
    }
    try {
      const res = await fetch('/api/np/cities/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCsrfToken(),
        },
        body: JSON.stringify({ query }),
      });
      const html = await res.text();
      cityDropdown.innerHTML = html;
      bindCityOptions();
    } catch (_) {
      cityDropdown.innerHTML = '';
    }
  }, 300);

  cityInput.addEventListener('input', (e) => {
    if (cityRefInput) cityRefInput.value = '';
    fetchCities(e.target.value.trim());
  });

  function bindCityOptions() {
    cityDropdown.querySelectorAll('.np-option[data-ref]').forEach(btn => {
      btn.addEventListener('click', () => {
        cityInput.value = btn.dataset.name;
        if (cityRefInput) cityRefInput.value = btn.dataset.ref;
        cityDropdown.innerHTML = '';
      });
    });
  }
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

    // Move any current --active to --prev so it stays fully visible underneath.
    // Clean up any lingering --prev listeners from a previous transition first.
    pictures.forEach(p => {
      if (p.classList.contains('bg-img--active')) {
        p.classList.remove('bg-img--active');
        p.classList.add('bg-img--prev');
      }
    });

    // Bring the new image on top with a fade-in.
    incoming.classList.remove('bg-img--prev');
    incoming.classList.add('bg-img--active');
    activeIdx = idx;

    // Once the new image has finished fading in, retire the --prev backdrop.
    // Use { once: true } so the handler auto-removes itself.
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

/* ── Close dropdowns on outside click ─────── */
function initDropdownDismiss() {
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.form-field')) {
      closeAll();
    }
  });
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

/* ── HTMX re-init after swap ─────────────── */
document.addEventListener('htmx:afterSwap', () => {
  initColorSwatches();
  initSizeButtons();
  initCityAutocomplete();
});

/* ── Init ─────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  initScrollButtons();
  initColorSwatches();
  initSizeButtons();
  initCityAutocomplete();
  initDropdownDismiss();
  initBgGallery();
});
