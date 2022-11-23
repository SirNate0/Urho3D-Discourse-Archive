lexx | 2017-01-02 00:58:53 UTC | #1

This engine is just great and it have almost everything (sometime later will need realtime SSAO and parallax mapping). 

What are you guys doing with it?  I'm (still) coding 2d+3d adventure game.

-------------------------

cadaver | 2017-01-02 00:58:54 UTC | #2

I might use the engine in a virtual world client (day job stuff), however this is yet unconfirmed. Otherwise I've not used the engine outside of the examples. It's a bit of a risky path, to code an engine with no target game in mind, but a large part of the development today is anyway motivated by user requests & issues.

-------------------------

szamq | 2017-01-02 00:58:54 UTC | #3

I'm making 3D adventure game, with physics puzzles and bit of creepy factor on Urho3D with AngelScript. The project is in very early state and not yet announced, but I hope I release it next year. Will create project thread in Showcase section as soon as there will be something to show and the details of the game plot will be arranged. Here's screenshot of what I'm working now 
[drive.google.com/file/d/0B-FH5c ... sp=sharing](https://drive.google.com/file/d/0B-FH5cooowQpVkRlSHBIZnBpX1U/edit?usp=sharing)
@lexx I agree, also for me SSAO and Parallax mapping are the most wanted features, SSAO because I don't like to bother with lightmaps, Parallax mapping for cool looking walls etc :smiley: But overall Urho3D is great engine, I use it with pleasure.

-------------------------

gasp | 2017-01-02 00:58:54 UTC | #4

i'm learning for now, i've do a basic tic tac toe, now i'm trying to do a more complex project, trying to use the engine to adapt a physic board game, i'm far from it for now so no picture

-------------------------

Canardian | 2017-01-02 00:58:54 UTC | #5

I'm making a OOP BASIC language translator and simplistic IDE, which translates to C/C++ and uses Urho3D as its main lib. If no translation is possible, it will leave the code how it is, so that it works also with C/C++ code directly.
The goal is to provide an as simple as possible language, which can be used for teaching kids and casual computer users to learn programming with powerful graphics, audio and other features which Urho3D provides.
I will use it myself also for business and games programming, to minimize development complexity and time.

-------------------------

cadaver | 2017-01-02 01:00:21 UTC | #6

The  project I talked about in April is now proceeding as open source. 

Basically, a virtual world client/server SDK currently using Qt & Ogre [github.com/realXtend/tundra-urho3d](https://github.com/realXtend/tundra-urho3d) . This will naturally not immediately supersede the older version, as it's much more feature-complete and used in real world use cases (also commercial). Rather, we'll see how the new version develops, and I also get to see Urho more from the viewpoint of an external developer :slight_smile:

-------------------------

gunnar.kriik | 2017-01-02 01:00:21 UTC | #7

That's really awesome - nice to see how you would use Urho3D as an "external developer"! Much to learn from here, I'm sure.

Just curious - what were you using Qt for in the Ogre implementation? I'm guessing 2D / Webkit integration?

Keep up the good work!

-------------------------

cadaver | 2017-01-02 01:00:21 UTC | #8

Qt is used for the signal/slot mechanism, http networking functionality, and for two very major features: scripting (QtScript, deprecated in newer versions of Qt), and input/UI. These latter two features are also the reason for endless cursing about lost / subpar performance :slight_smile: The UI works by software-rendering into a window-sized canvas, which Ogre then uploads to a texture and shows as an overlay.

-------------------------

gunnar.kriik | 2017-01-02 01:00:21 UTC | #9

OK, I see. So I take it you are going without Qt for the Urho3D implementation. Anyhow, neat to see how the project evolves. Is it somewhat similar to Second Life?

WRT offscreen rendering - I've been playing with the Chromium Embedded Framework lately. It's pretty neat - you can render Chromium / Blink into an offscreen buffer and upload it as a texture to the GPU. Currently in the progress of starting a demo using Urho3D. What CEF does differently from Qt is that it does rendering and scripting in separate processes, so the "main" process is mosly unaffected by that, however I have not done any benchmarking on using it as an overlay over heavy 3D scenes yet. It is however a very simple way to create 2D views, as you can use most of the latest HTML5, CSS3 and Javascript as you would for regular webpages. Pretty cool, but it is a HUGE third party dependency. HUGE.

-------------------------

cadaver | 2017-01-02 01:00:21 UTC | #10

The realXtend project started long ago (2007) using the Second Life client and Opensim server, so it's definitely inspired by those. But by the time it morphed into the Tundra SDK, its mission turned to be as application-agnostic as possible, meaning that you can build a typical VW with avatars, but you're not forced to, as the UI & user interaction are all defined by the scene/application you connect to. On the downside, it doesn't support huge worlds spanning servers (yet), rather you always connect to a single server at a time.

About CEF: yes, the GPU upload itself shouldn't be a huge performance hit, not more than an animated/procedural texture. Agreed that it's huge though (40MB just for the DLL) :slight_smile:

-------------------------

thebluefish | 2017-01-02 01:00:22 UTC | #11

I've been spending the past month and a half making a multiplayer Animal Crossing style game. It's still fairly basic and my graphics guy has been too busy to help out, but it's definitely coming along nicely. While most of the game is pure C++, I am making certain things extendable via Angelscript such as items, NPCs, etc... My ultimate goal is to have a modding system similar to Minecraft to allow people to customize their own servers while still retaining the base game.

-------------------------

gunnar.kriik | 2017-01-02 01:00:22 UTC | #12

[quote]I've been spending the past month and a half making a multiplayer Animal Crossing style game[/quote]

That's cool! Aiming for mobile or PC (or both)?

-------------------------

thebluefish | 2017-01-02 01:00:23 UTC | #13

[quote="gunnar.kriik"]That's cool! Aiming for mobile or PC (or both)?[/quote]

What I hope to achieve is to be able to play on the same server seamlessly between mobile and PC. So that a player could login to the same character (or 2 different characters) regardless of their platform of choice. Urho3D also makes it easy to transfer packages from server to client, so that custom content can propagate on both without forcing people to update the mobile client.

ATM my Android device doesn't want to work with my PC, something about drivers. I really don't want to mess with mobile ports for now, I still have nightmares about getting everything talking together, then I reformatted!

-------------------------

JTippetts | 2017-01-02 01:00:27 UTC | #14

I've been working on a turn-based, hex-based RPG called Goblinson Crusoe. I sometimes write about it in my [url=http://www.gamedev.net/blog/33-why-you-crying/]dev journal.[/url] Some (slightly older) screens:

[url]http://i.imgur.com/OzhAThQ.jpg[/url]

[url]http://i.imgur.com/Wmdhejn.png[/url]

[url]http://i.imgur.com/B7MRr6L.jpg[/url]

-------------------------

jonnenauha | 2017-01-02 01:00:28 UTC | #15

Hello all,

Quick intro: First post here. I work with Cadaver on realXtend and other stuff on my day job here in Finland. Personally very exited about tundra-urho3d and the potential it has.

[quote="gunnar.kriik"]OK, I see. So I take it you are going without Qt for the Urho3D implementation. Anyhow, neat to see how the project evolves. Is it somewhat similar to Second Life?

WRT offscreen rendering - I've been playing with the Chromium Embedded Framework lately. It's pretty neat - you can render Chromium / Blink into an offscreen buffer and upload it as a texture to the GPU. Currently in the progress of starting a demo using Urho3D. What CEF does differently from Qt is that it does rendering and scripting in separate processes, so the "main" process is mosly unaffected by that, however I have not done any benchmarking on using it as an overlay over heavy 3D scenes yet. It is however a very simple way to create 2D views, as you can use most of the latest HTML5, CSS3 and Javascript as you would for regular webpages. Pretty cool, but it is a HUGE third party dependency. HUGE.[/quote]

I assume you are using CEF3 if you have separate rendering etc. process. I've implemented a CEF1 based renderer myself for Meshmoon Rocket (a realXtend Tundra based client/server distro we work on at Meshmoon). We are working with the current tech with Qt and Ogre. The initial problem was that QtWebkit was crashing our main app as it was running in the same thread. CEF (basically the Chrome browser) is pretty stable but I didn't want to make that mistake again.

So I made a little process that our client starts up per rendered web page. They talk together via simple binary TPC protocol I cooked up. They share a common memory block so that both processes can read and write to it, for stuff like this Qt is pretty helpful framework. Easy to use API and good documentation, I used QSharedMemory for the mem and Qt networking stuff for the TCP client and server (and writing the binary messages). You can do stuff like resize, load url and route  full set of mouse and keyboard events to the process. In return the CEF process sends over rects that have been updated in the shared memory region texture and the main process updates the region to the Ogre texture. The result is live rendering a web page onto any submesh in the world and you can interact with mouse/keyboard in 3D. You can run youtube videos and all that stuff with good framerate. As a bonus of course this spends very little CPU in the Tundra processes main loop. CEFs rendering is nice as you hardly ever do full rect copies but a bunch of little ones where actual changes happened. QtWebkit it might have been possible to dig this info, probably if overloading the paint events or embedding into QGraphicsScene, but we didnt even try as 4.8.x QtWebKit is slow and buggy anyway :I

I'm in the process on porting this thing to CEF3 so we would get a bit more up to date chrome and get the multi process architecture. Currently a bit stuck porting the keyboard code as the API has changed quite a bit. Rendering and loading pages already work with minimal porting effort.

As said Qt is great for generic programming in a GUI app, but it has some pretty bad overhead too in certain places. It's not very suited for game engines at all, but your run of the mill GUi apps I would pick it any day of the week. Unfortunately we were too deep into embedding Qt everywhere once this was realized, and the fact that it made some non perf critical parts very easy to program, that there was no going back without a ~full rewrite of the Tundra core. Luckily the funding game through and we got Cadaver working on it now!

P.S. Would have included links to Meshmoon and Qt docs but apparently I cant post links on my first post. I guess makes sense so you cant make account to just post adverts and stuff :slight_smile: Google them if interested.

-------------------------

gunnar.kriik | 2017-01-02 01:00:29 UTC | #16

[quote="jonnenauha"]
I assume you are using CEF3 if you have separate rendering etc. process. I've implemented a CEF1 based renderer myself for Meshmoon Rocket (a realXtend Tundra based client/server distro we work on at Meshmoon). We are working with the current tech with Qt and Ogre. The initial problem was that QtWebkit was crashing our main app as it was running in the same thread. CEF (basically the Chrome browser) is pretty stable but I didn't want to make that mistake again.
[/quote]

Hey, welcome to the forums, awesome to hear from you! Yes - I have been experimenting with CEF3, as there has been quite a bit of changes there lately, such as they switched to Aura instead of GTK on Linux (windows had that already), and CEF3 now uses the new software compositor code path to render offscreen ( [code.google.com/p/chromiumembed ... il?id=1257](https://code.google.com/p/chromiumembedded/issues/detail?id=1257) ). 

The rendering and scripting is done in separate processes, so the "main" thread (game thread) is not held back - or crashed if the rendering or scripting goes bad. However, there is the issue of transferring the pixel buffer to GPU on the main thread, which may or may not be noticable (I am currently unsure of how the buffer is transferred from the rendering process to the main process, and how many memcpy-s are involved here). Probably not many, but needs investigating. They have an issue in the tracker for sharing a GL/D3D texture/surface between the processes, but this is still in the works ( [code.google.com/p/chromiumembed ... il?id=1006](https://code.google.com/p/chromiumembedded/issues/detail?id=1006) ). This would be super awesome.

[quote="jonnenauha"]
So I made a little process that our client starts up per rendered web page. They talk together via simple binary TPC protocol I cooked up. They share a common memory block so that both processes can read and write to it, for stuff like this Qt is pretty helpful framework. Easy to use API and good documentation, I used QSharedMemory for the mem and Qt networking stuff for the TCP client and server (and writing the binary messages). You can do stuff like resize, load url and route  full set of mouse and keyboard events to the process. In return the CEF process sends over rects that have been updated in the shared memory region texture and the main process updates the region to the Ogre texture. The result is live rendering a web page onto any submesh in the world and you can interact with mouse/keyboard in 3D. You can run youtube videos and all that stuff with good framerate. As a bonus of course this spends very little CPU in the Tundra processes main loop. 
[/quote]

That's a really interesting approach! Did you have this running on all desktop platforms (Win, Lin, OSX), or was this Windows only? Very clever indeed... 

[quote="jonnenauha"]
CEFs rendering is nice as you hardly ever do full rect copies but a bunch of little ones where actual changes happened. QtWebkit it might have been possible to dig this info, probably if overloading the paint events or embedding into QGraphicsScene, but we didnt even try as 4.8.x QtWebKit is slow and buggy anyway :I
[/quote]

They had the dirty-rect pattern in the old offscreen rendering codepath, but now you get the full frame each time in the OnPaint() callback. See: [code.google.com/p/chromiumembed ... il?id=1257](https://code.google.com/p/chromiumembedded/issues/detail?id=1257)

[quote="jonnenauha"]
I'm in the process on porting this thing to CEF3 so we would get a bit more up to date chrome and get the multi process architecture. Currently a bit stuck porting the keyboard code as the API has changed quite a bit. Rendering and loading pages already work with minimal porting effort.
[/quote]

You do get an up to date HTML5/CSS3 renderer, which IMO is super productive and awesome. You get all the Responsive Web stuff for your UI and whatnot.

[quote="jonnenauha"]
P.S. Would have included links to Meshmoon and Qt docs but apparently I cant post links on my first post. I guess makes sense so you cant make account to just post adverts and stuff :slight_smile: Google them if interested.
[/quote]

Awesome - thanks, will check it out!

-------------------------

izackp | 2017-01-02 01:00:30 UTC | #17

Hi All, 

Well, what I'm up to is that I'm trying to refactor this library: [github.com/RuntimeCompiledCPlusPlus](https://github.com/RuntimeCompiledCPlusPlus) into something a bit more readable (I'm not a fan of recursive templates). Then, I plan on integrating it with Urho3d and Urho3d's serialization system. (Or I might fork Urho3d and use protobuf; idk yet). After that, I should be able to recompile my code on the fly as soon as I save. 

Then, once I have that done, I will be working on an IDE, Scene & Class editor.  My goal is to be able to program my game from within my game. I would like to place scene components, play them, and edit them all in the same window :3

I do have greater ideas and aspirations. I want to make my own variation of C++, mostly simplifying the effort it takes to write classes and components. One example is that I don't want to update the header file every time I write a new function. I believe this should be done for me and other things such as unit test generation, getters and setters generation, automatic reference counting, ect. But RuntimeCompiledCPlusPlus is my focus for now.


My overall goal is to have a game engine that takes the least amount of effort to iterate/test your code. I don't want to worry about what platform I'm on, I don't want to worry about project settings, I don't want to have to recompile every small change I make, I want to get straight into game programming and minimize the amount of time between writing code and seeing the changes (reaping the rewards).

-------------------------

OvermindDL1 | 2017-01-02 01:01:18 UTC | #18

For note, QT5 QTQuick Gui renders in a different thread from your context and it pulls in your rendered side through the framebuffer, it is quite fast.  The GUI should always render at a minimum of 30fps though your side can render faster, animations and all.  It fixed a lot of issues of QT4 as long as you are at least dual-core.

-------------------------

