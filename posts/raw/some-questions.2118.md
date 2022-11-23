aldoz | 2017-01-02 01:13:14 UTC | #1

Hi guys,
I tried AGK2 and CopperCube but both can't handle projected shadows and for me a 3D game MUST have projected shadows.
So I found Urho3D today and I really impressed by some demos; wow! 

I have some basic questions :

1) Is There an IDE (like dark basic / AGK) or there is an interface like CopperCube ?

2) Can I get dynamic projected shadows?

3) Where is the command list?

4) Can I use Urho3D from my PC windows10 to program a game for android (apk)? 

5) Can I use heightmaps?

6) how I can start to program something? I get a folder with a lot of cmake files.. what is that?

Thank you in advance!

-------------------------

Sir_Nate | 2017-01-02 01:13:14 UTC | #2

1) Not really. There are some AngelScript IDEs out there, naturally there are a lot of things that support Lua, and C++ has Visual Studio, Eclipse CDT, Codeblocks, etc. But there isn't really anything specific to Urho besides the Editor, which is mostly just for scene construction. The Editor is, I suppose, kind of like CopperCube, but programming is a heavy focus of Urho (e.g. I almost never use the editor except to view the scene heirarchy of a saved scene from my game), while CopperCube from the brief look I gave it seems to hide that from the user.
2) Assuming I know what you mean, yes. Like what's in sample 18?
3) Not sure what you mean. API is here: [url]http://urho3d.github.io/documentation/HEAD/[/url]
4) You should be able to. I'm pretty sure I got it working before, but I've switched to just working in Linux, which I find to be much more programmer friendly.
5) Yes, though I don't know if support is official yet (it looks like it is): [url]http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_terrain.html[/url] (Also, Google "urho3d heightmaps" for some additional information
6) Build the library (that's what all the cmake scripts are for). There are directions for that in another link in the documentation, but if you've done that, then you want [url]http://urho3d.github.io/documentation/1.5/_using_library.html[/url].
6b) Alternatively, you could use Lua/AngelScript for your whole game (I would not advise that), but in that case you would just run it from the Urho3DPlayer.

-------------------------

codingmonkey | 2017-01-02 01:13:14 UTC | #3

[quote]how I can start to program something? I get a folder with a lot of cmake files.. what is that?
[/quote]
my old example
[video]https://www.youtube.com/watch?v=yImFcDZ61Lk[/video]

-------------------------

aldoz | 2017-01-02 01:13:14 UTC | #4

wow seems I am in a very different world than DarkBasicPRO/AGK world!

@Sir Nate:
Thank you so mutch for your answers, at least I realized that I was understanding NOTHING about Urho3D.
There are a lot of conceptual differences.. too time programming with a single IDE and now I need to face lula, angels and a lot of new things to handle.

@codingmonkey:
Thank you for the example!


I avoid to shot another questions before to take a good look to the tutorials!
For now THANK YOU guys! (and sorry for my weird english..)

-------------------------

Dave82 | 2017-01-02 01:13:15 UTC | #5

[quote="aldoz"]I avoid to shot another questions before to take a good look to the tutorials!
For now THANK YOU guys! (and sorry for my weird english..)[/quote]

If you used procedural languages before (DBpro ,  AGK , etc) I highly recommend to learn c++ and Object orinted programming first before you start with Urho3d. There are lots of stuff that are really hard to learn if you don't have a strong fundamental knowledge of  OOP , C++ and CMake. I'm not talking about buying expensive books with 864246512 pages but running through some basic c++ tutorials wouldn't hurt.

[url]http://www.cplusplus.com/doc/tutorial/[/url]

Practice a lot ! Build some pointless apps using the STL (Nothing fancy , just some basic sorting , simple text andveture games using the console, etc).
Study the structure of other libraries , and try to understand the core of OOP.

As for CMake : Urho3d builds beautifully without any additonal fiddling and error tracing in make files , so just use the CMake GUI (the method condingmonkey posted ) it should work out of box.If you using windows , it's even easier to just 
1 build urho3d using CMake GUI
2. Setup include paths , library paths in Visual Studio ( Something like Urho3D/Include and Urho3D/lib/) and thats it.
3. include Urho3d.h in you project and start coding.
4. Additionally include the required headers for your need (eg Urho3D/Physics/RigidBody.h or Urho3D/Audio/Sound.h , etc)

-------------------------

aldoz | 2017-01-02 01:13:15 UTC | #6

thanx Dave82!
I am studing about :slight_smile:

-------------------------

