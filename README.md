# Miss Y's Reading and Math Education

Practice games for K–4 reading and math intervention. Every math game gives **corrective feedback**: when a student makes a mistake, the game shows a visual model (ten-frame, place-value chart, base-ten blocks, or five-frame) and walks the student to the correct answer before moving on.

Live site: https://collingeorge.github.io/math-practice-games/

There is no build step, no framework, and no runtime dependencies. Each game is a single self-contained HTML file with inline CSS and JavaScript.

## Site structure

| File | Purpose |
|---|---|
| `index.html` | Home page with the greeting and the **Reading Games** / **Math Games** buttons |
| `math.html` | Math games grouped by level (grade) with skill filters |
| `reading.html` | Reading games grouped by level (games coming soon) |
| `site.css` | Shared styles for the three pages above |
| `filters.js` | Skill filter buttons on the Math page |
| `games/*.html` | The games (each links back to the Math page) |

## Math games

| Level | File | Skill | Rounds | Corrective feedback |
|---|---|---|---|---|
| 1 (K) | `games/count-to-10.html` | Count objects 1–10, match to numeral | 30 | Counts each object aloud with number badges |
| 1 (K–1) | `games/ten-frame-subitizing.html` | Subitize 1–10 on a ten-frame | 30 | Uses "full row is 5" and empty boxes |
| 1 (K–1) | `games/make-5-number-bonds.html` | Missing part of 5 + addition/subtraction sentences | 20 | Five-frame, known part blue, missing part orange |
| 2 (K–1) | `games/count-to-20.html` | Count 1–20 in two ten-frames | 40 | Full frame = 10, then count on |
| 2 (1) | `games/make-10-number-bonds.html` | Missing part of 10 + addition/subtraction sentences | 30 | Ten-frame, known part blue, missing part orange |
| 2 (1–2) | `games/numbers-to-120.html` | Write numbers, read base-ten blocks, sequence, place value to 120 | 30 | Place-value chart with blocks; catches "10012" for 112 |
| 3 (2–3) | `games/count-by-10s-and-100s.html` | Skip-count by 10s and 100s within 1,000 | 30 | Before/after place-value chart; regrouping explained |
| 3 (2–4) | `games/add-within-1000.html` | Multi-digit addition with regrouping | 30 | Base-ten blocks grouping 10 into the next place |

## Run locally

Requires Node 18+ only for the helper scripts. The pages open directly in a browser.

```bash
npm start          # serves the folder at http://localhost:8080
npm test           # syntax-checks every game's script and checks element ids
npm run lint:html  # validates the HTML with html-validate
```

## Deploy

The site is published with GitHub Pages from the `main` branch, `/ (root)` folder (**Settings → Pages**).

## How the game code is organized

All games share the same structure, so a fix in one usually applies to the others:

- **Settings block** at the top of each `<script>` (round counts, difficulty stages, timing). Teachers can change these without touching the logic.
- `buildRounds()` generates a fresh randomized set of rounds each play.
- `showRound()` draws the current round.
- `win()` handles a correct answer. `showFix()` / `correct()` / `countTogether()` handle corrective feedback.
- `say()` reads text aloud with the browser's built-in Web Speech API.
- Colors are CSS variables on `:root` with dark-mode overrides under `prefers-color-scheme: dark` and `[data-theme="dark"]`.

### Teacher-adjustable settings

| Game | Setting | What it does |
|---|---|---|
| count-to-20 | `REPEATS` | Times each number appears (2 = 40 rounds) |
| ten-frame-subitizing | `FLASH_MS`, `REPEATS` | How long dots show in quick-look mode; rounds per number |
| make-5 / make-10 | `KNOWN_LIST` | Which known parts appear and how often |
| numbers-to-120 | `BIG_COUNT`, `SMALL_COUNT`; `kinds` in `buildRounds()` | How many 100–120 vs. 20–99 numbers; mix of round types |
| count-by-10s-and-100s | `STAGES` | Difficulty stages: direction, crossing a hundred, blanks |
| add-within-1000 | `STAGES` | Difficulty stages: which columns regroup, special cases |

## Security and privacy

- Every page has a Content-Security-Policy that allows only the site's own files and Google Fonts. Pages cannot load other scripts, connect to servers, or submit forms.
- No data is collected or stored. There are no cookies, no analytics, and no browser storage. Scores reset when the page reloads.
- The only third-party request is Google Fonts (Andika and Fredoka). If a school filter blocks it, pages fall back to system fonts. To remove it entirely, self-host the fonts (both use the SIL Open Font License) and drop the Google URLs from each page's CSP.

## Things to test by hand

- **Speech:** Web Speech API voices, rate, and timing differ by browser and device. Chrome blocks speech until the first tap, so round 1's spoken prompt may be silent.
- **Emoji rendering** differs by OS (Windows, ChromeOS, iOS, Android).
- **Chromebooks and iPads** on the school network, especially touch targets and the on-screen keypads.
- **Screen readers:** buttons and live regions have labels, but the games have not been tested with VoiceOver, TalkBack, or NVDA.

## License

Proprietary. Copyright © 2026 Miss Y's Reading and Math Education. All rights reserved. See [LICENSE](LICENSE).
