Eugene | 2017-11-09 18:51:08 UTC | #1

**I propose to remove the following items from Contribution Checklist**

> For all code (classes, functions) for which it makes sense, both AngelScript and Lua bindings should exist. Refer to the existing bindings and the scripting documentation for specific conventions, for example the use of properties in AngelScript instead of setters / getters where possible, or Lua bindings providing both functions and properties.

> Unless impossible due to missing bindings (see above) new examples should be implemented in all of C++, AngelScript and Lua.

I _know_ that these rules are (were) important to keep Urho3D API consistent among C++, AS and Lua.

_However._

Let's be honest with ourselves. Everybody _hates_ writing bindings.

For Lua you should locate some files outside the project and add things, for AngelScript you should write binding string properly, and if you are not careful enough, everything will explode. You should either be very attentive or test all bindings manually. Perfectly both.

To make these samples you should recall "foreign" script language and spend x2-x3-x5 time to port your C++ code.

**This actually draws Urho into stagnation**. It's much easier for many people to maintain their own diverging forks than to follow these rules and make PRs.

I think that engine developement is more important than script API completeness.

So I suggest to drop these requrements and let code flow.

Of course, existing bindings shall be maintainted.

Of course, it is _appreciated_ to implement script bindings or even port samples.

Script bindings could be implemented in separate PR or requested in issue and implemented on demand, like any other suggestion.

If there is a volunteer who is ready to write bindings, that's perfect.

In summary...

**Pros:**

- More PRs from people who don't need bindings and don't like writing bindings
- Stimulate people who actually _need_ bindings to make PRs and develop the project.
- No time wasted for bindings that nobody actually use.

**Cons:**

- Script bindings become a kind of downstream projects behind the head.

-------------------------

1vanK | 2017-11-10 01:22:50 UTC | #2

Personally, I would throw out LUA from engine (but keep Angel Script), but for sure there are people who like LUA. It may be necessary to conduct a survey to find out how many people use LUA in their practice (personally I often use AngelScript for small test programs).

-------------------------

weitjong | 2017-11-10 01:39:41 UTC | #3

Our community is already small as it is. I think we should keep those LUA users by outside. Thank you. In fact so far we don't treat them as second class citizen. The way we have setup currently has made the script binding to require a small amount of work. Adding a few line in the pkg for LUA or the *API.cpp for AS is hardly time-consuming. We should also value maintainers more than contributors. A contributor would just drop the code here and expect the maintainer to keep them from rotting. Now if the would be contributor is already too lazy to maintain the would be contributed code to be compatible with all our supported APIs then there is little hope to think or ask the same person would still be here to maintain or fix the contributed code in the future. 

So, I would vote against this move.

-------------------------

Eugene | 2017-11-10 06:54:08 UTC | #4

[quote="weitjong, post:3, topic:3722"]
Adding a few line in the pkg for LUA or the *API.cpp for AS is hardly time-consuming.
[/quote]

When you tried to do it last time on your own? For some reason I think that if you were writing script binding regularly, you would have other opinion.

If contributor add two simple functions, it's quite easy to keep binding up-to-date.

If contributor add two new classes with hundreds of functions it may take whole day or two to make bindings and port samples. Especially if functions are not easily bound to scripts via standard binders.

Every time when contributor change any header, he has to go to both bindings and fix them. Then he has to fix both samples and ensure that they are running.

[quote="weitjong, post:3, topic:3722"]
Now if the would be contributor is already too lazy to maintain the would be contributed code to be compatible with all our supported APIs then there is little hope to think or ask the same person would still be here to maintain or fix the contributed code in the future
[/quote]

Such rules doesn't filter away lazy people who will not maintain their own code in the future.
Such rules filter away people who don't need Lua & AS bindings and don't want to spend time to maintain it.

I understand that personaly I will not push into Urho some code just because personally I don't need bindings for it. And I'm not the only person who avoids contributing because of this reason.

Our current rules literally push people away from contributing anything big.
At the same time, our current rules forcibly increase scope of maintenance _even if nobody really need it_.

PS. Any updates on Community Modules?

-------------------------

weitjong | 2017-11-10 07:59:14 UTC | #5

This is absurd. I don't believe I have to show you what I have done or have not done to proof my point. I also don't believe doing the after the fact binding would make the contribution rate any faster. On the contrary I believe it will make developer to take shortcut and may allow them to make a bad design decision and only to find out later when the actual binding is made. Those rules are made by Lasse then when he did most the things and I have never heard him whining.

-------------------------

Eugene | 2017-11-10 08:41:48 UTC | #6

[quote="weitjong, post:5, topic:3722"]
I don’t believe I have to show you what I have done or have not done to proof my point.
[/quote]
I don't ask you to show anything to proof.
I just wonder if you tried to maintain bindings and _especially_ script samples on your own. To be sure that you understand the amount of work. Especially for a contributor _who don't know Lua and AS_.

[quote="weitjong, post:5, topic:3722"]
I also don’t believe doing the after the fact binding would make the contribution rate any faster.
[/quote]
So I pin my hopes on community repos. It may become nice sandbox to try less strict contribution rules and analyze results.

[quote="weitjong, post:5, topic:3722"]
On the contrary I believe it will make developer to take shortcut and may allow them to make a bad design decision and only to find out later when the actual binding is made
[/quote]
Huh... Didn't think about this point.
What about bad _binding_ design (or even buggy binding) by people who are C++ developers and never used neither Lua nor AS?

-------------------------

weitjong | 2017-11-10 09:00:10 UTC | #7

You forget about there is still reviewer who approve or reject the PR and that our CI is non-forgiving. A bad AS binding would crash the Urho3DPlayer more often than not. And yes, I have done some bindings works in the past, so I know exactly what it entails.

-------------------------

cadaver | 2017-11-10 09:12:24 UTC | #8

Just want to chime in that by me (although I don't have official say as such anymore) it's fine that you change the contribution rules. It'd be good if you then communicate clearly that the script subsystems have been made, to a degree, second class citizens, because that is the inevitable end result. 

I certainly noticed Urho is to a degree a "matrix of death" ie. platforms, subsystems, script APIs. 

Typically script API binding troubles are related to containers, and you can note it in the C++ API sometimes, e.g. the pattern of providing indexed setter and getter functions. You would probably be able to make a smarter C++ API overall if you didn't need to think of bindings at all.

-------------------------

rku | 2017-11-10 09:27:34 UTC | #9

Bindings are a big point of pain. When i make a change and think should i submit a PR first thing i consider is if i will have to write bindings. More often than not answer is "yes", and it simply is easier to keep changes to myself instead of trying to upstream them. Imagine commercial user which would be willing to contribute their changes upstream. They already donate their work even if they are not required to. It is not exactly fair to ask them to maintain bindings as well, if they do not use them (and most likely they do not).

Bindings themselves are more of a toy thing rather than serious tool. Lua may be fine for scripting some scene logic, but noone in their sane mind will try to implement advanced features in scripting languages in actual product that ships. With that said - limited set of bindings make more sense as that would be enough for scripting scene logic alone and reduce maintenance burden.

We also had a lengthy discussion what to do with Atomic after Josh left the project. One very appealing option was to turn Atomic into into Urho3D+Addons, where addons part would be tools and c# bindings. Ultimately we deemed it not really possible because of maintenance burden Urho3D is carrying. We concluded that going this way would only be possible if we forked Urho3D and simply dropped all the excess stuff so we do not need to maintain it. That means fragmentation and it never is good, but sometimes inevitable.

If we want project to thrive then clear priorities should be set. There isnt exactly that many contributors to spare. Ask yourselves what is more important: handful of amateur users who can not write c++ code and thus depend on scripting languages, or handful of contributors?

My bottom line - bindings are good when they are auto-generated, and contributors are way more valuable than users.

-------------------------

1vanK | 2017-11-10 13:50:40 UTC | #10

Actually making bindings for C# can be fully automated (I reason with the example of UrhoSharp) so may be move to C# in official repo instead support As/LUA ?

-------------------------

Modanung | 2017-11-10 17:32:38 UTC | #11

Would it be possible to automate AS and Lua binding? If so, could this process be made part of building the engine, and - as such - be controlled by cmake flags and outside commit-space?

I'd think any language binding that can (already) be automated could be optionally supported... and left out by those who want to stick to the native language.

-------------------------

rku | 2017-11-10 18:41:05 UTC | #12

Bindings can definitely be automated, except noone wants to write code doing that.

-------------------------

Eugene | 2017-11-10 19:29:48 UTC | #13

[quote="cadaver, post:8, topic:3722"]
It’d be good if you then communicate clearly that the script subsystems have been made, to a degree, second class citizens, because that is the inevitable end result.
[/quote]
I think I mentioned it clearly in the end of topic head.

I don't think that it's really bad.
I suppose that script bindings shall be treated like any other Engine feature.
If one need it, he implement and PR it. And it is counter-productive to enforce contributors to implement and maintain features that they are not interested in.

[quote="weitjong, post:7, topic:3722"]
You forget about there is still reviewer who approve or reject the PR and that our CI is non-forgiving.
[/quote]
I think that PR reviewers could also check that new functionality has interface that is consistent with other parts of the engine, so it wouldn't make any sudden obstacle for binding maintainers.

To be honest, I highly desire that Atomic will re-union with Urho and bring its C# things, because I don't see any future behind AS and Lua. I doubt that AS will ever stay workable with new compilers because it isn't even true C++ library.

-------------------------

KonstantTom | 2017-11-10 20:44:44 UTC | #14

For my own project, I tried to automate AS bindings this summer. As I result I made this Lua script, which can be easily integrated to build process:
https://discourse.urho3d.io/t/asbindgen-c-to-angelscript-bindings-generator/3270
But it has one big disadvntage: it requires doxygen-like comments for each item you want to bind, for example:
```c++
//@ASBindGen Class ObjectType=Ref
class SampleContainer : public Urho3D::Object
...
```
Also this tool isn't well-structured and may require some changes to be used in projects such as Urho3D. In future, I can try to integrate it to Urho3D (if Urho needs it), but not earlier than in middle-January.

-------------------------

JTippetts | 2017-11-11 07:31:22 UTC | #15

I use Lua pretty heavily, but I'm willing to concede that having to provide AngelScript bindings has held me back from contribution in the past, so I can see the point of this suggestion. I'd most likely be willing to go along with the proposed change if that is the way you go (though I would naturally prefer otherwise, as I can see this leaving the Lua bindings pretty far behind.)

>  I highly desire that Atomic will re-union with Urho and bring its C# things

I think this would be a mistake, personally. Urho3D right now appeals to those of us who have no use for C# and no desire to spend the time learning to be comfortable with C#. I feel like C# users have their options (UrhoSharp among them). If C# is the way this project decides to go, I would certainly just fork before the change and never come back.

-------------------------

artgolf1000 | 2017-11-11 09:04:19 UTC | #16

Though I use the SDK in pure c++, but if it can do automate binding, the argument will terminate.

-------------------------

Modanung | 2017-11-11 09:54:57 UTC | #17

[quote="JTippetts, post:15, topic:3722"]
If C# is the way this project decides to go, I would certainly just fork before the change and never come back.
[/quote]

I'm urged to feel the same way. On the other hand this might make Urho the ideal gateway to open-source for those who started out with Unity (freshmen's default).
Admittedly, my guts raise most concerns when talking C#. :nauseated_face:

-------------------------

rku | 2017-11-11 09:57:30 UTC | #18

Whats wrong with C# though? I do not like it and i do not use it, but if some people find it useful why would any of you care? Bindings are optional. Just like you do not use AngelScript you can proceed not using C#. No need for dramtic forks over nothing.

With that said - i think ideally bindings should live in their own repositories possibly with their own maintainers, but most ideally they should be (like we already said) autogenerated. Everyone would be happy then.

-------------------------

Modanung | 2017-11-11 10:22:50 UTC | #19

[quote="rku, post:18, topic:3722"]
Whats wrong with C# though?
[/quote]

It is a hastily devolved member of the C family that should be ignored for the sake of sanity.

-------------------------

rku | 2017-11-11 10:43:19 UTC | #20

That sounds much like a personal opinion. I do not think anyone should dictate what others are supposed to do or not to do based on their personal opinion. I myself think that C# does not have much place if any in game development. There are people who think otherwise and as far as i am concerned they can shoot themselves in the foot as much as they want, provided it does not impact me. UrhoSharp exists for quite some time now. Notice how it changed nothing? I suggest we should be less dramatic and more pragmatic about technical decisions. Emotion has no place in technology.

-------------------------

esakylli | 2017-11-11 10:55:15 UTC | #21

I use C# (UrhoSharp) and I'm really happy with it. I feel I'm very productive with it.
(In my day-job I work with C#/Java, for the past 20 years.)

-------------------------

organicpencil | 2017-11-15 06:44:17 UTC | #22

Gotta say I love the quality of our current AS bindings. But as a hobbyist that never contributes, my opinion doesn't weigh a whole lot here.

On the C# front: Don't care so long as it's not a core dependency.
Don't get me wrong, I've had a few gigs with C# and don't completely hate it. The problem (maybe I'm crazy) is that MS could totally kill mono if they really wanted. It'd be pretty stupid if they did. But I wouldn't rely on Microsoft not to do something stupid (or greedy).

-------------------------

George1 | 2017-11-15 08:30:46 UTC | #23

.net core is already at version 2. It's opensource, there's no reason to not consider it.

-------------------------

organicpencil | 2017-11-16 02:41:22 UTC | #24

Was not aware of .net core! That's slick. I'm so behind the times :confused:

-------------------------

johnnycable | 2017-11-16 09:05:44 UTC | #25

Isn't this thread about "removing" pointless features which hamper development (lua/angelscript)? Why now are we talking about getting in another one (C#) just to get the matter worse?
But I guess it's only for the sake of talking...:wink:

-------------------------

Modanung | 2017-11-16 10:45:06 UTC | #26

[quote="johnnycable, post:25, topic:3722"]
Why now are we talking about getting in another one (C#) just to get the matter worse?
[/quote]

The notion of automation:

https://discourse.urho3d.io/t/changes-in-urho3d-contribution-checklist/3722/10?u=modanung

-------------------------

1vanK | 2017-11-16 10:46:43 UTC | #27

This thread about changes of PR rules (making bindings only at will). This will speed up the development of the C ++ base, but of course, bindings will start falling behind

-------------------------

Victor | 2017-11-16 13:56:45 UTC | #28

Nice, I'm glad C# was mentioned! C# is already incredibly popular and one of the best ways to get users involved in using an engine. It'd be nice to see the editor rebuilt using C# as well. I find it a very easy language to follow (just a personal opinion). While Godot is struggling to get official C# support, Urho already has a leg up on the support and it would be nice to see it made official, even if that meant dropping AngleScript or Lua since I'm sure it would be hard to keep maintaining all of the bindings as Unity found with Boo/Javascript.

Just my two cents (not meant to offend anyone already using Lua/As). While I have only really used C++ for Urho, (and C# at work), I can see C# bringing in more users to this community if it was an officially maintained language in the engine. I do think it would be wise however to drop one or both of the other languages just to reduce support overhead.

-------------------------

johnnycable | 2017-11-16 16:46:16 UTC | #29

Well, it seems Godot already has [C# support](https://godotengine.org/article/introducing-csharp-godot). Paid by Microsoft...
No, don't do that...

-------------------------

Victor | 2017-11-16 17:10:07 UTC | #30

Oh, I thought they were still struggling to add the support as of their current Alpha 3 version. Struggle might be the wrong word, but working out the kinks in their current implementation. Urho seems to have a bit better support with C#, even if it's not official, and I felt they should take advantage of that fact.

**Disclosure**: I'm probably the worse at suggesting this since I've only used Urho's C++ library and I've not dabbled with the Lua/As bindings, but I do feel like there is a lot of opportunity with C# for Urho's future.

-------------------------

johnnycable | 2017-11-16 17:14:23 UTC | #31

You mean Atomic...
I see they have Js too... this class here from the docs: http://docs.atomicgameengine.com/api/enums/atomic.clientconnecttogameserverstate.html
Looks like solving this problem here:
https://urho3d.github.io/documentation/1.7/_building.html

> Emscripten build process

    WHAT DOESN'T WORK:

        Networking. Javascript can only use http and websockets protocols so it's not likely that kNet will ever function.
I guess if this could be a solution...
Js appears to be much more palatable than C# anyway...

-------------------------

feltech | 2017-11-18 01:03:18 UTC | #32

Urho3D comes across (to me) as exceptionally professional in it's insistence on keeping scripting languages as first class citizens.  The demos are especially wonderful for cross referencing how the same things are done in the different languages.

I love LuaJIT for high level scene logic, with C++ for things that have to go quick and/or in parallel.  I would hate to lose first class Lua support. Especially as LuaJIT has been [benchmarked to be the fastest game scripting language](https://github.com/r-lyeh/scriptorium) - that list sold me on Lua (at #2) vs. AngelScript (at #15).  There is also the wonderful [MoonScript](https://moonscript.org/) to improve the syntax greatly (IMO).  

Lua bindings can be made easier (and more efficient) using [sol2](https://github.com/ThePhD/sol2).  The maintainer is great - I've even got him to [improve support for interop with other bindings](https://github.com/ThePhD/sol2/issues/511), in particular tolua++.

I really can't see the point of AngelScript, though.  I don't understand what it gives you - esoteric and statically typed, yet apparently slower than LuaJIT. The Lua community and 3rd party packages are also much more vibrant (though ageing).  I would be perfectly happy with dropping support for AngelScript (but then, I don't use it, so I would say that).

Encouraging contribution by not requiring bindings is indeed a conundrum. 

A patchwork of implemented vs. unimplemented bindings would detract from the perceived quality and surely turn away prospective users. 

Having lots of contributed features in the master code base isn't necessarily a good thing either.  Surely we all already have to disable a bunch (most, in my case) of the options in CMake (with a lot of trial and error because of the dependencies between them).  

So, in conclusion, I dunno - just don't abandon Lua, please!

-------------------------

organicpencil | 2017-11-18 04:00:26 UTC | #33

In defense of Angelscript: I love how closely it translates to C++. Fantastic for prototyping. And sadly my brain isn't wired for lua.

Overall I'd say a healthy minimum is that PRs can't break existing script APIs. I'll admit that, like others, the prospect of supplying multiple script examples has invoked laziness which blocked me from submitting a PR.

But perhaps rather than letting bindings & script examples stagnate... a contributor could be encouraged to seek community aid when they have no desire to learn/mess with additional scripting languages. I mean, if someone has to do the work anyway, might as well sit on the PR and keep master in pristine quality.

Just my 2 cents. Carry on.

-------------------------

1vanK | 2017-11-18 05:26:33 UTC | #34

[quote="feltech, post:32, topic:3722"]
I love LuaJIT for high level scene logic, with C++ for things that have to go quick and/or in parallel.  I would hate to lose first class Lua support. Especially as LuaJIT has been benchmarked to be the fastest game scripting language - that list sold me on Lua (at #2) vs. AngelScript (at #15).  There is also the wonderful MoonScript to improve the syntax greatly (IMO).
[/quote]

You can just compare samples AS/LUA/C++ and you can see  that in reality AS is faster then LUA. I do not know the reason. May be test is old and since that time the AS has been optimized. Maybe the test is synthetic and speed of calling functions from c++ is more important than speed of script execution

-------------------------

orefkov | 2017-11-21 05:31:55 UTC | #36

I share your opinion.

Tests for the AS at first are very old and at second do not reflect the specifics of the using of scripting languages ​​in games. Scripts do not require complex time-consuming calculations, which are tests oriented. Scripts are used to “glue” the logic of the basic components. In my practice, I never encountered a situation where the work of scripts became a “bottleneck” for the overall performance of the game. If this happens - there is something wrong with the design of your program, and not with the script engine. In addition, under x86 / x64 AS also has a JIT compiler, and I use it in my projects.

For me, AS is very good for scripting games - static typing helps to keep the game logic design clean and clear, and an excellent codecomplete helps in writing code. And the call to the engine functions without overhead really gives a huge increase in speed.

-------------------------

rku | 2017-11-21 08:00:55 UTC | #37

People who like AS/Lua, why dont you step up and improve bindings, possibly create auto-binding solution? It is a weird situation now. People who do not want or need bindings are forced to make them for people who do want bindings.

-------------------------

slapin | 2017-11-21 08:12:01 UTC | #38

And yes, people who want things to work only on Windiws are forced to make things work for Linux, Android, MacOS.
It is really sad world - everyone demands some quality level of contributions and nobody likes polishing. That is why most
people keep to their own toys.

-------------------------

rku | 2017-11-21 08:13:24 UTC | #39

Difference is that supporting major platforms reaches way more people. Wrapping entire engine in obscure scripting languages serves as a toy for few.

-------------------------

Eugene | 2017-11-21 08:20:30 UTC | #40

[quote="slapin, post:38, topic:3722"]
And yes, people who want things to work only on Windiws are forced to make things work for Linux, Android, MacOS.
[/quote]

Could you remind me _any_ Urho featrue (for last few years) that was OS-specific an required separate implemetation?

On the other hand, almost any change requre some binding tweaking.

-------------------------

slapin | 2017-11-21 08:33:46 UTC | #41

well, speaking directly, you won't increase amount of contributions by dropping scripting.
Look at how hard is contribute to projects like Linux kernel but still they have thousands of contributors
because the process is clean and friendly. You have tools to control quality and eyes willing to review patches.
Also you have very clean set of rules easy to follow. So common engineer really knows steps needed to be done
to have contribution. And nobody cries about bloat, become hostile, etc. because of your contribution.
As soon as Urho. As soon as people go in right direction and see others successfully contributing, amount of contributions
increases a lot.

However as I see, the respectable urho community are more into protecting status quo (i.e. Urho is good as is, no more bloat please), so everyone prefers to add needed things locally. This is quite strong position I respect, so I think somebody needs to just cleanly state the direction it all goes in.

As I observe, there are 2 extreme paths possible to take - Unity-style (all contributions are external, very little goes to
core and core kept minimal even for the price of rigidness) and UE4 way - put high level stuff in engine for people to easily start with stuff but have huge code base and great tools with amount of alternates integrated.
Path1 requires huge resource investment into marketing to be successful, second path requires more investment into code. Either way require some serious community-related work to be done and as of now, no onw is willing to do anything, which leads me to a single possible way for Urho as of now - do not change anything, just accept contributions to fix bugs,
increase performance, etc. this allows to keep status quo, keep everyone happy and less work for maintainers which is most important thing as of yet.

-------------------------

rku | 2017-11-21 08:43:22 UTC | #42

[quote="slapin, post:41, topic:3722"]
well, speaking directly, you won’t increase amount of contributions by dropping scripting.
[/quote]

And on the other side of fence we have people who decide against contributing so that they do not need to mess with manual bindings. And those people even include @Eugene, a core maintainer. Once you start contributing changes that require you to do ton of manual bindings you would reconsider.

There are people interested in pushing Urho3D forward, however they have no interest in spending time on this binding stuff. If anything this just raises a chances of eventual fork and duplicated effort. Considering Eugene does not like writing bindings and weitjong is also considering stepping down, where does that leave this project? I do understand some people like writing some stuff in Lua. That is great, now step up and maintain bindings. Put some work behind those words.

-------------------------

slapin | 2017-11-21 09:08:24 UTC | #43

Well, I would step up and maintain bindings in any other circumstances, but I decided never ever to contribute
or get associated with Urho in any way until some things change. Until then I prefer to play with my own toys in local fork.

-------------------------

johnnycable | 2017-11-21 09:14:04 UTC | #44

Of course, constraints of time and resources prevents Urho from going onward on the path of supporting a full feature set, imho. So it's just a question which things to drop out. And of course scripting it a good candidate. Mainly because it's redudant; you can do it with c++.
Secondly because it's used by very few people; in over a year with Urho, I remember having found only two examples of AS, none of Lua. 99% users are C++ guys...
So...
Let alone manual bindings. Nobody does. There are tools for that.
Add to it that AS Editor blocks access to Urho low level features, and in that way it's a hamperer of full editor development. De facto, it has already been desupported.
So it's not a question of what one wants (U3D and Unity are commercial ventures), it's a question of what you can really do.

-------------------------

alexrass | 2017-11-21 12:52:00 UTC | #45

If add C-API for Urho3D, the problem with adding a scripting engine would be less i think.

-------------------------

slapin | 2017-11-21 12:54:47 UTC | #46

and then @Eugene will say he do not want to support C-API and it threatens contributors, so it is no much different from scripting.

-------------------------

Eugene | 2017-11-21 13:12:39 UTC | #47

C API for most classes could be generated automatically from some metadata like the Atomic do.

+1 for "manual binding sux"

-------------------------

alexrass | 2017-11-21 13:17:22 UTC | #48

C API also add support for using Urho3D from many languages (c#, go, rust, pascal/delphi)

-------------------------

slapin | 2017-11-21 13:22:42 UTC | #49

How would you make automatic C api from C++ code?
Manual binding rulez, but only for things you care about.
Automatic binding is compromise, not something optimal or so. Scripting requires design
as everything else. So I suggest not putting head over heels and just understand, that
having no time to do things right it is just better to step away from something in hope
to improve something else. Itherwise it is just self-deception.

-------------------------

1vanK | 2017-11-21 19:01:24 UTC | #50

I created simple heades parser https://github.com/1vanK/Urho3D_DotNetBindings/tree/master/Tools/CppParser but 
there are many cases where automatic generation is not optimal and requires an individual approach, so I use it just to avoid making mistakes when copy-paste

This generate files like https://gist.github.com/1vanK/c59c9417c9422d700c3984d24f0832c3
(just inserts the wrapper into original  header file)

-------------------------

Eugene | 2017-11-21 13:35:51 UTC | #51

[quote="slapin, post:49, topic:3722"]
How would you make automatic C api from C++ code?
[/quote]

As I mentioned above, as Atomic do it.
Automatic C API is ugly and incomplete, but it's automatic.
And it's fast enough.

-------------------------

orefkov | 2017-11-22 14:27:22 UTC | #52

IMHO is the first step along the path, which can become a dead end. First, you will throw out the scripts, and those who use the engine because of the scripts will leave. The rest will groan that it is hard for them to write with glance at GLES, and you throw out GLES.
Then remove the support of some OS. As a result, a powerful engine will come out, which three people can approach.
Personally for me, the engine is good for developing for Android with scripts.
It's enough for me to have five seconds for the phone to tighten through rsync fresh scripts and assets from the working folder and feed them to urho3dplayer. I do not even need to restart the whole game, I just reload some of the scripts and see the result. No unity can do that to me.
Well, apparently I'll have to write bindings myself when I need it.

-------------------------

rku | 2017-11-22 14:43:57 UTC | #53

[quote="orefkov, post:52, topic:3722"]
Well, apparently I’ll have to write bindings myself when I need it.
[/quote]

How about commit to maintaining them for Urho3D instead?

-------------------------

orefkov | 2017-11-22 22:19:10 UTC | #54

Yes, if I make some bindings for own purpose, I will try contribute it.

-------------------------

lazypenguin | 2017-12-28 00:20:06 UTC | #55

Hello all,

It's a shame to see Urho losing a bit of steam these days. I want to offer my (unsolicited) perspective on things as a non-contributor/non-maintainer/user and expert-beginner C++ user :wink:.

**Note**: What follows are my OPINIONS, you don't have to agree with anything I say but I believe multiple perspectives are useful in discussions.

I'm a bit surprised that the current debate with regards to Urho is about whether to support Angelscript/Lua bindings while I feel as though there are bigger hurdles to adoption. FWIW I support @Eugene's recommendation to stop supporting script bindings (at least officially in master branch) and I would be even more aggressive and remove 2D and mobile support entirely. In my opinion, Urho's strength is that it's a lightweight C++ 3D engine with many features included (terrain, animation, UI, etc.) Urho has no competitive advantage in 2D or mobile compared to specialized engines, especially those with great editors. Urho has no competitive advantage with 3D engines with advanced scripting support (e.g. Unity + C#, Unreal + Blueprints). Urho has no competitive advantage with 3D engines that utilize VR or advanced graphics techniques (lumberyard, unity, unreal, etc.). Urho's single greatest competitive value is that it it's a clean, high-quality C++ code-base for developing 3D games. 

**Urho Strengths**
* Clean C++ API 
* Lightweight which is honestly the biggest reason to pick Urho over Unreal or similar
* Integration of great libraries with no NIH syndrome (see: godot :wink:)
* Mature codebase which has accumulated many bug fixes over the years
* Strong developers - I think due to the current state of this game engine the current members active in the community (and the current maintainers) are actually quite talented and are strong developers.
* Out-of-the box support for networking, terrains, databases, etc.
* 3D

I'm always dissapointed to see on /r/gamedev or gd.net during the weekly "What's the best C++ game engine/library/etc." questions that Urho is rarely mentioned. I think Urho fits that niche EXCEPTIONALLY well, catering to those that like more flexibility/control but are turned off by bloated enterprise-y code bases like unreal but are daunted by the prospects of writing their own engine from scratch. However, I think Urho suffers from a few weakness that prevent its adoption.

**Urho weaknesses**
* Documentation - The docs, api reference and examples are "okay" but there is a lack of depth. Each topic in the engine has one page and maybe 300 words about it, more if you are lucky. While we can all wish that users will be active in reading the api, looking at examples and reading the source code I think we have to all admit that most people don't do that. Urho could definitely use some "tutorial" style documentation for different topics.
* Build system - I am sure this is a point of contention but my biggest hurdle back when I was first looking at Urho was the build system. It was my first foray into cmake (or any C++ dev outside of visual studio) and it was definitely a barrier to my adoption. Even something as simple as "how should I manage the default shaders/materials/etc.?" wasn't obvious to me. This may be hard for the experienced C++ developers to relate to but it's definitely a barrier to adoption, let alone contribution. No matter how shitty scons is, I had no problem starting a project or contributing to godot engine as all I had to do to build a new version is `scons platform=x11`. Unity/Unreal? Hah, you don't even know there is a build system :joy:.
* Shaders/Techniques/Materials - Urho has a lot of wonder features but when you want to simply start a new blank project and you want to render some stuff, you either have to copy the default materials/techniques/shaders and use them as is or stumble around trying to figure out how they work.
* Editor - I like that Urho is not an "editor-first" game engine but when I was starting out and experimenting I wanted to learn the different components and how to compose a scene. I wanted to use the editor as a "sandbox" / for experimentation but it was cumbersome and difficult to use.

I am not sure what the point of my wall-of-text was except to share my perspective. If anything, I would hope that Urho can shore up it's attention and focus on its strengths as a lightweight and clean C++ 3D game engine. I think with a tighter focus, better user-experience development and cooperation Urho can continue to grow indefinitely. I am ready to contribute to the ecosystem but I think the community needs to agree on the future and an active developer/maintainer will have to step-up to maintain the vision.

> On a side note, removing Urho2D, LuaScript and Angelscript would reduce the maintenance overhead by ~20%

`Source/Urho3D`
```
-------------------------------------------------------------------------------
 Language            Files        Lines         Code     Comments       Blanks
-------------------------------------------------------------------------------
 Autoconf                2           66           36           24            6
 C Header              289        52164        27073        18003         7088
 C++                   287       134743       103956        10554        20233
 Lua                     3         1287          991          139          157
 Objective C             1          183          131           26           26
 Plain Text              1          531          531            0            0
-------------------------------------------------------------------------------
 Total                 583       188974       132718        28746        27510
-------------------------------------------------------------------------------
```
`Source/Urho3D/AngelScript`
```
-------------------------------------------------------------------------------
 Language            Files        Lines         Code     Comments       Blanks
-------------------------------------------------------------------------------
 C Header                7         2304         1597          443          264
 C++                    21        14997        12104         1116         1777
-------------------------------------------------------------------------------
 Total                  28        17301        13701         1559         2041
-------------------------------------------------------------------------------
```
`Source/Urho3D/LuaScript`
```
-------------------------------------------------------------------------------
 Language            Files        Lines         Code     Comments       Blanks
-------------------------------------------------------------------------------
 C Header                7          814          381          325          108
 C++                     6         2051         1560          157          334
 Lua                     3         1287          991          139          157
-------------------------------------------------------------------------------
 Total                  16         4152         2932          621          599
-------------------------------------------------------------------------------
```
`Source/Urho3D/Urho2D`
```
-------------------------------------------------------------------------------
 Language            Files        Lines         Code     Comments       Blanks
-------------------------------------------------------------------------------
 C Header               38         4509         1891         1917          701
 C++                    36        10075         7252          890         1933
-------------------------------------------------------------------------------
 Total                  74        14584         9143         2807         2634
-------------------------------------------------------------------------------
```

-------------------------

ricab | 2017-12-28 02:53:43 UTC | #56

> remove 2D and mobile support entirely

I strongly disagree with this. Both 2D and mobile targeting work well and add to one of Urho's greatest strengths IMO: encompassing scope. 2D support may not be extensive (I mainly miss lighting), but what exists is solid and reliable, and from what I have seen it requires very little maintenance. And I suspect cross-platform targeting is important to a lot of people.

Even if individual features, taken alone, are only crucial for a few people, together they are what sets Urho apart IMO (there aren't many C++ engines which are free, with a permissive open-source licence, mature good-quality code, great cross-platform targeting, multi-platform dev, a great flexible build system, 3D/2D support, 2 scripting languages, a vast set of features...)

I can still understand both sides of the scripting argument, as the cost is considerable and existing bindings would not be dropped. Simply dropping existing successful things that have almost no upkeep is a totally different matter... I don't think that makes much sense.

-------------------------

ricab | 2017-12-28 02:59:33 UTC | #57

Also, notice that "focusing on strengths" does not work in practice when work is not allocated centrally. Unless they are paid, people spend their effort on what matters to them, independently of whether it is considered "the focus".

-------------------------

yushli1 | 2017-12-28 03:13:50 UTC | #58

[quote="lazypenguin, post:55, topic:3722"]
remove 2D and mobile support entirely
[/quote]

This will kill Urho3D. end of story.

-------------------------

SirNate0 | 2017-12-28 04:16:54 UTC | #59

Like some of the others, I also disagree with the others about removing mobile support. Cross platform support including mobile and web support is one of the best points about Urho, if you ask me (and probably the reason the complex build system is required, and also one of the reasons I personally use Urho). While I personally don't really care about 2D support, it is there already, and should at least be maintained since, as far as I can tell, it is pretty solid.

As to the scripting issue, personally I would favor removing the requirement to add script bindings for contributions. Given that the scripting API is already incomplete (deliberately leaving out low level stuff) and inconsistent (e.g. there are AS bindings for PackageFile but there are no Lua bindings), I would favor asking that script bindings be included in contributions, but if they are not only requiring that an issue be raised requesting them for the new feature. Perhaps also we could require that script bindings be maintained -- if you change something that breaks script bindings, don't just get rid of the bindings but rather fix them, or include new bindings if the new functions/properties closely relate to existing features if it is easy enough to do. I don't necessarily think that should be a hard rule, as if you introduce Vectors the bindings can get very complicated, but neither should we allow you to add some integer to a class that is exposed only to the C++ api, when it would be one additional line each for the AS and Lua bindings.

I will say I definitely oppose removing scripting support from Urho. While that would ease maintenance, scripting is excellent for a number of things, most important of which I think is dynamic execution of somewhat complicated behaviors for things like item actions or NPC behaviour -- I want the NPC to say "blah", walk along some arbitrary path, push a button, and then say something else. Or the even more simple conditional execution of speech -- if some condition (like a global flag) has been set say "X" otherwise say "Y". On a less-globally-useful note, scripting is also a much better way to support modding of your game -- reskinning it is easy enough without it, but if you want to allow new items with interesting effects and such you either have to have a very complex class for the items in C++ (like Urho's Material class, for example) to allow all of the needed behavior on the C++ side based off of the stored data, or you can have a much simpler class that defers the important behavior to the scripting language.

On the other hand, I don't use Lua at all (I have no interest in learning it's strange syntax) and pretty much only like AngelScript because it is so similar to C++. I would definitely be open to other scripting languages replacing them (python (which I like, though I don't know how nicely it would fit as a game's script) or C# (which I've never used) perhaps, though the latter especially seems rather heavy for just a scripting language for your game)...

Regarding your comments about "Shaders/Techniques/Materials", I definitely agree that these are complicated, but I also feel that it is out of necessity. I think think the solution would probably be better documentation/tutorials (they needn't necessarily be included in the documentation), though at least for Materials I feel the Editor's  support may be enough. As to writing new shaders (and then accompanying Techniques and possibly Materials), this is indeed a very complicated topic and I'm not really sure how you can make it easier (docs/tutorials?) since what they do is complicated and, from my experience at least, writing shaders is a much harder to debug process than C++ code.

Regarding the Editor, I also think some definite improvements could be made. I think the simplest would probably be to have a default start-up file like Blender that is a really simple working scene (possibly a clone of Blender's -- a model, a light, a camera, and then a Zone with a not-black fog/ambient color (I don't like the black appearance, and I don't like having to add a zone myself to add ambient lighting whenever I want to look at some models/object prefabs. However, I also agree that it is good that Urho is "that Urho is not an 'editor-first' game engine,” especially since I use Blender as my editor for both models and scene layout.

Also, what program did you use to obtain the stats? It looks similar to the output from cloc, but it's different enough that I think it must be something else.

-------------------------

johnnycable | 2018-01-24 09:05:31 UTC | #60

Looks like everybody's talking about removing features they don't use...:wink:
I want to talk here about what I miss instead:

* Ability to use Alembic: the most used 3d interchange format for vfx. Uhro can't work so low-level. Enabling it would mean being able to turno Urho in a full vfx platform. 
* Per-usage modularization builds. I'd like to compile and use an Urho version for the web, one for mobile, one for high end desktops... could break a monolithic Urho vision while allowing for contributors to focus on what they like...
* Front-end enhancements. I'd like to set an animation path, write a lambda in c++, and see things moving. Requires some engineering on AI and state machines.
* A configurator. Something that allows people to drop the source in a directory and give one command for building the app. Present system is for building just the engine, what's missing is a per-project fast setup. Theorically outside of engine scope because is application dependent...
* The pipeline. Taking things from a 3D tool like Blender or Maya into Urho can be daunting. But the pipeline is the weak spot in all the 3d chain, so no blame on Urho. Things like Unity go great lenghts to ease it on users, and that cost a lot of resources. 
* A plugin architecture. Many contribuitions can be thought of non-core but they are worth the while. It could be a good choice to set something like a "Awesome Urho" page to gather all this community feeds. But probably would be highly opinionated. An exchange mechanism thru git could enable fast deploying into one's setup without bloating the core code.
* A community manager. Someone not like @cadaver who's a technical master but more like a PR guy who manages site changes, documentation, buzz, and so on. Yet, this requires resources.
* Network enhancements. Server-side is complicated thing and the present architecture appears not made to bear a high load of transaction. Special software is made for that (think world of tanks) so what Urho offers is okay. But not having network integration for the emscripten/web feel like something really strange...
* Full PBR. Not working on mobile at the moment. This may appear simple but it's not. The guys at Godot made a new full 3d core engine; then enrolled a specialist just for this. So it's not easy.
* Level Management. Something who can manage levels. Part AI part editor, and tied to pipeline and plugin architecture. Probably application dependent. You know what I mean.
* Business Interface. Something for managing business services and user retention. Could be useful
* Publishing howto. All the way through up-to-date guide explaining advantages and pitfalls of using Urho for publishing games in the market.
* New UI. Some new simple but powerful UI system able to spritescale9, ui skinning, flexible enough to be in-app and debug tool
* Urho 2D design interface. Allow 2D apps to be designed the easy way considering aspect ratio and screen sizes fitting.
* Quick painting ability. Ability to write simple lines and primitives like in debug draw but made better and usable outside debug.

All in all, these features requires time and effort, and, thinking it over a couple of time, they seems to be not really core-related. They are something which complements the engine, without being central to it. The icing on the cake.
Sure icing can be juicy, but in the end, contributions remain personal. If someone has the interest and time and will to do them, they are welcome. I feel Urho is good enough, and in some time I'll be able to fix thing myself if they are not the way I like them or broken. So... thank you all guys for this.
TL;DR; enough.

Edit: added level, business, publishing
Edit: added new UI, 2D design interface, quick painting

-------------------------

dragonCASTjosh | 2017-12-28 12:32:54 UTC | #61

What I feel would benefit urho is a feature freeze on the current master branch, then we spend time redesigning the core of the engine. That way features like 2d, mobile and High end rendering can all be developed and used independently. That way users can choose what they want.

On a side note features like PBR on mobile become much easier if we upgrade to GLes 3.0 due to the updated feature set bringing it closer to standard gl

-------------------------

