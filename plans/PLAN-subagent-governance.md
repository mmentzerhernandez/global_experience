# Plan: add "Subagent Governance" to the Business Operations section

**Target file:** `/Users/rabies/global_experience/id-skills.html`
**Section:** `<section class="panel" id="operating-system">` (starts line 2847)
**Source content:** `/Users/rabies/Desktop/BehavioralChanges.txt`
**New diagram source:** `/Users/rabies/global_experience/diagrams/op-subagents.mmd`
**New rendered SVG:** `/Users/rabies/global_experience/diagrams/rendered/op-subagents.svg`

## What exists today

The Business Operations panel runs as alternating prose block + `<div class="canvas">`
inline SVG pairs, in this order:

| Line | Heading | Diagram id |
|------|---------|------------|
| 2854 | Folders as Workstreams | `op-folders-svg` |
| 2866 | Three Tier Wiki | `op-wiki-tiers-svg` |
| 2878 | One Fact, One Home | `op-one-fact-svg` |
| 2889 | Session Waterfall | `op-waterfall-svg` |
| 2901 | Self Improvement Loop | `op-improvement-svg` |
| 2923 | How Plans are Made & Run | (text/table) |
| 2940 | What Makes a Plan Actually Finished | (text/table) |
| 2957 | How Plans are Organized | (text/table) |
| 2994 | Which Emails Get Sent | `op-emails-svg` |
| 3015 | Continuity | (text) |

Diagrams are Mermaid sources in `diagrams/`, rendered offline, then the resulting
`<svg>` is pasted inline into the HTML. There is no build step at page load.

## Placement decision

Insert the new subsection **after "Self Improvement Loop" (ends ~line 2915) and before
"How Plans are Made & Run" (line 2923)**.

Reasoning: the first five subsections describe where knowledge lives and how a session
carries it forward; the plan subsections describe how work gets executed. Who is allowed
to execute that work, and how many of them at once, is the hinge between the two. It reads
as the answer to "so who actually does the work" right before the plan mechanics explain
what they do.

## Content to write (3 steps, sequential)

The source file gives the same material three ways: technical detail, plain language, and
a flowchart. The page audience is non-technical, so the prose follows the plain-language
version and the diagram carries the specifics. House voice: short declaratives, no em
dashes, no bold spray.

Heading: `Subagent Governance`

Lead paragraph (~2 sentences): before August 2026 an agent could spin up as many helpers
as it wanted, in the background, and self-report success. Three changes, applied in order,
replaced that with a hard ceiling and evidence-based verification.

Then three numbered steps, one short paragraph each:

1. **Hard caps, enforced by settings.** Three agents at once, at most one nested layer of
   helpers, no background work. These are machine-enforced in `~/.claude/settings.json`,
   not conventions, so a session cannot talk its way past them.
2. **Behavior rules on top.** Each agent finishes before the next step starts. No agent
   spawns its own helpers. Finished work is credited only against real artifacts, files on
   disk, exit codes, or the audit log, never against the agent's own summary. Hitting any
   limit is reported on a `CEILING:` line rather than absorbed silently, and a run that
   produces no artifacts counts as failed, not as "nothing needed doing."
3. **Routing by task type.** Before dispatch, each phase is classified by one test: would
   rerunning it produce a different answer? Yes means judgment, and it goes to the careful
   architect agent whose output must land in the manifest. No means mechanical, and it goes
   to the cheap executor.

Closing line: the net effect is smaller batches, checked evidence, and a clean stop at the
limit instead of an unchecked run.

## Diagram

Author `diagrams/op-subagents.mmd` as `flowchart TD` following the same frontmatter block
every other `op-*.mmd` file uses (theme base, primaryColor `#f0f3ff`, primaryBorderColor
`#002fa7`, lineColor `#002fa7`, the system font stack).

Do not reuse the palette in `BehavioralChanges.txt`. That flowchart's classDefs
(`trigger`, `n8n`, `api`, `ai`, `excel`, `alert`, `req`) come from a different document and
would clash. Restyle onto the house classDefs already used across `diagrams/*.mmd`:
`people`, `access`, `course`, `enforce`, `report`, `sweep`, `gate`.

Shape, left to right in reading order:

- Start node: "Before August 2026, agents could fan out with few limits" as `people`.
- Three ordered stages, each an `access` node with its consequences as child nodes:
  1 Hard caps → three at once / one nested layer / no background work
  2 Behavior rules → finish before next step / no self-spawning / verify against artifacts
    / report the ceiling
  3 Routing → a `gate` diamond "Would a rerun give a different answer?" branching Yes to
    "architect agent" and No to "executor agent"
- All branches converge on a single `enforce` result node: "smaller batches, checked
  evidence, clean stop at limits."

Keep node label text short. The source diagram's labels are long enough to blow past the
~586px max-width the other diagrams sit at, so trim each to roughly five words and use
`<br/>` where a break helps.

Render with the recipe from `plans/PLAN.md` (needs `dangerouslyDisableSandbox: true`):

```
npx -y @mermaid-js/mermaid-cli -i diagrams/op-subagents.mmd \
  -o diagrams/rendered/op-subagents.svg --svgId op-subagents-svg \
  -b transparent -p diagrams/puppeteer.json
```

`--svgId op-subagents-svg` is required. Every scoped style rule in the page keys off that id.

## Steps

1. Write `diagrams/op-subagents.mmd`.
2. Render it to `diagrams/rendered/op-subagents.svg` with the command above.
3. Check the rendered viewBox width. If it exceeds ~600px, shorten labels and re-render
   rather than letting the diagram set a wider column than its neighbors.
4. Insert into `id-skills.html` between line 2915 and 2923: the prose `<div>` copying the
   exact inline style of its siblings (`max-width: 800px; margin: 0 0 8px; line-height:
   1.6; color: #333`, `<h3 style="color: #1a202c; margin-bottom: 8px">`), then a
   `<div class="canvas">` holding the pasted SVG verbatim.
5. Add `#operating-system .canvas svg#op-subagents-svg` to the three-selector label rule
   group at lines 632 to 643, matching the existing `.nodeLabel`, `.nodeLabel p`, and
   `foreignObject > div` pattern. Skipping this leaves the new diagram's label typography
   out of step with the other five.
6. Verify: serve locally (`python3 -m http.server 8080`), load
   `http://localhost:8080/id-skills.html#operating-system`, confirm at 360px width and at
   desktop that the diagram scales, the labels are legible, and no horizontal scroll
   appears on the page body.

## Constraints

- Mobile-first, authored at 360px. Any responsive override goes at the end of the main
  stylesheet, never mid-sheet.
- No em dashes anywhere, including inside diagram node labels.
- No external requests at runtime. The SVG is inlined, not linked.
- Read taste-skill v2 §11 Redesign Protocol, Preserve mode, before writing HTML or CSS.
- Do not touch the other five `op-*` diagrams or their sources.

## Open question

The source text names absolute paths (`~/.claude/settings.json`,
`~/.claude/rules/subagent-governance.md`, the audit log under `~/Library/Logs`). Every
other subsection in this panel names paths freely, so the plan above keeps one path
reference in step 1 and drops the rest. Say so if you want all three surfaced instead.
