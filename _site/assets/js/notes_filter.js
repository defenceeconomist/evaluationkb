(function () {
  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  ready(function () {
    const search = document.getElementById('notes-search');
    const section = document.getElementById('notes-section-filter');
    const type = document.getElementById('notes-type-filter');
    const count = document.getElementById('notes-filter-count');
    const cards = Array.from(document.querySelectorAll('[data-note-card]'));
    if (!search || !section || !type || !cards.length) return;

    function apply() {
      const q = search.value.trim().toLowerCase();
      const sectionValue = section.value;
      const typeValue = type.value;
      let visible = 0;
      for (const card of cards) {
        const text = card.textContent.toLowerCase();
        const matchesSearch = !q || text.includes(q);
        const matchesSection = sectionValue === 'all' || card.dataset.section === sectionValue;
        const matchesType = typeValue === 'all' || card.dataset.type === typeValue;
        const show = matchesSearch && matchesSection && matchesType;
        card.classList.toggle('is-hidden', !show);
        if (show) visible += 1;
      }
      if (count) count.textContent = visible + ' note' + (visible === 1 ? '' : 's') + ' shown';
    }

    search.addEventListener('input', apply);
    section.addEventListener('change', apply);
    type.addEventListener('change', apply);
    apply();
  });
})();
