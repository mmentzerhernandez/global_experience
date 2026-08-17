# automated-curriculum-development-business.html Business Operations section: narrative arc rewrite

Written 16 Aug 2026. Original plan. Never edit the text, only mark items `[x]`.

> **For agentic workers:** execute one session at a time, inline, plus at most one
> reviewer subagent that reviews the whole session diff before the handoff. Do not
> dispatch per-task implementer subagents. Stop at 50% context and follow the
> checkpoint procedure in `~/.claude/CLAUDE.md`. Never `Read` a line range of
> `automated-curriculum-development-business.html` that can contain an inline SVG. Use `grep -n` to find a line, then
> `sed -n 'NNNp' automated-curriculum-development-business.html | cut -c1-200` to look at it.

**Goal:** Rename `id-skills.html` to `automated-curriculum-development-business.html`
with a redirect from the old URL, then rewrite the `#operating-system` panel of
`/Users/rabies/global_experience/automated-curriculum-development-business.html` so that its ten sections follow the
narrative arc Foundation, Structure, Workflow, Execution, Systems, Communication,
Improvement, Resilience, so that every sentence follows ASD-STE100 Strict mode, and
so that every diagram shows the current folder numbering, the mistakes ledger, and
the current operating rules.

**Architecture:** The page is one static file with no build step. Task 0 renames it
with `git mv` and leaves a small stub at the old name that forwards the browser,
fragment included, to the new name. GitHub Pages has no server-side redirect, so the
stub is the redirect. The panel is
lines 2850 to 3047 today: prose blocks in inline-styled `<div>`s, each followed by a
`<div class="canvas">` that holds one pre-rendered Mermaid SVG. Diagram sources live in
`/Users/rabies/global_experience/diagrams/*.mmd`, and mermaid-cli renders them to
`diagrams/rendered/*.svg`. The work has three layers: rewrite the nine diagram sources
and render them, replace the panel prose with new arc-ordered HTML that carries empty
canvas placeholders, then inline each SVG into its placeholder with a small Python
script. A shell verification script checks every invariant after each task.

**Tech stack:** Plain HTML and CSS. Mermaid sources rendered offline with
`npx -y @mermaid-js/mermaid-cli`. Python 3.11 for the inline step. zsh for checks.

## Global constraints

- Task 0 renames the page. From then on the target page is
  `/Users/rabies/global_experience/automated-curriculum-development-business.html`. The old name
  `/Users/rabies/global_experience/id-skills.html` becomes a 14-line redirect stub and
  never holds content again. Diagram sources:
  `/Users/rabies/global_experience/diagrams/`. Rendered SVGs:
  `/Users/rabies/global_experience/diagrams/rendered/`. Repository root:
  `/Users/rabies/global_experience`, branch `main`.
- Never emit an em dash. Not in prose, not in HTML, not in a diagram label, not in a
  commit message. Use a comma, a colon, or a period.
- Every human-facing sentence follows ASD-STE100 Strict mode: active voice, one
  instruction per sentence, no idiom, no phrasal verb, no semicolon, no figurative
  word. Full rule set: `/Users/rabies/.claude/skills/asd-ste100/SKILL.md`. Copy the
  prose in this plan verbatim. Do not paraphrase it.
- Every Mermaid box holds one short line. No `<br>` and no `<br/>` in any node
  label. No number prefix that acts as a step number. Labels of about eight words.
  Edge labels of three words or fewer. Detail goes in the prose under the diagram.
  Folder names such as `1-AboutTheBusiness` are names, not step numbers, and stay
  verbatim.
- Keep every existing SVG id: `op-one-fact-svg`, `operating-loop-svg`,
  `op-folders-svg`, `op-waterfall-svg`, `op-subagents-svg`, `op-wiki-tiers-svg`,
  `op-emails-svg`, `op-improvement-svg`. The one new diagram is `op-continuity-svg`.
  The CSS allowlist at lines 632 to 646 references five of these ids by name.
- Do not add an `id` attribute to any `<h3>` or `<p>` inside the panel. Panel
  switching is `:target` based. A fragment link to a sub-heading would hide the
  panel.
- Do not touch the `mermaid-wiki-guard` script (lines 3412 to 3680) or the
  `:target` CSS (lines 207 to 219). A PostToolUse hook re-runs guard hardening after
  each edit to the page. It is idempotent. Run `git status` before any branch action.
- Section names inside the panel are fixed by the owner and used verbatim:
  Single Source of Truth, Workstream Architecture, Folder-Based Workstreams,
  Session Waterfall Workflow, Plan Execution Lifecycle, Completion Criteria & Quality
  Gates, Agent Governance System, Three-Tier Knowledge Base, Automated Communication
  Protocols, Continuous Improvement Cycle, Operational Continuity Framework. In HTML,
  write the ampersand as `&amp;`.
- Facts in the prose come from these files and were checked on 16 Aug 2026:
  `~/.claude/CLAUDE.md`, `~/.claude/rules/subagent-governance.md`,
  `~/.claude/rules/manifest-discipline.md`,
  `/Users/rabies/Desktop/IERHUB.com/CLAUDE.md`,
  `/Users/rabies/Desktop/IERHUB.com/10-Plans/README.md`,
  `/Users/rabies/Desktop/IERHUB.com/13-Mistakes/mistakes.md`,
  `/Users/rabies/Desktop/IERHUB.com/10-Plans/SkillProposals/PROPOSALS.md`,
  `/Users/rabies/Desktop/IERHUB.com/_Continuity/CONTINUITY.md`,
  `/Users/rabies/Desktop/IERHUB.com/15-OvernightRunner/15-overnight-runner/README.md`,
  `/Users/rabies/Desktop/IERHUB.com/Wiki/index.md`. Do not add a fact that is not in
  this plan. If a fact looks wrong, stop and report it in the handoff. Do not guess.
- Never publish an entity file number, an EIN, a server IP, a price, or a claim that
  the Spanish course is TDLR approved.
- Do not commit or push without the owner's approval. A push publishes to GitHub
  Pages at `https://mmentzerhernandez.github.io/global_experience/automated-curriculum-development-business.html`.

## Diagram render recipe

The recipe from the July plan still works with one change: the pinned Chrome build
moved. `diagrams/puppeteer.json` names
`mac_arm-150.0.7871.24`, and only `mac_arm-152.0.7977.42` exists under
`~/.cache/puppeteer/chrome-headless-shell/`. Task 2 fixes the config first.

```
cd /Users/rabies/global_experience
npx -y @mermaid-js/mermaid-cli -i diagrams/<name>.mmd \
  -o diagrams/rendered/<name>.svg --svgId <name>-svg \
  -b transparent -p diagrams/puppeteer.json
```

Run this command with `dangerouslyDisableSandbox: true`. npm writes its cache outside
the sandbox. Always pass `--svgId`. It gives the SVG a unique id and prefixes every
selector inside the embedded `<style>` with that id.

## Sessions

Session 1: Task 0, Task 1, and Task 2 (rename and redirect, verification script, all nine diagrams). Session 2:
Task 3, Task 4, Task 5 (panel HTML, inline SVGs, sidebar entry). Session 3: Task 6
(full verification, browser check, reviewer subagent, owner gate). Combine sessions
only if context stays under 50%.

---

### Task 0: Rename the page and redirect the old URL

GitHub Pages serves static files only. It cannot send a server redirect. The old
name stays as a small stub that forwards the browser to the new name and keeps the
`#fragment`, because the page selects its panel from the fragment.

**Files:**
- Rename: `/Users/rabies/global_experience/id-skills.html` to
  `/Users/rabies/global_experience/automated-curriculum-development-business.html`
- Create: `/Users/rabies/global_experience/id-skills.html` (the redirect stub)
- Modify: `/Users/rabies/global_experience/index.html:1725`, `:1764`, `:2079`, `:2131`
- Modify: `/Users/rabies/global_experience/sitemap.xml:10`

**Interfaces:**
- Produces: the page at the new path. Every later task edits the new path only.

- [x] **Step 1: Rename with git so git keeps the file history**

Run:
```
cd /Users/rabies/global_experience && git mv id-skills.html automated-curriculum-development-business.html && git status --short
```
Expected: `R  id-skills.html -> automated-curriculum-development-business.html`.

- [x] **Step 2: Write the redirect stub at the old name**

Write this file, exactly 14 lines, to `/Users/rabies/global_experience/id-skills.html`.
Use the Write tool or a heredoc. The `<script>` line runs first and keeps the
fragment and the query string. The `<meta http-equiv="refresh">` line is the
fallback when scripts are off. The link is the fallback for everything else.
`noindex` tells search engines to remove the old URL from their index. The canonical link names the new
one.

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Moved: Automating Curriculum Development as a Business</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="https://mmentzerhernandez.github.io/global_experience/automated-curriculum-development-business.html">
<script>location.replace("automated-curriculum-development-business.html" + location.search + location.hash)</script>
<meta http-equiv="refresh" content="0; url=automated-curriculum-development-business.html">
</head>
<body>
<p>This page moved. Open <a href="automated-curriculum-development-business.html">the new page</a>.</p>
</body>
</html>
```

Run: `grep -c '' /Users/rabies/global_experience/id-skills.html && grep -c 'automated-curriculum-development-business.html' /Users/rabies/global_experience/id-skills.html`
Expected: `14` and `4`. If the guard hook appended anything to the stub, remove it.
The stub holds no diagram and must stay 14 lines.

- [x] **Step 3: Update the links in index.html and sitemap.xml**

Four places name the old file. Replace each in place with `sed`, then confirm.

Run:
```
cd /Users/rabies/global_experience && sed -i '' 's#id-skills\.html#automated-curriculum-development-business.html#g' index.html sitemap.xml && grep -n 'automated-curriculum-development-business.html' index.html sitemap.xml | cut -c1-160
```
Expected: five lines, four in `index.html` (near 1725, 1764, 2079, 2131) and one in
`sitemap.xml` (line 10). The image `img/id-skills-pipeline.svg` keeps its name. It is
an asset, not a URL the owner asked to change.

- [x] **Step 4: Confirm the diff is only the rename**

Run: `cd /Users/rabies/global_experience && git status --short && git diff --stat`
Expected: the rename, the new stub as untracked or added, and small diffs in
`index.html` and `sitemap.xml`. Nothing else.

- [x] **Step 5: Confirm the redirect keeps the fragment**

Run with `dangerouslyDisableSandbox: true` and stop it before the turn ends:
```
cd /Users/rabies/global_experience && python3 -m http.server 8765 --bind 127.0.0.1 >/dev/null 2>&1 &
```
Open `http://127.0.0.1:8765/id-skills.html#operating-system` in the browser.
Expected: the address bar changes to
`http://127.0.0.1:8765/automated-curriculum-development-business.html#operating-system`
and the Business Operations panel is the visible one. Then stop the server with
`pkill -f "http.server 8765"`.

---

### Task 1: Verification script

**Files:**
- Create: `/Users/rabies/global_experience/plans/verify-ops-section.sh`

**Interfaces:**
- Produces: one zsh script that exits 0 only when every invariant in this plan holds.
  Every later task ends by running it. Until Task 4 lands it is expected to fail on
  the title and SVG checks. Read which lines say `FAIL` and confirm they are the ones
  the current task has not reached yet.

- [x] **Step 1: Write the script**

```zsh
#!/bin/zsh
# Verification for plans/PLAN.md, automated-curriculum-development-business.html Business Operations rewrite.
set -u
F=/Users/rabies/global_experience/automated-curriculum-development-business.html
D=/Users/rabies/global_experience/diagrams
fail=0
chk() { if [ "$1" != "$2" ]; then echo "FAIL: $3 (got $1, want $2)"; fail=1; else echo "ok:   $3"; fi }

chk "$(grep -c $'\u2014' "$F")" 0 "no em dash in the page"
chk "$(cat "$D"/op-*.mmd "$D"/operating-loop.mmd | grep -c $'\u2014')" 0 "no em dash in diagram sources"
chk "$(cat "$D"/op-*.mmd "$D"/operating-loop.mmd | grep -c '<br')" 0 "no <br> in diagram sources"

for t in "One Fact, One Home" "Session Waterfall</h3>" "Self Improvement Loop" \
         "Subagent Governance</h3>" "How Plans are Made" "What Makes a Plan Actually Finished" \
         "How Plans are Organized" "Folders as Workstreams" "Three Tier Wiki" \
         "Which Emails Get Sent" ">Continuity</h3>"; do
  chk "$(grep -c "$t" "$F")" 0 "old title gone: $t"
done

for t in "Single Source of Truth" "Workstream Architecture" "Folder-Based Workstreams" \
         "Session Waterfall Workflow" "Plan Execution Lifecycle" \
         "Completion Criteria &amp; Quality Gates" "Agent Governance System" \
         "Three-Tier Knowledge Base" "Automated Communication Protocols" \
         "Continuous Improvement Cycle" "Operational Continuity Framework"; do
  chk "$(grep -cE "<h3 style=\"color: #1a202c; margin: (0|32px) 0 8px\">$t</h3>" "$F")" 1 "new title once: $t"
done

for k in Foundation Structure Workflow Execution Systems Communication Improvement Resilience; do
  chk "$(grep -c "class=\"arc-kicker\">$k</p>" "$F")" 1 "arc kicker once: $k"
done

for id in op-one-fact-svg operating-loop-svg op-folders-svg op-waterfall-svg \
          op-subagents-svg op-wiki-tiers-svg op-emails-svg op-improvement-svg op-continuity-svg; do
  chk "$(grep -c "<svg id=\"$id\"" "$F")" 1 "svg inlined once: $id"
  [ -s "$D/rendered/${id%-svg}.svg" ] && echo "ok:   rendered file exists: ${id%-svg}.svg" \
    || { echo "FAIL: rendered file missing: ${id%-svg}.svg"; fail=1; }
done

chk "$(grep -c 'data-diagram=' "$F")" 0 "no empty diagram placeholder left"
chk "$(grep -c 'Memory, Waterfall, Wiki' "$F")" 0 "old sidebar blurb gone"

# Rename and redirect (Task 0)
R=/Users/rabies/global_experience
if [ -s "$F" ]
then
  echo "ok:   new page exists"
else
  echo "FAIL: new page missing"
  fail=1
fi
chk "$(grep -c '' "$R/id-skills.html")" 14 "old name is the 14-line redirect stub"
chk "$(grep -c 'automated-curriculum-development-business.html' "$R/id-skills.html")" 4 "stub points at the new name four times"
chk "$(cat "$R/index.html" "$R/sitemap.xml" | grep -c 'id-skills.html')" 0 "no old link in index.html or sitemap.xml"
chk "$(grep -c 'automated-curriculum-development-business.html' "$R/index.html")" 4 "index.html links the new name four times"
chk "$(grep -c 'automated-curriculum-development-business.html' "$R/sitemap.xml")" 1 "sitemap lists the new name once"

sed -n '/mermaid-wiki-guard:start/,/mermaid-wiki-guard:end/p' "$F" \
  | sed '1,/<script>/d' | sed '/<\/script>/,$d' > "${TMPDIR:-/tmp}/guard-check.js"
node --check "${TMPDIR:-/tmp}/guard-check.js" && echo "ok:   guard script parses" \
  || { echo "FAIL: guard script does not parse"; fail=1; }

exit $fail
```

- [x] **Step 2: Make it executable and run it**

Run: `chmod +x /Users/rabies/global_experience/plans/verify-ops-section.sh && /Users/rabies/global_experience/plans/verify-ops-section.sh; echo "exit $?"`

Expected now: `FAIL` on every "old title gone" line, every "new title once" line,
every "arc kicker once" line, `op-continuity-svg` inlined and rendered, and "old
sidebar blurb gone". `ok` on the em dash lines and the guard script line. Exit 1.

---

### Task 2: Rewrite and render the nine diagram sources

Every source below replaces the whole file. Copy each block verbatim, front matter
included. The classDef families are the ones the page already uses. Each label is one
line. The prose in Task 3 carries the detail the old multi-line labels held.

**Files:**
- Modify: `/Users/rabies/global_experience/diagrams/puppeteer.json`
- Modify: `/Users/rabies/global_experience/diagrams/op-one-fact.mmd`
- Modify: `/Users/rabies/global_experience/diagrams/operating-loop.mmd`
- Modify: `/Users/rabies/global_experience/diagrams/op-folders.mmd`
- Modify: `/Users/rabies/global_experience/diagrams/op-waterfall.mmd`
- Modify: `/Users/rabies/global_experience/diagrams/op-subagents.mmd`
- Modify: `/Users/rabies/global_experience/diagrams/op-wiki-tiers.mmd`
- Modify: `/Users/rabies/global_experience/diagrams/op-emails.mmd`
- Modify: `/Users/rabies/global_experience/diagrams/op-improvement.mmd`
- Create: `/Users/rabies/global_experience/diagrams/op-continuity.mmd`
- Regenerate: `/Users/rabies/global_experience/diagrams/rendered/<name>.svg` for each

**Interfaces:**
- Produces: nine SVG files whose root element is `<svg id="<name>-svg" ...>`. Task 4
  reads them by that id.

- [x] **Step 1: Set puppeteer.json to the installed Chrome**

Replace the whole file with:

```json
{"executablePath":"/Users/rabies/.cache/puppeteer/chrome-headless-shell/mac_arm-152.0.7977.42/chrome-headless-shell-mac-arm64/chrome-headless-shell","args":["--no-sandbox"]}
```

Run: `test -x /Users/rabies/.cache/puppeteer/chrome-headless-shell/mac_arm-152.0.7977.42/chrome-headless-shell-mac-arm64/chrome-headless-shell && echo present`
Expected: `present`. If not, run `ls ~/.cache/puppeteer/chrome-headless-shell/` and
put the directory you find into the path.

- [x] **Step 2: Write `op-one-fact.mmd`**

```
---
config:
  theme: base
  themeVariables:
    primaryColor: "#f0f3ff"
    primaryBorderColor: "#002fa7"
    primaryTextColor: "#2c3e50"
    lineColor: "#002fa7"
    fontFamily: "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif"
---
flowchart TD
    FACT["A new fact appears"]:::people
    KIND{{"What kind of fact is it?"}}:::gate

    D["A decision"]:::access
    P["Progress on a plan"]:::access
    K["Business knowledge"]:::access
    C["A code relationship"]:::access
    R["A retired term"]:::access

    DM["The manifest, .claude/manifest.json"]:::report
    PM["The plan folder, PLAN.md and handoffs"]:::enforce
    KM["The owning wiki"]:::course
    CM["The generated knowledge graph"]:::sweep
    RM["10-Plans/RETIRED-TERMS.md"]:::report

    FACT --> KIND
    KIND --> D --> DM
    KIND --> P --> PM
    KIND --> K --> KM
    KIND --> C --> CM
    KIND --> R --> RM

    classDef people fill:#ECEFF1,stroke:#455A64,color:#000000
    classDef access fill:#E3F2FD,stroke:#1565C0,color:#000000
    classDef course fill:#E8F5E9,stroke:#2E7D32,color:#000000
    classDef enforce fill:#FFF3E0,stroke:#E65100,color:#000000
    classDef report fill:#FFEBEE,stroke:#C62828,color:#000000
    classDef sweep fill:#F3E5F5,stroke:#6A1B9A,color:#000000
    classDef gate fill:#F9A825,stroke:#7A5200,color:#1A1200,stroke-width:2px
```

- [x] **Step 3: Write `operating-loop.mmd`**

```
---
config:
  theme: base
  themeVariables:
    primaryColor: "#f0f3ff"
    primaryBorderColor: "#002fa7"
    primaryTextColor: "#2c3e50"
    lineColor: "#002fa7"
    fontFamily: "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif"
  flowchart:
    nodeSpacing: 55
    rankSpacing: 70
---
flowchart TD
    OWNER["The owner approves a goal"]:::people
    FUT["FuturePlans, one dated file per plan"]:::access
    CUR["CurrentPlans, one folder per plan set"]:::enforce
    WATERFALL["Sessions work the plan and write handoffs"]:::enforce
    BOARD["Tasks/WORK-STATUS.md indexes the active sets"]:::access
    DOD{{"Does the set meet the definition of done?"}}:::gate
    REVIEW["Review the whole set for mistakes"]:::note
    DRIFT["check-drift.sh flags a false completion"]:::refuse
    PAST["PastPlans, plan and handoff trail kept"]:::course
    INACT["InactivePlans, paused or superseded"]:::report
    MAP["MIGRATION-MAP.md logs every move"]:::report

    OWNER --> FUT
    FUT -->|"Kickoff moves it"| CUR
    CUR --> WATERFALL
    WATERFALL -->|"Next session"| CUR
    CUR -->|"Indexed by"| BOARD
    CUR --> DOD
    DOD -->|"Yes"| REVIEW --> PAST
    DOD -->|"Paused"| INACT
    DOD -->|"Marked, not met"| DRIFT
    DRIFT -->|"Repair"| CUR
    PAST --> MAP

    classDef people fill:#ECEFF1,stroke:#455A64,color:#000000,stroke-width:2px
    classDef access fill:#E3F2FD,stroke:#1565C0,color:#000000,stroke-width:2px
    classDef course fill:#E8F5E9,stroke:#2E7D32,color:#000000,stroke-width:2px
    classDef enforce fill:#FFF3E0,stroke:#E65100,color:#000000,stroke-width:2px
    classDef report fill:#FFEBEE,stroke:#C62828,color:#000000,stroke-width:2px
    classDef refuse fill:#FFEBEE,stroke:#C62828,color:#000000,stroke-width:2px,stroke-dasharray: 5 5
    classDef note fill:#FFFDE7,stroke:#9E9D24,color:#000000,stroke-width:2px
    classDef gate fill:#F9A825,stroke:#7A5200,color:#1A1200,stroke-width:3px
```

- [x] **Step 4: Write `op-folders.mmd`**

The seventeen numbered folders sit in a four-column grid. Invisible edges (`~~~`)
force the columns. Numeric order runs down each column, then to the next column.

```
---
config:
  theme: base
  themeVariables:
    primaryColor: "#f0f3ff"
    primaryBorderColor: "#002fa7"
    primaryTextColor: "#2c3e50"
    lineColor: "#002fa7"
    fontFamily: "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif"
  flowchart:
    nodeSpacing: 30
    rankSpacing: 30
---
flowchart TD
    ROOT["IERHUB.com workspace"]:::people

    subgraph NUM["Numbered folders, one workstream each"]
        direction TB
        F000["000-Dashboard"]:::access
        F1["1-AboutTheBusiness"]:::access
        F2["2-Sitemap&TrafficFunnels"]:::access
        F3["3-BusinessTools"]:::access
        F4["4-Compliance"]:::access
        F5["5-CurriculumDevelopment"]:::access
        F6["6-FrontEndBackendIERhub.com"]:::access
        F7["7-SocialMedia"]:::access
        F8["8-Legal"]:::access
        F9["9-DesignFigma"]:::access
        F10["10-Plans"]:::access
        F11["11-Research"]:::access
        F12["12-Diagrams"]:::access
        F13["13-Mistakes"]:::access
        F14["14-Images"]:::access
        F15["15-OvernightRunner"]:::access
        F16["16-AdsAnalytics"]:::access
        F000 ~~~ F1 ~~~ F2 ~~~ F3 ~~~ F4
        F5 ~~~ F6 ~~~ F7 ~~~ F8 ~~~ F9
        F10 ~~~ F11 ~~~ F12 ~~~ F13
        F14 ~~~ F15 ~~~ F16
    end

    subgraph UND["Underscore folders, shared by every workstream"]
        direction TB
        UA["_Admin"]:::report
        UC["_Continuity"]:::report
        UX["_Archive"]:::report
        UK["_Credentials, one inside each folder"]:::report
        UA ~~~ UC
        UX ~~~ UK
    end

    WIKI["Wiki/index.md and 0-HitByABus.html at the root"]:::course
    ZERO["Zero-rename zones, reached by absolute path"]:::gate

    ROOT --> NUM
    ROOT --> UND
    ROOT --> WIKI
    NUM --> ZERO

    classDef people fill:#ECEFF1,stroke:#455A64,color:#000000
    classDef access fill:#E3F2FD,stroke:#1565C0,color:#000000
    classDef course fill:#E8F5E9,stroke:#2E7D32,color:#000000
    classDef report fill:#FFEBEE,stroke:#C62828,color:#000000
    classDef gate fill:#F9A825,stroke:#7A5200,color:#1A1200,stroke-width:2px
```

- [x] **Step 5: Write `op-waterfall.mmd`**

```
---
config:
  theme: base
  themeVariables:
    primaryColor: "#f0f3ff"
    primaryBorderColor: "#002fa7"
    primaryTextColor: "#2c3e50"
    lineColor: "#002fa7"
    fontFamily: "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif"
---
flowchart TD
    S1["Session 1 reads PLAN.md and works"]:::access
    HALF{{"Is half the context used?"}}:::gate
    STOP["Finish or revert the current edit"]:::enforce
    LESS["Answer the three lessons questions"]:::note
    H1["Write HANDOFF-1.md"]:::report
    CLEAR["Run /clear, never /compact"]:::enforce
    S2["Session 2 reads only the handoff"]:::access
    H2["Write HANDOFF-2.md"]:::report
    SN["Repeat until PLAN.md is fully checked"]:::course
    DONE["Final handoff says WATERFALL: COMPLETE"]:::course

    S1 --> HALF
    HALF -->|"No"| S1
    HALF -->|"Yes"| STOP --> LESS --> H1 --> CLEAR --> S2
    S2 --> H2 --> SN --> DONE

    classDef access fill:#E3F2FD,stroke:#1565C0,color:#000000
    classDef course fill:#E8F5E9,stroke:#2E7D32,color:#000000
    classDef enforce fill:#FFF3E0,stroke:#E65100,color:#000000
    classDef report fill:#FFEBEE,stroke:#C62828,color:#000000
    classDef gate fill:#F9A825,stroke:#7A5200,color:#1A1200,stroke-width:2px
    classDef note fill:#FFFDE7,stroke:#9E9D24,color:#000000
```

- [x] **Step 6: Write `op-subagents.mmd`**

```
---
config:
  theme: base
  flowchart:
    wrappingWidth: 400
    padding: 12
  themeVariables:
    primaryColor: "#f0f3ff"
    primaryBorderColor: "#002fa7"
    primaryTextColor: "#2c3e50"
    lineColor: "#002fa7"
    fontFamily: "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif"
---
flowchart TD
    START["A session wants to delegate work"]:::people

    CAP["Settings enforce the hard caps"]:::access
    CAPL["Three agents at most, no background, one nested layer"]:::report

    RULES["Eight behavior rules bind every session"]:::access
    RULESL["Foreground only, no recursion, verify from artifacts"]:::report

    ROUTE["Classify the task before dispatch"]:::access
    GATE{{"Would a rerun give a different answer?"}}:::gate
    ARCH["Architect agent writes into the manifest"]:::course
    EXEC["Executor agent does the mechanical work"]:::course

    AUDIT["The audit log records every start and stop"]:::enforce
    CEIL["Any limit hit writes a CEILING line"]:::enforce

    START --> CAP --> CAPL --> RULES --> RULESL --> ROUTE --> GATE
    GATE -->|"Yes"| ARCH
    GATE -->|"No"| EXEC
    ARCH --> AUDIT
    EXEC --> AUDIT
    AUDIT --> CEIL

    classDef people fill:#ECEFF1,stroke:#455A64,color:#000000
    classDef access fill:#E3F2FD,stroke:#1565C0,color:#000000
    classDef course fill:#E8F5E9,stroke:#2E7D32,color:#000000
    classDef enforce fill:#FFF3E0,stroke:#E65100,color:#000000
    classDef report fill:#FFEBEE,stroke:#C62828,color:#000000
    classDef gate fill:#F9A825,stroke:#7A5200,color:#1A1200,stroke-width:2px
```

- [x] **Step 7: Write `op-wiki-tiers.mmd`**

```
---
config:
  theme: base
  themeVariables:
    primaryColor: "#f0f3ff"
    primaryBorderColor: "#002fa7"
    primaryTextColor: "#2c3e50"
    lineColor: "#002fa7"
    fontFamily: "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif"
---
flowchart TD
    T1["Tier 1, Wiki/index.md, navigation and governance"]:::people
    T2["Tier 2, one wiki per workstream folder"]:::access
    T3["Tier 3, deep wiki beside the code"]:::course

    CONF{{"Do two tiers disagree?"}}:::gate
    WIN["The more specific tier wins"]:::enforce
    FIX["Fix the fact at its source"]:::enforce
    SYNC["Run /ierhub-current-state to sync upward"]:::enforce
    HTML["Rebuild 0-HitByABus.html from Tier 1"]:::report

    T3 -->|"Feeds"| T2
    T2 -->|"Feeds"| T1
    CONF -->|"Yes"| WIN --> FIX --> SYNC
    SYNC --> T1
    T1 --> HTML

    classDef people fill:#ECEFF1,stroke:#455A64,color:#000000
    classDef access fill:#E3F2FD,stroke:#1565C0,color:#000000
    classDef course fill:#E8F5E9,stroke:#2E7D32,color:#000000
    classDef enforce fill:#FFF3E0,stroke:#E65100,color:#000000
    classDef report fill:#FFEBEE,stroke:#C62828,color:#000000
    classDef gate fill:#F9A825,stroke:#7A5200,color:#1A1200,stroke-width:2px
```

- [x] **Step 8: Write `op-emails.mmd`**

Same senders, same triggers, same emails as before. Only the wording changes. Do not
add or remove an email.

```
---
config:
  theme: base
  themeVariables:
    primaryColor: "#f0f3ff"
    primaryBorderColor: "#002fa7"
    primaryTextColor: "#2c3e50"
    lineColor: "#002fa7"
    fontFamily: "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif"
---
flowchart TD
    classDef stripe fill:#dbe9ff,stroke:#3358d4,color:#122a6b;
    classDef moodle fill:#d4f4dd,stroke:#1a7f37,color:#0a3d1a;
    classDef app fill:#fff3cd,stroke:#b58900,color:#5c4400;
    classDef dormant fill:#f3e8ff,stroke:#8b5cf6,color:#4c1d95,stroke-dasharray:5 3;

    subgraph LIVE["Live today, the site payment link funnel"]
        pay["The buyer pays on the Stripe hosted link"]
        css["Stripe sends checkout.session.completed"]
        newu{"Is the buyer new or repeat?"}
        forgot["The buyer uses forgot password in Moodle"]
        rf["Stripe sends charge.refunded"]
        dp["Stripe sends charge.dispute.created"]
        form["The buyer sends the help center form"]
        lapse_near["About thirty days before the CE window lapses"]
        lapse_hit["The CE window lapses"]

        pay --> css --> newu
        pay -.->|"Dashboard toggle"| Lreceipt["Payment receipt to the buyer"]:::stripe
        newu -->|"New"| Lwelcome["Set password welcome to the buyer"]:::moodle
        newu -->|"Repeat"| Lreset["Password reset to the buyer"]:::moodle
        forgot --> Lreset2["Password reset to the buyer"]:::moodle

        rf --> Lstaffrf["Refund alert to staff"]:::app
        rf -.->|"Dashboard toggle"| Lsrefund["Refund receipt to the buyer"]:::stripe
        dp --> Lstaffdp["Dispute alert to staff"]:::app
        dp -.->|"Stripe side"| Lop["Payment or dispute alert to the operator"]:::stripe
        form --> Lform["Contact message to staff, reply to buyer"]:::app

        lapse_near -->|"Default on"| Lprelapse["Renewal reminder to the buyer"]:::moodle
        lapse_hit -->|"local_recompletion"| Lreset3["CE reset notice to the buyer"]:::moodle
    end

    complete["The buyer finishes four modules"] --> Lcert["Certificate email to the buyer"]:::moodle

    subgraph DORM["Built but dormant, Moodle payment gateway suite"]
        dcss["Moodle native payment, enrol_fee hook"] -->|"send_receipt"| Dreceipt["Branded TDLR receipt to the buyer"]:::dormant
        drf["Mapped charge.refunded webhook"] -->|"send_refund"| Drefund["Refund notice to buyer and staff"]:::dormant
        drf2["Unmapped webhook, fail safe"] -->|"unmapped_alert"| Dunmapped["Manual action needed, to staff"]:::dormant
        ddp["Dispute webhook"] -->|"send_dispute_alert"| Ddispute["Dispute alert to staff"]:::dormant
    end

    subgraph LEGEND["Legend"]
        g1["Sent by Stripe, dashboard toggle"]:::stripe
        g2["Sent by Moodle LMS"]:::moodle
        g3["Sent by the application"]:::app
        g4["Built but dormant"]:::dormant
    end
```

- [x] **Step 9: Write `op-improvement.mmd`**

```
---
config:
  theme: base
  themeVariables:
    primaryColor: "#f0f3ff"
    primaryBorderColor: "#002fa7"
    primaryTextColor: "#2c3e50"
    lineColor: "#002fa7"
    fontFamily: "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif"
---
flowchart TD
    CAP["Each handoff answers three lessons questions"]:::access
    ERR{{"Does a lesson come from a real error?"}}:::gate
    LEDGER["Append an entry to 13-Mistakes/mistakes.md"]:::report
    MEM["A durable lesson becomes a feedback memory"]:::note
    PROP["Stage a proposal in PROPOSALS.md as proposed"]:::report
    GATE{{"Owner morning pass"}}:::gate
    FROZEN["Rejected or untouched entries stay frozen"]:::note
    APPLY["An executor applies the exact diff after a backup"]:::enforce
    CODIFY["The ledger entry becomes codified"]:::course
    MEASURE["The Monday review scores the targeted metric"]:::course
    REVERT["Two flat reviews make it a revert candidate"]:::note
    SWEEP["A monthly sweep checks every open entry"]:::access

    CAP --> ERR
    ERR -->|"Yes"| LEDGER --> PROP
    ERR -->|"No"| MEM
    CAP --> PROP --> GATE
    GATE -->|"Approved"| APPLY --> MEASURE
    GATE -->|"Rejected"| FROZEN
    APPLY --> CODIFY
    MEASURE -->|"No movement twice"| REVERT
    REVERT -.-> GATE
    LEDGER --> SWEEP

    classDef access fill:#E3F2FD,stroke:#1565C0,color:#000000
    classDef course fill:#E8F5E9,stroke:#2E7D32,color:#000000
    classDef enforce fill:#FFF3E0,stroke:#E65100,color:#000000
    classDef report fill:#FFEBEE,stroke:#C62828,color:#000000
    classDef gate fill:#F9A825,stroke:#7A5200,color:#1A1200,stroke-width:2px
    classDef note fill:#FFFDE7,stroke:#9E9D24,color:#000000
```

- [x] **Step 10: Create `op-continuity.mmd`**

```
---
config:
  theme: base
  themeVariables:
    primaryColor: "#f0f3ff"
    primaryBorderColor: "#002fa7"
    primaryTextColor: "#2c3e50"
    lineColor: "#002fa7"
    fontFamily: "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif"
---
flowchart TD
    JOB["launchd fires sync.sh at 12:00 daily"]:::access
    SCAN["Scan the workspace for changes"]:::access
    LOG["Write one changelog per mirrored folder"]:::report
    ALLOW["Copy only allowlisted folders into mirror/"]:::enforce
    SECRET{{"Does the secret gate find a credential?"}}:::gate
    BLOCK["Block the commit and report"]:::report
    RENDER["Render wiki.html from the mirror"]:::course
    BEAT["Write today's date to heartbeat.txt"]:::course
    PUSH["Commit and push to the private repository"]:::course
    DEAD{{"Did seven days pass with no commit?"}}:::gate
    ISSUE["The dead-man action opens an issue for the successor"]:::report
    RUNBOOK["CONTINUITY.md tells a successor what to do"]:::note

    JOB --> SCAN --> LOG --> ALLOW --> SECRET
    SECRET -->|"Yes"| BLOCK
    SECRET -->|"No"| RENDER --> BEAT --> PUSH --> DEAD
    DEAD -->|"Yes"| ISSUE
    DEAD -->|"No"| JOB
    RUNBOOK -.-> ISSUE

    classDef access fill:#E3F2FD,stroke:#1565C0,color:#000000
    classDef course fill:#E8F5E9,stroke:#2E7D32,color:#000000
    classDef enforce fill:#FFF3E0,stroke:#E65100,color:#000000
    classDef report fill:#FFEBEE,stroke:#C62828,color:#000000
    classDef gate fill:#F9A825,stroke:#7A5200,color:#1A1200,stroke-width:2px
    classDef note fill:#FFFDE7,stroke:#9E9D24,color:#000000
```

- [x] **Step 11: Check the sources before rendering**

Run:
```
cd /Users/rabies/global_experience && grep -c '<br' diagrams/op-*.mmd diagrams/operating-loop.mmd; grep -c $'\u2014' diagrams/op-*.mmd diagrams/operating-loop.mmd
```
Expected: every line ends in `:0`.

- [x] **Step 12: Render all nine**

Run with `dangerouslyDisableSandbox: true`:
```
cd /Users/rabies/global_experience && for n in op-one-fact operating-loop op-folders op-waterfall op-subagents op-wiki-tiers op-emails op-improvement op-continuity; do npx -y @mermaid-js/mermaid-cli -i diagrams/$n.mmd -o diagrams/rendered/$n.svg --svgId $n-svg -b transparent -p diagrams/puppeteer.json || echo "RENDER FAILED: $n"; done; ls -la diagrams/rendered/op-*.svg diagrams/rendered/operating-loop.svg
```
Expected: no `RENDER FAILED` line, nine files with today's timestamp and size above
10 KB. If mermaid-cli reports a parse error, the error names the line. Fix that line
in the `.mmd`, keep the label on one line, and rerun that one file.

- [x] **Step 13: Confirm ids and label rule in the output**

Run:
```
cd /Users/rabies/global_experience && for n in op-one-fact operating-loop op-folders op-waterfall op-subagents op-wiki-tiers op-emails op-improvement op-continuity; do head -c 400 diagrams/rendered/$n.svg | grep -o "id=\"$n-svg\"" || echo "BAD ID: $n"; grep -c '<br' diagrams/rendered/$n.svg; done
```
Expected: nine `id="..."` lines, no `BAD ID`, and `0` after each.

- [x] **Step 14: Examine each render once**

Open each `diagrams/rendered/<name>.svg` in the browser, or with the Read tool on
the SVG file if it is under 25 KB, and confirm no label leaves its box. The
`op-folders` grid must show four columns in numeric order. If a label overflows,
shorten that label in the `.mmd`, keep the meaning, and rerun Steps 12 and 13 for
that file. Record any label change in the handoff.

- [x] **Step 15: Run the verification script**

Run: `/Users/rabies/global_experience/plans/verify-ops-section.sh; echo "exit $?"`
Expected: `ok` on every "rendered file exists" line and every em dash and `<br>`
line. The title, kicker, and "svg inlined once" lines still say `FAIL`. That is
correct at this point.

- [x] **Step 16: Checkpoint**

Do not commit yet. Write the handoff per the waterfall rule if context is near 50%.
Otherwise continue to Task 3.

---

### Task 3: Replace the panel prose with the arc-ordered HTML

Replace lines 2850 to 3047 of `automated-curriculum-development-business.html`, from `<section class="panel"
id="operating-system">` through the `</section>` that closes it, with the block below.
The block holds nine empty canvases marked `data-diagram="<name>"`. Task 4 fills them.

**Files:**
- Modify: `/Users/rabies/global_experience/automated-curriculum-development-business.html:2850-3047`
- Modify: `/Users/rabies/global_experience/automated-curriculum-development-business.html:646-648` (append one CSS
  rule for the kicker after the left-align allowlist block, see Step 1)

**Interfaces:**
- Produces: nine `<div class="canvas" data-diagram="NAME"></div>` placeholders. Task 4
  matches on the exact string `<div class="canvas" data-diagram="NAME"></div>`.

- [x] **Step 1: Add the kicker style**

Find the end of the left-align allowlist rule at line 646 to 648:

```css
      #operating-system .canvas svg#op-subagents-svg foreignObject > div {
        text-align: left !important;
      }
```

Insert directly after it:

```css

      /* ── Narrative arc labels in the Business Operations panel ── */
      #operating-system .arc-kicker {
        margin: 40px 0 4px;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #002fa7;
      }
```

- [x] **Step 2: Extract the exact block to replace**

Run:
```
cd /Users/rabies/global_experience && grep -n '<section class="panel" id="operating-system">\|<section class="panel" id="session-pipeline">' automated-curriculum-development-business.html
```
Expected: two lines. The first is the panel start, S. The second is the next panel
start, E. The block to replace is lines S through E-1. In the current file S is 2850
and E is 3048. Recompute after Step 1 shifted the file by ten lines.

Do the replacement with Python. Save this as
`/Users/rabies/global_experience/plans/replace-ops-panel.py`, then run it. It reads
`/Users/rabies/global_experience/plans/ops-panel.html` (written in Step 3) and inserts
it in place of the old block.

```python
#!/usr/bin/env python3
"""Replace the #operating-system panel of automated-curriculum-development-business.html with plans/ops-panel.html."""
import re, sys
PAGE = "/Users/rabies/global_experience/automated-curriculum-development-business.html"
NEW = "/Users/rabies/global_experience/plans/ops-panel.html"
src = open(PAGE, encoding="utf-8").read()
new = open(NEW, encoding="utf-8").read().rstrip("\n") + "\n"
start = src.index('<section class="panel" id="operating-system">')
start = src.rfind("\n", 0, start) + 1
end = src.index('<section class="panel" id="session-pipeline">')
end = src.rfind("\n", 0, end) + 1
if not (0 < start < end):
    sys.exit("markers not found in order")
out = src[:start] + new + src[end:]
open(PAGE, "w", encoding="utf-8").write(out)
print("replaced", src.count("\n", start, end), "lines with", new.count("\n"), "lines")
```

- [x] **Step 3: Write `plans/ops-panel.html`**

Copy this file verbatim. It is the whole new panel.

```html
        <section class="panel" id="operating-system">
          <div class="detail-head">
            <h2>2 - Business Operations</h2>
          </div>

          <div style="max-width: 800px; margin: 0 0 8px; line-height: 1.6; color: #333">
            <p style="margin-top: 16px; margin-bottom: 16px">
              This panel explains how the business runs itself. It has eight stages, in order. Foundation sets one home for each fact. Structure shows where plans and workstreams live. Workflow shows how work moves from one session to the next. Execution shows how a plan runs and when it is done. Systems shows the agent rules and the knowledge base. Communication shows which emails the business sends. Improvement shows how the business learns from each session. Resilience shows what preserves the business if the operator is away.
            </p>

            <p class="arc-kicker">Foundation</p>
            <h3 style="color: #1a202c; margin: 0 0 8px">Single Source of Truth</h3>
            <p style="margin-top: 0; margin-bottom: 16px">
              Each fact has one home. No fact lives in two places. This rule stops copies from becoming different over time.
            </p>
            <ul style="padding-left: 20px">
              <li style="margin-bottom: 8px"><strong>A decision</strong> has its home in <code>.claude/manifest.json</code>. The manifest holds durable facts only: decisions, paths to spec files, external state, and one pointer to the active plan. Every session reads the manifest first. A manifest longer than about 150 lines moves detail into spec files.</li>
              <li style="margin-bottom: 8px"><strong>Progress</strong> has its home in the plan folder, in <code>PLAN.md</code> and the numbered handoffs. The manifest never tracks progress.</li>
              <li style="margin-bottom: 8px"><strong>Business knowledge</strong> has its home in the wiki that owns the topic.</li>
              <li style="margin-bottom: 8px"><strong>A code relationship</strong> has its home in the generated knowledge graph.</li>
              <li style="margin-bottom: 8px"><strong>A retired term</strong> has its home in <code>10-Plans/RETIRED-TERMS.md</code> in the same turn as the decision that retired it.</li>
            </ul>
          </div>

          <div class="canvas" data-diagram="op-one-fact"></div>

          <div style="max-width: 800px; margin: 0 0 8px; line-height: 1.6; color: #333">
            <p class="arc-kicker">Structure</p>
            <h3 style="color: #1a202c; margin: 0 0 8px">Workstream Architecture</h3>
            <p style="margin-top: 0; margin-bottom: 16px">
              All plans live in <code>10-Plans/</code>. A plan is born there and never in a workstream folder. The diagram traces one plan through its life. A status change is a folder move and nothing else.
            </p>
            <ul style="padding-left: 20px">
              <li style="margin-bottom: 8px"><strong>FuturePlans</strong> holds approved plans that have not started. Each is one flat file named <code>YYYY-MM-DD-topic.md</code>. A folder inside FuturePlans is drift.</li>
              <li style="margin-bottom: 8px"><strong>CurrentPlans</strong> holds active work. Kickoff moves the dated file into a new folder named for its workstream and topic. Kickoff never copies. A file that remains in FuturePlans proves the kickoff was wrong. Each set folder holds one <code>PLAN.md</code>, the numbered handoffs, and one <code>APPROVALS.md</code> for gates.</li>
              <li style="margin-bottom: 8px"><strong>InactivePlans</strong> holds paused or superseded sets. The business keeps them so a later session can see what was tried.</li>
              <li style="margin-bottom: 8px"><strong>PastPlans</strong> holds finished sets with their full plan and handoff trail.</li>
              <li style="margin-bottom: 8px"><strong>Tasks</strong> holds the standing board <code>WORK-STATUS.md</code>, a run log, a drift report, and <code>check-drift.sh</code>. The board is an index only. Detail stays in each set.</li>
              <li style="margin-bottom: 8px"><strong>SkillProposals</strong> holds the queue of proposed skill and doc changes. <strong>MIGRATION-MAP.md</strong> logs every move.</li>
            </ul>
          </div>

          <div class="canvas" data-diagram="operating-loop"></div>

          <div style="max-width: 800px; margin: 0 0 8px; line-height: 1.6; color: #333">
            <h3 style="color: #1a202c; margin: 32px 0 8px">Folder-Based Workstreams</h3>
            <p style="margin-top: 0; margin-bottom: 16px">
              The workspace holds seventeen numbered folders, from <code>000-Dashboard</code> to <code>16-AdsAnalytics</code>. Each folder is one workstream. Underscore folders hold what every workstream shares. The main wiki and the one-file business briefing sit at the root.
            </p>
            <ul style="padding-left: 20px">
              <li style="margin-bottom: 8px"><strong>Zero-rename zones.</strong> Scheduled jobs, skills, and handoffs reach some paths by absolute path. Those paths never change. A plan set path changes only by a status move.</li>
              <li style="margin-bottom: 8px"><strong>Secrets.</strong> Each folder quarantines loose secrets in its own <code>_Credentials/</code>. The business never uploads, syncs, publishes, or commits them.</li>
              <li style="margin-bottom: 8px"><strong>Archive, never delete.</strong> Superseded material moves to the owning folder's <code>_Archive/</code>.</li>
              <li style="margin-bottom: 8px"><strong>New folders since July 2026.</strong> <code>12-Diagrams</code>, <code>13-Mistakes</code>, <code>14-Images</code>, and <code>15-OvernightRunner</code> were added. The ads workstream moved from folder 2 to <code>16-AdsAnalytics</code>. Folder 2 is now the site map and traffic funnels. Folder 8 is the legal knowledge base.</li>
            </ul>
          </div>

          <div class="canvas" data-diagram="op-folders"></div>

          <div style="max-width: 800px; margin: 0 0 8px; line-height: 1.6; color: #333">
            <p class="arc-kicker">Workflow</p>
            <h3 style="color: #1a202c; margin: 0 0 8px">Session Waterfall Workflow</h3>
            <p style="margin-top: 0; margin-bottom: 16px">
              No session uses more than half of its context window. Model quality decreases long before the hard limit. At the half mark the session stops, writes a handoff, and a fresh session continues from that file alone.
            </p>
            <ul style="padding-left: 20px">
              <li style="margin-bottom: 8px"><strong>The checkpoint has seven steps.</strong> Finish or revert the current edit. Commit the working state. Mark completed items in <code>PLAN.md</code>. Write <code>HANDOFF-N.md</code>. Record durable decisions in the project's <code>CLAUDE.md</code>. Run <code>/clear</code>, never <code>/compact</code>. Answer the three lessons questions in the handoff.</li>
              <li style="margin-bottom: 8px"><strong>Each handoff carries</strong> the verification command and its expected result, what is complete, the ordered remaining work, decisions and dead ends found, and the exact next step.</li>
              <li style="margin-bottom: 8px"><strong>A human gate always pauses the run</strong>, at any context level. The handoff names any open gate.</li>
              <li style="margin-bottom: 8px"><strong>Headless mode.</strong> A driver script can loop <code>claude -p</code> so each session starts fresh. There, one session equals one plan session in scope. A gate ends the session with a <code>GATE:</code> line, and the driver waits for the owner. The final handoff writes <code>WATERFALL: COMPLETE</code>. The driver refuses to run on API billing.</li>
            </ul>
          </div>

          <div class="canvas" data-diagram="op-waterfall"></div>

          <div style="max-width: 800px; margin: 0 0 8px; line-height: 1.6; color: #333">
            <p class="arc-kicker">Execution</p>
            <h3 style="color: #1a202c; margin: 0 0 8px">Plan Execution Lifecycle</h3>
            <p style="margin-top: 0; margin-bottom: 16px">
              Different models do different parts of the work.
            </p>
            <ul style="padding-left: 20px">
              <li style="margin-bottom: 8px"><strong>Fable</strong> designs the architecture and writes the plan.</li>
              <li style="margin-bottom: 8px"><strong>Sonnet 5</strong> runs the waterfall. It executes the steps, writes the code, and writes the handoffs.</li>
              <li style="margin-bottom: 8px"><strong>Opus 4.6</strong> is used rarely, only at a decision fork or to judge a risk the plan did not describe.</li>
              <li style="margin-bottom: 8px"><strong>Haiku</strong> does small structural edits, log cleanup, and file moves or renames.</li>
            </ul>
            <p style="margin-top: 0; margin-bottom: 16px">
              A session with no prior context reads the manifest, then <code>PLAN.md</code> and the highest-numbered handoff. It runs the verification command and continues at the next step. Before Phase 1 of any plan the session runs a preflight. The preflight lists every external dependency, tests each one with a read-only call, and prints a PASS or FAIL table. A dependency that was not called is UNKNOWN, never PASS. Anything that is not PASS stops the plan.
            </p>
            <p style="margin-top: 0; margin-bottom: 16px">
              A plan session does its tasks inline. It may dispatch one reviewer subagent that reviews the whole session diff before the handoff. Before any dispatch, the session classifies the task with one test: would a rerun give a different answer? A yes goes to an architect agent whose output must land in the manifest. A no goes to a cheaper executor agent.
            </p>
            <p style="margin-top: 0; margin-bottom: 16px">
              An overnight runner in <code>15-OvernightRunner/</code> works a plan while the operator sleeps. It runs only tasks that are reversible, local, and verifiable. The first night on any plan is a dry run, because the owner gates the classification. It snapshots each task before it runs and restores the snapshot when verification fails. Each task gets one fresh session. It never retries, never pushes, never deploys, and never spends. The operator wakes to a morning briefing.
            </p>

            <h3 style="color: #1a202c; margin: 32px 0 8px">Completion Criteria &amp; Quality Gates</h3>
            <p style="margin-top: 0; margin-bottom: 16px">
              A plan set is complete only when five things happen in one closing step. Every checkbox in <code>PLAN.md</code> is marked, or a dated note names each dropped item. The latest handoff carries <code>WATERFALL: COMPLETE</code> plus the verification command and its result. The set folder moves to PastPlans and the move is logged in <code>MIGRATION-MAP.md</code>. The board rows get their new paths. The manifest is updated if external state changed. Until the folder moves, the set is not complete, whatever its files claim. <code>check-drift.sh</code> exits non-zero when a finished set still sits in CurrentPlans.
            </p>
            <p style="margin-top: 0; margin-bottom: 16px">
              Before the move, the session reviews the whole set for mistakes that a per-session lessons step did not capture. Each distinct mistake class gets one entry in the mistakes ledger.
            </p>
            <ul style="padding-left: 20px">
              <li style="margin-bottom: 8px"><strong>Gates never advance without the owner.</strong> At a human checkpoint the session stops and presents the choice as options.</li>
              <li style="margin-bottom: 8px"><strong>Review by default.</strong> Any change to continuity code or plugin code gets a local code review. Anything that touches auth, credentials, or the Moodle server also gets a security review. <code>_Continuity/verify.sh</code> must exit 0 before the work counts as done.</li>
              <li style="margin-bottom: 8px"><strong>Proof over narration.</strong> After any external API write, the session reads the object back and pastes the returned id or status.</li>
            </ul>
          </div>

          <div style="max-width: 800px; margin: 0 0 8px; line-height: 1.6; color: #333">
            <p class="arc-kicker">Systems</p>
            <h3 style="color: #1a202c; margin: 0 0 8px">Agent Governance System</h3>
            <p style="margin-top: 0; margin-bottom: 16px">
              Without limits, a session can start as many helper agents as it wants, run them in the background, and report its own success. Two layers replace that with enforcement and evidence.
            </p>
            <ol style="padding-left: 20px">
              <li style="margin-bottom: 8px"><strong>Hard caps in settings.</strong> Three agents at once and three per session. One nested layer of helpers. No background work. Every helper is fixed to Sonnet. Every start and stop is written to an audit log. These caps live in <code>~/.claude/settings.json</code>. A session cannot override them.</li>
              <li style="margin-bottom: 8px"><strong>Eight behavior rules on top.</strong> Spawn at most three helpers per prompt. No helper starts its own helpers. Wait for each helper to return before the next step. Credit finished work only against files on disk, exit codes, or the audit log, never against the helper's own summary. Take the sidecar lock before writing any shared status file. Report any limit as a <code>CEILING</code> line. A run that ends without its expected files is a failed run. A plan session works inline with at most one reviewer helper.</li>
            </ol>
            <p style="margin-top: 0; margin-bottom: 16px">The result is cheaper runs, smaller batches, and checked evidence.</p>
          </div>

          <div class="canvas" data-diagram="op-subagents"></div>

          <div style="max-width: 800px; margin: 0 0 8px; line-height: 1.6; color: #333">
            <h3 style="color: #1a202c; margin: 32px 0 8px">Three-Tier Knowledge Base</h3>
            <p style="margin-top: 0; margin-bottom: 16px">
              Information is stored at the most specific level that owns it. Tier 1 is <code>Wiki/index.md</code>, the main wiki. It holds navigation and governance, never an operational fact. Tier 2 is one wiki per workstream folder. Tier 3 is a deep wiki beside the code, and it is authoritative for its own domain. When two tiers disagree, the more specific tier wins. The session fixes the fact at its source. Then <code>/ierhub-current-state</code> syncs each Tier 2 wiki upward and rebuilds <code>0-HitByABus.html</code>, the one-file briefing of the whole business.
            </p>
          </div>

          <div class="canvas" data-diagram="op-wiki-tiers"></div>

          <div style="max-width: 800px; margin: 0 0 8px; line-height: 1.6; color: #333">
            <p class="arc-kicker">Communication</p>
            <h3 style="color: #1a202c; margin: 0 0 8px">Automated Communication Protocols</h3>
            <p style="margin-top: 0; margin-bottom: 16px">
              Three separate systems send email to buyers and staff. The map below shows every trigger and every message. It exists so that gaps are visible and so that the real buyer experience is known.
            </p>
            <ul style="padding-left: 20px">
              <li style="margin-bottom: 8px"><strong>Stripe</strong> sends payment and refund receipts when the dashboard toggle is on.</li>
              <li style="margin-bottom: 8px"><strong>Moodle LMS</strong> sends the welcome email, password resets, the certificate email, the renewal reminder, and the CE reset notice.</li>
              <li style="margin-bottom: 8px"><strong>The application</strong> sends staff alerts for refunds, disputes, and contact form messages.</li>
              <li style="margin-bottom: 8px"><strong>Dormant.</strong> A Moodle payment gateway suite is built but its endpoint is not live. Its emails are shown with a dashed border.</li>
            </ul>
          </div>

          <div class="canvas" data-diagram="op-emails"></div>

          <div style="max-width: 800px; margin: 0 0 8px; line-height: 1.6; color: #333">
            <p class="arc-kicker">Improvement</p>
            <h3 style="color: #1a202c; margin: 0 0 8px">Continuous Improvement Cycle</h3>
            <p style="margin-top: 0; margin-bottom: 16px">
              Every session ends by answering three questions in its handoff. What failed or surprised this session? What fact had to be re-derived that should have been recorded? What skill or doc change would have prevented it? A durable lesson becomes a feedback memory. Any implied change to a skill or a doc becomes a proposal in <code>10-Plans/SkillProposals/PROPOSALS.md</code> with status proposed. No agent edits the target file directly.
            </p>
            <ul style="padding-left: 20px">
              <li style="margin-bottom: 8px"><strong>The owner's morning pass</strong> approves or rejects each entry. Anything not approved stays frozen.</li>
              <li style="margin-bottom: 8px"><strong>An executor applies</strong> each approved entry per <code>APPLY.md</code>. It backs up the target first and applies only the exact diff shown.</li>
              <li style="margin-bottom: 8px"><strong>A Monday review</strong> scores whether each change moved the metric it targeted. Two flat reviews make the change a revert candidate. The loop has run since 30 Jul 2026.</li>
            </ul>
            <p style="margin-top: 0; margin-bottom: 16px">
              A mistakes ledger at <code>13-Mistakes/mistakes.md</code> records each real error. A session appends an entry when a lesson traces to an actual error, or when the owner names a mistake mid-session. Each entry records the symptom, the root cause, the cost, the prevention, and where the prevention now lives. An entry closes only when its prevention is codified as a feedback memory or a proposal. A session reads the ledger when it drafts a plan and during preflight. The daily brief reports the open-entry count. A monthly sweep checks every codified link and every open entry. The first sweep is due 13 Sep 2026.
            </p>
          </div>

          <div class="canvas" data-diagram="op-improvement"></div>

          <div style="max-width: 800px; margin: 0 0 8px; line-height: 1.6; color: #333">
            <p class="arc-kicker">Resilience</p>
            <h3 style="color: #1a202c; margin: 0 0 8px">Operational Continuity Framework</h3>
            <p style="margin-top: 0; margin-bottom: 16px">
              A scheduled job mirrors the workspace into a private repository every day at 12:00, with a catch-up run after the Mac wakes. It copies only allowlisted folders. Credential folders and the payment and funnel tree appear only as a change count. A secret gate blocks any credential before it can be committed. The job renders a one-file <code>wiki.html</code>, writes today's date to <code>heartbeat.txt</code>, then commits and pushes.
            </p>
            <ul style="padding-left: 20px">
              <li style="margin-bottom: 8px"><strong>Dead-man check.</strong> A GitHub Action opens an issue that names the successor when no commit lands for seven days.</li>
              <li style="margin-bottom: 8px"><strong>Successor runbook.</strong> <code>_Continuity/CONTINUITY.md</code> tells a successor, an attorney, or a partner what the repository is and what to do.</li>
              <li style="margin-bottom: 8px"><strong>Two known traps.</strong> A scheduled script must not live under Desktop, Documents, or Downloads, because macOS blocks the job before its first line. And a session must never diagnose headless login from inside a sandboxed shell, because the sandbox returns a false expired-token error.</li>
            </ul>
          </div>

          <div class="canvas" data-diagram="op-continuity"></div>

        </section>
```

- [x] **Step 4: Run the replacement**

Run:
```
cd /Users/rabies/global_experience && python3 plans/replace-ops-panel.py && grep -c 'data-diagram=' automated-curriculum-development-business.html
```
Expected: `replaced 198 lines with N lines` (N near 170) and then `9`.

- [x] **Step 5: Run the verification script**

Run: `/Users/rabies/global_experience/plans/verify-ops-section.sh; echo "exit $?"`
Expected: `ok` on every title, kicker, em dash, sidebar blurb, and guard line. `FAIL`
on the nine "svg inlined once" lines and on "no empty diagram placeholder left". Exit 1.

---

### Task 4: Inline the nine SVGs

**Files:**
- Create: `/Users/rabies/global_experience/plans/inline-ops-svgs.py`
- Modify: `/Users/rabies/global_experience/automated-curriculum-development-business.html`

**Interfaces:**
- Consumes: the placeholders from Task 3 and the SVG files from Task 2.
- Produces: nine `<div class="canvas">` blocks each holding one inline SVG whose root
  carries `width="100%"` and a transparent background style, matching the page's
  diagram conventions.

- [x] **Step 1: Write the script**

```python
#!/usr/bin/env python3
"""Inline diagrams/rendered/<name>.svg into the matching data-diagram placeholder."""
import re, sys
PAGE = "/Users/rabies/global_experience/automated-curriculum-development-business.html"
REND = "/Users/rabies/global_experience/diagrams/rendered"
NAMES = ["op-one-fact", "operating-loop", "op-folders", "op-waterfall", "op-subagents",
         "op-wiki-tiers", "op-emails", "op-improvement", "op-continuity"]
src = open(PAGE, encoding="utf-8").read()
for n in NAMES:
    svg = open(f"{REND}/{n}.svg", encoding="utf-8").read().strip()
    if not svg.startswith("<svg"):
        sys.exit(f"{n}: file does not start with <svg")
    if f'id="{n}-svg"' not in svg[:400]:
        sys.exit(f"{n}: root id missing")
    # Match the page convention on the ROOT tag only: width 100%, transparent
    # background, keep viewBox. Never touch inner elements.
    head, rest = svg.split(">", 1)
    head = re.sub(r'\swidth="[^"]*"', ' width="100%"', head, count=1)
    if ' width="100%"' not in head:
        head += ' width="100%"'
    if "background-color: transparent" not in head:
        print(f"WARN {n}: root style lacks background-color: transparent, check -b flag")
    if "viewBox=" not in head:
        print(f"WARN {n}: root lacks viewBox")
    svg = head + ">" + rest
    hole = f'<div class="canvas" data-diagram="{n}"></div>'
    if src.count(hole) != 1:
        sys.exit(f"{n}: expected exactly one placeholder, found {src.count(hole)}")
    src = src.replace(hole, '<div class="canvas">\n            ' + svg + "\n          </div>")
    print("inlined", n)
open(PAGE, "w", encoding="utf-8").write(src)
```

- [x] **Step 2: Run it**

Run: `cd /Users/rabies/global_experience && python3 plans/inline-ops-svgs.py`
Expected: nine `inlined <name>` lines and no error.

- [x] **Step 3: Confirm the root attributes**

Run:
```
cd /Users/rabies/global_experience && for n in op-one-fact operating-loop op-folders op-waterfall op-subagents op-wiki-tiers op-emails op-improvement op-continuity; do L=$(grep -n "<svg id=\"$n-svg\"" automated-curriculum-development-business.html | cut -d: -f1); sed -n "${L}p" automated-curriculum-development-business.html | cut -c1-260; done
```
Expected: each line shows `<svg id="<name>-svg"`, `width="100%"`, and a `viewBox`.
If a root lacks `viewBox`, the guard script still fits it, but note it in the handoff.

- [x] **Step 4: Run the verification script**

Run: `/Users/rabies/global_experience/plans/verify-ops-section.sh; echo "exit $?"`
Expected: every line `ok`, `exit 0`.

---

### Task 5: Sidebar entry

**Files:**
- Modify: `/Users/rabies/global_experience/automated-curriculum-development-business.html:702-705`

- [x] **Step 1: Replace the blurb**

Old:
```html
        <a class="box" href="#operating-system"
          ><h3>2 - Business Operations</h3>
          <p>Memory, Waterfall, Wiki</p></a
```
New:
```html
        <a class="box" href="#operating-system"
          ><h3>2 - Business Operations</h3>
          <p>Foundation to Resilience</p></a
```

- [x] **Step 2: Run the verification script**

Run: `/Users/rabies/global_experience/plans/verify-ops-section.sh; echo "exit $?"`
Expected: `exit 0`.

---

### Task 6: Full verification, review, and owner gate

**Files:**
- Read only, unless a fix is needed: `/Users/rabies/global_experience/automated-curriculum-development-business.html`

- [x] **Step 1: Language check on the new prose**

Run:
```
cd /Users/rabies/global_experience && python3 - <<'EOF'
import re
src=open("automated-curriculum-development-business.html",encoding="utf-8").read()
s=src.index('<section class="panel" id="operating-system">'); e=src.index('<section class="panel" id="session-pipeline">')
panel=re.sub(r"<svg.*?</svg>","",src[s:e],flags=re.S)
import html
text=html.unescape(re.sub(r"<[^>]+>"," ",panel))
print("semicolons:", text.count(";"))
print("em dashes:", text.count("\u2014"))
for w in ["spin up","reach out","kick off","leverage","robust","seamless","delve","crucial","pivotal","landscape","navigate"]:
    if w in text.lower(): print("banned word:", w)
EOF
```
Expected: `semicolons: 0`, `em dashes: 0`, no `banned word` line. The script decodes
`&amp;` before it counts, so the ampersand in the section title does not count as a
semicolon. If the count is not 0, find the sentence and split it.

- [ ] **Step 2: Serve and examine**

Run with `dangerouslyDisableSandbox: true` and stop it before the turn ends:
```
cd /Users/rabies/global_experience && python3 -m http.server 8765 --bind 127.0.0.1 >/dev/null 2>&1 &
```
Open `http://127.0.0.1:8765/automated-curriculum-development-business.html#operating-system` in the browser at 1280px
and at 390px wide. Confirm: the eight kickers read in order, each diagram opens and
zooms, no label leaves its box, the `op-folders` grid shows four columns, and no
horizontal body scroll appears at 390px. Then stop the server:
`kill %1` or `pkill -f "http.server 8765"`.

If a left-aligned label overflows in `op-folders`, `op-wiki-tiers`, `op-waterfall`,
`op-improvement`, or `op-subagents`, remove that diagram's three selector lines from
the allowlist at lines 632 to 648 and re-check. Record the removal in the handoff.

- [x] **Step 3: Reviewer subagent**

Dispatch one reviewer subagent, foreground, Sonnet, with this prompt. Include the
line "You never spawn subagents." verbatim.

> Review `git diff` in `/Users/rabies/global_experience` against
> `plans/PLAN.md`. Check: every sentence in the new panel prose follows ASD-STE100
> Strict mode, no em dash anywhere, every Mermaid label in `diagrams/op-*.mmd` and
> `diagrams/operating-loop.mmd` is one line with no `<br>`, section names match the
> plan exactly, and no fact appears that the plan did not supply. Report each finding
> as file, line, quote, and fix. You never spawn subagents.

Fix confirmed findings inline. Rerun `plans/verify-ops-section.sh`.

- [ ] **Step 4: Owner gate**

Do not commit or push. Present to the owner:

> The rewritten Business Operations panel is ready for review at
> `/Users/rabies/global_experience/automated-curriculum-development-business.html#operating-system`. Diagram sources
> are in `/Users/rabies/global_experience/diagrams/`. A push publishes to
> `https://mmentzerhernandez.github.io/global_experience/automated-curriculum-development-business.html`. Options:
> commit and push now, commit only, or list changes to make first.

Record the gate in the handoff as a `GATE:` line if the session ends before the owner
answers.

- [ ] **Step 5: On approval, commit**

```
cd /Users/rabies/global_experience && git add diagrams plans id-skills.html automated-curriculum-development-business.html index.html sitemap.xml && git status --short
```
Read the list. Then:
```
git commit -m "docs(id-skills): rename page and rewrite Business Operations panel

Rename id-skills.html to automated-curriculum-development-business.html, leave a
redirect stub at the old name, repoint index.html and sitemap.xml. Rename the ten sections to the Foundation to Resilience arc, rewrite every
sentence in ASD-STE100 Strict mode, re-render nine diagrams with one-line
labels, current folder numbering 000 to 16, and the mistakes ledger, and add
the continuity pipeline diagram.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>"
```
Push only if the owner chose push.

---

## Self-review against the request

- Rename ten sections into the eight-stage arc: Task 3, Step 3, kickers and h3s.
- Mistakes folder and new operating rules: Task 3 (Improvement, Execution,
  Completion prose) and Task 2 Steps 4 and 9 (folder grid, improvement diagram).
- Diagrams updated for new numbering and folder organization: Task 2 Step 4.
- Wording in ASD-STE100: prose supplied verbatim, checked in Task 6 Step 1, reviewed
  in Task 6 Step 3.
- One-line Mermaid boxes: every source in Task 2, checked by the script.
- Rename the URL to `automated-curriculum-development-business.html` and forward
  the old URL: Task 0.
- Nothing published without the owner: Task 6 Step 4.
