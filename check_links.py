"""Check that every local href and src in the website points to an existing file.

Run from the repository root: python site/check_links.py
Exits with 1 and lists the broken references if any are missing. Standard library only.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys

SITE = Path(__file__).resolve().parent
BASE = "/open-journalist/"  # path of the site on https://kaimys.github.io


class Refs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in ("href", "src") and value:
                self.refs.append(value)
            if name == "id" and value:
                self.ids.add(value)


def main() -> int:
    pages = sorted(SITE.rglob("*.html"))
    parsed = {}
    for page in pages:
        p = Refs()
        p.feed(page.read_text(encoding="utf-8"))
        parsed[page] = p
    broken = []
    for page, p in parsed.items():
        for ref in p.refs:
            parts = urlsplit(ref)
            if parts.scheme or ref.startswith(("//", "mailto:")):
                continue
            path = unquote(parts.path)
            if path.startswith(BASE):  # absolute link to the published site, as in 404.html
                target = SITE / path[len(BASE):]
            elif not path:
                target = page
            else:
                target = page.parent / path
            if target.is_dir():
                target = target / "index.html"
            if not target.exists():
                broken.append(f"{page.relative_to(SITE)}: {ref} (missing file)")
                continue
            if parts.fragment and target.suffix == ".html":
                ids = parsed.get(target.resolve(), parsed.get(target))
                if ids is None:
                    ids = Refs(); ids.feed(target.read_text(encoding="utf-8"))
                if parts.fragment not in ids.ids:
                    broken.append(f"{page.relative_to(SITE)}: {ref} (missing anchor)")
    for line in broken:
        print(line)
    print(f"{len(pages)} pages checked, {len(broken)} broken references")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
