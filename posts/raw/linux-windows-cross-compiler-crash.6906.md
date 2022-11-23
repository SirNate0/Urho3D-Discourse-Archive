nickwebha | 2021-07-04 19:05:23 UTC | #1

I am cross-compiling from Linux for Windows using `x86_64-w64-mingw32-g++-posix` (version 9.3.0, Ubuntu 20.04). Everything compiles fine (Urho3D and my program) but crashes on `SendEvent()`. The thing is this problem is intermittent (I am calling `SendEvent()` multiple times in multiple places and it does not always crash in the same place).

In this example I am using it to change screens (go from the logo, to the main menu, to the game itself). Some times it just crashes right off the bat. Some times it shows the logo (first screen). Some times it shows the logo and the main menu. Some times (rarely) it works fine and gets all the way to the game itself without crashing.

There is no error message; The program just exits. I have tried compiling Urho3D with both DirectX and OpenGL with the same results.

I am compiling Urho3D like so:
`../script/cmake_mingw.sh . -D MINGW_PREFIX=/usr/bin/x86_64-w64-mingw32 -D URHO3D_NETWORK=0`

Neither the Linux nor Web versions using the same code base have this problem.

-------------------------

SirNate0 | 2021-07-05 00:21:12 UTC | #2

Run it in a debugger. That should help narrow down the cause of the problem. It sounds to me like you're probably using a deleted object or a resource that couldn't be found to send an event.

-------------------------

nickwebha | 2021-07-06 20:51:16 UTC | #3

Could you recommend a Windows debugger? Maybe something similar to *gdb*? After a Google search I tried *x64dbg* but I am not sure that is what I am looking for.

I am more of a Linux guy and have not used Windows since 98/2000. I think the last version of Visual Studio I used was 6. I use Windows 10 for games but strictly for playing games so I know little about it.

I tried running it from cmd. The same thing happens (with no error message). You would think, if there was a crash, there would be some kind of message, no?

-------------------------

SirNate0 | 2021-07-07 16:18:16 UTC | #4

Mingw has a gdb executable as well. You're cross compiler may not include it, for obvious reasons, but if you install mingw-w64 in Windows I think it should have it. Though I also use Linux generally and it's been a while since I tried debugging a Windows build, so maybe Google that before installing to double check.

Edit: If you want to try using WINE to debug it, it looks like it's possible to do that as well.
http://mingw-cross.sourceforge.net/cross_debug.html

-------------------------

