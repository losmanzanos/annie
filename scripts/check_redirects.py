#!/usr/bin/env python3
"""Fail the build on a _redirects rule that loops.

Cloudflare Pages serves /blog from blog.html and 308s /blog.html -> /blog.
A rule mapping /blog -> /blog.html therefore bounces forever and the page dies
with ERR_TOO_MANY_REDIRECTS. This has been written by hand twice already, so it
is an exit code and not a comment."""
import os, re, sys

F = os.path.join(os.path.dirname(__file__), '..', '_redirects')
if not os.path.exists(F):
    sys.exit(0)

errs = []
for n, raw in enumerate(open(F, encoding='utf-8'), 1):
    line = raw.strip()
    if not line or line.startswith('#'):
        continue
    parts = line.split()
    if len(parts) < 2:
        continue
    src, dst = parts[0], parts[1]

    if dst.endswith('.html'):
        errs.append(f"{n}: '{src} -> {dst}' targets a .html file. "
                    f"Cloudflare 308s .html to the clean URL, so this loops. Use '{dst[:-5]}'.")
    if src.rstrip('/') == dst.rstrip('/'):
        errs.append(f"{n}: '{src} -> {dst}' points at itself.")
    if src == '/*':
        errs.append(f"{n}: catch-all '/*' shadows every real page. Remove it; "
                    f"Pages serves 404.html automatically.")
    if re.match(r'^/admin', src):
        errs.append(f"{n}: '{src}' shadows the TinaCMS admin route.")

if errs:
    print("_redirects has loop-inducing rules:\n  " + "\n  ".join(errs), file=sys.stderr)
    sys.exit(1)
print("_redirects OK")
