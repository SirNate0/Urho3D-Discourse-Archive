Zyie | 2018-01-09 03:34:47 UTC | #1

I've got my game to a point where its playable and would like to let some people i know play it.

So i was wondering how you go about releasing a game for PC?

Edit::

sorry Its late and i didnt word this correctly. However i was wondering how you make an exe that i can send to someone as use release mode in visual studio resulted in errors

-------------------------

spwork | 2018-01-09 03:21:54 UTC | #2

Steam can help you sell games. But it will take 30% of your profit, but it's the best choice for individual developers.

-------------------------

spwork | 2018-01-09 03:25:33 UTC | #3

I've been doing a game that can be sold recently with Urho3d. I'm curious about what your game is. Can I play it after the release?

-------------------------

Zyie | 2018-01-09 03:33:53 UTC | #4

I should probably clarify, I meant how do i make an exe that i can send to people. I tried using Release Mode in Visual Studio but it gave me a lot of errors.

-------------------------

spwork | 2018-01-09 03:37:22 UTC | #5

Well, you should first compile the urho3d Library in release mode, make sure that your linker uses urho3d.lib instead of urho3d_d.lib, which should be generated correctly.

-------------------------

Florastamine | 2018-01-09 03:50:36 UTC | #6

What I normally do is to build the engine without any flags that might be involved with debugging support and any subsystems that I have no need. For example, `-DCMAKE_BUILD_TYPE="Release"`, `-DURHO3D_PROFILING=0`, `-DURHO3D_NETWORK=0` and so on. I don't know specifically about VS, but you can try passing the arguments into the batch file, like so

`cmake_vs2017.bat -DCMAKE_BUILD_TYPE="Release" -DURHO3D_PROFILING=0 -DURHO3D_SAFE_LUA=0 ...`

And build the generated project again. Debug mode in VS is just a fancy name for putting the debug macros in your code (`NDEBUG`, for example), so you can also turn off the definition when invoking CMake (`-DNDEBUG=0`), and build the project without using the Release mode. Also you might be interested in the optimization flags, which can be passed to "EXTRA_CXXFLAGS" ([here](https://webcache.googleusercontent.com/search?q=cache:WFlJbVd3D7MJ:https://msdn.microsoft.com/en-us/library/k1ack8f1.aspx+). Example: `DEXTRA_CXXFLAGS="/O2"`

-------------------------

