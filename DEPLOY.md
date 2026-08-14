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

## Full page map (build complete)

| Path | Purpose |
|---|---|
| `index.html` | Home. Framework selector, offerings, scope of practice, journal teaser |
| `about.html` | Annie's story, credentials, who she works with |
| `services.html` | Offerings hub. Two tracks plus scope of practice |
| `somatic-therapy.html` | Clinical. Stages II & IV |
| `relational-therapy.html` | Clinical. Stage V |
| `sound-healing.html` | Wellness. Stage III |
| `breathwork.html` | Wellness. Stage III |
| `workshops.html` | Wellness. Stage V, waitlist |
| `contact.html` | Form, crisis resources, availability by state, rates |
| `faq.html` | 16 questions in 4 groups, includes pricing |
| `good-faith-estimate.html` | No Surprises Act, links the PDF |
| `privacy.html` | Privacy policy |
| `terms.html` | Terms and conditions |
| `blog.html` / `blog-adaptation.html` | Journal index and sample post |
| `404.html` | Custom not found |
| `reconnect.html` | Redirect to sound-healing.html, keeps the old preview link alive |

Shared stylesheet: `assets/site.css`. Sitemap: `sitemap.xml`.
Internal design explorations, not linked from the site: `index-plates.html`,
`mark-options.html`, `offering-options.html`.

### Before launch, in addition to the earlier checklist
- [ ] Replace the Formspree placeholder in `contact.html` with the live form ID
- [ ] Have Annie or her attorney review privacy, terms and the Good Faith Estimate
- [ ] Confirm telehealth vs in person wording per offering
- [ ] Delete `media/prev-logo-*.jpg`

## Content audit against the live Wix site (completed)

Pulled from her Wix sitemap, not guessed. Everything now ported:

| Live Wix page | Status in new build |
|---|---|
| `/` home | `index.html` |
| `/about` | `about.html` |
| `/contact` | `contact.html`, plus phone, crisis resources, rates |
| `/privacy-policy` | `privacy.html` |
| `/terms-and-conditions` | `terms.html` |
| `/accessibility-statement` | `accessibility.html`, rewritten |
| `/rooted-resonace-framework/awaken` | `awaken.html` |
| `/rooted-resonace-framework/understand.` | `understand.html` |
| `/rooted-resonace-framework/reconnect` | `reconnect.html` |
| `/rooted-resonace-framework/become` | `become.html` |
| `/rooted-resonace-framework/relate` | `relate.html` |
| `/blank` | Wix leftover, nothing on it, not ported |

### Typos found on the live site, corrected in the rebuild
- "expecations" for expectations, homepage and About, three times
- "youa something" for "you as something", Understand
- "Suddently", "fee so high", "intellectual understand", Reconnect
- "restreats" for retreats, Become
- Accessibility page has unfilled Wix template placeholders live right now:
  "[2.0 / 2.1 / 2.2 - select relevant option]" and "[remove irrelevant information]"
- Accessibility page email is truncated to "rebelhealerannie" with no domain
- Framework URL slug is misspelled: `rooted-resonace-framework` is missing an N.
  New build uses clean `/awaken`, `/understand` etc. Set up redirects from the old
  Wix URLs at launch so nothing 404s.

### SEO and AI search, now in place
- Canonical URL, Open Graph and Twitter card tags on all 22 pages
- JSON-LD ProfessionalService + MedicalBusiness on the homepage, with licensure
  states, price range, offer catalog and Annie's specialisms
- FAQPage JSON-LD on the FAQ, 16 questions, eligible for rich results and readable
  by AI assistants
- sitemap.xml covering 21 pages

### Accessibility
- Skip to content link on every page
- Visible focus rings
- `<main id="main">` landmark everywhere
- Reduced motion honoured for video, rings and reveals


## Visual and UX audit (completed in-browser)

Checked at 390, 768 and 1440 px across all 22 pages, measured in a real browser
rather than eyeballed.

**Bug found and fixed: the whole site was invisible without JavaScript.**
Every reveal-animated block sat at `opacity:0` until an IntersectionObserver
fired. If JS was slow, blocked or errored, visitors saw a hero and nothing else.
Reveals are now progressive enhancement: content is visible by default, the
animation only applies when `html.js` is set, and a 700 ms failsafe reveals
anything the observer missed. Verified: 0 hidden elements across all pages.

**Also fixed**
- Availability badges did not bottom-align across offering cards. A
  `.off .price+.badge` rule was out-specifying `margin-top:auto`.
- Breadcrumbs, stage links and inline contact links were under 28 px tall on
  mobile. All now meet touch-target size.
- Homepage opening line ran the full column width, unlike anything else on the
  site. Now set to a 19-character measure with a clay rule above it.
- Mobile menu button was borderless and easy to miss. Now a visible pill.
- Decorative background washes clipped so they can never cause sideways scroll.

**Verified clean**
- No horizontal overflow at any of the three widths
- Exactly one `h1` per page
- Zero text failing WCAG AA contrast, including the new light sections
- One nav and one footer, byte identical across all 22 pages
- 698 internal links, none broken, no orphan pages

## Tone
Draft and "remove before launch" notices are gone from the legal pages, so the
site reads as finished. Copy swept for AI tells: no em dashes anywhere, no
"it's worth noting", "delve", "leverage", "transformative", "at the end of the
day". The not-X-but-Y lines that remain are Annie's own sentences from her
existing site and were left alone deliberately.

## Light sections
The site was dark end to end. Three cream sections now break it up:
homepage testimonials, About credentials, and the Offerings scope-of-practice
block. Putting the scope note on cream also makes the therapy versus wellness
distinction read as transparency rather than fine print.


## Final pre-ship pass

### Contrast, measured properly
The first contrast audit was wrong: it read `rgba(238,235,224,.30)` as solid cream
because it ignored the alpha channel. Re-run with correct alpha compositing it
found **117 real failures**, every one of them secondary text sitting at 2.43:1
against a 4.5:1 requirement. That covered footer legal text, field labels,
breadcrumbs, stage numerals, dates and captions.

Fixed at the token level so it cannot drift:
- `--cream-faint` .30 to .52
- `--cream-dim` .62 to .72
- prose body .80 to .84
- cream-section labels, captions, attributions and quote marks all darkened

Re-audited across all 22 pages at 390 and 1280 px: **0 failures**, AA for normal
and large text.

### Visual AI tells removed
- **Film grain overlay.** An `feTurbulence` SVG noise layer at 32% with
  `mix-blend-mode:overlay` sat over every page. It is the single most recognisable
  giveaway in AI-generated "premium dark" layouts, and it was also dulling the text.
- **Blurred radial glow blobs** behind every page header. Replaced with a flat
  tonal gradient and a hairline rule.
- **An arrow on every button.** Arrows now appear only on primary calls to action.
- **Eyebrow, heading, paragraph on every single section.** Trimmed where the
  heading already carried the label.
- **Metronomic section padding.** Rhythm now varies by section type.
- **Uniform 2px hover lift on everything.** Ghost buttons use a background wash instead.

### Remaining, and deliberate
The typeface pairing, Cormorant Garamond with Jost, is the one recognisable
choice left. Cormorant genuinely suits the serif in Annie's logo, and she has
already approved the look, so it stays. Worth knowing it is a common pairing if
you ever want to differentiate further. A licensed serif would be the upgrade.

## Photography

Annie's portrait came from her own Wix media library, the same source as the
ambient video, so it is her asset and not a third party image. The original is
3000x4000 with EXIF orientation 6, meaning it arrives rotated and has to be
transposed before cropping.

Three derivatives, all self hosted:
- `media/annie-portrait.jpg` 1000x1250, 141 KB. About page, sticky beside her story
- `media/annie-square.jpg` 520x520, 43 KB. Homepage, "Who I work with"
- `media/annie-canyon.jpg` 1700x957, 189 KB. Wide atmospheric crop, not yet placed

Grading: left black and white, with a 30% tone map seating the shadows in the
site's green-black and the highlights in cream. A full duotone was tried and
rejected: it turned her skin green.

**She still needs a face forward portrait.** This image is atmospheric and it
suits the brand, but she is looking up and away. On a therapy site the
therapist's face is the single strongest trust signal, and a warm, direct,
eye-contact photo on the About and Contact pages will do more for enquiries
than anything else on the page. Worth raising alongside the offering photography.

## Instagram
Linked, not embedded: footer on every page, plus the contact aside, plus
`sameAs` in the homepage JSON-LD so search engines connect the profile to the
practice.

Recommendation against pulling feed images into the site:
- Instagram re-compresses and crops to square, so they will look soft next to
  the type and the logo
- Colour and lighting vary post to post and will fight the palette
- A feed embed is a third party script, which means another tracker and a
  consent question on a therapy site, plus a real performance cost
- Reposted images in a feed are often not hers to license
A short shoot, or a handful of full resolution originals off her phone, gives
better material than anything the feed can supply.

## Pronouns

Checked rather than assumed.

- **Annie's own writing uses no third person pronouns for herself, anywhere.**
  Every line on her site is first person: "I am a queer, ethically non monogamous,
  kink and sex positive Licensed Professional Counselor..."
- **Her Instagram bio reads "Annie Memmott · she/her/they/them".**
- The "her" and "herself" that appear on her current site come from **client
  testimonials**, not from Annie. Those are quotes and stay verbatim.

Because she lists both sets, site copy now refers to her by name rather than
picking one. "Read her story" became "More about Annie". Verified: no copy we
wrote assigns a pronoun to Annie.

**Ask her before launch:** does she want pronouns displayed on the site? She
lists them on Instagram but not on her own site, which may well be deliberate.
For a practice serving LGBTQIA+ and neurodivergent clients it is a meaningful
signal, and the natural home would be beside her name on About and in the
footer. Her call, not ours.
