(function () {
  "use strict";

  // Progress is saved per problem file, not per page. run.py tags each problem
  // heading with its source file, e.g. <h2 id="problem-3" data-src="fa25-final/q03">.
  // The same problem shown on an exam page and a lecture page has the same
  // data-src, so marking it done (or flagged) on either shows up on both,
  // and on the homepage dashboard (home-progress.js).
  //
  //   pt-done  = { "fa25-final/q03": true, ... }
  //   pt-flags = { "fa25-final/q05": true, ... }
  const DONE_KEY = "pt-done";
  const FLAGS_KEY = "pt-flags";

  // "/fa25-final/index.html" and "/fa25-final/" are the same page.
  function normalizePath(path) {
    return path.replace(/index\.html$/i, "");
  }
  const PAGE_PATH = normalizePath(location.pathname);
  // Whether the badge's per-problem list is open, remembered per page.
  const EXPANDED_KEY = "pt-expanded:" + PAGE_PATH;

  function loadJSON(k) {
    try { return JSON.parse(localStorage.getItem(k) || "{}") || {}; }
    catch { return {}; }
  }
  function saveJSON(k, v) {
    try { localStorage.setItem(k, JSON.stringify(v)); return true; } catch { return false; }
  }
  // Always read-modify-write, so changes made in another tab aren't lost.
  // Returns false if the save failed (e.g. storage full or blocked).
  function setMany(key, srcs, on) {
    const all = loadJSON(key);
    srcs.forEach((src) => { if (on) all[src] = true; else delete all[src]; });
    return saveJSON(key, all);
  }

  // A heading without data-src (a page built before this change) still gets
  // tracked, just only on this page.
  function srcOf(h) {
    return h.getAttribute("data-src") || PAGE_PATH + "#" + h.id;
  }

  // One-time move of this page's progress from the old per-page keys
  // ("progress:/fa25-final/index.html" = { "problem-3": true }) to the
  // per-problem keys, using this page's headings to map problem-N to its file.
  // The homepage moves exam and quiz progress the same way, using
  // exam-totals.json, for exams the student doesn't revisit.
  function migrateOldKeys(idToSrc) {
    try {
      const old = [];
      for (let i = 0; i < localStorage.length; i++) {
        const k = localStorage.key(i);
        const m = k && k.match(/^(progress|flags|pt-meta):(.*)$/);
        if (m && normalizePath(m[2]) === PAGE_PATH) old.push([k, m[1]]);
      }
      old.forEach(([k, kind]) => {
        if (kind !== "pt-meta") {
          const saved = loadJSON(k);
          const srcs = Object.keys(saved).filter((id) => saved[id] && idToSrc[id]).map((id) => idToSrc[id]);
          // Keep the old key if the new one couldn't be saved.
          if (!setMany(kind === "progress" ? DONE_KEY : FLAGS_KEY, srcs, true)) return;
        }
        localStorage.removeItem(k);
      });
    } catch {}
  }

  function init() {
    // Skip pages where tracking doesn't belong: discussions, problem sets, the pretest.
    // Lecture pages keep it, since their problems count toward the exams they came from.
    if (/\/(disc\d+|probset\d+|pretest)\//.test(location.pathname)) return;

    const trackable = Array.from(document.querySelectorAll('h2[id^="problem-"]'));
    if (!trackable.length) return;

    const idToSrc = {};
    trackable.forEach((h) => { idToSrc[h.id] = srcOf(h); });
    // Only migrate once the page has its data-src tags. A page cached from
    // before this change would otherwise move progress to page-only fallback
    // keys that stop matching once the fresh page loads.
    if (trackable.every((h) => h.hasAttribute("data-src"))) migrateOldKeys(idToSrc);
    const pageSrcs = trackable.map(srcOf);

    let done = loadJSON(DONE_KEY);
    let flags = loadJSON(FLAGS_KEY);

    const badge = document.createElement("div");
    badge.id = "pt-badge";
    document.body.appendChild(badge);

    function allDone() {
      return trackable.every((h) => done[srcOf(h)]);
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
      trackable[0].parentNode.insertBefore(wrap, trackable[0]);
    }

    function refreshBulkBtn() {
      const undo = allDone();
      bulkBtn.textContent = undo ? "Unmark all" : "Mark all complete";
      bulkBtn.classList.toggle("pt-bulk-undo", undo);
    }

    // Make every heading's buttons match the saved state.
    function paint() {
      trackable.forEach((h) => {
        const isDone = !!done[srcOf(h)];
        const isFlagged = !!flags[srcOf(h)];
        h.classList.toggle("pt-done", isDone);
        h.classList.toggle("pt-flagged", isFlagged);
        const check = h.querySelector(".pt-check");
        if (check) {
          check.classList.toggle("pt-check-on", isDone);
          check.setAttribute("aria-pressed", String(isDone));
        }
        const flag = h.querySelector(".pt-flag");
        if (flag) flag.classList.toggle("pt-flag-on", isFlagged);
      });
      renderBadge();
      refreshBulkBtn();
    }

    function reload() {
      done = loadJSON(DONE_KEY);
      flags = loadJSON(FLAGS_KEY);
      paint();
    }

    bulkBtn.addEventListener("click", () => {
      setMany(DONE_KEY, pageSrcs, !allDone());
      reload();
    });

    function renderBadge() {
      let doneCount = 0, flagged = 0;
      trackable.forEach((h) => {
        if (done[srcOf(h)]) doneCount++;
        if (flags[srcOf(h)]) flagged++;
      });
      const total = trackable.length;
      const pct = total ? Math.round((doneCount / total) * 100) : 0;
      // Per-problem list, shown above the summary when expanded. It follows
      // the headings' current order and numbers, which the sort menu on
      // lecture pages can change.
      const inPageOrder = trackable.slice().sort((a, b) =>
        (a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING) ? -1 : 1);
      const problemRows = inPageOrder.map((h) => {
        const t = h.firstChild;
        const shown = t && t.nodeType === 3 && t.nodeValue.match(/Problem \d+/);
        const label = shown ? shown[0] : "Problem " + ((h.id.match(/\d+/) || ["?"])[0]);
        const isDone = !!done[srcOf(h)];
        const isFlag = !!flags[srcOf(h)];
        const cls = "pt-item" + (isDone ? " pt-item-done" : "") + (isFlag ? " pt-item-flag" : "");
        return (
          '<a class="' + cls + '" href="#' + h.id + '">' +
            '<span class="pt-item-label">' + label + '</span>' +
            (isFlag ? '<span class="pt-flag-icon pt-item-flag-icon" aria-hidden="true"></span>' : '') +
          '</a>'
        );
      }).join("");

      badge.innerHTML =
        '<div class="pt-badge-list">' + problemRows + '</div>' +
        '<div class="pt-badge-head">' +
          '<button type="button" class="pt-expand" aria-label="Show what\'s left" title="Show what\'s left"></button>' +
          '<span class="pt-badge-num">' + doneCount + " / " + total + "</span>" +
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
      let wasOpen = false;
      try { wasOpen = localStorage.getItem(EXPANDED_KEY) === "1"; } catch {}
      if (wasOpen) setExpanded(true);
    }

    function setExpanded(on) {
      badge.classList.toggle("pt-expanded", on);
      try { localStorage.setItem(EXPANDED_KEY, on ? "1" : "0"); } catch {}
    }

    trackable.forEach((h) => {
      const src = srcOf(h);

      const doneBtn = document.createElement("button");
      doneBtn.type = "button";
      doneBtn.className = "pt-check";
      doneBtn.title = "Mark complete";
      doneBtn.setAttribute("aria-label", "Mark complete");
      doneBtn.innerHTML =
        '<span class="pt-check-icon" aria-hidden="true"></span>' +
        '<span class="pt-check-mark">Mark done</span>';
      h.appendChild(doneBtn);
      doneBtn.addEventListener("click", () => {
        setMany(DONE_KEY, [src], !done[src]);
        reload();
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
      flagBtn.addEventListener("click", () => {
        setMany(FLAGS_KEY, [src], !flags[src]);
        reload();
      });
    });

    paint();

    // The same problem can be marked on another page. Pressing Back shows this
    // page from the browser's back/forward cache without re-running this
    // script, and another tab can change progress at any time, so re-read.
    window.addEventListener("pageshow", (e) => { if (e.persisted) reload(); });
    // Lecture pages: the sort menu reorders and renumbers problems.
    const sortSelect = document.getElementById("lec-sort-select");
    if (sortSelect) sortSelect.addEventListener("change", () => setTimeout(renderBadge, 0));
    window.addEventListener("storage", (e) => {
      if (!e.key || e.key === DONE_KEY || e.key === FLAGS_KEY) reload();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
