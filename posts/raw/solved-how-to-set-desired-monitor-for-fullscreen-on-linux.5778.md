wakko | 2020-12-05 15:12:17 UTC | #1

Issue resolved, see my last reply.
----------
Hello,
I am running a dual screen setup and for some reason the Linux build of my Urho3D fullscreen application always starts on the secondary screen. This happens since Ubuntu 18.04 (currently 19.10) with the native Nvidia drivers. Everything is fine on Windows.
I have found this topic but unfortunately none of the suggestions worked for me:
[Fullscreen Monitor Select](https://discourse.urho3d.io/t/fullscreen-monitor-select/2914)
Are there any updates on that?

-------------------------

weitjong | 2019-12-24 00:32:20 UTC | #2

Just wonder, does other Linux app started in fullscreen also exhibit this problem?

-------------------------

wakko | 2019-12-24 11:25:02 UTC | #3

I have tested some Steam games and a few native SDL/OpenGL games (e.g. Neverputt) which all start on the correct (i.e. primary) monitor.

-------------------------

weitjong | 2019-12-24 12:29:11 UTC | #4

It is a long shot but did you install "libxinerama-dev" package as one of the SDL2 (and hence also Urho3D) prerequisite? Our [Linux prebuilt binary](https://sourceforge.net/projects/urho3d/files/Urho3D/Snapshots/) from CI is built with "libxinerama-dev", so you can give the sample demo a quick try too to rule out whether missing "libxinerama-dev" is the root cause of your issue.

HTH.

-------------------------

wakko | 2020-01-20 19:24:49 UTC | #5

Thanks for the suggestion and sorry for the late reply but I somehow forgot about this thread over Christmas and winter holidays...
I've built Urho3D from source and the libxinerama-dev package was installed and enabled in cmake at build time.
The "Urho3DPlayer" indeed starts fullscreen on the primary screen. But I still couldn't find the runtime option to enable that on my program... :confused: 
I am using only C++ and no scripting.

-------------------------

weitjong | 2020-01-20 20:42:40 UTC | #6

I don’t have multiple monitor setup so take what I said with a grain of salt. I can see two things that could potentially be the cause. One, your build tree need to be regen after the new dep is installed on your host, or clear CMake cache and rerun CMake to reconfigure. Second, your program has requested a resolution that is better matched by your secondary monitor.

-------------------------

Pencheff | 2020-01-22 14:50:45 UTC | #7

I'm running my Urho3D based app mostly on Linux and fullscreen has always been an issue. It works fine on Windows with OpenGL, but always does weird things in Linux. I would suggest you try running your app in fullscreen borderless mode. 
Check this for a reference : https://github.com/PredatorMF/Urho3D/blob/SetModeTest/Source/Samples/54_GraphicsMode/GraphicsSettings.cpp

You can download this fork and build it yourself, I exposed most of the settings in an UI window in the 54_GraphicsMode sample.

-------------------------

wakko | 2020-01-22 18:50:46 UTC | #8

Thanks again for the suggestions. Both screens have the same native resolution and the cmake cache doesn't need to be cleared because nothing was changed. libxinerama-dev was already installed and enabled on my very first build of Urho3D.

@Pencheff: Thank you, too. My problem is not running the program in fullscreen which works fine already. It just starts on the wrong (secondary) screen which (as mentioned above) has the same resolution as the primary screen (1080p). I will look through your code to see if I can find something useful.

-------------------------

wakko | 2020-12-05 15:18:19 UTC | #9

Hi, just wanted to mention here that I could solve this with a fresh (K)Ubuntu install. 
Since then my application starts at the correct primary screen. This even works fine after swapping the monitors.
Not sure what was wrong with my previous >4 years old installation, but obviously there was a mix-up of the primary screen somewhere in the depths of the window manager/compositor.

-------------------------

urnenfeld | 2020-12-05 16:56:45 UTC | #10

Hello,

I have not dealt with this issue myself, but I am also having a dual screen setup, and the game always starts *on the left one*. 

I expected to arrange this with the [ParameterEngine](https://urho3d.github.io/documentation/HEAD/_main_loop.html), there is one called [EP_MONITOR](https://github.com/urho3d/Urho3D/blob/1151b8a2d6b4042eea6bfaa90931ee1068625fa3/Source/Urho3D/Engine/Engine.cpp#L878):

...In the base class of the examples [is used](https://github.com/urho3d/Urho3D/blob/1151b8a2d6b4042eea6bfaa90931ee1068625fa3/Source/Samples/Sample.inl#L60).

Is the actual problem that this parameter is not respected when it goes fullscreen?

-------------------------

