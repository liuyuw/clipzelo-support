# clipzelo-support

Official support and privacy policy for Clipzelo iOS app.

## Website

- Support: https://liuyuw.github.io/clipzelo-support/
- Privacy Policy: https://liuyuw.github.io/clipzelo-support/privacy.html
- Support and privacy contact: clipzelosupport@gmail.com

Static HTML/CSS only. No JavaScript, framework, build dependencies, backend, forms, analytics, tracking, remote fonts or embedded media.

## Files

- `index.html`: introduction, compression instructions, Free/Pro, Restore Purchases, troubleshooting and contact.
- `privacy.html`: on-device processing, Photos permissions, temporary/local data, StoreKit, support correspondence and GitHub Pages hosting.
- `styles.css`: shared responsive styling using system fonts.
- `.nojekyll`: serve these files without Jekyll processing.

GitHub Pages publishes `main` / root. Update these static files and push to main to redeploy. Locally preview with `python3 -m http.server 8766 --bind 127.0.0.1` and visit http://127.0.0.1:8766/.

Review content against actual app behavior before publishing updates. The website adds no tracking, but GitHub Pages logs visitor IP addresses for security as explained in the Privacy Policy. The app does not promise that Apple Photos retrieval, StoreKit or sharing is offline.

This is a separate public website repository. It contains no private iOS application source, project files, credentials or app-repository history. Do not copy that private repository into this one.
