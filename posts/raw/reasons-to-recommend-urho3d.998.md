Signalovernoise | 2017-01-02 01:04:42 UTC | #1

Hey, a bunch of folks at Slant are putting together a comparison of 3D game engines to serve as a comprehensive overview for people looking where to start with game developoment. Here's the work-in-progress comparison: slant.co/topics/1495/~what-are-the-best-3d-game-engines

There's some initial info on Urho3D, but not a lot. Mind helping out?

-------------------------

friesencr | 2017-01-02 01:04:42 UTC | #2

Here are my opinions.

The pluses of the engine are huge and very strongly define the engine.  Urho3d is a full featured, multi platform, near zero bullshit, clean architecture,  fast c++ engine with low platform requirements.

It has a familiar component model.

I would say the engine is API first meaning that you won't see much code in the engine to serve the sole purpose for it's editor. The editor is dependent on the core and not the other way around.  You have to be able to script/code to use Urho3D.




Positives: 

Everything - negatives :smiley:




Maybes:

Something that people might be afraid of is the build process, but the project is open source, multi platform, and c++ and after you account for those circumstances the build is a work of art.  If you ever had to build Ogre3D during its prime you know what I mean.  It can also take a little while to understand its memory model.  It uses ref counting and has it's own personality.  Experienced coders won't stumble too much but lesser experienced tend to stumble a little there.




Negatives:

I don't care for the UI for complex user interfaces.  If you are making a game with it and not tools you will be using 99% sprites so it isn't an issue.  Otherwise it is work to make it look the way you want.

It doesn't have tools for everything.  The asset pipeline could be hard for some people who are used to commercial engines.

-------------------------

GoogleBot42 | 2017-01-02 01:04:43 UTC | #3

One plus that hasn't already been mentioned is that it is in very active development.  Bugs are usually fixed that same day.  So there is a lot of direct communication with the devs.  One disadvantage of a lot of other engines is that there is a bug disconnect between the users of the engine and the core devs.  Plus, new features are constantly being added.  (HTML5, DirectX11, and OpenGL3.1 support were just recently added.)

Also one of the main reasons I use this engine is because it has support built in for standard things that I would expect out of a game engine.  By this I mean that I don't envy the guys who have to waste their time adding support for things such as pathfinding and bullet physics to Irrlicht.  :wink:

EDIT: I just looked at the section of Urho3D... why is the picture black and white?

EDIT2:
Also I read this:
[quote]A selection of samples in AngelScript and C++ are included with the engine.[/quote]

It should read:

[quote]A selection of samples in AngelScript, [b]Lua,[/b] and C++ are included with the engine.[/quote]

Also Urho3D can target HTML5 but it is still experimental...

And Urho3D has [unofficial] Oculus Rift support as well: [url]http://discourse.urho3d.io/t/oculus-rift-support-renderer-and-input/974/1[/url]

EDIT3:

Haha another thing I noticed...
Unread 4 Engine has this for supported languages:
[quote]C++; C#; GLSL; Cg; HLSL[/quote]
Don't you think GLSL and HLSL are kind of cheating? None of the other engines have these listed.
Urho3D and a lot of the other engines support these too... :stuck_out_tongue:

Also UDK doesn't support C++...

-------------------------

Signalovernoise | 2017-01-02 01:04:43 UTC | #4

Thanks for the info guys. Going through it now. :slight_smile:

-------------------------

