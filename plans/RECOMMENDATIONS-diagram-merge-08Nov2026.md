# Recommendations: which page diagrams to merge

Date: 08 Nov 2026
Page: `/Users/rabies/global_experience/automated-curriculum-development-business.html`
Preview of every diagram: `/private/tmp/claude-501/-Users-rabies-global-experience/c5f6d6fc-5241-4603-b87a-9aa251fdf427/scratchpad/panel-diagram-previews-08Nov2026.html`
Diagram sources: `/Users/rabies/global_experience/diagrams/`

## The 12 diagrams that were on the page before this update

| Panel | Diagram | What it shows |
|---|---|---|
| 2 | `op-one-fact` | Where each kind of fact is kept |
| 2 | `operating-loop` | The life of a plan set, from goal to PastPlans |
| 2 | `op-folders` | The numbered folders of the workspace |
| 2 | `op-waterfall` | How sessions hand the work to the next session at 50 percent context |
| 2 | `op-wiki-tiers` | The three wiki tiers and the sync upward |
| 2 | `op-emails` | The emails that Stripe and Moodle send to a buyer |
| 2 | `op-improvement` | How a mistake becomes a rule |
| 2 | `op-continuity` | The daily sync to the mirror and the wiki page |
| 4 | `coursefactory-overview` | The five stages and three gates of CourseFactory v2 |
| 4 | `factcheck-cascade` | How the fact checker judges one claim |
| 6 | `my-svg` | The learner steps from payment to the TDLR report |
| 7 | `op-subagents` | The limits on helper agents |

## Recommendation 1: merge `operating-loop` and `op-waterfall`

The box "Sessions work the plan and write handoffs" in `operating-loop` is the full content of `op-waterfall`. Put the `op-waterfall` steps inside that box as a group. The reader then sees one diagram for the life of a plan, from the goal to PastPlans, with the session handoffs in the middle.

## Recommendation 2: merge `op-wiki-tiers` and `op-continuity`

Both diagrams show how the records stay current. The wikis are synced about once a week, and a daily job copies the workspace to a private repository. One merged diagram puts both jobs in one place.

Correction, 08 Nov 2026: the first version of this file said that both diagrams name an old file. That was wrong for `op-continuity`. The daily job still renders `wiki.html`, a page that is separate from `0-HitByABus.html`. Proof: `/Users/rabies/IERHUB/IERHUB.com/_Continuity/bin/sync.sh`, lines 27 and 31. Only `op-wiki-tiers` named an old file, `0-CurrentState.html`.

## Recommendation 3: move `op-emails` to panel 6, and do not merge it

`op-emails` shows the emails to a buyer. Panel 2 is about how the business keeps its records, and panel 6 is about delivery to the buyer. The diagram has too many boxes to merge with `my-svg`. Put it in panel 6, after `my-svg`.

## Keep these diagrams separate

| Diagram | Reason |
|---|---|
| `op-one-fact` | It answers one question: where does a new fact go. A merge with the wiki diagram makes both harder to read. |
| `op-folders` | It is a list of folders, not a sequence. |
| `op-improvement` | It is the only diagram of the mistake process. |
| `coursefactory-overview` and `factcheck-cascade` | The second diagram is the detail of one box in the first diagram. A reader opens the detail only when needed. |
| `my-svg` | It is the only diagram of the learner steps. |
| `op-subagents` | It is the only diagram of the agent limits. |

Result: 12 diagrams become 10, and panel 2 has 5 diagrams in place of 8.

## Status

The owner approved all three recommendations on 08 Nov 2026, and all three are done on the page. The record is in `/Users/rabies/global_experience/plans/RECOMMENDATIONS-curriculum-business-page-update-06Nov2026.md`, section "Changes on 08 Nov 2026, second and third requests".
