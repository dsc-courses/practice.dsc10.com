(function () {
  "use strict";

  let EXAM_TOTALS = null;

  function slugFromPath(path) {
    const parts = path.split("/").filter(Boolean);
    const i = parts.lastIndexOf("index.html");
    return i >= 1 ? parts[i - 1] : parts[parts.length - 1] || "";
  }

  function prettySlug(slug) {
    return slug
      .replace(/-/g, " ")
      .replace(/\b([a-z])/g, (_, c) => c.toUpperCase());
  }

  const QUARTER_NAMES = { fa: "Fall", wi: "Winter", sp: "Spring", su: "Summer" };
  const QUARTER_ORDER = { wi: 1, sp: 2, su: 3, fa: 4 };

  function slugDateKey(slug) {
    const m = slug.match(/^([a-z]{2})(\d{2})/i);
    if (!m) return 0;
    const q = QUARTER_ORDER[m[1].toLowerCase()] || 0;
    const yr = parseInt(m[2], 10);
    return yr * 10 + q;
  }
  function quarterCode(slug) {
    const m = slug.match(/^([a-z]{2})(\d{2})/i);
    if (!m) return slug;
    const season = QUARTER_NAMES[m[1].toLowerCase()] || m[1].toUpperCase();
    return season + " 20" + m[2];
  }

  function fetchExamTotals() {
    return fetch("assets/exam-totals.json", { cache: "no-store" })
      .then((r) => r.ok ? r.json() : {})
      .catch(() => ({}));
  }

  function isHomepage() {
    return !!document.getElementById("exams") &&
           !document.querySelector('h2[id^="problem-"]');
  }

  function loadJSON(k) {
    try { return JSON.parse(localStorage.getItem(k) || "{}") || {}; }
    catch { return {}; }
  }

  // Progress is saved per problem file by progress-tracker.js:
  //   pt-done / pt-flags = { "fa25-final/q03": true, ... }
  // exam-totals.json lists each exam's problem files in page order, so a
  // problem marked on a lecture page counts for its exam too.
  const DONE_KEY = "pt-done";
  const FLAGS_KEY = "pt-flags";

  function categoryOf(slug) {
    if (/-quiz\d+$/i.test(slug)) return "quiz";
    if (/-midterm$/i.test(slug)) return "midterm";
    if (/-final$/i.test(slug)) return "final";
    return null;
  }

  // One-time move of exam and quiz progress saved by the old tracker, which
  // used per-page keys ("progress:/fa25-final/index.html" = { "problem-3": true }).
  // Problem N on an exam page is the Nth file in its exam-totals list.
  // Old keys for lecture and discussion pages are left for progress-tracker.js
  // to move the next time that page is opened.
  function migrateOldKeys() {
    try {
      const old = [];
      for (let i = 0; i < localStorage.length; i++) {
        const k = localStorage.key(i);
        const m = k && k.match(/^(progress|flags|pt-meta):(.*)$/);
        if (!m) continue;
        const slug = slugFromPath(m[2].replace(/index\.html$/i, ""));
        const entry = EXAM_TOTALS && EXAM_TOTALS[slug];
        if (entry && Array.isArray(entry.problems)) old.push([k, m[1], entry.problems]);
      }
      old.forEach(([k, kind, files]) => {
        if (kind !== "pt-meta") {
          const target = kind === "progress" ? DONE_KEY : FLAGS_KEY;
          const saved = loadJSON(k);
          const all = loadJSON(target);
          Object.keys(saved).forEach((id) => {
            const n = String(id).match(/^problem-(\d+)$/);
            const src = n && files[parseInt(n[1], 10) - 1];
            if (saved[id] && src) all[src] = true;
          });
          localStorage.setItem(target, JSON.stringify(all));
        }
        localStorage.removeItem(k);
      });
    } catch {}
  }

  function collect() {
    const done = loadJSON(DONE_KEY);
    const flags = loadJSON(FLAGS_KEY);
    const exams = [];
    Object.keys(EXAM_TOTALS || {}).forEach((slug) => {
      const category = categoryOf(slug);
      const raw = EXAM_TOTALS[slug];
      const files = (raw && Array.isArray(raw.problems)) ? raw.problems : [];
      if (!category || !files.length) return;
      exams.push({
        path: "/" + slug + "/",
        title: raw.title || "",
        category: category,
        total: files.length,
        done: files.filter((f) => done[f]).length,
        // As "problem-N" so the To review chips link to the exam page.
        flaggedIds: files
          .map((f, i) => (flags[f] ? "problem-" + (i + 1) : null))
          .filter(Boolean),
      });
    });
    return exams;
  }

  // Saved paths look like "/fa25-final/" (older ones "/fa25-final/index.html").
  // Always link relatively to "<slug>/index.html" like the rest of the homepage.
  function examHref(path) {
    return slugFromPath(path) + "/index.html";
  }

  function examEntry(slug) {
    const raw = EXAM_TOTALS ? EXAM_TOTALS[slug] : null;
    if (!raw) return null;
    if (typeof raw === "number") return { total: raw, title: "" };
    return { total: raw.total || 0, title: raw.title || "" };
  }

  function problemTotalsBySite() {
    const totals = { quiz: 0, midterm: 0, final: 0 };
    if (!EXAM_TOTALS) return totals;
    Object.keys(EXAM_TOTALS).forEach((slug) => {
      const e = examEntry(slug);
      if (!e || !e.total) return;
      if (/-quiz\d+$/i.test(slug)) totals.quiz += e.total;
      else if (/-midterm$/i.test(slug)) totals.midterm += e.total;
      else if (/-final$/i.test(slug)) totals.final += e.total;
    });
    return totals;
  }

  function render(exams) {
    const cats = [
      { key: "quiz",    label: "Quizzes",  anchor: "#quizzes" },
      { key: "midterm", label: "Midterms", anchor: "#exams"   },
      { key: "final",   label: "Finals",   anchor: "#exams"   },
    ];

    const siteTotals = problemTotalsBySite();
    const totals = {};
    cats.forEach((c) => (totals[c.key] = {
      done: 0,
      total: siteTotals[c.key] || 0,
      flagged: 0,
    }));
    exams.forEach((e) => {
      if (!totals[e.category]) return;
      totals[e.category].done += Math.min(e.done, e.total);
      totals[e.category].flagged += e.flaggedIds.length;
    });

    const examsByCat = { quiz: [], midterm: [], final: [] };
    const touched = {};
    exams.forEach((e) => {
      if (examsByCat[e.category]) {
        touched[e.path] = e;
      }
    });
    if (EXAM_TOTALS) {
      const slugs = Object.keys(EXAM_TOTALS)
        .sort((a, b) => slugDateKey(b) - slugDateKey(a));
      slugs.forEach((slug) => {
        const entry = examEntry(slug);
        if (!entry) return;
        let cat = null;
        if (/-quiz\d+$/i.test(slug)) cat = "quiz";
        else if (/-midterm$/i.test(slug)) cat = "midterm";
        else if (/-final$/i.test(slug)) cat = "final";
        if (!cat) return;
        const matched = exams.find((e) => slugFromPath(e.path) === slug);
        const done = matched ? Math.min(matched.done, entry.total) : 0;
        const flagged = matched ? matched.flaggedIds.length : 0;
        const title = (matched && matched.title) || entry.title || prettySlug(slug);
        examsByCat[cat].push({ slug, title, total: entry.total, done, flagged });
      });
    }

    const cards = cats.map((c) => {
      const t = totals[c.key];
      const pct = t.total ? Math.round((t.done / t.total) * 100) : 0;
      const renderRow = (e) => {
        const ePct = e.total ? Math.round((e.done / e.total) * 100) : 0;
        const label = quarterCode(e.slug);
        const fullTitle = e.title || prettySlug(e.slug);
        const flagMark = e.flagged > 0
          ? '<span class="hp-ex-flag" title="' + e.flagged + ' flagged for review">' +
              '<span class="hp-flag-icon" aria-hidden="true"></span>' +
              '<span class="hp-ex-flag-num">' + e.flagged + '</span>' +
            '</span>'
          : '';
        return (
          '<li class="hp-ex-row' + (e.done === 0 && e.flagged === 0 ? ' hp-ex-untouched' : '') + '">' +
            '<a href="' + e.slug + '/index.html" class="hp-ex-title" title="' + fullTitle + '">' + label + '</a>' +
            '<span class="hp-ex-meta">' + flagMark +
              '<span class="hp-ex-nums">' + e.done + ' / ' + e.total + '</span>' +
            '</span>' +
            '<div class="hp-ex-bar"><div class="hp-ex-fill" style="width:' + ePct + '%"></div></div>' +
          '</li>'
        );
      };

      let rows;
      if (c.key === "quiz") {
        const byNum = new Map();
        examsByCat[c.key].forEach((e) => {
          const m = e.slug.match(/-quiz(\d+)$/i);
          const num = m ? parseInt(m[1], 10) : 0;
          if (!byNum.has(num)) byNum.set(num, []);
          const quarter = (e.title || prettySlug(e.slug))
            .replace(/\s*Quiz\s*\d+\s*$/i, "")
            .trim();
          byNum.get(num).push({ e, quarter });
        });
        const nums = Array.from(byNum.keys()).sort((a, b) => a - b);
        rows = nums.map((n) => {
          const items = byNum.get(n)
            .map(({ e, quarter }) => renderRow(e, quarter))
            .join("");
          return (
            '<div class="hp-ex-group">' +
              '<div class="hp-ex-group-head">Quiz ' + n + '</div>' +
              '<ul class="hp-ex-group-list">' + items + '</ul>' +
            '</div>'
          );
        }).join("");
      } else {
        rows = examsByCat[c.key].map((e) => renderRow(e)).join("");
      }
      return (
        '<div class="hp-card" data-cat="' + c.key + '">' +
          '<div class="hp-card-head">' +
            '<a class="hp-card-label" href="' + c.anchor + '">' + c.label + '</a>' +
            '<span class="hp-card-pct">' + pct + '%</span>' +
          '</div>' +
          '<button type="button" class="hp-card-expand" aria-expanded="false" aria-label="Show breakdown">' +
            '<div class="hp-card-nums">' +
              '<span class="hp-card-done">' + t.done + '</span>' +
              '<span class="hp-card-of"> / ' + t.total + '</span>' +
              '<span class="hp-card-unit">questions completed</span>' +
              '<span class="hp-card-caret" aria-hidden="true"></span>' +
            '</div>' +
            '<div class="hp-bar-track"><div class="hp-bar-fill" style="width:' + pct + '%"></div></div>' +
          '</button>' +
          '<ul class="hp-ex-list hp-hidden">' + rows + '</ul>' +
        '</div>'
      );
    }).join("");

    const flaggedExams = exams
      .filter((e) => e.flaggedIds.length > 0)
      .sort((a, b) => {
        const d = b.flaggedIds.length - a.flaggedIds.length;
        if (d !== 0) return d;
        return slugDateKey(slugFromPath(b.path)) - slugDateKey(slugFromPath(a.path));
      });
    const totalFlagged = flaggedExams.reduce((s, e) => s + e.flaggedIds.length, 0);

    const problemNum = (id) => {
      const m = String(id).match(/problem-(\d+)/i);
      return m ? parseInt(m[1], 10) : null;
    };
    const slugCategory = (slug) => {
      if (/-quiz\d+$/i.test(slug)) return "quiz";
      if (/-midterm$/i.test(slug)) return "midterm";
      if (/-final$/i.test(slug)) return "final";
      return null;
    };
    const byCat = { quiz: [], midterm: [], final: [] };
    flaggedExams.forEach((e) => {
      const cat = slugCategory(slugFromPath(e.path));
      if (byCat[cat]) byCat[cat].push(e);
    });

    const catOrder = [
      { key: "quiz",    label: "Quizzes"  },
      { key: "midterm", label: "Midterms" },
      { key: "final",   label: "Finals"   },
    ];

    const reviewRows = catOrder.map((c) => {
      const items = byCat[c.key];
      const body = items.length === 0
        ? '<div class="hp-review-empty">Nothing flagged</div>'
        : items.map((e) => {
            const slug = slugFromPath(e.path);
            const entry = examEntry(slug);
            const fullTitle = e.title || (entry && entry.title) || prettySlug(slug);
            const href = examHref(e.path);
            const chips = e.flaggedIds
              .map((id) => ({ id, n: problemNum(id) }))
              .filter((x) => x.n !== null)
              .sort((a, b) => a.n - b.n)
              .map((x) =>
                '<a class="hp-review-chip" href="' + href + '#' + x.id + '">Problem ' + x.n + '</a>'
              ).join("");
            return (
              '<div class="hp-review-item">' +
                '<a href="' + href + '" class="hp-review-link">' + fullTitle + '</a>' +
                '<div class="hp-review-chips">' + chips + '</div>' +
              '</div>'
            );
          }).join("");
      const count = items.reduce((s, e) => s + e.flaggedIds.length, 0);
      return (
        '<div class="hp-review-col' + (items.length === 0 ? ' hp-review-col-empty' : '') + '">' +
          '<div class="hp-review-col-head">' +
            '<span class="hp-review-col-label">' + c.label + '</span>' +
            (count ? '<span class="hp-review-col-count">' + count + '</span>' : '') +
          '</div>' +
          body +
        '</div>'
      );
    }).join("");

    const reviewBlock = totalFlagged > 0
      ? '<div class="hp-review-card">' +
          '<button type="button" class="hp-review-head" aria-expanded="false">' +
            '<span class="hp-review-label">' +
              '<span class="hp-flag-icon" aria-hidden="true"></span>' +
              '<span>To review</span>' +
            '</span>' +
            '<span class="hp-review-count">' + totalFlagged + '</span>' +
            '<span class="hp-review-caret" aria-hidden="true"></span>' +
          '</button>' +
          '<div class="hp-review-list hp-hidden">' + reviewRows + '</div>' +
        '</div>'
      : '';

    const dash = document.createElement("section");
    dash.id = "progress-tracker";
    dash.innerHTML =
      '<hr class="hp-divider" />' +
      '<h3 class="hp-title">📊 Progress Tracker</h3>' +
      '<p class="hp-intro">As you work through problems from past quizzes and exams, mark them as complete to keep track of your progress. You can also flag questions for review if you want to come back to them later or ask for help.</p>' +
      '<p class="hp-intro"><strong>Note:</strong> Leaving and revisiting the site will save your progress, but clearing your browser history or cookies will erase your progress.</p>' +
      '<div class="hp-grid">' + cards + '</div>' +
      reviewBlock;

    // On a re-render, swap out the old dashboard in place and remember which
    // parts were open, so the page doesn't jump or collapse.
    const old = document.getElementById("progress-tracker");
    const wasCardsOpen = !!(old && old.querySelector(".hp-card.hp-card-open"));
    const wasReviewOpen = !!(old && old.querySelector(".hp-review-card.hp-card-open"));

    if (old) {
      old.replaceWith(dash);
    } else {
      // Insert above the <hr> that sits directly before the Pretest section,
      // so the intro paragraphs appear above the dashboard.
      const pretestH3 = document.getElementById("pretest");
      let anchor = pretestH3 ? pretestH3.previousElementSibling : null;
      while (anchor && anchor.tagName !== "HR") anchor = anchor.previousElementSibling;
      if (!anchor) anchor = document.querySelector("hr");
      if (anchor && anchor.parentNode) {
        anchor.parentNode.insertBefore(dash, anchor);
      } else {
        document.body.appendChild(dash);
      }
    }

    const allCards = Array.from(dash.querySelectorAll(".hp-card"));
    function setExpanded(open) {
      allCards.forEach((card) => {
        const list = card.querySelector(".hp-ex-list");
        const btn = card.querySelector(".hp-card-expand");
        if (list) list.classList.toggle("hp-hidden", !open);
        if (btn) btn.setAttribute("aria-expanded", String(open));
        card.classList.toggle("hp-card-open", open);
      });
    }
    allCards.forEach((card) => {
      const expandBtn = card.querySelector(".hp-card-expand");
      if (!expandBtn) return;
      expandBtn.addEventListener("click", () => {
        const anyOpen = allCards.some((c) => c.classList.contains("hp-card-open"));
        setExpanded(!anyOpen);
      });
    });

    const reviewCard = dash.querySelector(".hp-review-card");
    if (reviewCard) {
      const head = reviewCard.querySelector(".hp-review-head");
      const list = reviewCard.querySelector(".hp-review-list");
      function setReviewOpen(open) {
        list.classList.toggle("hp-hidden", !open);
        head.setAttribute("aria-expanded", String(open));
        reviewCard.classList.toggle("hp-card-open", open);
      }
      head.addEventListener("click", () => {
        setReviewOpen(list.classList.contains("hp-hidden"));
      });
      if (wasReviewOpen) setReviewOpen(true);
    }
    if (wasCardsOpen) setExpanded(true);
  }

  function init() {
    if (!isHomepage()) return;
    fetchExamTotals().then((map) => {
      EXAM_TOTALS = map || {};
      migrateOldKeys();
      render(collect());
      // Easter egg (progress-tracker.js): fireworks for a category finished
      // before celebrations existed, or finished in another tab.
      if (window.ptCelebrate) window.ptCelebrate.checkCategories(EXAM_TOTALS);

      // Pressing Back shows the homepage from the browser's back/forward
      // cache, without re-running this script, so the dashboard would show
      // the numbers from before you left. Rebuild it from storage then.
      window.addEventListener("pageshow", (e) => {
        if (e.persisted) render(collect());
      });
      // Progress changed in another tab: keep this tab's dashboard current.
      window.addEventListener("storage", (e) => {
        if (!e.key || e.key === DONE_KEY || e.key === FLAGS_KEY) render(collect());
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
