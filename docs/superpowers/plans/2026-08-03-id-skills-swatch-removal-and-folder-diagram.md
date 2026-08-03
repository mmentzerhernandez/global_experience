# id-skills.html swatch removal and folder-diagram correction

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remove the per-section color swatch system from `/Users/rabies/global_experience/id-skills.html` and correct the IERHUB.com folder diagram in the `#operating-system` panel so the numbering is complete.

**Architecture:** `id-skills.html` is a single self-contained static page, 3673 lines, no build step and no test framework. All CSS lives in one `<style>` block near the top; content lives in a sidebar of `.box` anchors plus a stack of `.panel` sections. The swatch system is one CSS custom property, `--swatch`, set inline on 20 elements and consumed by exactly two rules: the `.box::before` left strip and the `.pill` background. Removing both consumers first, then stripping the now-dead inline declarations, means the page is never in a broken intermediate state. The folder diagram is a pre-rendered Mermaid SVG with absolute coordinates, so its labels and its box geometry must be edited together by hand.

**Tech Stack:** Plain HTML5, hand-written CSS custom properties, inline Mermaid-generated SVG. Verification is `grep` assertions plus a visual check in a browser.

## Global constraints

- Target file, absolute path: `/Users/rabies/global_experience/id-skills.html`. No other file is modified.
- Never emit an em dash, in code, comments, prose, or SVG label text. Use a comma, a colon, or a period.
- Do not reformat or re-indent untouched lines. Every edit is a surgical string replacement so the diff stays readable.
- The repository is at `/Users/rabies/global_experience`, branch `main`. Commit after each task.
- There is no test runner. "Run the test" in this plan means run the exact `grep` or `python3` command given and compare against the stated expected output.

## File structure

Only one file changes. The regions that change, by current line number:

| Region | Lines | Change |
| --- | --- | --- |
| `.box::before` rule | 136 to 144 | Deleted |
| `.box` padding | 120 to 135 | Left padding normalized |
| `.pill` rule | 239 to 249 | Recolored, no `var(--swatch)` |
| Sidebar `.box` anchors | 704 to 761 | `style="--swatch: ..."` stripped |
| `.panel` sections | 764 to 3362 | `style="--swatch: ..."` stripped |
| `.pill` spans | 3152 to 3285 | `style="--swatch: ..."` stripped |
| Diagram prose | 2866 | Folder count corrected |
| Diagram SVG | 2871 | Label text and geometry corrected |

---

### Task 1: Remove the CSS consumers of `--swatch`

Removing the two rules that read `var(--swatch)` is what actually deletes the visual marker system. The inline declarations left behind after this task are inert, and Task 2 removes them.

`.box::before` painted a 5px strip flush against the left edge, and `.box` compensated with an asymmetric `padding-left: 1.25rem` against `1rem` on the right. With the strip gone, that asymmetry reads as a misalignment, so the padding is normalized to `0.9rem 1rem` in the same edit. The `position: relative` and `overflow: hidden` on `.box` stay: `.box-parent .caret` is absolutely positioned against that same box.

`.pill` is not purely decorative. All seven pills carry real text, for example `Per course · Once` and `Decide · Sign-off`, so the element stays and only its color changes. It becomes a neutral outlined chip that inherits the page's ink color, which is legible in every panel without a per-section color.

**Files:**
- Modify: `/Users/rabies/global_experience/id-skills.html:120-144` and `:239-249`

**Interfaces:**
- Consumes: nothing.
- Produces: a stylesheet with zero occurrences of `var(--swatch)`. Task 2 depends on that count being zero before it strips the inline declarations.

- [ ] **Step 1: Write the failing check**

Save this as the verification command for this task. Run it now, before editing:

```bash
grep -c 'var(--swatch)' /Users/rabies/global_experience/id-skills.html
```

Expected right now: `2`

- [ ] **Step 2: Delete the `.box::before` rule and normalize `.box` padding**

Find this exact block (lines 120 to 144) and replace it. Old:

```css
      .box {
        display: block;
        position: relative;
        background: var(--card);
        border: 1px solid rgba(0, 47, 167, 0.12);
        border-radius: var(--radius-md);
        padding: 0.9rem 1rem 0.9rem 1.25rem;
        margin-bottom: 0.6rem;
        overflow: hidden;
        text-decoration: none;
        color: inherit;
        transition:
          transform var(--dur) ease,
          box-shadow var(--dur) ease,
          border-color var(--dur) ease;
      }
      .box::before {
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 5px;
        background: var(--swatch);
      }
```

New:

```css
      .box {
        display: block;
        position: relative;
        background: var(--card);
        border: 1px solid rgba(0, 47, 167, 0.12);
        border-radius: var(--radius-md);
        padding: 0.9rem 1rem;
        margin-bottom: 0.6rem;
        overflow: hidden;
        text-decoration: none;
        color: inherit;
        transition:
          transform var(--dur) ease,
          box-shadow var(--dur) ease,
          border-color var(--dur) ease;
      }
```

- [ ] **Step 3: Recolor the `.pill` rule**

Find this exact block (lines 239 to 249). Old:

```css
      .pill {
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        border-radius: var(--pill);
        padding: 0.3rem 0.85rem;
        color: #fff;
        background: var(--swatch);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.12);
      }
```

New:

```css
      .pill {
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        border-radius: var(--pill);
        padding: 0.3rem 0.85rem;
        color: var(--text-muted);
        background: var(--card-alt);
        border: 1px solid rgba(0, 47, 167, 0.18);
      }
```

Note the `box-shadow` is dropped. It existed to lift a saturated colored chip off the page; on a low-contrast outlined chip it reads as smudge.

- [ ] **Step 4: Run the check**

```bash
grep -c 'var(--swatch)' /Users/rabies/global_experience/id-skills.html
```

Expected: `0`

Then confirm the two variables used in the replacement actually exist, so the pill does not fall back to transparent:

```bash
grep -n -- '--card-alt:\|--text-muted:\|--pill:' /Users/rabies/global_experience/id-skills.html | head
```

Expected: one definition line for each of the three, inside the `:root` block. If `--card-alt` is not defined, substitute the literal `#f5f7fb` and note the substitution in the commit message.

- [ ] **Step 5: Open the page and look at it**

```bash
open /Users/rabies/global_experience/id-skills.html
```

Expected: sidebar boxes are plain bordered cards with no colored left strip and no visible left-padding gap where the strip used to be. The seven pills, visible on the panels reached by the "Stage 0" through "Gates" sidebar links, are readable gray-on-light chips with a thin border. Nothing overlaps and no caret has moved.

- [ ] **Step 6: Commit**

```bash
cd /Users/rabies/global_experience
git add id-skills.html
git commit -m "style(id-skills): drop swatch-driven box strip and pill fill"
```

---

### Task 2: Strip the dead inline `--swatch` declarations

After Task 1 nothing reads `--swatch`, so all 20 inline declarations are dead weight. There are three syntactic shapes, and the third is the one that breaks a careless edit: three sidebar anchors carry `style="--swatch: #...;"` as the element's only attribute besides `class` and `href`, and the `style` attribute must be removed whole rather than emptied. Emptying it would leave `style=""`, which is valid but is exactly the kind of residue this task exists to prevent.

The other seventeen are the same shape: `style="--swatch: #xxxxxx"` on `<section class="panel">` and on `<span class="pill">`. Every one of those elements also has an `id` or a `class` doing real work, so only the `style` attribute goes.

**Files:**
- Modify: `/Users/rabies/global_experience/id-skills.html`, 20 sites between lines 704 and 3362

**Interfaces:**
- Consumes: from Task 1, the guarantee that no CSS rule reads `var(--swatch)`.
- Produces: a file where `grep -c 'swatch' id-skills.html` returns 0. Task 3 assumes the file is otherwise unchanged.

- [ ] **Step 1: Enumerate the exact sites**

```bash
grep -n 'swatch' /Users/rabies/global_experience/id-skills.html
```

Expected: 20 lines, at 704, 708, 711, 719, 725, 729, 733, 737, 741, 745, 749, 754, 758, 764, 2857, 3037, 3112, 3149, 3152, 3168, 3171, 3187, 3190, 3206, 3209, 3225, 3228, 3244, 3247, 3282, 3285, 3305, 3362. If the count or the line numbers differ from this list, stop and report: it means the file drifted since the plan was written, and blind editing would be unsafe.

- [ ] **Step 2: Remove the attributes**

The declarations are uniform enough for one pass. Use a single Python rewrite rather than 20 hand edits, because 20 hand edits on near-identical strings is where transposition errors live:

```bash
cd /Users/rabies/global_experience
python3 - <<'EOF'
import re
p = "id-skills.html"
s = open(p, encoding="utf-8").read()
before = s.count("swatch")
# Attribute is the element's only style attr in every case, so remove it whole,
# including the leading whitespace that separated it from the previous attribute.
s2 = re.sub(r'\s*style="--swatch:\s*#[0-9a-fA-F]{3,6};?"', '', s)
open(p, "w", encoding="utf-8").write(s2)
print("removed", before - s2.count("swatch"), "of", before)
EOF
```

Expected output: `removed 20 of 20`

- [ ] **Step 3: Verify nothing else moved**

```bash
cd /Users/rabies/global_experience
grep -c 'swatch' id-skills.html; grep -c 'style=""' id-skills.html; git diff --stat
```

Expected: `0`, then `0`, then a diff touching only `id-skills.html` with roughly 20 changed lines and no change to the total line count.

- [ ] **Step 4: Spot-check three representative sites**

```bash
cd /Users/rabies/global_experience
sed -n '704p;2857p;3152p' id-skills.html
```

Expected: line 704 is an `<a class="box" href="#business-overview"` with no `style`, line 2857 is `<section class="panel" id="operating-system">`, and the pill line is `<span class="pill">Per course · Once</span>` with its text intact. If a pill lost its text, revert with `git checkout id-skills.html` and redo Step 2 with a narrower pattern.

- [ ] **Step 5: Reload and look at the page**

```bash
open /Users/rabies/global_experience/id-skills.html
```

Expected: identical to the end of Task 1. Panels still switch when sidebar links are clicked, which confirms the `id` attributes survived, since panel switching is `:target` based and an id loss would break it silently.

- [ ] **Step 6: Commit**

```bash
cd /Users/rabies/global_experience
git add id-skills.html
git commit -m "style(id-skills): strip dead inline --swatch declarations"
```

---

### Task 3: Correct the IERHUB.com folder diagram

The diagram in the `#operating-system` panel lists ten numbered folders and skips 8. On disk, `/Users/rabies/Desktop/IERHUB.com` has eleven numbered workstream folders: `1-AboutTheBusiness`, `2-AdsAnalytics`, `3-BusinessTools`, `4-Compliance`, `5-CurriculumDevelopment`, `6-FrontEndBackendIERhub.com`, `7-SocialMedia`, `8-Legal`, `9-DesignFigma`, `10-Plans`, `11-Research`. So one line is added, `8 · Legal`, and the surrounding prose that says "Ten numbered folders" becomes "Eleven".

The SVG is Mermaid output with hardcoded coordinates, so adding a label line is not enough: the blue box must grow by one line height or the eleventh entry renders outside its own border. One line at the diagram's 16px font and 1.5 line-height is 24px. The box grows downward only, keeping its top edge at y=112 where the incoming arrow already lands, so only the outgoing arrow to the orange box needs a new path. The numbers below are precomputed from the current geometry: rect `y=-183 height=366` centered at `translate(138, 295)`, giving a top of 112 and a bottom of 478.

New geometry: height 390, `y=-195`, center `translate(138, 307)`, top still 112, bottom now 502. The label group and its foreignObject grow to match. The overall `viewBox` height of 686 does not change, because the orange box already ends at y=678 and the blue box's new bottom of 502 is well clear of it.

**Files:**
- Modify: `/Users/rabies/global_experience/id-skills.html:2866` (prose) and `:2871` (the `#op-folders-svg` element)

**Interfaces:**
- Consumes: from Task 2, a file with no `swatch` occurrences. Note that after Task 2 removed the `style` attribute from line 2857, the line numbers in this task are still valid, because that edit changed a line rather than adding or deleting one.
- Produces: nothing downstream.

- [ ] **Step 1: Write the failing check**

```bash
grep -c '8 · Legal' /Users/rabies/global_experience/id-skills.html
```

Expected right now: `0`

- [ ] **Step 2: Fix the prose count**

Replace on line 2866:

Old: `Ten numbered folders, one per workstream.`

New: `Eleven numbered folders, one per workstream.`

- [ ] **Step 3: Add the missing folder to the label**

Inside the SVG, find this exact substring and replace it:

Old:

```
7 · Social media<br />9 · Design<br />
```

New:

```
7 · Social media<br />8 · Legal<br />9 · Design<br />
```

- [ ] **Step 4: Grow the blue box to fit eleven lines**

Three coordinate edits, all inside the `<g class="node default access" id="op-folders-svg-flowchart-NUM-1" ...>` element. Make them in this order.

First the node transform. Old: `data-look="classic" transform="translate(138, 295)"`. New: `data-look="classic" transform="translate(138, 307)"`.

Then the rect. Old: `x="-130" y="-183" width="260" height="366"`. New: `x="-130" y="-195" width="260" height="390"`.

Then the label group and its foreignObject. Old:

```
<g class="label" style="color:#000000 !important" transform="translate(-100, -168)"><rect/><foreignObject width="200" height="336">
```

New:

```
<g class="label" style="color:#000000 !important" transform="translate(-100, -180)"><rect/><foreignObject width="200" height="360">
```

Only one `translate(-100, -168)` and one `height="336"` exist in the file, so these substrings are unambiguous. The `translate(138, 295)` is likewise unique; the sibling red box uses `translate(448, 295)`.

- [ ] **Step 5: Reroute the arrow leaving the blue box**

The edge `L_NUM_ZERO_0` starts at the blue box's old bottom edge, y=478, which is now 24px inside the box. Find the path with `id="op-folders-svg-L_NUM_ZERO_0"` and replace its `d` attribute.

Old:

```
d="M138,478L138,482.167C138,486.333,138,494.667,143.898,502.639C149.796,510.61,161.593,518.221,167.491,522.026L173.389,525.831"
```

New:

```
d="M138,502L138,506C138,512,138,518,145.5,522C153,526,166,527,173.389,527.5"
```

This is a hand-fitted curve, not Mermaid output: it leaves the new bottom edge at y=502 and arrives at the orange box's top-left entry point near (176.75, 528), the same target the original path used. Leave the `data-points` attribute alone; it is base64 metadata that Mermaid writes and nothing at render time reads.

- [ ] **Step 6: Verify the edits landed**

```bash
cd /Users/rabies/global_experience
grep -c '8 · Legal' id-skills.html
grep -c 'Eleven numbered folders' id-skills.html
grep -c 'height="390"' id-skills.html
grep -c 'M138,502' id-skills.html
grep -c 'M138,478' id-skills.html
```

Expected, in order: `1`, `1`, `1`, `1`, `0`.

- [ ] **Step 7: Look at the diagram**

```bash
open /Users/rabies/global_experience/id-skills.html
```

Click the "2 - Business Operations" sidebar link. Expected: the blue box lists 1 through 11 with no gaps, all eleven lines sit inside the blue border with even padding top and bottom, the arrow from the gray "IERHUB.com" box still meets the blue box's top edge, and the arrow from the blue box to the orange box starts at the blue box's bottom border rather than from inside it. The orange box has not moved and nothing is clipped at the bottom of the canvas.

- [ ] **Step 8: Commit**

```bash
cd /Users/rabies/global_experience
git add id-skills.html
git commit -m "content(id-skills): add missing folder 8 to IERHUB folder diagram"
```

---

## Open questions for the owner

Neither of these blocks the three tasks above. Both are discrepancies found while reading the real directory, and both are content decisions rather than bugs.

1. `000-Dashboard` exists on disk and is absent from the diagram. It was left out of this plan because the blue box is captioned "one workstream each" and a dashboard is not a workstream. If it should appear, it is one more line and the geometry deltas in Task 3 double: height 414, `y=-207`, node `translate(138, 319)`, label `translate(-100, -192)`, foreignObject height 384, and the outgoing arrow starts at y=526.

2. The red box lists four underscore folders, `_Admin · _Continuity · _Credentials · _Archive`, but only `_Admin` and `_Continuity` exist on disk. Either the diagram is aspirational or two folders were removed. Worth resolving before anyone treats the diagram as a map.
