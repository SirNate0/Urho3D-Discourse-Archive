Eugene | 2022-11-15 20:19:30 UTC | #1

I have been playing around with Urho3D and engine development for years.
While I have never released any "big" games, I am still trying to make one.
"rbfx" is a meme name of Urho3D fork I personally use when doing anything game/engine-related.

rbfx has reached the point when I can declare an "intermediate release": the core idea is implemented and the framework is usable. However, rbfx does not have a stable release yet, so there are bugs, there are missing features, and there would be breaking changes.

![image|690x374](upload://nuTcTjZO0NkZOxKuP5k6OeCV4fA.jpeg)

https://cdn.discordapp.com/attachments/1011222168958418954/1042120445912158248/Animation12.gif

## Links

Discord server with all relevant discussion: https://discord.gg/XKs73yf

GitHub page: https://github.com/rbfx/rbfx

WIP Documentation: https://rbfx.github.io/
Documentation contains a bit more of project philosophy, check it out if you care.

Sample project: https://github.com/rbfx/sample-project

Sample project on itch[dot]io: https://eugeneko.itch.io/sample-project

## So, why this project exists?

- I really like some aspects of original Urho engine and I want to keep them: wide platform support, relatively simple but customizable API, compact engine size.

- I wanted to change other aspects of Urho engine, and it was not possible without excessive backward compatibility breakage. [That thread](https://discourse.urho3d.io/t/to-rbfx-and-not-to-rbfx/5864) few years ago clearly showed me that Urho community didn't want this kind of changes.

- The goal is to replace outdated or misdesigned parts of Urho with reasonable effort and without too much feature bloat, and to reduce iteration times for project development.

- While original Urho offers only "engine" itself, rbfx attempts to consider entire development pipeline: from assets to publishing.

## What are the changes?

Well... there are quite a lot of them, and I am too lazy to list them all. Let's talk about big ones.

- **Lua and AS are removed.** Which is a deal-breaker for some, but it was necessary to speed up engine development and make big changes.

- First-class Editor application in C++:

  - Multiple tabs and windows;
  - Flexible architecture;
  - Game can be played in Editor "almost as-is";
  - Automatic asset importing;
  - DPI-aware;

- **AssImp is removed.** Instead, glTF standard is supported. There are a couple of minor quirks due to engine architecture, but almost all standard glTF are 100% correctly imported, and the rest is imported with minor differences. Blend and FBX formats are also partially supported via extensions.

- Renderer overhaul:

  - Unified shaders for DX and OpenGL;
  - Shaders are almost completely rewritten;
  - **XML Render Paths and postprocessing are removed**. Replacement on C++ side is WIP.
  - Physically-based rendering (actually working and correctly-looking);
  - Spherical harmonics for ambient lighting;
  - Light mapper and light probe baker;
  - Reflection probes with blending;
  - Compute shaders;
  - Graph-based particle system;
- XML permutation hell is removed, we only need a dozen Techniques now;

- Networking rewrite:

  - **Scene replication from Urho is removed** due to its clumsiness.
  - New networking requires more manual work, but it is *much* more flexible, reliable and has lower connection requirements.

- Tweaks and changes too numerous to list:

  - A lot of bugs in renderer and animation are fixed ([like this one](https://discourse.urho3d.io/t/data-races-in-octree-update-and-view-updategeometries/3913));
  - Universal animation system. AnimationController can animate everything, not just bones.
  - Microphone support;

- Some Urho parts are replaced with 3rdParty libraries.

  - EASTL for containers, fmt for string profiling, spdlog for logging, etc...
  - UI is replaced with Dear ImGUI (for Editor and tools) and with RmlUI (for in-game UI, still WIP)

- Experimental C# bindings are out there...

  - ... but I don't have a clue about its state, not using it.

## Plans for the future

- VR/XR support;

- Vulkan/Metal/DX12 support via middleware. Diligent? TheForge?

- Improved Inverse Kinematics;

- Polishing RmlUI integration, more samples;

- Replace Bullet Physics. PhysX? Jolt?

- Add scripting in some form. Lua? JS? Something else? Discussion is open.

- Polishing renderer. Custom postprocessing. Custom render pipelines w/o forking. Better SSAO? SSR? Terrain? Foliage?

- Improving asset and publishing pipeline. Docker images?

- Actually do some games :laughing: 

## Conclusion

I create this topic mostly to showcase this project, to gather feedback, and to post updates. Discussion is welcome, but I recommend to use Discord or GitHub for long technical discussions.

PS: Shout out to @rku, @glebedev and @JSandusky, who contributed a lot to this project! Also, ping me if I missed anything important in this post.

-------------------------

1vanK | 2022-11-15 19:53:49 UTC | #2

I would like more information about why some part of the engine has been or will be rewritten. For example, why is Bullet worse than PhysX? Why XML Render Paths and postprocessing are removed? Why inconvenient, but very powerful UI was replaced by ugly Dear ImGUI?

-------------------------

faesong | 2022-11-15 20:05:44 UTC | #3

UI was not replaced, it's still there, ImGUI is added as a secondary (and/or as a debug/developer addon). Only problem with it is that it's not vanilla ImGUI, but some patched version of some specific branch of it... About Bullet and Render paths I don't know tho...

Overall I like rbfx for the fact it's a bit quicker to set up for quick experimental development. Needs a lot of polishing for it to be marketable maybe... There's not much documentation, I think it's assumed that the user of the engine will just jump over the code and figure out things by jumping through the code in IDE and debugging tools (good thing there are samples, it's never enough samples for nubes like me heh). That makes a lot of sense on a bleeding-edge kind of development I guess...

Hopefully it keeps going, as I have a small pet-project going with it :smiling_face:

-------------------------

glebedev | 2022-11-15 20:15:24 UTC | #4

Render path been lost during refactoring. @Eugene just didn't have time to rewrite everything at once.

-------------------------

glebedev | 2022-11-15 20:16:15 UTC | #5

Render paths may come back in a different form. I would like to do it via visual scripting but it isn't ready too :-)

-------------------------

Eugene | 2022-11-15 20:17:35 UTC | #6

[quote="1vanK, post:2, topic:7351"]
For example, why is Bullet worse than PhysX?
[/quote]
My only real problem with Bullet is no Kinematic Character Controller (let's pretend that `btKinematicCharacterController` does not exist, it's waaay too bad and unstable).

Also, some users observed weird instability in some cases which I was unable to debug. I am not sure if it's Bullet issue or Urho3D issue. But I have *a bit* more trust in tested commerical physical engine like PhysX. Bullet may be better for science, I don't know, but not for games.

[quote="1vanK, post:2, topic:7351"]
Why inconvenient, but very powerful UI was replaced by ugly Dear ImGUI?
[/quote]
Because I needed iteration speed *much* more than I needed beauty. Dear ImGUI allows me to write UI *fast*. I can make a button or a textbox or a checkbox in *one* line of code. It took me a couple of hours to make resource browser or scene hierarchy. I made Editor from scratch in a couple of months because of these quick iterations. Urho UI would have been maybe 5-10 times slower, and I don't have infinite time unforutnatelly.

[quote="1vanK, post:2, topic:7351"]
Why XML Render Paths and postprocessing are removed?
[/quote]
It was a byproduct of renderer rewrite, and I just didn't care enough to bring them back. XML render paths are very limited by its nature. For example, if you launch PBR sample in Urho with autoexposure, you will notice a flash. It is a very simple bug in autoexposure effect, but it's impossible to fix without extending XML syntax. Also, XMLs create permutation hell: you need an XML for each combination of options.

-------------------------

1vanK | 2022-11-15 20:33:50 UTC | #7

[quote="Eugene, post:6, topic:7351"]
My only real problem with Bullet is no Kinematic Character Controller (let’s pretend that `btKinematicCharacterController` does not exist, it’s waaay too bad and unstable).
[/quote]

In order to create a kinematic character controller, sweep test is required and nothing more. For good example of KCC you can look OpenMW. It is not problem of the physics engine.

-------------------------

1vanK | 2022-11-15 20:37:43 UTC | #8

[quote="Eugene, post:6, topic:7351"]
But I have *a bit* more trust in tested commerical physical engine like PhysX.
[/quote]

Erwin Coumans (author of Bullet) also is  physx developer

-------------------------

Eugene | 2022-11-15 20:55:23 UTC | #9

[quote="1vanK, post:7, topic:7351"]
In order to create a kinematic character controller, sweep test is required and nothing more.
[/quote]
If you take a look at PhysX (or even Bullet) kinematic controller, you will see that it's quite complicated.

Even walking itself is challenging: penetration recovery heuristics and shit. Bullet does it poorly. Put two walls at unlucky angle, and walk into the corner: controller will be twitching in the corner instead of standing still.

Then we have object riding and object pushing... Bullet doesn't even try.

[quote="1vanK, post:7, topic:7351"]
It is not problem of the physics engine.
[/quote]
It is *my* problem. I want decent controller. PhysX has one, Bullet does not. Also, yes, I tried porting controller from PhysX to Bullet, I gave up after reading its code.

-------------------------

1vanK | 2022-11-15 21:05:10 UTC | #10

[quote="Eugene, post:9, topic:7351"]
Even walking itself is challenging: penetration recovery heuristics and shit. Bullet does it poorly. Put two walls at unlucky angle, and walk into the corner: controller will be twitching in the corner instead of standing still.

Then we have object riding and object pushing… Bullet doesn’t even try.
[/quote]

I studied both and even wrote my own. The same algorithm is used everywhere. In any case, you need to understand this algorithm in order to write the controller for a specific game.

For  example Unity uses PhysX and have no object riding, object pushing, wall running, climbing and a thousand other things

-------------------------

1vanK | 2022-11-15 21:43:55 UTC | #11

[quote="Eugene, post:9, topic:7351"]
Even walking itself is challenging: penetration recovery heuristics and shit. Bullet does it poorly.
[/quote]

When sweep test, any physics engine doesn't do anything like that at all. The idea is that physics is totally disabled for KCC. You analyze the surrounding space using sweep tests and change position of the character manually.

-------------------------

1vanK | 2022-11-15 21:31:22 UTC | #12

Some refs: <https://github.com/1vanK/Urho3DCharacterController>

-------------------------

hunkalloc | 2022-11-16 05:03:50 UTC | #13

For FPS, yes. 

For platformers, this one works well: https://github.com/Lumak/Urho3D-KinematicCharacterController

-------------------------

hunkalloc | 2022-11-16 05:04:37 UTC | #14

This one is Quake-inspired: https://github.com/hdunderscore/Urho3D-FPS-Controller/blob/master/Source/Character.cpp

-------------------------

rku | 2022-11-16 07:23:25 UTC | #15

[quote="faesong, post:3, topic:7351"]
Only problem with it is that it’s not vanilla ImGUI, but some patched version of some specific branch of it…
[/quote]

Why is that a problem? Patches are not essential actually. One big out-of-tree patch is HDPI support. It sucks, but it does allow us to support HDPI in some capacity. It is not necessary for editor to function. Then there is reordering API which can totally be added to rbfx itself and does not need to be in imgui core. And some fixes to make things build.. If we deemed it necessary we could make it work with vanilla imgui with minimal effort.

-------------------------

faesong | 2022-11-16 09:40:40 UTC | #17

[quote="rku, post:15, topic:7351"]
[quote="faesong, post:3, topic:7351"]
Only problem with it is that it’s not vanilla ImGUI, but some patched version of some specific branch of it…
[/quote]

Why is that a problem? ...... (truncated quote)
[/quote]

In my case it unfolded into a problem probably because of my own stupidity... :slight_smile: 

I used some code to reload fonts (different ranges of the same font) on the fly, and in some version it broke. First I went to check ImGui release notes and see if they broke anything, and found nothing... Then I began to look through git commits and couldn't understand what was exact version of **ImGui** that **rbfx** uses... So I ended up bisecting the problem through git until I found exact commit but I still have no idea what is the problem :see_no_evil:

*Only at that point I asked about it all on discord, and @rku  actually told he can look into it but I asked him not to waste time, it's not critical to me hehe*

(UPD commit that broke things is https://github.com/rbfx/rbfx/commit/7660ef7f433151286148ac5eea61956bceb12946#diff-de1e7dd1dd8b441b64d5bc421293b7d3b08f1530d4aeb30878bbdda53b1d24e8 )

-------------------------

rku | 2022-11-16 09:58:06 UTC | #18

would be a good idea to post all relevant info on our issue tracker (including what broke exactly)

-------------------------

faesong | 2022-11-16 10:03:54 UTC | #19

Right! Will do soon :+1:

-------------------------

JSandusky | 2022-11-19 23:30:53 UTC | #20

I've posted a dump of the OpenXR/SteamVR Urho3D stuff https://github.com/JSandusky/UrhoXR_Dump. VR folder is the important part really, I think someone could magick the rest into existence really once they get the gist that it's doubling instancing and view-constants). It isn't up to date with the RBFX XR (this is where it started, then I ported over to RBFX so it'd be there), but I'll merge the updates backwards over relatively soon and push those commits along with GL support.

I'm wayyy to far diverged from Urho3D/master to even consider doing a PR to master. But if someone really wants some XR but doesn't want to rip their hair out, here be a code dump and you do whatever you do. Warning though: I was much less pedantic about not cludging stuff together in Urho compared to RBFX porting, expect some slop.

-------------------------

JTippetts1 | 2022-11-20 01:40:34 UTC | #21

I've been using rbfx for awhile now. Have ported most of my games, my (dormant) terrain editor and an industrial simulation project for work. It's pretty nice.

One area I disagree with the rbfx devs is in the decision to deprecate the vanilla UI. I know it's a little broken in some ways, but I have experimented with the RmlUI solution and while I have gotten used to its ways and means, I have run into some knotty performance problems that I lack the brains to really sort out. The UI in one of my games is heavy on displaying pages of numbers run through a big-number text formatter, and so the constant rebuilding causes a large performance hit that I have been unable to resolve. Vanilla UI is much better in that regard, it just lacks in the area of inline text coloration and formatting. RmlUI seems to do better with less text-heavy "button and icon" type UIs.

UI quibbles aside, rbfx is a pretty strong successor to Urho3D. Now that Urho3D seems to be in its sunset days, you can't really go wrong switching to rbfx.

-------------------------

1vanK | 2022-11-21 00:26:01 UTC | #22

[quote="JTippetts1, post:21, topic:7351"]
I’ve been using rbfx for awhile now. Have ported most of my games, my (dormant) terrain editor and an industrial simulation project for work. It’s pretty nice.
[/quote]

I still think you don't really like rbfx

<https://github.com/urho3d/Urho3D/commits?author=JTippetts>

<https://github.com/rbfx/rbfx/commits?author=JTippetts>

I mean, if rbfx is so nice, then you probably would take a minute to at least fix some typo there or something like that. Although perhaps the engine is already ideal.

-------------------------

1vanK | 2022-11-21 00:28:12 UTC | #23

[quote="JTippetts1, post:21, topic:7351"]
Now that Urho3D seems to be in its sunset days, you can’t really go wrong switching to rbfx.
[/quote]

The main thing is not to forget to report it so that everyone knows, otherwise no one will even notice it.

-------------------------

JTippetts1 | 2022-11-21 02:51:58 UTC | #24

I'm not an engine dev, though. I'm one of those dirty users you so thoroughly loathe and have indicated are not welcome here. Honestly, at this point you should just take Urho private because other devs aren't working on it anymore, and you don't want users. Just take it private so you can pleasure yourself in peace and privacy.

-------------------------

hunkalloc | 2022-11-21 04:01:07 UTC | #25

not sure where the drama here comes from. it's odd. but anyways:

I find rbfx to be a good breath of fresh air. there are very wild and different ideas, such as removing all scripting, but that allows the devs to move faster. and that is good, one day it will stabilize and then things can be added to it. it is a way forward. maybe what urho needs are more and more forks.

hoping for more terrain work, like triplanar texturing, splatting, blending, etc. tools for indies, so we can also iterate faster with the engine and do less repetitive work and focus on game code

-------------------------

1vanK | 2022-11-21 08:16:47 UTC | #26

[quote="JTippetts1, post:24, topic:7351, full:true"]
I’m not an engine dev, though. I’m one of those dirty users you so thoroughly loathe and have indicated are not welcome here. Honestly, at this point you should just take Urho private because other devs aren’t working on it anymore, and you don’t want users. Just take it private so you can pleasure yourself in peace and privacy.
[/quote]

No engine needs such users. Following your logic, its need to close all engines. You help a engine with money in the case of a commercial engine, or with time in the case of a non-commercial one. Otherwise, your personal use of the engine is of no interest to anyone.

[quote="hunkalloc, post:25, topic:7351"]
there are very wild and different ideas, such as removing all scripting, but that allows the devs to move faster. and that is good, one day it will stabilize and then things can be added to it. it is a way forward. maybe what urho needs are more and more forks.
[/quote]

In Urho3D, bindings are generated in a fully automatic mode and do not restrict the devs in any way. You don't even need to remember them. If there are problems with bindings, they have a separate maintainer.

-------------------------

hunkalloc | 2022-11-21 10:53:06 UTC | #27

is there a roadmap for Urho3D?

-------------------------

1vanK | 2022-11-21 11:42:28 UTC | #28

Why this question? When you become a developer, you can make yourself a list of tasks, publish it and you will be rewarded with a couple of likes for it. There are too many idlers who like to organize other people's work.

-------------------------

JTippetts1 | 2022-11-21 14:40:58 UTC | #30

If you fork it, I'd recommend reverting a lot of commits. 1vanK's been crapping up the commit history with a lot of pointless and unnecessary churn. Probably a few regressions in there.

-------------------------

1vanK | 2022-11-21 14:54:17 UTC | #32

You been crapping up the forum history with a lot of pointless and unnecessary churn.

-------------------------

1vanK | 2022-11-21 15:46:45 UTC | #34



-------------------------

