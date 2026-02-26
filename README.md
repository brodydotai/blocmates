# Blocmates Show Prep

`Blocmates Show Prep` is a static, single-page web app for preparing and presenting episode content.

The current build lives in `app/blocmates-show-prep.html` and includes two modes:
- **Notes mode** for prep and editing
- **Display mode** for fullscreen slide-style presentation

## What the app does

- Organizes content into show sections (intro, events, cheat code, stack, overrated/underrated, wrap-up).
- Toggles between prep workflow and presenter display.
- Includes a built-in episode timer.
- Supports drag-and-drop section reordering.
- Lets you upload images into sections for visual support.
- Supports optional links per content item.
- Provides keyboard navigation in display mode.

## Tech stack

- Plain `HTML`, `CSS`, and `JavaScript` (no framework, no build step).
- Client-side only; no backend required.

## Run locally

### Option 1: Open directly

Open this file in a browser:

`app/blocmates-show-prep.html`

### Option 2: Serve over a local web server (recommended)

From the repo root:

```bash
python3 -m http.server 8000
```

Then open:

`http://localhost:8000/app/blocmates-show-prep.html`

## Hosting

Because this is a static app, you can host it on any static hosting provider.

### GitHub Pages

1. Push your code to GitHub (already done for this repo).
2. In GitHub, go to **Settings -> Pages**.
3. Under **Build and deployment**:
   - **Source**: `Deploy from a branch`
   - **Branch**: `main` and `/ (root)`
4. Save, then wait for deployment.
5. Your app URL will be:
   - `https://brodydotai.github.io/blocmates/app/blocmates-show-prep.html`

### Other static hosts (Netlify, Vercel, Cloudflare Pages)

- Point the project to this repository.
- Build command: _none_
- Publish directory: repo root
- App path after deploy: `/app/blocmates-show-prep.html`

## Notes

- Images currently in `genesis/images` are included in the repository.
- If you want a cleaner public URL (without `/app/blocmates-show-prep.html`), move/rename the app file to `index.html` at the repo root.
