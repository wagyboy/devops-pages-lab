"""Release gate for the built site.

Usage: python3 check_site.py <site_dir> <base_path>

Fails (exit 1) if the built site is not safe to deploy:
  1. index.html is missing, or the activity markers / at least one activity item are missing.
  2. A page has no <!doctype html>, no <html lang>, or an empty <title>.
  3. Raw Liquid ("{{" or "{%") leaked into the output.
  4. An internal link or asset (href/src) points to a file that does not exist.
  5. version.txt (used by the smoke test) is missing.
External links (https://...) are not fetched: they belong to other sites and
would make the gate flaky.
"""
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

START = "<!--START_SECTION:activity-->"
END = "<!--END_SECTION:activity-->"


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.lang = None
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.lang = attrs.get("lang")
        if tag == "title":
            self._in_title = True
        for name in ("href", "src"):
            if attrs.get(name):
                self.links.append(attrs[name])

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def resolve(site_dir, page_path, link, base_path):
    """Return the file a link points to, or None if the link is external."""
    parts = urlsplit(link)
    if parts.scheme or link.startswith("//") or link.startswith("#"):
        return None
    path = unquote(parts.path)
    if not path:
        return None
    if path.startswith("/"):
        if path != base_path and not path.startswith(base_path + "/"):
            return os.path.join(site_dir, "__outside_base_path__" + path)
        target = os.path.join(site_dir, path[len(base_path):].lstrip("/"))
    else:
        target = os.path.join(os.path.dirname(page_path), path)
    return os.path.normpath(target)


def exists(target):
    if os.path.isfile(target):
        return True
    if os.path.isdir(target) and os.path.isfile(os.path.join(target, "index.html")):
        return True
    return os.path.isfile(target + ".html")


def main(site_dir, base_path):
    base_path = "/" + base_path.strip("/") if base_path.strip("/") else ""
    errors = []

    index = os.path.join(site_dir, "index.html")
    if not os.path.isfile(index):
        errors.append("index.html is missing")
    else:
        html = open(index, encoding="utf-8").read()
        if START not in html or END not in html:
            errors.append("index.html: activity markers are missing")
        else:
            section = html.split(START, 1)[1].split(END, 1)[0]
            if "<li" not in section:
                errors.append("index.html: activity section has no items")

    if not os.path.isfile(os.path.join(site_dir, "version.txt")):
        errors.append("version.txt is missing")

    pages = links = 0
    for root, _, files in os.walk(site_dir):
        for name in files:
            if not name.endswith(".html"):
                continue
            path = os.path.join(root, name)
            rel = os.path.relpath(path, site_dir)
            html = open(path, encoding="utf-8").read()
            pages += 1

            if not re.match(r"\s*<!doctype html>", html, re.IGNORECASE):
                errors.append(f"{rel}: missing <!doctype html>")
            if "{{" in html or "{%" in html:
                errors.append(f"{rel}: raw Liquid tag in output")

            parser = PageParser()
            parser.feed(html)
            if not parser.lang:
                errors.append(f"{rel}: <html> has no lang attribute")
            if not parser.title.strip():
                errors.append(f"{rel}: empty <title>")

            for link in parser.links:
                target = resolve(site_dir, path, link, base_path)
                if target is None:
                    continue
                links += 1
                if not exists(target):
                    errors.append(f"{rel}: broken link {link}")

    print(f"Checked {pages} page(s) and {links} internal link(s).")
    for error in errors:
        print(f"::error title=Release gate::{error}")
    if errors:
        print(f"Gate FAILED with {len(errors)} problem(s); the site will not be deployed.")
        return 1
    print("Gate passed: the site is safe to deploy.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1], sys.argv[2]))
