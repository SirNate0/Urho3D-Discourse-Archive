LittleGameDev | 2019-10-07 12:18:51 UTC | #1

hi i am new user of Urho3d. I want to ask about Urho 3d editor ![Ed|647x500](upload://gHY5gdE06t9hPPIACYsoP6bfP5p.jpeg) 

Is this editor is just an example? 
Or

 It is full sdk to develop games it is complete tool with terrain editor etc and more. because Urho3d is game engine not a library 
I am confused about it.. thanks in advance

-------------------------

jmiller | 2019-10-07 14:46:58 UTC | #2

Hello and welcome to the forums! :confetti_ball:

Features (and especially limitations) should provide an overview: https://urho3d.github.io/

Your image is the scene and UI editor included with Urho3D.  Some get by with just a text editor. ;)
There are other editors (we try to link to from the wiki); most have forum topics and some are recently active.

-------------------------

LittleGameDev | 2019-10-07 15:03:55 UTC | #3

Thanks for reply. Can i use this UI editor to make a full game without going to make from scratch.

-------------------------

LittleGameDev | 2019-10-07 15:05:20 UTC | #4

Is it like unity 3d editor. or just to show that you can make an editor like that ?

-------------------------

jmiller | 2019-10-07 16:45:31 UTC | #5

That is the official Urho3D editor. It can manage Scene/Node graphs and common Components, import models, and edit Urho UI.. among other things.
Urho3D shares some similarities with Unity, I gather. More info in [docs](https://urho3d.github.io/documentation/HEAD/index.html) Scene Model etc.

There is the canonical Urho3D example game [NinjaSnowWar](https://github.com/urho3d/Urho3D/blob/master/bin/Data/Scripts/NinjaSnowWar.as) and  samples in AngelScript, Lua, C++
 https://github.com/urho3d/Urho3D/tree/master/bin/Data/Scripts/
 https://github.com/urho3d/Urho3D/tree/master/bin/Data/LuaScripts/
 https://github.com/urho3d/Urho3D/tree/master/Source/Samples
Web Samples
  https://urho3d.github.io/samples/

-------------------------

LittleGameDev | 2019-10-07 16:41:35 UTC | #6

Thank you very much. I tried sample you gave above. Thanks.

-------------------------

lezak | 2019-10-07 19:44:54 UTC | #7

[quote="LittleGameDev, post:3, topic:5652"]
Can i use this UI editor to make a full game without going to make from scratch.
[/quote]

No, quickest and easiest way to go would be to use <a href='https://urho3d.github.io/documentation/HEAD/_running.html'>Player application</a> (among others Editor use it), but still You'll have to write some startup logic that will load scenes and ui created in the editor (see all script samples for reference). If You wan't to do something more serious, You'll propably have to dig into <a href='https://urho3d.github.io/documentation/HEAD/_using_library.html'> using Urho3D library.</a>

[quote="LittleGameDev, post:4, topic:5652, full:true"]
Is it like unity 3d editor. or just to show that you can make an editor like that ?
[/quote]
None of these. Editor is not only a sample, as it allows You to create scenes, ui and some resources (materials, paritcles etc.) that can be loaded and used in Your application, so You don't have to create everything in code, but there is no build in scene managment, settings system etc. so You'll have to write them on Your own  and that's the biggest difference when compared to Unity or other popular engines. 
I know that these are personal preferences, but in my opinion this difference is one of the main advanteges of Urho over other engines - it requires a bit more work, but in exchange You get much more flexability, since, in most cases, You're not limited by some pre-designed systems.

-------------------------

