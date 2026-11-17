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
    try { return JSON.parse(localStorage.getItem(k) || "{}"); }
    catch { return {}; }
  }

  function countTrue(obj) {
    let n = 0;
    for (const k in obj) if (obj[k]) n++;
    return n;
  }

  function collect() {
    const exams = [];
    for (let i = 0; i < localStorage.length; i++) {
      const k = localStorage.key(i);
      if (!k || !k.startsWith("pt-meta:")) continue;
      const meta = loadJSON(k);
      if (!meta.path || !meta.category) continue;
      const progress = loadJSON("progress:" + meta.path);
      const flags = loadJSON("flags:" + meta.path);
      const flaggedIds = Object.keys(flags).filter((id) => flags[id]);
      exams.push({
        path: meta.path,
        title: meta.title || meta.path,
        category: meta.category,
        total: meta.total || 0,
        done: countTrue(progress),
        flaggedIds: flaggedIds,
      });
    }
    return exams;
  }

  function examHref(path) {
    const parts = path.split("/").filter(Boolean);
    const idx = parts.lastIndexOf("index.html");
    if (idx >= 1) return parts[idx - 1] + "/index.html";
    return path;
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
      head.addEventListener("click", () => {
        const open = list.classList.toggle("hp-hidden") === false;
        head.setAttribute("aria-expanded", String(open));
        reviewCard.classList.toggle("hp-card-open", open);
      });
    }
  }

  function init() {
    if (!isHomepage()) return;
    fetchExamTotals().then((map) => {
      EXAM_TOTALS = map || {};
      const exams = collect();
      render(exams);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
