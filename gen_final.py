# -*- coding: utf-8 -*-
from build import *

# ------------------------------------------------ ACCESSIBILITY STATEMENT
b = head("Accessibility Statement | " + SITE,
  "Rooted Resonance is committed to making this website usable by everyone, including people with disabilities. WCAG 2.1 AA is our standard.", active="")
b += phead(None, "Accessibility", "Accessibility<br>Statement",
  "Rooted Resonance is committed to ensuring that our website and services are accessible to everyone, including people with disabilities.")
b += '''<section class="sec" style="padding-top:16px"><div class="wrap col-c prose">
<p class="lede rv">We believe in creating an inclusive and supportive experience for all visitors
and clients.</p>

<h2>Our commitment</h2>
<ul>
  <li>We aim to follow the Web Content Accessibility Guidelines (WCAG) 2.1 at the AA level as our
  standard for accessibility.</li>
  <li>We continuously review this website to identify and fix accessibility barriers.</li>
  <li>We strive to provide alternative ways to access content, such as transcripts for audio
  material where possible.</li>
</ul>
<p>Accessibility is an ongoing effort. We regularly update the site to improve functionality,
readability, and compatibility with assistive technologies.</p>

<h2>What has been done</h2>
<ul>
  <li>Semantic headings and a logical content order on every page</li>
  <li>Alternative text on images, and decorative graphics hidden from screen readers</li>
  <li>Colour combinations checked against WCAG AA contrast requirements</li>
  <li>Full keyboard navigation, including a skip link to the main content</li>
  <li>Motion reduced, and all animation disabled automatically for anyone whose device requests
  reduced motion</li>
  <li>Form fields with visible, associated labels rather than placeholder text alone</li>
  <li>Text that can be resized without breaking the layout</li>
</ul>

<h2>Known limitations</h2>
<p>The homepage includes a short background video. It is muted, decorative, carries no information,
and is switched off automatically if your device requests reduced motion.</p>

<h2>Requests, issues and suggestions</h2>
<p>We welcome feedback. If you encounter a barrier on this website, or if you need information in
another format, please contact our accessibility coordinator:</p>
<ul>
  <li><strong>Annie Memmott</strong></li>
  <li>Phone <a class="link" href="tel:+15134978595">513-497-8595</a></li>
  <li>Email <a class="link" href="mailto:rebelhealerannie@gmail.com">rebelhealerannie@gmail.com</a></li>
</ul>
<p>We will do our best to respond promptly and provide reasonable accommodations.</p>

<p class="updated">Last updated ''' + UPDATED + '''</p>
</div></section>
'''
b += foot(); write("accessibility.html", b)
