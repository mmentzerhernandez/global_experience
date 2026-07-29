# id-skills.html refresh: CourseFactory v2 era

> **For agentic workers:** execute one session at a time. Read
> `docs/superpowers/specs/2026-07-29-id-skills-refresh-design.md` (the approved spec),
> `docs/superpowers/specs/shell-conventions.md` (how this file is built), and
> `docs/superpowers/specs/content-brief.md` (every fact you are allowed to publish).
> Do not read the page's inline SVGs; they will exhaust your context.

**Goal:** Replace the stale id-* pipeline content in `id-skills.html` with the current
CourseFactory v2 system, current compliance engineering, and how the business is
organized and run, without changing the page's structure, interaction model, or visual
character.

**Architecture:** All content changes stay inside the single self-contained file
`id-skills.html`, plus new Mermaid sources under `diagrams/` and small copy updates in
`index.html`. No build step, no runtime external requests.

**Tech stack:** Plain HTML/CSS/vanilla JS. Diagrams authored as Mermaid and rendered
offline with `npx @mermaid-js/mermaid-cli` (v11.15.0).

**Diagram render recipe (already working, do not rediscover this).** All four diagram
sources are authored and rendered; the SVGs are in `diagrams/rendered/`. To re-render:

```
npx -y @mermaid-js/mermaid-cli -i diagrams/<name>.mmd \
  -o diagrams/rendered/<name>.svg --svgId <name>-svg \
  -b transparent -p diagrams/puppeteer.json
```

Two gotchas already solved: the command needs `dangerouslyDisableSandbox: true` because
npm writes its cache outside the sandbox, and mermaid-cli's bundled puppeteer asks for a
Chrome build that is not installed, so `diagrams/puppeteer.json` pins it to the
chrome-headless-shell already in `~/.cache/puppeteer`. If that path stops existing, list
`~/.cache/puppeteer/chrome-headless-shell/` and update the config. `--svgId` is what
produces the unique, self-scoped id the plan requires; never omit it.

## Global constraints

- Governing design skill: taste-skill v2 at
  `/Users/rabies/.claude/plugins/cache/taste-skill/taste-skill/1.0.0/skills/taste-skill/SKILL.md`,
  §11 Redesign Protocol, **Preserve** mode, dials DESIGN_VARIANCE 5, MOTION_INTENSITY 3,
  VISUAL_DENSITY 5. Read it before writing any HTML or CSS.
- **Mobile-first is binding.** Author at 360px first. Responsive overrides go at the END
  of the main stylesheet, never mid-sheet (source order beats media queries at equal
  specificity). Tap targets 44px minimum. Tables are card-stacking flex blocks from the
  start.
- **Voice is third person, case-study.** Never "I built". Describe the system and the
  work. No em dashes anywhere. All patterns in `~/.claude/rules/ai-writing.md` are banned.
- **Facts only from `docs/superpowers/specs/content-brief.md`.** If you need a fact that
  is not there, read the source file named in the brief. Never invent. Never publish the
  course price, entity file numbers, server IPs, or anything from a `_Credentials/`
  folder.
- Never modify anything inside an existing `<svg>` element except where a task says so
  explicitly. Never modify the `:target` panel switching CSS (~lines 207-219) or the
  `mermaid-wiki-guard` block.
- New SVGs must use a unique id (never `my-svg`), with every selector in their embedded
  `<style>` block prefixed by that id.
- Desktop must be unaffected: new CSS goes inside `@media` blocks at the end of the
  stylesheet, or styles currently-unstyled classes.
- The page deploys via GitHub Pages on push to `main`. Work happens on branch
  `coursefactory-v2-refresh`. Commit after each task. **Push only at the final gate.**
- If a verification fails, stop and fix before moving on. Never skip verification.
- Local servers bind to 127.0.0.1 and stop before the session ends.

## File map

- Modify: `id-skills.html` (head title, header h1, sidebar `<aside class="index">`,
  panels in `<main class="detail panels">`, mobile CSS at end of main stylesheet).
- Modify: `index.html` (linking card copy near lines 1612-1663, prose near 2036 and 2088).
- Create: `diagrams/*.mmd` (Mermaid sources, committed).
- Possibly regenerate: `img/id-skills-pipeline.svg` (portfolio thumbnail).

## Panel target state

| # | Panel id | Sidebar label | Swatch | Nested |
|---|---|---|---|---|
| 1 | `business-overview` | 1 - The business | `#283593` | no |
| 2 | `session-pipeline` | 2 - How a course is made | `#00695c` | no |
| 3 | `coursefactory-overview` | 3 - CourseFactory v2 | `#283593` | parent |
| 3a | `cf-stage-0` | Stage 0 - Intake | `#1565c0` | yes |
| 3b | `cf-stage-1` | Stage 1 - Groundwork | `#00838f` | yes |
| 3c | `cf-stage-2` | Stage 2 - Author | `#2e7d32` | yes |
| 3d | `cf-stage-3` | Stage 3 - Package | `#e65100` | yes |
| 3e | `cf-stage-4` | Stage 4 - Sweep | `#6a1b9a` | yes |
| 3f | `cf-checkers` | The checkers | `#c62828` | yes |
| 3g | `cf-gates` | The three gates | `#455a64` | yes |
| 4 | `compliance-engineering` | 4 - Compliance engineering | `#b71c1c` | no |
| 5 | `operating-system` | 5 - How the business runs | `#4527a0` | no |
| 6 | `tx4hrce-delivery` | 6 - Delivery platform | `#1b5e20` | no |

---

## Session 1: strip the old, land the shell

**Files:** `id-skills.html`

- [ ] **Step 1: Remove the retired panels.** Delete the seven `<section class="panel">`
  blocks with ids `1-id-architect`, `2-id-chunker`, `3-id-scripter`, `4-id-evaluator`,
  `5-id-presenter`, `6-id-qa-auditor`, and `rlo-taxonomy`. Each is contiguous, opened by
  its `<section class="panel"` line and closed by the next `</section>`. Delete their
  matching sidebar `.box` anchors inside `<div class="nest" id="pipeline-nest">`. Do not
  touch the `pipeline-overview`, `business-overview`, `content-development-workflow`, or
  `tx4hrce-delivery` panels yet.
- [ ] **Step 2: Rename the surviving panels' ids.** `content-development-workflow`
  becomes `session-pipeline`; `pipeline-overview` becomes `coursefactory-overview`.
  Update both the `<section id=...>` and every `href="#..."` that points at them,
  including any `xlink:href` inside existing SVG drill nodes.
- [ ] **Step 3: Add the new sidebar entries** for `cf-stage-0` through `cf-gates` inside
  the nest, plus top-level entries for `compliance-engineering` and `operating-system`,
  using the swatches in the table above and the markup in `shell-conventions.md`. Leave
  the panel bodies as empty stubs (`<section class="panel" id="..." style="--swatch: ...">
  <div class="detail-head"><h2>Placeholder</h2></div></section>`) so navigation works.
- [ ] **Step 4: Update the title and header.** Page `<title>` and the header `<h1>` both
  change to reflect that the business is live and this is how it is built and run. Keep
  the `← Portfolio` back-link untouched.
- [ ] **Step 5: Verify.** Run:
  `grep -c '<section class="panel"' id-skills.html` (expect 13);
  `grep -o 'href="#[a-z0-9-]*"' id-skills.html | sort -u` and confirm every anchor has a
  matching panel id;
  `grep -c 'mermaid-wiki-guard' id-skills.html` (expect the markers intact).
  Serve on 127.0.0.1, click every sidebar entry, confirm each opens its panel. Stop the
  server. Commit.

## Session 2: CourseFactory v2 content

**Files:** `id-skills.html`, `diagrams/`

- [ ] **Step 1: Write the parent panel** `coursefactory-overview` from the content-brief
  section "Panel 3 parent", including the scaffold entry command and the point that stage
  order is enforced by input dependencies rather than a driver script.
- [ ] **Step 2: Author the overview diagram.** `diagrams/coursefactory-overview.mmd`,
  Mermaid `flowchart TD`, showing stages 0 through 4 with the three gates as decision
  nodes between them. Use the classDef families in `shell-conventions.md`. Render with
  `npx @mermaid-js/mermaid-cli -i diagrams/coursefactory-overview.mmd -o /tmp/... --svgId cf-overview-svg`
  and inline the result in a `<div class="canvas">`.
- [ ] **Step 3: Write the five stage panels** (`cf-stage-0` through `cf-stage-4`) from
  the corresponding content-brief sections. Each gets the in/out framing, the concrete
  specifics, and a short diagram where it earns one. Keep prose tight; these are detail
  panels, not essays.
- [ ] **Step 4: Write the checkers panel** `cf-checkers`. Six named checkers with what
  each validates and whether it blocks, plus the Stage 4 report-only sweep. Give the
  retrieval-grounded fact-checker its own diagram
  (`diagrams/factcheck-cascade.mmd`): sectionize, hybrid retrieval (BM25 plus dense),
  rerank, floor gate, NLI judge, escalation tier, verdict. Do not claim "seven checkers".
- [ ] **Step 5: Write the gates panel** `cf-gates`. The three gates, what a human decides
  at each, the approval files they write, and why piecemeal checker runs cannot skip them.
- [ ] **Step 6: Verify.** Confirm no new `id="my-svg"`
  (`grep -c 'id="my-svg"' id-skills.html` must still be the pre-existing count minus any
  removed with deleted panels, and never increase). Confirm each new SVG's embedded style
  selectors are prefixed with its own id. Serve on 127.0.0.1, check all six new panels at
  360px and 1280px. Stop the server. Commit.

## Session 3: compliance, operating, delivery

**Files:** `id-skills.html`, `diagrams/`

- [ ] **Step 1: Write the compliance panel** `compliance-engineering` from the
  content-brief. Lead with the four gates and the per-day penalty, then the engineering:
  the seat-timer versus dwell-gate distinction, server-computed credit with the grace
  cap, server-side enforcement independent of JavaScript, the auditor deliberately not
  exempt, EN/ES parity. Include the measured accrual numbers and the honest limitations.
- [ ] **Step 2: Diagram the dwell gate** (`diagrams/dwell-gate.mmd`, `flowchart TD`):
  client beat only when focused and visible, server computes min(gap, 75s grace) bounded
  by time since first view, `after_config` gate on every request, capability exemption
  check, credit written or refused.
- [ ] **Step 3: Write the operating panel** `operating-system` from the content-brief,
  and author its 9-node portrait diagram (`diagrams/operating-loop.mmd`) exactly as
  specified at the end of that brief section.
- [ ] **Step 4: Update the delivery panel** `tx4hrce-delivery`. Rewrite the prose for
  Stripe, Lob certificate mailing, and the EN/ES split. In its existing SVG, and ONLY
  these two edits: change the "Pay $29 / card payment via Stripe" node text to remove the
  price, and change "Records kept four years" to two years. Both are `foreignObject` text
  nodes; edit the text content only, never the geometry.
- [ ] **Step 5: Update the business overview panel** `business-overview` with current
  facts and the extended milestone table, marking 2026-07-08 as the major milestone row.
  Add the future course pipeline.
- [ ] **Step 6: Verify.** Same structural greps as session 2, plus
  `grep -c '\$29' id-skills.html` (expect 0) and confirm "four years" no longer appears in
  the retention node. Serve on 127.0.0.1, review all 13 panels at 360px. Stop the server.
  Commit.

## Session 4: mobile pass, portfolio ripples, gate

**Files:** `id-skills.html`, `index.html`, `img/`

- [ ] **Step 1: Mobile audit.** At 360, 390, and 430px: confirm no horizontal body
  scroll, every new table stacks into cards, tap targets are 44px or larger, and each new
  diagram opens legibly rather than zoomed to illegibility. Fix by adding rules at the END
  of the main stylesheet only.
- [ ] **Step 2: Session pipeline panel copy.** Write `session-pipeline` from the
  content-brief if session 2 left it as a stub. Plan mode, model switch in the same
  session, the three fork-gated skills. No mention of any earlier pipeline generation.
- [ ] **Step 3: Update `index.html`.** The card copy, alt text, and prose near lines
  1612-1663, 2036, and 2088 stop saying "six-stage AI pipeline" and describe the
  CourseFactory v2 system instead. Regenerate `img/id-skills-pipeline.svg` from the new
  overview diagram if the old thumbnail no longer represents the page.
- [ ] **Step 4: Full verification.** Structural greps; `node --check` on the extracted
  guard script; confirm zero em dashes in new copy
  (`grep -c '—' id-skills.html` should not increase over the pre-change count); confirm
  no `$29`, no server IPs, no entity file numbers. Serve on 127.0.0.1 one last time,
  walk every panel at 360px and 1280px. Stop the server. Commit.
- [ ] **Step 5: GATE.** Present the finished page to the owner for review before any
  push. Do not merge to `main` and do not push. State clearly that pushing publishes to
  GitHub Pages.
