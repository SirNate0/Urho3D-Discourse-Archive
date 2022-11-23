LiamM32 | 2017-07-30 00:24:34 UTC | #1

For awhile now, I have been interested in Lips of Suna, which is a game project abandoned by it's original developer (known as "Amuzen" on [the forum](https://forum.freegamedev.net/viewforum.php?f=25&sid=5ef6f3855ca4c639e201cc617f7a6958)).  I first discovered it on FreeGameDev forums in summer 2014, about a month before Amuzen left and never returned.  It has a custom game engine using OGRE for graphics, and scripts are in LuaJIT.  Although I have wanted to develop it further, I have been limited in what I can do due to my very limited coding skills.  Worse; being an abandoned project with a custom game engine, I get very little support.

However, I have recently managed to update the engine to make it work with OGRE 1.10 and Bullet 2.86.1, which I uploaded to [this repository](https://gitlab.com/electric-gecko/lipsofsuna).  The forum has become more active since I started doing this, although I'm still the only person who has been touching the code.

Originally suggested [by a moderator on the forum](https://forum.freegamedev.net/viewtopic.php?f=65&t=7487&p=73576&hilit=+Update+to+support+OGRE#p73576), I would now like to have Lips of Suna remade with Urho3D.  Here are the main reasons:
* The current version has performance issues which would likely be fixed with this.
* The current codebase of Lips of Suna is too messy, making it hard to develop further and scaring off potential contributors. 
* Can't get any support for the Lips of Suna game engine, as it's exclusive to this project and the developer has left.

Scripts can be written in Angelscript.  This should give better performance, as the Lua garbage collector seems to cause big frame-rate drops when it activates.

I have tried to create an Urho3D program, using the tutorials and the HelloGUI sample for reference.  But I haven't figured out how to get it working, as my programming skills are very limited.  I have taken online tutorials for the syntax of C++, but I have never written a main loop before.

It would be very nice if someone else to were to start writing the new game engine.  As I have struggled to do this first part myself, I'll likely have to join-in after this first step is done (or started).

In the current Lips of Suna, the main funtion is in "src/lipsofsuna/main/main.c".  But in Urho3D, doesn't the main function have to be in C++?

A good first milestone would be to replicate the game's main menu.

My vision of what Lips of Suna should become is something in-between version 0.5.0 & 0.8.0 (latest stable version).  I never got to play 0.5.0, only watched a video of it. It was made for an old Ubuntu version pre-12.04, so I couldn't compile it.

-------------------------

Victor | 2017-07-30 00:54:06 UTC | #2

Urho kinda hides the main function. It's defined through a macro. 
https://github.com/urho3d/Urho3D/blob/master/Source/Samples/01_HelloWorld/HelloWorld.cpp#L35

From there you can manage updates through the event system as shown in that example (update event).
https://urho3d.github.io/documentation/1.6/_events.html

I hope that helps you get started, and good luck!

-------------------------

S.L.C | 2017-07-30 09:04:37 UTC | #3

Extending @Victor 's answer, the macro comes from here https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Core/Main.h

-------------------------

LiamM32 | 2017-07-31 02:09:21 UTC | #4

I used the inline refactoring in Netbeans, so now I can somewhat tell what's happening.  Do the member functions of the class that I entered all need to be named a certain way.

I notice that the example on [this page](https://github.com/urho3d/Urho3D/wiki/First-Project) is written very differently from the included Urho3D samples.  No header, just one file.  Is this example outdated?
Just for test purposes, I tried to compile that example in Code::Blocks, but it complains that it could not find _<SDL/SDL_gamecontroller.h>_ which is included from _Urho3D/Input/InputEvents.h_.  I only have the SDL2 version of that header on my system.
EDIT: It appears that Urho comes with SDL_gamecontroller.h, which the samples are linking to.  Maybe I need to recompile Urho to have them installed on my system.

-------------------------

DrAlta | 2017-07-31 09:56:54 UTC | #5

[quote="LiamM32, post:17, topic:3373, full:true"]
@DrAlta So, do you think that you will help out with the engine remake?
You can talk about it on the thread that I linked to.
[/quote]
Sure I'll help but I'm new to c++, I'm a Perl5 man myself.

-------------------------

LiamM32 | 2017-07-31 22:30:08 UTC | #6

So I guess that you haven't started you're own project in Urho yet, have you?
Do you understand Urho and C/C++ enough to write the main file?  Since this is what the rest of the project is built on-top of, it would be nice if there's someone that can do it right.

I'm struggling to get a simple project working.  But remaking the engine for Lips of Suna appears to be too much for me.  Even if I went through the ridiculous amount of effort it would take, I'll probably end-up doing it badly.  That's why I'm hoping that someone else volunteers to do the beginning part, which includes the main file.

-------------------------

DrAlta | 2017-08-05 21:46:57 UTC | #7

[quote="LiamM32, post:6, topic:3396, full:true"]
So I guess that you haven't started you're own project in Urho yet, have you?
[/quote]

No. I haven't done much with Urho other than look at the documentation. But it's the only Open Source game engine that has software rasterized occlusion culling built in I could find. 

[quote="LiamM32, post:6, topic:3396, full:true"]
Do you understand Urho and C/C++ enough to write the main file?
[/quote]

No I don't know how to write a main file for Urho.
  Since this is what the rest of the project is built on-top of, it would be nice if there's someone that can do it right.

[quote="LiamM32, post:6, topic:3396, full:true"]
But remaking the engine for Lips of Suna appears to be too much for me.  Even if I went through the ridiculous amount of effort it would take, I'll probably end-up doing it badly. 
[/quote]

"good decisions come from experience, and experience comes from bad decisions"
Don't expect to get it all right at first, Plan on rewriting it as you learn what you are doing.

-------------------------

johnnycable | 2017-08-06 16:33:07 UTC | #8

Yes, that example is for urho 1.5. Anyway it works ok on 1.6 on my os X; you probably had some library build problem...
I've tried to waf compile etc, but it stops asking for bullet. I did a git clone <address> --recursive, so I was expecting it to download the external libraries too, and compile directly...
?

-------------------------

