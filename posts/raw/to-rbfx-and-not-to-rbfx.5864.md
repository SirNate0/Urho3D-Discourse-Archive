Eugene | 2020-02-08 00:32:43 UTC | #1

Hi everyone.

In this topic I want to discuss fork of Urho3D known as **rbfx** and possible feature merge from rbfx back into original Urho3D. This topic is _not_ a proposal or announcement but the opening of discussion.
I really don’t believe rbfx and vanilla can be merged completely, but I’d like to bring them as close as possible.

In case you have no idea what I'm talking about, here is the link to rbfx:
 https://github.com/rokups/rbfx

---

Initially rbfx was quite close to original Urho3D (I will call it vanilla from now on) in terms of codebase and feature set.

However, the divergence grows as time goes on.

And this divergence becomes really annoying for users of both projects.

I cannot make wide-scope changes in rbfx because it will make things even worse than they are now. I cannot merge my changes into vanilla because it would require tedious rework of codebase. Users of both projects cannot simply switch back and forth because API is already incompatible to a certain degree: it’s nearly impossible to write code working both on vanilla and rbfx.

Oh, I hate forks soo much. And I don't want to repeat the story of Atomic.

---

#### What does **rbfx** offer and why bother?

There are several major and multiple minor features, including native Editor (WIP), _automatic_ C# bindings, [built-in lightmapper that you all have probably seen](https://discourse.urho3d.io/t/ready-to-use-lightmapper-and-light-probe-baker/5844/1), universal user-friendly serialization from/to binary/XML/JSON instead of this terrible (and sometimes broken) x6 copy-paste in vanilla Urho, profiler, type-safe logging and string formatting using `fmt`, subdirectory support by build system and so on and so on.

I’m planning to do some major renderer changes too, but I won’t make any promises here.

#### What’s the problem with “just merging” everything back into vanilla Urho?

Short story: there are breaking changes. A lot. And a lot of dependencies between features too.

So it’s actually impossible to merge rbfx into vanilla “by bits”: it’s a package deal, and the package is huge.

1) The broadest (in terms or API affected) breaking change is using EASTL standard library instead of custom Urho containers. Yeah, Urho containers may have some nice features, but they are sorely lacking compared to EASTL or STL libraries. I personally switched to rbfx just because it’s so much easier to write code with standard containers. Maybe in the future it would even be possible to take the next step and switch to STL completely.

   This change is mandatory to merge anything else from rbfx into vanilla Urho. It will also require certain rework in script bindings. Lua would probably be easy to fix because it has compile-time type checks. AS would be more painful. Speaking of which...

2) The biggest (in terms of functionality) breaking change in rbfx: AngelScript is gone. Forever.

   You see, AS is _assembly_ library. Just think about it. Urho is using _raw assembly_ right now in 2020. Not just for optimization, but as scripting core. AS has _zero_ compile-time type safety, so if you make a mistake or forget to update some _manually written_ binding code, you will get real-time crash, or UB, or data corruption, or anything. Manual and fragile bindings to AS greatly decrease code maintainability.

   Consequently, vanilla Urho Editor is gone. Yeah, writing Editor basing on AS scripting sample was a mistake. It’s sad because vanilla Editor is quite nice and has a lot of features. But it is really hard to extend due to poor architecture and using AS bindings instead of propper C++.

   _Theoretically_, it’s possible to merge stuff from rbfx and keep AS and vanilla Editor. However, I’m not going to do anything for it -- neither to fix conflicts on merge nor support manual bindings, ever. Feel free to volunteer for this task.

---

So, what do you think?
Is it worth a shot, or I want too much?
Is it better to try to bring rbfx and Urho closer or let them diverge forever, essentially becoming separate projects?
It's not too late yet, but every major update in rbfx will make things more complicated than they are now.

Here are some polls.

#### About possible merge
[poll type=regular results=always public=true chartType=bar]
* [against] I’m fine with current state of Urho (stagnation) and I don’t care about any changes;
* [against] I want changes in Urho but I don't want to merge anything from rbfx;
* [tentative] I want to get breaking changes from rbfx as long as Urho doesn’t suffer _any_ feature cut;
* [supportive] I want to get breaking changes from rbfx and I’m ready for a reasonable feature cut (e.g. removing AS);
* [supportive] I’m already using rbfx and I want to get code merged back into Urho;
* [skip] I don't care
* [impossible] I want to get changes from rbfx as long as it doesn't break any API
[/poll]

#### And about AngelScript specifically (assuming that you will get native Editor as replacement):

[poll name=poll2 type=regular results=always public=true chartType=bar]
* I don’t care about AS;
* I’d like to have AS but I can deal with its removal;
* I _need_ AS support and I’m ready to maintain it;
* I _need_ AS support and I don’t want to do anything to maintain it;
[/poll]

---

Damn, I've spent hours writing this chunk of text. Please don't ignore it. Thanks.
I'm summoning here all ppl I can think of.

@rku, @weitjong, @Modanung, @Miegamicis, @JTippetts, @JTippetts1 (I have no idea who is real you), @boberfly, @Dave82, @Lumak... And I hit the limit of mentions, sorry if you aren't listed here. I'd summon @cadaver too, but I don't think he have strong opinion on the subject.

-------------------------

Modanung | 2020-02-05 12:37:34 UTC | #2

As long as that C# filth stays far away...

-------------------------

Miegamicis | 2020-02-05 13:18:22 UTC | #3

Here are my 2 cents of this proposal. 

It was actually one of my plans to get some parts of the rbfx back to the Urho. It has a lot of nice features that Urho lacks. It's sad seeing AS go, but I guess it's the right thing to do.

I know there are a lot of guys out there who don't want to see the C# support in it, but I guess it's fine as long as it's a optional dependency and by default the engine is built without it. (note: I'm not too excited about it either)

-------------------------

JTippetts1 | 2020-02-05 13:17:47 UTC | #4

I have so far been completely unbothered by the presence of the C# stuff. Was skeptical at first, but it really is separate.

-------------------------

Modanung | 2020-02-05 13:50:05 UTC | #5

[quote="Miegamicis, post:3, topic:5864"]
I guess it’s fine as long as it’s a optional dependency and by default the engine is built without it.
[/quote]

I believe this would be a foot in the door of a slippery slope to soullessness.

-------------------------

rku | 2020-02-05 13:37:11 UTC | #6

`-DURHO3D_CSHARP=OFF` :heart:

-------------------------

Modanung | 2020-02-05 14:09:20 UTC | #7

@rku Or people could be pointed to **rbfx** for that. I believe this is exactly the dispute that *inspired* you to fork Urho in the first place, correct?
Most other effort stuck into rbfx could have been applied to Urho3D.

[details=Fish Executioner]
> Flash of the knife, on top of a pizza box
Divide the fish into two
Eyes and mouth slowly open and close
Even after the mutilation
>
> Unceremoniously into trash
But the spirit remains to haunt
Fear for the day when it returns from the dead
And traps you into a net
>
> Two fish halves on top of a pizza box
Motion not yet ending
Electric impulses or proof of afterlife?
Never know for sure
>
> [Fish Executioner!](http://mikseri.net/artists/urho/fish-executioner/364603/)
Death to be done on this blasphemous day
[Fish Executioner!](http://mikseri.net/artists/urho/fish-executioner/364603/)
Face of the dead fish will never go away
[/details]

-------------------------

Miegamicis | 2020-02-05 14:45:17 UTC | #8

It's actually a technical question, we can't make our decision based on our emotions or religious beliefs. Nothing is decided yet, we as a comunity have to agree what's best for the engine.

-------------------------

SirNate0 | 2020-02-05 14:47:26 UTC | #9

In regards to removing AngelScript, is C# a usable replacement if the only use was in a handful of scripted components and plugin type things called from within C++ code, or does the C# code have to be the main application?
Is there a way to do something like `CallCSharpFunction("doStuff(int)", 42)` and get the result?

-------------------------

adhoc99 | 2020-02-05 14:51:29 UTC | #10

Hello, this is my first time using the forum although I have been using Urho3D for about 2 or 3 years now.

I would like to say that I think that this proposal is a very radical change.

Although I have seen rbfx mentioned before on the forum, I never took a close look at it until now.
And seeing C# and that WYSIWYG editor that looks like Unity sent shivers down my spine.

I fear that bringing C# to Urho3D will turn this into a nightmare, and, in time, will root itself permanently into the core of the engine.
Given how traumatic apparently merging the changes from rbfx to Urho3d will be, I am afraid that that will almost certainly be the case.

To be quite honest, I would like to see even AngelScript and Lua completely removed from the engine.
C/C++ is not that hard and it tends to force the developer to know what he is doing and to program properly and efficiently.

In my opinion, bringing C# and WYSIWYG to Urho3D is steering the ship on the very opposite direction of what Urho3D is now.

I only ask that if this goes forward, please, announce it early so those that don't like this direction can have time to fork Urho3D or move to some other engine or library.

-------------------------

WangKai | 2020-02-05 14:59:05 UTC | #11

I don't like AS because it has no IDE or real useful debugger which supports urho. I don't see scripting is useful in a serious project without IDE support. I don't like C# because it is heavy and pain to maintain? Though its IDE and stuff would be much better.

Urho's container is good IMO, light weight as Urho itself. Not as powful, but easy to read and use. Just like Urho. Why we like Urho, because it is simple and nice. Otherwise I would just use UE4, Unity or Godot.

The worst thing about Urho is Editor and workflow. IMHO, rbfx is better in some aspects is because the brave author has been really working hard on it.

If Urho also has a IMGUI based editor, people would be much optimistic.

-------------------------

rku | 2020-02-05 15:02:15 UTC | #12

[quote="SirNate0, post:9, topic:5864, full:true"]
In regards to removing AngelScript, is C# a usable replacement if the only use was in a handful of scripted components and plugin type things called from within C++ code, or does the C# code have to be the main application?
Is there a way to do something like `CallCSharpFunction("doStuff(int)", 42)` and get the result?
[/quote]

C# bit uses sort of a "hack" where main exe is .NET. This is so we can support multiple runtimes without writing code to host managed runtime. This is just a detail though. You can write most of your code in a `.dll`. Editor is a good example of large native application that gets loaded as a DLL. You do not even notice that it isnt a native exe.

`CallCSharpFunction` bit is possible (terms and conditions apply!), but someone needs to write it.

[quote="adhoc99, post:10, topic:5864"]
In my opinion, bringing C# and WYSIWYG to Urho3D is steering the ship on the very opposite direction of what Urho3D is now.
[/quote]
You do not have to use it as it is optional.

-------------------------

Modanung | 2020-02-05 15:02:20 UTC | #13

@adhoc99 Hear hear and welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

lebrewer | 2020-02-05 15:04:02 UTC | #14

Why is merging rbfx stuff back into Urho necessary? They're essentially different engines, with different goals. If people like rbfx, why not continue using it and supporting it?

-------------------------

rku | 2020-02-05 15:08:24 UTC | #15

It is not necessary. It is just merely an offer to progress the project.

-------------------------

WangKai | 2020-02-05 15:09:36 UTC | #16

"There are several major and multiple minor features, including native Editor (WIP),  *automatic*  C# bindings, [built-in lightmapper that you all have probably seen](https://discourse.urho3d.io/t/ready-to-use-lightmapper-and-light-probe-baker/5844/1), universal user-friendly serialization from/to binary/XML/JSON instead of this terrible (and sometimes broken) x6 copy-paste in vanilla Urho, profiler, type-safe logging and string formatting using  `fmt` , subdirectory support by build system and so on and so on."

I'm using my phone to type. To me, many of the features seems can be implemented without breaking the vinila and some are still optional.

-------------------------

Eugene | 2020-02-05 15:31:34 UTC | #17

[quote="adhoc99, post:10, topic:5864"]
In my opinion, bringing C# and WYSIWYG to Urho3D
[/quote]
This is quite funny to read about "bringing WYSIWYG to Urho3D" because vanilla Urho Editor _is_ the stereotypical example of WYSIWYG editor.

[quote="adhoc99, post:10, topic:5864"]
I fear that bringing C# to Urho3D will turn this into a nightmare, and, in time, will root itself permanently into the core of the engine.
[/quote]
How on Earth can it happen if is impossible to even build C# in some supported configurations?

[quote="WangKai, post:11, topic:5864"]
Urho’s container is good IMO, light weight as Urho itself. Not as powful, but easy to read and use.
[/quote]
Unusual point of view. I wouldn't say Urho containers are easy to use. They have maybe 5% of EASTL functionality and I had to write several times more code with Urho containers.
And this is after all the time we (me including) spent on improving these containers.

[quote="lebrewer, post:14, topic:5864"]
They’re essentially different engines
[/quote]
When two engines share 95% of codebase, I cannot really call them "different".

[quote="lebrewer, post:14, topic:5864"]
If people like rbfx, why not continue using it and supporting it?
[/quote]
Because it is a waste of manpower to split efforts on two projects when same effort can be spent on one.

[quote="WangKai, post:16, topic:5864"]
I’m using my phone to type. To me, many of the features seems can be implemented without breaking the vinila and some are still optional.
[/quote]
It is possible to merge these features without breaking vanilla, true.
If someone is ready to do tedious _manual_ merge every time either rbfx or Urho3D are updated.
Who is going to do that?

-------------------------

lebrewer | 2020-02-05 15:32:20 UTC | #18

So, you're basically saying that you want Urho3D to be rbfx.

-------------------------

Eugene | 2020-02-05 15:34:07 UTC | #19

I basically said the opposite in the very first paragraph of this topic.

-------------------------

WangKai | 2020-02-05 15:42:51 UTC | #20

I won't miss rbfx since we have urho. Is it because of the underlying container change which makes feature merge difficult? Brave  move for rbfx at the first place. I respect the author but dislike the change of stl introduction based on the destroy.
.

-------------------------

Modanung | 2020-02-05 16:30:05 UTC | #21

[quote="lebrewer, post:14, topic:5864"]
Why is merging rbfx stuff back into Urho necessary? They’re essentially different engines, with different goals.
[/quote]
Indeed - with **rbfx** having diverged as much as it apparently has - it should probably not be considered much different from the other open source engines out there with a compatible license when it comes to adopting certain features.
Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:
  
[quote="Eugene, post:17, topic:5864"]
Because it is a waste of manpower to split efforts on two projects when same effort can be spent on one.
[/quote]

That's a reason not to fork.

-------------------------

Eugene | 2020-02-05 16:06:59 UTC | #22

[quote="WangKai, post:20, topic:5864"]
Is it because of the underlying container change which makes feature merge difficult?
[/quote]
Yes, mostly this.

[quote="WangKai, post:20, topic:5864"]
I respect the author but dislike the change of stl introduction based on the destroy
[/quote]
If we are talking about some feature, e.g. container library, it can be in 4 states.

0) It may be completely finished.
1) It may stagnate (this is what happening with Urho Containers now)
2) It may be supported (thats what we did with Urho Containers before, e.g. I added move semantics for Vector)
3) It may be delegated to 3rd party (like we did in rbfx)

I personally cannot understand why choose to stagnate when there is available option of developement. This should be default way to go -- to delegate support if there is reasonably lightweight open-source 3rdparty. We don't have custom physics or custom image decoder. Why have custom containers?..

And Urho containers are not finished, they are missing a lot of features.
Small buffer optimization? Forget that. Allocators? Nah. Algorithms? Nope. Containers except vector and hash map? No, there is none. Move semantics? Barely. Spans and string views? Phew, nope, we will write copy-pasted `foo(const char*)` and `foo(const String&)` instead.
I would have never finished my lightmapper if I had to deal with ever-lacking custom container library.

[quote="Modanung, post:21, topic:5864"]
That’s a reason not to fork.
[/quote]
That's why I hate forks. Always said this much.

-------------------------

johnnycable | 2020-02-05 16:11:39 UTC | #23

Are there any changes in the rendering system in rbfx that can impact urho?
Will we able to alter the rendering system in the future, for instance by adding [angle-vulkan-metal](https://discourse.urho3d.io/t/metal-moltenvk-support-for-ios-an-mac-devices/4845) support? Or whatever else?

-------------------------

Eugene | 2020-02-05 16:14:26 UTC | #24

rbfx core is almost identical to vanilla Urho, including renderer.
The biggest change is lightmap/light probe support and even this is only a dozen of lines here and there.

-------------------------

Modanung | 2020-02-05 16:26:57 UTC | #25

[quote="Eugene, post:22, topic:5864"]
That’s why I hate forks. Always said this much.
[/quote]
Hygienic forks can be healthy extensions. :wink:

-------------------------

adhoc99 | 2020-02-05 16:33:41 UTC | #26

@Modanung Thank you!

[quote="lebrewer, post:14, topic:5864, full:true"]
Why is merging rbfx stuff back into Urho necessary? They’re essentially different engines, with different goals. If people like rbfx, why not continue using it and supporting it?
[/quote]
[quote="lebrewer, post:18, topic:5864, full:true"]
So, you’re basically saying that you want Urho3D to be rbfx.
[/quote]
I totally agree.

@Eugene But the Urho3D Editor is not required at all, neither it ever appeared to be the focus. Always thought it was just one of the samples of the Engine.

You say that both engines share 95% of the codebase, but also that the merge would be package deal.
I have to ask, for that 5% difference, why does Urho3D have to change to accommodate rbfx?
Why doesn't rbfx change themselves instead to be compatible with current Urho3D?
The EASTL change is, at best, debatable.

Please, do not take this the wrong way, but, in corporate terms, this almost looks like a "hostile takeover".

It's like SystemD all over again.

-------------------------

rku | 2020-02-05 16:35:42 UTC | #27

[quote="adhoc99, post:26, topic:5864"]
“hostile takeover”
[/quote]

I am offended. Hostile takeover would be us pushing rbfx and making Urho3D obsolete. Which is happening already.

-------------------------

adhoc99 | 2020-02-05 16:42:27 UTC | #28

Well, that is exactly what I feel when a project requires another project to change considerable itself instead of changing themselves.

-------------------------

Eugene | 2020-02-05 16:45:59 UTC | #29

[quote="adhoc99, post:26, topic:5864"]
But the Urho3D Editor is not required at all, neither it ever appeared to be the focus. Always thought it was just one of the samples of the Engine
[/quote]
And this is one more issue of vanilla Urho -- it doesn't have real full-featured Editor.
If you personally don't need it, it's not the reason to deprive others from this feature.

[quote="adhoc99, post:26, topic:5864"]
I have to ask, for that 5% difference, why does Urho3D have to change to accommodate rbfx?
[/quote]
EASTL, plus we are not going to maintain AS in any way.

[quote="adhoc99, post:26, topic:5864"]
Why doesn’t rbfx change themselves instead to be compatible with current Urho3D?
The EASTL change is, at best, debatable.
[/quote]
I see only two options of developenet here.
Either someone is willing to make Urho Containers as usable as EASTL, including all the features I mentioned above, or we are delegating this piece of maintenance to 3rdparty (e.g. EASTL).

I don't see any volunteers for the first option, so it's not like I have any choice.
I also don't consider stagnation as an option. Users who are willing to stagnate can always use outdated branch or fork.

-------------------------

adhoc99 | 2020-02-05 16:47:01 UTC | #30

[quote="Eugene, post:29, topic:5864"]
I don’t see any volunteers for the first option, so it’s not like I have any choice.
[/quote]

Why would anyone volunteer to change something that works well to support something they do not want.

And what about the choice if not merging rbfx at all. Unless that's not an option.

-------------------------

Modanung | 2020-02-05 16:51:53 UTC | #31

[quote="rku, post:27, topic:5864"]
Hostile takeover would be us pushing rbfx and making Urho3D obsolete. Which is happening already.
[/quote]

What made Urho3D *not* obsolete for you, when first encountering it? Why not go Godot?
To me, **rbfx** is just one among a myriad of comparable options. It no longer stands out, unlike Urho.

-------------------------

lebrewer | 2020-02-05 16:49:21 UTC | #32

[quote="rku, post:27, topic:5864"]
I am offended. Hostile takeover would be us pushing rbfx and making Urho3D obsolete. Which is happening already.
[/quote]


That's your biased opinion. Urho is alive and well and widely used. Just because a fork has bells and whistles doesn't mean the original is dying or becoming obsolete.

As for the EASTL vs. Urho, that's a discussion that should be done separately. Outsourcing complex things is one of the things Urho does well (very good libraries being used for many different things). However, I disagree that EASTL is more active than Urho. Just look a their repo: no leadership, no support, no release schedule, nothing. Just a bunch of fixes here and there by users. How is that different from what Urho has today?

-------------------------

Eugene | 2020-02-05 17:08:24 UTC | #33

[quote="adhoc99, post:30, topic:5864"]
Why would anyone volunteer to change something that works well to support something they do not want.
[/quote]
If you need only 5% of container functionality, it's your choise.
There are people who need more.
Why these people have to deal with underimplemented container library?
There's thin line between "lightweight" and "lacking features", and Urho Containers are more second than first.

[quote="adhoc99, post:30, topic:5864"]
And what about the choice if not merging rbfx at all. Unless that’s not an option.
[/quote]
I have created this whole topic for the sole purpose of discussing this question.

[quote="lebrewer, post:32, topic:5864"]
I disagree that EASTL is more active than Urho. Just look a their repo: no leadership, no support, no release schedule, nothing.
[/quote]
Sorry, WTF?.. EASTL is developed by EA (as you could have guessed), it is curated by a person from EA, and they periodically push releases.

[quote="lebrewer, post:32, topic:5864"]
How is that different from what Urho has today?
[/quote]
The difference is that EASTL has about 20 times more features than Urho Containers.
And these features are must have for me.
For example, strings and vectors that don't allocate memory.

And yes, EASTL is also updated. Unlike Urho Containers. HashMap still doesn’t support move semantics.

-------------------------

Modanung | 2020-02-05 17:16:20 UTC | #34

[quote="Eugene, post:29, topic:5864"]
If you personally don’t need it, it’s not the reason to deprive others from this feature.
[/quote]

1. Urho is defined as lightweight; avoiding encumbrance
2. Editor would probably be best as a seperate repository, with pre-built binaries

@Eugene How about `std` containers?

-------------------------

johnnycable | 2020-02-05 17:25:16 UTC | #35

Ok, my (very opinionated) pov:

* angescript - I don't use scripting. I hate scripting. Die!

* C# - same. Moreover, it is going to bring all those *use virtual-machine don't-want-to write-too-much code* pimps into the engine *oh-my-what's-this-make-shared-thing-here*

* Lua (subject-related) Another vm. Ultra-die!

* Python(more subject-related) - could make an *exception* for it as a scripting language. It's on the rampage. Sleep safe C#. Discarded Godot in the first place because *they messed with it so badly...* (and in the second place... when I checked the sources, recoiling in horror)

* editor - I'm on Mac and it never really worked here. So I've learned to live without it. Use Blender. So as you like it.

* stdlib - Of course 10 years ago C11 was in its infancy, so having own containers/std had a meaning. Now no more. C11 works and it's here to stay. Die C!

* light mapper and co. - good and good

* bad behaving forking guys & the forking turf wars - bad and bad

* happy community reunion and following drinking champagne cheers-up - sweet & tender

:cow:  
Lo and behold, [the prodigal son returns](https://www.biblica.com/bible/?osis=niv:Luke.15:11%E2%80%9315:32)...

- ...so basicly ok until Urho's name stays Urho, rbfx is rejoined into Urho, and the engine *political management* doesn't change...

-------------------------

WangKai | 2020-02-05 17:55:43 UTC | #36

I'm not a fan of containers, to me though urho's container is simple to some extent, as long as it is usable, it is good. I used other opensource game engines  before I don't see we are required to use powerful containers. Especially Urho is. C++ based game engine, KISS is an important characteristic among game engines out there. Additionally,  there is no critical features we really need from rbfx, though I love Eugene's embree lightmaping solution. I integrated Beast (lightmap midware Unity usefit before Enlighten, was bought by Autodesk, and dead?)before, I know how important lightmap for most of 3d games.

More importantly, we need better PBR,  Metal, Vulkan, better editor, and lightmaping.

-------------------------

WangKai | 2020-02-05 17:27:39 UTC | #37

Currently, Urho is not very "useble", if we are talking about making a game.

-------------------------

Eugene | 2020-02-05 17:34:13 UTC | #38

[quote="Modanung, post:34, topic:5864"]
@Eugene How about `std` containers?
[/quote]
Well... `std` containers are environment-dependent, they miss some really nice features, especially before C++20, and they cannot be extended with addons and adapters to simplify code migration (like I did in rbfx).

So, about STL in Urho... Maybe in the future -- yes. Now? Nope. EASTL is the first step in this direction anyway.

[quote="WangKai, post:36, topic:5864"]
I’m not a fan of containers, to me though urho’s container is simple to some extent, as long as it is usable, it is good
[/quote]
Well, I used vanilla Urho for years, Urho Containers are ok-ish. But every time I needed something I had to extend them. I have refactored `Vector<T>` two times instead of doing more useful tasks.
So I have legitimate reasons to dislike Urho Containers, if only for time I spent polishing it.

-------------------------

WangKai | 2020-02-05 17:33:18 UTC | #39

[quote="johnnycable, post:35, topic:5864"]
Python(more subject-related) - could make an *exception* for it as a scripting language. It’s on the rampage. Sleep safe C#. Discarded Godot in the first place because *they messed with it so badly…* (and in the second place… when I checked the sources, recoiling in horror)
[/quote]

IMHO, Python s*cks for an multiplatform game engine. There is no light weight and multiplatform VM, and it is very slow general ly. I love its expression and rapid dev, but I can not find a solution till now solve the two critical issues. I think that's why Godot choose to implement a Python look and feel language in the first place.

-------------------------

johnnycable | 2020-02-05 17:41:01 UTC | #40

Sadly that. Just another pointless, slow scripting thing... no use for playing... :confused: :confused: :confused:

-------------------------

WangKai | 2020-02-05 17:46:31 UTC | #41

Basically, AFAIK, there is not clean and fast  way to run Python on Android, iOS and web.

Edit: I'm a fan of Python. I developed a packing tool with 200 loc while my coworker writing 3000 loc with MFC.

-------------------------

WangKai | 2020-02-05 17:48:38 UTC | #42

It's time to bring the dying fish from ICU room who gave us hope and abandoned this project.

-------------------------

SirNate0 | 2020-02-05 17:58:04 UTC | #43

In regards to the containers, there are a few things I like more about the Urho containers (like CamelCase on the function names, which I prefer, and a couple other things I don't remember at the moment), but I would be in favor of switching to a more complete 3rd party solution, as long as we didn't lose features from it. I've run into issues with Urho's containers a couple times, and it would be nice to gain the extra features without having to reinvent the wheel and implement it myself. Beyond that, containers like the stl ones are the most likely to have already made solutions for script bindings, so implementing script bindings in the future could be easier that way (for those of us who do like having script bindings).

So I support switching to the new containers, though I don't necessarily support all of the changes (like removing AngelScript).

-------------------------

WangKai | 2020-02-05 18:12:21 UTC | #44

[quote="Eugene, post:38, topic:5864"]
Well, I used vanilla Urho for years, Urho Containers are ok-ish. But every time I needed something I had to extend them. I have refactored `Vector<T>` two times instead of doing more useful tasks.
So I have legitimate reasons to dislike Urho Containers, if only for time I spent polishing it.
[/quote]
Ue4 use its own containers, if we want them more powerful, heros can improve them. Personally, I prefer keep using current containers or embrace the future and radical change by using cpp std. I used to stay in a team where people wrap STLPort and make their own containers. I guess they want safer interfaces and an unified look & feel with other parts of the engine, or they might find stl is faster, such as memory and cache optimizations.

So about STL or STD or Urho Containers, shall we  start a new thread?

Edit: I don't have such a container sucks experience before, pls educate me.

-------------------------

SirNate0 | 2020-02-05 18:07:28 UTC | #45

Also, @Eugene, could you explain this in more detail, I didn't see any info when I (briefly) checked the rbfx wiki?

[quote="Eugene, post:1, topic:5864"]
universal user-friendly serialization from/to binary/XML/JSON instead of this terrible (and sometimes broken) x6 copy-paste in vanilla Urho
[/quote]

-------------------------

Eugene | 2020-02-05 18:40:22 UTC | #46

[quote="WangKai, post:44, topic:5864"]
So about STL or STD or Urho Containers, shall we start a new thread?
[/quote]

I don't think we need separate thread, because this topic highly corellates with subject.

If we want to stick with Urho containers, then we cannot merge code from rbfx to Urho.

If we want to move to std-like containers, the most reasonable thing is to pick already ported code from rbfx. We don't even need to pick anything else from rbfx: container migration alone will close 90% of the API gap between rbfx and Urho.

[quote="WangKai, post:44, topic:5864"]
Personally, I prefer keep using current containers or embrace the future and radical change by using cpp std.
[/quote]

I see only one issue with `std`. Somebody will need to do huge and tedious work of migration of whole Urho codebase at once. Some parts of code will have to be heavily rewritten, like Variant.
But migration to EASTL is _already done_.
Moreover, once you migrated to EASTL, you can migrate to `std` incrementally, file by file and place by place.

 

[quote="SirNate0, post:45, topic:5864"]
Also, @Eugene, could you explain this in more detail, I didn’t see any info when I (briefly) checked the rbfx wiki?
[/quote]

Here it is.

For complicated objects like `Node` or `Serializable` this looks scary, but this is just one function instead of 6 that do all binary/XML/JSON input and output.

 https://github.com/rokups/rbfx/blob/master/Source/Urho3D/Scene/Node.cpp#L131-L236

For simple user objects serialization is trivial:
https://github.com/rokups/rbfx/blob/master/Source/Urho3D/Math/SphericalHarmonics.cpp#L37-L51
https://github.com/rokups/rbfx/blob/master/Source/Urho3D/Graphics/LightProbeGroup.cpp#L41-L74

-------------------------

adhoc99 | 2020-02-05 21:04:24 UTC | #47

If rbfx already has EASTL, and C# and the WYSIWYG are already implemented there, why not just move there and continue development there?

It looks like the most logical move, since rbfx is already done and working.

I am certain that the success and innovation of the fork will speak for itself and more developers will certainly follow.

P.S.: Stagnation is not necessarily bad. Things do not change and and break constantly.

-------------------------

Eugene | 2020-02-05 21:53:49 UTC | #48

[quote="adhoc99, post:47, topic:5864"]
why not just move there and continue development there?
[/quote]

Are you basically suggesting us to do exactly what we are already doing for last 1..3 years?..
I and some other people "moved there" long time ago and "continued developement there" too.

And guess what? Not everyone is happy that Urho misses some useful contributions that rbfx receives.
You ever considered opinion of people who _both_ want changes and to stay with vanilla Urho?

You are arguing with me as if I'm the one who needs these changes.
_I don't_ need _this merge and I'm not enthusiastic about it because I have already moved to rbfx_.
I just think it would be the most optimal way to utilize resources and I like being optimal.

[quote="adhoc99, post:47, topic:5864"]
It looks like the most logical move
[/quote]
What's the most logical: to split or not to split already small community _second time_?

[quote="adhoc99, post:47, topic:5864"]
P.S.: Stagnation is not necessarily bad. Things do not change and and break constantly.
[/quote]
_Stability_ is not necessarily bad. I'd say, it's good!
Stability is when there are no changes because you have enough and you don't need more.
Stagnation _is bad_.
Stagnation is when changes are needed but they are hindered by obstacles, like container library written for 20 years old technologies or manual fragile bindings with zero compile time checks.

Whether the Urho is stable or stagnating... I'm not sure. I think, in between. It has a lot. It misses a lot.

-------------------------

Modanung | 2020-02-05 21:55:16 UTC | #49

[quote="Eugene, post:47, topic:5864"]
What’s the most logical: to split or not to split already small community *second time*?
[/quote]
Is someone forking **rbfx**? :face_with_raised_eyebrow:

-------------------------

Eugene | 2020-02-05 21:56:31 UTC | #50

[quote="Modanung, post:49, topic:5864"]
Is someone forking **rbfx** ? :face_with_raised_eyebrow:
[/quote]

I was talking about Atomic. It had it's own quite big community, and when it died this community just dispersed into nowhere. I'm not sure how many ppl made it back here.

-------------------------

Modanung | 2020-02-06 12:38:22 UTC | #51

Let's not forget UrhoSharp, another fork which added C# and died. Just like Atomic...

-------------------------

adhoc99 | 2020-02-05 22:01:53 UTC | #52

If they are not happy with Urho3D, why didn't they already move to rbfx, since it has all those amazing improvements everybody must want? Nobody knew about rbfx? Maybe nobody wanted that?

-------------------------

Eugene | 2020-02-05 22:19:12 UTC | #53

[quote="adhoc99, post:52, topic:5864"]
If they are not happy with Urho3D, why didn’t they already move to rbfx
[/quote]
This question is meaningless. People who are "not happy with Urho" moved _already_.

What about people who *both* want changes and to stay with vanilla Urho?
This is the most voted option in the poll, if you didn't notice. People who want changes _and_ want to stay. I was one of such people for a long time. Maybe I still am -- I'll return to vanilla Urho on first opportunity (when it gets _real_ container library and native editor. And no manual bindings because they suck so much).

-------------------------

1vanK | 2020-02-05 22:25:22 UTC | #54

Anyone who votes to removing AS is at the same time voting to removing the console...

-------------------------

Eugene | 2020-02-05 22:29:36 UTC | #55

Can we have lua console? Lua is at least safe and semiautomatic.
And AS removal is not required to merge changes from rbfx as long as someone will patch AS bindings for EASTL. I have no idea how hard it would be.

-------------------------

1vanK | 2020-02-05 22:31:56 UTC | #56

I hate GC and ugly Lua syntax. If need choosing from these two, then I will choose AS

-------------------------

adhoc99 | 2020-02-05 22:34:49 UTC | #57

The question is absolutely relevant. You are assuming everybody wants that. If they did, they would be there already.

Those who want both should really move to rbfx, since it's just 5% different and EASTL is clearly so much better and has so much more development going on.

Yeah, the poll, sample size of what, 15 people? And how many already are on rbfx? I wonder actually how many users even use the forum.

Shouldn't be Urho3D actually asking to be merged into rbfx?

-------------------------

Eugene | 2020-02-05 22:56:34 UTC | #58

[quote="adhoc99, post:57, topic:5864"]
Those who want both should really move to rbfx, since it’s just 5% different and EASTL is clearly so much better and has so much more development going on.
[/quote]
Why don’t you ask all these people who voted for changes why they don’t want to move to rbfx if you want to know the answer that badly?
Why are you asking the one who *did* move?
I’m, like, the worst possible interviewee to ask such question.

I can only tell for myself. I didn’t want to use rbfx because I hate forks and I think it’s suboptimal use of resources.

[quote="adhoc99, post:57, topic:5864"]
Yeah, the poll, sample size of what, 15 people? And how many already are on rbfx? I wonder actually how many users even use the forum.
[/quote]
It tells a lot about how many active users Urho actually have. 
I’d like to get more votes, but it’s not like I can force all these people to appear here.
I will work with the data I have, extrapolating it on the rest of hypothetical users that may or may not exist.

-------------------------

Modanung | 2020-02-05 22:58:31 UTC | #59

Seems to me like this overhaul would introduce a lot of work that would cause existing issues and PRs to get snowed in. If you want to work on Urho3D, do so, but let Urho be Urho and may rbfx fill a niche of its own. If you regret working on the wrong engine, rest assured in the fact that you gained experience while doing so.


[quote="adhoc99, post:57, topic:5864"]
I wonder actually how many users even use the forum.
[/quote]

I'm counting 23 [users](https://discourse.urho3d.io/u) with visits during the last week, over thirty in the last month.

-------------------------

adhoc99 | 2020-02-05 23:06:45 UTC | #60

The poll tells literally nothing. Most people just use the engine and never even step here. I have been using this for 2 to 3 years and never even bothered to join the forum.

Sure, because 10 votes (and 4 of them already use brfx and I have no idea what are doing here) represent the totality of users of the engine. Maybe checking how many clones or downloads the repository have would be a lot better indicator of the real userbase.

I am asking you exactly because it was your proposal.
So, you do not want to use rbfx, but want to merge all that here.
**How is that more logical than just moving there?**
**What does Urho3D have that rbfx does not?**

-------------------------

Eugene | 2020-02-05 23:07:26 UTC | #61

[quote="Modanung, post:59, topic:5864"]
that would cause existing issues and PRs to get snowed in
[/quote]
You mean these existing issues that nobody is going to fix?

It sad and funny that people want to get functional improvements, but when said improvements are basically offered the same people are complaining about the price (relatively small) that they have to pay.

It took me 10 minutes to move my project from Urho containers to EASTL and it already saved me ten times more.

-------------------------

Modanung | 2020-02-05 23:25:51 UTC | #62

[quote="Eugene, post:61, topic:5864"]
You mean these existing issues that nobody is going to fix?
[/quote]
I heard there are some rbfx developers that miss working on Urho3D.

> Soon it will be
Like in the days before

-------------------------

Eugene | 2020-02-05 23:35:50 UTC | #63

[quote="adhoc99, post:60, topic:5864"]
Most people just use the engine and never even step here
[/quote]
And we have no information about said people and what they want.
We also don't know if they would use rbfx given choice.
Urho3D is indexed and relatively known, rbfx is not promoted in any way.

[quote="adhoc99, post:60, topic:5864"]
**How is that more logical than just moving there?**
**What does Urho3D have that rbfx does not?**
[/quote]
Either I'm writing too cryptic or you are outright ignoring what I'm saying.
**It is the waste of human time to work on two divergent codebases when it is possible to work on two partially synchronized codebases.**
I don't know how else to explain it.

Also, I have a question.

You say you want changes, but when you are offered functional improvements with relatively small price... You don't want it anymore, because you will /gasp/ have to spend an hour to migrate your code to the new version.
What do you suggest then? What should be done instead? There are people who want to work with Urho and who need better container library. What do you suggest to do for these people?

-------------------------

JimMarlowe | 2020-02-05 23:36:34 UTC | #64

Those breaking changes sound significant.  In changing the containers, my existing programs are going to have to change, is this a drop in replacement or will logic have to change too.  I guess I won't have to worry about moving my Angelscript programs forward. I could use C# though?  As the rbfx wiki page says "⚠️ C# support is experimental ⚠️ It may not work correctly, fail or crash in spectacular ways. Managed APIs will likely change in the future.". 
To me, it sounds like some of these changes could be moved into Urho thru the Issue/Pull Request route and that way, it could be peer review and argued about. 
Dropping AS, Lua is interesting. For me, this would be the end of Urho and the start of rbfx, and anyone that had existing programs, they are done, choiceless.

-------------------------

SirNate0 | 2020-02-05 23:38:31 UTC | #65

Could we add another poll about switching to EASTL? If that is the primary obstacle to merging features from rbfx I feel that may be at least an important a question to ask as the one about AngelScript bindings.

-------------------------

Eugene | 2020-02-05 23:48:50 UTC | #66

[quote="JimMarlowe, post:64, topic:5864"]
Dropping AS, Lua is interesting. For me, this would be the end of Urho and the start of rbfx, and anyone that had existing programs, they are done, choiceless.
[/quote]
They are dropped in rbfx. Doesn’t mean we have to do the same in Urho. Even AS may be kept despite its huge maintenance burden.

[quote="JimMarlowe, post:64, topic:5864"]
Those breaking changes sound significant. In changing the containers, my existing programs are going to have to change, is this a drop in replacement or will logic have to change too.
[/quote]
I believe that with adapters enabled it would be enough to just rename first_/second_ to first/second for pairs. At least in most common use cases. Adapters may be extended on demand.

-------------------------

Sinoid | 2020-02-06 01:04:51 UTC | #67

Having recently switched to RBFX (~2 weeks ago) and been plugging away figuring out the differences and migrating my things over ... everything I thought I was against in it really is just "*who even cares, it works*" once I sat down with the repo and a lot of it (EASTL in particular) eased a lot of project ping-pong friction making it much more pleasant.

Some hiccups here and there, but in general I quite enjoy the move and don't see myself having any trouble getting most of my engine changes moved over - I'm looking forward to making PRs for some of those and porting a couple of the examples over to C# (working on 39_CrowdNavigation r/n).

All-in-all, RBFX is solid and a pleasant change.

---

> . Please, do not take this the wrong way, but, in corporate terms, this almost looks like a “hostile takeover”.

That's doesn't resemble anything. If anything this thread was opened with the vibe of being about things in RBFX reaching a cusp where if it continues on there will be nearly zero hope of porting them backwards to Urho3D and there will be no one remaining willing to bother with that work - which will only get worse and worse.

---

STL containers sure would make the CMake scripts *fun*. Joy for adding more build targets to deal with STL switches. Mismatched STL configurations between libraries is tons of fun. /s

---

[quote="johnnycable, post:35, topic:5864"]
C# - same. Moreover, it is going to bring all those *use virtual-machine don’t-want-to write-too-much code* pimps into the engine *oh-my-what’s-this-make-shared-thing-here*
[/quote]

Bluetooth & C++ == need rope, stool, and rafters. Bluetooth & C# == nuget and get to work.

C# is the indomitable king of glue languages, that fight is long over. CoreRT along with scores of TensorFlow for C# flavours ended it permanently without leaving reasonable ground for retort.

I think you're forgetting that C#-lord Unity is constantly botching everything they do and C# in master will likely bring a much needed talent infusion from the periodic handfuls of expats.

-------------------------

adhoc99 | 2020-02-06 02:36:27 UTC | #68

[quote="Eugene, post:63, topic:5864"]
Urho3D is indexed and relatively known, rbfx is not promoted in any way.
[/quote]
So, instead of working to promote rbfx, the idea is just move here. What a great idea.

Also, maybe it's not promoted in any way because nobody else cares for another C# WYSIWYG Unity-like.

[quote="Eugene, post:63, topic:5864"]
You say you want changes
[/quote]
I want no changes at all. Specially C# and EASTL.

[quote="Eugene, post:63, topic:5864"]
What do you suggest then?
[/quote]
How about moving to rbfx and continue rbfx development at rbfx. By what you describe, it will superseed Urho3D in no time.

But hey, what do I know. It is not like Atomic and Urhosharp failed hard, right. This time it will be different, for sure.

-------------------------

Sinoid | 2020-02-06 04:17:25 UTC | #69

[quote="adhoc99, post:68, topic:5864"]
But hey, what do I know. It is not like Atomic and Urhosharp failed hard, right. This time it will be different, for sure.
[/quote]

Neither of them captured contributors like RBFX has though. The commit logs alone show that almost all active talent has moved to RBFX. Urho3D is left with @SirNate0 @1vanK and @weitjong as active contributors of note.

The commit history sealed the deal for me to make the move, I recognized every contributor and knew roughly who they were and what they've done which gave me a lot of confidence moving to RBFX.

---

The ideal situation is that Urho3D grabs what it can right now while it still can from RBFX and RBFX then moves forward more heavy-handed than Urho3D willing to lock into things like "*we shall use Metal-ness*" (or spec, w/e, just lock into something so we can sit down and do PBR right).

@adhoc99 

I'd be wary about creating any hard-lined attitude about taking from RBFX as you're likely going to be upset - I'm an asshole and I will rub your words (screenshotted) in your face when you start demanding someone port compute shaders back to Urho3D ... which you will do.

-------------------------

Eugene | 2020-02-06 07:39:07 UTC | #70

[quote="adhoc99, post:68, topic:5864"]
I want no changes at all.
[/quote]
You literally voted for an option “I want changes”. Are you back on your word now?

[quote="adhoc99, post:68, topic:5864"]
How about moving to rbfx and continue rbfx development at rbfx.
[/quote]
If you convince all these people who want changes in Urho to move to rbfx instead, it will be fine for me. But, I dunno, these people want to stay in Urho for some reason. Maybe we should respect their choice?

-------------------------

Sinoid | 2020-02-06 06:58:40 UTC | #71

@Eugene you're pushing it there, given what you said about ASM for angelscript, I could carry that off into CoreRT hate since CoreRT runs on ASM. I didn't bother touching on it snce I assumed you just never reached that level of education to understand why AS uses ASM for thunks.

-------------------------

rku | 2020-02-06 07:02:55 UTC | #72

I am quite disappointed in the discussion. Nobody is talking about technical aspects of changes. Most vocal voices focus on what they want personally. There is absolutely no regard for what other people might find useful. If you do not need it - does not mean everyone else does not. If you do not like some feature - you do not have to use it (except for containers). And worst of all - nobody advocating for no change said "i will step up and maintain containers/bindings/etc". And most confusingly poll indicates exact opposite of general vibe in this thread.

So please @adhoc99 point out some technical problems with proposed approaches. Point out how your _important_ projects will get hurt. Do you have a commercial product that depends on maintenance of current codebase? This is important information.

---

@Sinoid CoreRT is not officially proposed solution any more. Seems like .NET people are going to use something else from AOT. So using CoreRT would be just like using any out of tree dependency - it would not impact upstream project in any way.

-------------------------

Sinoid | 2020-02-06 07:03:26 UTC | #73

@Eugene my remark is mostly moot, just bitching about in regards to AS. Core RT also uses ASM - is CoreRT terrible too?

-------------------------

Sinoid | 2020-02-06 07:07:39 UTC | #74

You said Urho3D is not truly cross-platform for having platform specific ASM for Angelscript.

-------------------------

Sinoid | 2020-02-06 07:08:38 UTC | #75

Urho3D uses SDL2 which is not truly cross-platform anyways as it doesn't support GearVR and numerous other targets.

-------------------------

Eugene | 2020-02-06 07:14:05 UTC | #76

I’m not against assembly in general because obviously it always boils down to it in the end, therefore some tools must use ASM in some way. 

My issue is that platform- and compiler-specific assembly library (like AS) requires much more support than C++ library. And I don’t think that benefits of having ASM are overweighting the costs in case of AS.

And I mostly hate brittle manual bindings that are made using ASM in AS, not the ASM usage itself.

-------------------------

Sinoid | 2020-02-06 07:17:25 UTC | #77

So super fast native calls weren't worth it in your opinion?

That's the whole point of AngelScript. Say it on record, "I'M AGAINST FAST NATIVE CALLS"

Edit: yes, I'm going to screenshot your response because there is none .. you've probably figured that out.

-------------------------

Sinoid | 2020-02-06 07:20:04 UTC | #78

Chill. We all need to chill down.

-------------------------

Eugene | 2020-02-06 07:21:05 UTC | #79

Super fast native calls are good.

Are super fast native calls worth highly increased maintenance burden in case of AS specifically? I’m not sure. In case of AS it’s not even obvious what bindings should be used — just look at all these flags. Did you know that replacing empty-body class ctor with default ctor breaks AS bindings?

I’ll rephrase myself. I don’t have issues with ASM inside AS but I hate that it is lays bare open for end user.

-------------------------

Sinoid | 2020-02-06 07:26:07 UTC | #80

CoreRT makes those calls for basic allocations however, ASM is invoked for all struct allocations. CoreRT pretty much murders all reason.

Who is wrong? Angelscript for using Thunk ASM or CoreRT for using ASM for thunks and memory?

If AS is wrong for using ASM then all Urho3D users should line up to die.

-------------------------

JTippetts1 | 2020-02-06 08:01:24 UTC | #81

Yikes. This went pretty far out into the weeds. It's a pretty straightforward question, I think, and not really warranting a holy war.

-------------------------

orefkov | 2020-02-06 08:27:55 UTC | #82

A bit of clarity.
AngelScript not using asm in binding process - it just some aripmetical tricks with provided function pointers, and it transparent for programmer. All the programmer needs to do is write the string with the AngelScript's method description correctly. The AngelScript uses assembler to package arguments when making an native call, and this also remains behind the scenes for the platforms it supports. C# does exactly the same thing, because it is not magic that it call to native functions.
The only difference in the details is that the bindings from C++ to the AngelScript are created manually, and to C# it done automatically using SWIG. And if SWIG is mistaken somewhere and forms the wrong binding, everything will fail the same way. If anybody teach SWIG to create bindings for a AngelScript, there will be no difference with C#.

AngelScript also potentially has a JIT - it can be embedded in the library and this will significantly increase its execution speed.
The AngelScript is much smaller than the C# and does not require dragging along a bunch of dependencies in the form of a .NET framework or Mono. Meanwhile, its capabilities are enough to implements the game logic. The only drawback is that there are no native calls for ARM64 yet, which somewhat slows down work on modern Android and IOS systems. And, of course, there are far fewer people who know the AngelScript than they know C# :slight_smile:

I forgot one more minus of the script - there is no ready-made debugger in the library, although can add it, there are such solutions.

-------------------------

Sinoid | 2020-02-06 08:39:14 UTC | #83

@orefkov, that's thunking. Which every sane scripting language uses. Lua doesn't because lua byte-code is so fast that it doesn't have to bother so they use a trash stack-machine.

You have to either do like lua and fat glue or do like Angelscript and thunk to make foreign calls. These are your options.

CoreRT uses thunking for all PInvoke calls just like angelscript ... so any argument against Angelscript for using ASM is outright dead because you have to call CoreRT everything you would call Angelscript for doing such.

Spoiler, you're losing that argument so hard your babies will have broken skulls.

-------------------------

Zamir | 2020-02-06 08:45:14 UTC | #84

C # will attract a considerable crowd of newcomers, who, if they do not participate in the development directly, will make it more popular and open the issue. See the unity experience. C ++ is not what game developers want. AS and LUA are blind coding (without an IDE), the framework's and mono behind Core steers and is optimized by leaps and bounds. I agree C # mod, but decent and deserves respect.

I am not against AS and LUA, but C # can safely and worthily replace them.

-------------------------

Eugene | 2020-02-06 08:45:57 UTC | #85

I have extraceted EASTL question into separate topic
 https://discourse.urho3d.io/t/migration-from-custom-container-library-to-augmented-eastl/5872

-------------------------

Eugene | 2020-02-06 10:14:26 UTC | #86

[quote="orefkov, post:82, topic:5864"]
AngelScript not using asm in binding process - it just some aripmetical tricks with provided function pointers, and it transparent for programmer
[/quote]
When you make AS bindings you lose all C++ type information about function.
Therefore the binding string directly controls the assembly that is going to perform the native call.
So when you are making a binding, you are touching asm thru very thin API layer.
Or am I wrong here?

The difference here is that SWIG is automatic and end user does not need to touch asm when they are writing their code. Once configured, it just works (tm) most of the time and if user made a mistake, they will get compilation or preprocessing error.

AS have asm exposed, so if _end user_ touches it in wrong way, the application explodes.

[quote="Sinoid, post:83, topic:5864"]
Spoiler, you’re losing that argument
[/quote]
Can you please remind me _who_ are you arguing with and what is the argument?..

Because I think I didn't make myself clear enough in starting post.
My argument against AS is this part:
![image|690x123](upload://iZN7ItM6yFbraWKIsXU3kfDuKx6.png)

-------------------------

Zamir | 2020-02-06 09:53:14 UTC | #87

he didn’t die because there was c #, there was one developer and he abandoned it, because they stopped financing the project

-------------------------

Modanung | 2020-02-06 10:47:41 UTC | #88

[quote="Zamir, post:84, topic:5864"]
C # will attract a considerable crowd of newcomers, who, if they do not participate in the development directly, will make it more popular and open the issue.
[/quote]
It will also chase away a core section of informed developers, who are fond of Urho, sprouting another fork. The must-C#ers could all be guided to rbfx instead of being smeared out.

[quote="Zamir, post:84, topic:5864"]
C ++ is not what game developers want.
[/quote]
Although true that it is not the industry/education standard, when it comes to Urho3D I believe writing your programs in C++ _is_ the community standard. There is no need to homogenize; diversity is strength.

-------------------------

Zamir | 2020-02-06 11:04:24 UTC | #89

And you didn’t notice that engine writers very rarely make games, your hands will never drop before that)
Happiness C ++ coder is a living engine)) Well, or pride that someone wrote a decent game on it ... and that's it

-------------------------

adhoc99 | 2020-02-06 11:10:45 UTC | #90

[quote="Eugene, post:70, topic:5864"]
You literally voted for an option “I want changes”. Are you back on your word now?
[/quote]
Changes like oh, look a bug, here is a bug fix, not hey lets change major core components of the engine because we want to add C# and turn this into a Unity.

[quote="Eugene, post:70, topic:5864"]
Maybe we should respect their choice?
[/quote]
**Maybe make a giant pinned topic here advertising the clearly better rbfx where all devs moved to and so should you.**
**Make one in the site too.**

[quote="rku, post:72, topic:5864"]
Do you have a commercial product that depends on maintenance of current codebase? This is important information
[/quote]
Yeah, sure it is a great idea to tell you that.

[quote="Sinoid, post:69, topic:5864"]
I’m an asshole and I will rub your words (screenshotted) in your face when you start demanding someone port compute shaders back to Urho3D … which you will do.
[/quote]
Which I will do not. But funny you just assume stuff.
Probably I want C# and EASTL but just do not know it yet.

[quote="Zamir, post:84, topic:5864"]
C # will attract a considerable crowd of newcomers, who, if they do not participate in the development directly, will make it more popular and open the issue. See the unity experience.
[/quote]
Which will be a total nightmare.
Oh they will participate. They will participate a lot.
They will ask absolutely [everything] about [everything]. "How do I do [everything]?" "Why does not [everything] work?" "I need an example for [everything]." "Can you add [everything] in the engine so I do not have to?"
Yeah, I would call that a pretty accurate Unity experience.

[quote="Zamir, post:84, topic:5864"]
C ++ is not what game developers want.
[/quote]
Indeed. They want is to shovel "games" as fast as they can regardless of quality or performance. And they want to do that in the easiest possible way.
C/C++ at least tends to force developers to know what they are doing and do it properly.
C# however...............

-------------------------

rku | 2020-02-06 11:13:48 UTC | #91

[quote="adhoc99, post:90, topic:5864"]
Yeah, sure it is a great idea to tell you that.
[/quote]

Just trying to gauge if there is any serious impact on you since you are so outspoken against. So far it seems this is just your personal preference for the sake of personal preference. Let me know if i am wrong.

-------------------------

Pencheff | 2020-02-06 11:18:43 UTC | #92

I'll leave my thoughts on scripting, based on my own Urho3D usage. I may not be right but here it goes... 
AngelScript is awesome, but I don't think its attracting people. The effort and skills required to use AS is close to (as not the same as) those required to just use C++, so why not just use C++... My Urho3D based (media player like) application requires some scripting but other devs I'm working with just don't have the skill to code on AS and enough time to learn it. They prefer having a Lua, JS or Python scripting system with running examples that they can extend and easy to find samples on the net.

-------------------------

1vanK | 2020-02-06 11:24:34 UTC | #93

[quote="Zamir, post:84, topic:5864"]
C ++ is not what game developers want.
[/quote]

I do not see big difference between

 https://github.com/Dviglo/Dviglo/blob/CSharp/Source/CSharpSamples/03_Sprites/Sprites.cs
and
 https://github.com/Dviglo/Dviglo/blob/CSharp/Source/Samples/03_Sprites/Sprites.h
 https://github.com/Dviglo/Dviglo/blob/CSharp/Source/Samples/03_Sprites/Sprites.cpp

Just C++ works faster

-------------------------

Zamir | 2020-02-06 11:39:41 UTC | #94

There are no special differences, it’s exactly not in the code writing, but for what conveniences, in terms of quick compilation, removal of the general code, the absence of "h" files, opening on the fly in andriod, ios, etc. Comfort from the additions of the language itself and various modern programming chips. Before 3-4 years ago, even there was no idea to use c #, but take a look at it now - these are completely different things.

"Just C ++ works faster" now the difference is miserable, with the advent of Core X, optimization went uphill

-------------------------

Modanung | 2020-02-06 11:42:07 UTC | #95

[quote="Pencheff, post:92, topic:5864"]
The effort and skills required to use AS is close to (as not the same as) those required to just use C++, so why not just use C++
[/quote]

Because in cases where you *do* need script (when sending behaviour over network for instance) AS is a god-sent to those who have been coding C++ up until that point for the same reasons. I think we all agree automatic bindings would be divine for any scripting language and is guaranteed to accelerate engine development.

-------------------------

Eugene | 2020-02-06 12:02:11 UTC | #96

[quote="adhoc99, post:90, topic:5864"]
**Maybe make a giant pinned topic here advertising the clearly better rbfx where all devs moved to and so should you.**
**Make one in the site too**
[/quote]
Eugene: There are people who don't want to use fork. What should they do?
adhoc99: They should use fork!

...

I think that this way of answering questions and solving problems is weird and quite... nonproductive.

-------------------------

rku | 2020-02-06 11:55:10 UTC | #97

[quote="Modanung, post:95, topic:5864"]
I think we all agree automatic bindings would be divine for any scripting language and is guaranteed to accelerate engine development.
[/quote]

Definitely agreed. But that is not happening for AS. It isnt even happening for lua even though lua is easier of two. But we should not forget lack of ecosystem around AS. It is said already that you basically have your notepad and thats it. lua at least has a richer ecosystem around it, editor plugins that support debugging even.. Of course nothing beats C# in editor support. Not trying to say that Urho needs C#, just pointing out that good tools make life a lot easier. That should be of some consideration at least.

-------------------------

Modanung | 2020-02-06 12:05:01 UTC | #98

[quote="rku, post:97, topic:5864"]
It is said already that you basically have your notepad and thats it.
[/quote]
Not all that is said is true.
https://discourse.urho3d.io/t/all-about-angelscriptide/3884/5?u=modanung


[quote="rku, post:97, topic:5864"]
Definitely agreed. But that is not happening for AS.
[/quote]
It is not impossible. The future is uncertain.

-------------------------

rku | 2020-02-06 12:08:15 UTC | #99

Code::Blocks AS editing is a hack that sort of works. It is not a proper solution.

Automatic AS bindings are possible, but nobody will put in the work to make them happen. Go and prove me wrong :D

-------------------------

Modanung | 2020-02-06 12:34:56 UTC | #100

[quote="rku, post:99, topic:5864"]
Go and prove me wrong :smiley:
[/quote]

This instant? You know that *is* impossible. But you proved yourself wrong about Urho being dead. Maybe the same will be true for AS auto-binding.

[quote="rku, post:99, topic:5864"]
Code::Blocks AS editing is a hack that sort of works. It is not a proper solution.
[/quote]

CodeLite any better?

https://discourse.urho3d.io/t/configuring-codelite-for-editing-as-scripts/68

-------------------------

