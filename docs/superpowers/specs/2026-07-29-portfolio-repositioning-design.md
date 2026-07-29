# Portfolio repositioning: AI & Data Workflow Specialist

Date: 29 JUL 2026
Status: approved design, pending user review of this written spec
Scope: `index.html` (full rebuild of content and CSS), new `diagrams/*.mmd` sources and
rendered SVGs, small copy sync in `llms.txt` and the resume-markdown download payload.
Out of scope: `map.html`, `id-skills.html`, `sitemap.xml` structure, hosting, build tooling.

## Goal

Reposition the portfolio from "educational learning practitioner with a global story" to
"AI & Data Workflow Specialist", modeled on the Alice Labs profile page of Eric Lundberg
(`/Users/rabies/Downloads/Eric Lundberg.md`): value proposition first, four service
pillars, opinionated working principles, biography last. The international teaching and
living history stays, reframed as the origin of the systems judgment. The interactive map
stays in the hero and still opens `map.html`.

## Persona

An independent operator: someone who can work in any condition, any place on earth, with
minimal resources and minimal supervision, and still ship reliable systems. Every section
should reinforce this. The conflict-zone teaching history is the proof, the AI and data
workflow practice is the current expression.

## Confirmed decisions

1. Hero is value-first (Eric Lundberg model), with the global story as differentiator in
   the subhead. The literal heading "A Global Perspective" is retired; the story remains.
2. Work experience becomes two chapters: "AI & data systems" (2025 to present) and
   "Global education & learning design" (2014 to 2026), the latter framed in one line as
   the origin of the systems thinking.
3. Full minimalist visual redesign: brandkit token pass first, then rebuild of the CSS
   with `taste-skill:redesign-skill` and `taste-skill:minimalist-skill`. Layout stays a
   single self-contained file with no build step and no external runtime requests.
4. Motion is subtle and in-page only, guided by `hyperframes-creative` doctrine: CSS-only
   reveals, all behind `prefers-reduced-motion`. No rendered video.
5. The three decision-making frameworks move on-page as diagrams rendered in the same
   fashion as the diagrams in `id-skills.html`. The Miro links are removed.
6. Date convention site-wide: two-digit day when a day exists, three-letter uppercase
   month, four-digit year. Examples: `01 AUG 2026`, `APR 2026 - Present`.

## Page architecture (new section order)

### 1. Hero

- Name, role line "AI & Data Workflow Specialist".
- Value headline in the spirit of "AI automation, agents, and data workflows for real
  operations".
- Subhead: independent operator persona. A decade of teaching and learning design across
  12+ countries, including two active conflict zones, is why these systems survive messy
  reality with minimal resources and supervision.
- Stat chips kept (12+ countries, 2 active conflict zones, Meta & Raytheon, systems
  thinking; drop or merge "Rapid Prototyping" if the chip row crowds the minimalist
  layout).
- Map container kept, still opens `map.html` in a new tab, with a caption tying the map
  to systems thinking (the map is evidence the persona is real, not decoration).
- Calendly button and resume-markdown download kept. The downloaded markdown content is
  rewritten to match the new positioning and date format.
- The Meta "Malicious Actor silo team" sentence moves out of the hero into the background
  chapter.

### 2. What I do (new section, four pillars)

Mirrors the Lundberg "What I do" section, worded for this history:

1. AI automation systems: remove repetitive work, reduce friction, make operations
   reliable.
2. Agent workflows: multi-agent and gated pipelines for research, triage, compliance,
   and structured decision support. Usefulness over hype.
3. Integrations and data logic: APIs, orchestration (n8n, serverless), business logic so
   information moves where it should.
4. Knowledge and process design: RAG, retrieval-grounded checking, structured knowledge.
   This pillar is where instructional design is recast as a present-tense asset:
   curriculum-grade sequencing makes AI systems dependable.

### 3. How I think about the work (new section)

Opinionated principles in first person, Lundberg register, built from the three hills:

1. **Augmented, not artificial.** AI should be rebranded Augmented Intelligence. The
   tool gives people access to larger and more detrimental decisions while feeding the
   Dunning-Kruger effect: high confidence without context. Position: no project ships
   without genuine subject matter expertise in the loop, and work without a domain
   expert available is declined or rescoped until one exists.
2. **Right-size the tool.** The common peer failure: treating AI as one-size-fits-all.
   That is turning off a light bulb with a hammer. Match the tool to the problem; the
   simplest version that solves the real problem wins.
3. **Precision in small things.** The best date format is two-digit day, three-letter
   month, four-digit year (`01 AUG 2026`): unambiguous in any country, sortable by eye,
   readable over bad radios and worse handwriting. The site practices it everywhere.
   Small conventions like this are what make systems trustworthy at scale.

Below the principles, a "How I decide" subsection hosts the three frameworks as diagrams
(see Diagrams). Short lead-in: these were developed teaching in low-resource,
unpredictable environments and are still how AI workflow projects get scoped today.

### 4. Background (two chapters)

Chapter A: **AI & data systems, 2025 to Present**
- GrapevineData.com, Remote, AUG 2026 - Present: AI & Data Workflow Specialist.
- Engage-AI.org, Remote, FEB 2026 - JUL 2026: AI Educational Consultant.
- StructureSense.ai, Remote, JUL 2025 - Present: AI Education & Adoption Consultant,
  keeping the two mermaid.ai pipeline links (RFP discovery, Grants.gov automation).

Chapter B: **Global education & learning design, 2014 to 2026** with a one-line framing
sentence (taught and designed learning on-site in Saudi Arabia, Iraq, and Afghanistan and
remotely at Meta scale; this chapter is where the independence persona was earned).
- Meta (Facebook, Instagram, Threads), Remote, 2024-2025 Learning Solutions Partner and
  2022-2023 Learning Consultant, including leading the Malicious Actor silo team.
- Austin Community College, Remote, 2020-2022: Instructional Designer.
- Raytheon, Kabul, Afghanistan (on-site), 2018-2019: Senior Development Specialist.
- American University of Iraq, Sulaimaniya (on-site), 2016-2018: Digital Media Literacy
  Instructor.
- King Faisal University, Hofuf, Saudi Arabia (on-site), 2014-2016: Academic Skills
  Instructor.
- The commented-out AUI Baghdad entry stays commented out.

Education and certifications stay beside the chapters: MA Education (Digital Media
Learning, University of San Francisco), the three Quality Matters certifications with
existing links, and the Texas electrical apprentice license with its TDLR link.

The current "Specialization" list (international audiences deck and its three bullets)
folds into the How I think section as a compact evidence link beside the diagrams; the
standalone "Specialization & Principles" section is retired.

### 5. Current projects

The three live projects are kept with their existing facts, restyled, each tagged with
the pillar(s) it proves:

- Automation: IERhub.com (APR 2026 - Present): proves agent workflows plus knowledge and
  process design. The existing "Personal Note" about Augmented Intelligence moves out of
  the project card and into How I think (hill 1); the card keeps the operational facts
  (CourseFactory v2, five stages, six checkers, three human gates, retrieval-grounded
  fact-checking, 600,000-700,000 licensee market). "View the Full Pipeline" button to
  `id-skills.html` stays.
- WriteTrace Chrome extension (MAR 2026 - Present): proves integrations and data logic.
  All outcome cards and tech badges keep their facts.
- GovConMaker.com (2024 - Present): proves AI automation systems. Existing architecture
  link stays.
- The commented-out Gate 15 project stays commented out.

### 6. Footer

Unchanged behavior, restyled. Year logic stays.

## Diagrams

Three new Mermaid sources under `diagrams/`, using the user-provided code verbatim
(minor syntax fixes only if the renderer rejects something):

1. `diagrams/decisions-unstructured.mmd`: "Navigating Unstructured and Unpredictable
   Contexts" (blue #100c77 circles, elk layout).
2. `diagrams/decisions-low-resource.mmd`: "Decision Making Framework for Low-Resource
   Conditions" (green #335c3b circles).
3. `diagrams/decisions-minimal-language.mmd`: "Explaining Complex Concepts Using Minimal
   Language and Visuals" (yellow #ffcc00 circles).

Render with the recipe already proven in `plans/archive` work:

```
npx -y @mermaid-js/mermaid-cli -i diagrams/<name>.mmd \
  -o diagrams/rendered/<name>.svg --svgId <name>-svg \
  -b transparent -p diagrams/puppeteer.json
```

(The command needs the sandbox disabled for Puppeteer; this is a known, accepted step.)

Embed on `index.html` as `<img>` referencing `diagrams/rendered/<name>.svg`, wired into
the existing modal zoom (`openModal`) so each opens full screen, matching how
`id-skills.html` presents its pipeline diagrams. No external requests, no Mermaid
runtime in the browser.

Accent colors from the three diagrams (deep blue, deep green, yellow) are input to the
brandkit pass so the diagrams look native to the new visual system.

## Visual system

1. `taste-skill:brandkit` first: type scale, spacing rhythm, restrained palette anchored
   on the existing black/white plus the three diagram accents. Output is a CSS custom
   property token block at the top of the stylesheet.
2. `taste-skill:redesign-skill` plus `taste-skill:minimalist-skill`: rebuild the CSS on
   those tokens. Calmer type hierarchy, sentence-case headings, fewer boxed cards, more
   whitespace, the nested-list resume markup replaced with clean semantic structure.
   Lucide icons kept but thinned. Mobile-first responsive behavior preserved.
3. All copy follows the owner's ai-writing rules: no em dashes anywhere, plain words,
   no AI-tell phrasing.

## Motion

`hyperframes-creative` is used as motion doctrine only: a restrained hero reveal, gentle
map hover, and section fade-ins on scroll, all CSS-only, all disabled under
`prefers-reduced-motion`. No JS animation libraries, no rendered video files.

## Constraints

- Single self-contained `index.html`, no build step, no runtime external requests
  beyond what already exists (Lucide is already vendored/loaded as today; do not add
  new third-party dependencies).
- `map.html` and `id-skills.html` are not modified; links to both must keep working.
- Every factual claim on the page must trace to the current page content or
  `docs/Michael_Mentzer_Hernandez_Background.md`. No invented metrics.
- Date format everywhere: `DD MMM YYYY` / `MMM YYYY`, months as three uppercase letters.

## Verification

- Serve locally via `dev.sh`, check desktop and mobile widths.
- Every link on the page resolves (map.html, id-skills.html, Calendly, mermaid.ai,
  Quality Matters, TDLR, GovConMaker, architecture links).
- Diagrams render crisply, open in the modal, and match the page's visual system.
- Resume markdown download reflects the new positioning.
- `prefers-reduced-motion` disables all animation.
- Copy audit: zero em dashes, date convention applied everywhere, ai-writing rules pass.

## Plan mechanics

- Move the completed `plans/PLAN.md` (id-skills refresh) to
  `plans/archive/PLAN-id-skills-refresh.md` alongside its handoff.
- writing-plans produces a new `plans/PLAN.md` sized to the 50% context waterfall,
  expected three sessions: (1) brandkit tokens plus content restructure and rewrite,
  (2) minimalist CSS rebuild plus diagram render and embed, (3) motion, resume payload,
  llms.txt sync, and full verification.
