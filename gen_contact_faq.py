# -*- coding: utf-8 -*-
from build import *

# ---------------------------------------------------------------- CONTACT
b = head("Contact | " + SITE,
  "Reach out to Annie Memmott, LPC. Therapy for residents of Ohio, Arizona and Colorado. Sound healing, breathwork and workshops available anywhere.",
  active="contact.html")
b += phead(None, "Reach out", "Start with<br>a conversation.",
  "You do not have to know which offering you want, or be able to explain what is going on. A short exchange is enough to find the first door.")
b += '''<section class="sec" style="padding-top:16px">
  <div class="wrap form-grid">
    <div class="rv">
      <!-- FORM ENDPOINT: replace the action below with the live Formspree ID before launch.
           On Netlify or Cloudflare Pages this can instead use a native form handler. -->
      <form action="https://formspree.io/f/REPLACE_WITH_FORM_ID" method="POST">
        <div class="field">
          <label for="name">Your name</label>
          <input id="name" name="name" type="text" autocomplete="name" required>
        </div>
        <div class="field">
          <label for="email">Email</label>
          <input id="email" name="email" type="email" autocomplete="email" required>
        </div>
        <div class="field">
          <label for="state">Where are you located?</label>
          <select id="state" name="state" required>
            <option value="">Select one</option>
            <option>Ohio</option><option>Arizona</option><option>Colorado</option>
            <option>Somewhere else in the US</option><option>Outside the US</option>
          </select>
          <div class="hint">Therapy is available to residents of Ohio, Arizona and Colorado.
          Sound healing, breathwork and workshops are open to anyone.</div>
        </div>
        <div class="field">
          <label for="interest">What are you interested in?</label>
          <select id="interest" name="interest">
            <option>I am not sure yet</option>
            <option>Somatic Therapy</option>
            <option>Relational Therapy</option>
            <option>Sound Healing</option>
            <option>Breathwork</option>
            <option>Workshops</option>
            <option>Something else</option>
          </select>
        </div>
        <div class="notice">
          <strong>Please keep this general.</strong> Email is not a secure or confidential channel,
          so do not include clinical details, symptoms, diagnoses or anything private in this message.
          Tell me you would like to talk and we will find a better place for the rest.
        </div>
        <div class="field">
          <label for="message">Message</label>
          <textarea id="message" name="message" required
            placeholder="A sentence or two is plenty."></textarea>
        </div>
        <button type="submit" class="btn btn-solid">Send <span class="arw">&rarr;</span></button>
        <p class="hint" style="margin-top:18px">I usually reply within two business days.
        Submitting this form does not create a therapist and client relationship.</p>
      </form>
    </div>

    <aside class="rv">
      <div class="aside-card">
        <h3>In a crisis</h3>
        <p>This inbox is not monitored for emergencies. If you are in danger or thinking about
        harming yourself, please reach out now.</p>
        <ul>
          <li><span class="lbl">Call or text</span> 988 Suicide &amp; Crisis Lifeline</li>
          <li><span class="lbl">Text</span> HOME to 741741, Crisis Text Line</li>
          <li><span class="lbl">Emergency</span> 911 or your nearest emergency room</li>
          <li><span class="lbl">LGBTQ+ support</span> Trevor Project, 1-866-488-7386</li>
          <li><span class="lbl">Trans peer support</span> Trans Lifeline, 1-877-565-8860</li>
        </ul>
      </div>
      <div class="aside-card">
        <h3>Who can work with me</h3>
        <ul>
          <li><span class="lbl">Therapy</span> Residents of Ohio, Arizona and Colorado</li>
          <li><span class="lbl">Sound healing</span> Anyone</li>
          <li><span class="lbl">Breathwork</span> Anyone</li>
          <li><span class="lbl">Workshops</span> Anyone</li>
        </ul>
        <p style="margin-top:16px">Not sure which one fits? Say so. Sorting that out together is
        part of the work.</p>
      </div>
      <div class="aside-card">
        <h3>Rates</h3>
        <ul>
          <li><span class="lbl">Therapy</span> $150 self pay, most major insurances accepted</li>
          <li><span class="lbl">Sound healing</span> $60 for 60 minutes</li>
          <li><span class="lbl">Breathwork</span> $75 for 90 minutes</li>
          <li><span class="lbl">Workshops</span> Pricing varies</li>
        </ul>
        <p style="margin-top:16px"><a class="link" href="good-faith-estimate.html">Good Faith
        Estimate</a> information for self pay clients.</p>
      </div>
    </aside>
  </div>
</section>
'''
b += foot(); write("contact.html", b)

# ---------------------------------------------------------------- FAQ
def qa(q,a): return '<details class="qa"><summary>%s</summary><div class="a">%s</div></details>' % (q,a)

groups = [
("Getting started", [
 qa("I don't know what I need. Where do I start?",
    "<p>That is a completely normal place to begin, and it is the reason the framework exists. Have a "
    "look at the five stages and see which one sounds like where you are. If none of them do, or several "
    "do, reach out and say that. Sorting it out together is part of the work.</p>"),
 qa("What is the difference between the therapy and the other offerings?",
    "<p>Somatic and relational therapy are psychotherapy. I provide those as a Licensed Professional "
    "Counselor, and they are available to residents of Ohio, Arizona and Colorado.</p>"
    "<p>Sound healing, breathwork and workshops are wellness and educational services. They are not "
    "psychotherapy, they are not a substitute for it, and they are open to anyone regardless of where "
    "you live.</p>"),
 qa("Can we work together if I do not live in Ohio, Arizona or Colorado?",
    "<p>Yes, for sound healing, breathwork and workshops. Not for therapy. Counseling licenses are "
    "state by state, so therapy is limited to the states where I am licensed.</p>"),
 qa("What happens after I reach out?",
    "<p>I reply, usually within two business days. If it looks like a fit we set up a short "
    "conversation at no cost, and if it does not, I will say so and try to point you somewhere useful.</p>"),
]),
("Money", [
 qa("What do sessions cost?",
    "<ul><li><strong>Therapy</strong> $150 per session, self pay</li>"
    "<li><strong>Sound healing</strong> $60 for 60 minutes</li>"
    "<li><strong>Breathwork</strong> $75 for 90 minutes</li>"
    "<li><strong>Workshops</strong> pricing varies by format and length</li></ul>"),
 qa("Do you take insurance?",
    "<p>Yes, most major insurances are accepted for therapy. If you would like the full list of plans "
    "I am in network with, just ask and I will send it.</p>"
    "<p>Sound healing, breathwork and workshops are wellness services and are not billable to "
    "insurance.</p>"),
 qa("What is a Good Faith Estimate?",
    "<p>If you are uninsured or paying out of pocket, you have a right to an estimate of what your care "
    "will cost before you start. <a class='link' href='good-faith-estimate.html'>Full details are "
    "here</a>, and I will provide one in writing on request.</p>"),
 qa("What is your cancellation policy?",
    "<p>Please give at least 24 hours notice if you need to cancel or reschedule. Late cancellations "
    "and missed appointments may be charged the full session rate. Life happens, and if something "
    "genuinely unavoidable comes up, tell me.</p>"),
]),
("The work itself", [
 qa("I have done therapy before and it did not change anything.",
    "<p>You are describing the most common reason people find me. Understanding your patterns is a "
    "cognitive act, and it happens in a different part of you than the part running the pattern. "
    "Somatic work goes after the reflex where it lives rather than where it gets explained.</p>"),
 qa("Do I have to talk about my trauma?",
    "<p>No. You set the pace, and nothing gets opened before there is enough support to hold it. "
    "Sound healing in particular is built for the days when talking is not the way in.</p>"),
 qa("Is sound healing woo?",
    "<p>It is a wellness practice, and I describe it as exactly that rather than as treatment. What it "
    "reliably does is slow the nervous system down and bring attention back into the body without "
    "requiring you to narrate anything. Plenty of people arrive skeptical. That is fine.</p>"),
 qa("How long does this take?",
    "<p>Longer than anyone wants, and I am not willing to lie about that. In my experience change feels "
    "gradual for a long time and then, fairly suddenly, obvious.</p>"),
]),
("Working with me", [
 qa("Are you queer, poly and kink affirming?",
    "<p>Yes, and not in a passive way. I am a queer, ethically non monogamous, kink and sex positive "
    "therapist, and I have spent six years working with LGBTQIA+, neurodivergent and kinky communities. "
    "You will not need to explain your relationship structure or your identity from scratch.</p>"),
 qa("Do you work with people in relationships of any configuration?",
    "<p>Yes. Partnerships of any shape or number, and people navigating them on their own.</p>"),
 qa("Are sessions in person or online?",
    "<p>Therapy is offered by telehealth across Ohio, Arizona and Colorado. Sound healing is currently "
    "offered in person. Breathwork can be done remotely.</p>"),
 qa("Is this the right fit if I am in crisis?",
    "<p>If you are in immediate danger, please call or text 988, or go to your nearest emergency room. "
    "My practice is not set up for crisis response, and I would rather tell you that plainly than have "
    "you waiting on an email.</p>"),
]),
]

b = head("FAQ | " + SITE,
  "Common questions about therapy, sound healing, breathwork and workshops with Annie Memmott, LPC. Rates, insurance, availability by state, and what to expect.",
  active="faq.html")
b += phead(None, "Questions", "The things people<br>ask first.",
  "Rates, availability, what the work is actually like, and how to tell which offering fits.")
b += '<section class="sec" style="padding-top:16px"><div class="wrap col-c">'
for title, items in groups:
    b += '<div class="faq-group rv"><div class="eyebrow">%s</div>%s</div>' % (title, "".join(items))
b += '''<div class="scope-card rv" style="margin-top:20px">
      <div class="eyebrow">Still unsure</div>
      <h4 style="margin-bottom:14px">Ask me directly.</h4>
      <p style="color:var(--cream-dim);font-size:15px">If your question is not here, send it over.
      A short answer now is better than a wrong guess later.</p>
      <p style="margin-top:22px"><a href="contact.html" class="btn btn-solid">Reach out <span class="arw">&rarr;</span></a></p>
    </div>
  </div></section>
'''
b += foot(); write("faq.html", b)
