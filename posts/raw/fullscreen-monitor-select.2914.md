Pencheff | 2017-03-17 10:16:47 UTC | #1

Is there a proper way to select the target monitor for device creation when starting in fullscreen ?

-------------------------

Eugene | 2017-03-17 11:05:45 UTC | #2

No, and I think it has to be solved at some point.

-------------------------

TheSHEEEP | 2017-03-17 11:41:56 UTC | #3

Wow, I did not know that.
Multi-monitor setups are becoming more and more common among regular users. Being able to select a monitor should be a top priority.

Sounds to me like the best idea currently would be to not let Urho3D, but something else create the window and point Urho to it as an external window.

-------------------------

Eugene | 2017-03-17 11:44:10 UTC | #4

Would it work for native fullscreen? Probably no.

-------------------------

Pencheff | 2017-03-17 11:54:17 UTC | #5

My application (currently migrating from Ogre3D) must be able to work in fullscreen/borderless fullscreen window on a selected monitor. Kind of a trivial task, but the Graphics subsystem currently does not use any monitor related parameters. 

I currently use a utility wrapper over SDL_video functions for display enumeration, something like this:
[code]
// Get number of currently present monitors
int GetMonitorCount();

// Get current desktop resolution
Resolution GetDesktopResolution(int monitor);

// Get a list of supported fullscreen resolutions
ResolutionVector GetFullscreenResolutions(int monitor);

// Get closest supported fullscreen resolution
Resolution GetClosestFullscreenResolution(int monitor, Resolution resolution);
[/code]

It would be nice if the Graphics subsystem can export such methods in Application::Setup() (after SDL video is initialized) so users can choose correct settings. 

I guess I can involve in development :)

-------------------------

cadaver | 2017-03-17 12:22:22 UTC | #6

Not sure if SDL knows how to switch to fullscreen properly for the second monitor. I managed to get a borderless window on the second monitor by just positioning it appropriately. PR or development is welcome.

-------------------------

Pencheff | 2017-03-17 12:34:31 UTC | #7

In the graphics subsystem:

[code]
bool Graphics::SetMode(int width, int height, bool fullscreen, bool borderless, bool resizable, bool highDPI, bool vsync,
    bool tripleBuffer, int multiSample)
{
....
[/code]

IMHO this function should provide at least two more parameters - monitor and refreshrate.
In Application::Setup(), user should be able to call:
[code]
Resolution resolution = GetDesktopResolution(1);
parameters["Monitor"] = 1;
parameters["WindowWidth"] = resolution.width;
parameters["WindowHeight"] = resolution.height;
parameters["Refreshrate"] = resolution.refreshrate;
parameters["Fullscreen"] = 1;
[/code]

Having convenient methods I mentioned in the above post when initializing the application would be a big plus.
Refresh rate (with vsync = on) is also something that I rely on, my application displays video content which does massive tearing when no vsync is present. I imagine that would also help with 144Hz monitors

-------------------------

Pencheff | 2017-03-17 20:03:33 UTC | #8

https://github.com/PredatorMF/Urho3D/commit/07b9675dfdd15d5d432d1b8eaae019aa40318213

Currently works on DX9 in both fullscreen and borderless modes.

-------------------------

Pencheff | 2017-03-17 22:10:40 UTC | #9

I've done patches for DX11 and OpenGL, tested on my dualmonitor machine, works just fine.
Silly question: at the end of the Graphics::SetMode() there's a code that sends an E_SCREENMODE event, should I add monitor and refresh rate there ?
Also, imagine a scenario where the engine is initializing, the user could have a dialog with graphics options to choose from, such as supported desktop resolutions, monitors - possibly with monitor names, etc.
Where is the appropriate place to place a couple of static functions (implemented with SDL and requiring SDL_Video to be initialized) for convenience such as GetMonitorCount(), GetDesktopResolution(int monitor), etc ?

-------------------------

Pencheff | 2017-03-18 11:02:10 UTC | #10

Ok, nevermind my silly questions...
https://github.com/PredatorMF/Urho3D/commit/2bef979152f456edb51f60bb614f7375de8158de

-------------------------

Pencheff | 2019-03-25 17:20:40 UTC | #11

I encountered a problem with Graphics::SetMode() and DirectX9 recently, so I made couple of changes today. I've added an example 54_GraphicsMode sample app. It shows a dialog with basic display mode settings like this:
![graphics-settings|641x500](upload://8GGcoKvmpLf49pMNnWzqn0mNBWZ.png) 

Here's the code:
https://github.com/PredatorMF/Urho3D/tree/SetModeTest
I'll be glad if someone with multi-monitor PC can test it out so I can PR.

So far I've only tested DX9 on Windows 10.

-------------------------

dertom | 2019-03-26 00:35:34 UTC | #12

Linux Ubuntu 18.04 opengl:
```
[ 59%] Building CXX object Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OpenGL/OGLShaderProgram.cpp.o
/home/ttrocha/_dev/ALWAYSDEL/urho3d/urho3d-setmode/Source/Urho3D/Graphics/OpenGL/OGLGraphics.cpp: In member function ‘bool Urho3D::Graphics::SetMode(int, int, bool, bool, bool, bool, bool, bool, int, int, int)’:
/home/ttrocha/_dev/ALWAYSDEL/urho3d/urho3d-setmode/Source/Urho3D/Graphics/OpenGL/OGLGraphics.cpp:291:114: error: ISO C++ forbids comparison between pointer and integer [-fpermissive]
         resizable == resizable_ && tripleBuffer == tripleBuffer_ && multiSample == multiSample_ && && monitor == monitor_ &&
                                                                                                                  ^~~~~~~~
/home/ttrocha/_dev/ALWAYSDEL/urho3d/urho3d-setmode/Source/Urho3D/Graphics/OpenGL/OGLGraphics.cpp:291:103: error: label ‘monitor’ used but not defined
         resizable == resizable_ && tripleBuffer == tripleBuffer_ && multiSample == multiSample_ && && monitor == monitor_ &&
                                                                                                       ^~~~~~~
Source/Urho3D/CMakeFiles/Urho3D.dir/build.make:2279: recipe for target 'Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OpenGL/OGLGraphics.cpp.o' failed
make[2]: *** [Source/Urho3D/CMakeFiles/Urho3D.dir/Graphics/OpenGL/OGLGraphics.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
CMakeFiles/Makefile2:1428: recipe for target 'Source/Urho3D/CMakeFiles/Urho3D.dir/all' failed
make[1]: *** [Source/Urho3D/CMakeFiles/Urho3D.dir/all] Error 2
Makefile:151: recipe for target 'all' failed
make: *** [all] Error 2
```

-------------------------

Pencheff | 2019-03-26 00:39:54 UTC | #13

There's a double "&&" I left there from copy-paste, can you remove one pair and try again, I'll fix it in my repo. Thank you very much.

-------------------------

Pencheff | 2019-03-26 01:56:17 UTC | #14

Fixed it and added more options. Needs testing on OpenGL and DirectX 11

-------------------------

Pencheff | 2019-03-26 21:22:09 UTC | #15

D3D9 seems to work fine with 2 monitors and different refresh rates (60 and 144Hz). Setting different rate-resolution combinations works. In D3D11 however, fullscreen mode works only with the same refresh rate as the desktop. This is fine with me, but I'm still not giving up on doing things the right way.

-------------------------

dertom | 2019-03-27 01:25:30 UTC | #16

Ok,...I finally found some time to test it. 
Setup: Linux/Ubuntu 18.04. Graphics: Nvidia GTX760 opengl

I write down some things as I test it. Not sure if all options are implemented,yet(or do you want it as issue on github?)

*  Monitors and their max resolution recoginzed correctly
*  In window-mode: apply any resolution resets always to the same (default) resolution
* trying to change the monitor in window-mode always stays on the default-monitor. Moving the window manually to the 2nd and applying this monitor in the settings also results in jumping back to the default-monitor!*  V-Sync works as expected,
*  resize-toggle works as expected
*  fps-limit works as expected
*  Borderless Window => Window with fullscreen resolution. Works as expected
*  Fullscreen: works with all selectable resolutions:
   * in Fullscreen. Clicking on other monitor => game gets minimized and recreates the window when selecting the programm in the taskbar. 
   * Changing the monitor in fullscreenmode works as expected, but
   * Changing the resolution on the right monitor to a resolution lower than the highest, switches to this resolution, BUT let you scroll right out of the window(not at the bottom) Seems like the horizontal resolution is kept and some kind of virtual display is available.
Before(red area visible):
![first|690x230,75%](upload://vcALl5xpzfJcnQe99xQJ2vwuLlq.png)  
Moving Cursor to most right position:
![second|690x230,75%](upload://yWhv302ZmJ9SSq8I5R2nphZiSh4.png) 

Leaving game while move to the most right virtual position(2nd image), keeps this state and you have to reset the resolution with system settings. Leaving the game in the situation like in the 1st image, resets the screen resolution right as before. 

The graphics-settings are doing what the should. Not sure how to check the hdr-switch,though

Ok,...I guess I'm through,...and running out of time. So I won't correct any typo ;) 

All in all, I love it. Really good job :+1:

-------------------------

Pencheff | 2019-03-27 01:55:49 UTC | #17

Thank you so much for that verbose testing @dertom.

-------------------------

