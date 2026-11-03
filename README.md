# Clipzelo website

The official product, support and privacy website for Clipzelo for iPhone.

## Public URLs

- Homepage and App Store Support URL: https://liuyuw.github.io/clipzelo-support/
- Support section: https://liuyuw.github.io/clipzelo-support/#support
- Privacy Policy: https://liuyuw.github.io/clipzelo-support/privacy.html
- App Store: https://apps.apple.com/us/app/clipzelo-video-compressor/id6824147929
- Support and privacy contact: clipzelosupport@gmail.com

The site root still contains the complete support content. Existing support fragments (`#getting-started`, `#plans`, `#restore`, `#faq`, `#contact`, `#main`, `#welcome`) remain valid. The Privacy Policy text and URL are preserved.

## Implementation

Static HTML/CSS and local PNG assets only. No runtime JavaScript, framework, build dependencies, backend, forms, analytics, tracking, remote fonts or embedded media. The App Store call to action is a text link, not a recreated Apple badge. The desktop QR code is a local image; phone visitors get the direct download link. See [asset provenance](assets/README.md).

- `index.html`: product landing page, Free/Pro, full support instructions, Restore Purchases, troubleshooting and contact.
- `privacy.html`: existing privacy policy, with direct support navigation and favicon.
- `styles.css`: responsive styles, system fonts, visible keyboard focus, reduced-motion support.
- `assets/`: official icon derivatives and the App Store QR image.
- `.nojekyll`: serve files without Jekyll processing.
- `tools/check_site.py`: dependency-free checks for local links, preserved support anchors, image attributes, external-link safety and metadata.

## Verify and preview

There is no compilation step: the checked-in HTML, CSS and image files are the production site. Run the checks on those exact files:

```sh
python3 tools/check_site.py
python3 -m http.server 8766 --bind 127.0.0.1
```

Visit http://127.0.0.1:8766/ and `/privacy.html`. Check at narrow phone and desktop widths, keyboard navigation, the help links and FAQ toggles. The QR card appears above 800 CSS pixels. Decode `assets/app-store-qr.png` with an independent QR reader; its complete payload must match the App Store URL above, without added query parameters or a redirect service.

GitHub Pages currently publishes `main` / root. Submit changes through a PR; pushing a feature branch does not publish the site. Merging into `main` is a separate owner decision that updates the live site.

The website adds no tracking, but GitHub Pages logs visitor IP addresses for security as explained in the Privacy Policy. On-device compression does not mean Photos retrieval, StoreKit or sharing is always offline.

This public website repository contains no private iOS application source, project files, credentials or app-repository history.
