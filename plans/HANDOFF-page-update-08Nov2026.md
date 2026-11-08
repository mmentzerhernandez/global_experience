# Handoff: curriculum business page update, after the session of 06 to 08 Nov 2026

This handoff is for the page update of 06 Nov 2026. It is not part of the plan of 16 Aug 2026 in `plans/PLAN.md` and `plans/HANDOFF-1.md`, which is finished. There is no `PLAN.md` for this update. The scope is in `/Users/rabies/global_experience/plans/RECOMMENDATIONS-curriculum-business-page-update-06Nov2026.md`.

## Verification

Run these from `/Users/rabies/global_experience`:

```
cat plans/KNOWN-TRAPS.md
git rev-parse --short HEAD                       # expected: e161815, nothing committed
grep -c 'data-diagram="' automated-curriculum-development-business.html   # expected: 6 until the render runs
grep -c 'diagram-fallback:start' automated-curriculum-development-business.html  # expected: 1 until the render runs
grep -o '<h2>[0-9] - [^<]*' automated-curriculum-development-business.html  # expected: 1 to 6, no 7
```

Measured by this session on 08 Nov 2026:

- The `div` tags are balanced in every panel and in the whole page.
- The STE-Checker found no finding on the page text, after one fix.
- The fallback script passes `node --check`.
- The fallback rebuild was tested twice: with no empty placeholder it removes the block, and with one empty placeholder it keeps the block for that one.
- No session has seen the 6 changed diagrams draw in a browser. Their Mermaid syntax is not tested.

## Completed so far

- All text changes of the 06 Nov 2026 recommendations, on all panels.
- Six diagram sources: `business-overview`, `session-pipeline`, `dwell-gate`, `plan-run`, `operating-loop` (now with the session waterfall) and `op-records` (the wiki tiers and the daily mirror).
- `op-emails` moved to the delivery panel.
- American spelling. The stray web address on CSS line 26 is removed.
- 08 Nov 2026, last request: panel 4 "CourseFactory v2" is now part of panel 3 "How a Course Gets Built", under the heading "CourseFactory v2: Five Stages and Three Gates". The panel 3 box in the list on the left opens the CourseFactory detail boxes. Compliance, Delivery and How AI Is Used are now panels 4, 5 and 6. The links to `#coursefactory-overview` are gone.
- No empty diagrams: a fallback block at the end of the page draws each unrendered diagram in the browser. It loads Mermaid 11.4.1 from cdn.jsdelivr.net.
- A side plan for the blocked continuity backup: `/Users/rabies/IERHUB/IERHUB.com/10-Plans/FuturePlans/2026-11-08-continuity-secret-gate-push-block.md`. It is not approved and not started.

## Remaining work

1. The owner opens the page and looks at every panel, mainly the 6 diagrams that the browser draws: `open /Users/rabies/global_experience/automated-curriculum-development-business.html`. If a diagram shows "did not render", fix its source in `/Users/rabies/global_experience/diagrams/`.
2. The owner runs the render command in a normal terminal. It bakes the 6 SVG files into the page and removes the fallback block:
   ```
   cd /Users/rabies/global_experience && export npm_config_cache=/tmp/npm-mmdc PUPPETEER_SKIP_DOWNLOAD=1 && for n in business-overview session-pipeline dwell-gate plan-run operating-loop op-records; do npx -y @mermaid-js/mermaid-cli -i diagrams/$n.mmd -o diagrams/rendered/$n.svg --svgId $n-svg -b transparent -c diagrams/mermaid-config.json -p diagrams/puppeteer-chrome.json || echo "RENDER FAILED: $n"; done && python3 plans/inline-06Nov2026-svgs.py
   ```
3. Check every panel in Claude in Chrome, when the owner allows a local server.
4. A separate task: add a graph refresh to `/ierhub-current-state`. Not started.
5. Commit when the owner asks. The commit holds the page, `diagrams/`, and the files in `plans/` of this update. It does not hold `sales-and-referrals-2026.html`.
6. Two old CSS rules for `op-wiki-tiers-svg` and `op-waterfall-svg` stay in the page. Those diagrams are gone, so the rules do nothing. Remove them in the next edit of the page.

## Decisions and constraints

- The owner's answers to the 9 questions are in the recommendations file, section "Decisions and status, 06 Nov 2026".
- The owner chose to keep the change record in the recommendations file (option (a), 08 Nov 2026).
- The merge reasons are in `/Users/rabies/global_experience/plans/RECOMMENDATIONS-diagram-merge-08Nov2026.md`.

## Exact next step

Ask the owner if the page looks correct in the browser (remaining work item 1). Put the page path in the question: `/Users/rabies/global_experience/automated-curriculum-development-business.html`.

## Kickoff prompt for the new session

```
Read /Users/rabies/global_experience/plans/HANDOFF-page-update-08Nov2026.md and do its Exact next step.
```

## Lessons

1. What failed or surprised this session: the render tool cannot start Chrome in the sandbox. The page held empty diagram spaces for two days. The browser fallback is the fix that the session could make itself.
2. What fact had to be found again: the continuity job makes `wiki.html`, not `0-HitByABus.html`. A reply to the owner stated it wrong, and a later reply corrected it. The fact is now in `plans/FACTS.md`.
3. What change would have prevented it: none to a skill. The rule "verified, inferred, unknown" already covers it, and the session did not apply it to a claim about a file it had not read.
