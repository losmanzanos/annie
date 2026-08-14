# -*- coding: utf-8 -*-
from build import *

OFFERINGS = {
"somatic-therapy": dict(
  name="Somatic Therapy", icon="somatic", track="clin", stage="Stages II &amp; IV",
  stage_line="Understand &amp; Become",
  title="Somatic<br>Therapy",
  sub="Working with the adaptations that once protected you. Less talking about the problem, more feeling and experiencing.",
  desc="Somatic and relational therapy with Annie Memmott, LPC. Licensed in Ohio, Arizona and Colorado. Queer, kink and sex positive, neurodivergent affirming.",
  signs_h="You have understood things<br>for a long time.",
  signs_lead="You can name every pattern and still find yourself repeating it. That gap is not a failure of effort. Insight lives in one part of the brain and the pattern runs in another.",
  pull="Nothing you did to survive was wrong. It was for a different life than the one you have now.",
  checks=["You can explain your patterns better than most people can explain theirs.",
          "You have done therapy before, maybe more than once.",
          "You notice a feeling and immediately explain it away.",
          "Rest feels unsafe, or only allowed once everything is done.",
          "You are tired of talking about it and nothing shifting."],
  what_h="You do not have to arrive with it figured out.",
  steps=[("01","Arriving","A conversation about where you are now and what you are carrying. No exhaustive history required in the first session."),
         ("02","Tracking","We follow where the old strategies live in your body. Posture, breath, the reflex to brace."),
         ("03","Working","Slow, relational, paced by you. Nothing gets pushed open before there is enough safety to hold it."),
         ("04","Integrating","What changes gets practiced in real decisions and real relationships, not only in the room.")],
  facts=[("Rate","$150","Self pay"),("Insurance","Accepted","Most major plans"),
         ("Format","Telehealth","Across OH, AZ, CO"),("Framework","Stages II &amp; IV","Understand, Become")],
  pair=("relational-therapy.html","Relational Therapy","Many people move between the two. Individual work builds the ground, relational work is where it gets tested."),
  cta="Inquire about therapy", next_=("relational-therapy.html","Also clinical","Relational Therapy")),

"relational-therapy": dict(
  name="Relational Therapy", icon="relational", track="clin", stage="Stage V",
  stage_line="Relate",
  title="Relational<br>Therapy",
  sub="Ongoing support for relational and nervous system work, for people in and out of relationships of all kinds.",
  desc="Relational therapy with Annie Memmott, LPC. Support for relationships of every configuration. Licensed in Ohio, Arizona and Colorado. Queer, ethically non monogamous and kink affirming.",
  signs_h="Authenticity is easy alone.",
  signs_lead="It is in the presence of other people that the old pull to adapt comes back. Relational work is where self trust stops being a concept and becomes something you have actually done.",
  pull="Self trust is built in company, not in isolation.",
  checks=["You get very agreeable exactly when you are most upset.",
          "You read the room before you decide what you feel.",
          "Conflict feels like a threat to the whole relationship.",
          "You are navigating a structure that most therapists do not understand.",
          "You want closeness and it makes you want to run."],
  what_h="Relationships of every configuration.",
  steps=[("01","Naming","What is actually happening between you, including the parts that are hard to say out loud."),
         ("02","Seeing the pattern","Where each person's adaptations meet, and what happens when they collide."),
         ("03","Practicing","New responses tried in the room first, where there is support for them."),
         ("04","Carrying it out","The work is only real once it survives an ordinary Tuesday.")],
  facts=[("Rate","$150","Self pay"),("Insurance","Accepted","Most major plans"),
         ("Format","Telehealth","Across OH, AZ, CO"),("Framework","Stage V","Relate")],
  pair=("somatic-therapy.html","Somatic Therapy","Individual work on the adaptations underneath. Often the ground that relational work stands on."),
  cta="Inquire about therapy", next_=("sound-healing.html","When words are not the way in","Sound Healing")),

"sound-healing": dict(
  name="Sound Healing", icon="sound", track="well", stage="Stage III",
  stage_line="Reconnect",
  title="Sound<br>Healing",
  sub="Rest, regulation, and integration without needing to talk.",
  desc="Sound healing with Annie Memmott. Rest, regulation and integration without needing to talk. A wellness service, not psychotherapy, open to anyone.",
  signs_h="You have understood things<br>for a long time.",
  signs_lead="This is the stage where understanding finally drops out of your head and into your body. You lie down. Nothing is asked of you.",
  pull="Real change happened when I learned to listen to my body, understand my nervous system, and build a kinder more honest relationship with myself.",
  checks=["You can name what happened, but you do not feel different.",
          "Talking about it has started to feel like circling.",
          "Your body sends signals you have learned to override.",
          "You want to work on something without having to narrate it.",
          "You are curious and slightly skeptical, which is fine."],
  what_h="You do not need to know what you are doing.",
  steps=[("01","Arriving","A short conversation. Where you are today, what your body is holding. No history intake required."),
         ("02","Settling","You lie down, fully clothed, supported. Breath slows before anything else begins."),
         ("03","Sound","Bowls, voice and tone move through the room and through you. Sensation shows up where you had stopped noticing it."),
         ("04","Returning","Slow re-entry, water, and space to say anything that surfaced, or to say nothing and let it settle.")],
  facts=[("Rate","$60","Per session"),("Length","60 minutes","Arrive a few minutes early"),
         ("Type","Wellness","Not psychotherapy"),("Available","Anyone","No state restrictions")],
  pair=("breathwork.html","Breathwork","Where sound works on you, breath is something you do. Many people move between the two as the stage deepens."),
  cta="Book a sound session", next_=("breathwork.html","Also stage III","Breathwork")),

"breathwork": dict(
  name="Breathwork", icon="breath", track="well", stage="Stage III",
  stage_line="Reconnect",
  title="Breathwork",
  sub="Embodiment practice and nervous system education. Learning to listen to your body rather than think your way around it.",
  desc="Breathwork and nervous system education with Annie Memmott. A wellness and educational service, not psychotherapy, available anywhere.",
  signs_h="The most direct door<br>into the nervous system.",
  signs_lead="Where sound healing works on you, breath is something you do. It is the fastest route between knowing something and feeling it, and it gives you a practice you can take home.",
  pull="I kept repeating the patterns until I began focusing less on learning, or talking about my problems, and more on feeling and experiencing.",
  checks=["You want a practice you can use on your own, not only in a session.",
          "Your body stays braced even when nothing is wrong.",
          "You have tried meditation and found it hard to stay in your body.",
          "You want to understand what your nervous system is actually doing.",
          "You would rather do something than discuss something."],
  what_h="You do the work. I hold the room.",
  steps=[("01","Orienting","A little education first. What your nervous system is doing and why, in plain language."),
         ("02","Beginning","We start slow and small. There is no version of this where you get pushed."),
         ("03","The practice","Guided breathing, with room for whatever surfaces. Sensation, emotion, or nothing at all."),
         ("04","Taking it with you","You leave with something you can do at home, which is the point.")],
  facts=[("Rate","$75","Per session"),("Length","90 minutes","Includes orientation"),
         ("Type","Wellness","Not psychotherapy"),("Available","Anyone","No state restrictions")],
  pair=("sound-healing.html","Sound Healing","If doing feels like too much on a given day, sound asks nothing of you at all."),
  cta="Book breathwork", next_=("workshops.html","When you are ready for company","Workshops")),

"workshops": dict(
  name="Workshops", icon="workshops", track="well", stage="Stage V",
  stage_line="Relate",
  title="Workshops",
  sub="Authentic community. Where self trust gets practiced with other people in the room.",
  desc="Small group workshops with Annie Memmott. Breath, sound and honest contact in authentic community. A wellness offering, not group therapy. Waitlist open.",
  signs_h="Authenticity is easy alone.",
  signs_lead="Groups are where it gets tested, with all the old pull to adapt still alive in the room. That is exactly why they work.",
  pull="Who am I when I am no longer performing for belonging?",
  checks=["You do your best work and then lose it around other people.",
          "You want community that does not require performing.",
          "You are curious what this feels like alongside others.",
          "One to one work has taken you as far as it can for now.",
          "You want to practice, not just understand."],
  what_h="A practice space, not a performance.",
  steps=[("01","Arriving","Small group. Names, and only as much about yourself as you want to give."),
         ("02","Settling","Breath and sound first, so nobody has to talk their way into the room."),
         ("03","Contact","Structured practice with other people. Always opt in, never put on the spot."),
         ("04","Closing","Time to land before you go back out into the day.")],
  facts=[("Pricing","Varies","By format and length"),("Group","Small","Intentionally"),
         ("Type","Wellness","Not group therapy"),("Status","Waitlist","Open now")],
  pair=("sound-healing.html","Sound Healing","If a group feels like a lot right now, one to one is a reasonable place to start."),
  cta="Join the waitlist", next_=("index.html#framework","Back to the beginning","The Framework")),
}

for slug, o in OFFERINGS.items():
    facts = "".join(
      '<div class="fact"><div class="k">%s</div><div class="v">%s<small>%s</small></div></div>' % f
      for f in o["facts"])
    checks = "".join('<li><span class="mk"></span>%s</li>' % c for c in o["checks"])
    steps = "".join(
      '<div class="step rv"><div class="no">%s</div><h4>%s</h4><p>%s</p></div>' % s
      for s in o["steps"])
    scope = ("Somatic and relational therapy are psychotherapy, provided under Annie's counseling "
             "licenses to residents of Ohio, Arizona and Colorado."
             if o["track"]=="clin" else
             "This is a wellness and educational service. It is not psychotherapy, diagnosis or "
             "crisis care, and no therapeutic relationship is created by booking it. It is open to "
             "anyone regardless of where you live.")
    body = head("%s | %s" % (o["name"], SITE), o["desc"], active="services.html")
    body += phead([("services.html","Offerings"),(None,o["name"])],
                  "%s &nbsp;·&nbsp; %s" % (o["stage"], o["stage_line"]),
                  o["title"], o["sub"])
    body += '''<section class="sec alt">
  <div class="wrap" style="display:grid;grid-template-columns:1.1fr 1fr;gap:66px;align-items:start">
    <div class="rv">
      <div class="eyebrow">Is this where you are?</div>
      <h2 style="font-size:clamp(1.8rem,3.8vw,2.9rem);margin-top:16px">%s</h2>
      <p style="margin-top:24px;color:var(--cream-dim);max-width:480px">%s</p>
      <p style="font-family:var(--display);font-style:italic;font-size:1.32rem;color:var(--cream);margin-top:26px;padding-left:20px;border-left:1px solid var(--moss);line-height:1.45">%s</p>
    </div>
    <div class="rv"><ul class="checks">%s</ul></div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="rv" style="display:flex;align-items:flex-end;justify-content:space-between;gap:40px;flex-wrap:wrap;margin-bottom:38px">
      <div>%s<div class="eyebrow">The offering</div>
        <h2 style="font-size:clamp(2rem,4.4vw,3.2rem);margin-top:14px">%s</h2></div>
      <div style="max-width:330px">%s</div>
    </div>
    <div class="facts rv">%s</div>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <div class="sec-head rv">
      <div class="eyebrow">What it is like</div>
      <h2>%s</h2>
    </div>
    <div class="steps">%s</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="pair-card rv">
      <div>
        <div class="eyebrow">Often paired with</div>
        <h3>%s</h3>
        <p>%s</p>
      </div>
      <a href="%s" class="btn btn-ghost">Explore <span class="arw">&rarr;</span></a>
    </div>
  </div>
</section>

<section class="cta" id="book">
  <div class="wrap">
    <div class="eyebrow rv">Take the next step</div>
    <h2 class="rv">%s</h2>
    <p class="rv">If you are not sure whether this is the right fit, start with a conversation. No cost, no commitment.</p>
    <div class="row rv">
      <a href="contact.html" class="btn btn-solid">%s <span class="arw">&rarr;</span></a>
      <a href="contact.html" class="btn btn-ghost">Ask a question first</a>
    </div>
    <p class="rv" style="max-width:640px;margin:30px auto 0;font-size:12.5px;color:var(--cream-faint);line-height:1.65">%s</p>
  </div>
</section>

<section class="nextlink">
  <div class="wrap">
    <a href="%s"><div><div class="k">%s</div><div class="t">%s</div></div><span class="arw">&rarr;</span></a>
  </div>
</section>
''' % (o["signs_h"], o["signs_lead"], o["pull"], checks,
       badge(o["track"]), o["name"], o["sub"], facts,
       o["what_h"], steps,
       o["pair"][1], o["pair"][2], o["pair"][0],
       "Let the body lead." if o["track"]=="well" else "Start where you are.",
       o["cta"], scope,
       o["next_"][0], o["next_"][1], o["next_"][2])
    body += foot()
    write(slug + ".html", body)
