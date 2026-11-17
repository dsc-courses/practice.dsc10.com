(function () {
  "use strict";

  const PAGE_KEY = "progress:" + location.pathname;
  const FLAG_KEY = "flags:" + location.pathname;
  const META_KEY = "pt-meta:" + location.pathname;
  const EXPANDED_KEY = "pt-expanded:" + location.pathname;

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
    // Skip pages where tracking doesn't belong: discussions, problem sets, lectures.
    if (/\/(disc\d+|probset\d+|lectures|pretest)\//.test(location.pathname)) return;

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
      // Per-problem list, shown above the summary when expanded.
      const problemRows = trackable.map((h) => {
        const n = (h.id.match(/\d+/) || ["?"])[0];
        const isDone = !!state[h.id];
        const isFlag = !!flags[h.id];
        const cls = "pt-item" + (isDone ? " pt-item-done" : "") + (isFlag ? " pt-item-flag" : "");
        return (
          '<a class="' + cls + '" href="#' + h.id + '">' +
            '<span class="pt-item-label">Problem ' + n + '</span>' +
            (isFlag ? '<span class="pt-flag-icon pt-item-flag-icon" aria-hidden="true"></span>' : '') +
          '</a>'
        );
      }).join("");

      badge.innerHTML =
        '<div class="pt-badge-list">' + problemRows + '</div>' +
        '<div class="pt-badge-head">' +
          '<button type="button" class="pt-expand" aria-label="Show what\'s left" title="Show what\'s left"></button>' +
          '<span class="pt-badge-num">' + done + " / " + total + "</span>" +
          '<span class="pt-badge-pct">' + pct + '%</span>' +
        '</div>' +
        '<div class="pt-bar-track"><div class="pt-bar-fill" style="width:' + pct + '%"></div></div>' +
        (flagged
          ? '<div class="pt-badge-flags">' +
              '<span class="pt-flag-icon" aria-hidden="true"></span>' +
              '<span>' + flagged + ' to review</span>' +
            '</div>'
          : '');
      badge.querySelector(".pt-expand").addEventListener("click", (e) => {
        e.stopPropagation();
        setExpanded(!badge.classList.contains("pt-expanded"));
      });
      if (localStorage.getItem(EXPANDED_KEY) === "1") setExpanded(true);
    }

    function setExpanded(on) {
      badge.classList.toggle("pt-expanded", on);
      try { localStorage.setItem(EXPANDED_KEY, on ? "1" : "0"); } catch {}
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
