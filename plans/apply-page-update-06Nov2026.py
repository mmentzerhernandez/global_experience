#!/usr/bin/env python3
"""Apply the 06 Nov 2026 text changes to the curriculum business page.

Source of each change: plans/RECOMMENDATIONS-curriculum-business-page-update-06Nov2026.md
Every replacement must match exactly once, or the script exits and writes nothing.
The new diagrams go in as placeholders. plans/inline-06Nov2026-svgs.py fills them.
"""
import re, sys

PAGE = "/Users/rabies/global_experience/automated-curriculum-development-business.html"
src = open(PAGE, encoding="utf-8").read()


def sub1(old, new, regex=False):
    global src
    if regex:
        n = len(re.findall(old, src, flags=re.S))
        if n != 1:
            sys.exit(f"expected 1 match, found {n}: {old[:80]}")
        src = re.sub(old, lambda m: new, src, count=1, flags=re.S)
    else:
        n = src.count(old)
        if n != 1:
            sys.exit(f"expected 1 match, found {n}: {old[:80]}")
        src = src.replace(old, new)


def hole(name):
    return f'<div class="canvas" data-diagram="{name}"></div>'


P = '<p style="margin-top: 0; margin-bottom: 16px">'
LI = '<li style="margin-bottom: 8px">'
BLOCK = '<div style="max-width: 800px; margin: 0 0 8px; line-height: 1.6; color: #333">'
H3 = '<h3 style="color: #1a202c; margin: 0 0 8px">'
H3B = '<h3 style="color: #1a202c; margin: 32px 0 8px">'

# ---------------------------------------------------------------- navigation
for old, new in [
    ("<h3>1 - Overview</h3>\n          <p>Automation</p>", "<h3>1 - Overview</h3>\n          <p>Automation to First Sale</p>"),
    ("<p>Foundation to Resilience</p>", "<p>Knowledge Is the Base</p>"),
    ("<p>One Session, Two Models</p>", "<p>Nine Stages from Rule to Sale</p>"),
    ("<p>Five Stages, Three Gates</p>", "<p>Five Stages and Three Gates</p>"),
    ("<p>Detail · Source intake</p>", "<p>Detail · Source Intake</p>"),
    ("<p>Detail · Moodle LMS build</p>", "<p>Detail · Moodle LMS Build</p>"),
    ("<h3>The checkers</h3>", "<h3>The Checkers</h3>"),
    ("<p>Reference · Six checkers</p>", "<p>Reference · Seven Checkers</p>"),
    ("<h3>The three gates</h3>", "<h3>The Three Gates</h3>"),
    ("<p>Reference · Review gates</p>", "<p>Reference · Review Gates</p>"),
    ("<p>Seat Time & Evidence</p>", "<p>Seat Time and Evidence</p>"),
]:
    sub1(old, new)
sub1(
    '<h3>6 - Delivery platform</h3>\n          <p>Moodle LMS, Stripe, Certificates</p></a\n        >',
    '<h3>6 - Delivery Platform</h3>\n          <p>Moodle LMS, Stripe and Certificates</p></a\n        >\n'
    '        <a class="box" href="#how-ai-is-used"\n          ><h3>7 - How AI Is Used</h3>\n'
    '          <p>Models, Agent Rules, Four Pane Runs</p></a\n        >',
)

# ---------------------------------------------------------------- panel 1
sub1(
    """          <td class="c-step">5</td>
          <td class="c-name">Curricula to Social Media</td>""",
    """          <td class="c-step">5</td>
          <td class="c-name">Courses #3 and #4 Approval</td>
          <td class="c-status"><span class="status-badge completed">Completed</span></td>
          <td>
            <strong>Texas Cosmetology 4-Hour CE</strong> (TDLR #33555) and <strong>Texas Cosmetology 2-Hour CE</strong> for licensees of 15 years or more (TDLR #33554) were approved by TDLR in <strong>Nov 2026</strong>. Each course holds English and Spanish in one Moodle course.
          </td>
        </tr>
        <tr>
          <td class="c-step">6</td>
          <td class="c-name">Cosmetology on the Website</td>
          <td class="c-status"><span class="status-badge completed">Completed</span></td>
          <td>
            The English and Spanish course pages and the checkout went live on <strong>November 5, 2026</strong>.
          </td>
        </tr>
        <tr>
          <td class="c-step">7</td>
          <td class="c-name">Curricula to Social Media</td>""",
)
sub1(
    """          <td class="c-step">6</td>
          <td class="c-name">Scale & Repeat Cycle</td>""",
    """          <td class="c-step">8</td>
          <td class="c-name">Scale & Repeat Cycle</td>""",
)
sub1(
    "Currently converting the curriculum pipeline to an automated social media distribution pipeline to market the English and Spanish electrician courses.",
    "The business is changing the course content into an automated social media process, to market the English and Spanish courses.",
)
sub1(
    "From idea to paying customers, the goal is to scale the remaining TDLR continuing education courses to targeted TDLR professionals.",
    "The goal is to build, approve and sell the remaining TDLR continuing education courses with the same process.",
)
sub1("<strong>Consistency:</strong> standardized, high-quality course structures every time.",
     "<strong>Consistency:</strong> each course has the same checked structure.")
sub1("<strong>Speed:</strong> drastically reduced course development time.",
     "<strong>Speed:</strong> each course takes less time to develop.")
sub1("<strong>Scale:</strong> rapid production and deployment to market.",
     "<strong>Scale:</strong> the same process builds each new course for a new trade.")
# Overview diagram: the first canvas inside the business-overview panel.
i = src.find('id="business-overview"')
j = src.find('id="operating-system"')
sec = src[i:j]
m = re.search(r'<div class="canvas">\s*<svg\s+id="my-svg".*?</svg>\s*</div>', sec, flags=re.S)
if not m:
    sys.exit("overview canvas not found")
src = src[:i] + sec[: m.start()] + hole("business-overview") + sec[m.end():] + src[j:]

# ---------------------------------------------------------------- panel 2
sub1(
    r'<p style="margin-top: 16px; margin-bottom: 16px">\s*The business runs via the eight listed processes below:.*?</ul>\s*</div>\s*(?=<div class="canvas">\s*<svg id="op-one-fact-svg")',
    f"""<p class="arc-kicker">Foundation</p>
            {H3}Records Are the Base of the Business</h3>
            {P}
              The business runs on its written records. Each fact has one home, and every AI session reads that home before it does any work. Decisions live in the project manifest, <code>.claude/manifest.json</code>. The progress of each plan lives in its plan folder, in <code>PLAN.md</code> and the numbered handoff files. Business knowledge lives in three levels of wikis: one main wiki, one wiki for each workstream folder, and detailed wikis for reference documents and code. A knowledge graph connects all of these files. The graph holds 6,448 items and 9,774 links between them, and a session asks the graph how one file, plan or course connects to another. Because the records hold the knowledge, a new session continues the work of the last session without a repeat explanation. The sections below show how the business uses these records to plan, run, communicate, improve and recover.
            </p>
          </div>

          """,
    regex=True,
)
sub1("The diagram traces one plan through its life. A status change is a folder move and nothing else.",
     "The diagram shows each folder that one plan moves through. A status change moves the folder.")
sub1("The workspace holds seventeen numbered folders, from <code>000-Dashboard</code> to <code>16-AdsAnalytics</code>.",
     "The workspace holds nineteen numbered folders, from <code>000-Dashboard</code> to <code>18-RunPlan</code>.")
sub1(
    "Every day a sync runs <code>/ierhub-current-state</code> syncs each tier upward and rebuilds <code>0-CurrentState.html</code>, the one-file briefing of the whole business.",
    "About once a week, the operator runs <code>/ierhub-current-state</code>. It syncs each tier upward and rebuilds <code>0-HitByABus.html</code>, the one-file briefing of the whole business.",
)
# Remove Execution and Systems. The Systems diagram moves to panel 7.
m = re.search(
    r'\s*<div style="max-width: 800px; margin: 0 0 8px; line-height: 1.6; color: #333">\s*<p class="arc-kicker">Execution</p>.*?(<div class="canvas">\s*<svg id="op-subagents-svg".*?</svg>\s*</div>)',
    src, flags=re.S)
if not m or len(re.findall(r'<p class="arc-kicker">Execution</p>', src)) != 1:
    sys.exit("execution block not found")
subagents_canvas = m.group(1)
src = src[: m.start()] + src[m.end():]

# ---------------------------------------------------------------- panel 3
sub1(
    r'<section class="panel" id="session-pipeline">.*?</section>',
    f"""<section class="panel" id="session-pipeline">
          <div class="detail-head">
            <h2>3 - How a Course Gets Built</h2>
          </div>
          {BLOCK}
            {P}
              Each new course starts as a copy of one Jira template, KAN-1. The copy holds nine stages. Each stage ends with a proof, and a stage with no proof is not done. One course holds English and Spanish together, with one TDLR application and one TDLR course number.
            </p>
          </div>
          <div class="path-table-wrap">
            <table class="path-table">
              <thead>
                <tr><th>Stage</th><th>Work</th><th>Proof</th></tr>
              </thead>
              <tbody>
                <tr><td class="c-name">A. Rules and Sources</td><td>Get the current rule text of the trade. Map each rule to a module. Calculate the required minutes.</td><td>The rule files with their amendment dates</td></tr>
                <tr><td class="c-name">B. Outline</td><td>Write the outline by topic, with minutes and a source for each row.</td><td>The outline passes the language checker.</td></tr>
                <tr><td class="c-name">C. Moodle Shell</td><td>Make a hidden bilingual course, the certificate and the TDLR application.</td><td>A second run of the script changes nothing.</td></tr>
                <tr><td class="c-name">D. English Text</td><td>Write each module with <a href="#coursefactory-overview">CourseFactory v2</a>, then check the facts.</td><td>A person approves the English text.</td></tr>
                <tr><td class="c-name">E. Spanish and Package</td><td>Write the Spanish text and the diagrams. Package the course.</td><td>The approval files of the gates</td></tr>
                <tr><td class="c-name">F. Load and Timing</td><td>Load each module. Test the 200 minute seat time with a test learner.</td><td>The timing test result</td></tr>
                <tr><td class="c-name">G. Walkthrough</td><td>Open every page in English and in Spanish.</td><td>A screenshot of every page</td></tr>
                <tr><td class="c-name">H. TDLR Approval</td><td>Send the application. Put the TDLR course number on the certificate.</td><td>The certificate PDF shows the correct number.</td></tr>
                <tr><td class="c-name">I. Website and Sale</td><td>Add the course page and the checkout. Buy the course and refund it.</td><td>The enrollment, the email and the refund records</td></tr>
              </tbody>
            </table>
          </div>
          {BLOCK}
            {P}
              The electrician course is the one exception. It is two Moodle courses, one for English and one for Spanish, because it came first.
            </p>
          </div>
          {hole("session-pipeline")}
        </section>""",
    regex=True,
)

# ---------------------------------------------------------------- panel 4
sub1(
    r"CourseFactory v2 is deliberately not a one-command pipeline.*?not a workflow engine's internal state\.",
    "CourseFactory v2 has no single script that runs all stages. A session reads the <code>ORCHESTRATION.md</code> file of the course and runs each stage in order. Each checker stops when the file from the stage before it is missing. Each gate is a file on disk.",
    regex=True,
)
sub1("<strong>Five stages, three gates:</strong>", "<strong>Five stages and three gates:</strong>")
for old, new in [
    ("<h2>Stage 0, intake</h2>", "<h2>Stage 0: Intake</h2>"),
    ("<h2>Stage 1, groundwork</h2>", "<h2>Stage 1: Groundwork</h2>"),
    ("<h2>Stage 2, author</h2>", "<h2>Stage 2: Author</h2>"),
    ("<h2>Stage 3, package</h2>", "<h2>Stage 3: Package</h2>"),
    ("<h2>Stage 4, sweep and filing</h2>", "<h2>Stage 4: Sweep and Filing</h2>"),
    ("<h2>Checkers</h2>", "<h2>The Checkers</h2>"),
    ("<h2>Gates</h2>", "<h2>The Three Gates</h2>"),
    ('<span class="pill">Per course · Once</span>', '<span class="pill">Per Course · Once</span>'),
    ('<span class="pill">Per module · Ends at Gate 1</span>', '<span class="pill">Per Module · Ends at Gate 1</span>'),
    ('<span class="pill">Per module · Ends at Gate 2</span>', '<span class="pill">Per Module · Ends at Gate 2</span>'),
    ('<span class="pill">Per module, then per course · Ends at Gate 3</span>', '<span class="pill">Per Module, Then per Course · Ends at Gate 3</span>'),
    ('<span class="pill">Per course</span>', '<span class="pill">Per Course</span>'),
    ('<span class="pill">Validate · Block or report</span>', '<span class="pill">Validate · Block or Report</span>'),
    ('<span class="pill">Decide · Sign-off</span>', '<span class="pill">Decide · Sign-Off</span>'),
    ("Each module's archetype is chosen deliberately: overview, changes, awareness, or procedure.",
     "Each module has one archetype: overview, changes, awareness, or procedure."),
    ("where Continue advances; each Check block", "where Continue advances. Each Check block"),
    ("<strong>Honest limitation:</strong> a synthetic reference archive is the packaging base, and Moodle LMS restore validation into the staging sandbox is still pending before first production use.",
     "<strong>Not yet proven:</strong> a synthetic reference archive is the packaging base. Nobody has yet restored the archive into the Moodle LMS staging site."),
    ("produces <code>qa-report.md</code> for triage; it blocks nothing by itself.",
     "produces <code>qa-report.md</code> for triage. It blocks nothing by itself."),
    ("Fails on any UNSUPPORTED or CONTRADICTED verdict; NOT-IN-SOURCE", "Fails on any UNSUPPORTED or CONTRADICTED verdict. NOT-IN-SOURCE"),
    ('<h3 style="color: #1a202c; margin-bottom: 8px">Fact-checker architecture</h3>',
     '<h3 style="color: #1a202c; margin-bottom: 8px">How the Fact Checker Works</h3>'),
    ("An\n              escalation tier adds a token-span hallucination detector for closer review.",
     "An\n              escalation tier adds MiniCheck and LettuceDetect, a token-span hallucination detector, for closer review."),
    ("<strong>Gate 1</strong>, between Stage 1 and Stage 2: the outline.md, checker output, the checker output, and the NOT-IN-SOURCE and NEEDS-REVIEW claim list, then decides.",
     "<strong>Gate 1</strong>, between Stage 1 and Stage 2: a person reads outline.md, the checker output, and the NOT-IN-SOURCE and NEEDS-REVIEW claim list, then decides."),
]:
    sub1(old, new)
sub1(
    r"Six checker CLIs run at fixed points across the five stages, each independently runnable by hand\s*against a checked-in fixture module, plus a report-only QA sweep at Stage 4 that blocks nothing on\s*its own\.",
    "Seven checker scripts run at fixed points across the five stages. A person can run each one by hand against a test module. A QA sweep at Stage 4 writes a report and blocks nothing.",
    regex=True,
)
sub1(
    f"{LI}<strong>build_mbz.py</strong> (blocking)",
    f"{LI}<strong>check_nonwords.py</strong>: finds words in the lesson text that do not exist, at Stage 2.</li>\n              {LI}<strong>build_mbz.py</strong> (blocking)",
)
sub1(
    r"Gates are files on disk, not a checklist someone can skip by working faster\. build_mbz\.py refuses to\s*run unless both approval files exist, so a piecemeal run of the checkers cannot substitute for a gate\s*review\. The failure-handling table in ORCHESTRATION\.md is closed: anything not listed in it is a hard\s*stop\.",
    "Each gate writes a file, and the next stage does not start without that file. build_mbz.py refuses to run unless both approval files exist. The failure table in ORCHESTRATION.md is closed: any failure that the table does not list stops the run.",
    regex=True,
)

# ---------------------------------------------------------------- panel 5
sub1("<h2>5 - Compliance Organization</h2>", "<h2>5 - Compliance Engineering</h2>")
i = src.find('id="compliance-engineering"')
j = src.find('id="tx4hrce-delivery"')
sec = src[i:j]
m = re.search(r'<div class="canvas">\s*<svg id="dwell-gate-svg".*?</svg>\s*</div>\s*<div style="margin: 0; padding: 0; font-family: sans-serif; line-height: 1.6; color: #333">.*?</div>', sec, flags=re.S)
if not m:
    sys.exit("compliance block not found")
rows = [
    ("Before the course", "The learner holds a license for the trade.", "The license gate keeps the course closed until the learner selects a valid TDLR license."),
    ("At the sale", "Each advertisement shows the provider number and the course number. A web page is an advertisement.", "Each course page must show both numbers and the full fee."),
    ("During the course", "Each CE hour is 50 minutes of instruction. A 4-hour course is 200 minutes.", "Each page has a minimum time. Each lesson totals 3,000 seconds. The server counts the time. The browser never sends a time."),
    ("During the course", "The learner does the lessons in order.", "Each lesson opens only after the lesson before it is complete."),
    ("During the course", "The learner is present.", "A heartbeat goes to the server every 30 seconds. After 5 minutes with no input, a warning shows. One minute later, the site logs the learner out."),
    ("After the course", "The learner gets a certificate within 15 days.", "The certificate needs every lesson complete. The PDF goes to the learner by email. It shows the trade, the TDLR course number, 200 minutes and a verification code."),
    ("After the course", "TDLR gets the roster within 7 days.", "A staff alert with a seat time line goes out about 2 minutes after completion. A person files the roster. A script reads the TDLR confirmation twice a day and emails the learner."),
    ("Always", "Records stay for 2 years. TDLR auditors get access at any time and never pay.", "A TDLR auditor has a read only account. The timer applies to the auditor the same as to a learner, so the auditor sees the same evidence."),
    ("Once a year", "The provider registration and each course approval stay current.", "Internal review starts 90 days before each expiry date."),
]
body = "\n".join(
    f"                <tr><td class=\"c-name\">{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in rows
)
new_compliance = f"""{BLOCK}
            {H3}How the Courses Meet TDLR Rules</h3>
            {P}
              TDLR sets rules before a sale, at the sale, during and after the course, and once a year. A broken rule can cost up to $5,000 for each day (Texas Occupations Code §51.302(a)). The Moodle LMS site enforces each rule in code, and it keeps a record that an auditor can read.
            </p>
          </div>
          <div class="path-table-wrap">
            <table class="path-table">
              <thead>
                <tr><th>When</th><th>Rule</th><th>How the Business Meets It</th></tr>
              </thead>
              <tbody>
{body}
              </tbody>
            </table>
          </div>
          {BLOCK}
            {H3B}How the Seat Time Gate Works</h3>
            {P}
              Two Moodle LMS plugins share the work. <code>local_pagedwell</code> shows the timer and holds each page until its minimum time is met. <code>local_seattimer</code> sends the heartbeat and logs out an inactive learner. The server checks every request, so a change in the browser cannot open a page early. Only teachers and managers are exempt.
            </p>
          </div>
          {hole("dwell-gate")}"""
src = src[:i] + sec[: m.start()] + new_compliance + sec[m.end():] + src[j:]

# ---------------------------------------------------------------- panel 6
sub1(
    r"A self-hosted Moodle LMS instance at start\.ierhub\.com delivers the approved course.*?Two courses run on it, English and\s*Spanish\.",
    "A self-hosted Moodle LMS site at start.ierhub.com delivers the approved courses. It is the system of record for completions and for the two-year retention requirement. Four courses run on it: electrician in English (TDLR #32815), electrician in Spanish (TDLR #32973), cosmetology 4-hour (TDLR #33555) and cosmetology 2-hour (TDLR #33554).",
    regex=True,
)
sub1(
    r"English has a webhook-driven enrollment path\..*?a Spanish checkout flow is in progress but not shipped\.",
    "A Stripe webhook starts the enrollment of each buyer. The Spanish electrician course is on sale since July 31, 2026.",
    regex=True,
)
sub1(
    "<strong>Certificate mailing:</strong> Certificates print and mail through mailing integration.",
    "<strong>Certificates:</strong> each learner gets the certificate PDF by email. The print and mail code is complete, but it is not in use.",
)
sub1(
    f"""{LI}
                <strong>Certificates:</strong>""",
    f"""{LI}
                <strong>The diagram:</strong> it shows the four modules of the electrician course. The cosmetology courses use the same steps.
              </li>
              {LI}
                <strong>Certificates:</strong>""",
)

# ---------------------------------------------------------------- panel 7 (new)
model_rows = [
    ("Fable 5", "Writes the plan and makes the hard design decisions. It has no item tag, because the operator uses it only for plans and high risk decisions."),
    ("Opus 5.5", "Does the items tagged <code>[OPUS]</code>. It also runs the Decision Maker pane when a run stops."),
    ("Sonnet 5.5", "Does the items tagged <code>[SONNET]</code> and every item with no tag. It writes most of the code and the handoffs."),
    ("Haiku 5.5", "Does the items tagged <code>[HAIKU]</code>: small edits, log cleanup, file moves and file renames."),
]
pane_rows = [
    ("Red: All Steps of the Plan", "Shows every group and item with its state: done, active or queued. It shows the percent of the plan that is complete, the time left, and the time used."),
    ("Green: Work", "Runs one Claude session for each group. The session does one item at a time, in plan order, and marks each item done when its check passes."),
    ("Blue: Director", "Runs the director script. It starts each Green session, waits for the handoff, checks the result files on disk, and then starts the next group."),
    ("Yellow: Decision Maker", "Stays open for the whole run. When a run stops on a problem, the director starts one Opus session here. That session decides the next step and writes the decision to a file."),
]
mrows = "\n".join(f"                <tr><td class=\"c-name\">{a}</td><td>{b}</td></tr>" for a, b in model_rows)
prows = "\n".join(f"                <tr><td class=\"c-name\">{a}</td><td>{b}</td></tr>" for a, b in pane_rows)
panel7 = f"""
        <section class="panel" id="how-ai-is-used">
          <div class="detail-head">
            <h2>7 - How AI Is Used</h2>
          </div>
          {BLOCK}
            <p class="arc-kicker">Models</p>
            {H3}Each Model Has One Job</h3>
            {P}
              Each plan item carries a tag that names the model that does it. The tag sets the cost of the item.
            </p>
          </div>
          <div class="path-table-wrap">
            <table class="path-table">
              <thead><tr><th>Model</th><th>Job</th></tr></thead>
              <tbody>
{mrows}
              </tbody>
            </table>
          </div>

          {BLOCK}
            <p class="arc-kicker">Runs</p>
            {H3B}From a Conversation to a Plan to a Four Pane Run</h3>
            <ol style="padding-left: 20px">
              {LI}The operator and Claude Code talk through the work in a brainstorm session. The session asks questions until the goal, the limits and the proof of each step are clear.</li>
              {LI}The session writes a plan folder. <code>PLAN.md</code> holds the work in numbered groups. Each item names its model, the result it must give, and a time estimate. <code>APPROVALS.md</code> holds the operator's answer to each decision gate. <code>FACTS.md</code> holds the measured facts.</li>
              {LI}The <code>/herdr-plan-run</code> skill prepares the folder. It checks every permission, service and file that the items need, and it writes <code>RESOURCES: PASS</code> only when each check passes. Then it gives the operator two commands.</li>
              {LI}The operator types the commands in herdr, a terminal program that shows several panes on one screen. The director script opens four panes, side by side.</li>
            </ol>
          </div>
          <div class="path-table-wrap">
            <table class="path-table">
              <thead><tr><th>Pane</th><th>What It Does</th></tr></thead>
              <tbody>
{prows}
              </tbody>
            </table>
          </div>
          {BLOCK}
            <ol start="5" style="padding-left: 20px">
              {LI}Each Green session measures its own context use with a script. At 50 percent, it writes a handoff and stops. The director starts a new session from the handoff.</li>
              {LI}The last item of every plan pushes the branch and opens a pull request. No session merges. The operator reviews the pull request.</li>
            </ol>
          </div>

          {BLOCK}
            <p class="arc-kicker">Life of a Feature</p>
            {H3B}How a Plan Runs from Start to Finish</h3>
            {P}
              The diagram shows the full life of one feature: the command that starts it, the herdr run, the pull request, and the removal of the finished work from the disk. A box with a dashed border is a part that the tooling plan builds.
            </p>
          </div>
          {hole("plan-run")}

          {BLOCK}
            <p class="arc-kicker">Agent Rules</p>
            {H3B}Limits on Helper Agents</h3>
            {P}
              A session can start helper agents. Without limits, a session can start too many, run them out of view, and report its own success. Two layers stop this.
            </p>
            <ul style="padding-left: 20px">
              {LI}<strong>Hard limits, set by the system.</strong> A session can start three helper agents at most, and three at a time at most. A helper cannot start a helper. Every start and every stop goes into an audit log. A session cannot change these limits.</li>
              {LI}<strong>Rules that each session follows.</strong> A session credits finished work only from files on disk, exit codes or the audit log. A helper's own summary is not proof. A session reports every limit that stopped it as a <code>CEILING</code> line. A run that ends without its expected files is a failed run.</li>
            </ul>
            {P}The result is cheaper runs, smaller batches of work, and evidence that a person can check.</p>
          </div>

          {subagents_canvas}
        </section>"""
sub1("        </section>\n      </main>", "        </section>" + panel7 + "\n      </main>")

open(PAGE, "w", encoding="utf-8").write(src)
print("applied")
