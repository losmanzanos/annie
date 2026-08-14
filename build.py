# -*- coding: utf-8 -*-
"""Rooted Resonance static build. Emits consistent nav/footer across every page."""
import os, html, datetime

SITE = "Rooted Resonance"
LPC  = "Annie Memmott, LPC"
STATES = "Ohio, Arizona and Colorado"
STATES_SHORT = "OH · AZ · CO"
UPDATED = "August 2026"

NAV = [("about.html","About"),("services.html","Offerings"),
       ("index.html#framework","Framework"),("blog.html","Journal")]

FOOT = {
 "Offerings":[("somatic-therapy.html","Somatic Therapy"),("relational-therapy.html","Relational Therapy"),
              ("sound-healing.html","Sound Healing"),("breathwork.html","Breathwork"),
              ("workshops.html","Workshops")],
 "Practice":[("about.html","About Annie"),("index.html#framework","The Framework"),
             ("blog.html","Journal"),("faq.html","FAQ"),("contact.html","Contact")],
 "Legal":[("good-faith-estimate.html","Good Faith Estimate"),("privacy.html","Privacy Policy"),
          ("terms.html","Terms & Conditions")],
}

ICONS = {
"somatic":'''<svg class="ico" viewBox="0 0 32 32"><path class="g" d="M16 3v16.4"/><circle class="g" cx="16" cy="23.4" r="3.4"/><path class="f" d="M9.4 18.6a9 9 0 0 0 0 9.6M22.6 18.6a9 9 0 0 1 0 9.6"/><path class="warm" d="M5.6 16.2a12.8 12.8 0 0 0 0 14.4M26.4 16.2a12.8 12.8 0 0 1 0 14.4"/></svg>''',
"relational":'''<svg class="ico" viewBox="0 0 32 32"><circle class="g" cx="12.4" cy="13.2" r="7.4"/><circle class="g" cx="19.6" cy="13.2" r="7.4"/><circle class="f" cx="16" cy="20.4" r="7.4"/></svg>''',
"sound":'''<svg class="ico" viewBox="0 0 32 32"><circle class="g" cx="16" cy="16" r="5"/><circle class="g" cx="16" cy="16" r="10"/><circle class="f" cx="16" cy="16" r="15"/></svg>''',
"breath":'''<svg class="ico" viewBox="0 0 32 32"><path class="g" d="M3 20c4.8-11 9.6 6.4 12.8-4.8C19 4 23.8 12 28.8 8.8"/><path class="f" d="M3 26.4c4.8-7.2 9.6 4 12.8-3.2 3.2-7.2 8 5.6 13-2.4"/></svg>''',
"workshops":'''<svg class="ico" viewBox="0 0 32 32"><circle class="g" cx="10.4" cy="12" r="4"/><circle class="g" cx="21.6" cy="12" r="4"/><path class="f" d="M4 26.4c0-4.8 2.9-7.2 6.4-7.2s6.4 2.4 6.4 7.2M15.2 26.4c0-4.8 2.9-7.2 6.4-7.2s6.4 2.4 6.4 7.2"/></svg>''',
}

def badge(track):
    return ('<span class="badge clin"><span class="pip"></span>Therapy · OH AZ CO</span>'
            if track=="clin" else
            '<span class="badge well"><span class="pip"></span>Wellness · Nationwide</span>')

def head(title, desc, active=""):
    parts=[]
    for h,t in NAV:
        cls=' class="on"' if h==active else ''
        parts.append('<a href="'+h+'"'+cls+'>'+t+'</a>')
    links="".join(parts)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- PREVIEW ONLY: remove this line before launch -->
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Jost:wght@200;300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>

<nav id="nav">
  <a href="index.html" class="mark">
    <img class="glyph" src="media/logo-mark.png" alt="">
    <span class="b">Rooted</span> <span class="a">Resonance</span></a>
  <button class="burger" id="burger" aria-expanded="false" aria-controls="navlinks">Menu</button>
  <div class="navlinks" id="navlinks">{links}
    <a href="contact.html" class="navbtn">Reach out</a>
  </div>
</nav>

<main>
'''

def foot():
    cols = ""
    for h5, items in FOOT.items():
        cols += '<div class="f-col"><h5>' + h5 + '</h5>' + "".join(
            '<a href="' + h + '">' + t + '</a>' for h, t in items) + "</div>"
    year = str(datetime.date.today().year)
    htmlpart = """</main>

<footer>
  <div class="wrap">
    <div class="f-top">
      <div class="f-col f-brand">
        <img class="f-seal" src="media/logo-full.png" alt="Rooted Resonance Coaching and Therapy">
        <p>""" + LPC + """<br>Licensed in """ + STATES + """<br>Coaching and wellness offered nationwide.</p>
      </div>
      """ + cols + """
    </div>
    <p class="f-scope">Somatic and relational therapy are psychotherapy, provided under Annie's
    counseling licenses to residents of """ + STATES + """. Sound healing, breathwork, coaching and
    workshops are wellness and educational services, available anywhere, and are not psychotherapy,
    diagnosis or crisis care. If you are in crisis, call or text 988.</p>
    <div class="f-bottom">
      <div>&copy; """ + year + """ Rooted Resonance Coaching &amp; Therapy</div>
      <div>Become yourself. Transform everything.</div>
    </div>
  </div>
</footer>

"""
    js = """<script>
const nav=document.getElementById('nav');
addEventListener('scroll',()=>nav.classList.toggle('solid',scrollY>60));
const b=document.getElementById('burger'),nl=document.getElementById('navlinks');
if(b){b.addEventListener('click',()=>{const o=nl.classList.toggle('open');
  b.setAttribute('aria-expanded',o);b.textContent=o?'Close':'Menu';});}
const io=new IntersectionObserver(es=>es.forEach(e=>{
  if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}
}),{threshold:.1,rootMargin:'0px 0px -50px 0px'});
document.querySelectorAll('.rv').forEach((el,i)=>{el.style.transitionDelay=(i%4)*80+'ms';io.observe(el)});
</script>
</body>
</html>
"""
    return htmlpart + js

def phead(crumbs, eyebrow, h1, sub):
    c = ""
    if crumbs:
        parts=[]
        for i,(h,t) in enumerate(crumbs):
            parts.append(f'<a href="{h}">{t}</a>' if h else f'<span class="cur">{t}</span>')
        c = '<div class="crumb">'+'<span class="sep">/</span>'.join(parts)+'</div>'
    return f'''<header class="phead">
  <div class="glow"></div>
  <div class="wrap phead-in rv">
    {c}<div class="eyebrow">{eyebrow}</div>
    <h1>{h1}</h1>
    <p class="sub">{sub}</p>
  </div>
</header>
'''

def write(name, body):
    open(name,"w",encoding="utf-8").write(body)
    print("wrote", name)
