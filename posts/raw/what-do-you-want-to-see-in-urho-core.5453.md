suppagam | 2019-08-13 14:54:27 UTC | #1

Lately, there has been tons of discussion about the future of the engine. Some people are comfortable with it the way it is, others want more features, others want less. This is all great because it shows that the community is passionate about the project. Also, since the project is open, anyone can do what they think it's best, but it's good to know what others are thinking, so you know that your contribution won't be useless.

So, what would you like to see in Urho Core?
[poll type=multiple results=always min=1 max=20 public=true]
* Area Lights
* SDF Shadows
* SSR
* Octahedral Impostors
* QT / imgui editor
* More samples
* Tesselation
* Dynamic sky models
* GI - Radiance Hints? Voxel Cone?
* SSAO
* MSAA, SMAA
* Automatic instancing
* Ocean shader
* Networking examples: lobby, PVP
* Physics samples: destructables, fluids, controllers
* IK Examples: Limb IK, Aim at IK
* LOD for foliage, vegetation
* Performance improvements
* Bug fixing
* Lightmapper
[/poll]

-------------------------

JTippetts1 | 2019-08-12 15:02:40 UTC | #2

Completely off topic, but this post just made me realize my phone and my laptop are logged into 2 different accounts. Never noticed that before.b

-------------------------

Modanung | 2019-08-12 19:25:37 UTC | #3

I think the number of samples is reaching a point where it may be wise to start merging some. We could have a single physics sample for instance where you can drive a raycast vehicle into a tower of blocks and push a soft body blob around.
There would still be separate files for the code, just less folders and binaries.

-------------------------

suppagam | 2019-08-12 19:30:16 UTC | #4

Samples are supposed to be simple for people to understand. Those "sample binary" galleries are usually complex and require advanced code.

-------------------------

1vanK | 2019-08-12 19:44:10 UTC | #5

pls add level streaming to vote :)

-------------------------

Modanung | 2019-08-12 20:21:50 UTC | #6

(Un)fortunately polls cannot be modified after 5 minutes of their creation, it would require an extra poll.

It's good to see your (upside down) face again, @1vanK. :upside_down_face:

[quote="suppagam, post:4, topic:5453"]
Samples are supposed to be simple for people to understand.
[/quote]
I don't think a merger of sample 46 into sample 11 would require more complex code. The `Vehicle` would still have its own source files... and it could have a cannon to maintain the possibility to launch physics objects. Note that there is no terrain sample, but two samples that use terrain.
I think the sample could be made more fun (emotionally worth it) to explore by turning them into richer sandboxes. All the while giving a quicker overview of the engine's capabilities.

-------------------------

suppagam | 2019-08-12 20:22:08 UTC | #7

@1vanK, polls have a limit of 20 options, unfortunately. :(

-------------------------

suppagam | 2019-08-12 20:23:05 UTC | #8

What you are looking for is a demo, not a sample. A sample has a clear focus, and a demo is a showcase of the engine's capabilities.

-------------------------

Modanung | 2019-08-12 20:24:19 UTC | #9

In that case I'm suggesting to turn *sample* 11 into a *demo* that would still be called a sample.

-------------------------

suppagam | 2019-08-12 20:25:30 UTC | #10

Cool! But Sample 11 continues to exist.

-------------------------

throwawayerino | 2019-08-12 20:51:48 UTC | #11

Honestly the engine itself is amazing and does not lack anything I need (so far)
What I would like is more samples/learning material to encourage others to try it out and not think of it as another small time engine.
Also Urho3D 1.8 please!

-------------------------

dev4fun | 2019-08-12 21:30:14 UTC | #12

Better lightning, ocean and sky would be amazing for me atm. We can't hire someone for somethings like this? Patreon I dont think would works, coz our community is very small.

I see the Urho editor is very poor compared to others, but the best thing for me on Urho3D its the engine as library, this way I have a lot of more freedom than fuckin game engines where u do evertyhing on editor and c# (mee).

-------------------------

suppagam | 2019-08-12 22:10:09 UTC | #13

It would be cool to have a sample scene with atmospheric scattering, sun and ocean together, kinda like the sample scene from CryEngine 2:

![image|690x387](upload://cCJcB5T0FiC64N2y20iEVHx69wv.jpeg) 

Or UE:
![image|690x388](upload://mmgrZB4raTmEoP5mNJuqyaFHEYS.jpeg)

-------------------------

suppagam | 2019-08-12 22:13:55 UTC | #14

It's funny how everyone obsesses about editors, yet they're the last items on the list.

-------------------------

Modanung | 2019-08-13 09:59:40 UTC | #15

There is also the [wiki](https://github.com/urho3d/urho3d/wiki) where additions by the community could be categorized.
Do not hesitate to improve it.

-------------------------

Pencheff | 2019-08-13 01:48:46 UTC | #16

Javascript integration...anyone ?

-------------------------

S.L.C | 2019-08-13 03:04:40 UTC | #17

Definitely no.

At least for me.

We already have 2 scripting languages. Lua is already a pain in the a$$ for anyone who wants to contribute as it has an awkward binding.

If you want JavaScript then there's the Atom game engine. Which is basically a fork of this one but integrates Ducktape as the JavaScript engine.

Besides, a scripting component can be implemented as a standalone component. So anyone is free to do  it as a third-party component.

A lot of the unnecessary components could probably be moved into their dedicated repository and provided as a standalone option. For example, the Database component, both Lua and Angelscript. And to provide a minimal c++ experience with an option to try the others.

-------------------------

Dave82 | 2019-08-13 03:52:07 UTC | #18

Great , constructive topic ! Finally we can see what the community wants. For me personally what Urho lacks right now is custom depth maps and/or subtractive shadows.

And a series of advanced tutorials how to use/create shaders , how to create custom renderpaths , how the material/technique system works , how to access certain textures in shaders (depth map , shadow maps , etc) so basically a better guide how to use the 3d effect capabilities of the engine. For now if you're not an experienced core developer you have to figure out everything on your own by trial and error which is a PITA and really time consuming.

-------------------------

Modanung | 2019-08-13 10:05:54 UTC | #19

The [wiki](https://github.com/urho3d/urho3d/wiki) is also a perfect place for _that_.
Yes, it's a mess, but it used to be empty and the community changed that too in the past.

-------------------------

Modanung | 2019-08-13 10:13:55 UTC | #20

@suppagam  Did you see Lumak's FFT ocean?
https://discourse.urho3d.io/t/fast-fft-ocean-ocean/1949/9
Maybe you could make it prettier?

-------------------------

Modanung | 2019-08-13 16:26:49 UTC | #21

Just to put the idea out there. There could also be a feature-heavy repository (_within_ the [Urho3D orginisation](https://github.com/urho3d)) - I was thinking project *Leviathan* or _Iku-Turso_ would be fitting names. It would use Urho3D as its core and mainly focus on growing some noodly appendages. This way I believe everyone can stay happy together.

This would turn the discussion towards what we consider _Core_ and what should be considered _Leviathan_.

From [Wikipedia](https://en.wikipedia.org/wiki/Leviathan):
> Later Jewish sources describe Leviathan as a dragon who lives over the Sources of the Deep and who, along with the male land-monster Behemoth, will be served up to the righteous at the end of time. The Book of Enoch describes Leviathan as a female monster dwelling in the watery abyss (as Tiamat), while Behemoth is a male monster living in the desert of Dunaydin ("east of Eden").

[poll type=regular results=always public=true]
* Yes, let's introduce this split and call it **Leviathan**
* Yes, let's introduce this split and call it **Iku-Turso**
* Yes, let's introduce this split and call it **Behemoth**
* Yes, let's introduce this split and call it **Cthulhu**
* Yes, let's introduce this split, but I don't like these names 
* No, we should limit ourselves to *Core* and cloud
[/poll]

...both could be supported by a unified editor, like ManaWarg.

-------------------------

dev4fun | 2019-08-13 15:51:10 UTC | #22

Ye I already checked this lumak code of ocean. I see the people said the Urho need something like plugins, but already exists a lot of modifications by community (just search on github). All these modifications could be simplified to use as component and we could organize and list all components on Urho website, dno. Or already exist something like this?

-------------------------

Modanung | 2019-08-13 17:33:19 UTC | #23

Whatever the final form I think it would help to catgorize them in an easily modifiable location like the [wiki](https://github.com/urho3d/urho3d/wiki). This would give oversight to people who would want to work towards emplementating these extras into Core or a single neat database (like Leviathan or [Urho3D-Components](https://github.com/urho3d/Urho3D-Components)).

This is actually a continuous collaborative endeavour in its own right. Things will (e)merge. Even small and seemingly meaningless modifications matter as a part of the whole.
*Anyone* can contribute.

-------------------------

weitjong | 2020-05-17 04:27:11 UTC | #24

2 posts were split to a new topic: [openWorld - working implementation of SSR and vegetation impostors](/t/openworld-working-implementation-of-ssr-and-vegetation-impostors/6157)

-------------------------

bvanevery | 2019-08-13 18:42:47 UTC | #26

[quote="S.L.C, post:17, topic:5453"]
Besides, a scripting component can be implemented as a standalone component. So anyone is free to do it as a third-party component.
[/quote]

Several years ago, I did a complete cleanup of the Ogre3D website ecology.  I identified all the projects that wouldn't actually build anymore and moved them to a "graveyard" folder.  An overwhelming pattern, is **scripting languages that are not officially blessed, die out.**  The author of the third-party component "gets hit by a bus" so to speak, although usually not tragically.  They just lose interest in the maintenance as new versions of the engine are released and break compatibility.

I'm not sure what Ogre's policy is now, but back then, it insisted on being "just a rendering engine" and not integrating stuff like scripting languages.  They had your idea that "anyone" can and will integrate a scripting component.  My evaluation of Ogre's history, is that this kind of "add stuff on yourself" attitude, rather than supporting integrated components as core work, results in **no less than the death of the engine** for practical purposes over time.  You may say Ogre isn't dead, but really, how many years have they stagnated without moving substantially forwards?

If a *lot* of people want Javascript and will *do the work* of integrating Javascript, then that should become core.  It's the only way to ensure that things actually keep working over time.  Of course in open source, *will people actually do the work* is always the issue.  If there aren't people actually doing the work, then it's better to just say "no" to another language, so as to not water down the community focus.

Myself, I do not currently care about Javascript.  But I do care about people having misguided ideas about what will make a scripting language actually work, in the real world of ongoing project support and maintenance.  If it isn't core, *it doesn't work.*

-------------------------

Sinoid | 2019-08-14 03:05:45 UTC | #27

Occluder boxes that only draw into the software depth-test buffer would be super handy.

-------------------------

S.L.C | 2019-08-14 08:54:25 UTC | #28

While I understand what you say and can agree with it. I will interpret it differently from what you intend it.

Which is. If those libraries/components got left behind so far. It just means they weren't needed that much. Essentially they were dead weight.

If something open source is abandoned by original author. As long as someone needs that something. That someone will take over maintaining it.

If not, it just wasn't that necessary.

If this whole engine (not just a part of it) were to die today. Completely. As long as I need it. I will fork it and maintain it to my needs. Isn't that the nature of open source?

-------------------------

bvanevery | 2019-08-14 09:38:06 UTC | #29

[quote="S.L.C, post:28, topic:5453"]
Isn’t that the nature of open source?
[/quote]

Only for small scale projects that are destined to die.  *Major* open source projects do not run things with such a lackadaisical regard for infrastructure, support, and maintenance.  Having at least 1 "blessed" scripting language is really important to keeping a 3D engine going, because people write important project maintenance items on top of that language, such as Tutorials and Demos.  Without those, you fail to attract more users.  Without more users, you fail to attract more developers, because getting attention and interest is a numbers game.  If you're not planning for this kind of "big picture" ecology stuff, then you *inevitably* succumb to whatever can be maintained by 1 person.  Which *ain't much.*  Person stops dinking around, suddenly has to go survive and make money, then marches mostly to the beat of whoever their paymaster is.

-------------------------

Modanung | 2019-08-14 13:28:43 UTC | #30

@bvanevery I like how you talk. :slightly_smiling_face:

-------------------------

bvanevery | 2019-08-14 18:33:02 UTC | #31

Over the years I've seen a lot of project death.  I've been monitoring Urho for several years.  A few years ago, I contributed some CMake debugging.  Weitjong is a very competent buildmaster in that regard.  I tried to see if I could get some Samples to run with decent performance on my 2 ancient, decrepit laptops, and the results were bad.  At that point my interest was fading, and then the project leadership went into limbo.  Today the leadership isn't exactly solid, but the project did survive, so it can't be pronounced dead yet either.  I figure I should finally see whether "low spec" rendering is viable on my laptops.  I know most people think it's sexy to chase PBR, shadow volumes, or whatever other beautiful and exotic rendering features they can get their hands on, but I'm more concerned about things like basic game visualization and game UI elements.  Things that a lone wolf indie needs to bang out a game, not things that drag the indie into horribly time consuming high production values.  Truth is a lot of game concepts are "good enough" with a lot less graphics work, and players often turn on lower spec rendering anyways just so they can keep their frame rates up.

-------------------------

QBkGames | 2019-08-15 02:22:27 UTC | #32

Although I sympathize with what you are saying, that indie is usually associated with, simplistic/stylized graphics that run on low spec hardware and that we don't have the budget to take advantage of sophisticated rendering systems, I also believe there are a few advanced features that the engine should provide out of the box which would benefit all.
I'm thinking primarily of global illumination and post processing effects (especially SSAO). Even for simple graphics, these features can make the difference between your game looking like a '80-'90 game or a modern game. So I strongly believe they should be part of the Urho core, but with the option to easily be opted out of, by both the developer or the player. I've already spend weeks just researching how to do a decent looking SSAO (and still haven't done it yet), so having them part of the core would be a great time saver for all users of the engine.

-------------------------

suppagam | 2019-08-15 03:12:23 UTC | #33

That's a very good point. GI and SSAO can make low poly stuff like this:

![image|690x388](upload://hVLHKPtseIftAi9oLFNCRJmMGSH.jpeg) 

![image|690x388](upload://pKLZw81d90PZZPAiHXFgEWFolCT.jpeg) 

Look gorgeous.

-------------------------

throwawayerino | 2019-08-15 11:36:16 UTC | #34

The reason we're talking about fancy graphics now is because most core features are "production usable" (except for the UI, but at this point it's tradition to keep it that way).
Being capable of high end graphics is a deal breaker for some people and we don't want to drive them away. Even if they never release a game, they still have experience with it and could tell their friends about it

-------------------------

bvanevery | 2019-08-15 14:20:51 UTC | #35

People will plan and put work into whatever they actually wish.  But there are *other kinds* of dealbreakers for other people.  Some people want to target really pathetic hardware, like DirectX 10 class parts that are running DX11 as the interface.  There isn't basically a lot of shader oomph on such devices, and so techniques that pile on the shader cycles aren't going to work.

I haven't evaluated Urho's in-game GUI capabilities lately, but that's another area important to me.  If I can't readily skin a decent looking GUI and not have it be a pile of work, that's a dealbreaker.  For a lone wolf, getting a game together is first about getting it *running*, so it needs to be relatively easy to get basic features operational.  Adequate documentation similarly falls under this heading of "get the prototype working".  If people can't figure it out, that's a dealbreaker in practice.  Stability of a preferred scripting language also falls under that "can be a dealbreaker" heading.  Question being, the language that Urho prefers, or that the developer prefers?  Supporting Javascript isn't crazy talk, even if I don't personally care about it.

"Gorgeous rendering" isn't driving my concerns because as a lone wolf indie, I know that tends to drive up my production cost.  In my game development universe, **gameplay is king.**  Not fancy rendering.  I'm a visual artist, I'm not basically satisfied with ugly rendering.  But much of what can make stuff aesthetically appealing, is geometry, line, form, and color.  The concerns that analog artists have had in museum quality work for generations.  Aesthetics do not have to be driven by whatever the AAA crowd is doing lately.

I also think it is mildly economically suicidal to chase high end rendering features that only big budget studios can support with with their big art teams.  What that threshold is or isn't, is up to people to decide.  But a $0 open source engine probably better consider what indies want in the real world, rather than trying to be a Unity replacement.

An indie would like stuff that's *easy to use* and that *scales*.  So that I can start *now* on basic game capability, and worry about fancy rendering *later*.

I also want to blow my CPU budget on AI, not graphics so much.

-------------------------

Modanung | 2019-09-07 11:06:37 UTC | #36

8 posts were split to a new topic: [Emergent Impostors](/t/emergent-impostors/5555)

-------------------------

slapin | 2019-09-06 20:38:01 UTC | #41

I think uniform shader language would be nice addition to engine too.

-------------------------

maryahmgrace | 2019-09-08 11:19:26 UTC | #42

i don't know if i'm "asking too much", but something like a gui editor + SDK for 2d with mesh deformation, spritesheet and bones using generic c++ (like esoteric spine, godot and animeeffects to make 2d into a 3d like, will be nice) in license MIT

(animeeffects that is the only just for this and free is GPL 3 and QT :()

http://animeeffects.org/en/

https://github.com/hidefuku/AnimeEffects

https://www.youtube.com/watch?v=CrBCbaorOv0

-------------------------

Bluemoon | 2019-09-21 09:04:25 UTC | #43

Well, not really what I'll want to see in the core but more of what might be beneficial if looked into and that is mobile game development. If more attention can be focused on the fact that Urho3D can be a game changer in mobile game development that would be nice.

It can be a go to for indie 3d mobile game developers

(*Pardon me, I've been away for a while I just hope I'm not missing out somethings*)

-------------------------

Modanung | 2019-09-21 09:24:03 UTC | #44

[quote="maryahmgrace, post:42, topic:5453"]
animeeffects that is the only just for this and free is GPL 3 and QT :(
[/quote]
What's the problem with that?

Welcome to the forums, btw! :confetti_ball: :slightly_smiling_face:

[quote="Bluemoon, post:43, topic:5453"]
( *Pardon me, I’ve been away for a while I just hope I’m not missing out somethings* )
[/quote]

@Bluemoon welcome back! :confetti_ball: :smiley:

-------------------------

marialnmgrace | 2019-09-21 11:18:00 UTC | #45

thank you for the welcome :slight_smile:, GPL and MIT, implement animeeffects or '.ani' sdk directly doesn't break the license?

-------------------------

Modanung | 2019-09-21 11:30:21 UTC | #46

Well, the animation editor would not have to be included to support the *format*. Which means only the license of (librararies related to) the latter would matter.

-------------------------

marialnmgrace | 2019-09-21 12:16:10 UTC | #47

* oh * this is interesting, so using for learning purposes, is it possible to turn some code or GPL file into another license with certain modifications? even with SIMILAR PARTS? :open_mouth:

-------------------------

Modanung | 2019-09-21 13:22:02 UTC | #48

It would be allowed to create a library *inspired* by existing ones under a different license. But not to simply copy and relicense someone else's work.
Although it can be hard to draw a line sometimes. For instance code from answers that are posted here or on Stack Exchange _technically_ defaults to being "all rights reserved", I think. But I'm no lawyer.

AnimeEffects currently does not seem to have a separate library as such. Tiled, for instance, is licensed GPL, but the TMX format is CC-BY-SA.

-------------------------

