#!/usr/bin/env python3
"""Print the email addresses and phone links published on web pages.

Usage: extract_contacts.py URL [URL ...]

Reads the raw HTML of each page, so it sees addresses that a
text-rendering fetch tool shows as "[email protected]". Handles plain
addresses, mailto: links, HTML-entity encoding, Cloudflare email
protection, and "name [at] domain [dot] com" spellings.

Standard library only. Output is one block per URL.
"""

import html
import re
import sys
import urllib.parse
import urllib.request

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120 Safari/537.36"
)
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+")
SPELLED = re.compile(
    r"([A-Za-z0-9._%+-]+)\s*[\[\(]\s*at\s*[\]\)]\s*"
    r"((?:[A-Za-z0-9-]+\s*[\[\(]\s*dot\s*[\]\)]\s*)+[A-Za-z]{2,})",
    re.I,
)
DOT = re.compile(r"\s*[\[\(]\s*dot\s*[\]\)]\s*", re.I)
CLOUDFLARE = re.compile(
    r'data-cfemail="([0-9a-fA-F]+)"|email-protection#([0-9a-fA-F]+)'
)
TEL = re.compile(r'href="tel:([^"]+)"', re.I)
# Addresses that appear in page source but are not the business's contact
# details: image filenames, font licences, error-reporting services.
NOISE = re.compile(
    r"\.(png|jpe?g|gif|webp|svg|css|js)$|sentry|wixpress|example\.|"
    r"@(2x|3x)\b",
    re.I,
)


def decode_cloudflare(encoded):
    """Cloudflare stores the key in the first byte and XORs the rest."""
    data = bytes.fromhex(encoded)
    return "".join(chr(b ^ data[0]) for b in data[1:])


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read().decode("utf-8", "replace")


def contacts(page):
    page = html.unescape(page)
    emails = {}

    def add(address, how):
        address = address.strip().strip(".").lower()
        if EMAIL.fullmatch(address) and not NOISE.search(address):
            emails.setdefault(address, how)

    for a, b in CLOUDFLARE.findall(page):
        try:
            add(decode_cloudflare(a or b), "cloudflare-protected")
        except ValueError:
            pass
    for name, domain in SPELLED.findall(page):
        add(name + "@" + DOT.sub(".", domain), "spelled out")
    for address in EMAIL.findall(urllib.parse.unquote(page)):
        add(address, "plain")

    phones = sorted({urllib.parse.unquote(t).strip() for t in TEL.findall(page)})
    return emails, phones


def main(urls):
    if not urls:
        sys.exit(__doc__)
    for url in urls:
        print(url)
        try:
            emails, phones = contacts(fetch(url))
        except Exception as error:  # report and move on to the next URL
            print(f"  error: {error}")
            continue
        for address, how in sorted(emails.items()):
            print(f"  email: {address} ({how})")
        for phone in phones:
            print(f"  phone: {phone}")
        if not emails and not phones:
            print("  nothing found")


if __name__ == "__main__":
    main(sys.argv[1:])
