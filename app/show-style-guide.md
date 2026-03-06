# blocmates. — Show Style Guide

This document defines the complete design system for the blocmates AI weekly show prep tool (`blocmates-show-prep.html`). Any generated show content **must stay strictly within these parameters**. Never introduce new colors, fonts, layout patterns, or component types that are not described here.

---

## Brand Signature

- The logo is always written in lowercase: `blocmates.`
- The **period at the end** is always colored `--red` (`#aa4946`). This is a core brand mark. Never omit it.
- In HTML: `<div class="logo">blocmates<em>.</em></div>` where `.logo em { color: var(--red); }`

---

## Color Palette

All colors are CSS variables defined on `:root`. Use **only** these values. Do not use hex codes directly in content HTML — reference the CSS variables.

| Variable     | Hex       | Usage                                             |
|--------------|-----------|---------------------------------------------------|
| `--black`    | `#1f1f1f` | Body background, topbar                          |
| `--navy`     | `#253f58` | Active mode button, subtle accents               |
| `--red`      | `#aa4946` | Primary accent: logo period, nav active state, bullet dots, labels, numbers, badge overlays |
| `--gold`     | `#e6a93e` | Tips / tools accent, `try` boxes, gold-themed tags |
| `--sage`     | `#80a76a` | Positive / underrated accent, sage-themed tags   |
| `--cream`    | `#ede6dd` | Primary text, all body copy                      |
| `--charcoal` | `#444342` | Subtle backgrounds, dividers (used sparingly)    |

### Opacity Conventions
Text and borders are frequently semitransparent versions of `--cream`. Common values:
- `rgba(237,230,221, 0.72)` — body bullets in display
- `rgba(237,230,221, 0.60)` — secondary notes text
- `rgba(237,230,221, 0.38)` — muted sidebar items
- `rgba(237,230,221, 0.28)` — very muted (ep label)
- `rgba(237,230,221, 0.18)` — placeholder text, subtle labels
- `rgba(237,230,221, 0.08)` — faint divider borders
- `rgba(237,230,221, 0.06)` — background fills, section borders

---

## Typography

**Font:** `Space Grotesk` (Google Fonts) — weights: 400, 500, 600, 700. No other fonts are used.

### Notes Mode Text Scale
| Element           | Size  | Weight | Notes                              |
|-------------------|-------|--------|------------------------------------|
| Section title     | 18px  | 700    | `.n-sec-title`                     |
| Section number    | 11px  | 700    | Red, `.n-sec-num`                  |
| Block label       | 10px  | 700    | Uppercase, 1px letter-spacing      |
| Editable text     | 14px  | 400    | Cream at 60%, `.n-editable`        |
| Card title        | 14px  | 700    | `.n-card-title`                    |
| Tags              | 10px  | 700    | Uppercase, `.tag`                  |
| Sidebar nav items | 13px  | 500    | `.nav-it`                          |
| Sidebar labels    | 10px  | 700    | Uppercase, 1.5px letter-spacing    |

### Display Mode Text Scale
| Element         | Size  | Weight | Notes                                         |
|-----------------|-------|--------|-----------------------------------------------|
| Label           | 11px  | 700    | Uppercase, 2px letter-spacing, red            |
| Title (has-img) | 44px  | 700    | -1.5px letter-spacing, 1.05 line-height       |
| Title (no-img)  | 56px  | 700    | Larger on full-screen slides                  |
| Bullet text     | 17px  | 400    | Cream at 72%, 1.55 line-height (has-img)      |
| Bullet text     | 20px  | 400    | Larger on no-img slides                       |
| Slide counter   | 13px  | 700    | Top-right, cream at 25%; red number           |
| Section badge   | 10px  | 700    | Top-left, uppercase, 2px letter-spacing       |
| Stack names     | 20px  | 700    | `.d-stack-name`                               |
| Stack roles     | 11px  | 700    | Uppercase, red, `.d-stack-role`               |

---

## Layout System

### App Shell
- **Topbar:** fixed height, `padding: 11px 22px`, dark background, cream border-bottom at 8% opacity
- **Main area:** `display:flex; flex:1; overflow:hidden`
- Two modes: **Notes** (`#notesPanel`) and **Display** (`#displayPanel`)
- Mode is toggled with `.mode-btn` buttons; active state uses `--navy` background

### Notes Mode Layout
- **Sidebar** (220px, fixed): section nav with red left-border on active item
- **Notes scroll area:** `padding: 36px 44px`, scrollable
- Sections are `.n-section` cards: `border-radius:12px`, dark border, hover state brightens border

### Display Mode Layout
- `overflow-y: scroll; scroll-snap-type: y mandatory` — full snap scrolling
- Each slide: `height: 100vh; scroll-snap-align: start`
- Dot navigation: fixed right side, red active dot
- Arrow key navigation supported

---

## Slide Types (Display Mode)

### 1. `has-img` — Content + Image
Split grid: `grid-template-rows: 44vh 56vh`
- **Top 44vh:** `.d-content` — label, title, bullets
- **Bottom 56vh:** `.d-img-area` — image with rounded container (`border-radius: 22px`, margin `14px 20px 22px`)
- Content padding: `28px 72px`

**Use for:** Any segment topic that has a visual (chart, tweet, screenshot, graph)

### 2. `no-img` — Full Viewport Text
Single row: `grid-template-rows: 1fr`
- Full page `.d-content` with `padding: 60px 100px`
- Title is larger (56px)
- Bullet text is larger (20px)

**Use for:** Transition slides (segment start), Tap In / conclusion, segment intros without visuals

### 3. `intro-hero` — Cover Slide
Two-column: `grid-template-columns: 56% 44%`
- Left: `.d-content` with title, show tagline, 3 high-level bullets — `padding: 70px 60px 60px 92px`
- Right: `.d-intro-right` with `.pfp-triangle` — host at top center, guests at bottom-left and bottom-right
- PFP cards: 224px circular images, name in lowercase, role in red uppercase

**Use for:** Episode 1 — Cover slide only

### 4. `transition-slide` — Segment Intro
Full-width `.d-content`: `padding: 28px 72px`
- Large title naming the segment
- Short subtitle (1 sentence) previewing what's about to be covered
- No image area

**Use for:** The first slide of every segment (Introduction, High Signal, The Tool Shed, variable segments, Tap In)

### 5. `tweet-slide` — Twitter/X Embed
Full content area: `padding: 60px 100px`
- `.d-twitter-grid` with one or more `.tweet-wrap` containing `<blockquote class="twitter-tweet">`
- Single tweet: centered, max-width 540px
- Multiple tweets: flex-wrap grid

**Use for:** Any segment item that references a tweet/X post

### 6. `image-only` — Full Screen Image
Centered image with generous padding
- `.d-img-area` fills most of the viewport
- No text overlay

**Use for:** Charts, screenshots, or visuals that need maximum real estate

---

## Components

### Bullet List
```html
<div class="d-bullets">
  <div class="d-bullet"><div class="d-bdot"></div>Bullet text here</div>
  <div class="d-bullet"><div class="d-bdot"></div>Bullet text here</div>
  <div class="d-bullet"><div class="d-bdot"></div>Bullet text here</div>
</div>
```
- Always exactly **3 bullets** per content slide (unless the slide type explicitly requires otherwise)
- Bullet dots: 7px circle, `--red`
- Text: cream at 72%

### Section Label + Title
```html
<div class="d-label">SEGMENT NAME</div>
<div class="d-title">Main Slide Title<em>.</em></div>
```
- Label: red, uppercase, 2px letter-spacing
- Title: large, bold, `letter-spacing: -1.5px`
- The `<em>` red period can be used at the end of titles for brand consistency (optional but encouraged)

### Slide Counter
```html
<div class="d-counter"><em>03</em> / 09</div>
```
- Always present on each display slide
- Current slide number in red `<em>`, total in cream at 25%

### Section Badge
```html
<div class="d-badge">HIGH SIGNAL</div>
```
- Top-left corner, uppercase, red at 30% — identifies which segment this slide belongs to

### Tags (Notes Mode)
Three tag types:
- `.tag.ts` — red, story/news tag
- `.tag.tt` — sage, tool/tip tag
- `.tag.tw` — gold, warning/watch tag

### Or/Underrated Boxes (Notes Mode)
- `.or-box.ov` — red-tinted, for "Overrated" items
- `.or-box.un` — sage-tinted, for "Underrated" items

### Try Box
```html
<div class="try-box">
  <div class="try-title">try this week</div>
  <div class="try-chips">
    <div class="try-chip">Tool Name</div>
  </div>
</div>
```
Gold-accented, used for The Tool Shed actionable recommendations

### Image Slot (Notes Mode)
```html
<div class="n-img-slot" id="slot-X">
  <label class="n-upload-label" for="img-X">
    <span class="ico">🖼</span>
    <span>drop image or click to upload</span>
    <span class="hint">png · jpg · gif</span>
  </label>
  <input type="file" id="img-X" accept="image/*" onchange="loadImg('slot-X','disp-X',this)">
</div>
```
- Each Notes slot is synced to a Display `<img>` with matching IDs via `loadImg()`
- Slot IDs follow pattern: `slot-[segment]-[number]` (e.g. `slot-hs-1`, `slot-tt-1`)

---

## Segment Structure

### Fixed Segments (Every Show)
Every show always contains these segments in this order:

| #  | Segment Name     | Notes Label         | Approx Time |
|----|------------------|---------------------|-------------|
| 01 | Introduction     | introduction        | ~15 min     |
| 02 | High Signal      | signal events       | ~15 min     |
| 03 | The Tool Shed    | the cheat code      | ~10 min     |
| —  | [Variable 1]     | [from content-ideas]| ~10 min     |
| —  | [Variable 2]     | [from content-ideas]| ~10 min     |
| 06 | Tap In           | wrap up             | ~5 min      |

### Variable Segments
- Positions 4 and 5 rotate weekly
- Pull from `content-ideas.md` in this directory
- Can be supplemented with web search for current, timely angles
- Variable segments follow the same slide composition rules as fixed segments

---

## Slide Composition Rules

### Cover / Intro Slide
- Slide type: `intro-hero`
- Left side: show title + episode number + 3 high-level preview bullets of the episode
- Right side: `pfp-triangle` with host at top, guests at bottom-left and bottom-right
- PFP images: circular, 224px, with name in lowercase and role in red uppercase
- If guest images aren't available, show placeholder circles

### Segment Start Slides
- Slide type: `transition-slide` or `no-img`
- Required fields: `d-badge` (segment name), `d-label` (e.g. "SEGMENT 02"), `d-title` (segment display name)
- Add 1–2 sentence subtitle under the title describing what's about to be covered
- No bullets, no image

### Topic/Event Slides
- Slide type: `has-img` (if visual available) or `no-img` (if text-only)
- Required: `d-badge`, `d-counter`, `d-label`, `d-title`, exactly 3 bullets
- Always include image slot — even if image isn't available yet, render `.d-img-placeholder`
- Bullets must be succinct: max 12–15 words each, declarative statements, no filler

### Concluding / Tap In Slide
- Slide type: `no-img`
- Must include a newsletter CTA: "subscribe at blocmates.com" or equivalent
- Recap: 2–3 bullets on key takeaways
- Sign-off tone: warm, direct, lowercase

---

## Writing Voice & Copy Rules

- **Lowercase everywhere** unless it's an acronym (AI, NFT, ETH) or a proper name (Anthropic, OpenAI)
- **No jargon** — write for someone smart but not crypto-native
- **Bullets are declarative facts**, not questions or hype
- **Titles are punchy** — short, noun-led, under 6 words when possible
- **Red period** at end of titles is optional but encouraged for brand consistency
- Segment badges use ALL CAPS (e.g. `HIGH SIGNAL`, `TIPS & TRICKS`, `TAP IN`)

---

## What Not to Do

- Do not add new CSS variables or inline colors
- Do not use any font other than Space Grotesk
- Do not change the scroll-snap behavior or slide height
- Do not use more than 3 bullets on a content slide
- Do not use all-caps in body text (only labels, badges, tags)
- Do not remove the red period from the logo
- Do not add slides that don't match one of the 6 slide types above
- Do not alter the `has-img` grid split (44vh / 56vh)
- Do not write bullets longer than ~15 words
- Do not introduce layout columns not present in the existing system
