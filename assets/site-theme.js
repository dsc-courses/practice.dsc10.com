(function () {
  'use strict';
  var root = document.documentElement;
  var key = 'dsc10-theme';
  var theme = 'light';
  try {
    var saved = localStorage.getItem(key);
    // Carry over a selection made while reviewing the original Quiz 2 prototype.
    if (saved === null) {
      saved = localStorage.getItem('dsc10-fa26-quiz2-theme');
      if (saved === 'light' || saved === 'dark') localStorage.setItem(key, saved);
    }
    if (saved === 'dark') theme = 'dark';
  } catch (_) {}
  function apply(next) {
    root.dataset.siteTheme = next;
    document.querySelectorAll('[data-theme-choice]').forEach(function (button) {
      button.setAttribute('aria-pressed', String(button.dataset.themeChoice === next));
    });
  }
  apply(theme);
  // Delegate immediately so the switch works even while deferred CDN scripts load.
  document.addEventListener('click', function (event) {
    var button = event.target.closest('[data-theme-choice]');
    if (!button) return;
    var next = button.dataset.themeChoice;
    if (next !== 'light' && next !== 'dark') return;
    apply(next);
    try { localStorage.setItem(key, next); } catch (_) {}
  });
  document.addEventListener('DOMContentLoaded', function () { apply(root.dataset.siteTheme); });
  window.addEventListener('storage', function (event) {
    if (event.key === key || event.key === null) apply(event.newValue === 'dark' ? 'dark' : 'light');
  });
})();
