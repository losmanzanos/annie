#!/usr/bin/env python3
"""Blog generator. Tina edits content/blog/*.json only; this writes the HTML.

published:false does not hide a post, it removes it: the file is deleted from
disk and dropped from the sitemap, so the URL genuinely 404s."""
import os, json, glob, re, html, sys

ROOT = os.path.join(os.path.dirname(__file__), '..')
BASE = "https://rootedresonancetherapy.com/"
TEMPLATE_SRC = os.path.join(ROOT, 'blog-adaptation.html')

def esc(s): return html.escape(s, quote=True)

def render_body(blocks):
    out, first = [], True
    for b in blocks:
        b = b.strip()
        if not b: continue
        if b.startswith('## '):
            out.append('    <h2>%s</h2>' % esc(b[3:].strip())); first = False
        elif b.startswith('> '):
            out.append('    <blockquote>%s</blockquote>' % esc(b[2:].strip())); first = False
        else:
            cls = ' class="drop"' if first else ''
            out.append('    <p%s>%s</p>' % (cls, esc(b))); first = False
    return '\n\n'.join(out)

def load():
    posts = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'content/blog/*.json'))):
        p = json.load(open(f, encoding='utf-8'))
        p.setdefault('slug', os.path.splitext(os.path.basename(f))[0])
        posts.append(p)
    posts.sort(key=lambda p: p.get('date', ''), reverse=True)
    return posts

SHELL = None
def shell():
    """Reuse the existing post page as the chrome, so the design cannot drift."""
    global SHELL
    if SHELL is None:
        SHELL = open(TEMPLATE_SRC, encoding='utf-8').read()
    return SHELL

def build_post(p):
    s = shell()
    title = p['title'].rstrip('.')
    full = f"{title} | Rooted Resonance"
    url = BASE + p['slug']
    s = re.sub(r'<title>.*?</title>', '<title>%s</title>' % esc(full), s, flags=re.S)
    for attr in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        s = re.sub(r'<meta %s content="[^"]*">' % re.escape(attr),
                   '<meta %s content="%s">' % (attr, esc(p['metaDescription'])), s)
    for attr in ('property="og:title"', 'name="twitter:title"'):
        s = re.sub(r'<meta %s content="[^"]*">' % re.escape(attr),
                   '<meta %s content="%s">' % (attr, esc(full)), s)
    s = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="%s">' % url, s)
    s = re.sub(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="%s">' % url, s)
    s = re.sub(r'"headline":"[^"]*"', '"headline":%s' % json.dumps(p['title']), s)
    s = re.sub(r'"datePublished":"[^"]*"', '"datePublished":"%s"' % p['date'], s)

    header = (
      '<header class="post">\n  <div class="wrap col">\n'
      '    <div class="crumb"><a href="blog.html">Journal</a> &nbsp;/&nbsp; %s</div>\n'
      '    <h1>%s</h1>\n    <div class="byline">\n      <span>%s</span>\n'
      '      <span>%s</span>\n    </div>\n  </div>\n</header>'
      % (esc(p.get('stageLabel','')), p.get('titleHtml') or esc(p['title']),
         esc(p.get('author','Annie Memmott, LPC')), esc(p.get('dateLabel', p['date'])))
    )
    s = re.sub(r'<header class="post">.*?</header>', lambda _: header, s, flags=re.S)

    endnote = ''
    if p.get('endnoteTitle'):
        endnote = ('\n\n    <div class="rule"></div>\n\n    <div class="endnote">\n'
                   '      <div class="k">%s</div>\n      <p>%s</p>\n    </div>'
                   % (esc(p['endnoteTitle']), esc(p.get('endnoteBody',''))))
    article = ('<article>\n  <div class="wrap col">\n%s%s\n  </div>\n</article>'
               % (render_body(p['body']), endnote))
    s = re.sub(r'<article>.*?</article>', lambda _: article, s, flags=re.S)
    return s

LIST_ENTRY = ('      <a class="entry" href="{slug}.html">\n'
              '        <span class="meta">{meta}</span>\n'
              '        <div>\n          <h2>{title}</h2>\n          <p>{excerpt}</p>\n        </div>\n'
              '        <span class="arw">&rarr;</span>\n      </a>')

def build_index(live):
    idx = os.path.join(ROOT, 'blog.html')
    s = open(idx, encoding='utf-8').read()
    if live:
        entries = '\n\n'.join(LIST_ENTRY.format(
            slug=p['slug'],
            meta=esc(('%s · %s' % (short_date(p), p.get('readingTime',''))).strip(' ·')),
            title=esc(p['title']), excerpt=esc(p['excerpt'])) for p in live)
        soon = '<div class="soon rv"><span class="dot"></span> More entries as they\'re written.</div>'
    else:
        entries = ''
        soon = '<div class="soon rv"><span class="dot"></span> First entry coming soon.</div>'
    block = ('<div class="list rv">\n%s\n    </div>\n\n    %s' % (entries, soon))
    s = re.sub(r'<div class="list rv">.*?<div class="soon rv">.*?</div>',
               lambda _: block, s, flags=re.S)
    open(idx, 'w', encoding='utf-8').write(s)

MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
def short_date(p):
    try:
        y, m, d = p['date'].split('-')
        return "%s %d, %s" % (MONTHS[int(m)-1], int(d), y)
    except Exception:
        return p.get('dateLabel', p.get('date', ''))

def update_sitemap(live):
    f = os.path.join(ROOT, 'sitemap.xml')
    s = open(f, encoding='utf-8').read()
    urls = '\n'.join(
        '<url><loc>%s%s</loc><lastmod>%s</lastmod><changefreq>monthly</changefreq>'
        '<priority>0.6</priority></url>' % (BASE, p['slug'], p['date']) for p in live)
    block = '<!-- blog:start -->\n%s\n<!-- blog:end -->' % urls
    if '<!-- blog:start -->' in s:
        s = re.sub(r'<!-- blog:start -->.*?<!-- blog:end -->', lambda _: block, s, flags=re.S)
    else:
        # first run: drop any hand-written post URLs, then insert the managed block
        s = re.sub(r'\s*<url><loc>[^<]*blog-[^<]*</loc>.*?</url>', '', s, flags=re.S)
        s = s.replace('</urlset>', block + '\n</urlset>')
    open(f, 'w', encoding='utf-8').write(s)

def main():
    posts = load()
    live = [p for p in posts if p.get('published')]
    known = {p['slug'] for p in posts}
    for p in live:
        open(os.path.join(ROOT, p['slug'] + '.html'), 'w', encoding='utf-8').write(build_post(p))
        print('  wrote', p['slug'] + '.html')
    # unpublishing must remove the URL, not merely unlink it
    for p in posts:
        if not p.get('published'):
            f = os.path.join(ROOT, p['slug'] + '.html')
            if os.path.exists(f):
                os.remove(f); print('  removed (unpublished)', p['slug'] + '.html')
    build_index(live)
    update_sitemap(live)
    print('blog: %d published, %d total' % (len(live), len(posts)))

if __name__ == '__main__':
    main()
