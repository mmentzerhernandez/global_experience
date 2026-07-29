# Verified content brief for the id-skills.html refresh

Compiled 2026-07-29 from `/Users/rabies/Desktop/IERHUB.com` and
`/Users/rabies/Desktop/Operating`. Every fact below traces to a source file. Do not add
facts that are not here without reading the source yourself.

## Publication rules

- **Do not publish the course price.** Sources disagree ($29 in
  `1-AboutTheBusiness/Wiki/strategy.md`, $58 in `6-FrontEndBackendIERhub.com/Wiki/index.md`).
  Unresolved, so omit it. The existing delivery diagram shows "Pay $29"; change that node
  to "Card payment via Stripe" with no figure.
- **Do not publish** owner personal details, entity file numbers, EIN, taxpayer number,
  server IP addresses, hostnames beyond the public `start.ierhub.com` and `ierhub.com`,
  or anything from a `_Credentials/` folder.
- **Do not claim "seven checkers."** Six are confirmed as named scripts; the seventh is
  the Stage 4 QA-auditor pass, whose script path was not confirmed. Write it as "six
  checker CLIs plus a report-only QA sweep at Stage 4."
- Do not claim the Spanish course is TDLR-approved. It is not.
- Do not state an incorporation date. None is documented.

## Panel 1: business overview

- International Educational Resources Inc., DBA IERhub.com. Texas TDLR-registered CE
  provider **#2520**, certificate in hand 2026-06-30.
- Live product: **TDLR Course #32815**, Texas Electrician 4-Hour CE Course (English).
  Effective 2026-06-22, expires 2027-06-22. Four 50-minute modules (Texas law and
  Occupations Code Ch. 1305; 16 TAC Ch. 73; NFPA 70E electrical safety; 2026 NEC
  significant changes) totalling 200 minutes and 4.0 CE hours.
- **First paying customer 2026-07-08.** The business is live and selling.
- Buyers: Texas-licensed electricians who must complete state-mandated CE to renew.
  Addressable market roughly 67,000 electricians in CE-required tiers (journeyman
  44,600, master 19,700, residential wireman 2,500, from live TDLR data 2026-07-13).
  The 253,600 apprentices need no CE. Spanish-speaking electricians are the intended
  differentiator; contractors buying for crews are the bulk channel.
- Storefront: ierhub.com, bilingual EN and ES, presented as a 9-trade course catalog
  with 1 purchasable course and 8 trades marked coming soon with notify-me capture.
- Milestone timeline for the table (all verified):
  2026-04 DBA filing; 2026-06-22 course approval effective; 2026-06-30 provider
  certificate; **2026-07-08 first customer**; 2026-07-15 Stripe funnel architecture
  complete; 2026-07-21 Lob becomes the sole certificate-mailing path; 2026-07-22
  license-renewal pages shipped; 2026-07-23 homepage redesign and Spanish renewal
  funnel shipped; 2026-07-27 per-page dwell plugin first installed; 2026-07-28 dwell
  gate deployed to both courses, compliance evidence produced, closeout verification
  PASS.
- Mark 2026-07-08 as the major milestone row.

## Panel 2: how a course is made (session pipeline, adopted 2026-07-12)

Source: `5-CurriculumDevelopment/Wiki/claude-code-session-pipeline.md`.

- Planning model in plan mode gathers requirements and writes the plan; the human
  approves it; `/model sonnet` switches models **in the same session** so the full
  conversation context carries over; the execution model then builds.
- Three skills are reserved for genuine decision forks rather than run on every task:
  deep research only when a plan depends on facts outside the repo and outside training
  data, a decision-maker skill only at a real architectural fork, and an engineering
  plan review for large or risky plans before approval.
- "Fork" here means a decision branch point in the work, not a subagent mechanism. Do
  not conflate them.
- Do not mention any earlier pipeline generation, NotebookLM, Thinkific, or the id-*
  skills. The page covers CourseFactory v2 only.

## Panel 3 parent: CourseFactory v2

Sources: `5-CurriculumDevelopment/CourseFactory-v2/CONTRACT.md` and `ORCHESTRATION.md`,
plus the four `coursefactory-v2*.md` pages in `5-CurriculumDevelopment/Wiki/`.

Framing for the parent panel: CourseFactory v2 is deliberately **not** a one-command
pipeline and there is no master script. A human scaffolds a course directory, then
points a session at that course's ORCHESTRATION.md, and the session is the orchestrator.
Stage order is enforced by input dependencies, not by a driver: each checker hard-fails
when its predecessor's artifact is missing, and the gates are physical files on disk.

Entry: `python3 scaffold.py --dest <path> --slug <course-slug> --modules <count>`.
Refuses to run if the destination exists and is non-empty. Copies CONTRACT.md,
ORCHESTRATION.md, templates/ and tools/ into the new course directory, writes a
commented `course.yaml`, and creates `module-N/lessons/` per module plus `reference/`,
`build/`, and `qa/`.

### Stage 0, Intake (per course, once)

- In: raw sources a human drops into each `module-N/` folder, any format.
- Out: `module-N/fullsource.txt` normalized, plus a filled `course.yaml`.
- Normalization strips headers, footers and page numbers, preserves section numbering
  exactly, UTF-8, one blank line between sections.
- `course.yaml` fields (title, slug, total_minutes, audience, license_fields) are never
  guessed, only asked for. A human picks each module's archetype: overview, changes,
  awareness, or procedure.
- Exit condition: `fullsource.txt` frozen read-only and `course.yaml` validated.

### Stage 1, Groundwork (per module)

- In: `fullsource.txt`. Out: `structure.md`, `relationships.md`, `outline.md`,
  `factcheck/claim-inventory.json`, `factcheck-verdicts.json`. Ends at Gate 1.
- `structure.md` is a complete table-of-contents diff against the source, checked by
  `check_structure.py`.
- `outline.md` must match CONTRACT.md §3 exactly: a time-budget table summing to the
  module's minutes, a `## Sections` block citing real section IDs, an optional
  `## Infographics` table. Checked by `check_outline.py`.
- The claim inventory is verified by `check_facts.py` before the gate.

### Stage 2, Author (per module)

- In: the Gate-1-approved `outline.md`. Out: `reference/explore-the-text.md` (first
  module only), `lessons/LESSON.md`, optional `infographics/`, `timing-stamp.json`,
  `factcheck-report.md`. Ends at Gate 2.
- Page rules: 150 to 450 words per page, the pattern "plain restatement, workplace
  example, citation", a knowledge check every 3 to 5 pages, and no verbatim source text
  on any page.
- Fact-checking over LESSON.md is unconditional: never skipped, never sampled. Every
  infographic title, label, description and value counts as a claim.
- Non-public-domain passages get a copyright-gate pass.

### Stage 3, Package (per module, then per course)

- In: both `gate1-approved.txt` and `gate2-approved.txt`. Out: `build/module-N.mbz` and
  `build/import-checklist.md`. Ends at Gate 3.
- `build_mbz.py` refuses to run without both gate files, then self-checks page counts,
  that every knowledge check has a correct answer, that the completion timer equals
  minutes times 60, and that the archive parses.
- Mapping (CONTRACT.md §7): each `### Page:` becomes a Moodle `mod/lesson` content page
  where Continue advances; each `### Check:` becomes an ungraded multichoice question
  page where a wrong answer returns the learner to the same page. Each module becomes
  one lesson activity with `completion=2`, `completionendreached=1`, and
  `completiontimespent` set to minutes times 60. Infographics embed as
  `@@PLUGINFILE@@` images with `files.xml` and `inforef.xml` records.
  `reference/explore-the-text.md` becomes an untimed Book or Page resource added
  manually per the import checklist.
- Caveat to state honestly: a synthetic reference `.mbz` is the packaging base, and
  Moodle restore validation into the staging sandbox is still pending before first
  production use.

### Stage 4, Sweep and filing (per course)

- In: all module fact-check reports plus a passed Gate 3. Out:
  `qa/course-factcheck-summary.md`, `qa/qa-report.md`, an approval package, and
  `qa/feedback-log.md`.
- Requires zero outstanding UNSUPPORTED claims. The QA-auditor pass is report-only and
  produces `qa-report.md` for human triage. The feedback log is reviewed each renewal
  cycle.

### Checkers panel

Six confirmed checker CLIs, each independently runnable by hand against a checked-in
fixture module, plus the Stage 4 report-only QA sweep:

1. `check_structure.py` (blocking): structure.md is a complete TOC diff against source.
2. `check_outline.py` (blocking): time budget sums exactly, mandated topics present,
   section IDs real.
3. `check_facts.py` (blocking): the retrieval-grounded claim verifier, run at Stage 1
   over outline claims and Stage 2 over lesson claims. Fails on any UNSUPPORTED or
   CONTRADICTED verdict. NOT-IN-SOURCE and NEEDS-REVIEW go to the gate list without
   failing the check.
4. `check_infographics.py` (blocking when infographics are planned): runs the 5-stage
   infographic pipeline and checks output against the Gate-1-approved plan.
5. `stamp_timing.py`: computes estimated minutes and a verdict of OK, OVER or UNDER
   against budget. OVER or UNDER requires rework before Gate 2.
6. `build_mbz.py` (blocking): packaging plus the self-checks listed under Stage 3.

Fact-checker architecture, the most technically interesting piece, describe accurately:
it re-execs into an isolated venv, sectionizes `fullsource.txt` into section-aware
chunks, and runs hybrid retrieval combining BM25 with dense embeddings through a
LangChain ParentDocumentRetriever and EnsembleRetriever, followed by a cross-encoder
rerank. A LangGraph StateGraph cascade retrieves, applies a rerank-floor gate (below
0.15 goes straight to UNSUPPORTED without running NLI), then an NLI judge computes
entailment and contradiction (entailment at or above 0.60 is SUPPORTED, contradiction
at or above 0.60 is CONTRADICTED, anything else escalates). An escalation tier adds
MiniCheck and LettuceDetect, a token-span hallucination detector. Claims explicitly
marked external skip retrieval and always return NOT-IN-SOURCE. The vector store is
Chroma, persisted per module and keyed to a corpus hash. Test and production profiles
swap the embedding and reranker models. Verdict vocabulary: SUPPORTED, UNSUPPORTED,
NOT-IN-SOURCE, CONTRADICTED, NEEDS-REVIEW.

### Gates panel

- **Gate 1**, between Stage 1 and Stage 2. A human reviews `outline.md`, the checker
  output, and the NOT-IN-SOURCE and NEEDS-REVIEW claim list, then decides. Approval
  writes `module-N/gate1-approved.txt`.
- **Gate 2**, between Stage 2 and Stage 3. A human reviews `LESSON.md`, the timing
  verdict, the fact-check summary, copyright verdicts, and any infographic renders.
  Approval writes `module-N/gate2-approved.txt`.
- **Gate 3**, per course, between Stage 3 and Stage 4. A human restores the `.mbz` into
  a Moodle sandbox and checks, per module, that the completion timer blocks until the
  declared minutes have elapsed and the lesson end is reached, that real read time is
  within tolerance of the timer (the 16 TAC §59.30(k) requirement), and that the
  certificate issues with license fields populated.
- Why piecemeal checker runs cannot skip gates: gates are files on disk, and
  `build_mbz.py` refuses to run unless both approval files exist. The failure-handling
  table in ORCHESTRATION.md is closed; anything not in it is a hard stop.

## Panel 4: compliance engineering

Sources: `1-AboutTheBusiness/Wiki/syntheses/ce-provider-revenue-criteria.md` and the
`4-Compliance/` evidence files dated 2026-07-28.

The four gates that stand between the business and its revenue:

1. **Before selling**: CE provider registration current on fees (§59.20), course
   approval per course and occupation (§59.22(e)), entity in good standing, background
   statement commitments on file. TDLR will not approve courses from a provider past
   due (§59.22(o)).
2. **At the moment of sale**: every advertisement must show the provider number and
   course number, and a web page counts as an advertisement (§59.24(b)); no false or
   misleading advertising (§59.24(j)); full fee disclosure (§59.24(k)); the course must
   run as represented, including attendance verification and seat-time enforcement
   (§59.24(l)); no enrolling while past due (§59.24(n)).
3. **After completion, two clocks**: the certificate must issue within **15 days**
   (§59.24(d)) and the completion roster must reach TDLR within **7 days** (§59.24(e)).
   Standing tail: retain records 2 years (§59.24(f)), provide participant records
   within 10 days of a request (§59.24(g)), and allow unannounced auditor access where
   auditors never pay to enroll (§59.22(n)).
4. **Annual renewal**: provider registration renewal (§59.21) and course approval
   renewal before the 2027-06-22 expiry, with internal review starting 90 days prior. A
   lapsed registration or expired approval makes every subsequent sale unlicensed.

Penalty exposure across all four: up to **$5,000 per day per violation** (Tex. Occ.
Code §51.302(a)), with each day a violation continues counted separately, plus possible
revocation, suspension, or ordered consumer refunds.

Engineering that keeps gate 2 and gate 3 open. Two distinct mechanisms, and the
distinction matters:

- `local_seattimer` is the binding control that satisfies the 50-minutes-per-module
  requirement of §59.30(k). It measures cumulative seat time from the lesson timer rows.
- `local_pagedwell`, the per-page dwell gate live 2026-07-28, is a **voluntary**
  strengthening layer on top. It is not itself a TDLR requirement; disable it and the
  courses still meet the binding requirement through the seat timer.

How the dwell gate works, and why the design is the interesting part:

- Every gated lesson page carries a required-seconds allocation, and the per-lesson sum
  is always exactly 3000 seconds, or 50 minutes. Verified across all 8 gated lessons on
  2026-07-28.
- A client-side widget beats the server about every 30 seconds, but only while the tab
  is focused, visible, and has seen activity since the last beat. **The server computes
  the credit itself** as the smaller of the gap since the last beat and a 75-second
  grace cap, bounded absolutely by the time since first view. The client never sends a
  duration and the server never trusts one. Over-credit is structurally impossible
  rather than merely unobserved.
- Enforcement runs server-side on every request through Moodle's `after_config` hook,
  independent of JavaScript. A learner who strips the disabled attribute off a button
  in devtools is still refused.
- Exemption is capability-based and granted only to editing-teacher and manager
  archetypes. The TDLR auditor role is deliberately **not** exempt and is gated exactly
  like a student, so an auditor walkthrough produces the same evidence trail a real
  learner's would.
- English and Spanish are page-for-page identical in page count and per-page split,
  each totalling 3000 seconds. Two orientation lessons are deliberately excluded and
  carry no CE credit.

Measured accrual behavior (the rate investigation closed 2026-07-27): active reading
credits at 0.85 to 1.0 times wall clock and never above; passive idle with no requests
credits zero; returning after idle credits exactly the 75-second grace, with a clawback
that moves the start time forward to strip anything beyond it; two concurrent browser
tabs credit 1.0 times, not 2.0, measured directly rather than reasoned about. Both
defects found were under-credit only, never over-credit.

Honest limitations to state rather than hide: refused navigation attempts are not
logged anywhere, so an auditor cannot get a discrete count of skip attempts even though
enforcement itself is unaffected. A learner with JavaScript disabled has no fallback
accrual path and gets stuck, a usability finding rather than a security gap. Two of
three designed remedy layers for the start-over defect were never shipped.

## Panel 5: how the business is organized and run

Source: the IERHUB.com `CLAUDE.md`, `Wiki/index.md`, `.claude/manifest.json`,
`10-Plans/README.md`, `_Continuity/CONTINUITY.md`, and
`/Users/rabies/Desktop/Operating/OperatingSystem.md`.

- **Folders as workstreams.** Ten numbered folders, each owning one workstream: the
  right to operate (1), paid acquisition (2), the tool library (3), compliance (4),
  curriculum development (5), the funnel and delivery stack (6), social media (7),
  design (9), plans (10), and research (11). Folder 8, certificate printing by mail,
  was retired 2026-07-21 when the Lob path inside folder 6 took over. Underscore-prefixed
  folders hold cross-cutting infrastructure: `_Admin`, `_Continuity`, `_Credentials`,
  `_Archive`. Certain paths are zero-rename zones because launchd jobs, skills, and
  handoffs reference them by absolute path.
- **Three-tier wiki.** Tier 1 is the master wiki and carries navigation and governance
  only, never operational facts. Tier 2 is one wiki per workstream. Tier 3 is a deep
  operational wiki sitting beside the code it documents. When two tiers disagree, the
  more specific tier wins for its own domain; the fix goes in at the authoritative
  source and syncs upward. A skill cascades tier 2 up into tier 1 and regenerates a
  single self-contained HTML briefing of the whole business.
- **One fact, one home.** Decisions live in `.claude/manifest.json`, progress lives in
  the plan folders, know-how lives in the wiki. A fact stored in two places will
  eventually disagree with itself. The manifest holds durable judgment calls with dates
  and rationales, roughly 30 of them, and deliberately does not hold task progress.
- **Session waterfall.** No session exceeds 50% of its context. At that mark work stops
  cleanly, a handoff is written containing the verification command, what was completed,
  the ordered remaining work, the constraints and dead ends discovered, and the exact
  next step, and a fresh session picks up from the handoff alone.
- **Plans discipline.** Status is a folder move and nothing else: current, future,
  inactive, past. A plan set is not complete until every checkbox is marked, the final
  handoff carries a completion line plus its verification result, and the folder has
  physically moved. A completion marker still sitting in the current folder is drift by
  definition, and a script exits non-zero when it finds one.
- **Continuity.** A scheduled job mirrors the workspace daily into a private repo,
  sanitized: credential folders and the whole payments and funnel tree are excluded by
  design, appearing in changelogs as change counts only. A heartbeat file records proof
  of life, and a scheduled check opens an issue if no commit lands for 7 days.
- **Cold start.** A session with no prior context reads the manifest, then the plan and
  the highest-numbered handoff, runs the verification script, and continues at the next
  step.
- The whole arrangement is a general toolkit installed into this business, adopted in
  stages rather than all at once, and this business is its production example.

Diagram, portrait TD, 9 nodes: Owner drives plan work in 10-Plans (PLAN.md plus
HANDOFF-N); plan work runs under the session waterfall which stops at 50% and hands off;
decisions land in the manifest; the manifest governs both the three-tier wiki (which
renders to the HTML briefing) and the numbered workstream folders; the workstreams feed
the daily sanitized continuity mirror, which is watched by the dead-man check.

## Panel 6: delivery platform

- Self-hosted Moodle at start.ierhub.com delivers the approved course and is the system
  of record for completions and the 2-year retention requirement. Two courses: English
  and Spanish.
- Stripe checkout is the system of record for who bought what and when. English has a
  webhook-driven enrollment path. Spanish currently has no fee enrollment row and
  cannot be sold through the self-service path yet; a Spanish checkout flow is in
  progress but not shipped.
- Certificate mailing runs through Lob, the sole canonical path since 2026-07-21. The
  pipeline is built, deployed, and verified end to end in test mode; only the owner's
  go-live steps remain.
- Certificates must issue within 15 days and carry the TDLR-required fields. The
  Spanish certificate template deliberately carries placeholder text instead of a
  course number, so it cannot falsely claim an approval that does not exist yet.
- Existing diagram content that stays accurate: the learner, provider admin and TDLR
  auditor roles; pay, enroll and log in; four 50-minute modules; the seat-time gate; no
  duplicate credit within 12 months; certificate issued; roster to TDLR within 7 days.
  Update the retention node from four years to two years, and remove the price figure.

## Future course pipeline (for the business overview panel)

- Spanish electrician: phase 3 of 5, translations done, language-pack switch next. Not
  TDLR-approved and must not be described as approved.
- Barber and cosmetology: all four modules authored and packaged, QA not yet run.
- Registered Accessibility Specialist: sources gathered for four modules, no build yet.
  Self-reported, so no TDLR provider approval is needed, making it the fastest possible
  launch once built.
- Towing operators: not started, and next in the market decision, followed by HVAC,
  which is blocked on copyrighted code licensing.
- Cross-cutting: an NFPA copyright clearance request has been pending since 2026-05-30,
  which is why the newer verticals deliberately use public-domain sources.
