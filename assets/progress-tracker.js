(function () {
  "use strict";

  const PAGE_KEY = "progress:" + location.pathname;
  const FLAG_KEY = "flags:" + location.pathname;
  const META_KEY = "pt-meta:" + location.pathname;

  function detectCategory(path) {
    if (/-final\b/i.test(path)) return "final";
    if (/-midterm\b/i.test(path)) return "midterm";
    if (/-quiz\d+\b/i.test(path)) return "quiz";
    return null;
  }

  function loadJSON(k) {
    try { return JSON.parse(localStorage.getItem(k) || "{}"); }
    catch { return {}; }
  }
  function saveJSON(k, v) {
    try { localStorage.setItem(k, JSON.stringify(v)); } catch {}
  }
  const loadState = () => loadJSON(PAGE_KEY);
  const saveState = (s) => saveJSON(PAGE_KEY, s);
  const loadFlags = () => loadJSON(FLAG_KEY);
  const saveFlags = (f) => saveJSON(FLAG_KEY, f);

  function init() {
    const mains = Array.from(document.querySelectorAll('h2[id^="problem-"]'));
    if (!mains.length) return;

    const trackable = mains;
    const state = loadState();
    const flags = loadFlags();

    const liveIds = new Set(trackable.map((h) => h.id));
    let pruned = false;
    for (const id of Object.keys(state)) {
      if (!liveIds.has(id)) { delete state[id]; pruned = true; }
    }
    for (const id of Object.keys(flags)) {
      if (!liveIds.has(id)) { delete flags[id]; pruned = true; }
    }
    if (pruned) { saveState(state); saveFlags(flags); }

    try {
      const titleEl = document.querySelector("header#title-block-header h1.title") ||
                      document.querySelector("h1.title") ||
                      document.querySelector("h1");
      const title = titleEl ? titleEl.textContent.trim() : document.title;
      const category = detectCategory(location.pathname);
      if (category) {
        localStorage.setItem(META_KEY, JSON.stringify({
          total: trackable.length,
          title: title,
          category: category,
          path: location.pathname,
        }));
      }
    } catch {}

    const badge = document.createElement("div");
    badge.id = "pt-badge";
    document.body.appendChild(badge);

    function allDone() {
      return trackable.every((h) => state[h.id]);
    }
    const titleHdr = document.querySelector("header#title-block-header");
    const bulkBtn = document.createElement("button");
    bulkBtn.type = "button";
    bulkBtn.className = "pt-bulk-btn";
    if (titleHdr) {
      titleHdr.classList.add("pt-title-row");
      titleHdr.appendChild(bulkBtn);
    } else {
      const wrap = document.createElement("div");
      wrap.className = "pt-bulk";
      wrap.appendChild(bulkBtn);
      mains[0].parentNode.insertBefore(wrap, mains[0]);
    }

    function refreshBulkBtn() {
      const undo = allDone();
      bulkBtn.textContent = undo ? "Unmark all" : "Mark all complete";
      bulkBtn.classList.toggle("pt-bulk-undo", undo);
    }

    function doBulk() {
      const makeDone = !allDone();
      trackable.forEach((h) => {
        state[h.id] = makeDone;
        h.classList.toggle("pt-done", makeDone);
        const btn = h.querySelector(".pt-check");
        if (btn) {
          btn.classList.toggle("pt-check-on", makeDone);
          btn.setAttribute("aria-pressed", String(makeDone));
        }
      });
      saveState(state);
      renderBadge();
      refreshBulkBtn();
    }
    bulkBtn.addEventListener("click", doBulk);

    function renderBadge() {
      let done = 0, flagged = 0;
      trackable.forEach((h) => {
        if (state[h.id]) done++;
        if (flags[h.id]) flagged++;
      });
      const total = trackable.length;
      const pct = total ? Math.round((done / total) * 100) : 0;
      badge.innerHTML =
        '<div class="pt-badge-head">' +
          '<span class="pt-badge-num">' + done + " / " + total + "</span>" +
          '<span class="pt-badge-pct">' + pct + '%</span>' +
          '<button type="button" class="pt-reset" aria-label="Clear" title="Clear completion and flags on this page">×</button>' +
        '</div>' +
        '<div class="pt-bar-track"><div class="pt-bar-fill" style="width:' + pct + '%"></div></div>' +
        (flagged
          ? '<div class="pt-badge-flags">' +
              '<span class="pt-flag-icon" aria-hidden="true"></span>' +
              '<span>' + flagged + ' to review</span>' +
            '</div>'
          : '');
      badge.querySelector(".pt-reset").addEventListener("click", () => {
        if (confirm("Clear completion and flags on this page?")) {
          localStorage.removeItem(PAGE_KEY);
          localStorage.removeItem(FLAG_KEY);
          location.reload();
        }
      });
    }

    trackable.forEach((h) => {
      const doneBtn = document.createElement("button");
      doneBtn.type = "button";
      doneBtn.className = "pt-check";
      doneBtn.title = "Mark complete";
      doneBtn.setAttribute("aria-label", "Mark complete");
      doneBtn.setAttribute("aria-pressed", String(!!state[h.id]));
      doneBtn.innerHTML =
        '<span class="pt-check-icon" aria-hidden="true"></span>' +
        '<span class="pt-check-mark">Mark done</span>';
      h.appendChild(doneBtn);
      h.classList.toggle("pt-done", !!state[h.id]);
      doneBtn.classList.toggle("pt-check-on", !!state[h.id]);

      doneBtn.addEventListener("click", () => {
        const now = !state[h.id];
        state[h.id] = now;
        h.classList.toggle("pt-done", now);
        doneBtn.classList.toggle("pt-check-on", now);
        doneBtn.setAttribute("aria-pressed", String(now));
        saveState(state);
        renderBadge();
        refreshBulkBtn();
      });

      const flagBtn = document.createElement("button");
      flagBtn.type = "button";
      flagBtn.className = "pt-flag";
      flagBtn.title = "Mark for review";
      flagBtn.setAttribute("aria-label", "Mark for review");
      flagBtn.innerHTML =
        '<span class="pt-flag-icon" aria-hidden="true"></span>' +
        '<span class="pt-flag-text">Mark for review</span>';
      h.appendChild(flagBtn);
      h.classList.toggle("pt-flagged", !!flags[h.id]);
      flagBtn.classList.toggle("pt-flag-on", !!flags[h.id]);

      flagBtn.addEventListener("click", () => {
        const now = !flags[h.id];
        if (now) flags[h.id] = true; else delete flags[h.id];
        saveFlags(flags);
        h.classList.toggle("pt-flagged", now);
        flagBtn.classList.toggle("pt-flag-on", now);
        renderBadge();
      });
    });

    refreshBulkBtn();
    renderBadge();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
