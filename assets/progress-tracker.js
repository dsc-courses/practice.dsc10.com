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

  // ---- Celebrations (an easter egg) ----
  // When a page reaches 100%, the progress badge celebrates quietly (the panda
  // hops). When a click finishes every problem in a category (all quizzes, all
  // midterms, or all finals), full-screen fireworks. home-progress.js also
  // calls checkCategories() on the homepage, once per category, so a category
  // finished before this existed still gets its moment.
  // The confetti library is only downloaded for the fireworks.
  const CELEBRATED_KEY = "pt-celebrated"; // { "final": 233 } = celebrated when Finals had 233 problems
  const CONFETTI_URL = "https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js";
  const SCRIPT_SRC = (document.currentScript && document.currentScript.src) || "";

  const celebrate = (function () {
    let libPromise = null, totalsPromise = null;
    const Z = 2000; // above the navbar and the progress badge

    function lib() {
      if (window.confetti) return Promise.resolve(window.confetti);
      if (!libPromise) {
        libPromise = new Promise((resolve, reject) => {
          const s = document.createElement("script");
          s.src = CONFETTI_URL;
          s.onload = () => (window.confetti ? resolve(window.confetti) : reject());
          s.onerror = reject;
          document.head.appendChild(s);
        }).catch(() => { libPromise = null; return null; }); // offline: try again next time
      }
      return libPromise;
    }

    // exam-totals.json sits next to this script in assets/.
    function examTotals() {
      if (!totalsPromise) {
        let url = null;
        try { url = new URL("exam-totals.json", SCRIPT_SRC).href; } catch {}
        totalsPromise = url
          ? fetch(url).then((r) => (r.ok ? r.json() : {})).catch(() => ({}))
          : Promise.resolve({});
      }
      return totalsPromise;
    }

    // No confetti while the exam timer is running.
    const timerRunning = () => document.body.classList.contains("timed-running");
    const reducedMotion = () => !!(window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches);

    function categoryOf(slug) {
      if (/-quiz\d+$/i.test(slug)) return "quiz";
      if (/-midterm$/i.test(slug)) return "midterm";
      if (/-final$/i.test(slug)) return "final";
      return null;
    }

    // A quiet moment in the progress badge: the panda hops, the badge glows,
    // and "100%" reads "All done!" for a bit (styles in progress-tracker.css).
    let celebrateTimer = null;
    function pageDone() {
      if (timerRunning()) return;
      const badge = document.getElementById("pt-badge");
      if (!badge) return;
      badge.classList.remove("pt-celebrate");
      void badge.offsetWidth; // restart the animation if it's already playing
      badge.classList.add("pt-celebrate");
      clearTimeout(celebrateTimer);
      celebrateTimer = setTimeout(() => badge.classList.remove("pt-celebrate"), 2500);
    }

    // About 4 seconds of bursts across the whole screen.
    function fireworks(confetti) {
      if (reducedMotion()) {
        confetti({ particleCount: 80, spread: 100, startVelocity: 25, gravity: 1.5, ticks: 100, origin: { y: 0.6 }, zIndex: Z });
        return;
      }
      const duration = 4000, end = Date.now() + duration;
      const rand = (a, b) => a + Math.random() * (b - a);
      (function burst() {
        const left = end - Date.now();
        if (left <= 0) return;
        const particleCount = Math.round(50 * (left / duration)) + 10;
        const opts = { particleCount, startVelocity: 30, spread: 360, ticks: 70, zIndex: Z };
        confetti(Object.assign({}, opts, { origin: { x: rand(0.1, 0.3), y: rand(0.1, 0.5) } }));
        confetti(Object.assign({}, opts, { origin: { x: rand(0.7, 0.9), y: rand(0.1, 0.5) } }));
        setTimeout(burst, 250);
      })();
    }

    // Fireworks when a category (all quizzes, midterms, or finals) is fully done.
    // - After a click (newlyDone = the problems that click marked done): fire
    //   if one of them completed a category. Unmark and re-mark to see it again.
    // - On the homepage (no newlyDone): fire for a finished category only if it
    //   hasn't been celebrated at its current size, so it isn't on every visit.
    function checkCategories(knownTotals, newlyDone) {
      if (timerRunning()) return Promise.resolve();
      return (knownTotals ? Promise.resolve(knownTotals) : examTotals()).then((totals) => {
        const done = loadJSON(DONE_KEY);
        const files = {};
        Object.keys(totals || {}).forEach((slug) => {
          const cat = categoryOf(slug);
          const list = totals[slug] && totals[slug].problems;
          if (!cat || !Array.isArray(list) || !list.length) return;
          (files[cat] = files[cat] || []).push(...list);
        });
        const seen = loadJSON(CELEBRATED_KEY);
        const finished = Object.keys(files).filter((cat) => {
          if (!files[cat].every((f) => done[f])) return false;
          return newlyDone
            ? newlyDone.some((f) => files[cat].includes(f))
            : seen[cat] !== files[cat].length;
        });
        if (!finished.length) return;
        return lib().then((confetti) => {
          if (!confetti) return; // couldn't load: leave it uncelebrated, try again later
          finished.forEach((cat) => { seen[cat] = files[cat].length; });
          saveJSON(CELEBRATED_KEY, seen);
          fireworks(confetti);
        });
      });
    }

    return { pageDone, checkCategories };
  })();
  window.ptCelebrate = celebrate;

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

    // After a "done" change: confetti if this page just reached 100%, and
    // fireworks if the problems just marked finished a whole category.
    function afterDoneChange(wasAllDone, newlyDone) {
      reload();
      if (!wasAllDone && allDone()) celebrate.pageDone();
      if (newlyDone.length) celebrate.checkCategories(null, newlyDone);
    }

    bulkBtn.addEventListener("click", () => {
      const was = allDone();
      const newlyDone = was ? [] : pageSrcs.filter((s) => !done[s]);
      setMany(DONE_KEY, pageSrcs, !was);
      afterDoneChange(was, newlyDone);
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
      // lecture pages can change, and leaves out problems hidden by "Hide done".
      const inPageOrder = trackable
        .filter((h) => !(h.closest(".lec-problem") || h).classList.contains("pt-hidden"))
        .sort((a, b) => (a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING) ? -1 : 1);
      const problemRows = !inPageOrder.length
        ? '<span class="pt-item">Nothing left on this page</span>'
        : inPageOrder.map((h) => {
        const t = h.firstChild;
        // \s+: pandoc can wrap the heading's line between "Problem" and the number.
        const shown = t && t.nodeType === 3 && t.nodeValue.match(/Problem\s+(\d+)/);
        const label = "Problem " + (shown ? shown[1] : (h.id.match(/\d+/) || ["?"])[0]);
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
        const was = allDone();
        const marking = !done[src];
        setMany(DONE_KEY, [src], marking);
        afterDoneChange(was, marking ? [src] : []);
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

    // Lecture pages only: a "Hide done" checkbox next to the sort menu.
    // - The page shows only what's left: visible problems are numbered 1, 2, 3, …
    //   in the current sort order, and the badge's dropdown lists only them.
    //   Turning it off numbers every problem again.
    // - The filter is applied when the box is ticked, when the page loads, when
    //   you come back to the page, and when you change the sort (after the sort
    //   script has reordered and numbered everything). A problem you mark done
    //   while reading stays visible until then, so it doesn't vanish under you.
    const sortSelect = document.getElementById("lec-sort-select");
    const sortBox = sortSelect && sortSelect.closest(".lec-sort-box");
    let applyHide = () => {};
    if (sortBox) {
      const HIDE_KEY = "pt-hide-done-lectures";
      let hideDone = false;
      try { hideDone = localStorage.getItem(HIDE_KEY) === "1"; } catch {}

      const toggle = document.createElement("span");
      toggle.className = "pt-hide-toggle";
      toggle.innerHTML =
        '<input type="checkbox" id="pt-hide-done" autocomplete="off">' +
        '<label for="pt-hide-done">Hide done</label>' +
        '<span class="pt-hide-count" aria-live="polite"></span>';
      sortBox.appendChild(toggle);
      const box = toggle.querySelector("input");
      const count = toggle.querySelector(".pt-hide-count");
      box.checked = hideDone;

      const allHiddenNote = document.createElement("p");
      allHiddenNote.className = "pt-all-hidden";
      allHiddenNote.textContent = "You've marked every problem on this page as done. Untick “Hide done” to see them again.";
      allHiddenNote.hidden = true;
      (sortBox.closest(".lec-sort") || sortBox).insertAdjacentElement("afterend", allHiddenNote);

      const wrapperOf = (h) => h.closest(".lec-problem") || h;
      const updateCount = () => {
        const n = trackable.filter((h) => wrapperOf(h).classList.contains("pt-hidden")).length;
        count.textContent = n ? n + " hidden" : "";
        allHiddenNote.hidden = !(n && n === trackable.length);
      };
      // Number the visible problems 1, 2, 3, … in page order, the same way the
      // sort script numbers them ("Problem N" and subparts "Problem N.k").
      const renumberVisible = () => {
        let k = 0;
        document.querySelectorAll(".lec-problem").forEach((w) => {
          if (w.classList.contains("pt-hidden")) return;
          k++;
          w.querySelectorAll("h2, h3").forEach((h) => {
            const t = h.firstChild;
            if (t && t.nodeType === 3 && /^Problem\s+\d+/.test(t.nodeValue)) {
              t.nodeValue = t.nodeValue.replace(/^Problem\s+\d+/, "Problem " + k);
            }
          });
        });
      };
      applyHide = () => {
        trackable.forEach((h) => wrapperOf(h).classList.toggle("pt-hidden", hideDone && !!done[srcOf(h)]));
        renumberVisible();
        updateCount();
        renderBadge();
      };
      box.addEventListener("change", () => {
        hideDone = box.checked;
        try { localStorage.setItem(HIDE_KEY, hideDone ? "1" : "0"); } catch {}
        applyHide();
      });
      applyHide();
    }

    // The same problem can be marked on another page. Pressing Back shows this
    // page from the browser's back/forward cache without re-running this
    // script, and another tab can change progress at any time, so re-read.
    window.addEventListener("pageshow", (e) => { if (e.persisted) { reload(); applyHide(); } });
    // Lecture pages: the sort menu reorders and renumbers problems. Sorting
    // also re-applies "Hide done", so problems marked done since the last
    // refresh are hidden too (instead of showing up in new places).
    if (sortSelect) sortSelect.addEventListener("change", () => setTimeout(() => { renderBadge(); applyHide(); }, 0));
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
