# id-skills.html shell conventions (audited 2026-07-29)

Reference for implementers. Read this instead of re-reading the page's inline SVGs,
which are enormous and will blow out a context window.

## File shape

Single self-contained file, `/Users/rabies/global_experience/id-skills.html`, ~12,900
lines, ~750 KB. No build step, no runtime external requests.

- `<head>`: main stylesheet, plus 11 further `<style>` blocks that live INSIDE the
  inlined SVGs (12 total in the file).
- `<header class="bar">`: back-link `<a id="back-btn" href="index.html">← Portfolio</a>`,
  then `<h1>`, then `<span class="sub">`.
- `<div class="split">` wraps `<aside class="index">` (sidebar) and
  `<main class="detail panels">` (panels).
- Tail: `<script>` with `toggleNest()`, then the guard block between
  `<!-- mermaid-wiki-guard:start v2 -->` and `<!-- mermaid-wiki-guard:end -->`.

## Sidebar entry markup

Top-level entry:

```html
<a class="box" href="#PANEL-ID" style="--swatch: #283593"
  ><h3>1 - Title</h3>
  <p>Subtitle</p></a
>
```

Parent entry with nested children (the caret toggle):

```html
<a class="box box-parent" href="#PARENT-ID" onclick="toggleNest(this)"
   aria-expanded="false" style="--swatch: #283593"
  ><h3>3 - Title</h3>
  <p>Subtitle</p>
  <span class="caret" aria-hidden="true">▶</span></a
>
<div class="nest" id="pipeline-nest">
  ...child `.box` anchors...
</div>
```

`toggleNest()` in the tail script targets `document.getElementById("pipeline-nest")`.
Keep that id, or update the function to match. Anchor tags close on the next line
(`></a\n>`); match that formatting so diffs stay small.

## Panel markup

```html
<section class="panel" id="PANEL-ID" style="--swatch: #1b5e20">
  <div class="detail-head">
    <h2>Heading</h2>
    <span class="pill" style="--swatch: #1b5e20">Verb · Noun</span>
  </div>

  <div style="margin: 0; padding: 0; font-family: sans-serif; line-height: 1.6; color: #333">
    <h3 style="color: #1a202c; margin-bottom: 8px">Sub-heading</h3>
    <p style="margin-top: 0; margin-bottom: 16px">Lede paragraph.</p>
    <ul style="padding-left: 20px">
      <li style="margin-bottom: 8px"><strong>Label:</strong> detail.</li>
    </ul>
  </div>

  <div class="canvas">
    <svg id="UNIQUE-ID" width="100%" ...>...</svg>
  </div>
</section>
```

Panels are contiguous: each `<section class="panel">` is closed by the next
`</section>` with no nesting. Panel switching is `:target`-based CSS around lines
207-219; do not touch it. The `--swatch` custom property drives the panel accent and
must match the sidebar entry's swatch.

Note: existing panels use inline styles on content divs. This is the established
pattern in this file; match it rather than introducing new classes, unless a rule
belongs in the mobile layer at the end of the stylesheet.

## Diagram conventions

Rendered Mermaid flowcharts, baked to inline SVG. Observed conventions:

- Mermaid theme accent throughout is `#002fa7` (edges, markers, node strokes,
  gradients). Node fills default `#f0f3ff`.
- Semantic classDefs carry the category color, not the panel swatch. Existing set:
  `people` (#ECEFF1 / #455A64), `access` (#E3F2FD / #1565C0), `course` (#E8F5E9 /
  #2E7D32), `enforce` (#FFF3E0 / #E65100), `report` (#FFEBEE / #C62828), `drill`
  (#F9A825 / #7A5200, 2px stroke).
- The `drill` class marks clickable cross-panel navigation nodes, wrapped in
  `<a xlink:href="#panel-id">`, labelled like "← Back to Business Overview". Reuse this
  for links between the new panels.
- Every SVG carries `width="100%"`, an intact `viewBox`, and
  `style="max-width: Npx; background-color: transparent"`.
- Existing SVGs all use `id="my-svg"` (11-way collision, known legacy defect). New
  SVGs MUST use a unique id, and every selector inside their embedded `<style>` block
  must be prefixed with that unique id, exactly as mermaid-cli emits when given a
  custom id. This is what keeps embedded styles from leaking across diagrams.

## Guard script

The `mermaid-wiki-guard` block owns diagram sizing via `viewBox`, injects the zoom
controls and hint (`.zoom-controls`, `.zoom-hint`, `.canvas.panning`, styled around
line 514), and adds touch pinch/pan. Extend it rather than fighting it with CSS
min-widths. A PostToolUse hook re-runs guard hardening after edits to this file; it is
idempotent, but check `git status` before branch operations.

Verify after tail edits: extract the script and run `node --check`.

## Cascade constraint (learned the hard way)

Responsive overrides must sit at the END of the main stylesheet. Base rules such as
`.path-table` appear later in source than the mid-sheet media blocks, so a mobile
block placed earlier loses at equal specificity even though it is inside a media
query. Source order decides.
