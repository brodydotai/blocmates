# blocmates. Show Builder — SKILL

**Trigger:** Use this skill whenever Brody asks to "build the show", "prep the show", "make the show", "generate the show", or drops raw content/notes for an episode.

---

## What This Skill Does

Takes raw content (news links, bullet points, segment ideas, notes, tweets) and generates a fully formatted episode of `blocmates-show-prep.html` — the Display panel slides only, following the brand system defined in `style.md`. Do not generate Notes panel content.

---

## Pre-Flight Checklist

Before writing a single line of HTML, complete ALL of these steps:

1. **Read** `style.md` (in `.skills/`) — internalize every design and copy rule. This is law.
2. **Read** `content-ideas.md` — identify available variable segment ideas.
3. **Review** the content Brody dropped — parse out: news items, tool recommendations, quotes, tweets, topics.
4. **Do web searches** on any topics that need current context or fact-checking.
5. **Select variable segments** — pick 2 from `content-ideas.md` that best complement the week's news. Avoid overlap with High Signal.
6. **Plan the full slide order** before writing HTML (see Show Architecture below).

---

## Show Architecture

Every episode has this exact structure. Never deviate.

```
01  COVER SLIDE          → intro-hero layout
02  INTRODUCTION         → transition-slide (segment intro)
03  [Intro topic 1]      → has-img or no-img
04  [Intro topic 2]      → has-img or no-img  (optional)
05  HIGH SIGNAL          → transition-slide (segment intro)
06  [News item 1]        → has-img or tweet-slide
07  [News item 2]        → has-img or tweet-slide
08  [News item 3]        → has-img (optional)
09  THE TOOL SHED        → transition-slide (segment intro)
10  [Tool/tip 1]         → has-img or no-img
11  [Tool/tip 2]         → has-img (optional)
12  [VARIABLE SEGMENT 1] → transition-slide (segment intro)
13  [VS1 topic 1]        → has-img or no-img
14  [VS1 topic 2]        → has-img (optional)
15  [VARIABLE SEGMENT 2] → transition-slide (segment intro)
16  [VS2 topic 1]        → has-img or no-img
17  [VS2 topic 2]        → has-img (optional)
18  TAP IN               → no-img (with newsletter CTA)
```

Adjust slide count up or down based on content density. A typical episode is 12–18 slides.

---

## Segment-by-Segment Build Rules

### 01 — Cover Slide
- **Slide type:** `intro-hero`
- **Left side:** Show title + episode number (e.g. "episode 02") + preview bullets (one per segment)
- **Episode title:** must be snappy and clickbaity. it should evoke emotion about what the viewer is missing out on or should be thinking about. think curiosity gap, urgency, or bold claims. not generic descriptions.
- **Preview bullets:** one bullet for each segment in the episode, focused on the segment topic (not specifics). if there are 4 segments, there are 4 bullets. if 6, then 6.
- **Right side:** `pfp-triangle` with host PFP at top, guests at bottom-left and bottom-right
  - If real images are not available, render placeholder circles with `background: rgba(237,230,221,0.08)`
  - PFP names in lowercase, role (e.g. "host", "guest") in red uppercase
- **Title format:** `blocmates.<em>.</em>` is the logo — the episode title goes as a subtitle

### 02 — Introduction (Transition)
- **Slide type:** `transition-slide`
- **`d-label`:** `SEGMENT 01`
- **`d-title`:** `introduction.`
- **Subtitle:** 1–2 sentences on who's on the show this week and what they'll be discussing

### 03–04 — Introduction Content Slides
- Cover: who the guests are, their backgrounds, why they're on this week
- Use `no-img` if no headshots/visuals; `has-img` if guest headshots or bio images are available
- 3 to 5 bullets per slide: background facts, current work, why relevant now

### 05 — High Signal (Transition)
- **Slide type:** `transition-slide`
- **`d-label`:** `SEGMENT 02`
- **`d-title`:** `high signal.`
- **Subtitle:** "this week's most important AI and crypto signal events"

### 06–08 — High Signal News Slides
- Each major news story gets its own slide
- **Slide type:** `has-img` (default), `tweet-slide` (if story is tweet-driven), `no-img` (if text-only)
- **`d-badge`:** `HIGH SIGNAL`
- **`d-title`:** Punchy headline for the story (under 6 words)
- **3 to 5 bullets:** what happened, why it matters, what to watch
- Always include image slot — render `.d-img-placeholder` if image not yet loaded
- Do a web search to verify facts and find the most current angle

### 09 — The Tool Shed (Transition)
- **Slide type:** `transition-slide`
- **`d-label`:** `SEGMENT 03`
- **`d-title`:** `the tool shed.`  (also acceptable: `the cheat code.`)
- **Subtitle:** "tools, strategies, and workflows worth adding to your stack"

### 10–11 — The Tool Shed Content Slides
- **Slide type:** `has-img` or `no-img`
- **`d-badge`:** `THE TOOL SHED`
- **`d-title`:** Tool or strategy name
- **3 to 5 bullets:** what it is, how to use it, why it's worth your time
- Do a web search to confirm the tool still exists and get current pricing/features

### 12 — Variable Segment 1 (Transition)
- **Slide type:** `transition-slide`
- **`d-label`:** `SEGMENT 04`
- **`d-title`:** [Segment name from content-ideas.md]
- **Subtitle:** 1–2 sentences framing the discussion

### 13–14 — Variable Segment 1 Content
- Follow the same pattern as High Signal or The Tool Shed depending on segment type
- Do a web search to get the most current take on this topic
- **`d-badge`:** Segment name in ALL CAPS

### 15 — Variable Segment 2 (Transition)
- Same pattern as Variable Segment 1 transition
- **`d-label`:** `SEGMENT 05`

### 16–17 — Variable Segment 2 Content
- Same pattern as Variable Segment 1 content
- **`d-badge`:** Segment name in ALL CAPS

### 18 — Tap In (Conclusion)
- **Slide type:** `no-img`
- **`d-label`:** last segment number (e.g. `SEGMENT 05` or `SEGMENT 06`)
- **`d-title`:** `tap in.`
- **Bullets are strictly limited to:**
  - guest's social handle (e.g. "@oliverhenry")
  - guest's project URL (e.g. "check out projectname.com")
  - blocmates CTA: "subscribe at blocmates.com for the weekly breakdown"
- Do not add episode takeaways or specific recap bullets. keep it clean.

---

## Writing the HTML

### File to Edit
`blocmates-show-prep.html` in the mounted `app/` directory.

**CRITICAL RULES:**
- Never touch any `<style>` blocks
- Never modify the `<script>` at the bottom
- Never change the topbar HTML structure
- Only edit the Display Panel slide content. Do not generate Notes panel content (no sidebar, no `.n-section` blocks, no notes-scroll area)
- Preserve all `id` attributes on panels and sections

### Display Panel Structure

Each slide uses one of the slide type templates:

**has-img slide:**
```html
<div class="d-slide has-img" id="d-[slug]">
  <div class="d-badge">[SEGMENT NAME]</div>
  <div class="d-counter"><em>XX</em> / YY</div>
  <div class="d-content">
    <div class="d-label">[LABEL TEXT]</div>
    <div class="d-title">[Slide Title]<em>.</em></div>
    <div class="d-bullets">
      <div class="d-bullet"><div class="d-bdot"></div>First bullet text here</div>
      <div class="d-bullet"><div class="d-bdot"></div>Second bullet text here</div>
      <div class="d-bullet"><div class="d-bdot"></div>Third bullet text here</div>
    </div>
  </div>
  <div class="d-img-area" onclick="openLightbox(this.querySelector('img'))">
    <img id="disp-[id]" src="" alt="" style="display:none">
    <div class="d-img-placeholder">
      <div class="p-ico">🖼</div>
      <div>[Placeholder label]</div>
      <div class="p-hint">upload in notes mode</div>
    </div>
  </div>
</div>
```

**no-img / transition slide:**
```html
<div class="d-slide no-img transition-slide" id="d-[slug]">
  <div class="d-counter"><em>XX</em> / YY</div>
  <div class="d-content">
    <div class="d-label">[LABEL]</div>
    <div class="d-title">[Segment Title]<em>.</em></div>
    <div class="d-bullets">
      <div class="d-bullet"><div class="d-bdot"></div>Subtitle line 1</div>
    </div>
  </div>
</div>
```

### Slide Counter

Update the total count in ALL `d-counter` elements once you know the final slide count:
`<em>XX</em> / [TOTAL]`

### Dot Navigation

The dot nav at the bottom of the display panel must have one `.dot` per slide:
```html
<div class="dot-nav" id="dotNav">
  <button class="dot active" onclick="goSlide(0)"></button>
  <!-- one per slide -->
</div>
```

The JavaScript `initDisplay()` function handles this automatically if the dot nav is present. Alternatively, manually add dots to match slide count.

---

## Image Handling

- All images live in the `images/` directory in the mounted app folder
- Wipe this directory clean at the start of each new episode
- **Image naming convention:** images are named `image1.png`, `image2.png`, `image3.png`, etc. in chronological slide order (first `has-img` slide gets `image1.png`, second gets `image2.png`, and so on)
- In `has-img` slides, set `<img src="images/image1.png">` (incrementing the number per slide) so Brody knows exactly what to name each image file
- Placeholders use `.d-img-placeholder` with the image filename label (e.g. "image1.png") so it's clear which image goes where
- For tweet embeds, use `<blockquote class="twitter-tweet">` with the tweet URL as a fallback link

---

## Quality Checklist (Run Before Finishing)

- [ ] All segment types are present (Cover, segment transitions, content slides, Tap In)
- [ ] Every slide has a `d-counter` with correct total
- [ ] Every content slide has 3 to 5 bullets (unless transition/intro slide)
- [ ] No bullet exceeds ~15 words
- [ ] All titles are punchy, under 6 words
- [ ] Episode title is snappy and clickbaity (evokes emotion/curiosity)
- [ ] Cover slide has one bullet per segment
- [ ] Tap In slide has only: guest handle, project URL, blocmates CTA
- [ ] Images named image1.png through imageN.png in chronological slide order
- [ ] No inline colors or new CSS variables were introduced
- [ ] The style block was not modified
- [ ] The script block was not modified
- [ ] The topbar episode label is updated (e.g. "genesis — episode 02")
