DeathArrow | 2017-01-02 00:57:55 UTC | #1

I opened the NinjaSNowWar scene in the editor. However I don't see the objects in the scene in FillSolid mode, just an ugly interrupted grid. How can I setup the scene to properly see objects in it?
It is possible to run a scene from the editor? 
Reading the wiki I see nodes can have components like in Unity. A script is also a component? It is possible to modify some variables in a script from within the editor?
Is there a script reference with class list and function list?

Where can I find some tutorials and more examples?

-------------------------

weitjong | 2017-01-02 00:57:56 UTC | #2

Welcome to our forum.

You need to read the documentation hosted in GitHub pages instead of GoogleCode wiki (which contains outdated documentation). The latest documentation can be found in Urho3D website ([urho3d.github.io/](http://urho3d.github.io/) - the URL is also available at the forum footer below). 

[quote]I opened the NinjaSNowWar scene in the editor. However I don't see the objects in the scene in FillSolid mode, just an ugly interrupted grid. How can I setup the scene to properly see objects in it?[/quote]
You are not supposed to do that with NinjaSnowWar.xml scene because it is really only describing an "empty" scene. To get you started quickly, I think you are better of first running 11_Physics or 13_Ragdolls sample apps, pressing F7 to save the scene, exiting sample app, launching again Editor app, loading back the newly saved scene XML file in the editor. From there you can use the attribute inspector to inspect all the attributes of the selected node or component, then modify their attribute values, adding new node/component or deleting existing node/component to see what it does. You can build the samples apps by specifiying -DENABLE_SAMPLES=1 when you invoke cmake_xxx.bat or .sh.

[ul]
[li][b]It is possible to run a scene from the editor?[/b]
Yes, you can run or pause the scene in a limited sense in editor but don't expect it to be like Unity just yet[/li]
[li][b]A script is also a component? It is possible to modify some variables in a script from within the editor?[/b]
Yes, more precisely it is the ScriptInstance component. You can modify its attributes in the editor just like any other components.[/li]
[li][b]Is there a script reference with class list and function list?[/b]
Yes, we have two scripting subsystems: AngelScript (more mature) and Lua (newly added); and both scripting APIs are listed in the main page of the documentation.[/li][/ul]

[quote]Where can I find some tutorials and more examples?[/quote]
We already have over 20 examples in each language (C++, Lua, AngelScript). How much more do you need ? :slight_smile:
But I do agree with you that Urho3D still lacks of guides and tutorials. We need people to start contributing back to fill up our new Wiki page at GitHub, which is currently totally empty.

HTH

-------------------------

Mike | 2017-01-02 00:57:56 UTC | #3

[quote]Urho3D still lacks of guides and tutorials. We need people to start contributing back to fill up our new Wiki page at GitHub, which is currently totally empty.[/quote]

What kind of tutorial would you like to see? Maybe we could set somewhere a todo list of useful tutorials to get started.

-------------------------

weitjong | 2017-01-02 00:57:57 UTC | #4

This is just my two cents.

For coding tutorial, I think a step-by-step from basic to advance topics similar to NeHe will be kind of cool. As Urho3D is not just rendering engine but a game engine, so of course we have to adjust the topics to be more relevant for game building than to follow NeHe topics closely.

For artist/asset tutorial, I think a series of HowTos that describes exporting and importing from one modeling software to Urho3D editor would be a godsend. A series of tutorials on how to use various techniques and materials to construct a render path to achieve the desired effect from basic forward rendering to advanced deffered rendering with post processing, if that is not too much to ask.  :smiley:

-------------------------

Mike | 2017-01-02 00:57:57 UTC | #5

I'll start with asset import/export for Blender, as it's one of the most basic tasks for beginners.

-------------------------

DeathArrow | 2017-01-02 00:58:01 UTC | #6

I'm thinking about:

- creating a basic GUI, maybe a video tutorial or a tutorial with screenshots to show how the editor is used?

- creating a very simple 2d game detailing steps made in the editor

- creating a very simple 3d scene detailing steps made in editor

Personally I think that using the code is easy to understand, what I'd like to see is how to design e level in the editor.

I would like some tutorials like these (made for Unity) :

Breakout: [youtube.com/watch?v=kNJJql-_ ... 89256228A0](http://www.youtube.com/watch?v=kNJJql-_-YA&list=PL8F195F89256228A0) (level design and code)
3d Level: [youtube.com/watch?v=mbm9lPB5GPw](http://www.youtube.com/watch?v=mbm9lPB5GPw)
3D Level: [youtube.com/watch?v=xQoTGXTn25M](http://www.youtube.com/watch?v=xQoTGXTn25M)
Gui: [youtube.com/watch?v=5tcmtz1- ... HNhsjeNtpk](http://www.youtube.com/watch?v=5tcmtz1-Po8&list=PLXeP8_0UWlD7uHI8CJsTHsZHNhsjeNtpk)

-------------------------

jmiller | 2017-01-02 00:58:13 UTC | #7

Thanks to [b]reattiva[/b] for continuing work on the Blender export script (your name should be in the script credits!). For some reason, I have had no luck with AssetImporter and current Blender.

I have a quick question. #Urho3D on freenode IRC is not too busy... [b]yet[/b] :wink:

Local node > Local node > Light
Light appears in editor, but not at render time. Reproducible in NinjaSnowWar.
Checking debug stats, it seems the light was removed or never added.

-------------------------

cadaver | 2017-01-02 00:58:14 UTC | #8

That could be a bug; you should post an issue into the github tracker with detailed steps on how to reproduce.

If you mean that adding a light into the NinjaSnowWar scene in the editor, saving the scene, then running the game doesn't show the light, I couldn't reproduce that outright (the light showed up fine)

-------------------------

jmiller | 2017-01-02 00:58:15 UTC | #9

Correction: not reproducible in NinjaSnowWar - I just did not notice the light the first time :slight_smile:
Thanks for verifying this cadaver.

Edit: It seems the light was not appearing when I added a [b]ScriptInstance[/b] component to the same node (disabled or subnode or not), while I can create it in pure script...

-------------------------

gasp | 2017-01-02 00:58:22 UTC | #10

hello, my questions seem to be in the sam scope of the original threads, so it seem a good idea for me to regroup tutorial idea in the same thread.

I woul like some tutorial for :

 1?)  make a cube not from importing a model mdl, but from draw geometry, i've see the drawgeometry class, mamybe a minimalistic sample can be cool for more complex idea
 2?)  Rorating a cube around another cube
 3?)  playing with coordonate x,y,z for helping ppl representing how the world is make
 4?) a pick drag & drop a model, pick a model with you''r mouse who follow you'r mouse a drop it in another place (in a fixed you + 20z per exemple)

Building a development platform :
5?) a noob tutorial for configuring a dev env independant of the platform from download the IDE to compile a hello World for windows / mac / linux if possible
6?) i see a tutorial for using angel script with AS, CodeLite seem to be a good IDE, how can we be able to build Urho3D from here ?

 what is the prefered platform , windows, mac or linux ?

what is the most common an suffisiant environement, how i see it  :
a?) build Uhro3D from source in the projet, full liberty but need cmake / VS to be able to compile and i don't really see debugging how it is 
b?)build Uhro3D from source in the OS to build a library (platform dependant, a project can't be build in another os), full acces to C++ / Uhro3d feature
c?) use Uhro3dPLayer.exe with AS, most simple, can't use c++, only what is exposed by in the AS API

b?) seem to be the most preferable if you don't intend to hack into Uhro3D source, you juste need to be able to build from source / download last library to be up to date
a?) is too complex for me if i want to start in linux, i can build with cmake, dev with litecode / codeblock with a library
 can cmake build a projet for litecode/codeblock like he do for VS ? or it's too complicated ?


sorry for the long post.

-------------------------

jmiller | 2017-01-02 00:58:29 UTC | #11

hello gasp,
I just have some quick notes, a bit tired..
and anyone please correct where I'm wrong.

Urho3D has strong platform independence, so maybe that's more a matter of preference?
I found the docs and Sample scripts instructive. Code completion in CodeLite is useful, as text-searching docs+Samples.
Personally, I had no trouble building with gcc or MSVC, was there anything in particular?

Getting the source? Personally I like the bleeding edge repository.  :sunglasses: Options are Git and Subversion.
Urho doesn't require a command prompt / shell AFAIK. It kinda goes with the territory but if it helps some Windows users:
[stackoverflow.com/questions/6090 ... c-location](http://stackoverflow.com/questions/60904/how-can-i-open-a-cmd-window-in-a-specific-location)
using Git: git clone [github.com/urho3d/Urho3D.git](https://github.com/urho3d/Urho3D.git) (to update, 'git pull' in the directory)
or using Subversion: svn co [github.com/urho3d/Urho3D.git/trunk](https://github.com/urho3d/Urho3D.git/trunk) Urho3D  (to update, 'svn up')
There are choices made in CMake so you might be returning to that (options described in the docs).

5 and 6 re. IDEs/building:
CodeLite and CodeBlocks IDEs can install MinGW (g++, Make, other tools) for you.

C++/AngelScript/Lua? depends on your requirements..

Script:
The engine exposes a lot of functionality, you can build complete applications, shared or static..
Scripts execute fast.. The messages and log file are informative.
It's easy to prototype and may not be hard to migrate to C++ later.

Urho3DPlayer has a lot of useful options and can pass your own to your script (see docs and NinjaSnowWar).

C/++: interfaces may be needed for integrating native libraries or performance critical stuff.
Debugging: Depends on environment - some people find MSVC easier than using MinGW/gdb with the Windows IDEs.

-------------------------

gasp | 2017-01-02 00:58:29 UTC | #12

thanks you for you'r reply, i discover more and more, i've already accomplish somes task on the list, somes on the way.

I really love Urho3d, sometimes i feel to be too "noob" to ask question, yes exemple are really inscructive

-------------------------

