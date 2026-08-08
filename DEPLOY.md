# Deploy and preview

## 1. Push to GitHub

Repo already exists at `losmanzanos/annie`. From this folder:

```bash
git init -b main
git add .
git commit -m "Rooted Resonance prototype: home, Reconnect, journal, 404"
git remote add origin https://github.com/losmanzanos/annie.git
git push -u origin main
```

If the repo was created with a README or license, the push will be rejected.
Reconcile rather than force:

```bash
git pull --rebase origin main
git push -u origin main
```

Confirm the ignore rules worked. This should return nothing:

```bash
git ls-files | grep prev-logo
```

## 2. Preview hosting

**Netlify, connected to the repo** so every push redeploys.

Browser route (recommended, gives auto-deploy):
1. app.netlify.com, Add new site, Import an existing project
2. Pick GitHub, authorise, choose `losmanzanos/annie`
3. Build command: leave empty. Publish directory: `.`
4. Deploy

CLI route:

```bash
npm i -g netlify-cli
netlify login
netlify init      # links this repo, sets up auto-deploy
netlify deploy --prod
```

Then rename the site to something you can say out loud on a call:
Site configuration, Change site name, e.g. `rooted-resonance-preview`
giving `https://rooted-resonance-preview.netlify.app`

Cloudflare Pages is an equally good free alternative. Same idea:
connect repo, no build command, output directory `.`

## 3. Verify the preview is not indexable

```bash
curl -sI https://rooted-resonance-preview.netlify.app | grep -i x-robots-tag
```

Expect: `x-robots-tag: noindex, nofollow, noarchive`

If that header is missing, `_headers` did not get picked up and the
preview is crawlable. Fix before sending the link to anyone.

## 4. What Annie sees

Send her the root URL only.

| Path | Page |
|---|---|
| `/` | Home. Framework selector, offerings, scope of practice |
| `/reconnect` | Stage III offering page |
| `/journal` | Journal index |
| `/journal/intellectualizing` | Sample post |
| anything else | Custom 404 |

Not linked from the nav, but reachable if she guesses a URL:
`index-plates.html`, `mark-options.html`, `offering-options.html`.
These are internal design explorations. Delete them locally before the
launch commit, or move them into a `_design/` folder.

## 5. Launch checklist (later, not now)

- [ ] Delete the preview block from `_headers`
- [ ] Replace `robots.txt` with an allow rule plus sitemap reference
- [ ] Add `sitemap.xml`
- [ ] Point the domain at this site, DNS at a registrar in **Annie's** name
- [ ] Netlify, GitHub, Tina, GA4 accounts all owned by Annie, Chad as collaborator
- [ ] GA4 kept off any intake or booking path
- [ ] Clinical intake routed to a HIPAA compliant tool, not a plain form
- [ ] SPF, DKIM, DMARC on the sending domain
- [ ] Confirm licensure wording: currently OH, AZ, CO on clinical services
- [ ] Swap `media/logo-mark.png` for a vector once she supplies one
- [ ] Self host the ambient video, already done, confirm it is not still hotlinked

## Note: GitHub Pages preview

`_headers` and `netlify.toml` are Netlify features. GitHub Pages ignores both,
and `robots.txt` under `/annie/` is never read because robots.txt is only
honoured at the domain root (`losmanzanos.github.io/robots.txt`).

So on Pages, indexing is blocked by a per page meta tag instead:

```html
<meta name="robots" content="noindex, nofollow">
```

Present in every HTML file, each marked `PREVIEW ONLY`. Remove them at launch
or the production site will be invisible to Google. Find them with:

```bash
grep -rn "noindex" *.html
```

Also on Pages: clean URLs like `/reconnect` do not work, so send links ending
in `.html`. The custom 404 does work, verified returning 404 with the styled page.
