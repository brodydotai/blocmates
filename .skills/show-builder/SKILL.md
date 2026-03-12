# blocmates. Show Builder — SKILL

**Trigger:** Use this skill whenever Brody asks to "build the show", "prep the show", "make the show", "generate the show", or drops raw content/notes for an episode.

---

## What This Skill Does

Takes raw content (news links, bullet points, segment ideas, notes, tweets) and generates a fully formatted episode of `blocmates-show-prep.html` — a complete show prep document with both Notes mode and Display mode populated, following the brand system defined in `show-style-guide.md`.

---

## Pre-Flight Checklist

Before writing a single line of HTML, complete ALL of these steps:

1. **Read** `show-style-guide.md` — internalize every rule. This is law.
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
- **Left side:** Show title + episode number (e.g. "episode 02") + 3 preview bullets summarizing the episode
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
- 3 bullets per slide: background facts, current work, why relevant now

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
- **3 bullets:** What happened → Why it matters → What to watch
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
- **3 bullets:** What it is → How to use it → Why it's worth your time
- In Notes mode: use `.try-box` with `.try-chip` items for the "try this" recommendation
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
- **`d-label`:** `SEGMENT 06`
- **`d-title`:** `tap in.`
- **3 bullets:** 2 episode takeaways + 1 newsletter CTA
- **Newsletter CTA bullet must always say:** "subscribe at blocmates.com for the weekly breakdown"
- Warm, direct tone — lowercase, conversational sign-off

---

## Writing the HTML

### File to Edit
`blocmates-show-prep.html` in the mounted `app/` directory.

**CRITICAL RULES:**
- Never touch any `<style>` blocks
- Never modify the `<script>` at the bottom
- Never change the topbar HTML structure
- Only edit the Notes Panel content sections and Display Panel slide content
- Preserve all `id` attributes on panels and sections
- Keep the sidebar navigation in sync with actual segments

### Notes Panel Structure

Each segment is a `.n-section` block:

```html
<div class="n-section" id="n-[segment-slug]" draggable="true" ...>
  <div class="n-sec-head">
    <span class="drag-handle">⠿</span>
    <span class="n-sec-num">01</span>
    <span class="n-sec-title">[segment name]</span>
    <div class="n-sec-line"></div>
    <span class="n-sec-time">~XX min</span>
  </div>
  <!-- content blocks inside -->
</div>
```

Editable text fields use `contenteditable="true"`:
```html
<div class="n-editable" contenteditable="true">[text]</div>
```

Cards for news items:
```html
<div class="n-card">
  <div class="n-card-title">
    Story Title
    <span class="tag ts">story</span>
  </div>
  <div class="n-editable" contenteditable="true">Notes about this story...</div>
  <div class="n-img-slot" id="slot-[id]">
    <label class="n-upload-label" for="img-[id]">
      <span class="ico">🖼</span>
      <span>drop image or click to upload</span>
      <span class="hint">png · jpg · gif</span>
    </label>
    <input type="file" id="img-[id]" accept="image/*" onchange="loadImg('slot-[id]','disp-[id]',this)">
  </div>
</div>
```

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

### Sidebar Navigation

Keep the sidebar nav in sync with your segment list:
```html
<div class="nav-it active" data-s="n-intro" onclick="navTo('n-intro',this)">
  <span class="nav-n">01</span>introduction
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

- All images live in the `/genesis/` directory in the mounted app folder
- Wipe this directory clean at the start of each new episode
- Image slots in Notes mode use `loadImg()` to load base64 in-memory — no files are referenced by path
- Placeholders in Display mode use `.d-img-placeholder` — they're replaced when user uploads in Notes mode
- For tweet embeds, use `<blockquote class="twitter-tweet">` with the tweet URL as a fallback link

---

## Quality Checklist (Run Before Finishing)

- [ ] All 6 fixed segment types are present (Cover, Intro, High Signal, The Tool Shed, Var1, Var2, Tap In)
- [ ] Every slide has a `d-counter` with correct total
- [ ] Every content slide has exactly 3 bullets (unless transition/intro slide)
- [ ] No bullet exceeds ~15 words
- [ ] All titles are punchy, under 6 words
- [ ] The newsletter CTA is on the Tap In slide
- [ ] Sidebar nav items match actual segment sections
- [ ] No inline colors or new CSS variables were introduced
- [ ] All `loadImg()` IDs are unique and matched between Notes and Display panels
- [ ] The style block was not modified
- [ ] The script block was not modified
- [ ] `genesis/` directory is clean (previous show images wiped)
- [ ] The topbar episode label is updated (e.g. "genesis — episode 02")
