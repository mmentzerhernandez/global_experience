# HANDOFF-1: id-skills.html CourseFactory v2 refresh

Written 2026-07-29 at the 50% context checkpoint of the orchestrating session.
Sessions 1 through 3 of `plans/PLAN.md` were dispatched as Sonnet subagents from that
session. **Session 4 remains.**

## Verification (run this first)

```
cd /Users/rabies/global_experience
git log --oneline -1                  # expect the session 3 commit on coursefactory-v2-refresh
git status --short                    # expect a clean tree
grep -c '<section class="panel"' id-skills.html    # expect 13
grep -c '<h2>Placeholder</h2>' id-skills.html      # expect 0
grep -c 'id="my-svg"' id-skills.html               # expect 3, must never increase
grep -c '—' id-skills.html                         # expect 0
grep -c '\$29' id-skills.html                      # expect 0
grep -c 'mermaid-wiki-guard' id-skills.html        # expect 5
```

Branch: `coursefactory-v2-refresh`. Nothing has been pushed. `main` is untouched.

If the placeholder count is 2 rather than 0, Session 3 did not finish; re-run the
Session 3 section of `plans/PLAN.md` before starting Session 4.

## Read these before doing anything

- `docs/superpowers/specs/2026-07-29-id-skills-refresh-design.md`, the owner-approved spec.
- `docs/superpowers/specs/shell-conventions.md`, how this page is built.
- `docs/superpowers/specs/content-brief.md`, the only facts that may be published.
- `plans/PLAN.md`, the task list. Session 4 is what is left.

## Completed so far

**Session 1** removed the seven retired panels (`1-id-architect` through
`6-id-qa-auditor` and `rlo-taxonomy`) and their sidebar entries, renamed
`content-development-workflow` to `session-pipeline` and `pipeline-overview` to
`coursefactory-overview`, added nine placeholder panels with sidebar entries, and
changed the page title and h1. Verified at 13 panels, guard intact.

**Session 2** wrote the CourseFactory v2 parent panel plus the five stage panels, the
checkers panel, and the gates panel, and inlined two prerendered diagrams. It also
cleared all 19 dangling drill-links left by Session 1, repointing the six live ones in
the `business-overview` diagram at `#coursefactory-overview`. Verified: zero dangling
links, zero em dashes, `my-svg` count down to 3 and never increasing, guard script
passes `node --check`.

**Session 3** (dispatched, verify its result before proceeding) fills the compliance
engineering and operating panels, inlines their two diagrams, corrects the delivery
panel's SVG (removes the price, changes retention from four years to two), and updates
the business overview with current facts and the extended milestone table.

**Diagrams** are authored, rendered, and committed: `diagrams/*.mmd` sources,
`diagrams/rendered/*.svg` outputs, `diagrams/puppeteer.json` config. All four carry
unique self-scoped SVG ids.

## Remaining work: Session 4

Execute the "Session 4" section of `plans/PLAN.md` in order. In short:

1. **Mobile audit** at 360, 390, and 430px. No horizontal body scroll, tables stack into
   cards, tap targets 44px or larger, diagrams open legibly. Fix only by adding rules at
   the END of the main stylesheet.
2. **Fill `session-pipeline`** if Session 2 left it stale. Content is in the content
   brief under "Panel 2". Plan mode, the model switch inside the same session, the three
   skills reserved for genuine decision forks. No mention of any earlier pipeline
   generation.
3. **Update `index.html`.** The linking card copy, alt text, and prose near lines
   1612-1663, 2036, and 2088 currently say "six-stage AI pipeline". Rewrite for
   CourseFactory v2. Regenerate `img/id-skills-pipeline.svg` from
   `diagrams/rendered/coursefactory-overview.svg` if the old thumbnail no longer
   represents the page.
4. **Full verification**, the command block at the top of this file plus `node --check`
   on the extracted guard script.
5. **GATE.** Present the finished page to the owner. Do not merge, do not push. State
   plainly that pushing publishes to GitHub Pages.

## Decisions and constraints discovered

- **Never `Read` a line range in `id-skills.html` that might straddle an inline SVG.**
  Two subagents burned large amounts of context this way. Use `grep -n` to find
  boundaries, then `sed -n 'NNNp' id-skills.html | cut -c1-200` to inspect a line.
- **Inline SVGs into the page with a python substitution script**, never by reading the
  SVG into context and pasting it.
- **Responsive CSS must go at the very end of the main stylesheet.** Base rules such as
  `.path-table` appear later in source than the mid-sheet media blocks, so a mobile rule
  placed earlier loses at equal specificity even inside a media query. Source order wins.
- **mermaid-cli needs two workarounds**, both already solved and recorded in
  `plans/PLAN.md`: run it with `dangerouslyDisableSandbox: true` because npm writes its
  cache outside the sandbox, and pass `-p diagrams/puppeteer.json` because its bundled
  puppeteer asks for a Chrome build that is not installed. Always pass `--svgId`.
- **Backgrounding a local http server also needs `dangerouslyDisableSandbox: true`** (the
  sandbox blocks its `nice()` call). Bind to 127.0.0.1 and stop it before finishing.
- **Facts that must not ship**, decided from source conflicts: the course price (sources
  disagree, $29 versus $58), any claim of "seven checkers" (only six are confirmed as
  named scripts), and any suggestion the Spanish course is TDLR-approved (it is not).
  Also never publish entity file numbers, EIN, or server IP addresses.
- **The delivery diagram had two factual errors** carried from the old page: a hardcoded
  price and a four-year retention claim where the regulation says two years.
- A PostToolUse hook re-runs guard hardening after edits to `id-skills.html`. It is
  idempotent, but check `git status` before any branch operation.
- Known pre-existing defect, out of scope: three inlined SVGs still share
  `id="my-svg"`. Do not add to that count; new SVGs get unique ids.

## Exact next step

Run the verification block at the top of this file. If it passes, execute Session 4
Step 1 of `plans/PLAN.md`: the mobile audit at 360px, adding any fixes only at the end
of the main stylesheet.

## Pending gate

`GATE: Session 4 Step 5.` The owner reviews the finished page before anything is merged
or pushed. Pushing to `main` publishes to GitHub Pages. No session may advance this gate
on its own.

---

## Update: sessions 3 and 4 complete (2026-07-29)

All PLAN.md work is done except the final human gate. Commits `164687b`, `d281053`,
`1243136`, `d336c29` on `coursefactory-v2-refresh`. Nothing pushed.

Final verification, all passing:
- 13 panels, 0 placeholders, 0 orphan anchors, guard markers intact, guard script
  passes `node --check`.
- 0 em dashes in `id-skills.html` and `index.html`.
- 0 references to the retired id-* skills, RLO taxonomy, Thinkific, or NotebookLM.
- 0 occurrences of the disputed price; retention corrected to two years.
- `id="my-svg"` collisions reduced from 11 to 2 (never increased).
- No horizontal overflow at 360, 390, or 430px; no tap target under 44px.

Two problems found and fixed during session 4 that earlier sessions missed: the
`session-pipeline` panel still carried a diagram naming the six retired id-* skills, now
replaced by `diagrams/session-pipeline.mmd`; and the sidebar still carried stale labels
and "Placeholder" subtitles.

WATERFALL: COMPLETE (pending the gate below)

GATE: The owner reviews the page before anything merges or pushes. Pushing to `main`
publishes to GitHub Pages.
