# id-skills.html content refresh: CourseFactory v2 era

Date: 2026-07-29. Status: approved by owner (design gate passed same day).

## Goal

Refresh `/Users/rabies/global_experience/id-skills.html` so its content matches how the
business is actually organized and run as of 2026-07-29, while preserving the page's
existing structure, interaction model, and visual character. The page remains a
diagram-dense technical deep dive linked from the public portfolio
(`/Users/rabies/global_experience/index.html`, deployed via GitHub Pages), told in
third-person case-study voice.

## Decisions locked at the design gate

| Decision | Choice |
|---|---|
| Page shape | Content refresh only. Keep header bar, sidebar index, `:target` panel switching, nested caret UX, mermaid-wiki-guard zoom/pan script. |
| Pipeline story | Replace the six id-* stage panels (and RLO taxonomy panel) with CourseFactory v2: stages 0 to 4, seven checkers, three human gates. |
| Operating layer | One new panel covering how the business is organized and run. |
| Public scope | All four content areas approved for publication: business facts and milestones, CourseFactory v2 internals, compliance engineering detail, operating layer detail. |
| Voice | Third person, case-study voice, throughout new and revised copy. Never "I built..."; describe the system and the work, not the author. |
| Design governance | taste-skill v2 (`/Users/rabies/.claude/plugins/cache/taste-skill/taste-skill/1.0.0/skills/taste-skill/SKILL.md`), §11 Redesign Protocol, **Preserve** mode. Dials: DESIGN_VARIANCE 5, MOTION_INTENSITY 3, VISUAL_DENSITY 5. redesign-skill's audit checklist (same plugin, `skills/redesign-skill/SKILL.md`) is a reference source during the shell audit, not a second governing skill. |
| Mobile | Mobile-first is binding for everything new (rules below). |

Design read (taste-skill §0): a Preserve-mode content refresh of a technical portfolio
deep-dive for recruiters and prospective clients, with a diagram-dense
engineering-notebook language, leaning toward the page's existing swatch system plus
native CSS. Motion stays low deliberately: the page carries a dozen large inline SVGs
and must stay fast on phones.

## New panel lineup (replaces the current 11 panels)

Sidebar order and nesting:

1. **Business overview** (swatch `#283593`): idea, TDLR provider #2520, course #32815
   approved, first sale 2026-07-08, live and selling. Milestone timeline extended
   through 2026-07 (Spanish parity 07-23, license-renewal funnel 07-22, dwell gate live
   07-28). Next-course pipeline: electrician ES (phase 3 of 5), barber (built, QA
   pending), RAS (sources gathered; fastest launch, self-reported), towing (not
   started).
2. **How a course is made today**: the Claude Code session pipeline adopted
   2026-07-12 (plan on the strong model, `/model sonnet` in the same session to
   execute, research and decision skills gated to genuine forks). 
3. **CourseFactory v2** parent panel (nested, caret UX like today's pipeline section):
   - Stage 0, Stage 1, Stage 2, Stage 3, Stage 4 (one nested panel each; content from
     `/Users/rabies/Desktop/IERHUB.com/5-CurriculumDevelopment/CourseFactory-v2/CONTRACT.md`
     and `ORCHESTRATION.md` plus the four coursefactory-v2 wiki pages in
     `/Users/rabies/Desktop/IERHUB.com/5-CurriculumDevelopment/Wiki/`).
   - **Seven checkers** (one nested panel), including the retrieval-grounded
     fact-checker (`tools/factcheck/check_facts.py`, LangChain/LangGraph).
   - **Three human gates** (one nested panel): why piecemeal checker use cannot skip
     gates; scaffold entry via `scaffold.py`; output lands in `PreApprovedCourses/`;
     `.mbz` Moodle packaging.
4. **Compliance engineering**: the four compliance gates (before sale, at sale, after
   completion, annual renewal; $5,000/day/violation stakes), per-page dwell-gate
   enforcement live 2026-07-28 for TX4HRCE EN and ES, seat-time and
   proof-of-completion evidence work.
5. **How the business is organized and run** (the operating panel): numbered
   workstream folders (_Admin through 11-Research), three-tier wiki with
   more-specific-tier-wins, manifest memory (`.claude/manifest.json` decisions),
   session waterfall at 50% context, plans consolidated in `10-Plans/` with
   status-as-folder-move, continuity mirror with daily push and dead-man check.
6. **Delivery platform**: Moodle at start.ierhub.com, Stripe checkout on the bilingual
   EN/ES storefront, certificate mailing ,
   dwell gate integration.

Total: 13 panels (6 top-level entries including the CourseFactory v2 parent, plus 7
nested under it). The six id-*
stage panels, the RLO taxonomy panel, and their SVGs are removed.

## Mobile-first rules (binding for all new content)

- Author at 360px first, enhance upward. Single-column flow by default.
- Responsive overrides live at the END of the main stylesheet. Constraint discovered in
  the prior waterfall (`plans/archive/HANDOFF-1.md`): media queries placed mid-sheet
  lose the cascade to later same-specificity base rules.
- Tables are written as card-stacking flex blocks from the start, not retrofitted.
  Tabular numerals (`font-variant-numeric: tabular-nums`) on the milestone table.
- Tap targets 44px minimum. The existing sticky chip nav is reused as-is.
- Diagrams drawn portrait-friendly: prefer Mermaid `TD` orientation over wide `LR` so
  phones do not open zoomed out to illegibility.
- No new animation beyond what the page already has (MOTION_INTENSITY 3; the guard
  script's zoom/pan and existing transitions are the ceiling).

## Diagram production

- Author each diagram as Mermaid source in `/Users/rabies/global_experience/diagrams/`
  (new folder, committed) so every SVG is regenerable.
- Render offline with mermaid-cli (`npx @mermaid-js/mermaid-cli`), inline the SVG into
  the page. No external requests at runtime; the page stays self-contained.
- Every new SVG gets a unique id (never `my-svg`; the 11-way collision is a known
  legacy issue and must not grow). Keep `viewBox` intact: the mermaid-wiki-guard
  script owns sizing through it.
- Color diagrams with the page's existing per-panel swatch palette, not the IERhub
  brand palette; this is the portfolio's visual language.
- Embedded SVG `<style>` blocks must be scoped (prefix selectors with the SVG's unique
  id) so styles cannot collide across inlined SVGs.

## Copy rules

- Third person, factual, plain words. No em dashes anywhere. All AI-writing patterns
  in `~/.claude/rules/ai-writing.md` are banned.
- Facts come only from verified sources in `/Users/rabies/Desktop/IERHUB.com` and
  `/Users/rabies/Desktop/Operating`. Anything uncertain is checked against the source
  file before it is written into the page. No invented metrics, no revenue claims
  (none are documented).
- Sentence-case headings.

## Ripples outside id-skills.html

- Page `<title>` (currently "Automation & Curriculum Development Project") and header
  h1 (currently "How Automating a Curriculum Development Pipeline Became a Business")
  change to match the new story. New h1 direction: the business is live; the page now
  covers idea to revenue, not idea to first sale.
- `/Users/rabies/global_experience/index.html`: the linking card's copy ("six-stage AI
  pipeline"), its alt text, and the thumbnail
  `/Users/rabies/global_experience/img/id-skills-pipeline.svg` are updated to the
  CourseFactory v2 story. The two prose mentions near lines 2036 and 2088 are updated
  the same way.

## What never changes (Preserve-mode guarantees)

- URL: the file stays `id-skills.html` (it is linked publicly).
- The shell: header bar, sidebar and nesting behavior, `:target` panel switching,
  panel/`--swatch` CSS architecture, mermaid-wiki-guard script.
- The portfolio back-link in the header.
- Desktop layout character; existing typography and palette.

## Verification

- Structural greps after each panel lands: expected panel count, no `id="my-svg"` in
  new SVGs, guard markers (`mermaid-wiki-guard:start v2` / `end`) intact, no `##`
  colors in CSS.
- `node --check` on the extracted guard script after any tail edits.
- Local preview server bound to 127.0.0.1 only, stopped before session end; eyeball at
  360, 390, and 1280 widths.
- A PostToolUse hook re-runs guard hardening after edits to this file; it is
  idempotent, but check `git status` before branch operations.
- Push to GitHub Pages only at a final human gate (GATE in the plan).

## Process

- Multi-session waterfall per the global 50% rule. The completed mobile plan
  (`plans/PLAN.md`, `plans/HANDOFF-1.md`) moves to `plans/archive/` first; the new
  plan becomes the active `/Users/rabies/global_experience/plans/PLAN.md`, with
  sessions sized to fit under 50% context.
- Work happens on a feature branch off `main`; merge and push only at the final gate.
- Implementers must read the taste-skill v2 SKILL.md at the path above before writing
  any HTML/CSS, and apply Preserve mode with dials 5/3/5.

## Source inventory for implementers (read-only inputs)

- `/Users/rabies/Desktop/IERHUB.com/5-CurriculumDevelopment/CourseFactory-v2/` (CONTRACT.md, ORCHESTRATION.md, tools/, scaffold.py)
- `/Users/rabies/Desktop/IERHUB.com/5-CurriculumDevelopment/Wiki/` (coursefactory-v2*.md, claude-code-session-pipeline.md, course-pipeline-status.md)
- `/Users/rabies/Desktop/IERHUB.com/1-AboutTheBusiness/Wiki/syntheses/ce-provider-revenue-criteria.md` (four compliance gates)
- `/Users/rabies/Desktop/IERHUB.com/Wiki/index.md` and per-workstream Wiki pages (organization panel)
- `/Users/rabies/Desktop/IERHUB.com/.claude/manifest.json` (binding decisions; thinkific_retired, plans_home_10_plans, main_not_master)
- `/Users/rabies/Desktop/IERHUB.com/_Continuity/CONTINUITY.md` (continuity mirror)
- `/Users/rabies/Desktop/Operating/OperatingSystem.md` and `/Users/rabies/Desktop/Operating/wiki/` (operating panel)
- `/Users/rabies/Desktop/IERHUB.com/4-Compliance/` and `10-Plans/CurrentPlans/tdlr-audit-check/` (compliance engineering panel)
