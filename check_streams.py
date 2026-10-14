#!/usr/bin/env python3
"""
Check which streams in an M3U playlist are actually working, and write a
cleaned playlist containing only the working ones.

Usage:
    python3 check_streams.py input.m3u working.m3u

It requests each stream URL (following redirects) and keeps entries whose
master playlist responds with HTTP 200 and a non-empty body. Tune TIMEOUT
and WORKERS below if needed.

Requires only the Python standard library.
"""

import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor

TIMEOUT = 8      # seconds per request
WORKERS = 40     # parallel requests


def is_working(url: str) -> bool:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (VLC/3.0; like Gecko)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            if resp.status != 200:
                return False
            chunk = resp.read(2048)
            return len(chunk) > 0
    except Exception:
        return False


def parse(path):
    lines = open(path, encoding="utf-8").read().replace("\r\n", "\n").split("\n")
    entries = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("#EXTINF"):
            url = lines[i + 1] if i + 1 < len(lines) else ""
            if url.startswith("http"):
                entries.append((lines[i], url))
            i += 2
        else:
            i += 1
    return entries


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    src, dst = sys.argv[1], sys.argv[2]

    entries = parse(src)
    print(f"checking {len(entries)} streams with {WORKERS} workers...")

    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        results = list(ex.map(lambda e: is_working(e[1]), entries))

    working = [e for e, ok in zip(entries, results) if ok]
    print(f"working: {len(working)} / {len(entries)}")

    with open(dst, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for extinf, url in working:
            f.write(extinf + "\n" + url + "\n")
    print(f"wrote {dst}")


if __name__ == "__main__":
    main()
