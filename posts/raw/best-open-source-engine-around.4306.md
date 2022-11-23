smellymumbler | 2018-06-10 18:51:02 UTC | #1

There's a lot of negativity around these parts lately and I just wanted to thank the developers of Urho3D for making the best open-source game engine around. Not because of bells and whistles, but because of modularity, extensibility and code maintainability. It has one of the best architectures I've ever seen and you guys **_rock_**. I'm learning so much from it.

-------------------------

TheComet | 2018-06-11 06:55:07 UTC | #2

I second this opinion!

-------------------------

mustacheemperor | 2018-06-19 16:04:09 UTC | #3

I agree, this engine is far more capable than other projects like Godot and is also quite robust already even though there's hills left to climb. Honestly, this project is really suffering more than it deserves recently from the lack of distinct leadership. Without Cadaver, it feels like things are a bit unsteered right now even though it's clear on github that people like Egor are contributing quality code and working hard. The project needs someone who has deep knowledge of the engine and the time to communicate with the communities both developing with and for Urho. It's not fair to ask that of the remaining productive contributors if they don't want to do it, though I think it'd be awesome if someone from Xamarin stepped up as project leadership. Microsoft is investing in Urho to some degree, but the community is languishing right now and that is not good for this kind of project. I'm surprised at how much more buzz Godot gets online than Urho. This is nearly an open source Unity competitor, and it runs on damn near everything. MS also dropped the ball on XNA so I don't think we should count on them to keep this project afloat. 

But there's a great example: unless the Metal bindings happen it'll be off iOS forever because nobody has been able to rally the troops any of the times the issue's been raised. How can a mobile game developer be honestly expected to adopt an engine that can't run in the most profitable mobile marketplace?

Edit: Actually, in the metal discussion thread there's a guy bragging about how fast he built the bindings and selling them. That's all you need to see.

-------------------------

Lumak | 2018-06-19 16:34:50 UTC | #4

Here, I corrected this for you:
> Honestly, this project is really suffering more than it deserves recently from the **demoralizing leadership**.

-------------------------

weitjong | 2018-06-19 17:05:21 UTC | #5

Just to put the record straight. When cadaver stepping down as the project lead, no one else step up to fill his role, me included. I am merely keeping the project alive while waiting for cadaver to come back or any one who has the same passion to continue cadaver's work. So, don't let me hold anyone back. Please step up and show yourself. However, so far people that I know of that are capable of doing good to the project are shying away for taking more responsibility. I can understand people just want to make game and make money instead of making free game engine. What I don't understand is, the very same people that should have taken bigger role in the project are the ones complain about the project lack of leadership.

-------------------------

TheComet | 2018-06-19 19:10:13 UTC | #6

At least in my case I don't want to step up because I don't have that overview of every line of code in the engine as cadavar did. That and I have doubts about being able to deliver.

-------------------------

Blackfox | 2018-06-20 07:20:56 UTC | #7

Last time I try near 10 different engines. Result always was "**NEGATIVE**". Usually all engines looks like unusable overweighted stuff. Things like Blitz doesn`t have much features. Urho3d have all I need. Fast, compact, ultracomfortable, I don`t need to launch slow-motion IDE. All I need is F7, F5 + notepad to make new project. And O`korz good perfomance. It looks like you make best thing.

-------------------------

Modanung | 2018-06-27 21:06:21 UTC | #8

4 posts were split to a new topic: [Choice of engine](/t/choice-of-engine/4359)

-------------------------

Alan | 2018-06-28 04:13:28 UTC | #9

[quote="Blackfox, post:7, topic:4306"]
Things like Blitz doesn `t have much features`
[/quote]
Now that isn't very fair in my opinion, Blitz (3D/Max) or more recently Monkey aren't on the same league, you can compare them to say XNA maybe, but comparing them to Urho is apples and oranges.
That being said I totally agree with everything else you said. Urho code is easy to pick up, it's lightweight compared to other engines, and has all the important features.

-------------------------

cadaver | 2018-06-28 09:05:33 UTC | #10

Godot has IMO earned its hype though, by the developers being active and community-oriented, even if there are shortcomings. 

The flipside of hype / buzz is too many expectations and potentially getting burned out or bitter from those expectations not being realized, but that's always everyone's own responsibility.

And let me repeat one more time that I'm not coming back. I think you're doing fine, as long as everyone maintains realistic expectations. I also now believe more firmly that engines should have a concrete game project behind them, so with the knowledge I have today I would likely not have started Urho at all, or at least kept a stronger disclaimer that hey, this is just a learning project for rendering techniques, do not use :)

-------------------------

fnadalt | 2018-06-28 14:27:00 UTC | #11

"Do not use?" man I think this engine is awesome. Wish I have enough knowledge to take it up....

-------------------------

cadaver | 2018-06-28 14:56:15 UTC | #12

Note the smiley. It's all about expectations, so when you know exactly what you're getting, then it's no problem. Certainly the engine was a necessary "mistake" to make, especially in that time, when on the open source front there was practically just Ogre (+ some more smaller, obscure or abandoned / stalled engines).

-------------------------

slapin | 2018-06-29 01:10:01 UTC | #13

About engines and opinions... through some years I looked at some engines and created
some opinions which I'm more than happy to share now and then:

1. Godot - hype/buzz based development. Most disappointment is from false expectations and developers' false promises. Technically a problem with it is that their direction is quite chaotic.
Also engine features are always have lower priority than ease of use/simplicity which is sometimes not quite logical. It is somewhat changed with 3.x versions, but still shows-up from time to time.
There are some great people there which do stuff though, physics side was quite improved in 3.0, but they dropped GLES2 which makes me just observe Godot development, but not actually use it.
Also it is hard to get help from the community for anything more complicated than some basic things, as the engine is mostly used for very simple games.

2. Torque3D - been powerful once, but now one-man project with small community. Has a lot of features everyone forgot about and re-discovered again. Very powerful editor and if you're going for a shooter with a small map, it is way to go. A problem is that it does not support OpenGL ES. Renderer is quite good, but no mobile path. The development is very slow but steady (it is developed in free time by single great person). Asset pipeline for characters is hardcoded on Biped from 3Ds max which is sad sad sad (lots of older code depend on 3Ds Max). Props and enemies are based on Collada and the asset pipeline is quite fluent, I'd say it is much better than any engine from this list except for Armory. Also use script as data everywhere is fantastic and much better than xml/json.

3. Armory3D - a new bird. Been playing with it for some time, it leaves a lot to be desired (countless basic things are missing, but still looks great as a concept). Uses Blender as editor for everything. Implements node logic and haxe scripts (can run native code via haxe though). Targets lots of platforms, including Linux, Android, MacOS, iOS, html5, wasm, etc. Looks very promising as it implements both design-oriented and code-oriented approach. For me current serious shortcomings are lack of any sort of documentation for things like to/from ragdoll transition, complete lack of layered animation. But asset pipeline is so easy that I can't stop playing with this engine for some things. The renderer is great and mature. Nice thing, definitely worth observing.

4. Urho3D - I'd call it not engine per se but a framework/library to write engine for oneself with all features you need writing them from scratch. If that is your approach, then it is way to go. Urho3D is quite feature-complete on low-level (unlike Godot for example) but to actually make things work the needed way one is supposed to write middle-level and top-level subsystems/components. If you have serious experienced team who can do it, the go for it (I think in this case you could write engine from scratch too). Otherwise you can write simple games like in Godot but with inferior usability and less featured editor. Or you can like me learn things and write code for years in hope to not develop Alzheimer before you finish it. Asset pipeline is more friendly to simple models and low bone counts (bone count is better than with Godot and T3D, but worse than with Armory). Exporting meshes is simple, but for other things one is supposed to write exporters/tools/editors. But this gives great chance that when (if) you are complete with all this you will have most great tool set for you and your engine will lack any bloat. Probably. If some group of people did write some set of middle-level subsystems which would make some frequent tasks easier, that would make the engine more accessible, but that would turn away people who are against "bloat" "even on source level".
So to be honest, among 4 listed open source engines, if I just come here not spending some years making game using Urho, I would not recommend it for non-professional use. But this engine is most powerful of all four with things you can accomplish with it. If you can.

-------------------------

johnnycable | 2018-06-29 10:23:08 UTC | #14

[quote="slapin, post:13, topic:4306"]
There are some great people there which do stuff though, physics side was quite improved in 3.0, but they dropped GLES2 which makes me just observe Godot development
[/quote]

Have to correct you here; things are now reversed. Opengles2 will be kept for low level rendering targets, and vulkan -> metal something for high level. Read [here](https://godotengine.org/article/abandoning-gles3-vulkan-and-gles2)

[quote="slapin, post:13, topic:4306"]
Torque3D
[/quote]

Really?

[quote="slapin, post:13, topic:4306"]
Uses Blender as editor for everything
[/quote]


:heartbeat::heartbeat::heartbeat::heartbeat:

[quote="slapin, post:13, topic:4306"]
haxe
[/quote]
NO!
Everything short of C++ is simply not serious for game development. You gain traction in the beginning, and stop in the middle. Anything script should simply be forbidden.

[quote="slapin, post:13, topic:4306"]
If some group of people did write some set of middle-level subsystems
[/quote]

that is too much dependent on use cases to be really doable. Even if you do, contributing back could be a conversion hell...

-------------------------

smellymumbler | 2018-06-29 14:50:54 UTC | #15

I think you guys might want to continue this discussion on the thread that @Modanung split: https://discourse.urho3d.io/t/choice-of-engine/4359/9 

Let's keep this one for discussing the strengths of Urho and why it rocks! :slight_smile:

-------------------------

TheComet | 2018-07-03 14:01:27 UTC | #16

[quote="cadaver, post:10, topic:4306"]
so with the knowledge I have today I would likely not have started Urho at all
[/quote]

What exactly is this knowledge you know now that would have prevented you from starting urho?

-------------------------

slapin | 2018-07-04 11:25:16 UTC | #17

As for Godot vs OpenGL ES 2 - these are only words, lets see when it is implemented. It was too frequent to be let down by Godot developers, so I never even read their plans or proclamatios - only git commits
and issues.

Torque3D is really cool, try it. Have shooter of your dream in a few hours is fun.
Also you can overcome much of it asset pipelime limitations using a bit of C++ knowledge, if you target only PCs.

As for Armory - it is WIP and progressing quite well. As I mentioned - you can use C++ code if you target native architectures (Linux, MacOS, Windows), but not when targeting html5/wasm/js.
Probably they eventually resolve this. I don't care much though at this moment. Haxe is compiled to native code and looks fast enough for my purposes at this moment. I do not try to do something big like with Urho, just some small for a change.

-------------------------

cadaver | 2018-07-04 16:33:16 UTC | #18

That engines are a shitload of stuff, not just the obvious graphics + physics + animation but platform support, social / advertising / IAP mechanisms etc. That it's a constant struggle to stay current, with new API's cropping up.. That pro engines do it with tens (or even a hundred?) of fulltime employees. And that without a real game or other "do or die" project to back it up, I will eventually run out of interest.

-------------------------

slapin | 2018-07-04 18:55:41 UTC | #19

This could be said about any framework or library. Some game engines are just plain libraries, some are full-blown self-contained content development platforms. One just need to choose where to stop.
Having real project would of course make the whole thing easier, as most of commercial game engines was developed for a game first and then was made into all-purpose engines and evolved.
Understaffedness is common problem even for commercial engines, some projects overcome this by "bounty list" and roadmap thing, others by "doing what they can" and not allowing much development, but manage somehow. Some are so greedy that prefer to delete their github repository than let other people develop it, some just constantly whine about understaffedness when asked about features implemented but when you submit patch to them with feature implemented and tested by a few people they refuse your patch because they "did not have this feature planned", would prefer to implement it themselves, and drop your PRs/submissions.

So everyone manages somehow, the situation is not unique and not something to feel bad about.
It just requires spending some time, creative ideas, people who are truly interested (not just saying that) and progress which is possible to show (not just constant architecture shuffling, the actual things people need. If people don't need anything, your project is dead (as there is no such thing as completed software)).

-------------------------

cadaver | 2018-07-04 20:03:43 UTC | #20

Sure, and now that Urho exists, you have all the opportunity in the world to solve these problems :) 

The problem of scope, related to open source engines, is interesting. Obviously a full game engine is a (too) large undertaking for a solo dev, yet I don't think there have been very successful results from just putting together a bunch of libraries, or trying to provide a "core" for others to extend. Rather, the tempting approach is still to attempt doing the whole thing, or nearly the whole thing with perhaps only the graphics library as external.

This goes a bit back to the "make games not engines" mantra. For example, integrating a physics engine or a scripting language for just your own needs in a game will be more focused, likely faster, potentially also dirtier than providing the integration in an engine for others to build on.

-------------------------

slapin | 2018-07-04 20:56:33 UTC | #21

I think the most important thing for any game engine is asset pipeline. This should be as fluent as possible
and allow quickly putting-up visual aspect of game so to show to others. Also having some common high level systems help a lot. There are common tasks people do, which makes engine the engine and not just assorted framework of different things. But after this comes a point where people have different goals, i.e. some people want minimal engine without physics/anything, just ECS + renderer. Other people want more powerful scene graph, some want some AI helpers. The problem with Urho in this aspect is mainly lack of ground for implementation of such systems. So even if you decide not to "write game for anybody" you still want engine to have not too high entry complexity. Simple example - having node editor UI element would make many tools development much easier. Also adding simple 2d rasterizer drawing lines, arcs and text would allow much better debugging and nifty things. These things are still low level enough to not "write games" for someone, but help a lot in writing these games, as with engines like Urho one first writes tools and then writes games. So there is a lot of features one can implement which are completely generic and still very useful for implementation of high level systems. Also improving editor's interface to components (like adding custom per-component editors) would also quite improve quality of life. As I truly believe that a set of simple common components for multiple game genres (like behavior trees, data-driven animation tree, etc.) would not hurt too (but there are people who are extremely againt that), but these are for the end with a cake.
But still I truly believe that if Urho's asset pipeline was as fluent as at least Torque3D, that would not hurt anyone's feelings and drastically improve engine overall. And would add at least one happy person here.

-------------------------

TheComet | 2018-07-05 06:11:06 UTC | #22

[quote="cadaver, post:20, topic:4306"]
“make games not engines”
[/quote]

Or more generally, "don't reinvent the wheel"

-------------------------

Alan | 2018-07-05 22:21:12 UTC | #23

I second that the asset pipeline is one of the most important thing that's currently missing. The Blender exporter is OK though, and many (most?) indies use Blender. Besides that in my wishlist there's a new editor too. However, these things require a substantial amount of work.

The renderer could use some modernization but I feel that for indies GL3.3+DX11 is still OK and many (most?) even target older APIs (DX9+GL2.1) because supporting old hardware is much more important for the indie audience.

Overall I've had my gripes with Urho (especially when it comes to rendering stuff manually), but in my opinion it's a great engine for indies! It doesn't have the bestest pipeline, collaboration would be a bit of a pain (LFS + one-way arts?) and of course it's not the greatest one when it comes to rendering, but if you're making a photorealistic game with a budget and a team, then there are of course other options to consider.

That being said, the core is getting old quickly, it doesn't extract the performance of modern hardware as it could, not even mobile. While GLES2 is still very common, in terms of CPU everything has many cores/threads these days.

-------------------------

cadaver | 2018-07-06 16:25:17 UTC | #24

I'd phrase that more as "reinvent the wheel when you know you have to, otherwise don't"

-------------------------

Modanung | 2018-07-07 11:50:11 UTC | #25

[quote="cadaver, post:24, topic:4306"]
reinvent the wheel when you know you have to
[/quote]
[details=Something like this?]
![image|397x500](upload://pgaleg1sZ1xktckBN3vEyPskHhr.jpg)

[Gwar - The Wheel](https://www.youtube.com/watch?v=dak-mudrugo)
[/details]

-------------------------

slapin | 2018-07-07 06:46:54 UTC | #26

Not this kind of wheel I presume. This kind:

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/e/ea713e962b9a60c81be4edabaacc7061d1742070.jpg'>

-------------------------

TheComet | 2018-07-07 11:31:43 UTC | #27

Maybe the key is to not re-invent the wheel, but shape the world around your wheel so it works anyway:

https://www.youtube.com/watch?v=FayemJb2-w4

-------------------------

johnnycable | 2018-07-07 13:12:00 UTC | #28

Best workout tool ever

-------------------------

QBkGames | 2018-07-14 08:14:57 UTC | #29

After spending considerable time trying out a number of popular engines out there (Unreal 4, Unity, Lumberyard, Godot, etc), I have to say that what makes Urho3d truly unique is the fact that it's a lightweight, yet complete engine that does contains all the functionality required to build a game. It's also easy(er) to learn and understand and to get started with (if you are a coder). So far, with Urho I've been able to do more than with any other engine. I certainly hope it keeps going.

-------------------------

JTippetts | 2018-07-14 22:00:28 UTC | #30

From what I've seen through the years, the open source projects most likely to survive long-term are those which attract corporate backers who have a vested interest in the project staying alive and healthy, and who are willing to pour money into it, or which originate from and maintain a foothold in academia (see Lua). Additionally, they mostly have a "Benevolent Dictator For Life" calling the overall shots, even if the actual development is done by others at the dictator's direction. Design by committee, where nobody is really in charge or has the final say, rarely seems to work well. Such projects usually end up mired in a swamp of conflicting styles and visions, while falling further and further behind the technology curve. They also give rise to a vast amount of bickering and infighting, that can further hamper progress and damage the brand.

I can understand @cadaver not wanting to continue in the dictator role. It's a huge investment in time, for little to no gain without the backing of corporate sponsors. I think maintaining an engine of this scope long-term is outside the capabilities of a lone hobbyist developer. I believe that if Urho3D is to continue, and not dwindle, it is going to need a new BDFL with a salary, and some source of funding (whether corporate sponsorship or crowdfunded). Without that, I just don't see it progressing to keep up with the new technologies already in play, much less any new stuff coming down the line.

Godot seems to be in a similar boat; the difference there, from what I can see, is the existence of crowdfunding efforts, and a BDFL that currently seems invested in the project. Even for all that, in my experience with both engines, Urho3D is the superior one, and I will be personally extremely saddened to see it wither if such is to be its fate. I do stand ready to contribute financially to this engine, if at some point the ability to do so comes into existence.

-------------------------

Alan | 2018-07-14 23:00:05 UTC | #31

Lua had a ton of commercial interest from the industry, not just academia. But I agree, projects need strong leadership from a committed person, democracy doesn't work very well :P .

Urho is so much better than Godot at least technically, but Godot has the editor and all the "*cool*" stuff people expect these days like visual programming, asset store, GI, devs active on social media... that attracts the noobs (as @rku puts it) who provide a ton of free publicity and then it's a virtuous circle, more community means more users and more visibility, and a few of those users are happy to contribute financially to the project.

Urho isn't going to stop working or something though, and DX11/GL3.3 are still fine for new indie games, but they're getting obsolete quickly, same with the single-threaded internals.

-------------------------

smellymumbler | 2018-07-15 01:23:36 UTC | #32

FYI: Lua's development was largely funded by Petrobras, a very large state-owned oil company.

-------------------------

QBkGames | 2018-07-15 06:50:04 UTC | #33

I still believe democracy could work if it's well organised and has clearly defined rules that everyone abides by. What I suggest is:
* Contributors submit their proposed changes/updates to the engine in some form (maybe pull requests)
* Have a voting system, where any user can vote for/against the change. We could have the vote of the core developers be worth more than other users, but every user is invested in the engine and should have the right to vote. The vote should be open for a limited period of time (say 2 weeks).
* Have a moderator (for a lack of committed leader), who, even if s/he only works part time, can regularly check the voting system and bring in the positively voted or reject the down voted pull requests

-------------------------

JTippetts | 2018-07-15 14:15:47 UTC | #34

One issue with this, though, is that you'll get proposals for a lot of cool stuff, stuff that's fun/interesting to work on, and no proposals for the boring stuff. Plenty of folks want to write a GI solution; almost nobody wants to maintain script bindings, or write shader variations for 3 different APIs. Sometimes, you need a boss to make sure the icky stuff gets done.

-------------------------

cadaver | 2018-07-16 11:32:14 UTC | #35

Or you need to make certain "heroic" one-off efforts so that there isn't any icky stuff anymore :) Easier said than done, though, and some things like multi platform support and the build system is never going to become just simple and beautiful, I believe.

-------------------------

slapin | 2018-07-16 13:37:35 UTC | #36

That depends on person, myself I find platform stuff and build system stuff fascinating.

-------------------------

JTippetts | 2018-07-16 23:22:36 UTC | #37

This is your lucky day, then, because as it so happens Urho3D could use a build system maintainer!

-------------------------

slapin | 2018-07-16 23:45:01 UTC | #38

I thought Wei did that, is he not? BTW, I think it is much easier

to find low level development / build system people than actual

engine architects and game designers.

-------------------------

weitjong | 2018-07-17 00:35:02 UTC | #39

Build system is easy, after someone shows you the way. And don’t count on me keep staying with the project. The project needs new blood.

-------------------------

Alan | 2018-07-19 04:45:48 UTC | #40

[quote="JTippetts, post:34, topic:4306"]
Plenty of folks want to write a GI solution; almost nobody wants to maintain script bindings, or write shader variations for 3 different APIs. Sometimes, you need a boss to make sure the icky stuff gets done.
[/quote]
That's true, and funnily enough GI is certainly one of the most desired features too, yet nobody seems to be contributing that anytime soon although @Lumak did some stuff already. 
I say let's get rid of manual scripts (and some platforms) and use a shader transpiler... the fact is a lot of the 'icky' stuff in Urho simply doesn't have much reason to exist. Insisting on keeping the 'icky' stuff while that drives away possible contributors is not reasonable imho. I don't think we need a boss to make sure the icky stuff gets done, we need a boss to get rid of the icky stuff altogether :wink:. 
We have to face the reality that there simply isn't enough manpower to maintain the current featureset with the current quality standards. It doesn't look like that's going to change soon, but I think that if Urho gets rid of a little bit of the dead weight perhaps it can keep going a bit further.
And... RebelFork Ftw! :trolleybus:

-------------------------

smellymumbler | 2018-07-19 15:51:26 UTC | #41

Not sure if GI is that important or feasible. Seems very project-specific to me. What would be cool is a a wide library of usable shaders and effects, that allows the engine to be used by many different projects, without requiring them to have a graphics programmer on the team. This also has the benefit of being small additions that different contributors can make, instead of a huge change in the engine. For example:

* Grass shader
* Foliage
* Water, water foam, waves, etc.
* SSAO
* Planar reflections
* Blurs
* Wet
* Toon

All additions that can be made by different people, without changing the architecture drastically. Easy to review, easy to merge, easy to contribute to.

-------------------------

JTippetts | 2018-07-23 21:46:07 UTC | #42

GI was just an example. But sure, you might get some submissions for all of that stuff. From where I sit, the 5 greatest pinch points for Urho3D are:

1) Backend stuff, like renderers for new architectures like Vulkan and Metal. Apple got the ball rolling on deprecating OpenGL, Microsoft is always progressing their own architecture, things are always rolling forward and without someone to write backends for the new architectures, Urho3D is inevitably going to fall behind. Additionally, without someone to prune the cruft, the engine is going to be hampered by having to support ancient architectures. For example, the D3D9 backend is quickly approaching its expiration date, and already leads to branching in HLSL shader versioning. Which leads me to...

2) Shaders. Urho3D really needs a unified shader system. I've seen plenty of tech demos that are D3D11 only, or GL only, etc... writing 'bulletproof' shaders workable on all platforms for a given tech is a hard and (most importantly) boring problem. It's boilerplate, it's tedious, it's prone to errors. Shaders written in HLSL require conditional includes depending on if they are for D3D9 or D3D11. GL shaders require differentiating between GL and GL ES. If shaders could be unified into a single common syntax and structure, to be compiled invisibly (to the user) to whatever the backend requires, that would solve a lot of the roadblocks to introducing new tech.

3) Scripting. I love Lua, but I still feel like it was a bit of a mistake to introduce Lua, at least without implementing some sort of language-neutral script binding system. Introducing tech to the engine requires the same kind of redundant boilerplate as shader code: having to implement the tech in C++ as well as provide bindings for both AngelScript and Lua. Anything less than full support for all 3 codepaths risks having the tech rejected in pull requests, yet having to support all 3 codepaths is unnecessarily burdensome to the implementer. Allowing tech into the base without full script support risks rendering the script systems useless and broken.

4) The Editor. I only typically use it for UI stuff, but in the age of Unity, having an editor is probably a necessity. Unless Urho's editor gets some badly-needed TLC, it is quickly going to become a liability rather than an asset. Ideally, of course (as has been discussed before) the editor should probably be rewritten in C++ so that it is usable in builds without enabled script support. (FWIW, I tend to prefer editors that are more closely tailored to specific games, rather than general-purpose editors. For example, I've repurposed my [terrain editor](https://github.com/JTippetts/U3DTerrainEditor) to create hex-tile levels for my game, Goblinson Crusoe, something that would be quite difficult to do with the Urho3D editor.)

5) Build system. What we have works, and works pretty well considering the relative complexity of supporting so many environments. But it definitely has its drawbacks, and I think that new project launching and minimal application scaffolding could use some love as well. 

A case could be made for including UI as a 6th point, but I personally don't find the UI system to be too onerous, all things considered.

Unless these 5 issues are seen to, I don't know that Urho3D has a very rosy future. And unless we can attract talented developers to contribute to these 4, then they'll continue to be sticking points.

I think what Urho3D needs most is evangelization. It's a solid library. I've introduced many people to it over the years, and most of them have loved it. It has always baffled me as to why it isn't more popular and well-known than it is, given its strengths. @cadaver, @weitjong, and everyone else have given us a pretty cool engine, now we just need to sell the shit out of it so that we can keep it alive and help it to grow.

-------------------------

rku | 2018-08-08 06:33:46 UTC | #43

As for build system i have given my old attempt some love recently and it seems like it works with exported cmake projects now. Can not do full test because current build system/CI setup fights against me every step of the way though. In case anyone wants to pick it up - nudge me and ill point you to it.

-------------------------

elix22 | 2018-08-08 09:12:47 UTC | #44

[quote="rku, post:43, topic:4306"]
In case anyone wants to pick it up - nudge me and ill point you to it
[/quote]

I am interested  
Twenty chars

-------------------------

rku | 2018-08-08 09:28:19 UTC | #45

https://github.com/rokups/Urho3D-Upstream/commits/add_subdirectory

-------------------------

glitch-method | 2019-08-26 01:14:27 UTC | #46

i feel i should say, stagnant or not, urho3d is far from dead.

i'm just a "noob," trying to push a grandiose project forward more or less alone, with almost zero knowledge of rendering or game engines. after months of looking at puffed-up crap "solutions," here i am. trying to make the process too "friendly" also introduces limits. there's no way around using/tweaking/making multiple tools if you want anything original.

my buddy (who tries to help but doesn't code) and i may end up using unity or the like short-term. but for my end-goal, i believe urho3d (+nuklear) is exactly what i was after. light, flexible, tweakable, without bloat or silly restrictions.
I just have to learn what anyone serious about this kind of game project should know anyway.

frankly, i don't care about dx12 or vulkan, or "losses" because //apple/ doesn't want to support/ a mature open standard. i'd rather make a unique game that runs well on 10-year-old hardware (for the masses), than one that "takes advantage of the newest and best" to look shiny (for those with gaming rigs).

imo there's not a lot this project /needs/.
it wants a few things, polish or maintenance or new API bindings...but that's what the community is for. it'll get done when someone needs it. 
needs? maybe a better docs system, and /exposure/.

-------------------------

Modanung | 2019-08-26 01:37:32 UTC | #47

And a better editor of course. :slight_smile:
[![ManaWarg](https://gitlab.com/luckeyproductions/manawarg/raw/master/logo.svg)](https://discourse.urho3d.io/t/manawarg/5403)

-------------------------

glitch-method | 2019-08-26 03:06:58 UTC | #48

maybe, i'm no authority on that, for sure. but several engines' editors crashed right out of the box on my laptop, godot couldn't keep window and mouse geometry aligned once maximized, etc... from what I can see so far, unity is the only one with a really "better" built-in editor, but it's almost apples and oranges... unity is a big machine with a cult following, aimed at getting new users, urho3d is still small and only recently truly community-driven, aimed at giving experienced devs a flexible framework.

keep in mind i'm a noob (please correct me where i'm wrong), pretty ignorant about game production. but from a logician's standpoint, urho3d is still the right tool for the job, with or without work on the editor.

myself as an example:
i'm not sure how much use i'd give any engine's editor. i'm comfortable enough with code, but i personally don't have much interest in things like 3d modeling, and the whole rendering half of my project feels secondary to the lower level mechanics. my search over the last couple months had become "what engine /can/ render my mechanics (without major hacks)" simply because they're not intended to rely on pre-baked assets, and most engines (with "better editors") seem to want everything baked before run-time. this doesn't seem to be quite as severe a handicap with urho3d. and by the time i'm really ready to use an editor, it seems like i'll mostly be using my own (variant)/nuklear in runtime, and i guess blender/collada anyway.

so, maybe, i get that my method is an exception, but afaik i'd still file editor updates under "want" and not "need."

-------------------------

glitch-method | 2019-08-26 03:35:07 UTC | #49

oh it's a link. -_-'

that does look nice and clean, actually... 😂

-------------------------

suppagam | 2019-08-26 13:15:11 UTC | #50

Urho's performance compared to pretty much every other engine out there is amazing. The thing just runs, and maintains awesome FPS the more you throw at it. All this on pretty much any potato computer. As long as you don't use the PBR thing, it's crazy fast.

-------------------------

Sinoid | 2019-09-04 03:10:58 UTC | #51

[quote="JTippetts, post:42, topic:4306"]
Backend stuff, like renderers for new architectures like Vulkan and Metal. Apple got the ball rolling on deprecating OpenGL, Microsoft is always progressing their own architecture, things are always rolling forward and without someone to write backends for the new architectures, Urho3D is inevitably going to fall behind.
[/quote]

Integrating a gutted version of BGFX looks better and better as time passes, take the working bits and tear out that BX and BIMG filth. Dump that ShaderC scum for SPIRV-Cross for HLSL->GLSL/SPIR-V.

---

Vulkan is still a giant shit-stain that crumbles under 162 instanced Utah-teapots while OpenGL does it's thing (4 draw calls for Vulkan). I renamed my stress test project to `DOOMx64vk.exe` and matched the metadata, for a whopping 10% perf-upgrade (because I patterned my usage after RenderDoc outputs from Doom captures). 

Driver bullshit isn't over. Sad reality is that today is probably just Glide all over again. *Life changing graphics shit that's over-hyped and way over-pumped* ... dead in 4 years is generous (glide lasted a very long time, we're at the apex of glide).

OpenGL is a massively better option in the long term. So much Mantle/PS documentation being under-wraps assures that Vulkan is probably toast. DX12 also at least prioritized clearing textures ... clearing buffers in Vulkan is infuriatingly slow.

Let's not forget that GNM-1 still has async compute *silently* disabled on PC in Vulkan because it's a dumpster fire that doesn't work.

-------------------------

nodageboh | 2019-09-04 03:43:31 UTC | #52

bgfx is terrible, hard to build, and the whole Orthodox C++ bullshit goes against the decent architecture and code behind Urho.

-------------------------

Sinoid | 2019-09-04 07:04:32 UTC | #53

You're not wrong, I despise BGFX particularly for that nonsense ortho-C++-horse-shit and the BX/BIMG scum - that bottom of the barrel worthless trash has to go.

What I mean is taking the core of BGFX, refactoring it to use our types and properly tying it into our build system, while ditching all of that trash that comes with BGFX (BX/BIMG ... I can't call those trash enough times).

Offloading problems isn't a bad decision and one of slicing consequences as preferred.

Sadly, assessing real problems is a dead talent, it's just *DOD ALL THE THINGS*, despite Quake-3 era super-classes usually being exactly what you need, very few varieties of genuine things.

-------------------------

johnnycable | 2019-09-04 14:59:12 UTC | #54

Let's see the market.
The "paying" market, I mean,
50+% whole gaming is on Windows. MS has its own renderer.
The rest is on Ios. Apple now has its own renderer.
Vulkan? What's its platform? Linux. Out of paying market.
No customers for Vulkan. And no customer means no usage, no improvements.
OpenGL has its foot already, going to last for a few time, until Ios scraps it.
Vulkan is no adoption. Play the dead march.

-------------------------

suppagam | 2019-09-04 19:24:11 UTC | #55

Urho3D is great the way it is. Most people want to see more samples and docs: https://discourse.urho3d.io/t/what-do-you-want-to-see-in-urho-core/5453

-------------------------

Eugene | 2019-09-11 22:29:13 UTC | #56

What do you think of Sokol and Diligent graphics frameworks? They both look better than BGFX.
Sokol is basically BGFX without shitshaders and batch abstraction hell.
Diligent is kinda huge thing with the size of the engine, but quite feature-full.

Or The Forge that I didn't look at, however this thing seems to abandon WebGL altogether.

-------------------------

Sinoid | 2019-10-29 08:11:36 UTC | #57

@Eugene, Sorry I missed this for so long. I like Diligent a lot but it's brittle as hell in the build process.

If it comes down to Diligent vs BGFX, I'd choose Diligent just because of the attitude behind the project. BGFX maintainer has a nonsensically stupid attitude about geometry shaders. He's apparently never needed to render hair where GS is basically king. Also, continues to cite antique data from when the 8800GTX-fatso was boss (I had to use a dremel to make space for my 8800).

Which is messed up because giants like Capcom will then drop shit about how much GS they're using in MT-Framework and running GS passes off of screen-space data (lost-planet fur), etc. BGFX maintainer cannot be trusted, and that's old as hell facts.

---

Truthfully, Urho's abstraction is super fast. I've been working on a library [GLVU] that's a GL3.3+ and Vulkan thing running just the rendering tasks and meeting Urho3D's targets has been stupid fucking hard.

I spent weeks optimizing said GL and VK renderer, and it still ended up losing to the Urho3D DX11 renderer, memcpy is 20% of CPU time per frame. (HugeObjectCount example's 62,500 cubes)

Only the VEZ based Vulkan backend is actually beating it, and even then it's by fractions.

For right now, I think Urho3D is still actually pretty boss, maybe just optimizing shadows with dirty caching would be enough to band-aid it for another 5 years.

-------------------------

