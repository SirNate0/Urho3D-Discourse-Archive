GodMan | 2019-05-01 01:46:26 UTC | #1

My urho3d application starts making the GPU fan real high after running for a few minutes. So I am looking for some ways to improve performance. Maybe see what other users have done.

I'm using d3d9 on windows 7.

Here are some basic engine parameters I have changed.

	engineParameters_["WindowResizable"] = true;
	engineParameters_["FullScreen"] = true;
	engineParameters_["FrameLimiter"] = true;
	engineParameters_["WorkerThreads"] = true;
	engineParameters_["LowQualityShadows"] = true;
	engineParameters_["VSync"] = true;

Thanks

-------------------------

Leith | 2019-05-01 05:47:10 UTC | #3

I believe the issue may be due to WindowResizable.
This flag implies that the window titlebar is accessible for minimizing, maximizing and resizing the application window... which implies that we're not really running in full screen mode.

Under Windows, applications can either run in true "exclusive" fullscreen mode (titlebar hidden, desktop is not being drawn) or in false fullscreen mode (window of application is maximized to size of screen, titlebar may or may not be hidden, but desktop is still being drawn).

VSync is the main one for performance - and you have it enabled.. usually we leave it enabled, it creates a cap on frames per second that matches your video hardware - if we turn it off, we can get massive FPS, just to taste how well our code is really running - then we turn it on again.

Tell me more about your machine specifications :slight_smile: Maybe we can find some ways to squeeze more performance.

-------------------------

Pencheff | 2019-05-01 11:45:11 UTC | #4

Enable debug HUD and watch the values, the cause of bad performance will be easy to find.
[code]
    // Get default style
    ResourceCache* cache = GetSubsystem<ResourceCache>();
    XMLFile* xmlFile = cache->GetResource<XMLFile>("UI/DefaultStyle.xml");
    // Create debug HUD.
    DebugHud* debugHud = engine_->CreateDebugHud();
    debugHud->SetDefaultStyle(xmlFile);
    debugHud->ToggleAll();
[/code]

-------------------------

GodMan | 2019-05-01 18:06:06 UTC | #5

If I remove windowresizable, and leave fullscreen equals true the application no longer goes fullscreen.

-------------------------

GodMan | 2019-05-01 18:37:59 UTC | #6

Okay after reading the docs I believe I fixed it. I moved my engine parameters into void setup() before start, and everything seems to be working.

-------------------------

GodMan | 2019-05-02 16:35:28 UTC | #7

On the GPU fan issue. In the debug text my RenderQuad is going from 1650 - 1800. I am using the HDR PostProcessing effect. This has the highest value in the debug text.

-------------------------

