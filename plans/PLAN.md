# id-skills.html Mobile-First Rendering Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make `id-skills.html` render as well as possible on phones (320–430px wide) without degrading the desktop layout.

**Architecture:** All changes stay inside the single self-contained file `id-skills.html`: fix broken CSS, style the JS-injected zoom controls, add touch pinch/pan to the existing `mermaid-wiki-guard` script, replace the lone 820px media query with a full mobile layer (sticky chip nav, readable type, card-stacked table). No build step, no new files, no external requests.

**Tech Stack:** Plain HTML/CSS/vanilla JS. Verified with `grep`, `node --check`, and a local `python3 -m http.server` bound to 127.0.0.1.

## Global Constraints

- Every edit targets `/Users/rabies/global_experience/id-skills.html` only.
- Never modify anything inside an `<svg ...>` element (the Mermaid geometry, its embedded `<style>` blocks, or the `id="my-svg"` attributes). The duplicate `id="my-svg"` across 11 SVGs is a known pre-existing issue and is OUT OF SCOPE.
- Never modify the panel HTML content or the `:target`-based panel switching (`.panel`, `.panels` rules at ~line 207–219).
- Use the Edit tool with the exact `old_string` blocks given below. If an `old_string` does not match, re-Read the surrounding region and adapt whitespace only — do not rewrite logic. Do not use sed/regex for these edits.
- Desktop must be unaffected: new CSS goes either (a) inside `@media (max-width: ...)` blocks or (b) styles the currently-unstyled `.zoom-controls`/`.zoom-hint`/`.canvas.panning` classes.
- The page deploys via GitHub Pages on push to `main`. Commit after each task; push only when the human approves at the final gate.
- If any verification fails, stop and fix before moving to the next task. Never skip a verification step.
- Local servers must bind to 127.0.0.1 and be stopped before the session ends.

## File Map

- Modify: `id-skills.html`
  - Head: lines ~4–6 (meta), ~32–34 (`html` rule), ~426–429 (broken `.hurdle-row`), ~287–304 (the only `@media` block), just before `</style>` at ~line 444 (append new rules).
  - Tail: `mermaid-wiki-guard` script between `<!-- mermaid-wiki-guard:start v2 -->` and `<!-- mermaid-wiki-guard:end -->` (~lines 12485–12726).
- Create: nothing else. (This PLAN.md and HANDOFF files live in `plans/`.)

---

### Task 1: Fix broken CSS and add mobile meta hygiene

**Files:** Modify `id-skills.html` (head only)

**Interfaces:** Produces valid CSS for `.hurdle-row`; later tasks assume the stylesheet parses cleanly.

- [x] **Step 1: Fix the invalid double-hash background**

The "Major Milestone" table row is currently `background: ##1f5eff !important;` — invalid CSS, so the highlight row renders with no background. Intent is a subtle blue highlight (bright `#1f5eff` would clash with the muted text color). Edit:

old_string:
```
     .path-table tbody tr.hurdle-row {
    background: ##1f5eff !important;
    box-shadow: inset 4px 0 0 var(--accent);
      }
```

new_string:
```
      .path-table tbody tr.hurdle-row {
        background: rgba(31, 94, 255, 0.1) !important;
        box-shadow: inset 4px 0 0 var(--accent);
      }
```

- [x] **Step 2: Stop iOS font inflation**

old_string:
```
      html {
        scroll-behavior: smooth;
      }
```

new_string:
```
      html {
        scroll-behavior: smooth;
        -webkit-text-size-adjust: 100%;
        text-size-adjust: 100%;
      }
```

- [x] **Step 3: Add theme-color meta**

old_string:
```
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

new_string:
```
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="theme-color" content="#eff7ff" />
```

- [x] **Step 4: Verify**

Run: `grep -c '##1f5eff' /Users/rabies/global_experience/id-skills.html`
Expected: `0`

Run: `grep -c 'text-size-adjust: 100%' /Users/rabies/global_experience/id-skills.html`
Expected: `2`

Run: `grep -c 'theme-color' /Users/rabies/global_experience/id-skills.html`
Expected: `1`

- [x] **Step 5: Commit**

```bash
cd /Users/rabies/global_experience && git add id-skills.html && git commit -m "fix: repair invalid hurdle-row background, add text-size-adjust and theme-color"
```

---

### Task 2: Style the injected zoom controls and hint

The guard script appends `<div class="zoom-controls">` (three buttons: `+`, `−`, `FIT`) and `<div class="zoom-hint">` into every `.canvas`, but no CSS exists for them — they render as raw unstyled buttons in the flex flow next to each diagram, on every viewport. This task styles them as overlays.

**Files:** Modify `id-skills.html` (main stylesheet, append before `</style>`)

**Interfaces:** Produces `.zoom-controls`, `.zoom-hint`, `.canvas.panning` rules; Task 3's JS relies on `.canvas` being `position: relative`.

- [x] **Step 1: Append overlay styles at the end of the main stylesheet**

old_string:
```
      .benefits li strong {
        color: var(--text-heading);
      }
    </style>
```

new_string:
```
      .benefits li strong {
        color: var(--text-heading);
      }
      /* ── Diagram zoom controls & hint (elements injected by mermaid-wiki-guard) ── */
      .canvas {
        position: relative;
      }
      .zoom-controls {
        position: absolute;
        top: 0.75rem;
        right: 0.75rem;
        display: flex;
        flex-direction: column;
        gap: 0.4rem;
        z-index: 5;
      }
      .zoom-controls button {
        width: 44px;
        height: 44px;
        border: 1px solid rgba(0, 47, 167, 0.2);
        border-radius: 12px;
        background: rgba(255, 255, 255, 0.92);
        color: var(--accent);
        font-size: 1.15rem;
        font-weight: 700;
        font-family: var(--font);
        cursor: pointer;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
      }
      .zoom-controls button.reset {
        font-size: 0.62rem;
        letter-spacing: 0.05em;
      }
      .zoom-controls button:hover,
      .zoom-controls button:active {
        background: var(--chip-bg);
      }
      .zoom-hint {
        position: absolute;
        bottom: 0.6rem;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(44, 62, 80, 0.75);
        color: #fff;
        font-size: 0.68rem;
        padding: 0.25rem 0.7rem;
        border-radius: var(--pill);
        pointer-events: none;
        white-space: nowrap;
        z-index: 5;
      }
      .canvas.panning {
        cursor: grabbing;
      }
    </style>
```

- [x] **Step 2: Verify**

Run: `grep -c '\.zoom-controls button' /Users/rabies/global_experience/id-skills.html`
Expected: `4` (base rule, `.reset`, and the `:hover` + `:active` selector lines)

Run: `grep -c 'position: relative' /Users/rabies/global_experience/id-skills.html`
Expected: `2` (one pre-existing occurrence elsewhere in the file, plus the new `.canvas` rule)

- [x] **Step 3: Commit**

```bash
cd /Users/rabies/global_experience && git add id-skills.html && git commit -m "feat: style diagram zoom controls and hint as canvas overlays"
```

---

### Task 3: Touch support for diagrams (pinch zoom + pan-when-zoomed)

The guard script's pan handler is mouse-only (`e.button !== 0`, single-pointer). On phones: no wheel, drag scrolls the page, pinch zooms the whole page. This task adds two-finger pinch zoom and single-finger pan *only while zoomed in*, so normal page scrolling over a diagram still works at the fitted view. The `+ − FIT` buttons keep working as before.

**Files:** Modify `id-skills.html` (guard script between the `mermaid-wiki-guard` comment markers)

**Interfaces:** Consumes `vb`, `orig`, `apply()`, `zoomAt()` already defined in `setup()`. Produces `isZoomed()` / `syncTouchAction()` (function declarations, hoisted within `setup()`).

- [x] **Step 1: Make apply() keep touch-action in sync**

old_string:
```
          function apply() {
            svg.setAttribute("viewBox", vb.x + " " + vb.y + " " + vb.w + " " + vb.h);
          }
```

new_string:
```
          function apply() {
            svg.setAttribute("viewBox", vb.x + " " + vb.y + " " + vb.w + " " + vb.h);
            syncTouchAction();
          }
          function isZoomed() {
            return vb.w < orig.w - 0.5;
          }
          function syncTouchAction() {
            // At the fitted view let the page scroll normally; while zoomed in,
            // capture touches so one finger pans the diagram.
            canvas.style.touchAction = isZoomed() ? "none" : "pan-y";
          }
```

- [x] **Step 2: Replace the mouse-only pan handlers with multi-pointer pinch/pan**

old_string:
```
          var down = false,
            moved = false,
            sx = 0,
            sy = 0;
          canvas.addEventListener("pointerdown", function (e) {
            if (e.button !== 0) return;
            down = true;
            moved = false;
            sx = e.clientX;
            sy = e.clientY;
            canvas.classList.add("panning");
          });
          window.addEventListener("pointermove", function (e) {
            if (!down) return;
            var dx = e.clientX - sx,
              dy = e.clientY - sy;
            if (!moved && Math.abs(dx) + Math.abs(dy) > 4) moved = true;
            if (moved) {
              var r = svg.getBoundingClientRect();
              if (r.width && r.height) {
                vb.x -= (dx * vb.w) / r.width;
                vb.y -= (dy * vb.h) / r.height;
                apply();
              }
              sx = e.clientX;
              sy = e.clientY;
            }
          });
          window.addEventListener("pointerup", function () {
            down = false;
            canvas.classList.remove("panning");
          });
```

new_string:
```
          var pointers = new Map(); // pointerId -> {x, y}; supports mouse drag, touch pan, 2-finger pinch
          var pinchDist = 0;
          var moved = false;
          syncTouchAction();
          canvas.addEventListener("pointerdown", function (e) {
            if (e.pointerType === "mouse" && e.button !== 0) return;
            pointers.set(e.pointerId, { x: e.clientX, y: e.clientY });
            moved = false;
            if (pointers.size === 2) {
              var pts = Array.from(pointers.values());
              pinchDist = Math.hypot(pts[0].x - pts[1].x, pts[0].y - pts[1].y);
            }
            canvas.classList.add("panning");
          });
          window.addEventListener("pointermove", function (e) {
            if (!pointers.has(e.pointerId)) return;
            var prev = pointers.get(e.pointerId);
            pointers.set(e.pointerId, { x: e.clientX, y: e.clientY });
            if (pointers.size === 2) {
              var pts = Array.from(pointers.values());
              var d = Math.hypot(pts[0].x - pts[1].x, pts[0].y - pts[1].y);
              if (pinchDist > 0 && d > 0) {
                zoomAt(d / pinchDist, (pts[0].x + pts[1].x) / 2, (pts[0].y + pts[1].y) / 2);
                moved = true;
              }
              pinchDist = d;
              return;
            }
            if (e.pointerType === "touch" && !isZoomed()) return; // fitted view: leave the touch to page scroll
            var dx = e.clientX - prev.x,
              dy = e.clientY - prev.y;
            if (!moved && Math.abs(dx) + Math.abs(dy) > 4) moved = true;
            if (moved) {
              var r = svg.getBoundingClientRect();
              if (r.width && r.height) {
                vb.x -= (dx * vb.w) / r.width;
                vb.y -= (dy * vb.h) / r.height;
                apply();
              }
            }
          });
          function endPointer(e) {
            pointers.delete(e.pointerId);
            if (pointers.size < 2) pinchDist = 0;
            if (pointers.size === 0) canvas.classList.remove("panning");
          }
          window.addEventListener("pointerup", endPointer);
          window.addEventListener("pointercancel", endPointer);
```

- [x] **Step 3: Device-aware hint text**

old_string:
```
          hint.textContent = "Scroll to zoom · drag to pan";
```

new_string:
```
          hint.textContent = window.matchMedia("(pointer: coarse)").matches
            ? "Pinch to zoom · use FIT to reset"
            : "Scroll to zoom · drag to pan";
```

- [x] **Step 4: Syntax-check the modified script**

```bash
cd /Users/rabies/global_experience && python3 -c "
import re
html = open('id-skills.html').read()
block = html.split('mermaid-wiki-guard:start')[1].split('mermaid-wiki-guard:end')[0]
js = block.split('<script>')[1].split('</script>')[0]
open('plans/_guard_check.js','w').write(js)
" && node --check plans/_guard_check.js && rm plans/_guard_check.js && echo SYNTAX_OK
```
Expected: `SYNTAX_OK`

- [x] **Step 5: Verify the old handler is fully gone**

Run: `grep -c 'var down = false' /Users/rabies/global_experience/id-skills.html`
Expected: `0`

Run: `grep -c 'pointercancel' /Users/rabies/global_experience/id-skills.html`
Expected: `1`

- [x] **Step 6: Commit**

```bash
cd /Users/rabies/global_experience && git add id-skills.html && git commit -m "feat: add touch pinch-zoom and zoomed-in panning to diagram canvases"
```

---

### Task 4: Mobile layout layer — sticky chip nav, readable type, tighter chrome

Replaces the existing thin `@media (max-width: 820px)` block wholesale. On phones the sidebar becomes a sticky, horizontally scrollable chip row (labels only, descriptions hidden, nested stage links always visible in the row), headings scale with `clamp()`, and small text is floored at ~12.5px.

**Files:** Modify `id-skills.html` (the single `@media` block at ~line 287)

**Interfaces:** Consumes classes already in the markup (`.index`, `.box`, `.nest`, `.caret`, `.panel`, …). No markup changes. `display: contents` on `.nest` intentionally neutralizes its collapse animation on mobile only.

- [x] **Step 1: Replace the whole 820px media block**

old_string:
```
      @media (max-width: 820px) {
        .split {
          grid-template-columns: 1fr;
          padding: 1rem;
        }
        header.bar {
          margin: 1rem 1rem 0;
          flex-direction: column;
          align-items: flex-start;
          gap: 0.4rem;
        }
        .index {
          max-height: 300px;
        }
        .detail {
          padding: 1.5rem;
        }
      }
```

new_string:
```
      @media (max-width: 820px) {
        header.bar {
          margin: 0.75rem 0.75rem 0;
          padding: 0.75rem 1rem;
          flex-direction: column;
          align-items: flex-start;
          gap: 0.4rem;
          border-radius: var(--radius-md);
        }
        header.bar h1 {
          font-size: clamp(0.95rem, 4vw, 1.1rem);
          line-height: 1.3;
        }
        .split {
          grid-template-columns: 1fr;
          padding: 0.75rem 0.75rem 1.25rem;
          gap: 0.75rem;
        }
        /* Sidebar becomes a sticky, horizontally scrollable chip row */
        .index {
          position: sticky;
          top: 0.5rem;
          z-index: 20;
          display: flex;
          gap: 0.5rem;
          overflow-x: auto;
          -webkit-overflow-scrolling: touch;
          max-height: none;
          padding: 0.6rem 0.75rem;
          border-radius: var(--radius-md);
          scrollbar-width: thin;
        }
        .index-label {
          display: none;
        }
        .index .box {
          flex: 0 0 auto;
          display: flex;
          align-items: center;
          min-height: 44px;
          margin: 0;
          padding: 0.4rem 0.9rem 0.4rem 1.05rem;
        }
        .index .box p,
        .index .caret {
          display: none;
        }
        .index .box h3 {
          font-size: 0.78rem;
          white-space: nowrap;
        }
        .index .box-parent {
          padding-right: 0.9rem;
        }
        .nest {
          display: contents;
        }
        .detail {
          padding: 1.1rem 1rem 1.5rem;
        }
        .detail-head h2 {
          font-size: clamp(1.25rem, 5.5vw, 1.9rem);
        }
        .panel {
          scroll-margin-top: 80px;
        }
        .detail-note {
          font-size: 1rem;
        }
        .lede,
        .facts li,
        .benefits li {
          font-size: 0.92rem;
        }
        .box p {
          font-size: 0.78rem;
        }
        .section-label {
          font-size: 0.72rem;
        }
        .canvas {
          padding: 0.75rem;
        }
      }
```

- [x] **Step 2: Verify**

Run: `grep -c 'display: contents' /Users/rabies/global_experience/id-skills.html`
Expected: `1`

Run: `grep -c 'scroll-margin-top' /Users/rabies/global_experience/id-skills.html`
Expected: `1`

Run: `grep -c 'max-height: 300px' /Users/rabies/global_experience/id-skills.html`
Expected: `0` (old block fully replaced)

- [x] **Step 3: Commit**

```bash
cd /Users/rabies/global_experience && git add id-skills.html && git commit -m "feat: mobile layout layer - sticky chip nav, clamp type, readable font floors"
```

---

### Task 5: Card-stacked pipeline table under 640px

The business-overview table (`.path-table`, `min-width: 560px`) currently side-scrolls on phones. Stack each row into a card using CSS only — the `Step` prefix is generated with `::before`, so no markup edits.

**Files:** Modify `id-skills.html` (append a new media block right after the 820px block's closing brace — anchor on the unique `.canvas` padding rule inside it)

- [x] **Step 1: Append the 640px block**

old_string:
```
        .canvas {
          padding: 0.75rem;
        }
      }
```

new_string:
```
        .canvas {
          padding: 0.75rem;
        }
      }
      @media (max-width: 640px) {
        .path-table {
          min-width: 0;
          font-size: 0.9rem;
        }
        .path-table thead {
          display: none;
        }
        .path-table tbody tr {
          display: block;
          padding: 0.8rem 0.9rem;
          border-bottom: 1px solid rgba(0, 0, 0, 0.08);
        }
        .path-table tbody tr:last-child {
          border-bottom: none;
        }
        .path-table tbody td {
          display: block;
          padding: 0.15rem 0;
          border-bottom: none;
        }
        .path-table .c-step,
        .path-table .c-status,
        .path-table .c-name {
          text-align: left;
          white-space: normal;
        }
        .path-table .c-step::before {
          content: "Step ";
        }
        .path-table .c-step {
          font-size: 0.72rem;
          letter-spacing: 0.06em;
          text-transform: uppercase;
        }
        .path-table .c-name {
          font-size: 1rem;
        }
      }
```

- [x] **Step 2: Verify**

Run: `grep -c 'max-width: 640px' /Users/rabies/global_experience/id-skills.html`
Expected: `1`

Run: `grep -c 'content: "Step "' /Users/rabies/global_experience/id-skills.html`
Expected: `1`

- [x] **Step 3: Commit**

```bash
cd /Users/rabies/global_experience && git add id-skills.html && git commit -m "feat: stack pipeline table into cards under 640px"
```

---

### Task 6: Full-page verification and human visual gate

- [x] **Step 1: Serve locally**

```bash
cd /Users/rabies/global_experience && python3 -m http.server 8321 --bind 127.0.0.1 &
sleep 1 && curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8321/id-skills.html
```
Expected: `200`

- [x] **Step 2: Structural sanity check**

```bash
cd /Users/rabies/global_experience && python3 - <<'EOF'
html = open('id-skills.html').read()
checks = {
  'panels intact': html.count('class="panel"') == 11,
  'svgs intact': html.count('<svg') == 11,
  'style blocks intact': html.count('<style') == 12,
  'no double-hash colors': '##' not in html.split('</style>')[0],
  'guard markers intact': 'mermaid-wiki-guard:start' in html and 'mermaid-wiki-guard:end' in html,
}
for name, ok in checks.items():
    print(('PASS' if ok else 'FAIL'), name)
assert all(checks.values())
EOF
```
Expected: five `PASS` lines, no traceback.

- [x] **Step 3: GATE — human visual review**

GATE: Ask the human to review `http://127.0.0.1:8321/id-skills.html` in Chrome DevTools device emulation at 375×812 (iPhone), 768×1024 (iPad), and a normal desktop window, checking:
1. Chip nav scrolls horizontally, sticks to the top, and every panel is reachable (including the six nested stages and RLO Taxonomy).
2. Zoom controls sit at the top-right of each diagram; `+ − FIT` work by tap; pinch zooms; one finger pans only after zooming in; page scroll still works over a fitted diagram.
3. Business-overview table reads as stacked cards at phone width; milestone row shows a light blue highlight.
4. No text under ~12px; headings don't overflow; desktop layout looks unchanged.

Do not push to `main` until the human approves. If running headless, write the gate question into the handoff under a `GATE:` line and stop.

- [x] **Step 4: Stop the server**

```bash
kill %1 2>/dev/null; pkill -f "http.server 8321" 2>/dev/null; echo stopped
```

- [x] **Step 5: Push after approval**

```bash
cd /Users/rabies/global_experience && git push
```

Then confirm the GitHub Pages deploy succeeds (Actions tab or `gh run list --limit 1`).

---

## Decisions & Non-Goals

- **Diagram strategy:** keep the existing fit-to-canvas + zoom model and make it touch-capable, rather than switching to natural-size horizontal scrolling. The guard script already owns the viewBox; fighting it with CSS min-widths would conflict.
- **Mobile nav:** sticky horizontal chip row chosen over a collapsible accordion — every destination stays one tap away without markup changes, and `:target` switching already scrolls to the opened panel.
- **Out of scope:** deduplicating the 11 `id="my-svg"` SVGs and their globally-colliding embedded styles; dark mode; splitting the 745KB file. Note these in the final handoff as known follow-ups.

## Completion

When all tasks are checked and the gate is approved, write `plans/HANDOFF-1.md` with the verification command, commit shas, and the line `WATERFALL: COMPLETE`.
