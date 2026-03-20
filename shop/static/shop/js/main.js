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

/* ── Ukrainian phone mask (+380 XX XXX-XX-XX) ── */
function initPhoneMask() {
  const PREFIX = '+380';

  function formatDigits(digits) {
    const d = digits.slice(0, 9);
    if (!d.length) return PREFIX;
    let r = `${PREFIX} (${d.substring(0, 2)}`;
    if (d.length <= 2) return r;
    r += `) ${d.substring(2, 5)}`;
    if (d.length <= 5) return r;
    r += `-${d.substring(5, 7)}`;
    if (d.length <= 7) return r;
    r += `-${d.substring(7, 9)}`;
    return r;
  }

  function extractDigits(value) {
    // повертає лише цифри після +380
    const raw = value.replace(/\D/g, '');
    if (raw.startsWith('380')) return raw.slice(3);
    if (raw.startsWith('38')) return raw.slice(2);
    if (raw.startsWith('3')) return raw.slice(1);
    return raw;
  }

  function applyMask(input) {
    const pos = input.selectionStart;
    const before = input.value;
    const digits = extractDigits(before).replace(/\D/g, '').slice(0, 9);

    if (digits.length === 0) {
      input.value = '';
      return;
    }

    const formatted = formatDigits(digits);
    input.value = formatted;

    // відновити позицію курсору приблизно там само
    const diff = formatted.length - before.length;
    const newPos = Math.max(PREFIX.length + 1, Math.min(pos + diff, formatted.length));
    input.setSelectionRange(newPos, newPos);
  }

  function lockPrefix(input) {
    if (!input.value.startsWith(PREFIX)) {
      const digits = extractDigits(input.value).slice(0, 9);
      input.value = digits.length ? formatDigits(digits) : '';
    }
  }

  document.querySelectorAll('input[data-phone-mask]').forEach(input => {
    // Ініціалізація: якщо є значення (після помилки серверу) — відформатувати
    if (input.value) {
      const digits = extractDigits(input.value).slice(0, 9);
      if (digits.length) input.value = formatDigits(digits);
    }

    input.addEventListener('focus', () => {
      if (!input.value) {
        input.value = PREFIX + ' ';
        input.setSelectionRange(input.value.length, input.value.length);
      } else {
        lockPrefix(input);
      }
    });

    input.addEventListener('blur', () => {
      const digits = extractDigits(input.value);
      if (digits.length === 0) {
        input.value = '';
      }
    });

    input.addEventListener('keydown', e => {
      const pos = input.selectionStart;
      const selEnd = input.selectionEnd;
      const minPos = PREFIX.length + 1; // після "+380 "

      if (e.key === 'Backspace' && pos === selEnd) {
        if (pos <= minPos) {
          e.preventDefault();
          input.setSelectionRange(minPos, minPos);
          return;
        }
        // Пропустити форматні символи назад і видалити саме цифру
        const val = input.value;
        let p = pos;
        while (p > minPos && !/\d/.test(val[p - 1])) p--;
        if (p <= minPos) {
          e.preventDefault();
          input.setSelectionRange(minPos, minPos);
          return;
        }
        if (p < pos) {
          e.preventDefault();
          input.value = val.slice(0, p - 1) + val.slice(pos);
          input.setSelectionRange(p - 1, p - 1);
          input.dispatchEvent(new Event('input'));
          return;
        }
      }

      // Дозволити лише цифри, спецклавіші та клавіші навігації
      const allowed = [
        'Backspace', 'Delete', 'Tab', 'Escape', 'Enter',
        'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown',
        'Home', 'End',
      ];
      if (!allowed.includes(e.key) && !/^\d$/.test(e.key) && !e.ctrlKey && !e.metaKey) {
        e.preventDefault();
      }
    });

    input.addEventListener('input', () => {
      lockPrefix(input);
      applyMask(input);
    });

    input.addEventListener('paste', e => {
      e.preventDefault();
      const pasted = (e.clipboardData || window.clipboardData).getData('text');
      const allDigits = pasted.replace(/\D/g, '');

      let operatorDigits;
      if (allDigits.startsWith('380')) {
        operatorDigits = allDigits.slice(3, 12);
      } else if (allDigits.startsWith('38')) {
        operatorDigits = allDigits.slice(2, 11);
      } else if (allDigits.startsWith('0')) {
        operatorDigits = allDigits.slice(1, 10);
      } else {
        operatorDigits = allDigits.slice(0, 9);
      }

      if (operatorDigits.length) {
        input.value = formatDigits(operatorDigits.slice(0, 9));
        input.setSelectionRange(input.value.length, input.value.length);
      }
    });

    // Не дати курсору потрапити до префіксу при кліку
    input.addEventListener('click', () => {
      if (input.value && input.selectionStart < PREFIX.length + 1) {
        const pos = PREFIX.length + 1;
        input.setSelectionRange(pos, pos);
      }
    });
  });
}

/* ── Init ─────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  initScrollButtons();
  initColorSwatches();
  initBgGallery();
  initPhoneMask();
});

// Після HTMX-swap (форма може бути перемальована) — переініціалізувати маску
document.addEventListener('htmx:afterSwap', initPhoneMask);
