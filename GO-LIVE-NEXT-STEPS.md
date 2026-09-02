# Go-live: remaining steps

Status as of last check: Cloudflare zone for **rootedresonancetherapy.com** created
(Free plan), Porkbun nameservers set to `izabella.ns.cloudflare.com` /
`kianchau.ns.cloudflare.com`, registry mid-propagation. Cloudflare shows **Pending**.
Site is built and pushed with all 220 canonical / schema / sitemap references already
pointing at the new domain.

Do nothing until the Cloudflare zone shows **Active**.

---

## 1. Attach the domain (once zone is Active)
Cloudflare → Workers & Pages → rootedresonance → Custom domains
- Add `rootedresonancetherapy.com`
- Add `www.rootedresonancetherapy.com`
- Wait for SSL to issue (a few minutes). Confirm https loads before going further.

## 2. Stop the preview URL competing with the real one   <-- easy to forget
`rootedresonance.pages.dev` is indexable right now. Once the custom domain is live
there are two crawlable copies of the same site.

Fix with a Cloudflare Redirect Rule:
- Rules → Redirect Rules → Create
- If `hostname equals rootedresonance.pages.dev`
- Then 301 to `https://rootedresonancetherapy.com` + preserve path + preserve query

Canonical tags already point at the real domain, which helps, but a 301 is definitive.

## 3. MX records for Google Workspace
Cloudflare's import scan copied Porkbun's defaults into the new zone.
- **DELETE** `fwd1.porkbun.com` (priority 10) and `fwd2.porkbun.com` (priority 20)
- **ADD** Google's MX records exactly as Workspace provides them
- Add the TXT verification record Google supplies
- Leaving both sets in place makes mail delivery unpredictable. Delete first.

After Workspace verifies, remind Annie to accept the **BAA** in
Admin Console → Account → Legal & Compliance. Paying for Workspace does not
enable HIPAA coverage on its own. This is the whole reason she bought it.

## 4. Update the two services that still reference the old domain
- **TinaCloud** → project → Configuration → Site URLs: add
  `https://rootedresonancetherapy.com`, remove the rootedresonancecoaching entries
- **EmailJS** → Account → Security → allowed origins: add the new domain,
  keep `rootedresonance.pages.dev` only until step 2 is done

## 5. Redirect the old domain (needs Wix login)
`rootedresonancecoaching.com` is on `ns8/ns9.wixdns.net`. To 301 it properly:
- Get registrar access at Wix, move its nameservers to Cloudflare
- Add it as a second zone in Cloudflare
- Redirect Rule: all paths -> `https://rootedresonancetherapy.com` (301, preserve path)
- Reconcile `_redirects` against the real Wix URL list first. The current file is
  inferred from typical Wix patterns, NOT verified against her actual sitemap.
- Once this is live her Wix site is no longer visible. Confirm with Annie first.
- Keep the old domain registered indefinitely (~$12/yr). Her URL is listed on
  Psychology Today, Headway, Rula, Instagram and Google Business Profile, and some
  of those cannot be updated quickly or at all.

## 6. Final verification
- Every route 200 on the new domain, `/nope` still 404s
- `/admin` loads and login works
- Toggle a post's Published off -> the URL genuinely 404s, and returns when back on
  (**still never tested end to end**)
- Submit the contact form from the live domain, confirm it arrives
- Search Console: add the new domain, submit the sitemap, use the
  change-of-address tool for the old domain
- Confirm no `noindex` anywhere

## 7. Handoff and security
- 2FA on Porkbun, Cloudflare, GitHub and Workspace pointed at **Annie's** phone
- She changes the Porkbun password. It was emailed in plaintext twice and is the
  same password as her Gmail. Registrar plus email in one credential is the worst
  case if it leaks.
- Remove any shared access once setup is complete
- Handoff doc: every account, credential and renewal date, all in her name
