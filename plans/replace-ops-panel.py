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
