(() => {
  const search = document.querySelector('#faq-search');
  const items = [...document.querySelectorAll('.faq-item')];
  const filters = [...document.querySelectorAll('.filter')];
  const count = document.querySelector('#result-count');
  const empty = document.querySelector('#empty-state');
  const clear = document.querySelector('#clear-search');
  let category = 'all';

  function applyFilters() {
    const term = search.value.trim().toLowerCase();
    let visible = 0;

    items.forEach((item) => {
      const categoryMatch = category === 'all' || item.dataset.category === category;
      const searchMatch = !term || item.textContent.toLowerCase().includes(term);
      item.hidden = !(categoryMatch && searchMatch);
      if (!item.hidden) visible += 1;
    });

    count.textContent = visible === items.length
      ? `Showing all ${visible} questions`
      : `${visible} matching question${visible === 1 ? '' : 's'}`;
    empty.hidden = visible !== 0;
  }

  filters.forEach((button) => {
    button.addEventListener('click', () => {
      category = button.dataset.category;
      filters.forEach((candidate) => {
        const active = candidate === button;
        candidate.classList.toggle('active', active);
        candidate.setAttribute('aria-pressed', String(active));
      });
      applyFilters();
    });
  });

  search.addEventListener('input', applyFilters);
  clear.addEventListener('click', () => {
    search.value = '';
    filters[0].click();
    search.focus();
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === '/' && document.activeElement !== search) {
      event.preventDefault();
      search.focus();
    }
    if (event.key === 'Escape' && document.activeElement === search) {
      search.value = '';
      applyFilters();
      search.blur();
    }
  });

  applyFilters();
})();
