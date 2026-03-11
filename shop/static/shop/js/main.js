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
  const warehouseInput = document.getElementById('warehouse-input');
  const warehouseRefInput = document.getElementById('warehouse-ref');
  const warehouseDropdown = document.getElementById('warehouse-dropdown');

  if (!cityInput) return;

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
    cityRefInput.value = '';
    warehouseInput.value = '';
    warehouseInput.placeholder = 'Оберіть місто спочатку';
    warehouseRefInput.value = '';
    warehouseDropdown.innerHTML = '';
    fetchCities(e.target.value.trim());
  });

  function bindCityOptions() {
    cityDropdown.querySelectorAll('.np-option[data-ref]').forEach(btn => {
      btn.addEventListener('click', async () => {
        const ref = btn.dataset.ref;
        const name = btn.dataset.name;

        cityInput.value = name;
        cityRefInput.value = ref;
        cityDropdown.innerHTML = '';

        warehouseInput.value = '';
        warehouseInput.placeholder = 'Завантаження...';
        warehouseInput.removeAttribute('readonly');

        await loadWarehouses(ref);
      });
    });
  }

  async function loadWarehouses(cityRef) {
    try {
      const res = await fetch('/api/np/warehouses/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCsrfToken(),
        },
        body: JSON.stringify({ city_ref: cityRef }),
      });
      const html = await res.text();
      warehouseDropdown.innerHTML = html;
      warehouseInput.placeholder = 'Оберіть відділення';
      bindWarehouseOptions();
    } catch (_) {
      warehouseInput.placeholder = 'Помилка. Спробуйте ще раз.';
      warehouseDropdown.innerHTML = '';
    }
  }

  function bindWarehouseOptions() {
    warehouseDropdown.querySelectorAll('.np-option[data-ref]').forEach(btn => {
      btn.addEventListener('click', () => {
        const ref = btn.dataset.ref;
        const name = btn.dataset.name;

        warehouseInput.value = name;
        warehouseRefInput.value = ref;
        warehouseDropdown.innerHTML = '';
      });
    });
  }

  warehouseInput.addEventListener('focus', () => {
    const ref = cityRefInput.value;
    if (ref && !warehouseDropdown.children.length) {
      loadWarehouses(ref);
    }
  });
}

/* ── Fixed background gallery ────────────────── */
function initBgGallery() {
  const pictures = document.querySelectorAll('#bg-layer .bg-img');
  const sections = document.querySelectorAll('section[data-bg]');
  if (!pictures.length || !sections.length) return;

  let activeIdx = 0;

  function activate(idx) {
    if (idx === activeIdx) return;
    activeIdx = idx;
    pictures.forEach((p, i) =>
      p.classList.toggle('bg-img--active', i === idx)
    );
  }

  // Pick the most-visible intersecting section and activate its background
  const observer = new IntersectionObserver(
    (entries) => {
      const visible = entries
        .filter(e => e.isIntersecting)
        .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
      if (visible) activate(Number(visible.target.dataset.bg));
    },
    { root: null, threshold: 0.4 }
  );

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

/* ── HTMX re-init after swap ─────────────── */
document.addEventListener('htmx:afterSwap', () => {
  initColorSwatches();
  initSizeButtons();
  initCityAutocomplete();
});

/* ── Init ─────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  initColorSwatches();
  initSizeButtons();
  initCityAutocomplete();
  initDropdownDismiss();
  initBgGallery();
});
