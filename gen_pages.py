# -*- coding: utf-8 -*-
from build import *

# ---------------------------------------------------------------- ABOUT
b = head("About Annie Memmott, LPC | " + SITE,
    "Annie Memmott is a queer, ethically non monogamous, kink and sex positive Licensed Professional Counselor in Ohio, Arizona and Colorado, serving LGBTQIA+, neurodivergent and kinky communities.",
    active="about.html")
b += phead(None, "Meet Annie", "I knew who I needed to be<br>for other people.",
    "Before I ever came to know how to be myself.")
b += '''<section class="sec" style="padding-top:20px">
  <div class="wrap col-c prose rv">
    <p>I have spent my life living out the patterns of adapting, people pleasing, and mastering the
    art of self abandonment. Not because I wanted to, but because that is what I thought I needed to
    do to survive.</p>
    <p>My own healing journey led me to a different question. Not "How do I become who I am supposed
    to be?" but "Who am I when I am no longer performing for belonging?" That question became the
    foundation for Rooted Resonance.</p>

    <h2>What actually changed things</h2>
    <p>I spent years intellectualizing my problems. I knew every trauma, every trigger, I could even
    tell you why I did the things I did, but none of that changed anything. I kept repeating the
    patterns until I began focusing less on learning, or talking about my problems, and more on
    feeling and experiencing.</p>
    <blockquote>Real change happened when I learned to listen to my body, understand my nervous
    system, and build a kinder more honest relationship with myself.</blockquote>

    <h2>Who I work with</h2>
    <p>I find myself working with people who have spent years adapting to keep relationships, avoid
    conflict, earn love, meet expectations, or all of the above. Most arrive feeling lost, worried
    about the future and unsure of their place in it. They are exhausted, burnt out from trying to
    fit in, and they don't know how to change it.</p>
    <p>I am a queer, ethically non monogamous, kink and sex positive Licensed Professional Counselor
    in the states of Ohio, Arizona, and Colorado, with a passion for working with people who feel
    like they don't know who they are and are in search of a deeper understanding of themselves.
    Over the past 6 years I have worked in private practice serving LGBTQIA+, neurodivergent, and
    kinky communities, assisting people in and out of relationships of all kinds to find who they
    are in the midst of feeling pressured to be like everyone else.</p>

    <h2>What I believe</h2>
    <p>I believe this is not about fixing yourself. It is about remembering who you have always been.</p>
    <p>At Rooted Resonance, I help people come home to themselves through therapy, sound healing,
    nervous system education, embodiment practices, and authentic community. My goal isn't to tell
    you who to be. It's to help you discover who you are beneath the roles, the expectations, and
    the survival strategies you have learned along the way.</p>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <div class="sec-head rv" style="text-align:center;max-width:640px;margin:0 auto 44px">
      <div class="eyebrow">Credentials</div>
      <h2>Licensed Professional Counselor</h2>
    </div>
    <div class="facts rv">
      <div class="fact"><div class="k">Licensure</div><div class="v">LPC<small>Ohio, Arizona, Colorado</small></div></div>
      <div class="fact"><div class="k">Private practice</div><div class="v">Since 2020<small>Six years</small></div></div>
      <div class="fact"><div class="k">Communities</div><div class="v">LGBTQIA+<small>Neurodivergent, kinky</small></div></div>
      <div class="fact"><div class="k">Approach</div><div class="v">Somatic<small>Nervous system informed</small></div></div>
    </div>
  </div>
</section>

<section class="cta">
  <div class="wrap">
    <div class="eyebrow rv">Ready for the next step?</div>
    <h2 class="rv">Become Yourself.<br><em>Transform Everything.</em></h2>
    <p class="rv">Whether you are navigating relationship challenges, rebuilding your sense of self,
    or longing to feel more at home in your own life, you are welcome here.</p>
    <div class="row rv">
      <a href="index.html#framework" class="btn btn-solid">Find where you are <span class="arw">&rarr;</span></a>
      <a href="contact.html" class="btn btn-ghost">Reach out</a>
    </div>
  </div>
</section>
'''
b += foot(); write("about.html", b)

# ---------------------------------------------------------------- SERVICES HUB
def card(href, icon, name, copy, track, price):
    return ('<a class="off" href="%s">%s<h4>%s</h4><p>%s</p><div class="price">%s</div>%s</a>'
            % (href, ICONS[icon], name, copy, price, badge(track)))

b = head("Offerings | " + SITE,
    "Somatic and relational therapy in Ohio, Arizona and Colorado. Sound healing, breathwork and workshops available nationwide. Every offering connects to a stage of the Rooted Resonance framework.",
    active="services.html")
b += phead(None, "What I Offer",
    "Every offering belongs to<br>a stage of the walk home.",
    "I help people come home to themselves through therapy, sound healing, nervous system education, embodiment practices, and authentic community.")
b += '''<section class="sec" style="padding-top:10px">
  <div class="wrap">
    <div class="track-head rv"><h3>Therapy</h3>
      <span class="avail">Licensed clinical work &nbsp;·&nbsp; OH, AZ, OH</span></div>
    <p class="track-sub rv">Psychotherapy provided under my Ohio, Arizona and Colorado counseling
    licenses, available to residents of those states. $150 self pay, and most major insurances accepted.</p>
    <div class="off-grid rv">
      %s
      %s
    </div>

    <div class="track-head rv"><h3>Coaching &amp; Wellness</h3>
      <span class="avail">Available nationwide</span></div>
    <p class="track-sub rv">Educational and experiential work. Not psychotherapy, and not limited by
    state lines.</p>
    <div class="off-grid three rv">
      %s
      %s
      %s
    </div>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <div class="scope-card rv">
      <div class="eyebrow">Scope of Practice</div>
      <h4>Two kinds of work, clearly separated.</h4>
      <div class="scope-rows">
        <div><span class="badge clin"><span class="pip"></span>Therapy</span>
          <p><strong>Somatic and relational therapy is psychotherapy.</strong> I provide it as a
          Licensed Professional Counselor to residents of Ohio, Arizona and Colorado. It can include
          assessment, treatment planning and clinical care.</p></div>
        <div><span class="badge well"><span class="pip"></span>Coaching &amp; Wellness</span>
          <p><strong>Sound healing, breathwork and workshops are not psychotherapy.</strong> They are
          educational and experiential practices supporting rest, body awareness and personal growth,
          and they are open to anyone, anywhere.</p></div>
      </div>
      <p class="scope-fine">Coaching and wellness services are not a substitute for mental health
      treatment, diagnosis or crisis care, and no therapeutic relationship is created by booking them.
      If you are unsure which one fits, start with a conversation. Sorting that out together is part
      of the work. In an emergency, call or text 988.</p>
    </div>
  </div>
</section>

<section class="cta">
  <div class="wrap">
    <div class="eyebrow rv">Not sure where to start?</div>
    <h2 class="rv">You don't have to<br>arrive <em>knowing.</em></h2>
    <p class="rv">The framework will tell you where you are, and each stage has a door.</p>
    <div class="row rv">
      <a href="index.html#framework" class="btn btn-solid">Find your stage <span class="arw">&rarr;</span></a>
      <a href="faq.html" class="btn btn-ghost">Read the FAQ</a>
    </div>
  </div>
</section>
''' % (
 card("somatic-therapy.html","somatic","Somatic Therapy","Working with the adaptations that once protected you. Less talking about the problem, more feeling and experiencing.","clin","$150 self pay"),
 card("relational-therapy.html","relational","Relational Therapy","Ongoing support for relational and nervous system work, for people in and out of relationships of all kinds.","clin","$150 self pay"),
 card("sound-healing.html","sound","Sound Healing","Rest, regulation, and integration without needing to talk.","well","$60 &nbsp;/&nbsp; 60 min"),
 card("breathwork.html","breath","Breathwork","Embodiment practice and nervous system education. Learning to listen to your body rather than think your way around it.","well","$75 &nbsp;/&nbsp; 90 min"),
 card("workshops.html","workshops","Workshops","Authentic community. Where self trust gets practiced with other people in the room.","well","Pricing varies"),
)
b = b.replace("OH, AZ, OH","OH, AZ, CO")
b += foot(); write("services.html", b)
