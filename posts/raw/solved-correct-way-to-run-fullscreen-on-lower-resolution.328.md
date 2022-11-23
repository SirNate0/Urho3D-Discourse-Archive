gunnar.kriik | 2017-01-02 00:59:39 UTC | #1

Hi,

I'm attempting to run my application full-screen while forcing a lower resolution then the current screen resolution (force a video mode change). I cannot seem to make this work properly. I can see from Source/Engine/Graphics/OpenGL/OGLGraphics.cpp that SDL_CreateWindow() is invoked with the SDL_WINDOW_FULLSCREEN flags, which should force a video mode change according to the docs, but I seem to get some weird behaviour regarding the resolution used. On Linux the app runs full screen, but the video mode is not changed - always runs at 1920x1080, which is the default desktop resolution. That might be an issue with my xorg config, but on windows the video mode is changed, but the resolution I specify does not seem to be respected - this is how the engine parameters are specified.

[code]
engineParameters_["FullScreen"]   = true;
engineParameters_["Headless"]     = false;
engineParameters_["WindowWidth"] = 1600;
engineParameters_["WindowHeight"]  = 900;
[/code]

The following results in vertical letterboxing, similar to the example in the middle here:
[img]http://e2e.ti.com/resized-image.ashx/__size/550x0/__key/CommunityServer-Discussions-Components-Files/100/8737.LetterBoxing_5F00_UseCases.png[/img]

It seems that when on full screen, then the incorrect resolution is used (looks to be 4:3 instead of 16:9 as specified). The correct resolution is however used when in windowed mode (fullscreen=false).

Has anybody else experienced this issue, and / or have any advice before I debug the code further?

Thanks

-------------------------

cadaver | 2017-01-02 00:59:41 UTC | #2

There are many ways this can work not as expected.

To my knowledge the current Linux SDL code does not switch resolutions in fullscreen; it always uses the desktop resolution. 

Urho queries SDL (which in turn queries the operating system) for the available fullscreen resolutions, and it will pick the closest match if the exact resolution is not supported. On Windows, if you pick a resolution which you know that the GPU & monitor will support, it should switch resolution correctly.

Furthermore, in GPU driver options you can usually choose whether it will actually switch resolution or perform stretching (to something that's suboptimal for the monitor), or perform letterboxing. Urho cannot influence this.

However: I think there's a bug in scanning for available fullscreen resolutions, as it's not giving those resolutions that don't fit the aspect ratio exactly. I'll look into this.

-------------------------

cadaver | 2017-01-02 00:59:41 UTC | #3

There was an error in the "resolution error metric" calculation which would cause eg. resolution 1366x768 to be used, though 1024x768 was requested. If you check the latest master branch revision, that part should work better now.

-------------------------

gunnar.kriik | 2017-01-02 00:59:41 UTC | #4

[quote="cadaver"]There was an error in the "resolution error metric" calculation which would cause eg. resolution 1366x768 to be used, though 1024x768 was requested. If you check the latest master branch revision, that part should work better now.[/quote]

Thanks Lasse - on Windows the behaviour is now as expected (fullscreen and video mode change working), however on Linux the app runs fullscreen, but SDL never changes the video mode. I tested a simple GLFW based app aswell, and I'm having the same problem here, so I suspect that it's an issue with my xorg configuration. I'll figure it out. Thanks!

-------------------------

