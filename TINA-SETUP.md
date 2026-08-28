# TinaCMS /admin — remaining steps

Code side is done: package.json, .nvmrc, tina/config.js, content/posts/.
Build outputs the admin UI to /admin, so the live route is /admin/index.html.

## 1. Tina Cloud project  (app.tina.io)
Sign in with ANNIE'S GitHub. New Project -> "Import your site" ->
repo `rootedresonance/rootedresonance`, branch `main`.
Copy the **Client ID**. Then Tokens -> generate a **Read Only Token**.

## 2. Cloudflare Pages -> Settings -> Environment variables (Production AND Preview)
NEXT_PUBLIC_TINA_CLIENT_ID = <client id>
TINA_TOKEN                 = <read only token>
NODE_VERSION               = 20

## 3. Cloudflare Pages -> Settings -> Builds & deployments
Build command:      npm ci && npx tinacms build
Output directory:   /
Root directory:     (leave blank)

## 4. Redeploy, then visit /admin and log in with GitHub.

## Local test before pushing
npm install
npx tinacms dev -c "python3 -m http.server 8000"
-> http://localhost:8000/admin

## Gotchas
- `outputFolder: "admin"` + `publicFolder: "."` is what puts it at /admin. Don't change.
- The _redirects file must NOT contain a /admin rule or it will shadow the route.
- Tina writes markdown to content/posts/. blog.html is currently hand-written, so a new
  post will appear in the repo but not on /blog until the listing is generated from
  content/posts at build time. That is the one remaining piece.
