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
