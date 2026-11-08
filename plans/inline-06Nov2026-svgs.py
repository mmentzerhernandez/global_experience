#!/usr/bin/env python3
"""Inline rendered diagrams into their data-diagram placeholders, then rebuild the browser fallback.

Usage:
  inline-06Nov2026-svgs.py              inline every rendered SVG that exists, then rebuild the fallback
  inline-06Nov2026-svgs.py --fallback   rebuild the fallback only

The fallback is a script block at the end of the page. The Mermaid script tag carries an SRI hash
that matches the hash jsDelivr publishes for mermaid@11.4.1. "antiscript" keeps the click links
and removes script tags from labels. It draws each placeholder that has no
rendered SVG yet, in the browser, from its .mmd source. When no placeholder remains, the block
is removed, so the page loads no Mermaid library.
"""
import json, os, re, sys
PAGE = "/Users/rabies/global_experience/automated-curriculum-development-business.html"
DIAG = "/Users/rabies/global_experience/diagrams"
REND = DIAG + "/rendered"
NAMES = ["business-overview", "session-pipeline", "dwell-gate", "plan-run", "operating-loop", "op-records"]
START, END = "<!-- diagram-fallback:start -->", "<!-- diagram-fallback:end -->"
FALLBACK_JS = """<script src="https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.min.js" integrity="sha384-rbtjAdnIQE/aQJGEgXrVUlMibdfTSa4PQju4HDhN3sR2PmaKFzhEafuePsl9H/9I" crossorigin="anonymous"></script>
    <script id="diagram-fallback-src" type="application/json">%s</script>
    <script>
      /* Draw each diagram that is not rendered into the page yet, then run the label guard again.
         The guard marks each canvas it sets up, so a second run sets up only the new diagrams. */
      (async function () {
        var src = JSON.parse(document.getElementById("diagram-fallback-src").textContent);
        mermaid.initialize({ startOnLoad: false, securityLevel: "antiscript", flowchart: { htmlLabels: true } });
        for (var name in src) {
          var hole = document.querySelector('.canvas[data-diagram="' + name + '"]');
          if (!hole) continue;
          try { hole.innerHTML = (await mermaid.render(name + "-svg", src[name])).svg; }
          catch (e) { hole.textContent = "Diagram " + name + " did not render: " + e.message; }
        }
        var guard = Array.prototype.find.call(document.scripts, function (el) {
          return el.textContent.indexOf("mermaid-wiki-guard v1") !== -1;
        });
        if (guard) { window.__mermaidWikiGuard = undefined; new Function(guard.textContent)(); }
      })();
    </script>"""

def write_fallback(src):
    src = re.sub(re.escape(START) + r"[\s\S]*?" + re.escape(END) + r"\n?\s*", "", src)
    holes = re.findall(r'<div class="canvas" data-diagram="([^"]+)"></div>', src)
    if not holes:
        print("fallback: none needed, block removed")
        return src
    code = {n: open(f"{DIAG}/{n}.mmd", encoding="utf-8").read() for n in holes}
    data = json.dumps(code).replace("</", "<\\/")
    block = START + "\n    " + (FALLBACK_JS % data) + "\n    " + END + "\n  "
    i = src.rindex("</body>")
    print("fallback: browser draws", ", ".join(holes))
    return src[:i] + block + src[i:]

src = open(PAGE, encoding="utf-8").read()
if "--fallback" not in sys.argv:
    for n in NAMES:
        path = f"{REND}/{n}.svg"
        hole = f'<div class="canvas" data-diagram="{n}"></div>'
        if hole not in src:
            continue
        if not os.path.exists(path):
            print(f"skip {n}: no rendered SVG")
            continue
        svg = open(path, encoding="utf-8").read().strip()
        if not svg.startswith("<svg"):
            sys.exit(f"{n}: file does not start with <svg")
        if f'id="{n}-svg"' not in svg[:400]:
            sys.exit(f"{n}: root id missing")
        # Match the page convention on the ROOT tag only: width 100%, keep viewBox.
        head, rest = svg.split(">", 1)
        head = re.sub(r'\swidth="[^"]*"', ' width="100%"', head, count=1)
        if ' width="100%"' not in head:
            head += ' width="100%"'
        if "background-color: transparent" not in head:
            print(f"WARN {n}: root style lacks background-color: transparent, check -b flag")
        if src.count(hole) != 1:
            sys.exit(f"{n}: expected exactly one placeholder, found {src.count(hole)}")
        src = src.replace(hole, '<div class="canvas">\n            ' + head + ">" + rest + "\n          </div>")
        print("inlined", n)
src = write_fallback(src)
open(PAGE, "w", encoding="utf-8").write(src)
