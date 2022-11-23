Serge | 2017-01-02 00:59:34 UTC | #1

Hello everyone!

Editor eat 100% CPU, is it ok? How to avoid that?

PS Ubuntu 14.04, Blender 2.71

-------------------------

jorbuedo | 2017-01-02 00:59:34 UTC | #2

I think it's normal.

-------------------------

Serge | 2017-01-02 00:59:34 UTC | #3

[quote="jorbuedo"]I think it's normal.[/quote]

Disagree... Blender working with 3d model too and does not use CPU on 100%. It should be option something like maxCpu or something.

-------------------------

jorbuedo | 2017-01-02 00:59:35 UTC | #4

I don't think it's ok, because it could use less. But I think it's normal, because not only happens to you.

I was just clarifying that it's not just you. Try to modify the code and limit it.

-------------------------

Serge | 2017-01-02 00:59:35 UTC | #5

[quote="jorbuedo"]I don't think it's ok, because it could use less. But I think it's normal, because not only happens to you.

I was just clarifying that it's not just you. Try to modify the code and limit it.[/quote]

Thank you for your answer. Will know that I'm not along :slight_smile: About modifying code - I'm noobie in C++ but will try.

-------------------------

jorbuedo | 2017-01-02 00:59:35 UTC | #6

The code is in AngelScript, it's a bit easier.

-------------------------

Serge | 2017-01-02 00:59:35 UTC | #7

Thank you for answer, can you give me advice how to do it? And why not to make it default?

-------------------------

lexx | 2017-01-02 00:59:35 UTC | #8

As it uses Urho3DPlayer, check its parameters how it works. 
Ie, enable vsync is  -v (add it in Editor.sh), maybe it helps?

-------------------------

Serge | 2017-01-02 00:59:35 UTC | #9

[quote="lexx"]As it uses Urho3DPlayer, check its parameters how it works. 
Ie, enable vsync is  -v (add it in Editor.sh), maybe it helps?[/quote]

Just tried - no effect :frowning: 100% CPU used.
In Engine.cpp, in constructor, I set  SetMaxInactiveFps(10) and SetMaxFps(60), recompile library and now  Urho3DPlayer eat 95% CPU. Not much. If engine will be so hungry it will eat battery on IOS and Android and users will not play in my game :frowning: What else I can do? Any ideas?

-------------------------

friesencr | 2017-01-02 00:59:36 UTC | #10

Urho has a hierarchtical cpu profiler.  See what is eating the cpu.  The samples bind it to F2

GetSubsystem<DebugHud>()->ToggleAll();

-------------------------

Serge | 2017-01-02 00:59:36 UTC | #11

Please open this image in new tab.
[spoiler][img]https://lh6.googleusercontent.com/-s-t0Jo8NXrg/U6qpBBeQqxI/AAAAAAAAALM/VbjIneFDbbQ/w1078-h839-no/Untitled.png[/img][/spoiler]

[code]
Engine::Engine(Context* context) :
    Object(context),
    timeStep_(0.0f),
    timeStepSmoothing_(2),
    minFps_(10),
    #if defined(ANDROID) || defined(IOS) || defined(RASPI)
    maxFps_(60),
    maxInactiveFps_(10),
    pauseMinimized_(true),
    #else
    maxFps_(30),
    maxInactiveFps_(10),
    pauseMinimized_(false),
    #endif
#ifdef URHO3D_TESTING
    timeOut_(0),
#endif
    autoExit_(true),
    initialized_(false),
    exiting_(false),
    headless_(false),
    audioPaused_(false)
[/code]


maxFps_(30) but as you can see it completely ignored by the Urho library :frowning:

-------------------------

cadaver | 2017-01-02 00:59:36 UTC | #12

Check the following line in the editor script (Editor.as line 193); it will override the maxFps setting set earlier during Engine's construction.

[code]
if (renderingElem.HasAttribute("framelimiter")) engine.maxFps = renderingElem.GetBool("framelimiter") ? 200 : 0;
[/code]
You can naturally change those values if you want. 

Regarding mobiles, if you don't need 60fps screen update, you should be able to set lower maxFps for lower power consumption. Depending on the graphics drivers & API used, using vsync may not reduce CPU usage, as it may be busy-polling for the vertical sync.

Also, the reason why something like Blender and Urho's editor can't be compared CPU usage-wise is that the Urho editor is running a constant screen redraw (just like a game), while GUI applications that use the native OS windowing (like Blender) typically redraw only when the user does something.

-------------------------

