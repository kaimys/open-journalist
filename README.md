# Open Journalist website

The website of [Open Journalist](https://github.com/open-journalist/open-journalist), published with GitHub Pages from the root of the `main` branch to <https://kaimys.github.io/open-journalist/>. It is static HTML, one stylesheet and a little JavaScript, with no build step and no third-party requests: no analytics, no cookies, no fonts or scripts from other hosts.

| Path | Content |
|---|---|
| `index.html` | Landing page: problem, idea, the demo case, principles, privacy, story graph, roadmap |
| `docs/` | Documentation for users: overview, installation, user guide with a worked example, concepts |
| `blog/` | Blog index and articles |
| `404.html` | Page for missing addresses; uses absolute paths under `/open-journalist/` |
| `assets/css/site.css` | Styles, following the design system v1.1 (ink on paper; dashed = proposed, solid = confirmed) |
| `assets/js/site.js` | Mobile navigation and the tabs of the install instructions |
| `check_links.py` | Checks that every local link, image and anchor exists; run it before every push |

## Preview locally

```
python -m http.server 8640
python check_links.py
```

Open <http://localhost:8640/>. All links inside the site are relative, so the same files work locally and under `/open-journalist/`.

## Add a blog article

Copy `blog/ai-for-media-hackathon-2026.html`, change title, description, date and text, and add a card for it at the top of `blog/index.html`.

## Where the images come from

- **Logo and mark:** copies of [`docs/assets/logo/`](https://github.com/open-journalist/open-journalist/tree/main/docs/assets/logo).
- **Diagrams** in `assets/img/readme/`: the README images of [`docs/assets/readme/`](https://github.com/open-journalist/open-journalist/blob/main/docs/assets/readme/README.md), converted to WebP.
- **Illustrations** in `assets/img/illu/`: cropped from the slides of the hackathon pitch and from the project's desktop backgrounds, both drawn in the design system; see [`docs/assets/readme/README.md`](https://github.com/open-journalist/open-journalist/blob/main/docs/assets/readme/README.md) for how the figures were made.
- **Screenshots** in `assets/img/screens/`: the prototype on `main` as of 2026-11-25, started with `--demo` in an empty data directory and a separate settings directory. The material is the synthetic demo case ([demo](https://github.com/open-journalist/open-journalist/blob/main/docs/demo.md)); the name "Alex Beispiel" in the approvals is fictional. Model steps ran against the team endpoint with `public` material only.

## Fonts

Inter and JetBrains Mono, copied from the `@fontsource` packages of the user interface and served from this site. Both are under the SIL Open Font License 1.1; the license texts are in `assets/fonts/`.
