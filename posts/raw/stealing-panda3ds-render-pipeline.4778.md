QBkGames | 2018-12-27 04:41:47 UTC | #1

The people with the right skills and time (sadly that's not me on both accounts) might want to take a look at this:
https://github.com/tobspr/RenderPipeline

It's an awesome looking renderer (quality comparable to Unreal). It MIGHT be possible to adapt it for Urho3D, or at least "steal" some ideas. I don't have the skills (nor the time) to tell how easy/hard it would be to modify it to work with Urho, but I thought (in my nativity) that it might be easier than writing something like that from scratch.

-------------------------

Sinoid | 2018-12-27 08:17:04 UTC | #2

It's a straight rip of the UE4 code, I got into it ages ago, but it was and still is just copy-paste from UE4. Down to the exact enums, arg names, and switch statements on identical material codes bad. 

Use at your own risk. You still owe Epic their % cut since no sane person will say it isn't Epic's property.

It's like SpeedTree, you think you're smart hijacking UE4's stuff for it, you're just going to get sued and lose.

**Edit:**

You're doubly screwed though since my grievances with the Panda PBR pipeline document the issue and prove that you're working with Epic's work. I even have a private legacy fork of it should I need it to justify my asshole behaviour.

I will testify against you.

-------------------------

QBkGames | 2018-12-27 08:24:56 UTC | #3

That explains why it's quality looks just like UE4.
If they use the same code then, yes, it's not at good idea to use it (I thought someone came up with something original and just as good as UE4).

I wonder if Panda3D have any agreement with Epic, or will they just get in legal trouble as soon as they release version 1.10 !?

-------------------------

johnnycable | 2018-12-27 18:17:52 UTC | #4

Interesting. So it would be basically a stealing of a stealing... :open_mouth:
EDIT: what about this [filament](https://github.com/google/filament) thing? Someone posted the link some time ago...
I tried it on Mac. OpenGL is ok, Vulkan renderer thru Molten is not.
Did someone try it on windows or linux? (oops)

-------------------------

GoldenThumbs | 2018-12-27 20:06:24 UTC | #5

From what I've seen filament is awesome, and it shouldn't be ripped code considering it's affiliated with Google. (from what I understand at least)

-------------------------

Modanung | 2018-12-28 00:31:24 UTC | #6

[quote="GoldenThumbs, post:5, topic:4778"]
it shouldn’t be ripped code considering it’s affiliated with Google
[/quote]

Although I do think this is reason to be suspicious/cautious, the license _is_ compatible.

-------------------------

johnnycable | 2018-12-28 14:15:33 UTC | #7

The project is led by Philip Rideout, a.k.a [the little grasshopper](https://prideout.net/). 
This guy seems to know its way about 3d.
The project is actively developed by Google (4 person I think), and is used in the [Sceneform](https://developers.google.com/ar/develop/java/sceneform/) Android Library.
Apparently can be accessed in Android Studio with a plugin. Didn't tried that.
It can be useful to substitute for a Metal renderer, and, in the long time, it's probably the only viable option out of bgfx.

-------------------------

Dave82 | 2018-12-29 14:25:50 UTC | #8

Actually there is an engine i found iteresting. Xenko. What's really interesting is that looks absolutely professional has all the tools , it's crossplatform , supports all nexgen effects.Only thing i don't like , it is written in C#... But what's  really amazing is that it is licensed under MIT ! Awesome ! Unity could be in trouble :D 

https://xenko.com/

-------------------------

GoldenThumbs | 2018-12-30 02:05:37 UTC | #9

Pretty sure they only went open source because they couldn't sell enough licenses. Could be totally wrong here though. Besides, that doesn't really matter if the engine is any good.

-------------------------

QBkGames | 2018-12-30 04:50:43 UTC | #10

I had a brief look at Xenko a few months ago, and although it has a pretty looking renderer, I think it's not much more than that. It has a very limited (non-existent) scene management, which means you can only have small scenes with limited number of objects (they have some kind of sub-scene streaming mechanism, but that only suitable for some kind of games). Also I don't think they have a terrain, or networking. So, it might be a good start for something to be built on top of it.
Unity is not in trouble yet (at least not from Xenko).

In my experience I'm yet to find another free open-source engine that's as well designed and overall functional as Urho3D. If we could get some global illumination and some post-processing shaders in its pipeline by default, it should be quite awesome.

-------------------------

GoldenThumbs | 2018-12-30 06:30:15 UTC | #11

I'm working on a new-ish SSAO shader. One already exists from the community but I wasn't happy with it. Will probably post that up when I feel it's good enough. Some other cool post effects would also be nice, but I can't think of any that aren't very specific. Like a dithering shader. Pretty sure no one wants that unless they are making a VERY stylized game.

-------------------------

QBkGames | 2018-12-30 08:29:02 UTC | #12

I think a good SSAO shader with some bloom on top (which I think we already have) would go a long wait to improving the visual quality of the engine.

-------------------------

GoldenThumbs | 2018-12-30 22:52:29 UTC | #13

I think some big issues lay more on the fault of the dev than the engine itself. A big issue I'm seeing is texture quality, and another is lighting. If those 2 things are fixed the engine could look passable without needing to change any code. That doesn't mean there aren't problems with the engine, of course. For instance, while it's nice to have PBR Urho's implementation of it isn't the best looking. Far from ugly, but also far from AAA quality... Honestly I think a lot of the graphical issues could be fixed if someone knows their way around shaders.

-------------------------

GodMan | 2019-01-01 13:35:39 UTC | #14

I agree with this. I have spent alot of time with other engines. I even used Irrlicht engine for 2 years. Although Irrlicht engine is easier to use I have been able to accomplish more with Urho3d than I did in months of using Irrlicht Engine.

-------------------------

GodMan | 2019-01-01 13:37:57 UTC | #15

I feel like Urho3d is a good balance of good graphics, and other features. Many people just concentrate on graphics, but many games look great, and they still suck.

-------------------------

QBkGames | 2019-01-02 11:33:30 UTC | #16

The quality of the assets you use will certainly have an impact on the visual quality of the game and the engine cannot do much about that.

However, on the engine's side of things, producing AAA quality is a combination of techniques, which include: good lighting (global illumination), PBR and post-processing (SSAO and bloom being the most significant). Having just one and not the others cannot compete with engines that have them all. But the technique that makes the most impact by itself (IMO), is actually SSAO, maybe even more that PBR, so I'm really looking forward to your implementation.

-------------------------

GoldenThumbs | 2019-01-02 17:31:07 UTC | #17

I'm having a lot of trouble getting any variation of SSAO to work aside from the one that was already made. I tried modding that one to look better and I almost did it, but it still didn't look right. One issue with the community implementation is that it changes based on viewing angle, which is ugly.

-------------------------

SirNate0 | 2019-01-02 23:00:26 UTC | #18

Isn't SSAO expected to change based on viewing angle, since it is Screen Space? From Wikipedia, it is "rather local and in many cases view-dependent, as it is dependent on adjacent texel depths which may be generated by any geometry whatsoever." (I don't really know anything about it beyond the basics, though, so I may misunderstand what you mean)

-------------------------

GoldenThumbs | 2019-01-02 23:17:35 UTC | #19

IDK, maybe it IS supposed to do that... I should get a video of it, because it doesn't look very good or intentional.

-------------------------

glebedev | 2019-01-04 13:22:33 UTC | #20

It maybe an offtopic but I would like to bring BGFX to the conversation. It still sounds reasonable to use it for rendering abstraction but keep all the other code the same (render paths, etc).

-------------------------

cadaver | 2019-01-04 14:17:44 UTC | #21

Look at https://gitter.im/urho3d/Urho3D for continued discussion on the bgfx work, among other things. TLDR: it is not trivial, and could result in loss of functionality or having to do some things differently.

-------------------------

cosar | 2019-01-04 18:39:22 UTC | #22

@cadaver
Quite offtopic, but have you considered coming back to leading Urho3D development? 
It's been more than a year since you stepped down, and, no offence to the other core developers, the leadership void that you left behind does not look like was filled yet.
Maybe starting a patreon for Urho (I know it was discussed before) is not such a bad idea.
There might be more than a few people from Urho community that would rather pay some amount monthly for Urho development rather then for a bloated commercial engine license (I do for sure). Good leadership is a great incentive.
Just think about it. It's quite obvious that you still care about the project.

-------------------------

cadaver | 2019-01-04 21:20:59 UTC | #23

No; I believe things must happen naturally according to people having a use for the engine, and wanting to take more responsibility. I don't, any more, so I'd be forcing myself. 

Also I think I have said it before, but for me personally money would be an anti-incentive, as it would mean more pressure to get things right. I think I've also said for the project in total donations / Patreon could very well be a good idea, if there just are other people who want to pursue it.

Obviously I care for the project in the sense that it's nice seeing people working on it, keeping it going on, and keeping it on their minds (even if it means the same people bickering about it in several gitters), but like I said, things can't be forced.

-------------------------

rku | 2019-01-05 10:48:10 UTC | #24

@boberfly did most of bgfx porting already: https://github.com/boberfly/Urho3D/tree/feature/bgfx

What @cadaver said is very true. Port is at a point where it stops being simple. bgfx expects things to be done bit differently. Going full-bgfx would make sense as engine could be mended as needed to accommodate bgfx. So far work has stalled and we have no idea if it will ever be finished.

-------------------------

Sinoid | 2019-01-06 06:42:14 UTC | #25

I've said it before and I'll say it again ... I don't believe the renderer is anything holding Urho3D back, if it is holding it back it's less the renderer and more that the platforms being supported have complicated it to such a degree that no general purpose API can really cover either.

The real hold back is what hardware those that can do things have access to, I just don't have reliable access to GL4.3 hardware (or that which can do it well) to be able to do GL compute, so while I've completed OpenCL/DX11 compute I can't just magically make that work elsewhere.

I can plop my geometry/tessellation shader code onto github, but that isn't as great a help as many might think, the hash structures Urho3D uses rely on 32-bit keys ... enjoy collision city, in even basic tests shit collided constantly.

-------------------------

I3DB | 2019-01-06 17:53:52 UTC | #26

[quote="rku, post:24, topic:4778"]
Going full-bgfx would make sense as engine could be mended as needed to accommodate bgfx.
[/quote]

From my beginners perspective, and working with sharpreality as the wrapper ... being able to import and display other peoples work easily and on-the-fly will enhance the immediate utility of Urho3D. bgfx would help it seems. but i'm still dependent upon the uptake by sharp reality of the implementation of urho3D-next.

[quote="Sinoid, post:25, topic:4778"]
I don’t believe the renderer is anything holding Urho3D back, if it is holding it back it’s less the renderer and more that the platforms being supported have complicated it to such a degree that no general purpose API can really cover either.
[/quote]

As I work through the various samples in feature samples and get them to work on a hololens, there is a bit of work to convert, and it's related to the sharpreality api. But it's the same conversion for most all of them, and not hard or time consuming once you get the pattern. But yes there is a conversion to do. It's camera and scene related mostly, and reformatting.

Most of my time is spent reformatting to an AR environment and providing appropriate control of the scene with a different set of inputs and triggers, also with more info available such as surrounding physical environment, and generally a 360 degree view ability, around the scene and around the camera, depending on body movement, an additional degrees of freedom of sorts when using AR. 

I describe this time as spent opening wide the door into AR rather than about fumbling with urho3d's api, even though I do fumble a lot, and around the rendering, it's not holding me back though, it's just a set of different issues than other APIs might have depending upon what services are offered. 

For what I've been doing the Urho3d api and engine is a great tool as is. I see your point about the different platforms supported versus supporting the most active ones and positioning for straightforward future enhancements. 

But for me overall the Urho3D API is quite powerful and I think my current limitations is on-the-fly import of models.  Though if I could get shadows working and had networking and 3d audio. Still, even without these immediate out of the box capabilities with sharprealty there is so much available that does work great. Even [something simple like the animating scene](https://urho3d.github.io/samples/Urho3DPlayer.html?Scripts/05_AnimatingScene.as) is quite stunning visually in AR and opens the mind's door to many possibilities that don't readily appear when viewing on a screen versus standing in the middle of it in holographic space.

-------------------------

WangKai | 2019-01-08 09:15:52 UTC | #27

IMHO -
PBR should be fixed to work, on mainstream platforms Urho supports.
More rendering APIs should be supported and enhanced.
Edit: And also put rendering into another thread.

Maybe we should learn something from game engines such as Godot has been doing.

-------------------------

Sinoid | 2019-01-12 08:42:05 UTC | #28

> PBR should be fixed to work, on mainstream platforms Urho supports.

What are those *mainstream platforms*? 

We can use business analysis data here, by default Linux and Mac are reliably year to year not a mainstream platform for games purchases (there's problems because of dual-booting, but guess what, doesn't matter ... what platforms are games being purchased for). Should all linux and mac support be abandoned?

PBR has an awkward history in Urho3D, IIRC I was 3rd to begin a large work at it with the objective of being real-time on Intel HD4000 / Ivy-Bridge hardware and eventually got fed up with the general griping that PBR causes (that's exactly what happened, I still google the last-straw user regularly to see his odd porn interests) and DragonCastJosh picked it up from me and carried it off into it's current state while adding his own flavor to it dropping some of the things I had done that were specific to low-spec machines like YCoCg interleave and the like because they did in fact over-complicate the pipeline.

If you want a unified workflow that works everywhere you're going to have to sacrifice with a preprocessing step to make that happen and remap your data. 

Guess what, everything but Visual Studio absolutely sucks at that - it's 2019 and everything except Visual Studio is incompetent at batch or partial-exec tasks ... everything. How many CMake or premake commands do you want to memorize? How many batch files do you want to write to do those tasks and clean up after them?

-------------------------

Sinoid | 2019-01-12 08:53:27 UTC | #29

Note, I would be 100% behind and would contribute to a full rewrite to target a reasonable end-game common graphics API like [Diligent](https://github.com/DiligentGraphics/DiligentEngine) as it covers a sufficiently broad scope compared to narrow trash like BGFX ... note: using *trash* as a reference to clearly misinformed comments about geometry shader performance and nothing else that bk described while doing exactly what every single GPU vendor said **DO NOT DO THIS** that's my beef with BGFX, the soviet pisses on reality and none of the BG utility stuff has any merit just a bunch of absolute garbage attempts at STL but failing grossly.

-------------------------

dragonCASTjosh | 2019-01-12 10:36:42 UTC | #30

When I picked it up from you I had no real prior rendering knowledge and was very new to programming on this scale, but I had a passion for advanced rendering techniques. 

But overall it came down to if I struggled to understand a topic or some of the work you did I put it aside for a later date. This never came as o became busy with work after landing a job due to my work on PBR.

Since then I have learned a lot and have started playing around in a local branch of atomic with plans to submit a much better PBR system with many of the accompanying features you would expect in a modern engine.

As for platforms I now have a few android devices so I am able to test and development a version that works for Android, possibly striped down and simplified.

-------------------------

johnnycable | 2019-01-12 14:30:49 UTC | #31

Didn't know about this diligent thing. I'll add it to the list of possible candidates. Thx.

-------------------------

glebedev | 2019-01-14 00:20:27 UTC | #32

Does Diligent support Metal on iOS? There is an open ticket to add metal support...

-------------------------

johnnycable | 2019-01-14 16:01:27 UTC | #33

That's not clear. I'm going to try that next.

-------------------------

johnnycable | 2019-01-24 11:21:16 UTC | #34

I'm giving a try to Diligent.
- on Mac, it supports Vulkan thru MoltenVK and it works.

![45|605x500](upload://7w5sgFtpRZ21URgfqNABB5HaXmy.png) 

the dreaded cube

![55|585x500](upload://qhiSYpcWvCHft76784zGrHTU8O8.jpeg) 

on Ios, it is still opengl and it has some problems:

![29|690x388](upload://myNyeOf2sGRgc1H9LtQRTBJUwVN.png) 

I'm now gonna try Android

EDIT: it's me? It seems the image I posted are... like blurred...

-------------------------

Sinoid | 2019-01-24 06:07:45 UTC | #35

@dragonCASTjosh not one bit of that was meant to disparage you, if it came across that way I apologize. 

I was just trying to get across that there were conflicting motivations throughout the process.

I had my own strong bias to favor low tech devices, and it is very much present in the early code.

That's a big part of why I bailed the second things got serious with tessellation and geometry shaders. Can of worms that most can't deal with. Having done the first publicly accessible pass of crowds I've been numb ever since.

-------------------------

dragonCASTjosh | 2019-01-24 19:01:36 UTC | #36

Dont worry i know there was no hostile intent. Just through ill fill in my motivation and reasoning because i know it took a very different direction and not sure i ever really explain my reasoning :slight_smile: 

If you have any input or improvements for the existing integration please go for it because i know its very far from perfect. Even now there is so much i want to change i just need the time.

Id love to see some of your performance specific features make a return.

I would also love some editor side improvements related to PBR such as cubemap filtering in engine, maybe as a standalone tool. currently its a nightmare to build a level due to the cubemap filtering.

-------------------------

Sinoid | 2019-01-26 06:52:18 UTC | #37

@johnnycable it's a considerable overhaul to make tweaks to make Diligent appropriate, but I suspect most of the API can remain intact building buffered pieces of piplines and querying for their existence by dual-hashes (or multi-hashes).

I don't see going backwards to GL3 to be a problem - the common changes benefit all, really the GL API just uses 4.5 features willy nilly based on calls. The change would mean losing DX9 but GL is really the better case in those  DX9 locked environments until someone can say otherwise.

The reason I favor something like Diligent over BGFX is that it brings very little with it, it's just a straight modern graphics wrapper, doesn't bring BX/BIMG/etc like BGFX does and is very much on point - it doesn't mess with your draw calls like BGFX does. Basically, I favor it because it's just remapping a problem domain into a common space, instead of trying to be a toolkit.

Because it's so on point, only the core guts of Urho3D would need to change to fit it. Which is much less radical than most other libraries would require.

It's also, so insanely close to my own DX12 and vulkan code that it feels like a copy-paste even though I know it isn't. It's just solid.

My chief concern with it is shader reflection issues. I haven't worked with it enough to know that it can actually work in arbitrary shader and variable environments.

-------------------------

smellymumbler | 2019-01-28 16:56:12 UTC | #38

Open-source BSDFs: https://github.com/DassaultSystemes-Technology/EnterprisePBRShadingModel

-------------------------

johnnycable | 2019-01-29 11:03:08 UTC | #39

No CC-something (except cc0) can be used in closed-source products...
Let alone assigning a classical art asset license to a software...

-------------------------

QBkGames | 2019-01-30 09:06:30 UTC | #40

I check out the link but I could not find the actual shader code only the manuals. Am I missing something?

-------------------------

guk_alex | 2019-01-30 09:19:44 UTC | #41

This is description of PBR model for some proprietary 3d software.
> The Enterprise PBR Shading Model (DSPBR) is a material model for physically based rendering, supported by all renderers in the  **3D** EXPERIENCE Platform

-------------------------

smellymumbler | 2019-01-30 16:09:16 UTC | #42

https://github.com/DassaultSystemes-Technology/EnterprisePBRShadingModel/blob/master/LICENSE.txt

It can be used in commercial projects, as long as there is attribution and is shared alike. Similar to GPL.

-------------------------

QBkGames | 2019-01-31 11:20:06 UTC | #43

Thanks for clarifying, I misread the title and was thinking that it's an actual graphics shader in GLSL or HLSL. OK, so it's just a shader model, the theory based on which you can program your own shader.

-------------------------

Yonnji | 2019-05-15 07:13:25 UTC | #44

[quote="Sinoid, post:2, topic:4778"]
It’s a straight rip of the UE4 code, I got into it ages ago, but it was and still is just copy-paste from UE4. Down to the exact enums, arg names, and switch statements on identical material codes bad.
[/quote]

Can you tell me exactly where it's similar to UE4? I'm using this renderer in my game, so I need to make sure. I have checked almost every GLSL shader, but haven't found anything similar to UE4.

-------------------------

QBkGames | 2019-05-16 04:05:43 UTC | #45

Did you adapt it to work with Urho? Do you mind sharing some ideas on how you did it? Thanks.

-------------------------

Valdar | 2019-05-16 07:52:46 UTC | #46

There is was thread in the "Issues" tracker [here](https://github.com/tobspr/RenderPipeline/issues/23) on GitHub that you can still view. It looks to be the extent of the infringement claim, but I too would be interested in knowing if there is still possible concerns.

-------------------------

Yonnji | 2019-05-16 08:14:38 UTC | #47

[quote="Valdar, post:46, topic:4778"]
There is was thread in the “Issues” tracker [here](https://github.com/tobspr/RenderPipeline/issues/23) on GitHub that you can still view. It looks to be the extent of the infringement claim, but I too would be interested in knowing if there is still possible concerns.
[/quote]

Ah, I see. So it's already solved a few years ago.

[quote="QBkGames, post:45, topic:4778, full:true"]
Did you adapt it to work with Urho? Do you mind sharing some ideas on how you did it? Thanks.
[/quote]

I'm using it with Panda3D.

-------------------------

johnnycable | 2019-05-16 15:27:21 UTC | #48

So, in short, is that copied or not?
To be sure, one should have to diff the two sources, I guess...

-------------------------

Yonnji | 2019-05-16 15:47:54 UTC | #49

[quote="johnnycable, post:48, topic:4778, full:true"]
So, in short, is that copied or not?
To be sure, one should have to diff the two sources, I guess…
[/quote]

It can't be just copied. It's more complicated.
The RenderPipeline was written in Python (~49%), GLSL (~49%) and a little bit of C++ (~2%).
The Python part is for shaders management, preview and configuration UI. The C++ part is just the lights manager, which is simple.
I has checked most of the GLSL shaders, trying to compare the similar shaders between UE4 and RP, but not able to find anything similar.
The author said that he already removed some questionable parts, which other people complained about.

-------------------------

johnnycable | 2019-05-17 14:42:17 UTC | #50

I see. I checked Panda engine some time ago, but honestly I don't remember right now the reason I let it go...
How was to work with it? Is it worth? Or is a pain?

-------------------------

Yonnji | 2019-05-17 15:00:49 UTC | #51

Panda3D is easy to use for me. I has tried UE4 and Unity3D, they are a lot more difficult to use. Also the development is going fast because of the Python language.

-------------------------

QBkGames | 2019-05-18 04:10:44 UTC | #52

The reasons I chose Urho over Panda back a couple of years ago when I started looking into 3D engines were:
* Urho has a much nicer design with the Node-Component system that's easier to work with
* Urho supports instancing (automatically and manually using groups), Panda does not
* Without this Render Pipeline the Panda graphics (at least in the samples they provide) look crappier than the Urho samples
* The C++ documentation was lacking (I think it has improved in the meanwhile).
* Python is nice overall language but not very performant as a scripting language, making the engine suitable for certain type of games (with not too much action), like adventure, puzzle, etc. Maybe as hardware performance improves, this may become less of an issue, but if you want to squeeze as much performance as possible, Python is not the best.

-------------------------

QBkGames | 2019-05-18 04:20:43 UTC | #53

Well, if there are no legal issues with Panda's render pipeline, I'm back to suggesting that we 'steal' it :) and integrate it into Urho (at least some shaders or algorithms).
Someone who knows well the Urho render pipeline and is good with shader programming, could perhaps look into it (hopefully those people have not all left the project).

-------------------------

Leith | 2019-05-18 06:44:40 UTC | #54

Some just arrived - I can do shaders

-------------------------

johnnycable | 2019-05-18 15:23:22 UTC | #55

Surely lacking of instancing is worryingly....
Personally I'm a fan of bare models, ECS plus a renderer... but I see it can be annoying, all that c++
Pythons pros: confortably fast to write, horribly slow to run... but basicly I'm against scripting in general...

-------------------------

johnnycable | 2019-05-18 15:25:02 UTC | #56

So you used python for development? Does it work? Python is slow, but maybe it can be made to work fast, you know...

-------------------------

Yonnji | 2019-05-18 19:07:32 UTC | #57

[quote="QBkGames, post:52, topic:4778"]
* Urho has a much nicer design with the Node-Component system that’s easier to work with
[/quote]
The Panda3D system is Node based too. Every game model and UI widget is a Node, which is part of a tree.

[quote="QBkGames, post:52, topic:4778"]
* Urho supports instancing (automatically and manually using groups), Panda does not
[/quote]
Yes. This is true.

[quote="QBkGames, post:52, topic:4778"]
* Without this Render Pipeline the Panda graphics (at least in the samples they provide) look crappier than the Urho samples
[/quote]
Yes. The default render have only some old CG shaders. So you have to use them or write your own. This is fine for me, because I don't need PBR and I'm removing all the PBR stuff from RP xD

[quote="QBkGames, post:52, topic:4778"]
* The C++ documentation was lacking (I think it has improved in the meanwhile).
[/quote]
Yes. This could be true. Panda3D does not recommend using a C++, this is not the way the engine was designed for. 

[quote="QBkGames, post:52, topic:4778"]
* Python is nice overall language but not very performant as a scripting language, making the engine suitable for certain type of games (with not too much action), like adventure, puzzle, etc. Maybe as hardware performance improves, this may become less of an issue, but if you want to squeeze as much performance as possible, Python is not the best.
[/quote]
Python is not the problem here, the engine was written in C++, so the Python is not the slowest thing in a complete game. Python is for scripting the game logic. I'm mostly bound by GPU, because of unoptimized graphics and shaders.

[quote="johnnycable, post:56, topic:4778, full:true"]
So you used python for development? Does it work? Python is slow, but maybe it can be made to work fast, you know…
[/quote]
Yes. It work. There are a lot of ways to optimize it.

-------------------------

weitjong | 2019-05-19 01:01:14 UTC | #58

[quote="Yonnji, post:57, topic:4778"]
Yes. It work. There are a lot of ways to optimize it.
[/quote]

I am interested to know how big is the python runtime and which python version (2.7 or 3.x already) you use.

-------------------------

Leith | 2019-05-19 05:38:42 UTC | #59

We all know python is not a good choice for runtime scripting (but it is beautiful for offline).
The trick when using expensive script languages, is to confine your events that are handled by script, to those which occur infrequently, and/or those whose complexity warrants it. I'm guessing he's not dealing with full frame rate in his scripts.

-------------------------

Yonnji | 2019-05-19 12:53:06 UTC | #60

[quote="weitjong, post:58, topic:4778"]
I am interested to know how big is the python runtime and which python version (2.7 or 3.x already) you use.
[/quote]
Python 3.7, it's ~40Mb compressed - https://anaconda.org/kitsune.ONE/kitsunetsuki-runtime/files
It's an Anaconda Python without some unused stuff + Panda3D.

-------------------------

johnnycable | 2019-05-19 14:35:47 UTC | #61

I see. Thx [any character filler]

-------------------------

UNDEFINED-BEHAVIOR | 2019-05-24 19:00:27 UTC | #62

Hello.
A little late to this thread (didn't know urho3d had a forum lol)

No love for SPIR-V based shader pipeline?

Basic gestalt: 
https://www.khronos.org/spir/
https://www.khronos.org/assets/uploads/developers/library/2016-vulkan-devday-uk/4-Using-spir-v-with-spirv-cross.pdf

>but muh bgfx

This toolset requires shader to be written in somewhat constrained "Vulkan GLSL" dialect of GL but in return it:
* Supposedly gives you true cross platform shader compatibility without relying on string macros.
* Forward compatible.
* Allows some out of band IR optimization, just like LLVM.
* Rich reflection. (Mainly for converting to vulkan shader)
* Blessed by KHRONOS

https://community.arm.com/developer/tools-software/graphics/b/blog/posts/spirv-cross-working-with-spir-v-in-your-app
https://eleni.mutantstargoat.com/hikiko/2018/03/04/opengl-spirv/

Here's some engine that have seemingly adopted spir-v pipeline.
oryol
https://floooh.github.io/2017/05/15/oryol-spirv.html
Shader system of libretro
https://github.com/shader-slang/slang

tools:

GLSL -> spirv
https://github.com/KhronosGroup/glslang/tree/master/SPIRV
spirv -> glsl/ gles/ hlsl/ metal/ dx
https://github.com/KhronosGroup/SPIRV-Cross
ir language utility
https://github.com/KhronosGroup/SPIRV-Tools

-------------------------

GoldenThumbs | 2019-05-25 01:45:59 UTC | #63

I do feel like I should ask this since no one (I could find) seems to have asked it, but do we really need to replace the existing pipeline? I've been able to do quite a bit with it. We do need to add Vulkan support, not sure if that would require a full rewrite or not as I just work with shaders mostly. This is a genuine question, not saying we should or shouldn't start work on another pipeline.

-------------------------

johnnycable | 2019-05-25 15:32:42 UTC | #64

I guess so. Possibly a Vulkan compliant pipeline is the only way for an open source project which lives on contributions. There's already a Vulkan fallback for Metal, given Apple has deprecated opengl:

https://discourse.urho3d.io/t/metal-moltenvk-support-for-ios-an-mac-devices/4845/49

Apparently Vulkan is the only way to go. If you have to expect some contributions, they probably will come that way only.
Beyond that, it all boils down to have a double feature, one for low-end devices craving opengl-es like graphics, and one for more advances and powerful devices, let's say an AAA one...

-------------------------

Sinoid | 2019-07-13 05:51:31 UTC | #65

[quote="johnnycable, post:64, topic:4778"]
Apparently Vulkan is the only way to go. If you have to expect some contributions, they probably will come that way only.
[/quote]

Vulkan is like writing for that Linux ALSA garbage. It's pure pain.

Flat out ... Vulkan is not compatible with a generic engine. Sure, you can pull out the wazoo as much as you want and run some caches like Doom3-Vulkan, but if you want to actually beat the GL drivers you **MUST** know ahead of time WTF you are doing.

Meeting those *generic* criteria means locking out those specifics that make DX12/Vulkan shine.

The most damaging part to existing engines is in render-target handling. No one talks about it, but if you look at how the APIs work for DX12 and Vulkan, you'd have to be an idiot to miss how badly those rip shit apart.

Yes, pick Vulkan - it's still a bug-ridden trash-heap (validation layers are mostly useless except for logs) but in the long-run it's a safe bet. Granted, I'm at an ARB member company now ... we're top-to-bottom not happy with Vulkan ... so take that as you will.

---

Before anyone attempts to draw some Unity/UE4 comparison ... do recall that in Urho3D shadows are massively cheaper than those other engines due to basic advancements over the years and reasonable defaults. We might not have GI and other fancy things, but we've got the fastest shadows you're ever going to see.

-------------------------

johnnycable | 2019-07-13 15:06:02 UTC | #66

It doesn't matter what I want; it matters what contributions are given. And apart from @elix22 contribution about Metal / Molten / Vulkan, we  haven't had any other contribution, recently. But maybe I've skipped something...
The feeling Vulkan is not being so quickly adopted is in the air, anyway... I don't think you're too far from the truth...

-------------------------

Leith | 2019-07-14 05:26:17 UTC | #67

This is something I have seen in the past.
We hang onto old technology, because "it works right now, and we understand it intimately, including its drawbacks, which we acknowledge and accept".
Switching between DX versions has always been a painful experience, while in contrast, new versions of OpenGL have always had strong backward compatibility.

I am not sold on Vulkan at this point either, but in terms of cross platform alternatives, I see no better alternative, at this moment.

-------------------------

glebedev | 2019-07-24 07:38:31 UTC | #68

I've take a pause with Urho3D recently and started to explore alternatives. From this experience I would suggest not to switch to Vulkan completely but adopt SPIR-V and SPIRV-Cross. This will allow to expand platform list as it supports shader code generation for OpenGL (+ES), DirectX, Metal and it is native to Vulkan.

The problem is that with it the Urho3D will loose compatibility with existing shaders and older platforms like OpenGL ES 2. I would guess 2020 is a good time to let them go.

-------------------------

Leith | 2019-07-24 07:44:50 UTC | #69

I don't see why we need to "lose compatibility" in terms of a new back end rendering layer.
At least I can see a kludged together "try, then fall back" setup working, without much effort.
I know, I am simplifying, but that should be our aim.

-------------------------

glebedev | 2019-07-24 07:54:37 UTC | #70

I meant that all hand-written shaders won't work anymore. The Urho3D can still be compatible with older versions on Material/Technique and the actual shaders shall be updated to the Spir-V compatible GLSL.

But the good thing - you can throw away HLSL shaders and never come back to supporting multiple shader languages.

-------------------------

Leith | 2019-07-24 08:07:09 UTC | #71

To make an omelette, you need to break a few eggs
So far the social vote here seems to be that, hey, its, ok, to break a few things, for the greater good
Personally, I think that refusing to change, is an indication that you are decaying, and not growing.

-------------------------

elix22 | 2019-07-24 09:38:59 UTC | #72

I am not trying to promote anything ...
But have you tried my Urho3D OpenGL-ES2  running on top of  Vulkan/Metal back-ends ? 
It works quit well , SPIR-V and SPIRV-Cross are being used to convert GLSL to SPIR-V and/or Metal Shading language .

The latest is on my angle-20190712   branch.

https://github.com/elix22/Urho3D/tree/angle-20190712
- # [`Wiki`](https://github.com/elix22/Urho3D/wiki)

-------------------------

glebedev | 2019-07-24 17:39:39 UTC | #73

Why this is not yet in the main branch? :-)

-------------------------

elix22 | 2019-07-25 04:32:08 UTC | #74

Eventually it will .
For that to happen :

* I have to be very confident that it works well on all MacOS and iOS devices on top of the Metal backend.
So far only @ [johnnycable](/u/johnnycable) helped in verifying it on his 2 devices.
It would be helpful if the community would help in testing it on various iOS/MacOS devices and provide some feedback.

* I am working on it alone during my spare time , so I need more of it(I don't have much of it lately)

* Although I am aware that fixing the remaining issues requires specific skills that are absent from the most members in this community , actual help in fixing the remaining issues would be more than welcome (shadows support on iOS , SDF support on all platforms  and some small memory leakages on iOS/MacOS) .

The actual thread of this feature is 
https://discourse.urho3d.io/t/metal-moltenvk-support-for-ios-an-mac-devices/4845/52

-------------------------

rku | 2019-07-25 08:03:03 UTC | #75

@elix22 this is so very wrong. If it were my decision i would not allow such hack anywhere near `master` branch. I am not saying it to take a dump on your work. It is great as an experiment. Problem is that you stacked multiple intermediary levels of API abstraction on top of least featureful Urho3D renderer. It may be a good solution for a very specific application that must run on metal. It is absolutely terrible as a general purpose solution. Not only there will be a performance penalty due to all these layers of abstraction, there will also be cryptic bugs coming from gods know what layer. At present time Urho3D does not need any of that because running on metal or vulkan gives absolutely nothing. OpenGL ES2 applications still run on iOS. Project may benefit from a metal renderer for some future proofing. And D3D11/OpenGL backends will be enough for quite a long while still. Which means we should not take a horrible shortcuts for the sake of "new and shiny" only.

-------------------------

elix22 | 2019-07-25 09:08:56 UTC | #76

My main motivation was to replace the deprecated OpenGL/ES  on Apple devices .
Yes OpenGL/ES2 is still running on MacOS/iOS  but it is  officially deprecated by Apple,  it means that they are going to remove it entirely in future Versions (probably next year)  , which means you won't be able to run Urho3D on Apple devices , this is a backup solution for such an event. 

Lets hope that by some miracle Apple will revert its decision on deprecating OpenGL/ES .

> Not only there will be a performance penalty due to all these layers of abstraction, there will also be cryptic bugs coming from gods know what layer

The performance is surprisingly very good even on low-end devices such as iPhone 5c.
You can download and try the samples, you will be surprised on how well they work on Metal/Vulkan The abstractions (Angle-Vulkan & MoltenVK) are already very stable and feature complete , bug fixes  will arrive mostly from the big players such as Google and the "The Khronos Group".

Given the state of the (no) development of this engine , and given of the imperfections and instabilities of the other Graphics solutions (take my word on this , I tried them all) , I think this is the best option for the "rainy day" .

-------------------------

johnnycable | 2019-07-25 15:48:13 UTC | #79

[quote="elix22, post:76, topic:4778"]
The performance is surprisingly very good even on low-end devices such as iPhone 5c.
[/quote]

I can confirm that. To tell you the truth, the very curious thing is a couple of examples run 2x 3x *faster*..., to the extent you can't interact with the device... :no_mouth:

-------------------------

Sinoid | 2019-08-14 01:53:13 UTC | #80

[quote="glebedev, post:68, topic:4778"]
I’ve take a pause with Urho3D recently and started to explore alternatives. From this experience I would suggest not to switch to Vulkan completely but adopt SPIR-V and SPIRV-Cross. This will allow to expand platform list as it supports shader code generation for OpenGL (+ES), DirectX, Metal and it is native to Vulkan.
[/quote]

While SPIR-V bytecode itself still isn't viable for GL support-wise (basically nothing *budget-level* supports it), SPIR-V cross and glslangValidator are definitely worthwhile endeavors now that they've finally become viable over the past year. MS oss'ing their shader stuff a while back apparently put a bon-fire under khronos to actually get things done.

Just a shell-tool tying in with the internal shader-defines to offline check shaders for errors is a blessing. Cross-compiling is a boon.

There is the catch that those tools are so pedantic that I suspect Urho3D's shaders would all fail given how many hands have touched them.

[quote="Leith, post:69, topic:4778, full:true"]
I don’t see why we need to “lose compatibility” in terms of a new back end rendering layer.
At least I can see a kludged together “try, then fall back” setup working, without much effort.
I know, I am simplifying, but that should be our aim.
[/quote]

**Just in Urho3D::Graphics and keypoints of the render-loop**:

Half of `Urho3D::Graphics` members become meaningless when you're looking at Vulkan, even if you're using V-EZ (which is definitely the way to go given how data-fed Urho's rendering is).

This gets worse and worse as you move through the graphics objects.

---

Some things are indeed not *that bad* as far as cludge goes. Threading has been brought up regarding Vulkan/DX12 but really that's only applicable to batch-rendering loops - and even then only really meaningful for the 3d drawing loops (Urho2D / UI, probably wouldn't gain a whole lot and have unique 2D-related concerns). That's just splitting up command-buffer building into what the threadpool can handle then submitting them later. #ifdef around and put an alternate Vulkan specific implementation in another file ... not terrible - but cludge.

There's also some restructuring that would have to happen there as Vulkan doesn't really let you halt to upload a random uniform buffer. Now you need an outer command-buffer (stage bits are per submission, not per frame) that if you're using threading must always be accessed under lock - this creates weirdness. Thus you now need a pre-pass over the render pipeline to assess your uploads so that your workers aren't lacking or multiplying work.

That nastiness is the reason render-graphs became a thing.

---

**Globally**:

Transfering data (buffers/textures and transitioning [MSAA]) lack the outer atomic behaviour that Urho3D expects from GL/DX9/DX11. As above, that means refactoring or cludging.

---

To what queues does a resource belong? Are all resources exclusively for graphics? Should all resources support compute? Supporting all queues is an easy way to fail the nasty nuances of the resource usage bits.

---

Resource views in Vulkan are alien to the older APIs. A single UBO can be updated for all lights to be rendered but only a portion of that bound to each forward-lighting draw-call for that particular light instead of constantly updating/cycling small UBOs. Edit: there are analogs - they just suck to use.

---

It's not in core Urho3D but at least a few have probably implemented texture-buffers, in a renderer that supports GL and Vulkan that is a mess, one API handles them as textures and the other API handles them as buffers.

---

Introduces yet another API that has discrete sampler objects (GL sampler objects still have garbage support), this creates added pressure for other features like per-material sampling traits (maybe that's already there ... I'm wayyy out of date).

Edit: removed unnecessary hostility.

-------------------------

codexhound | 2019-08-14 09:06:03 UTC | #81

I just want to import that UI editor. It's beautiful.

-------------------------

Modanung | 2019-08-16 21:43:48 UTC | #82

Indeed some dragging, dropping and more dragging should be enough for creating a basic UI setup.
But I'm missing icons in their _UI Library_. A list of only text has insufficient visual cues, in my opinion.

Those people at Xenko sure made up some creative [editor-element names](https://doc.xenko.com/latest/en/manual/ui/media/ui-editor.png), btw: The _Visual tree_, the _Solution explorer_ and the _Property grid_, really? I'll just call 'em _Node tree_, _Resource browser_ and _Properties (editor)_ - or something along those lines - in ManaWarg.

-------------------------

