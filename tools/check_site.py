#!/usr/bin/env python3
"""Dependency-free checks for the exact static files served by GitHub Pages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
STORE = 'https://apps.apple.com/us/app/clipzelo-video-compressor/id6824147929'

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids, self.refs, self.metas = set(), [], {}
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f"Duplicate ID: {attrs['id']}"
            self.ids.add(attrs['id'])
        if tag == 'meta':
            self.metas[attrs.get('property', attrs.get('name'))] = attrs.get('content')
        if tag == 'img':
            assert 'alt' in attrs and 'width' in attrs and 'height' in attrs, attrs
        if tag == 'script':
            raise AssertionError('This site should remain script-free')
        if tag == 'a' and attrs.get('target') == '_blank':
            assert {'noopener', 'noreferrer'} <= set(attrs.get('rel', '').split())
        for key in ('href', 'src'):
            if key in attrs:
                self.refs.append(attrs[key])

pages = {p.name: Page(p) for p in ROOT.glob('*.html')}
for name, page in pages.items():
    for ref in page.refs:
        url = urlsplit(ref)
        if url.scheme:
            assert url.scheme in ('https', 'mailto'), f'Unsafe URL: {ref}'
            continue
        assert not url.netloc, f'Unexpected remote resource: {ref}'
        path = unquote(url.path)
        target = (ROOT / path) if path else (ROOT / name)
        if target.is_dir():
            target /= 'index.html'
        assert target.is_file(), f'Missing target in {name}: {ref}'
        if url.fragment:
            assert unquote(url.fragment) in pages[target.name].ids, f'Broken anchor: {ref}'
    assert page.metas.get('description') and page.metas.get('viewport')

home = pages['index.html']
# These were public support fragments before the product launch.
assert {'main', 'welcome', 'getting-started', 'plans', 'restore', 'faq', 'contact'} <= home.ids
assert STORE in home.refs
assert all(ref == STORE for ref in home.refs if 'apps.apple.com' in ref)
for key in ('og:type', 'og:title', 'og:description', 'og:url', 'og:image', 'og:image:alt'):
    assert home.metas.get(key), f'Missing {key}'
assert home.metas['og:url'] == 'https://liuyuw.github.io/clipzelo-support/'
assert (ROOT / '.nojekyll').is_file()
assert not list(ROOT.glob('*.js')), 'No runtime JavaScript expected'
print(f'PASS: {len(pages)} production HTML pages, all local links/fragments/assets, preserved support anchors, metadata and external-link safety')
