(function () {
  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  ready(function () {
    const search = document.getElementById('notes-search');
    const book = document.getElementById('notes-book-filter');
    const type = document.getElementById('notes-type-filter');
    const count = document.getElementById('notes-filter-count');
    const cards = Array.from(document.querySelectorAll('[data-note-card]'));
    if (!search || !type || !cards.length) return;

    function apply() {
      const q = search.value.trim().toLowerCase();
      const bookValue = book ? book.value : 'all';
      const typeValue = type.value;
      let visible = 0;
      for (const card of cards) {
        const text = card.textContent.toLowerCase();
        const matchesSearch = !q || text.includes(q);
        const matchesBook = bookValue === 'all' || card.dataset.book === bookValue;
        const matchesType = typeValue === 'all' || card.dataset.type === typeValue;
        const show = matchesSearch && matchesBook && matchesType;
        card.classList.toggle('is-hidden', !show);
        if (show) visible += 1;
      }
      if (count) count.textContent = visible + ' note' + (visible === 1 ? '' : 's') + ' shown';
    }

    search.addEventListener('input', apply);
    if (book) book.addEventListener('change', apply);
    type.addEventListener('change', apply);
    apply();
  });
})();
