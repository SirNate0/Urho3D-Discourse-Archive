Lcbx | 2020-12-08 13:26:41 UTC | #1

Hello,

sorry if I reopen a contentious topic.
I believe some possibilities weren't brought up in the last discussion.

rbfx adds neat features/changes to Urho : the lightmapper, automatic bindings via swig (C# for now, but lua should be relatively easy to add), built-in serialization, better containers, ...

But some people want to : 
- avoid the C# ecosystem (because Microsoft)
- keep angelscript (which is removed in rbfx, and would need work to add to swig definitions)
- keep the original editor (built on angelscript)
- avoid the eastl containers (because EA)

Here's my take on it :
 - so long as the engine itself doesn't depend on C#, the *binding does no harm*.
I don't like Microsoft either, but the language is good for scripting purposes and is becoming the industry standard. If Microsoft fuckery happens, we just keep the last clean open-source version of the .Net environment until the userbase has migrated their projects, then ditch the binding

- while angelscript can't have auto bindings, we could *keep the original angelscript manual bindings* (@rku : can you confirm that the manual bindings could be brought back ?). Also, let's drop the burden of maintaining them to whoever uses them instead of those that add features.
 
- thus, the original editor can be kept with angelscript for the sake of retro-compatibility, but having the editor dependent on one of the scripting languages was a really bad idea. The new editor already in rbfx, while not full-featured, *is in c++ like the rest of the engine* as it should, on top of being easier on the eyes. Let's just build it up to what the old one was capable of.

- the eastl containers are different from the C# bindings in that they are an integral part of the engine. BUT *a container library is very different from a language*. Even if it goes closed-source or stops being maintained, we would just keep the last clean open-source version and maintain it ourselves, which is already the case with the actual containers anyway.

Hope that makes sense, looking forward to your responses,
and thanks for coming to my TED talk :p

-------------------------

1vanK | 2020-12-08 13:44:58 UTC | #2

 https://github.com/AtomicGameEngine/AtomicGameEngine

JavaScript, C#, own editor, 2d lighting and other cool features

-------------------------

rku | 2020-12-08 14:00:29 UTC | #3

[quote="Lcbx, post:1, topic:6605"]
automatic bindings via swig (C# for now, **but lua should be relatively easy to add**)
[/quote]

We should not. SWIG support for lua is quite bad. No polymorphism support for example. However i am eyeing [sol2](https://github.com/ThePhD/sol2) for that. Bindings using sol2 could be generated from clang ast. clang10+ can dump ast as json and i am working on a python script that would pregenerate lots of SWIG crap. There is another similar script i made, but it uses pyclang and is terrible in just about any way you could imagine so it must be set afire :fire:. 

[quote="Lcbx, post:1, topic:6605"]
@rku : can you confirm that the manual bindings could be brought back ?
[/quote]
There is no technical obstacle, lack of AS in rbfx is purely political. I am not going to put any work behind something i think is a bad investment.

---

It is clear that there are multiple groups of people who want different things. People who would like to maintain status quo may keep using upstream Urho3D. People who want to experiment may use rbfx. This is totally fine.

-------------------------

Eugene | 2020-12-08 14:03:12 UTC | #4

Oh hell here we go again. God I hate such threads so badly. 

Last time I had a poll it was clear that significant portion of Urho users enjoy its stability and lack of breaking changes and feature removal. It’s their choice and I am fine with it.

Whereas the main purpose of the rbfx fork (and almost any other fork in general) is to be different from original, to change things in breaking manner. To lose something and to gain something else.

I don’t see how you can realistically reconcile these two very different approaches to development. It’s hard to make breaking changes in fork. It would be three times as hard to make similar non-breaking changes in master.

-------------------------

1vanK | 2020-12-08 14:08:56 UTC | #5

[quote="rku, post:3, topic:6605"]
There is no technical obstacle, lack of AS in rbfx is purely political. I am not going to put any work behind something i think is a bad investment.
[/quote]

Does this mean that there is only one person making decisions in your organization?

-------------------------

rku | 2020-12-08 14:10:51 UTC | #6

No. But this particular decision was made when there was just one person total. Be that as it may, it does not change a fact that AngelScript is a bad investment.

-------------------------

1vanK | 2020-12-08 14:12:06 UTC | #7

I've always considered AS to be one of the best scripting languages out there. Can you substantiate your point of view?

-------------------------

Modanung | 2020-12-08 14:18:27 UTC | #8

[quote="Lcbx, post:1, topic:6605"]
But some people want to :

* avoid the C# ecosystem (because Microsoft)
* keep angelscript (which is removed in rbfx, and would need work to add to swig definitions)
* keep the original editor (built on angelscript)
* avoid the eastl containers (because EA)
[/quote]

Those may also want to consider giving [Dry](https://gitlab.com/luckeyproductions/dry) a try, which also comes with a (∞WIP) [editor cluster](https://gitlab.com/explore/projects?tag=Dry).

-------------------------

Eugene | 2020-12-08 14:22:49 UTC | #9

[quote="1vanK, post:7, topic:6605, full:true"]
I’ve always considered AS to be one of the best scripting languages out there. Can you substantiate your point of view?
[/quote]
I admit that AS has good aspects, efficient C++AS interop in first place.
What I don't like in AS:
1) No automatic binding library. Your autobinder may or may not fill this niche later, but at the moment of AS removal from rbfx there were none, and your binder is still not generic enough.
2) AS is assembly library and it cannot work without platform-specific assembly code implemented by AS maintainers. I don't think it caused actual issues with Urho, but I don't like this kind of dependency. I just don't want to rely on portability of assembler library in year 2020.
3) Derived from 1) and 2), C++AS bindings are very type-unsafe. One mistake may lead to crash or security risk.

-------------------------

rku | 2020-12-08 14:23:20 UTC | #10

[quote="1vanK, post:7, topic:6605, full:true"]
I’ve always considered AS to be one of the best scripting languages out there. Can you substantiate your point of view?
[/quote]

* AS is very C++\-like. If i wanted something like C++, i would use C++.
  * Since it is a scripting language i do not understand why it adds a cognitive load of C++ concepts.
* AS has no ecosystem around it.
  * No editors
  * No debugging
  * No libraries

[quote="Modanung, post:8, topic:6605"]
Those may also want to consider giving [Dry](https://gitlab.com/luckeyproductions/dry) a try, which also comes with a (∞WIP) [editor cluster](https://gitlab.com/explore/projects?tag=Dry).
[/quote]

You split a community. :eyes:

-------------------------

1vanK | 2020-12-08 14:28:22 UTC | #11

[quote="rku, post:10, topic:6605"]
AS is very C++-like. If i wanted something like C++, i would use C++.
[/quote]

C# is very C++-like. If i wanted something like C++, i would use C++.

-------------------------

1vanK | 2020-12-08 14:30:05 UTC | #13

[quote="Eugene, post:9, topic:6605"]
AS is assembly library and it cannot work without platform-specific assembly code implemented by AS maintainers. I don’t think it caused actual issues with Urho, but I don’t like this kind of dependency. I just don’t want to rely on portability of assembler library in year 2020.
[/quote]

C# uses assembler for interopt

-------------------------

rku | 2020-12-08 14:30:57 UTC | #14

C# is syntax is C++\-like, but we do not need to think about pointers when writing a C# script. It also has insanely rich ecosystem around it (libraries and tools). And no, it does not use assembly for interop.

-------------------------

1vanK | 2020-12-08 14:32:26 UTC | #15

[quote="rku, post:14, topic:6605, full:true"]
C# is syntax is C++-like, but we do not need to think about pointers when writing a C# script. It also has insanely rich ecosystem around it (libraries and tools). And no, it does not use assembly for interop.
[/quote]

But C# not scripting language.  And use assbler for interopt.

-------------------------

Eugene | 2020-12-08 14:35:20 UTC | #16

[quote="1vanK, post:13, topic:6605"]
C# uses assembler for interopt
[/quote]
Sure, C# interop is quite dirty. That’s why I don’t want to use C# as script language as well. It has even bigger platform compatibility issues than AS.
However, I have a bit more trust in long term support of C# than support of AS.

If I had a choice, I would have used Lua or some similar lightweight 100% integrated and platform independent language for scripting

-------------------------

1vanK | 2020-12-08 14:36:05 UTC | #17

[quote="Eugene, post:16, topic:6605"]
However, I have a bit more trust in long term support of C# than support of AS.
[/quote]

 https://killedbymicrosoft.info/

-------------------------

1vanK | 2020-12-08 14:39:11 UTC | #18

Strange why there is no UrhoSharp and mfc in this list xD

-------------------------

rku | 2020-12-08 14:41:11 UTC | #19

And? Claiming that we can not rely on Microsoft to not kill C# is like saying we can not rely on Microsoft to not kill Windows. These are their flagship products, they are not going anywhere ever. Besides C# is so widely used in enterprise sector and is opensource and MIT, that it is essentially unkillable now.

Still i agree lighter alternative would also be good. They serve different usecases and having both would be good.

-------------------------

1vanK | 2020-12-08 14:45:51 UTC | #20

Great template "X are their flagship products, they are not going anywhere ever".

UrhoSharp are their flagship products, they are not going anywhere ever.
XNA are their flagship products, they are not going anywhere ever.
MFC are their flagship products, they are not going anywhere ever.
Kinect are their flagship products, they are not going anywhere ever.
SilverLight are their flagship products, they are not going anywhere ever.

> Microsoft to not kill Windows

Microsoft installs Linux on its servers and adds support for running Linux applications on Windows.

-------------------------

rku | 2020-12-08 14:47:03 UTC | #21

[quote="1vanK, post:20, topic:6605"]
Great template “X are their flagship products, they are not going anywhere ever”.

UrhoSharp are their flagship products, they are not going anywhere ever.
XNA are their flagship products, they are not going anywhere ever.
MFC are their flagship products, they are not going anywhere ever.
Kinect are their flagship products, they are not going anywhere ever.
SilverLight are their flagship products, they are not going anywhere ever.
[/quote]

Neither of those were ever flagship products.

[quote="1vanK, post:20, topic:6605"]
Microsoft installs Linux on its servers and adds support for running Linux applications on Windows.
[/quote]

So Microsoft goes where money is. Big surprise. Enterprise windows licensing is big money too.

-------------------------

1vanK | 2020-12-08 14:49:11 UTC | #22

C# and Windows

[quote="rku, post:21, topic:6605"]
Neither of those were ever flagship products.
[/quote]

https://images.a2-finance.com/uploads/2019/11/16/17_04-rpwuquko-cW4cVotgFAS6w/Microsoft_Revenue.png

-------------------------

1vanK | 2020-12-08 14:54:27 UTC | #23

Windows Phone are their flagship products, they are not going anywhere ever..

But where is Nokia xD

-------------------------

Eugene | 2020-12-08 14:56:59 UTC | #24

[quote="1vanK, post:17, topic:6605"]
https://killedbymicrosoft.info/
[/quote]
Jokes aside, I would like to compare "killed by Microsoft" to "not killed by Miscrosoft" and "died of old age unrelated to Microsoft" and to "killed by anything else".

What is the fraction of discontinuted software in total, comparing to all supported software in the world?
What is the fraction of discontinuted software to supported software among everything owned by Microsoft?

-------------------------

1vanK | 2020-12-08 14:58:15 UTC | #25

If you have such a question, you may have already found this list. So how many Microsoft products do you use besides Windows and VS?

-------------------------

Modanung | 2020-12-08 15:33:01 UTC | #26

[quote="rku, post:10, topic:6605"]
[quote="Modanung, post:8, topic:6605"]
Those may also want to consider giving [Dry](https://gitlab.com/luckeyproductions/dry) a try, which also comes with a (∞WIP) [editor cluster](https://gitlab.com/explore/projects?tag=Dry).
[/quote]

You split a community. :eyes:
[/quote]

It's more of a salvaging operation, really. :wink:

-------------------------

Lcbx | 2020-12-08 15:36:08 UTC | #27

I should have waited until after work to start this. you guys are quick :slight_smile:

[quote="1vanK, post:2, topic:6605, full:true"]
https://github.com/AtomicGameEngine/AtomicGameEngine

JavaScript, C#, own editor, 2d lighting and other cool features
[/quote]

Atomic died because the main developer moved on with no contributor willing to take his place.
Urho3d survives despite the same happening because of the people and the features. Both go together. No features no devs, no devs no features. Splitting the project harms both 

[quote="1vanK, post:17, topic:6605, full:true"]
[quote="Eugene, post:16, topic:6605"]
However, I have a bit more trust in long term support of C# than support of AS.
[/quote]

[https://killedbymicrosoft.info/ ](https://killedbymicrosoft.info/)
[/quote]
your concern over the future of C# is noted ;)

[quote="rku, post:3, topic:6605"]
[quote="Lcbx, post:1, topic:6605"]
@rku : can you confirm that the manual bindings could be brought back ?
[/quote]

There is no technical obstacle, lack of AS in rbfx is purely political. I am not going to put any work behind something i think is a bad investment.
[/quote]

Then I don't see why it can't be brought back for those that use it.


All I've seen in this thread thus far is two camps arguing over each other's choice of programming language. *Who cares ?*

vanilla and rbfx can use the same game engine and different scripting languages. Don't spit on each other's contributions to the engine itself

the bigger question was can the merge be done without harming one too much.
The C# part is moot, don't use if you don't want to. 
The angelscript part is too, surprisingly. just bring it back and let whoever uses it maintain it.
And it seems like the eastl bit isn't that problematic since no one brought it up.

-------------------------

1vanK | 2020-12-08 15:47:07 UTC | #28

> your concern over the future of C# is noted

I have nothing against C #. It's just that it will attract users who do not write C ++ code and will not do PRs to the engine.

-------------------------

Eugene | 2020-12-08 15:47:21 UTC | #29

[quote="Lcbx, post:27, topic:6605"]
And it seems like the eastl bit isn’t that problematic since no one brought it up.
[/quote]
Oh, it's very problematic. No one brought it up because there is nothing to argue about.

Significant part of current Urho users prefer custom Urho containers and want to use them.
Most (all?) of rbfx users prefer standard (EASTL) containers and want to use them.
I don't see how it can be "merged". One can't do both.

-------------------------

rku | 2020-12-08 15:55:57 UTC | #30

[quote="Lcbx, post:27, topic:6605"]
the bigger question was can the merge be done without harming one too much.
[/quote]

No it can not, because nobody in upstream wants it. And that is fine. To be honest i dont think i want it either.

[quote="1vanK, post:28, topic:6605"]
I have nothing against C #. It’s just that it will attract users who do not write C ++ code and will not do PRs to the engine.
[/quote]
So no different compared to current userbase.

-------------------------

1vanK | 2020-12-08 15:58:19 UTC | #31

[quote="rku, post:30, topic:6605"]
So no different compared to current userbase.
[/quote]

Yes, but at the moment we do not often have to answer the question "How can I add a button to Urhosharp"

-------------------------

Lcbx | 2020-12-08 15:58:23 UTC | #32

[quote="Eugene, post:29, topic:6605"]
Significant part of current Urho users prefer custom Urho containers and want to use them.
Most (all?) of rbfx users prefer standard (EASTL) containers and want to use them.
[/quote]

can't understand why, but if that's the case then the merge is indeed sleeping with the fishes :upside_down_face:

-------------------------

1vanK | 2020-12-08 16:04:41 UTC | #33

becuase eastl is slow

 https://discourse.urho3d.io/t/migration-from-custom-container-library-to-augmented-eastl/5872/130

-------------------------

rku | 2020-12-08 16:07:57 UTC | #34

[quote="1vanK, post:33, topic:6605, full:true"]
becuase eastl is slow
[/quote]

EASTL iterators are raw pointers so iteration is as fast as it gets. If it still is slow for you, then problem is in a chosen data structure or in the code. Typical frame should not be allocating memory. Hot path should not allocate memory. If these are true then any possible slowdown is amortized by vastly expanded feature set. Did you know that Urho3D HashMap used to allocate memory even if it was empty? And it was like that for years. Some SendEvent() variant would cause memory allocation even if no parameters were passed. Urho code is not as stellar as people say it is.

-------------------------

1vanK | 2020-12-08 16:09:47 UTC | #35

> Did you know that Urho3D HashMap used to allocate memory even if it was empty? 

How does this affect performance?

-------------------------

rku | 2020-12-08 16:12:53 UTC | #36

Someone already explained the issue [here](https://discourse.urho3d.io/t/re-to-rbfx-and-not-to-rbfx/6605/34?u=rku).

-------------------------

1vanK | 2020-12-08 16:13:46 UTC | #37

I don't see any measurements taken there.

-------------------------

adhoc99 | 2020-12-08 16:16:18 UTC | #38

If rbfx already has everything you want, then go use rbfx.

If you want C#/UrhoSharp, then go ask MS to support it there. They created that mess, it's their problem.

Please stop trying to push C# and EASTL here.

-------------------------

Eugene | 2020-12-08 16:20:59 UTC | #39

[quote="1vanK, post:33, topic:6605"]
becuase eastl is slow
[/quote]
It’s slower, but why does it matter? Urho is slower than plain OpenGL, yet you still use it because it offers more.

-------------------------

1vanK | 2020-12-08 16:23:54 UTC | #40

We have already discussed this many times. No one is stopping you from using your containers wherever you need to. But why replace fast containers with slow ones inside the engine?

-------------------------

Eugene | 2020-12-08 16:29:40 UTC | #41

It was done because maintaining two sets of incompatible containers is even worse than having just EASTL or just Urho containers. I wouldn’t want to work with such code.

So yep there are three options all of which are bad. You just choose your preferred kind of bad

-------------------------

1vanK | 2020-12-08 16:31:30 UTC | #42

My favorite example is an array of batches, which is sorted every frame. It directly affects performance, but you don't interact with it in any way. Why touch him?

-------------------------

Lcbx | 2020-12-08 16:52:23 UTC | #43

I do believe that in an open-source project where people do voluntary work, readability and maintainability should trump performance as a goal (unto a point. t'would be idiotic remake the engine in python). If devs hate touching the code, they won't.
The eastl while less performant than custom-made code, is probably a better choice for the project itself. You're still using a reasonably fast c++ library.

-------------------------

1vanK | 2020-12-08 16:59:22 UTC | #44

I have a different question. Do you choose which project you will send PRs, or just decided to engage in organizational activities?

-------------------------

Lcbx | 2020-12-08 17:07:59 UTC | #45

maybe my last message was a bit preachy. Apologies.

I stumbled onto Urho recently while searching for an alternative to Godot.

I read the last rbfx thread and thought the problem could be solved by keeping angelscript and wanted to make the suggestion. I am not dictating what you should do or not.

-------------------------

adhoc99 | 2020-12-08 17:21:36 UTC | #46

rbfx is also open source. If it already has all those changes, why not use it instead? Why change Urho3D and turn it into another rbfx?

-------------------------

Eugene | 2020-12-08 17:23:13 UTC | #47

Does it worth keeping whole class of container for sake of tiny performance gain per frame? I dunno, maybe for someone. Not for me. So I don’t really care. 
I never needed these extra 0.05ms per frame.

It’s not like I’m asking anyone to replace Urho containers with EASTL in their projects

-------------------------

1vanK | 2020-12-08 17:23:41 UTC | #48

> I never needed these extra 0.05ms per frame.

60 FPS = 1/60 = 0.01ms

-------------------------

Eugene | 2020-12-08 17:31:38 UTC | #49

[quote="Lcbx, post:45, topic:6605"]
I read the last rbfx thread and thought the problem could be solved by keeping angelscript and wanted to make the suggestion.
[/quote]
If only things were so easy, if only.
rbfx discussion was the longest thread on this forum, and probably had more activity than whole year prior and after it.

And there were no solution found. The only outcome was that different things should sometimes just stay different.

-------------------------

Modanung | 2020-12-08 17:34:21 UTC | #50

`60F/1000ms ~ 17ms/F`

-------------------------

1vanK | 2020-12-08 17:37:03 UTC | #51

Yes you are right. In any case, this figure was invented and not confirmed by the test. In any case, together with eastl, we get terrible string class. And what about smart pointers?

-------------------------

1vanK | 2020-12-08 17:45:26 UTC | #52

 https://github.com/rokups/rbfx/blob/master/Source/Urho3D/Engine/Application.cpp

```
std::vector<std::string> cliArgs;
```

 https://github.com/rokups/rbfx/blob/master/Source/Urho3D/IO/File.h

```
const ea::string& GetAbsoluteName()
```

-------------------------

Lcbx | 2020-12-08 17:47:11 UTC | #53

Despite (minor) differences like eastl, this is the same code base/3d engine.
So it would be better for the userbase and devs both if efforts are not duplicated.
You seem to devilify rbfx. I don't believe that's rational.

-------------------------

1vanK | 2020-12-08 17:51:22 UTC | #54

There is no duplication of effort, code is ported from two repositories in both directions.

-------------------------

adhoc99 | 2020-12-08 17:59:40 UTC | #55

Wouldn't it be more rational just to use rbfx instead of having to implement major breaking changes to current Urho3D?

-------------------------

Lcbx | 2020-12-08 18:04:34 UTC | #56

The implementation is already done. We're talking about a merge, which isn't much work. And I answered to that [already](https://discourse.urho3d.io/t/re-to-rbfx-and-not-to-rbfx/6605/53?u=lcbx).

-------------------------

Lcbx | 2020-12-08 18:07:11 UTC | #57

Welp I don't think this will be solved today. feel free to close the thread.

-------------------------

JSandusky | 2020-12-09 07:39:59 UTC | #58

.NET Native AOT is totally worth selling one's soul to a lifetime of adoring MS. Even while a buggy mess it's still a hundred times better than a ten mile long esoteric log for a handful of template errors.

You can run BEPU Physics as fast native Bullet, the whole thing is nuts.

-------------------------

1vanK | 2020-12-09 07:51:32 UTC | #59

.net is very fast until it runs out of memory. After that, the permanent StopTheWorld begins.

-------------------------

rku | 2020-12-09 19:35:43 UTC | #60

eastl string is great. Also I kept Urho3D smart pointers because moving away from those proved to be too difficult. Maybe one day, but not today.

-------------------------

1vanK | 2020-12-09 19:51:17 UTC | #61

If eastl strings are so great, why didn't you adapt them for your engine? Why all your functions outside string class?

At the same time, you were able to modify the terrible RefCounted for your engine. When you go to great eastl smart pointers, will the new functionality be outside the class too?

-------------------------

rku | 2020-12-09 19:56:08 UTC | #62

We did add extra functions to string class. Only few utf-8 ones are outside due to obvious reasons.

I don't recall details regarding smart pointers in eastl. Not sure if there is intrusive variant. If there isn't then there may be nothing left to do othert han sticking to current implementation.

-------------------------

1vanK | 2020-12-09 20:04:47 UTC | #63

> We did add extra functions to string class. Only few utf-8 ones are outside due to obvious reasons.

The reasons are not obvious to me. In Urho3D utf-8 is the internal encoding for strings (like UTF-16 is internal encoding for .net).

What is the internal encoding in your engine?

-------------------------

Modanung | 2020-12-09 21:38:07 UTC | #64

Does it introduce support for dextrosinistral writing systems?
[spoiler]Also, did anyone try [Klingon](https://www.evertype.com/standards/csur/klingon.html) by now?[/spoiler]

-------------------------

Modanung | 2020-12-09 21:40:01 UTC | #65

Btw, in [**Dry**](https://en.wiktionary.org/wiki/dry#Old_English) `String::Empty()` was renamed to `String::IsEmpty()`, for the sake of consistency.
"Breaks" things though.

...and `IntVector#`s are converted to float vectors in calculations, just as separate `int`s would be.

-------------------------

Eugene | 2020-12-09 21:53:42 UTC | #66

[quote="1vanK, post:63, topic:6605"]
In Urho3D utf-8 is the internal encoding for strings
[/quote]
It's not. You cannot do `str[2]` in Urho and expect it to pick 3rd UTF-8 character from string. Same with all other string functions. They don't care about string being in UTF-8.

I would say, ASCII is internal encoding for strings in Urho, same as in EASTL.
It just so happens that UTF-8 and ASCII are kind of compatible.

[quote="1vanK, post:61, topic:6605"]
you were able to modify the terrible RefCounted for your engine. When you go to great eastl smart pointers
[/quote]
EASTL has no equivalent of Urho WeakPtr/SharedPtr/RefCounted.
What did you expect to happen?
To have `RefCounted` replaced... with what exactly?

-------------------------

1vanK | 2020-12-09 22:05:53 UTC | #67

> EASTL has no equivalent of Urho WeakPtr/SharedPtr/RefCounted.

I thought it was the ideal library... It turns out that you have replaced one imperfect library with another imperfect library.

-------------------------

1vanK | 2020-12-09 22:10:06 UTC | #68

> It’s not. You cannot do `str[2]` in Urho and expect it to pick 3rd UTF-8 character from string

What encoding are characters extracted from a string in when rendering text?

-------------------------

Eugene | 2020-12-09 22:29:56 UTC | #69

[quote="1vanK, post:67, topic:6605"]
I thought it was the ideal library…
[/quote]
I don’t know who told you that EASTL is perfect library...
It just offers about 10 times as much as Urho containers and I find it quite convenient when writing code.

 [quote="1vanK, post:68, topic:6605"]
What encoding are characters extracted from a string in when rendering text?
[/quote]
If I remember correctly, Urho treats string contents as UTF-8, converts it to UTF-32 and then does the rendering. Urho text renderer works with UTF-8 string as input, but String doesn’t know anything about it.

-------------------------

1vanK | 2020-12-09 22:34:23 UTC | #70

> Urho treats string contents as UTF-8

Exactly.

For any input / output (localization, clipboard, input, rendering), strings are interpreted as UTF-8 without any checks. The engine does not even expect that there may be some other coding. But of course that does not mean that the internal encoding is UTF-8.

-------------------------

1vanK | 2020-12-09 22:43:43 UTC | #71

[quote="Eugene, post:66, topic:6605"]
I would say, ASCII is internal encoding for strings in Urho, same as in EASTL.
It just so happens that UTF-8 are kind of compatible.
[/quote]

Windows-1251, CP866 are ASCII compatible, so maybe Urho3D works with it?

-------------------------

JSandusky | 2020-12-09 22:48:31 UTC | #72

RogueWave STL is the only good STL, like any good STL, it doesn't even know what UTF-8 is. As all things should be.

-------------------------

1vanK | 2020-12-09 23:00:00 UTC | #73

STL is ThirdPary library. In Urho3D all ThirdPary libraries are wrapped. When you use Urho3D, you are not accessing Bullet and Box2D directly, you are not accessing SDL and Recast directly. In Urho3D we use UTF-8. So need we wrap std::string ?

-------------------------

Eugene | 2020-12-09 23:01:03 UTC | #74

[quote="1vanK, post:71, topic:6605"]
Windows-1251, CP866 are ASCII compatible, so maybe Urho3D works with it?
[/quote]
String as container can keep all these formats. Urho classes just cannot work with them. 

UTF-8 support in Urho is at the level of public API (I.e. class methods), while internal format of String is just ASCII-like something.

-------------------------

1vanK | 2020-12-09 23:04:39 UTC | #75

From this point of view, why did you decide that String knows something about ASCII?

-------------------------

JSandusky | 2020-12-09 23:27:32 UTC | #76

[quote="1vanK, post:73, topic:6605"]
In Urho3D all ThirdPary libraries are wrapped.
[/quote]

Which is the single most terrible thing in the entirety of Urho3D.

[quote="1vanK, post:73, topic:6605"]
STL is ThirdPary library
[/quote]

There would probably be a lot less debate about this if Urho's TL (JTL as I call it, because it's junk) were a an external library (along with the math and core data types) eliminating most of the code-sharing headaches that rise up in real-world pipeline projects.

-------------------------

1vanK | 2020-12-09 23:32:38 UTC | #77

[quote="JSandusky, post:76, topic:6605"]
Which is the single most terrible thing in the entirety of Urho3D.
[/quote]

How would you change this? How it should look like, for example, adding a node with a physical body in a user's application with a direct call Bullet functions and conversion btVector3 to Urho3D::Vector3 every time?

-------------------------

JTippetts1 | 2020-12-10 00:28:18 UTC | #78

I know I'm just a user here, but part of what has always annoyed me about Urho3D is the custom containers. I don't believe that containers should be encapsulated or wrapped, unlike the other ThirdParty bits, and I think that any containers you do use should be compatible with C++ language constructs. I'm not 100% sold on EASTL itself, but at least it supports standard library naming conventions so that switching to the standard library, or using C++ iteration constructs, is possible.

-------------------------

1vanK | 2020-12-10 01:10:07 UTC | #79

No professional engine uses STL. But we need to ignore the needs of our engine and use other people's libraries that do not fully suit us.

-------------------------

rku | 2020-12-10 06:00:11 UTC | #80

[quote="1vanK, post:77, topic:6605"]
How would you change this? How it should look like, for example, adding a node with a physical body in a user’s application with a direct call Bullet functions and conversion btVector3 to Urho3D::Vector3 every time?
[/quote]

Things should be wrapped, but within a reason. It makes sense with bullet, but for example we wrapped next to nothing for RmlUi because it's a lot of stuff and we ironed out type compatibility. There are times when you do need full power of library api. Same is true for bullet. Try doing something complicated, I do not believe everything is possible without including bullet headers.

[quote="1vanK, post:79, topic:6605"]
No professional engine uses STL.
[/quote]
Frostbite (eastl), proprietary engine used by Black Desert (stdlib). Just a few that come to mind. Take any game from those companies it will be using stl I bet.

-------------------------

Eugene | 2020-12-10 08:10:12 UTC | #81

[quote="1vanK, post:77, topic:6605"]
How it should look like, for example, adding a node with a physical body in a user’s application with a direct call Bullet functions and conversion btVector3 to Urho3D::Vector3 every time?
[/quote]
`RigidBody` is not just `btRigidBody` with Urho types and Urho-style names, it's much more. It is component of rigid body implemented via `btRigidBody`.

It's quite silly to have "wrapper" that does nothing expect... well... wrapping.
Wrapping is a tool, not a goal.

[quote="1vanK, post:73, topic:6605"]
In Urho3D we use UTF-8. So need we wrap std::string ?
[/quote]
What kind of functionality you want to add to std::string by wrapping?
These ones?
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Container/Str.h#L452-L472

-------------------------

1vanK | 2020-12-10 09:12:14 UTC | #82

StartsWith, ReplaceAll, Join, TrimStart, TrimEnd() etc etc etc

-------------------------

Eugene | 2020-12-10 09:29:22 UTC | #83

We added all this stuff directly to EASTL classes.
This was part of the reason why EASTL is better suited for our goal than STL.
It's a shame C++ standard doesn't have such basic methods in standard string type.

-------------------------

Modanung | 2020-12-10 11:58:16 UTC | #84

With `std::basic_string`, `+`, `+=` and `append` concatenate. C++20 introduces `starts_with` and `ends_with` functions to it. [`erase`](https://en.cppreference.com/w/cpp/string/basic_string/erase) is quite powerful in that it can do all your trimming.
https://en.cppreference.com/w/cpp/string

-------------------------

1vanK | 2021-02-23 21:33:51 UTC | #85

[quote="Eugene, post:9, topic:6605"]
AS is assembly library and it cannot work without platform-specific assembly code implemented by AS maintainers. I don’t think it caused actual issues with Urho, but I don’t like this kind of dependency. I just don’t want to rely on portability of assembler library in year 2020.
[/quote]

 https://www.angelcode.com/angelscript/sdk/docs/manual/doc_generic.html

-------------------------

Eugene | 2021-02-24 07:16:28 UTC | #86

Okay, it’s nice that AS has fallback route that doesn’t depend on ASM. Can Urho work on this fallback route only? Perhaps in new bindings?

-------------------------

1vanK | 2021-02-24 08:16:20 UTC | #87

Yes.

The engine used generic calling functions on some platform (WEB, ARM64). After the last workaround of VS bugs, this mode is available on any platform.

https://github.com/urho3d/Urho3D/commit/711053d293183d4d94cd043c5b7cdce0926727bc

New bindings are not needed, as there is a set of macros that wraps functions automatically.

-------------------------

George1 | 2021-02-24 10:30:23 UTC | #88

elix22 have updated UrhoSharp...  The .net binding is generated.  See his post.

https://discourse.urho3d.io/t/urho-net-c-cross-platform-game-development-framework/6674

Actually C# is not bad.

-------------------------

WangKai | 2021-02-24 12:32:52 UTC | #89

The renderer imrovements @Eugene has been doing on rbfx seems very promising. I wonder if these changes would go to upstream Urho3d? 

Thanks!

-------------------------

adhoc99 | 2021-02-24 12:57:46 UTC | #90

Yes, [it's bad](https://docs.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/).
[Really bad](https://docs.microsoft.com/en-us/dotnet/core/tools/telemetry).
[Really really bad](https://github.com/mono/mono/issues/16875).
[Really really really bad](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/csharpcore-gpp.html).

-------------------------

adhoc99 | 2021-02-24 13:00:12 UTC | #91

Since rbfx is so promising, why not use rbfx instead.

Also, apparently Github has "forum" ([Discussion tab](https://docs.github.com/en/github/administering-a-repository/enabling-or-disabling-github-discussions-for-a-repository)) support now. Maybe ask rbfx to enable it on their Github so they can finally have a forum.

-------------------------

1vanK | 2021-02-24 13:15:42 UTC | #92

[quote="adhoc99, post:91, topic:6605"]
Also, apparently Github has “forum” ([Discussion tab](https://docs.github.com/en/github/administering-a-repository/enabling-or-disabling-github-discussions-for-a-repository)) support now. Maybe ask rbfx to enable it on their Github so they can finally have a forum.
[/quote]

It looks interesting. Is it possible to download a forum using a git client the same way as wiki?

-------------------------

WangKai | 2021-02-24 13:21:48 UTC | #93

[quote="adhoc99, post:91, topic:6605"]
Since rbfx is so promising, why not use rbfx instead.
[/quote]

Hi @adhoc99 , don't misunderstand me, I'm working on Urho3D some times and recently just contributed a little to the project when I got some vocation. 

If you look at the rendering subsystem of Urho3D closely, you'd find there is surely need more work. For the future of Urho, it needs improvements, a lot. Additionally, Eugene is also one of the main maintainers of Urho for a long time.

-------------------------

adhoc99 | 2021-02-24 13:41:36 UTC | #94

I took a look at the [Discussion documentation](https://docs.github.com/en/discussions) but couldn't find an option for that at the moment. Apparently [it looks more like the issue system](https://docs.github.com/en/discussions/managing-discussions-for-your-community/managing-discussions-in-your-repository) than the wiki system.

-------------------------

Eugene | 2021-02-24 13:47:51 UTC | #95

[quote="WangKai, post:89, topic:6605"]
The renderer imrovements @Eugene has been doing on rbfx seems very promising. I wonder if these changes would go to upstream Urho3d?
[/quote]
I don't really see a point in talking about it now, since upstream community has *already* declined to accept these changes.

We had [this discussion](https://discourse.urho3d.io/t/to-rbfx-and-not-to-rbfx/5864) year ago, and *significant* portion of Urho community has refused to accept breaking changes from the fork to upstream repo. And I respect others' choises even if I don't agree with them.

-------------------------

George1 | 2021-02-25 01:51:35 UTC | #96

I know that you are afraid of telemetry, but elix22 work is not Microsoft's work.

Everything you do now a day is monitored.  E.g. Google record everything you do on android phone, Windows record things you do on windows,   Apple record everything you do on Apple's phone etc... Now stop using them.  When you go to the web, website track your interest with AI and display your last view items.  Now, do you stop using the internet too?

.Net core is opensource.   Just disable what ever function you wanted...

-------------------------

JSandusky | 2021-02-25 02:04:47 UTC | #97

Guess we have to run in terror at v1 and v2 UUIDs because how dare someone other than me be able to use hard work to figure out my mac-address from a bunch of UUIDs ... when my mac address is already used pretty much everywhere /s.

Telemetry and sysinfo arguments are tiresome because when someone complains about basic telemetry data they're likely also complaining about Wirth's Law or "*planned obsolescence*" somewhere else. 

Do you expect platform vendors to just magically divine the decisions they need to make in regards to their targets to support?

The last time MS made "*magical*" decisions ... we got Silverlight.

-------------------------

adhoc99 | 2021-02-25 02:34:02 UTC | #98

No, just not oblivious to it. Some people actually care about privacy.

Maybe use Startpage or DuckDuckGo instead of Google, LineageOS instead of Android, Linux instead of Windows or MacOS, Firefox instead of Chrome, and NoScript, uBlockOrigin, TOR, /etc/hosts, etc.

And being opensource doesn't make it good in the slightest. It and C# are still horribly slow.

-------------------------

George1 | 2021-02-25 02:53:02 UTC | #99

duckduckgo knows everything you do.  When you are on the internet, really there is no privacy.

How big is the game you are making? 100 players?  1000 players?  The wrapper is auto generated, so if you are developing in C++ then it does not effect you.

-------------------------

throwawayerino | 2021-02-25 06:22:18 UTC | #100

Telemetry is what's bothering you people? If anything, I'm against C# simply because it requires another compiler. Angelscript is interpreted letting you edit it faster and could be later compiled for release

-------------------------

Eugene | 2021-02-25 06:43:53 UTC | #101

[quote="throwawayerino, post:100, topic:6605"]
I’m against C# simply because it requires another compiler
[/quote]
I don't like C# simply because `¯\_(ツ)_/¯`
I just like C++ more, nothing else.

Yes, you have good point too. C# introduces too much build complexity into project, I just don't trust it to be reliable and stable.

-------------------------

