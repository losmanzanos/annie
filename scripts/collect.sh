#!/usr/bin/env bash
# Assemble the publishable site into dist/.
# Never publish the repo root: once npm install has run, node_modules blows past
# the 20,000 file cap Cloudflare Pages enforces and the deploy is rejected.
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf dist && mkdir -p dist

cp -R ./*.html dist/
cp -R assets media dist/
cp favicon.ico manifest.json robots.txt sitemap.xml llms.txt _redirects _headers dist/ 2>/dev/null || true
[ -d admin ] && cp -R admin dist/admin
[ -d content ] && cp -R content dist/content   # Tina reads these at runtime

find dist -name '.DS_Store' -delete
echo "dist: $(find dist -type f | wc -l | tr -d ' ') files"
