# Facts for the curriculum business page

Append only. One row per fact: the fact, the file and line that proves it, the date.

| Fact | Proof | Date |
|---|---|---|
| The page has 6 panels that use `:target`. The CourseFactory detail panels `cf-stage-0` to `cf-stage-4`, `cf-checkers` and `cf-gates` sit under panel 3 in the list on the left. | `/Users/rabies/global_experience/automated-curriculum-development-business.html`, the `<aside class="index">` block | 08 Nov 2026 |
| A link to an id inside a panel hides every panel, because only a `section.panel` can be the `:target`. Link only to panel ids. | The `:target` CSS of the page | 08 Nov 2026 |
| A diagram that is not rendered yet is an empty `<div class="canvas" data-diagram="NAME"></div>`. The fallback block between `<!-- diagram-fallback:start -->` and `<!-- diagram-fallback:end -->` draws it in the browser from `diagrams/NAME.mmd`. | `/Users/rabies/global_experience/plans/inline-06Nov2026-svgs.py` | 08 Nov 2026 |
| `inline-06Nov2026-svgs.py` puts each rendered SVG into the page, then rebuilds the fallback block. With no empty placeholder left, it removes the block. Tested on 08 Nov 2026 with all placeholders filled (block removed) and with one left (block kept for that one). | Same file, function `write_fallback` | 08 Nov 2026 |
| The label guard `mermaid-wiki-guard` marks each canvas with `data-wiki-guard`, so a second run of the guard sets up only new diagrams. | The guard script at the end of the page, function `setup` | 08 Nov 2026 |
| `new-feature.sh --done` deletes the local branch with `git branch -D`, not `-d`. | `/Users/rabies/Desktop/Tools/new-feature/scripts/new-feature.sh`, line 394 | 08 Nov 2026 |
| The continuity job renders `wiki.html`, a page separate from `0-HitByABus.html`. | `/Users/rabies/IERHUB/IERHUB.com/_Continuity/bin/sync.sh`, lines 27 and 31 | 08 Nov 2026 |
