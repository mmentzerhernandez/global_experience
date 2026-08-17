#!/bin/zsh
# Verification for plans/PLAN.md, automated-curriculum-development-business.html Business Operations rewrite.
set -u
F=/Users/rabies/global_experience/automated-curriculum-development-business.html
D=/Users/rabies/global_experience/diagrams
fail=0
chk() { if [ "$1" != "$2" ]; then echo "FAIL: $3 (got $1, want $2)"; fail=1; else echo "ok:   $3"; fi }

chk "$(grep -c $'—' "$F")" 0 "no em dash in the page"
chk "$(cat "$D"/op-*.mmd "$D"/operating-loop.mmd | grep -c $'—')" 0 "no em dash in diagram sources"
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
