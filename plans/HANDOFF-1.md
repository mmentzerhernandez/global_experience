# HANDOFF-1: automated-curriculum-development-business.html Business Operations rewrite

Written 16 Aug 2026, after Session 1 (all of Task 0 through Task 5, and Task 6
Steps 1 and 3).

## Verification

Run:
```
/Users/rabies/global_experience/plans/verify-ops-section.sh; echo "exit $?"
```
Expected: every line `ok`, exit 0.

Commit to check against: none. Nothing is committed. Every file the plan
names is staged with `git add` but not committed, because the plan's global
constraints say never commit or push without the owner's approval.

## Completed so far

- Task 0: renamed `id-skills.html` to
  `automated-curriculum-development-business.html`, wrote the 14-line
  redirect stub at the old name, updated the four links in `index.html` and
  the one link in `sitemap.xml`, confirmed the redirect keeps the fragment.
- Task 1: wrote `plans/verify-ops-section.sh`.
- Task 2: fixed `diagrams/puppeteer.json`, wrote and rendered all nine
  diagram sources.
- Task 3: added the `.arc-kicker` CSS rule, wrote `plans/ops-panel.html`
  and `plans/replace-ops-panel.py`, and ran the swap. The old panel, 196
  lines, is now the new 185-line panel with nine empty diagram
  placeholders.
- Task 4: wrote `plans/inline-ops-svgs.py` and ran it. All nine SVGs are
  inlined, each with `width="100%"`, `background-color: transparent`, and
  a `viewBox` on the root element.
- Task 5: replaced the sidebar blurb under "2 - Business Operations" from
  "Memory, Waterfall, Wiki" to "Foundation to Resilience".
- Task 6, Step 1: ran the language check script on the new panel prose.
  Result: `semicolons: 0`, `em dashes: 0`, no banned word found.
- Task 6, Step 3: dispatched the one reviewer subagent allowed by the
  waterfall rule, foreground, with the prompt from the plan plus the line
  "You never spawn subagents." Its report: no findings. The diff matches
  `plans/PLAN.md` exactly on prose, section names, and diagram sources.
- `plans/PLAN.md` has every step through Task 6 Step 1 and Step 3 marked
  `[x]`. Three steps remain unmarked: Task 6 Step 2, Step 4, and Step 5.

## Remaining work

1. Task 6, Step 2: serve the page and examine it in a real browser at 1280px
   and 390px wide. This session could not run it. The Claude in Chrome
   extension reported "Browser extension is not connected" when
   `tabs_context_mcp` was called. A `curl` check confirmed the page serves
   with HTTP 200, but that does not confirm layout, diagram overflow, or the
   absence of horizontal scroll at 390px. Start the server with
   `python3 -m http.server 8765 --bind 127.0.0.1` from
   `/Users/rabies/global_experience`, open
   `http://127.0.0.1:8765/automated-curriculum-development-business.html#operating-system`,
   confirm the eight kickers, that no label leaves its box, that
   `op-folders` shows four columns, and no horizontal body scroll at 390px.
   Stop the server after.
2. Task 6, Step 4: the owner gate. Do not commit or push. See the `GATE:`
   line below.
3. Task 6, Step 5: on approval, commit with the message in the plan, then
   push only if the owner chose push.

## GATE

GATE: The rewritten Business Operations panel is ready for review at
`/Users/rabies/global_experience/automated-curriculum-development-business.html#operating-system`.
Diagram sources are in `/Users/rabies/global_experience/diagrams/`. The
handoff at `/Users/rabies/global_experience/plans/HANDOFF-1.md` has the full
session record. A push publishes to
`https://mmentzerhernandez.github.io/global_experience/automated-curriculum-development-business.html`.
Recommendation: run the Task 6 Step 2 browser check first, since it has not
run yet, then commit and push. Options: commit and push now, commit only, or
list changes to make first.

## Decisions and constraints discovered

- The installed Chrome build for mermaid-cli is
  `mac_arm-152.0.7977.42/chrome-headless-shell-mac-arm64/chrome-headless-shell`,
  not the `150.0.7871.24` build the plan's July recipe named.
  `diagrams/puppeteer.json` now points at the installed build.
- `index.html` carried an unrelated pre-existing change (two list items under
  "Daily" cleared out) before this session started. That change was not
  touched and stays in the working tree along with this session's link swap.
- `npx @mermaid-js/mermaid-cli` prints `npm WARN EBADENGINE` lines on every
  render because the installed Node is `v20.11.1` and the package wants
  `>=22.12.0`. The warning is noise. All nine renders finished with exit 0.
- The Claude in Chrome browser extension was not connected in this session,
  so the Task 6 Step 2 visual check did not run. A future session or the
  owner must run it before the commit, or explicitly accept the risk.

## Exact next step

Run the Task 6 Step 2 browser check, then present the GATE question above to
the owner and wait for an answer before any commit.

## Lessons

1. What failed or surprised this session: the Claude in Chrome extension was
   not connected, so the planned browser check at Task 6 Step 2 could not
   run. A `curl` check substituted for it, which confirms the server
   response but not the rendered layout.
2. What fact had to be re-derived: none beyond what Session 1's handoff
   already recorded, the installed Chrome build path.
3. What skill or doc change would have prevented it: a preflight check for
   the Claude in Chrome connection at the start of any plan step that names
   a browser check, so the gap surfaces before the step is reached rather
   than during it. This is a candidate for
   `10-Plans/SkillProposals/PROPOSALS.md`, staged as proposed, not applied
   here since this workspace is outside IERHUB.com.
