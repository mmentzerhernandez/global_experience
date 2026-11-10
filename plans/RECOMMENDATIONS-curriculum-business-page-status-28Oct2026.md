# Recommendations: update the curriculum business page from IERHUB.com

Date: 28 Oct 2026
Page reviewed: `/Users/rabies/global_experience/automated-curriculum-development-business.html`, section `#business-overview` and the sections that follow it.
Published copy: https://mmentzerhernandez.github.io/global_experience/automated-curriculum-development-business.html#business-overview

## What the page says now

The business overview holds a six step pipeline table. Steps 1 to 4 are dated milestones from May to July 2026. Step 5, "Curricula to Social Media", reads "In Progress". Step 6 is the goal. The last dated fact on the page is 29 Jul 2026 (Spanish course approval). The delivery section says the Spanish course "cannot be sold through the self-service path yet". The compliance section covers the seat timer work of 27 and 28 Jul 2026 only.

The page is three months behind the workspace. The sources below give the current status. Each item names the file that proves it.

## 1. Correct one stale statement

The delivery section (page section 6, near line 3371) says Spanish has no fee enrollment row and no shipped checkout. This is false now.

- The Spanish checkout flow shipped on `main` in commit `1e78b5f`, and course 32973 is `available`. Source: `/Users/rabies/Desktop/IERHUB.com/6-FrontEndBackendIERhub.com/Wiki/index.md`, section "Spanish checkout flow, shipped" at line 782.
- Spanish is the course most buyers choose. On 18 Oct 2026 the buyer table read Spanish 22 of 28 known, English 6 of 28 known. Source: `/Users/rabies/Desktop/IERHUB.com/16-AdsAnalytics/Wiki/index.md`, section "Recent (2026-10-18)".

Recommendation: rewrite that paragraph to say both courses sell through the same Stripe path and name the commit.

## 2. Add a sales step to the pipeline table

The table stops at "First Customer" on 08 Jul 2026. The repo already holds a sales page and the overview links to it at line 762, but the table does not show the result.

Facts as of 27 Oct 2026, read from Stripe by `/sale-report`:

| Measure | Value |
|---|---|
| Buyers | 35 |
| Live payments | 38 |
| Gross | $911.66 |
| Refunded | $39.98 |
| Net | $871.68 |
| October 2026 to date | 18 payments, $415.85 net |

Source: `/Users/rabies/Desktop/IERHUB.com/16-AdsAnalytics/SaleReports/CUSTOMERS.md`, summarised in `/Users/rabies/Desktop/IERHUB.com/16-AdsAnalytics/Wiki/index.md`, section "Recent (2026-10-27)".

Channel facts for the same table, known sources only: `chatgpt.com` referral 17 of 30, Google organic 7 of 30, paid click 1 of 33, Meta ad touch 0 of 33. Paid spend to 22 Sep 2026 was $401.75 for one paid sale of $58.00. Source: `/Users/rabies/Desktop/IERHUB.com/16-AdsAnalytics/PaidAdsVersusAIReferral/2026-09-22_cost-per-sale.md`.

Recommendation: add a step "Sales to date" between steps 4 and 5 with the net figure, the buyer count, and one sentence on the ChatGPT referral share. Link the step to `sales-and-referrals-2026.html`. The sales page in this repo was updated to 27 Oct 2026 (commit `0ab0531`), so the two pages then agree.

## 3. Add the course 3 status

The page says nine courses are planned and shows two approved. The workspace holds the state of the next three.

- **Barber and cosmetology 4-hour CE.** All four modules are authored and packaged as a Moodle `.mbz`. Lessons were revised on 26 Oct 2026 and the checkers re-ran: 45.0 to 45.8 minutes per module against a 50 minute budget. Next step is owner review, then TDLR application. Source: `/Users/rabies/Desktop/IERHUB.com/5-CurriculumDevelopment/Wiki/course-pipeline-status.md`.
- **Two course structure, draft.** A 27 Oct 2026 recommendation proposes two TDLR registrations: course A at 4 hours and course B at 2 hours for licence holders of 15 years or more. The owner has decided two things: one content set for both trades, and two Moodle courses from one source. The rest is open. Source: `/Users/rabies/Desktop/IERHUB.com/5-CurriculumDevelopment/PreApprovedCourses/tx-barber-4hr-ce/RECOMMENDATIONS-two-course-structure-27Oct2026.md`.
- **Checkout design for four products** (`bc-4hr-en`, `bc-2hr-en`, `bc-4hr-es`, `bc-2hr-es`), no code yet, three local mockups. TDLR course numbers not applied for. Source: `/Users/rabies/Desktop/IERHUB.com/6-FrontEndBackendIERhub.com/RECOMMENDATIONS-barber-cosmetology-checkout-routing-27Oct2026.md` and `mockups/` beside it.
- **RAS 4-hour annual CE.** Sources gathered for all four modules, no lessons written, no build. Source: `course-pipeline-status.md` as above.
- **Towing operators CE.** Not started. Decision stands: towing next, then ACR/HVAC. Source: same file.
- **Constraint.** NFPA copyright clearance, reference 45647447085, pending since 30 May 2026. It affects every NEC or NFPA based course. Barber, RAS and towing avoid it by design. Source: same file, section `Cross-cutting constraint`.

Recommendation: add a short "Course 3 and later" table under the pipeline table with one row per course and its state. Mark the two course structure as a draft, not a decision.

## 4. Update step 5, social media

Step 5 says "In Progress". The workspace gives a more exact state.

- The pipeline is built end to end and runs in draft mode. The Facebook gate (English and Spanish) opened on 30 Jul 2026. YouTube and Instagram still wait on their gate.
- `Objects/` holds 25 reusable learning objects, 12 of them a Spanish renewal series drafted 13 Sep 2026.
- The last dry run on 12 Sep 2026 showed 56 pending sets, 0 approved, 0 posts sent. No content change since 13 Sep 2026.

Source: `/Users/rabies/Desktop/IERHUB.com/7-SocialMedia/Wiki/index.md`, sections "New material (13 Sep 2026)" and "Locked configuration".

Recommendation: keep "In Progress" and add one sentence: built, queued, not sent, Facebook only.

## 5. Extend the compliance section past the seat timer

The page covers the "at delivery" gate only. The business now runs the "after completion" gate too.

- **TDLR roster filing.** Roster 1188231 filed two Spanish completions on 27 Oct 2026 (course 32973). A person clicked POST. Learner emails went out through Resend on 28 Oct 2026. Source: `/Users/rabies/Desktop/IERHUB.com/6-FrontEndBackendIERhub.com/Wiki/index.md`, section "New this sync, 28 Oct 2026".
- **Exception handling.** `Moodle-ier/docs/TDLR-EXCEPTIONS.md` records three exception groups: A name differs, B licence expired, C no TDLR record. Three cases were open on 26 Oct 2026. Source: same wiki, section "New this sync, 27 Oct 2026".
- **Plugins.** `local_certnotify` logs each filing and stops a second learner email. `local_licmatch` (version `2026102702`) matches a learner to a TDLR licence. Source: same section.
- **Course renewal dates.** Course 32815 expires 22 Jun 2027. Course 32973 expires 27 Jul 2027. Source: `/Users/rabies/Desktop/IERHUB.com/Wiki/index.md`, section "Approved Courses".

Recommendation: add a panel "After completion: reporting to TDLR" with the roster flow, the three exception groups, and the two renewal dates.

## 6. Add the tools built since July

These exist and the page does not mention them.

- **TDLR licence lookup tool** at `/tools/license-lookup` and `/es`, with a live pick as the person types (26 Oct 2026). A daily TDLR pull holds 376,556 licence rows as of 27 Oct 2026 and runs as a GitHub workflow at 22:00 UTC. Source: `/Users/rabies/Desktop/IERHUB.com/16-AdsAnalytics/Wiki/index.md`, "Recent (2026-10-27)" and "Recent (2026-10-22)".
- **Metrics dashboard** (`17-Dashboard`), refreshed by `/ierhub-dashboard`, with a monthly goal of $2,000. Last refresh 24 Oct 2026. Source: `/Users/rabies/Desktop/IERHUB.com/17-Dashboard/Wiki/index.md`.
- **On-site checkout page**, built on branch `feat/onsite-checkout`, not merged, not live. The switch `NEXT_PUBLIC_CHECKOUT_UI` defaults to `hosted`. Source: `/Users/rabies/Desktop/IERHUB.com/6-FrontEndBackendIERhub.com/Wiki/index.md`, section "New this sync, 23 Oct 2026".
- **Plan runner** (`18-RunPlan`), version 1 of 11 Oct 2026, runs a plan as headless sessions of at most 3 items. Source: `/Users/rabies/Desktop/IERHUB.com/Wiki/index.md`, workstream table. This fits page section 2, "Business Operations", under Execution.

Recommendation: add the lookup tool and the dashboard to the overview as marketing and operations assets. Mention the on-site checkout as built, not live.

## 7. One trap for whoever edits the page

The front end wiki says 619 files changed since 28 Sep 2026 and a waterfall pass is pending. Only its dated sections of 23, 27 and 28 Oct 2026 are current. Do not cite its older sections as present state without a check. Source: `/Users/rabies/Desktop/IERHUB.com/Wiki/index.md`, workstream table row for `6-FrontEndBackendIERhub.com`.

## Order of work

1. Item 1, the false Spanish statement. Smallest edit, highest cost if left.
2. Item 2, the sales step. The numbers already exist in the sales page of this repo.
3. Item 3, course 3 status.
4. Items 4, 5 and 6 in one pass.
