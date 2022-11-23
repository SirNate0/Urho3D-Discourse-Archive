slapin | 2017-05-05 19:53:55 UTC | #1

I just want to leave these 2 here:

http://gdcvault.com/play/1015683/Embracing-the-Dark-Art-of

http://www.gdcvault.com/play/1012410/Improving-AI-Decision-Modeling-Through

And this one pointed by @Sinoid
 
https://www.youtube.com/watch?v=OiFdlYY-GFA

Also I decided to link AI tool I make (for completeness):

https://youtu.be/wjoE8TTHt1Y

Also I need to mention that while Utility AI might improve your BT-based AI it will not make
it any simpler to comprehend. I myself find that Utility AI is much messier and harder to manage than
BT-based thing. So, to my mind, the best approach is to use both ways, implementing utility BT nodes and linking
both. I see utility AI as top-level AI which selects global behavior, but that behavior is explained by micro-behaviors
using BT. Trying to do all micro-behaviors using Utility AI would lead to code which an author himself will have hard time maintaining after a week.

-------------------------

Sinoid | 2017-05-04 03:48:20 UTC | #2

Utility AI is absurdly easy to implement. [The Bible](https://www.amazon.com/Behavioral-Mathematics-Game-AI-Applied/dp/1584506849).

Having written an extensive Utility AI implementation for Unity and integrated it with Node Canvas' behavior trees, I wouldn't consider mixing the two. Decision trees, sure - but decision trees exist implicitly even if they're not actually there. AI anything is such an atrocious scenario to be in and support that I abandoned it once I fully assessed just how bad "idiots" were going to be - far beyond worse than usual.

[Old repo with Unity C# ResponseCurve and Curve Visual Guide](https://github.com/JSandusky/UtilityBasedAIDocuments), I never released the entire Unity code outside of a few cases where dollars were thrown at me.

Once you've solved the *targeting* problem it's all cake from there. The convenient bit is that you can have *zones* attach behaviours and remove them on exit via clustered groups of actions (ActionSets, or rather TemporaryActionSets).

Also, Utility theory is just *Layers of Protection Analysis* inverted. Coming from the Chem safety industry that made it super trivial to me and I incorporated other principles such as ALARP and the like, Dual-Utility theory is sort of like ALARP but less robust.

---

Summary, it's all scalars, normalization, and curves.

-------------------------

slapin | 2017-05-04 08:52:06 UTC | #3

Well, the problem with Utility AI is ranking system - you have to choose what is more important to you at any given time,
also thou need to make sure that behavior actually runs as chosen without switching to something else.
The choosing thing is handled by BTs quite well. So I use utility to produce a set of interdependent parameters
and use BT to make actual decision, then use that decision(s) as additional system parameters.
As I have to run AI at multiple interdependent levels (where to go now, what animation group to play, etc.)
it is often really hard to keep this all structured under control, so I use BT as selection tool and
utility AI as parametrization (factoring out things).

The example - I use basic needs and declare things as safety, alignment, urge, agression. Then
I use BT to choose behavior, which does ranking automatically, as ranking of each parameter is too complicated
to handle. This BT just runs all global  behaviors which are to be run according to numbers, selecting one of
mutually exclusive ones in each group of behaviors - goals, internal, external.
Each global behavior have utility part with its own local parameters and BT part which selects micro-behaviors.

This way I have control on what is going on, but the structure becomes overly complicated too.

What do you mean by [b]targeting problem[/b]? Also how action sets mix with BTs or utility AI? I never
experienced the concept.

-------------------------

slapin | 2017-05-04 09:03:27 UTC | #4

Too bad the book is not available as ebook, Amazon won't sell it to me for some reason...

-------------------------

sabotage3d | 2017-05-04 12:34:46 UTC | #5

For me personally I found Behavior Trees in Unity quite easy to use compared to Utility and Fuzzy logic alternatives. You can also judge by the popularity of Behavior Designer that is the preferred choice. For Crowds simulations in the VFX industry is seems that the preferred one is Fuzzy logic, but I don't find it artist friendly.

-------------------------

slapin | 2017-05-04 12:41:47 UTC | #6

I never seen BTs in Unity, but I implemented them using the following tutorial:

https://www.youtube.com/watch?v=n4aREFb3SsU

-------------------------

slapin | 2017-05-04 12:42:53 UTC | #7

And as I'm not artist, BTs still are better than some chaotic structure.

-------------------------

slapin | 2017-05-04 14:11:05 UTC | #8

By the by, what is most common implementation of Sequence in BTs - the one which
continuously ticks last RUNNING child node, or the one, which ticks from first child until
one returns RUNNING, or FAILURE?

-------------------------

Sinoid | 2017-05-05 05:02:29 UTC | #9

[quote="slapin, post:3, topic:3092"]
need to make sure that behavior actually runs as chosen without switching to something else.
[/quote]

That's *hysteresis* and present in anything. Spring functions for biasing against rampant switching and actions that *lock* take care of that.

> What do you mean by targeting problem?

If you have an *Action* which also needs to select a target (such as a generic *MoveTo*) and the purpose of the action-instance and criteria are to select a place to get a "health-pack" to regain health, you need to enumerate the viable *targets* and choose which one to actually go for.

That's the target problem in a more elaborate case. The simple case is "I have a banker, billionaire, pregnant woman, child, man with stained clothes, and a bank teller - all in front of me, who do I shoot?" Though that sounds oddly specific I just enumerated in detail because minutae is problematic.

> Also how action sets mix with BTs or utility AI?

In NodeCanvas I implemented them as a custom node in the behaviour tree. Basically the node just ran an ActionSet (which in my implementation is a collection of actions that are categorically equivalent, "war is murder with a different name" sort of clustering). 

It only worked because NodeCanvas is not stateful and is actually just a decision-tree and not a behaviour tree. Most behaviour trees are just manually authored decision trees anyways. UE's is the only one that stands out to me as, "that's what should be called a behaviour tree." If it can't deal with *events* it's not a behaviour tree, it's a decision tree and you'd probably have been happier with an Excel spreadsheet and running ID3 on it.

> Too bad the book is not available as ebook, Amazon won't sell it to me for some reason...

Don't worry, it's 75% historical filler, that historical filler is still meaningful but you could probably read the TOC and google to get the gist of most of the book. Dave Mark does write that filler really well though in a "hammer it into your head" fashion.

Between the two talks you already linked and [Building a Better Centaur](https://www.youtube.com/watch?v=OiFdlYY-GFA) everything you really need to know is already out there.

---

> By the by, what is most common implementation of Sequence in BTs - the one which
continuously ticks last RUNNING child node, or the one, which ticks from first child until
one returns RUNNING, or FAILURE?

There are no conventions. Zero.

-------------------------

slapin | 2017-05-05 11:41:39 UTC | #10

Well, digging into matter some more and more questions arise :)

As I uderstand, to prevent accidental switching of actions, carefully crafted scoring system is used.
Some actions get min score which is higher than other actions max score, which makes some
things to be always selected if needed.
When one selected to 'go north' he will not accidentally go south because it is implemented as on/off switch
so another decision is required to do this, is it correct?

I see that the scoring (ranking) system looks a lot like decision/behavior tree and could be represented by
a tree, I wonder if anybody did that... Or probably I did not understand the concept.

Anyway I implement utility and traditional AI by using "utility" nodes in BT. Utility node does some black-box thing
if selected by BT which is configured elsewhere (mostly in code). An idea of making this better is yet to cook in my brain...

-------------------------

slapin | 2017-05-05 19:59:46 UTC | #11

Linked video of my current progress with BT editor. Sorry for hijacking the topic,
but I hope it is at place. I still have more questions than answers.

I still don't understand how Utility AI scoring system is supposed to work.
Like I need to play 3 sequences of animation depending on what target is acquired,
i.e. got to vehicle, need to open door,enter and close door. Or if the target is chair,
sit on it. But walk to target is the same for both cases. How to implement such choices with Utility AI
so that the sequience is not broken in illogical way?

-------------------------

Sinoid | 2017-05-07 03:49:07 UTC | #12

> As I uderstand, to prevent accidental switching of actions, carefully crafted scoring system is used.

Scoring system doesn't matter, that's still *hysteresis*. You have to bias (implement inertia of some kind) and lock to prevent switching into new actions, not craft scoring - that would be an endless task. An *Action* should be locking itself as current until it is complete, an action sufficiently surpasses it for suitability, or aggregate emergency *Criteria* have been met.

[Inertia hystereris handling at line 32](https://hastebin.com/otucegeqac.cs), emergency exits are elsewhere, but that's pretty trite.

> When one selected to 'go north' he will not accidentally go south because it is implemented as on/off switch
so another decision is required to do this, is it correct?

That doesn't even sound related, that's just bad *Action* design - I think you're thinking too micro, North/South don't matter it's "Where do I have to go?" -> "Do I want to go there?" -> "I have a path, now I will follow it". North/South is neural net thinking. The door problem you state is the same deal.

> I see that the scoring (ranking) system looks a lot like decision/behavior tree and could be represented by
a tree, I wonder if anybody did that... Or probably I did not understand the concept.

If your "utility" setup isn't at least sort of similar (or conceptually mappable) to the pseudocode below, then you probably don't get it (note this is raw, and not "fact" just if it doesn't come as "well yeah" or "duh" then you don't get it):

    struct Criteria {
        ResponseCurve weightCurve_;
        virtual float GetNormalizedValue() = 0;
        float GetCriteriaWeight();
    }

    struct Action {
        Criteria[] selectionCriteria;
        float GetWeight(float weightToBeat, ...);
    }
   
    struct ActionSet {
        int tag_;
        Action[] actions_;
        ActionResult GetBestAction(float weightToBeat, ...);
    }

*Criteria* is the fumbling point usually. Getting that part right is useful because it can be reused by pretty much anything, such as being used for predicates in decision/behaviour trees, FSMs, ID3 code-generators, etc. [Minimalist "Distance From" Criteria](https://hastebin.com/debuxibube.cs) from my Unity implementation (C++ implementation is nasty).

> Or if the target is chair, sit on it.

Your objective is to sit: you find an unused chair to sit on, you go to the chair, and you sit on it ... and basically all of your *ActionSets* and *Actions* become invalid except the one to leave the chair (or play the flute, sitting down - whatever madness occurs while seated).

> But walk to target is the same for both cases.

That's not an action, that something an action may do to fulfill dependencies. *MeleeAttack* must walk into range to even complete, that's a fundamental part of the action, once in range it can perform it's final execution. It's one action, "I'm going to walk up to him and bash him on the head."

>  How to implement such choices with Utility AI so that the sequience is not broken in illogical way?

You don't. That's not what it's for. The action may be an atomic action, or may be a complete sequence. You're thinking like neural-nets/decision-trees. Utility was for selecting an action, everything about how long to continue with that action is outside of it, you could just lock on any single action until it is complete - an *Action* may be as trite as shooting a target or as complicated as walking across half of a dungeon to activate a shrine. 

Switching actions is only for responsiveness to environmental changes, not a matter of sequence - though it could be if you wrote it that way ... that'd be "fun" to debug.

-------------------------

slapin | 2017-05-07 06:21:56 UTC | #13

Thank you so much for explanation!
Now I need some time to think and redesign...

But I like that I choose Utility AI as top-level behavior selection, that was a right thing to do.
The only problem is that I use BTs as actions for Utility AI and these sometimes turn into nightmare.
I use BTs where it is important to do things in order and for micro-things (which can be described by single animation or motion). Also criteria for action completion is on BT too.

As I understand, for Utility AI we go for action selection only after all actions are complete, which I could not grasp,
now I understand it, BTs and FSMs are just broke my brain enough for making understanding that a difficult task..

-------------------------

slapin | 2017-05-07 15:03:32 UTC | #14

Well, I finally made my AI system work so I dropped fixed code AI finally. That is good progress,
there are many steps which I can do faster now and most steps are not slower to do.

What I'm currently concerned about is how do they implement external behaviors. I.E. NPC roams around and arrives at zone with benches, looks for a bench, sits there and smokes. So the looking for a bench behavior is
"bench zone" behavior and sitting and smoking is "bench" behavior. (usually zone setup is more complicated,
like awareness zone, engage zone, etc.). So how do they find which zone NPC belongs to? (physics will kill CPU
if used like that), how do they activate the behavior so that it replaces default behavior?
I have very rough understanding on how to do this with BTs but no idea on how this might be done with utility AI...

-------------------------

Sinoid | 2017-05-09 03:14:37 UTC | #15

> (usually zone setup is more complicated,
like awareness zone, engage zone, etc.). So how do they find which zone NPC belongs to? (physics will kill CPU
if used like that)

That's the domain of acceleration structures, it's technically unrelated. But if you have fewer than 100 zones then just iterating through them per agent is no big deal for a few agents. When you have more zones or more agents you have to look at BVHs, kd-trees, quad-trees, and octrees to store the zones. That's a data structure and query problem.

> I.E. NPC roams around and arrives at zone with benches, looks for a bench, sits there and smokes.

So in that pseudo-code I posted before you'll see the *ActionSet* and you'll hear Dave Mark talk about the same thing in the "Building a Better Centaur" talk. When the agent enters a zone you can attach a temporary action set to the agent (reference counted likely, [Unity code for 'TemporaryActionSet'](https://hastebin.com/lujunopeqo.cs) - not a lot going on there). This appends an entire collection of possible actions (and their criteria/considerations) to those that are possible.

1) Assuming the agent has a nicotine addiction and the only place to smoke is on a bench, the action to "go sit on a bench" can have a criteria which exceeds the usual 0-1 normalized range of weight when the agent is suffering withdrawal so the agent will favor sitting on a bench (a non-smoker would always return 1.0 to keep the other criteria for sitting on a bench ... this is an addiction so exceeding 1.0 is sane).

2) The action to "smoke while sitting on a bench" has a criteria that first requires the agent is sitting on a bench, if that passes then we can check the next criteria which is that they need a nicotine fix and weight their need to smoke on that bench. It passes so the agent smokes (there's not much else they can probably do from a bench).

3) There is no right answer for the "smoking action," likely you'd just decrease nicotine desire as long as the smoking action is running, so that eventually a different action would become more important because all of the nicotine related criteria would fall so low that other actions would take priority. This is an addiction/personality scenario so it could get pretty interesting.

Smoking is actually a good scenario to use for examples, it has other cases than just smoking on a bench such as no-smoking zones and the needs of other agents.

-------------------------

