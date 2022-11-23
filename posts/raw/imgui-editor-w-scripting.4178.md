Sinoid | 2018-04-16 04:07:47 UTC | #1

Fairly close to complete ImGui based editor with several points of extension via Angelscript.

Windows x64 binaries only, just drop into your `bin` directory. Tabbed scene/prefab editor, material editor, particle effect editor, and model viewer + tweaker.

Major things:
- Most important editor functionality is there
- OS thumbnails and embeds thumbnails into Scene and Node prefab files (based on active viewport)
- *Favorites* and *Recent* folder groups in asset browser
    - Asset browser is generally a first-class citizen
        - play sounds, run scripts as one-offs, run scripts as editor actions on the current scene, drag-drop, etc
- Configurable *rig* scenes for Material/Particle/Model scenes
- Scripts can:
    - Add additional docking windows
    - Add menu items, commands, windows, etc
        - Example for Bulk Renaming nodes
    - Extend or overwrite the property page's handling of any Urho3D::Object derived type
        - Example for attaching "Build NavMesh" button to the property page of NavigationMesh and DynamicNavigationMesh
    - See readme for a full list of all of the events available for scripts to subscribe to and the API for registering things ... slap a crapload of buttons on top of the 3d viewport if you want

Only major stuff missing is the renderpath setup, spawner, picking modes, and terrain tools - mostly trivial stuff. Multiple viewports are actually already there but hidden away ATM.

Unfortunately there's no shortcuts / accelerators ATM, still working out what to do there that won't suck.

https://github.com/JSandusky/Blocks

![image|690x373](upload://pmmjEnLBbwne9qiRpl8cOf0RrJR.jpg)

-------------------------

Miegamicis | 2018-04-16 05:43:16 UTC | #2

Nice! This looks like something that I would like to test out.
Is there a functionality to support node switching between local and replicated? I know someone from the forums already did that for the old editor.

-------------------------

Sinoid | 2018-04-16 07:47:11 UTC | #3

[quote="Miegamicis, post:2, topic:4178"]
Is there a functionality to support node switching between local and replicated? I know someone from the forums already did that for the old editor.
[/quote]

Added that (as well as temporary/permanent conversion), only available through the context menu n the scene tree.

-------------------------

rku | 2018-04-16 09:09:51 UTC | #4

Is this closed-source?

-------------------------

Sinoid | 2018-04-16 11:44:09 UTC | #5

[quote="rku, post:4, topic:4178, full:true"]
Is this closed-source?
[/quote]

Uses the ImGuiElement and bindings I posted before: https://discourse.urho3d.io/t/dear-imgui-w-o-steamrolling/3960.

But as a whole, for the time being yeah. That's a debate I haven't had with myself yet, a *locked repo* or *tarball* I'll probably do for the "*can't use with my engine customizations"* case, as there's a lot of stuff that I'm outright not even remotely open to comment on or what not.

-------------------------

rku | 2018-04-16 14:13:02 UTC | #6

I am curious, what is the reasoning behind keeping it closed but sharing binaries for free?

-------------------------

Sinoid | 2018-04-16 16:37:19 UTC | #7

[quote="rku, post:6, topic:4178, full:true"]
I am curious, what is the reasoning behind keeping it closed but sharing binaries for free?
[/quote]

1) Doubt the community is large enough for any incentivized development
2) OSS'ing would have no actual benefit on it itself (just end-users with customized engine code)
   - Any PR's for anything other than script extensions would almost certainly be useless and out of touch (unless someone's psychic and can divine my direction)
3) Closes off a lot of stuff I'd like to port over or do
    - Engine stuff that would realistically never get into master, like multiple windows
    - Inevitably the other operating systems pop up and have to be put down
    - There's some stuff that I would never ever OSS
    - Added hassle of now adding a DLL based extension point, but yes, most things can be worked around
        - Or a hassle in code management, having to *cook* to deploy the OSS version and juggle it
4) Lots of work to strip out or make sane before I could even do such
    - Have to rip out a bunch of #def'd out CoreCLR stuff, etc
5) Incomplete codebase, it's a waste of time for anyone to be looking at it at the current pace.
   - More than half of that WIP/TODO list will be finished by the end of the week

-------------------------

rku | 2018-04-16 16:53:16 UTC | #8

Well that is unfortunate. I maintain my soft fork for very same reasons you outlined. I always advocate sharing code if there is no serious reason not to. In your case there really isnt. If you want this to be your personal project and you do not want to deal with accepting contributions and what not - you can still work on a public repository while clearly stating that contributions will not be accepted. At least someone would be able to learn from your work and that is moving a world to a positive direction a tiny bit. We both are working on very similar things. At least i would find it useful. The way it is now this is more a show-off project saying "look what i have", not "look what you could use". ¯\\\_(ツ)_/¯

-------------------------

elix22 | 2018-04-16 21:33:14 UTC | #9

Just my 2 cents.
I am playing with game engines for the last  20 years as an hobby , probably to compensate for the accumulated frustration created due to my daytime job (writing some code for mobile devices internals).   
I was always fascinated of the inner-workings of game engines ,even ported some of them to various platforms as P.O.C. at my spare time.
Never made money out of it and didn't plan to make any (however made large amounts of money at my day job :slight_smile: ).

I noticed of numerous (not so successful) attempts of individuals trying to create an Game Editor for Urho3D in the past.
The question I asked myself was what is the end goal ?
If the answer was to learn about the internals of the game engine , than it make sense , I can relate to that.
However if the end goal was to make a fully featured functional Game Editor , I believe it can't be done by a single individual in a reasonable amount of time .
The things I saw you all do in the past just amazes me every time .  
If you will all share knowledge , join forces and will combine your amazing talent you will accomplish a lot more and maybe you will stand a chance in creating a fully functional developer friendly Game Editor.
Sorry for the long comment :slight_smile:

-------------------------

Sinoid | 2018-04-17 23:03:03 UTC | #10

> The question I asked myself was what is the end goal ?

Phasing out my usage of WPF is my main goal. Urho3D editing is just a sideshow because it's a complete cake-walk to do and provides enough proof-testing scenarios that I can be sure of robustness in the code generation from XAML step.

> If you will all share knowledge , join forces

Already tried to get people to help years ago on an ATF based editor. I ended up just finishing it on my own and it's been my main editor for my STL / no-nonsense fork. Kept the last early public version up sitting: https://github.com/JSandusky/UrShell

My QT stuff was never meant for Urho3D, editing of Urho3D files was also just a side-show since it was a tool using Urho3D for the rendering, which was then moved to MonoGame and WPF then sold off.

Also, no. Not happening. There's at best 2-weeks of work on my entire to-do list, help is pointless.

-------------------------

elix22 | 2018-04-18 06:52:25 UTC | #11

Last comment , and will stop nagging you :slight_smile:

ATF is supported only on Windows (I don't understand the Sony guys).
Would not be my first choice  of framework developing tools for cross-platform game engine. 
Might be the reason that others didn't help you .

QT (and wxWidgets ) will not play well with SDL on Mac OS  , so it won't work for Urho3d on Mac OS.
QT and wxWidgets are using  NSView  as their main objects as opposed to SDL which is using NSWindow .

I found some branch that tries to fix this issue , not sure it will work for Urho3D.
https://github.com/flowercodec/sdl2

Anyway those of you that plan to try integrate Urho3D with Qt/wxWidgets   on Mac (might be also Linux), prepare for sleepless nights.

-------------------------

rku | 2018-04-20 18:03:51 UTC | #12

@Sinoid it seems to me like you are looking for excuses to not share your work. This is perfectly fine but maybe this thread should be in showcase section then.

Also are your reasons are mute. It is very easy to work on own thing and share it all: https://discourse.urho3d.io/t/net-bindings-for-urho3d/4119 . Lets be honest with ourselves - neither you nor me will get rich from this stuff, so why not at least score in some bonus karma points ;)

Aaaand now i stop nagging you as well :white_flag:

-------------------------

Sinoid | 2018-04-21 04:15:29 UTC | #13

> it seems to me like you are looking for excuses to not share your work ... Also are your reasons are mute.

They're not mute. The XAML pipeline is sublicensed. I don't have authority to redistribute the code that does all of the code generation. There's fewer than 2k lines of hand-written code and another 4k of XAML, an additional 22k entirely generated as a result of cooking down the XAML. 

Thus I'd have to cook all of that and rewrite to OSS - unless you like reading `a_->NotifyPropertyChanged(hashes_InternalCtrlID[432], hashes_InternalSrcID[SRC_HASH(a_->GetID())]);` for several thousand lines.

For instance on the *There’s some stuff that I would never ever OSS*:
- Radial-edge mesh editor
    - Sublicensed, I have authority to use, not to relicense - I sold that right
- XAML (full databinding implementation, with all of the expression refolding wildness)
    - that's sublicensed again
- UV recharter
    - Thekla and DX-UVAtlas are both awful, I'm not OSS'ing a not-awful mapper that copes with non-manifolds
- OpenCL rasterizer
    - So not worth the work of trying to port over DX12's raytracing to replace
- Lightmapper
    - Not OSS'ing, done it before - it was far more hassle than it was worth

You're also going to make me say it. I don't want it appearing in any external forks or seeing Linux/Mac support, period. It would **never ever** be OSS, if source is ever made available it'll be under a license that puts it squarely under my thumb.

> It is very easy to work on own thing and share it all

[That's](https://discourse.urho3d.io/t/geom-shader-branch/4012) my contribution for the semester, take it or leave it.

Edit: But like I've reiterated over and over and over and over, I'll consider it but now is not the time. All of the points above, I can address - but I cannot wave a wand and dump it on github. That's a few additional weeks of work and hunting for a license that gives me distribution control authority without denying modification for internal non-distributed use (aside from just a tacit *"I say it's okay so long as you don't distribute"*).

-------------------------

