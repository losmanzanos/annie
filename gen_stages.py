# -*- coding: utf-8 -*-
from build import *

STAGES = [
 dict(slug="awaken", num="I", name="Awaken",
   sub="Something doesn't feel right, and that's where your journey begins.",
   desc="Awaken is the first stage of the Rooted Resonance framework. Most people don't begin healing because they wake up inspired. They begin because something no longer fits.",
   intro=["Most people don't begin healing because they wake up one morning feeling inspired. They begin because something no longer fits.",
          "You keep trying to change things, but it never feels like enough. You are exhausted from holding it all together. You spend your time exhausting yourself for others, and never knowing how to slow down for yourself. Throughout your days and nights you have held a quiet sense that there has to be another way to live.",
          "You don't need to know exactly what's wrong to begin. You only need the willingness to become curious."],
   pull="Awakening isn't about getting to the answer. It's about allowing yourself to ask new questions.",
   happening=["Before we ever know there is a problem, when things feel like normal, change seems unnecessary.",
              "Many of the patterns that helped you survive now feel limiting. Over time your nervous system learned how to adapt to your environment in order to create safety, belonging and acceptance.",
              "These patterns and adaptations were intelligent. They helped you navigate the world with the resources you had.",
              "The goal is not to judge the patterns or how you got here. The goal is to learn about them, get curious, and seek understanding."],
   together=["Together, we'll slow down enough to notice what your mind and body have been trying to communicate. Through compassionate exploration, we'll begin identifying the patterns that no longer serve you while honoring the ways they've protected you."],
   offers=[("contact.html","A Conversation",None,"No cost and no commitment. Say out loud what you have been carrying, and we will find the first door together.")],
   nxt=("understand.html","Continue the journey","Understand")),

 dict(slug="understand", num="II", name="Understand",
   sub="Recognize the adaptations that once protected you.",
   desc="Understand is the second stage of the Rooted Resonance framework. As awareness grows, so does compassion. Somatic therapy with Annie Memmott, LPC.",
   intro=["As awareness grows, so does compassion.",
          "What once felt like a reflex suddenly gets pulled into the light. The patterns that once defined you, people pleaser, hyperindependent, the person who never says no, now become known as strategies for survival.",
          "They developed as adaptations to your relationships, environment, and experiences."],
   pull="Instead of asking, what's wrong with me, you begin asking, what was I trying to protect?",
   happening=["Your nervous system is beginning to separate the past from the present. As you understand how your adaptations formed, you gain the freedom to choose rather than simply react.",
              "Insight creates possibilities, but lasting change also requires embodiment."],
   together=["We will explore all the things that keep you feeling stuck. Whether it's relationship patterns, feeling like you don't know who you are, or deep generational beliefs that have been unconsciously leading your life.",
             "Here we build understanding without shame, and without treating you as something to be fixed."],
   offers=[("somatic-therapy.html","Somatic Therapy","clin","Individual clinical work tracing where the old strategies live in the body."),
           ("blog-adaptation.html","Journal: I spent years intellectualizing my problems",None,"Annie on why insight alone did not change anything, and what finally did.")],
   nxt=("reconnect.html","Continue the journey","Reconnect")),

 dict(slug="reconnect", num="III", name="Reconnect",
   sub="Learn to trust your body and nervous system.",
   desc="Reconnect is the third stage of the Rooted Resonance framework. Sound healing, breathwork and nervous system education. Available nationwide.",
   intro=["Connection with your body begins with experiencing that which we have learned to disconnect from. Recovery from survival states means traveling away from the mind and allowing the body to have a voice.",
          "Reconnection is the practice of returning. Learning to breathe. To pause. To notice."],
   pull="To trust that your body carries wisdom, rather than something to overcome.",
   happening=["As you begin to build the bridge of connection between you and your body, things begin to feel more regulated. Suddenly the highs don't feel so high and the lows don't feel so low.",
              "The body becomes a place to inhabit rather than avoid. Healing begins to shift from intellectual understanding into lived experience."],
   together=["In this stage we are all about the body. The tools offered here have less to do with verbal processing and more to do with somatic experience.",
             "Through breathwork, nervous system education, sound healing, mindfulness, and embodied practices, you'll develop a deeper relationship with yourself from the inside out."],
   offers=[("sound-healing.html","Sound Healing","well","Rest, regulation, and integration without needing to talk. $60 for 60 minutes."),
           ("breathwork.html","Breathwork","well","Embodiment practice and nervous system education. $75 for 90 minutes.")],
   nxt=("become.html","Continue the journey","Become")),

 dict(slug="become", num="IV", name="Become",
   sub="Discover who you are beneath old patterns.",
   desc="Become is the fourth stage of the Rooted Resonance framework. Less about fixing yourself, more about discovering yourself.",
   intro=["This stage is less about fixing yourself and more about discovering yourself.",
          "What do you value? What brings you joy? What boundaries feel true? What kind of life feels aligned with who you are, not who you've been expected to be?",
          "These questions, and more, begin to outline the ways in which you form your identity."],
   pull="This is not about fixing yourself. It is about remembering who you have always been.",
   happening=["After years of living your life in adaptation or survival, you're beginning to organize and arrange your life around authenticity. Your decisions become rooted in a sense of self trust."],
   together=["Through therapy, a community of your choosing, and other offerings like workshops and retreats, we'll create space for you to cultivate a life that feels deeply your own."],
   offers=[("somatic-therapy.html","Somatic Therapy","clin","The same container, different work. Practising the true self in real decisions and real relationships."),
           ("workshops.html","Workshops","well","Authentic community, where what you are becoming gets practised alongside others.")],
   nxt=("relate.html","Continue the journey","Relate")),

 dict(slug="relate", num="V", name="Relate",
   sub="Create relationships rooted in authenticity and choice.",
   desc="Relate is the fifth stage of the Rooted Resonance framework. Relational therapy and community for relationships of every configuration.",
   intro=["This is where we put everything to the test. Healing doesn't end with knowing a more authentic version of you. It continues as you bring that authentic self into connection with others.",
          "Relationships are the fertile ground where you practice honesty, setting boundaries, vulnerability, and mutual care.",
          "This doesn't mean that relationships are effortless and easy."],
   pull="It means that after years of leaving yourself behind, you no longer have to abandon yourself to feel like you belong.",
   happening=["As your relationship with yourself strengthens, your relationships with others begin to change. You're more able to respond in ways that honor your needs rather than reacting from old survival strategies."],
   together=["Whether through relationship therapy, coaching, community circles, or ongoing support, we'll continue integrating what you've discovered into your everyday life and relationships."],
   offers=[("relational-therapy.html","Relational Therapy","clin","For partnerships of any shape or number, and for the people navigating them solo."),
           ("workshops.html","Workshops","well","Community circles and group practice. Waitlist open.")],
   nxt=("index.html#framework","Back to the start","The Framework")),
]

RAIL = ["awaken","understand","reconnect","become","relate"]
NAMES = {"awaken":"Awaken","understand":"Understand","reconnect":"Reconnect",
         "become":"Become","relate":"Relate"}
SUBS  = {"awaken":"Notice","understand":"Recognize","reconnect":"Trust",
         "become":"Discover","relate":"Choose"}
ROMAN = {"awaken":"I","understand":"II","reconnect":"III","become":"IV","relate":"V"}

for s in STAGES:
    rail = ""
    for slug in RAIL:
        on = " on" if slug == s["slug"] else ""
        rail += ('<a class="st%s" href="%s.html"><span class="node">%s</span>'
                 '<span class="nm">%s</span><span class="sv">%s</span></a>'
                 % (on, slug, ROMAN[slug], NAMES[slug], SUBS[slug]))
    offers = ""
    for href, name, track, copy in s["offers"]:
        offers += ('<a class="off" href="%s">%s<h4>%s</h4><p>%s</p></a>'
                   % (href, (badge(track) + "<br>") if track else "", name, copy))
    ncols = " three" if len(s["offers"]) > 2 else ""
    b  = head("%s | The Rooted Resonance Framework" % s["name"], s["desc"], active="index.html#framework")
    b += phead([("index.html#framework","The Framework"),(None,s["name"])],
               "Stage %s of Five" % s["num"], s["name"], s["sub"])
    b += '<section class="stage-rail-wrap"><div class="wrap"><div class="stage-rail">%s</div></div></section>\n' % rail
    b += '<section class="sec"><div class="wrap col-c prose rv">'
    b += "".join("<p>%s</p>" % p for p in s["intro"])
    b += '<blockquote>%s</blockquote>' % s["pull"]
    b += '<h2>What is happening</h2>' + "".join("<p>%s</p>" % p for p in s["happening"])
    b += '<h2>How we work together</h2>' + "".join("<p>%s</p>" % p for p in s["together"])
    b += '</div></section>\n'
    b += '''<section class="sec alt">
  <div class="wrap">
    <div class="sec-head rv"><div class="eyebrow">What supports you here</div>
      <h2>Where this stage leads.</h2></div>
    <div class="off-grid%s rv">%s</div>
  </div>
</section>

<section class="nextlink">
  <div class="wrap"><a href="%s"><div><div class="k">%s</div><div class="t">%s</div></div>
  <span class="arw">&rarr;</span></a></div>
</section>
''' % (ncols, offers, s["nxt"][0], s["nxt"][1], s["nxt"][2])
    b += foot()
    write(s["slug"] + ".html", b)
