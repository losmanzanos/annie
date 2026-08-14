# -*- coding: utf-8 -*-
from build import *

NOTE = ('<div class="notice rv" style="margin-bottom:34px"><strong>For Annie, remove before launch.</strong> '
        'This is a working draft written for a solo practice website. Please read it against how you '
        'actually operate, and have your attorney or licensing boards review it before the site goes live.</div>')

# ---------------------------------------------------------------- PRIVACY
b = head("Privacy Policy | " + SITE,
  "How Rooted Resonance handles information collected through this website.", active="")
b += phead(None, "Privacy Policy", "Privacy Policy",
  "How information collected through this website is handled.")
b += '<section class="sec" style="padding-top:16px"><div class="wrap col-c prose">' + NOTE + '''
<p class="lede rv">This policy covers the website only. Information you share inside a therapy
session is protected separately and more strictly, under HIPAA and state law.</p>

<h2>What this website collects</h2>
<p><strong>Information you send me.</strong> If you use the contact form, I receive your name, email
address, the location and interest you select, and whatever you write in the message. That is
delivered to an email inbox and stored there.</p>
<p><strong>Basic analytics.</strong> I use Google Analytics to understand how many people visit and
which pages they read. This collects things like approximate location, browser type and pages
viewed. It is not used to identify you personally, and analytics is deliberately kept off any
booking or intake page.</p>
<p><strong>Server logs.</strong> The hosting provider records standard technical information such as
IP address and request time, which is used to keep the site running and secure.</p>

<h2>What this website does not collect</h2>
<ul>
  <li>No health information, diagnoses or clinical records</li>
  <li>No payment details. Payment is handled outside this website</li>
  <li>No advertising trackers, and no selling or renting of your information to anyone</li>
</ul>

<h2>Please do not send clinical details by email</h2>
<p>Email and web forms are not secure or confidential channels. The contact form is intended for
general inquiries only. Please do not include symptoms, diagnoses, clinical history or anything
private in it. Once we are working together, I will tell you which channels are appropriate for
what.</p>

<h2>How long information is kept</h2>
<p>Inquiries that do not become client relationships are kept only as long as needed to respond,
and are deleted periodically. Client records are governed by professional record keeping
requirements, not by this policy.</p>

<h2>Third parties</h2>
<p>This site relies on a small number of outside services: a hosting provider, a form delivery
service, Google Analytics, and Google Fonts for typography. Each has its own privacy practices.
No other party receives your information.</p>

<h2>Your choices</h2>
<ul>
  <li>You can ask what information I hold about you and request that it be deleted</li>
  <li>You can browse the site without using the contact form</li>
  <li>You can block analytics with a browser setting or extension, and the site will work normally</li>
  <li>Depending on where you live, you may have additional rights under state privacy law</li>
</ul>

<h2>Children</h2>
<p>This website is not directed at children under 13, and I do not knowingly collect information
from them.</p>

<h2>Changes</h2>
<p>If this policy changes, the updated date below will change with it.</p>

<h2>Contact</h2>
<p>Questions about this policy can go through the <a class="link" href="contact.html">contact
page</a>.</p>

<p class="updated">Last updated ''' + UPDATED + '''</p>
</div></section>
'''
b += foot(); write("privacy.html", b)

# ---------------------------------------------------------------- TERMS
b = head("Terms & Conditions | " + SITE,
  "Terms of use for the Rooted Resonance website.", active="")
b += phead(None, "Terms", "Terms &amp; Conditions",
  "The terms that apply to using this website.")
b += '<section class="sec" style="padding-top:16px"><div class="wrap col-c prose">' + NOTE + '''
<p class="lede rv">Using this website means you agree to what follows. If you do not, please do not
use the site.</p>

<h2>This website is not therapy</h2>
<p>Everything here is general information. Reading it, filling in the contact form, or exchanging
emails with me does not create a therapist and client relationship. That relationship begins only
when we have both agreed to it in writing and completed intake paperwork.</p>
<p>Nothing on this site is medical, psychological or legal advice, and it is not a substitute for
care from a qualified professional who knows your situation.</p>

<h2>In an emergency</h2>
<p>This website is not monitored, and neither is my inbox, for emergencies. If you are in crisis,
call or text 988, text HOME to 741741, or call 911.</p>

<h2>Therapy is limited by state</h2>
<p>Psychotherapy is provided only to residents of ''' + STATES + ''', where I hold a counseling
license. Sound healing, breathwork, coaching and workshops are wellness and educational services,
are not psychotherapy, and are available regardless of where you live.</p>

<h2>Booking, payment and cancellation</h2>
<p>Fees are listed on the <a class="link" href="faq.html">FAQ page</a> and are subject to change with
notice. Please give at least 24 hours notice to cancel or reschedule. Late cancellations and missed
appointments may be charged the full session rate.</p>

<h2>Content on this site</h2>
<p>The writing, design, images and marks on this site belong to Rooted Resonance Coaching &amp;
Therapy. You are welcome to share links and to quote briefly with attribution. Please do not
reproduce substantial portions or republish the material as your own.</p>

<h2>Links to other sites</h2>
<p>Where this site links elsewhere, those sites are not under my control and I am not responsible
for their content or their privacy practices.</p>

<h2>No guarantees of outcome</h2>
<p>Therapy, coaching and wellness work are collaborative, and results vary from person to person.
Nothing on this site promises a particular outcome.</p>

<h2>Limitation of liability</h2>
<p>To the extent permitted by law, Rooted Resonance Coaching &amp; Therapy is not liable for any
loss arising from use of this website or reliance on its general information.</p>

<h2>Governing law</h2>
<p>These terms are governed by the laws of the State of Colorado.</p>

<h2>Changes</h2>
<p>These terms may be updated from time to time. The date below reflects the current version.</p>

<p class="updated">Last updated ''' + UPDATED + '''</p>
</div></section>
'''
b += foot(); write("terms.html", b)

# ---------------------------------------------------------------- GOOD FAITH ESTIMATE
b = head("Good Faith Estimate | " + SITE,
  "Your right to a Good Faith Estimate of expected costs under the No Surprises Act, for uninsured and self pay clients of Rooted Resonance.", active="")
b += phead(None, "No Surprises Act", "Good Faith<br>Estimate",
  "If you are uninsured or paying out of pocket, you have the right to know what your care will cost before it begins.")
b += '<section class="sec" style="padding-top:16px"><div class="wrap col-c prose">' + NOTE + '''
<p class="lede rv">You have the right to receive a Good Faith Estimate explaining how much your care
will cost.</p>

<p>Under the No Surprises Act, health care providers must give people who are uninsured or who are
not using insurance an estimate of the expected charges for services.</p>

<h2>What you are entitled to</h2>
<ul>
  <li>A Good Faith Estimate in writing, at least one business day before your first appointment</li>
  <li>An estimate for the total expected cost of any services, including the anticipated number of
  sessions where that can reasonably be predicted</li>
  <li>An estimate on request, at any time, before you schedule anything</li>
  <li>A copy you can keep, and a copy saved in your record</li>
</ul>

<h2>Current self pay rates</h2>
<div class="facts rv" style="margin:26px 0 30px">
  <div class="fact"><div class="k">Therapy</div><div class="v">$150<small>Per session, self pay</small></div></div>
  <div class="fact"><div class="k">Sound Healing</div><div class="v">$60<small>60 minutes</small></div></div>
  <div class="fact"><div class="k">Breathwork</div><div class="v">$75<small>90 minutes</small></div></div>
  <div class="fact"><div class="k">Workshops</div><div class="v">Varies<small>By format</small></div></div>
</div>
<p>Therapy is the service the No Surprises Act applies to. Sound healing, breathwork and workshops
are wellness services rather than health care, and their pricing is listed here for transparency.</p>

<h2>How to request one</h2>
<p>Ask me at any point, in a session or through the <a class="link" href="contact.html">contact
page</a>, and I will provide it in writing. You do not need a reason, and asking does not commit
you to anything.</p>

<h2>If the bill is much higher than the estimate</h2>
<p>If you receive a bill that is at least $400 more than your Good Faith Estimate, you can dispute
it. You have 120 calendar days from the date of the bill to start a patient provider dispute
resolution process.</p>
<p>Keep a copy of your Good Faith Estimate. For questions or to learn more about your rights, visit
<a class="link" href="https://www.cms.gov/nosurprises" rel="noopener">cms.gov/nosurprises</a> or
call 1-800-985-3059.</p>

<h2>Download</h2>
<p>A printable copy is available here: <a class="link" href="media/good-faith-estimate.pdf">Good
Faith Estimate information (PDF)</a>.</p>

<p class="updated">Last updated ''' + UPDATED + '''</p>
</div></section>
'''
b += foot(); write("good-faith-estimate.html", b)
