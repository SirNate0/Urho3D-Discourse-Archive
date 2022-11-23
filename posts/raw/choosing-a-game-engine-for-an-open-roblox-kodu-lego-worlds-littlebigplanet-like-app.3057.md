DuncanCragg | 2017-04-27 01:10:19 UTC | #1

Hi everyone!

I'm looking for a game engine that's suitable for an Open Source app that I want to write and share on GitHub. I'm evaluating Godot, Atomic, Urho3D, Blender and OpenSceneGraph. I'm hoping some of you here can help me determine if this engine is a candidate :-) I'm not 'hawking' my game idea, and sincerely hope this is the right sub-forum!

My idea for the app is "building and programming your own games - without technical skills" - along the lines of [Roblox](https://www.roblox.com/), [Kodu](https://www.kodugamelab.com/), [Lego Worlds](https://www.lego.com/en-gb/worlds/), [LittleBigPlanet](http://littlebigplanet.playstation.com/), [Struckd](https://struckd.com/), [Blockland](https://en.wikipedia.org/wiki/Blockland_%28video_game%29) (apparently defunct), [Project Spark](https://en.wikipedia.org/wiki/Project_Spark) (defunct).

It will have a simple rule programming language to bring things to life. Aside from the app being Open Source, this language is the main differentiator to these other approaches. It isn't text-based, it appears as simple 2D grids expressing rules, that are similar to spreadsheet formulae, and that react to scene object state changes.

The game engine should thus ideally make the following elements nice and easy:

 - 2D interface panels...
 - with scrollable selectors, grids holding text items, buttons
 - to choose and configure renderable game objects into scenes
 - to enter and edit the animation rules for those objects
 - that either pop up over the live scenes or appear inside them

The last point in the list above is because the rule editor, rule runner and game loop won't be started and stopped, they will run continuously, even as rules are being updated.

 - API access to the states of scene objects, to read and write their properties and be notified of events
 - persistence of scene structures and their rules to a database or files
 - access to threads and the event loop to give my stuff plenty of CPU
 - easy API access and C/C++ code extension
 - building to Android and other common platforms

I would strongly prefer to write the rule runner in C, rather than C++. I've implemented similar systems in every language known to man, including these three, but C feels like the right low-level language to implement another very high-level language in. This is partly because of speed and resource usage, but also because C is very portable, so I'd find it easy to port the language to any other hardware or OS, including embedded systems, etc. Having said that, I'm open to strong arguments in favour of C++.

So my question is, can Urho3D easily support the bullet points above? :-D

Duncan

-------------------------

DuncanCragg | 2017-04-28 21:42:44 UTC | #2

Well, after some more research and engaging with their active community, it looks like **Godot** is the best game engine of my list.

Cheers!
Duncan

-------------------------

